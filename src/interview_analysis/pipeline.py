from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from .loader import (
    load_messages_csv,
    build_sessions_data,
    load_documents_from_folder,
    iter_documents_from_folder,
    iter_documents_with_metadata,
    DocumentWithMetadata,
    load_scraper_metadata
)
from .prompts import load_and_render
from .model_provider import create_provider, ModelConfig
from .citation import (
    CitationRegistry,
    expand_citations_to_links,
    generate_citation_appendix,
    finalize_report_citations,
    load_scraper_metadata as load_citation_metadata
)
from .token_tracker import TokenTracker


@dataclass
class RunConfig:
    mode: str  # hypothesis | initial | initial_auto | initial_part1 | initial_part2 | update | merge | pre_hypothesis_auto | pre_hypothesis_iterative
    model: str
    temperature: float = 0.0  # Map/Reduceフェーズ用（決定論的）
    comparison_temperature: float = 1.0  # Comparisonフェーズ用（創造的）
    max_output_tokens: int = 64000
    top_p: float = 0.95
    top_k: int = 40
    output_length_guidance: str = ""
    focus: str = ""  # 分析のフォーカス（主眼）  # 任意


def _call_model(prompt: str, cfg: RunConfig, step_name: str = "unknown") -> str:
    """
    モデル名から自動判定してプロバイダーを選択し、生成を実行
    
    プレフィックス:
      - gemini:model_name → Gemini
      - openrouter:model_name → OpenRouter
      - プレフィックスなし → Gemini
    """
    provider, actual_model = create_provider(cfg.model)
    model_config = ModelConfig(
        model=actual_model,
        temperature=cfg.temperature,
        max_output_tokens=cfg.max_output_tokens,
        top_p=cfg.top_p,
        top_k=cfg.top_k,
    )
    text, usage = provider.generate(prompt, model_config)
    
    TokenTracker.track(
        pipeline=cfg.mode,
        step=step_name,
        model=cfg.model,
        usage=usage
    )
    
    return text


# --- Token Estimation and Dynamic Batching ---

def estimate_tokens(text: str) -> int:
    """
    テキストのトークン数を推定
    
    日本語/英語混在テキストの場合、1 token ≈ 4 characters で概算
    """
    return max(1, len(text) // 4)


def calculate_dynamic_batch_size(
    session_contents: Dict[str, str],
    session_ids: List[str],
    prompt_template_tokens: int = 2000,
    max_input_tokens: int = 1_048_576,
    target_utilization: float = 0.8,
    min_batch_size: int = 5,
    max_batch_size: int = 100
) -> int:
    """
    トークン上限に基づいて動的にバッチサイズを計算
    
    Args:
        session_contents: セッションIDとコンテンツのマッピング
        session_ids: 処理対象のセッションIDリスト
        prompt_template_tokens: プロンプトテンプレートの予想トークン数
        max_input_tokens: モデルの入力トークン上限
        target_utilization: トークン上限の目標使用率 (0.0-1.0)
        min_batch_size: 最小バッチサイズ
        max_batch_size: 最大バッチサイズ
    
    Returns:
        最適なバッチサイズ
    """
    if not session_ids:
        return min_batch_size
    
    # 各セッションの平均トークン数を推定
    sample_size = min(50, len(session_ids))
    sample_ids = session_ids[:sample_size]
    total_tokens = sum(estimate_tokens(session_contents.get(sid, "")) for sid in sample_ids)
    avg_tokens_per_session = total_tokens / sample_size if sample_size > 0 else 500
    
    # ヘッダー（=== Comment ID: xxx ===\n\n）のオーバーヘッド
    header_overhead = 50  # tokens per comment
    
    # 目標トークン数を計算
    target_tokens = int(max_input_tokens * target_utilization) - prompt_template_tokens
    
    # バッチサイズを計算
    tokens_per_session = avg_tokens_per_session + header_overhead
    calculated_batch_size = int(target_tokens / tokens_per_session) if tokens_per_session > 0 else min_batch_size
    
    # 上下限でクリップ
    batch_size = max(min_batch_size, min(max_batch_size, calculated_batch_size))
    
    print(f"[Dynamic Batching] avg tokens/session: {avg_tokens_per_session:.0f}, "
          f"target: {target_tokens:,} tokens ({target_utilization*100:.0f}% of {max_input_tokens:,}), "
          f"batch size: {batch_size}", flush=True)
    
    return batch_size


def calculate_dynamic_merge_size(
    items: List[str],
    prompt_template_tokens: int = 2000,
    max_input_tokens: int = 1_048_576,
    target_utilization: float = 0.8,
    min_merge_size: int = 2,
    max_merge_size: int = 20
) -> int:
    """
    Tree Reduceのmerge_sizeをトークン上限に基づいて動的に計算
    
    Args:
        items: マージ対象のアイテム（YAMLレポート等）
        prompt_template_tokens: プロンプトテンプレートの予想トークン数
        max_input_tokens: モデルの入力トークン上限
        target_utilization: トークン上限の目標使用率 (0.0-1.0)
        min_merge_size: 最小マージサイズ
        max_merge_size: 最大マージサイズ
    
    Returns:
        最適なマージサイズ
    """
    if not items or len(items) <= 1:
        return min_merge_size
    
    # 各アイテムの平均トークン数を推定
    sample_size = min(10, len(items))
    sample_items = items[:sample_size]
    total_tokens = sum(estimate_tokens(item) for item in sample_items)
    avg_tokens_per_item = total_tokens / sample_size if sample_size > 0 else 1000
    
    # 目標トークン数を計算
    target_tokens = int(max_input_tokens * target_utilization) - prompt_template_tokens
    
    # マージサイズを計算（currentReport + newInfo の2つのコンテンツを渡すので2倍）
    # merge_size個のアイテムを1グループとして処理するが、順次マージなので
    # 最大でnewInfo分のトークンが増える
    calculated_merge_size = int(target_tokens / avg_tokens_per_item) if avg_tokens_per_item > 0 else min_merge_size
    
    # 上下限でクリップ
    merge_size = max(min_merge_size, min(max_merge_size, calculated_merge_size))
    
    print(f"[Dynamic Merge] avg tokens/item: {avg_tokens_per_item:.0f}, "
          f"target: {target_tokens:,} tokens ({target_utilization*100:.0f}% of {max_input_tokens:,}), "
          f"merge size: {merge_size}", flush=True)
    
    return merge_size


# --- YAML Parsing Helpers ---

import yaml
import re


def extract_yaml_from_response(response: str) -> Optional[Dict[str, Any]]:
    """
    LLMのレスポンスからYAMLブロックを抽出してパースする。
    
    期待フォーマット:
    ```yaml
    ...
    ```
    
    Returns:
        パース成功時はdict、失敗時はNone
    """
    # ```yaml ... ``` ブロックを探す
    yaml_pattern = r"```ya?ml\s*\n(.*?)```"
    matches = re.findall(yaml_pattern, response, re.DOTALL | re.IGNORECASE)
    
    if not matches:
        # フォールバック: 全体をYAMLとしてパースを試みる
        try:
            return yaml.safe_load(response)
        except yaml.YAMLError:
            return None
    
    # 最初のマッチをパース
    try:
        return yaml.safe_load(matches[0])
    except yaml.YAMLError as e:
        print(f"Warning: YAML parse error: {e}", flush=True)
        return None


def merge_prior_hypothesis_yamls(text: str) -> str:
    """
    テキストから複数のYAMLブロックを抽出し、統合された単一のYAML文字列を返す。
    
    複数のpre_hypothesis_iterativeレポート（審議会 + 国会など）を
    統合して単一の事前仮説として扱うための前処理。
    
    Args:
        text: 複数のYAMLブロックを含む可能性のあるテキスト
        
    Returns:
        統合されたYAML文字列（```yaml ... ``` 形式）
    """
    import re
    
    # YAMLブロックを全て抽出
    pattern = r"```yaml\s*(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)
    
    if not matches:
        # YAMLブロックがない場合はそのまま返す
        return text
    
    if len(matches) == 1:
        # 単一のYAMLブロックの場合はそのまま返す
        return text
    
    print(f"[Merge] Found {len(matches)} YAML blocks, merging into single prior hypothesis...", flush=True)
    
    # 複数のYAMLをパースしてマージ
    merged: Optional[Dict[str, Any]] = None
    
    for i, yaml_text in enumerate(matches):
        try:
            parsed = yaml.safe_load(yaml_text)
            if parsed:
                if merged is None:
                    merged = parsed
                else:
                    merged = merge_yaml_topics(merged, parsed)
                print(f"  [Merge] Block {i+1}/{len(matches)}: {len(parsed.get('topics', []))} topics", flush=True)
        except yaml.YAMLError as e:
            print(f"  [Merge] Block {i+1} parse error: {e}", flush=True)
            continue
    
    if merged is None:
        return text
    
    # 統合結果をYAML文字列に変換
    yaml_str = yaml.dump(merged, allow_unicode=True, default_flow_style=False, sort_keys=False)
    print(f"  [Merge] Result: {len(merged.get('topics', []))} total topics, {len(merged.get('metadata', {}).get('source_documents', []))} source docs", flush=True)
    
    return f"```yaml\n{yaml_str}```"


def dump_yaml_output(data: Dict[str, Any]) -> str:
    """
    辞書をYAML形式の文字列に変換（マークダウンコードブロック付き）
    """
    yaml_str = yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False)
    return f"```yaml\n{yaml_str}```"


def merge_yaml_topics(current: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, Any]:
    """
    2つのYAML構造をマージする（プログラム側での補助統合）
    
    Note: 主にLLMが統合を行うが、パース後の補助処理として使用可能
    """
    if not current:
        return new
    if not new:
        return current
    
    result = {
        "metadata": {
            "focus": current.get("metadata", {}).get("focus", new.get("metadata", {}).get("focus", "")),
            "source_documents": [],
            "generated_at": datetime.now().isoformat(),
            "document_summary": ""
        },
        "topics": []
    }
    
    # source_documents をマージ（重複排除）
    seen_filenames = set()
    doc_counter = 1
    for doc in current.get("metadata", {}).get("source_documents", []) + new.get("metadata", {}).get("source_documents", []):
        filename = doc.get("filename", "")
        if filename and filename not in seen_filenames:
            seen_filenames.add(filename)
            doc["id"] = f"doc_{doc_counter:03d}"
            result["metadata"]["source_documents"].append(doc)
            doc_counter += 1
    
    # topics をマージ（同じタイトルは統合）
    topic_map: Dict[str, Dict] = {}
    for topic in current.get("topics", []) + new.get("topics", []):
        title = topic.get("title", "")
        if title in topic_map:
            # 既存のtopicにevidence_chunksを追加
            existing = topic_map[title]
            existing["evidence_chunks"] = existing.get("evidence_chunks", []) + topic.get("evidence_chunks", [])
            # spectrumの更新（新しい方を優先）
            if topic.get("spectrum"):
                existing["spectrum"] = topic["spectrum"]
        else:
            topic_map[title] = topic.copy()
    
    # IDを振り直し
    for i, (title, topic) in enumerate(topic_map.items(), 1):
        topic["id"] = f"topic_{i:03d}"
        for j, chunk in enumerate(topic.get("evidence_chunks", []), 1):
            chunk["id"] = f"chunk_{j:03d}"
        result["topics"].append(topic)
    
    return result


def tree_reduce(
    items: List[str],
    reduce_fn,
    max_workers: int = 10,
    checkpoint=None,
    checkpoint_prefix: str = "reduce",
    merge_size: int = 5  # 一度にマージする数
) -> tuple:
    """
    ツリー型並列Reduce
    
    O(n) の逐次処理を O(log_k n) レベルの並列処理に変換。
    k = merge_size (デフォルト5)
    
    Args:
        items: 処理対象のリスト
        reduce_fn: 2つのアイテムを統合する関数 (item1, item2) -> merged
        max_workers: 並列ワーカー数
        checkpoint: チェックポイントオブジェクト（オプション）
        checkpoint_prefix: チェックポイントのプレフィックス
        merge_size: 一度にマージする数（デフォルト5）
    
    Returns:
        (result, stats) のタプル
        - result: 最終的に統合された1つの結果
        - stats: {"initial_count": N, "levels": [groups_per_level]}
    """
    from concurrent.futures import ThreadPoolExecutor
    import time
    
    # リトライロジックのラッパー（複数アイテムを順次マージ）
    def reduce_group_with_retry(args):
        index, group = args
        if len(group) == 1:
            return group[0]
        
        print(f"    [Group {index}] Processing {len(group)} items...", flush=True)
        import time
        start_t = time.time()
        
        MAX_RETRIES = 3
        # グループ内のアイテムを順次マージ
        result = group[0]
        for i in range(1, len(group)):
            item2 = group[i]
            if not item2:  # 空文字はスキップ
                continue
            
            last_error = None
            for attempt in range(MAX_RETRIES):
                try:
                    result = reduce_fn(result, item2)
                    break
                except Exception as e:
                    last_error = e
                    if attempt < MAX_RETRIES - 1:
                        wait_time = 2 ** attempt
                        print(f"    [Group {index} - Retry {attempt + 1}/{MAX_RETRIES}] Error: {e}. Waiting {wait_time}s...", flush=True)
                        time.sleep(wait_time)
                    else:
                        print(f"    [Group {index} - Skip] Failed after {MAX_RETRIES} attempts: {e}", flush=True)
                        # 失敗時は現在の結果を保持
        
        elapsed = time.time() - start_t
        print(f"    [Group {index}] Finished in {elapsed:.1f}s", flush=True)
        return result
    
    stats = {"initial_count": len(items), "levels": []}
    
    if not items:
        return "", stats
    
    if len(items) == 1:
        return items[0], stats
    
    current_level = items
    level_num = 0
    
    while len(current_level) > 1:
        level_num += 1
        groups = []
        
        # merge_size個ずつグループ化
        for i in range(0, len(current_level), merge_size):
            group = current_level[i:i + merge_size]
            groups.append((len(groups) + 1, group))  # インデックスを付与
        
        stats["levels"].append(len(groups))
        print(f"  Tree Reduce Level {level_num}: {len(groups)} groups (parallel, {merge_size}-way merge)...", flush=True)
        
        # 並列実行（リトライロジック付き）
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(reduce_group_with_retry, groups))
        
        # None をフィルタリング（API エラー時の対策）
        results = [r if r is not None else "" for r in results]
        
        current_level = results
        
        # チェックポイント保存（各レベル完了後）
        if checkpoint:
            checkpoint.save_part2_state(level_num * 1000, current_level[0] if len(current_level) == 1 else "\n---\n".join(current_level))
    
    return current_level[0], stats


def _build_metadata_header(cfg: RunConfig, prompt_template: str, session_count: int) -> str:
    """レポートの先頭に付与するメタ情報を生成"""
    now = datetime.now()
    lines = [
        "---",
        "# 実験メタ情報",
        f"- 実行日時: {now.strftime('%Y-%m-%d %H:%M:%S')}",
        f"- モード: {cfg.mode}",
        f"- モデル: {cfg.model}",
        f"- 温度: {cfg.temperature}",
        f"- max_output_tokens: {cfg.max_output_tokens}",
        f"- top_p: {cfg.top_p}",
        f"- top_k: {cfg.top_k}",
        f"- セッション数: {session_count}",
        "",
        "## 使用プロンプトテンプレート",
        "```",
        prompt_template,
        "```",
        "---",
        "",
    ]
    return "\n".join(lines)


def _build_process_metadata(
    pipeline_name: str,
    data_sources: list,
    steps: list,
    tree_stats: dict = None,
    focus: str = ""
) -> str:
    """処理メタデータセクションを生成"""
    from datetime import datetime
    
    lines = []
    lines.append("\n\n---\n")
    lines.append("# 処理メタデータ\n")
    
    # 分析フォーカス
    if focus:
        lines.append(f"**分析フォーカス**: {focus}\n")
    
    # データソース
    if data_sources:
        lines.append("## データソース\n")
        lines.append("| 種別 | パス | 件数 |")
        lines.append("|------|------|------|")
        for ds in data_sources:
            lines.append(f"| {ds['name']} | `{ds['path']}` | {ds['count']:,} {ds.get('unit', '件')} |")
        lines.append("")
    
    # 処理パイプライン
    lines.append(f"## 処理パイプライン: {pipeline_name}\n")
    
    for step in steps:
        lines.append(f"### {step['name']}")
        lines.append(f"- **フェーズ**: {step['phase']}")
        lines.append(f"- **入力**: {step['input']:,} → **出力**: {step['output']:,}")
        lines.append(f"- **モデル**: `{step['model']}`")
        if step.get('details'):
            lines.append(f"- **詳細**: {step['details']}")
        lines.append("")
    
    # ツリーReduce統計
    if tree_stats and tree_stats.get('levels'):
        lines.append("## ツリーReduce統計\n")
        lines.append(f"- 初期バッチ数: {tree_stats['initial_count']}")
        lines.append(f"- 並列レベル数: {len(tree_stats['levels'])}")
        level_str = " → ".join([f"L{i+1}:{n}ペア" for i, n in enumerate(tree_stats['levels'])])
        lines.append(f"- レベル詳細: {level_str}")
        lines.append("")
    
    lines.append(f"\n*生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
    
    return "\n".join(lines)


def _extract_prior_process_metadata(report: str) -> str:
    """
    事前仮説レポートから処理メタデータセクションを抽出
    
    Returns:
        見つかった場合はメタデータセクション、なければ空文字
    """
    # "# 処理メタデータ" セクションを探す
    marker = "# 処理メタデータ"
    if marker not in report:
        return ""
    
    # セクション開始位置
    start_idx = report.find(marker)
    
    # 次の "---" または "# 実験メタ情報" までを抽出
    end_markers = ["---\n# 実験メタ情報", "\n---\n# 実験"]
    end_idx = len(report)
    for em in end_markers:
        idx = report.find(em, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
    
    extracted = report[start_idx:end_idx].strip()
    
    # ヘッダーを "先行処理" として書き換え
    if extracted:
        extracted = extracted.replace("# 処理メタデータ", "## 先行処理メタデータ (事前仮説生成)")
    
    return extracted


def _load_prior_hypothesis(meta: Dict[str, Any]) -> str:
    """事前仮説ファイルを読み込む。ファイルが指定されていない場合は空文字を返す。"""
    prior_hypothesis = meta.get("priorHypothesis", "")
    prior_hypothesis_file = meta.get("priorHypothesisFile", "")
    
    if prior_hypothesis_file:
        file_path = Path(prior_hypothesis_file)
        if file_path.exists():
            prior_hypothesis = file_path.read_text(encoding="utf-8")
    
    return prior_hypothesis


def build_context(meta: Dict[str, Any], sessions_data: str, session_ids: List[str], output_length_guidance: str, reference_documents: str = "") -> Dict[str, Any]:
    ctx = {
        "interviewTitle": meta.get("interviewTitle", ""),
        "interviewDescription": meta.get("interviewDescription", ""),
        "interviewOverview": meta.get("interviewOverview", ""),
        "interviewThemes": meta.get("interviewThemes", ""),
        "interviewQuestions": meta.get("interviewQuestions", ""),
        "knowledgeContext": meta.get("knowledgeContext", ""),
        "priorHypothesis": _load_prior_hypothesis(meta),
        "outputLengthGuidance": output_length_guidance,
        "sessionCount": len(session_ids),
        "sessionsData": sessions_data,
        "referenceDocuments": reference_documents,
    }
    return ctx


def run_hypothesis(prompt_path: Path, meta: Dict[str, Any], df_path: Path, cfg: RunConfig) -> Dict[str, Any]:
    df = load_messages_csv(df_path)
    session_ids, sessions_data, _ = build_sessions_data(df)
    ctx = build_context(meta, sessions_data, session_ids, cfg.output_length_guidance)

    from .prompts import load_template
    prompt_template = load_template(prompt_path)
    prompt = load_and_render(prompt_path, ctx)
    output = _call_model(prompt, cfg, step_name="hypothesis")

    metadata_header = _build_metadata_header(cfg, prompt_template, len(session_ids))
    report_with_metadata = metadata_header + output
    return {"prompt": prompt, "report": report_with_metadata}


def run_initial(prompt_path: Path, meta: Dict[str, Any], df_path: Path, cfg: RunConfig) -> Dict[str, Any]:
    df = load_messages_csv(df_path)
    session_ids, sessions_data, _ = build_sessions_data(df)
    ctx = build_context(meta, sessions_data, session_ids, cfg.output_length_guidance)

    from .prompts import load_template
    prompt_template = load_template(prompt_path)
    prompt = load_and_render(prompt_path, ctx)
    output = _call_model(prompt, cfg, step_name="initial")

    metadata_header = _build_metadata_header(cfg, prompt_template, len(session_ids))
    report_with_metadata = metadata_header + output
    return {"prompt": prompt, "report": report_with_metadata}


def run_update(prompt_path: Path, meta: Dict[str, Any], df_path: Path, previous_report: str, cfg: RunConfig) -> Dict[str, Any]:
    df = load_messages_csv(df_path)
    session_ids, sessions_data, _ = build_sessions_data(df)
    ctx = build_context(meta, sessions_data, session_ids, cfg.output_length_guidance)
    ctx.update({
        "previousReport": previous_report,
        "newSessionCount": len(session_ids),
    })

    from .prompts import load_template
    prompt_template = load_template(prompt_path)
    prompt = load_and_render(prompt_path, ctx)
    output = _call_model(prompt, cfg, step_name="update")

    metadata_header = _build_metadata_header(cfg, prompt_template, len(session_ids))
    report_with_metadata = metadata_header + output
    return {"prompt": prompt, "report": report_with_metadata}


def run_merge(prompt_path: Path, meta: Dict[str, Any], batch_reports: List[str], cfg: RunConfig) -> Dict[str, Any]:
    ctx = {
        "interviewTitle": meta.get("interviewTitle", ""),
        "interviewDescription": meta.get("interviewDescription", ""),
        "interviewOverview": meta.get("interviewOverview", ""),
        "interviewThemes": meta.get("interviewThemes", ""),
        "interviewQuestions": meta.get("interviewQuestions", ""),
        "knowledgeContext": meta.get("knowledgeContext", ""),
        "priorHypothesis": _load_prior_hypothesis(meta),
        "outputLengthGuidance": cfg.output_length_guidance,
        "batchCount": len(batch_reports),
        "batchReports": "\n\n---\n\n".join(batch_reports),
    }

    from .prompts import load_template
    prompt_template = load_template(prompt_path)
    prompt = load_and_render(prompt_path, ctx)
    output = _call_model(prompt, cfg, step_name="merge")

    metadata_header = _build_metadata_header(cfg, prompt_template, len(batch_reports))
    report_with_metadata = metadata_header + output
    return {"prompt": prompt, "report": report_with_metadata}


def run_initial_part1(prompt_path: Path, meta: Dict[str, Any], df_path: Path, cfg: RunConfig) -> Dict[str, Any]:
    """第1部: 新しい切り口（事前仮説になかった論点）を生成"""
    df = load_messages_csv(df_path)
    session_ids, sessions_data, _ = build_sessions_data(df)
    ctx = build_context(meta, sessions_data, session_ids, cfg.output_length_guidance)

    from .prompts import load_template
    prompt_template = load_template(prompt_path)
    prompt = load_and_render(prompt_path, ctx)
    output = _call_model(prompt, cfg, step_name="initial_part1")

    metadata_header = _build_metadata_header(cfg, prompt_template, len(session_ids))
    report_with_metadata = metadata_header + output
    return {"prompt": prompt, "report": report_with_metadata}


def run_initial_part2(prompt_path: Path, meta: Dict[str, Any], df_path: Path, part1_report: str, cfg: RunConfig) -> Dict[str, Any]:
    """第2部: 事前仮説の検証とよくある質問を生成"""
    df = load_messages_csv(df_path)
    session_ids, sessions_data, _ = build_sessions_data(df)
    ctx = build_context(meta, sessions_data, session_ids, cfg.output_length_guidance)
    ctx.update({
        "part1Report": part1_report,
    })

    from .prompts import load_template
    prompt_template = load_template(prompt_path)
    prompt = load_and_render(prompt_path, ctx)
    output = _call_model(prompt, cfg, step_name="initial_part2")

    metadata_header = _build_metadata_header(cfg, prompt_template, len(session_ids))
    report_with_metadata = metadata_header + output
    return {"prompt": prompt, "report": report_with_metadata}


def _extract_body_from_report(report_with_metadata: str) -> str:
    """メタデータヘッダーを除去してレポート本文のみを抽出"""
    lines = report_with_metadata.split("\n")

    # "---" で囲まれたメタデータセクションを探して除去
    in_metadata = False
    metadata_end_index = 0

    for i, line in enumerate(lines):
        if line.strip() == "---":
            if not in_metadata:
                in_metadata = True
            else:
                # 2つ目の "---" が見つかった
                metadata_end_index = i + 1
                break

    # メタデータ以降の本文を返す（空行をスキップ）
    body_lines = lines[metadata_end_index:]
    while body_lines and not body_lines[0].strip():
        body_lines.pop(0)

    return "\n".join(body_lines)


def _build_combined_metadata(cfg: RunConfig, session_count: int, part1_prompt: str, part2_prompt: str) -> str:
    """統合レポート用のメタデータヘッダーを生成"""
    now = datetime.now()
    lines = [
        "---",
        "# 実験メタ情報",
        f"- 実行日時: {now.strftime('%Y-%m-%d %H:%M:%S')}",
        f"- モード: {cfg.mode} (2段階自動実行)",
        f"- モデル: {cfg.model}",
        f"- 温度: {cfg.temperature}",
        f"- max_output_tokens: {cfg.max_output_tokens}",
        f"- top_p: {cfg.top_p}",
        f"- top_k: {cfg.top_k}",
        f"- セッション数: {session_count}",
        "---",
        "",
    ]
    return "\n".join(lines)


def _build_combined_prompts_section(part1_prompt: str, part2_prompt: str) -> str:
    """統合レポート末尾のプロンプトセクションを生成"""
    lines = [
        "",
        "---",
        "",
        "## 使用プロンプト",
        "",
        "### Part 1 プロンプト（新規論点発見）",
        "",
        "```",
        part1_prompt,
        "```",
        "",
        "### Part 2 プロンプト（事前仮説検証）",
        "",
        "```",
        part2_prompt,
        "```",
    ]
    return "\n".join(lines)


def run_initial_auto(prompt_dir: Path, meta: Dict[str, Any], df_path: Path, cfg: RunConfig) -> Dict[str, Any]:
    """
    initial_auto: Part1とPart2を自動的に順次実行し、統合レポートを生成

    出力構造:
    - メタデータ
    - Part1本文（まとめ + 第1部）
    - Part2本文（第2部 + よくある質問）
    - プロンプト（Part1 + Part2）
    """
    # 共通データをロード
    df = load_messages_csv(df_path)
    session_ids, sessions_data, _ = build_sessions_data(df)

    # Part1を実行
    from .prompts import load_template
    part1_prompt_path = prompt_dir / "initial_part1.md"
    part1_prompt_template = load_template(part1_prompt_path)

    ctx1 = build_context(meta, sessions_data, session_ids, cfg.output_length_guidance)
    part1_prompt = load_and_render(part1_prompt_path, ctx1)
    part1_output = _call_model(part1_prompt, cfg, step_name="initial_auto_part1")

    # Part1の本文のみを抽出（メタデータなし）
    part1_body = part1_output

    # Part2を実行（Part1の本文全体を渡す）
    part2_prompt_path = prompt_dir / "initial_part2.md"
    part2_prompt_template = load_template(part2_prompt_path)

    ctx2 = build_context(meta, sessions_data, session_ids, cfg.output_length_guidance)
    ctx2.update({
        "part1Report": part1_body,
    })
    part2_prompt = load_and_render(part2_prompt_path, ctx2)
    part2_output = _call_model(part2_prompt, cfg, step_name="initial_auto_part2")

    # Part2の本文のみを抽出
    part2_body = part2_output

    # 統合レポートを構築
    metadata_header = _build_combined_metadata(cfg, len(session_ids), part1_prompt_template, part2_prompt_template)
    prompts_section = _build_combined_prompts_section(part1_prompt, part2_prompt)

    # 最終レポート: メタデータ + Part1本文 + Part2本文 + プロンプト
    combined_report = metadata_header + part1_body + "\n\n" + part2_body + prompts_section

    # プロンプトも統合（記録用）
    combined_prompt = f"=== Part 1 Prompt ===\n{part1_prompt}\n\n=== Part 2 Prompt ===\n{part2_prompt}"

    return {"prompt": combined_prompt, "report": combined_report}


def run_pre_hypothesis_iterative(prompt_dir: Path, meta: Dict[str, Any], source_path: Path, cfg: RunConfig, use_checkpoint: bool = True, source_type: str = "shingikai") -> Dict[str, Any]:
    """
    pre_hypothesis_iterative:
    1. (Map) 各ドキュメントに対して Part1 (論点抽出) を実行
    2. (Reduce) 抽出された論点群をバッチごとに Part2 (Q&A生成・更新) にかけて、最終的なQ&Aリストを作成

    チェックポイント機能により、途中再開が可能。
    Citation Registry機能により、出典情報を追跡可能。
    """
    if not source_path.is_dir():
        raise ValueError("pre_hypothesis_iterative requires a directory path for documents")

    from .prompts import load_template
    from .checkpoint import get_checkpoint
    import os

    # チェックポイント初期化
    checkpoint = get_checkpoint(source_path, "pre_hypothesis_iterative", cfg.focus) if use_checkpoint else None

    # --- Citation Registry 構築 ---
    # スクレイパーのメタデータを読み込み、Citation Registry を初期化
    scraper_metadata = load_scraper_metadata(source_path)
    citation_registry = CitationRegistry()

    # ファイル名→引用IDのマッピングを構築
    filename_to_cite_id: Dict[str, str] = {}

    # --- Phase 1: Map (Extract Points from each document) ---
    part1_prompt_path = prompt_dir / "pre_hypothesis_part1.md"
    part1_prompt_template = load_template(part1_prompt_path)

    # === 最適化：まずチェックポイントを確認し、Part 1 が完了していればPDF読み込みをスキップ ===
    part1_results = None
    documents = None  # 遅延初期化
    
    # ファイル数のみを高速に取得（PDFコンテンツは読み込まない）
    target_exts = ('.pdf', '.txt')
    pdf_files = sorted([f for f in os.listdir(source_path) if f.lower().endswith(target_exts)])
    num_files = len(pdf_files)
    
    # チェックポイントからPart 1（完全版）を復元
    if checkpoint and checkpoint.has_part1_checkpoint():
        part1_results = checkpoint.load_part1()
        # キャッシュがあれば使用（ファイル数の完全一致は不要）
        if part1_results:
            print(f"[Checkpoint] Using cached Part 1 results ({len(part1_results)} items, directory has {num_files} files) - Skipping PDF loading", flush=True)
        else:
            print(f"[Checkpoint] Part 1 cache empty. Checking partials.", flush=True)
            part1_results = None

    # 事前にpartialを読み込み（重複読み込み防止）
    partial = checkpoint.load_partial_map_results() if checkpoint else {}
    
    # インクリメンタルチェックポイントの確認
    if part1_results is None and checkpoint:
        if len(partial) == num_files:
             part1_results = []
             # index順に並べ替え
             sorted_indices = sorted(partial.keys())
             for idx in sorted_indices:
                 part1_results.append(partial[idx])
             
             print(f"[Checkpoint] Consolidated {len(part1_results)} items from incremental checkpoints", flush=True)
             checkpoint.save_part1(part1_results)

    # Part 1 結果がある場合：Citation Registryをファイル名リストから構築（PDFコンテンツ不要）
    if part1_results is not None:
        # スクレイパーメタデータからCitation Registryを構築（PDF読み込み不要）
        for filename in pdf_files:
            metadata = scraper_metadata.get(filename, {})
            cite_id = citation_registry.add_document(
                file=filename,
                url=metadata.get('url', ''),
                page_title=metadata.get('page_title', ''),
                link_text=metadata.get('link_text', '')
            )
            filename_to_cite_id[filename] = cite_id

    if part1_results is None:
        # Part 1を実行 - この場合のみPDFを読み込む
        print(f"[Map Phase] Loading {num_files} PDF documents...", flush=True)
        documents = list(iter_documents_with_metadata(source_path))
        
        # Citation Registry にドキュメントを登録
        for doc in documents:
            cite_id = citation_registry.add_document(
                file=doc.filename,
                url=doc.url,
                page_title=doc.page_title,
                link_text=doc.link_text
            )
            filename_to_cite_id[doc.filename] = cite_id
        
        from concurrent.futures import ThreadPoolExecutor
        import threading
        lock = threading.Lock()

        # 完了済みアイテムをロード（上で読み込み済みのpartialを再利用）
        partial_results = partial
        
        if partial_results:
             print(f"[Checkpoint] Resuming Part 1: {len(partial_results)} items already completed, {len(documents) - len(partial_results)} remaining", flush=True)

        def process_document_with_checkpoint(args):
            idx, doc = args
            filename = doc.filename
            
            # 既に完了していれば返す
            if idx in partial_results:
                return partial_results[idx]

            print(f"Processing Part 1 for: {filename}...", flush=True)
            
            # 遅延読み込み: このファイルのPDFコンテンツをここで取得
            content = doc.to_enriched_content()
            
            ctx1 = build_context(meta, "", [], cfg.output_length_guidance, reference_documents=f"=== File: {filename} ===\n\n{content}")
            ctx1["focus"] = cfg.focus
            ctx1["sourceType"] = source_type
            part1_prompt = load_and_render(part1_prompt_path, ctx1)
            
            # リトライロジック: 最大3回試行、失敗したらスキップ
            MAX_RETRIES = 3
            last_error = None
            for attempt in range(MAX_RETRIES):
                try:
                    output = _call_model(part1_prompt, cfg, step_name="pre_hypothesis_part1")
                    # 成功したらチェックポイント保存
                    if checkpoint:
                        with lock:
                            checkpoint.save_map_batch(idx, filename, output)
                    return (filename, output)
                except Exception as e:
                    last_error = e
                    if attempt < MAX_RETRIES - 1:
                        import time
                        wait_time = 2 ** attempt  # 指数バックオフ: 1, 2, 4秒
                        print(f"[Retry {attempt + 1}/{MAX_RETRIES}] Error processing {filename}: {e}. Waiting {wait_time}s...", flush=True)
                        time.sleep(wait_time)
                    else:
                        print(f"[Skip] Failed to process {filename} after {MAX_RETRIES} attempts: {e}", flush=True)
            
            # 3回失敗したらスキップ（空の結果を返す）
            skip_output = f"[SKIPPED: {filename} - Error: {last_error}]"
            if checkpoint:
                with lock:
                    checkpoint.save_map_batch(idx, filename, skip_output)
            return (filename, skip_output)

        with ThreadPoolExecutor(max_workers=3) as executor:  # 503エラー防止のため並列数を削減
            part1_results = list(executor.map(process_document_with_checkpoint, enumerate(documents)))

        # チェックポイント保存 (Complete)
        if checkpoint:
            checkpoint.save_part1(part1_results)

    if not part1_results:
        return {"prompt": "", "report": "No documents found or processed."}

    # Part 1レポート（出力のみ）のリストを作成
    part1_reports = [output for _, output in part1_results]

    # --- Phase 2: Reduce (Tree-Based Parallel) ---
    part2_prompt_path = prompt_dir / "pre_hypothesis_part2_iterative.md"
    part2_prompt_template = load_template(part2_prompt_path)
    
    # 動的バッチサイズ計算（トークン制限最適化）
    # Gemini Flash: 1M input, 65K output
    MAX_INPUT_TOKENS = 1_000_000
    TARGET_TOKENS_PER_BATCH = 100_000  # 安全マージン込みで10万トークン/バッチ
    
    # 平均トークン数を推定（日本語: 約1.5文字/トークン）
    total_chars = sum(len(r) for r in part1_reports)
    avg_chars_per_report = total_chars / len(part1_reports) if part1_reports else 1000
    avg_tokens_per_report = avg_chars_per_report / 1.5  # 日本語概算
    
    # 最適バッチサイズを計算
    optimal_batch_size = max(1, int(TARGET_TOKENS_PER_BATCH / avg_tokens_per_report))
    optimal_batch_size = min(optimal_batch_size, 10)  # 最大10 (latency対策)
    optimal_batch_size = max(optimal_batch_size, 3)   # 最小3
    
    # マージサイズも動的調整（バッチが大きければマージ数を減らす）
    optimal_merge_size = max(2, min(5, 50000 // int(avg_tokens_per_report * optimal_batch_size)))
    
    print(f"[Token Optimization] Avg tokens/report: {int(avg_tokens_per_report)}, batch_size: {optimal_batch_size}, merge_size: {optimal_merge_size}", flush=True)
    
    initial_batches = []
    for i in range(0, len(part1_reports), optimal_batch_size):
        batch = part1_reports[i:i + optimal_batch_size]
        initial_batches.append("\n\n---\n\n".join(batch))
    
    # チェックポイントからPart 2途中経過を復元（リジューム機能）
    if checkpoint:
        part2_data = checkpoint.load_part2_state()
        if part2_data:
            _, content = part2_data
            # NOTE: tree_reduceは結果を "\n---\n" で結合して保存している
            initial_batches = content.split("\n---\n")
            print(f"[Checkpoint] Resuming Part 2 from last saved state: {len(initial_batches)} items", flush=True)

    print(f"Starting Tree Reduce: {len(initial_batches)} initial batches", flush=True)
    
    # ツリー型Reduce用の統合関数を定義
    def reduce_pair(item1: str, item2: str) -> str:
        """2つのQ&A/レポートを統合"""
        if not item2:  # 奇数の場合
            return item1
        
        ctx2 = build_context(meta, "", [], cfg.output_length_guidance)
        ctx2.update({
            "currentQA": item1,
            "newInfo": item2,
            "focus": cfg.focus,
            "sourceType": source_type
        })
        
        prompt = load_and_render(part2_prompt_path, ctx2)
        return _call_model(prompt, cfg, step_name="pre_hypothesis_reduce")
    
    # ツリー型並列Reduceを実行
    import time
    reduce_start = time.time()
    final_qa, reduce_stats = tree_reduce(initial_batches, reduce_pair, max_workers=3, checkpoint=checkpoint, merge_size=optimal_merge_size)
    reduce_time = time.time() - reduce_start
    
    # 最終プロンプトを記録（代表としてラスト生成時のものを使用）
    ctx_final = build_context(meta, "", [], cfg.output_length_guidance)
    ctx_final.update({"currentQA": "(accumulated)", "newInfo": "(merged)", "focus": cfg.focus, "sourceType": source_type})
    last_part2_prompt = load_and_render(part2_prompt_path, ctx_final)

    # --- Final Report Construction ---
    metadata_header = _build_combined_metadata(cfg, len(part1_reports), part1_prompt_template, part2_prompt_template)

    prompts_section = _build_combined_prompts_section(
        part1_prompt_template,
        last_part2_prompt
    )

    # 処理メタデータを生成
    process_metadata = _build_process_metadata(
        pipeline_name="事前仮説生成 (pre_hypothesis_iterative)",
        data_sources=[
            {"name": "審議会資料", "path": str(source_path), "count": len(part1_reports), "unit": "ファイル"}
        ],
        steps=[
            {
                "name": "Part 1 (Map)",
                "phase": "論点抽出",
                "input": len(part1_reports),
                "output": len(part1_reports),
                "model": cfg.model,
                "details": "並列10ワーカー"
            },
            {
                "name": "Part 2 (Tree Reduce)",
                "phase": "Q&A統合",
                "input": len(initial_batches),
                "output": 1,
                "model": cfg.model,
                "details": f"{len(reduce_stats.get('levels', []))}レベル並列"
            }
        ],
        tree_stats=reduce_stats,
        focus=cfg.focus
    )

    # Citation Registry: 出典一覧を生成（実際に引用されている出典のみ）
    citation_appendix = generate_citation_appendix(citation_registry, report_text=final_qa)

    # --- Token Usage Statistics ---
    from .token_tracker import TokenTracker
    token_stats = TokenTracker.get_summary()
    
    token_stats_md = "\n\n# Token Usage Statistics\n\n| Process / Step | Model | Input Tokens | Output Tokens | Est. Cost (USD) |\n| :--- | :--- | ---: | ---: | ---: |\n"
    
    total_input = 0
    total_output = 0
    total_cost = 0.0
    
    for key in sorted(token_stats.keys()):
        stats = token_stats[key]
        model_name = stats.get("model", "unknown")
        cost = stats.get("cost", 0.0)
        
        token_stats_md += f"| {key} | {model_name} | {stats['input_tokens']:,} | {stats['output_tokens']:,} | ${cost:,.2f} |\n"
        
        total_input += stats.get('input_tokens', 0)
        total_output += stats.get('output_tokens', 0)
        total_cost += cost
    
    token_stats_md += f"| **TOTAL** | | **{total_input:,}** | **{total_output:,}** | **${total_cost:,.2f}** |\n"

    # Final Report Construction - メタ情報は最後に配置（読者はコンテンツを先に見たい）
    final_report = "# 最終成果物 (Q&Aリスト)\n\n" + final_qa + "\n\n---\n\n" + citation_appendix + token_stats_md + "\n\n" + process_metadata + "\n\n" + metadata_header

    # Part 1 Log Construction
    part1_log_content = "# Part 1 Outputs (Individual Document Analysis)\n\n"
    for filename, report in part1_results:
        part1_log_content += f"## File: {filename}\n\n{report}\n\n---\n\n"

    # 完了後、チェックポイントをクリア
    if checkpoint:
        checkpoint.clear()

    return {
        "prompt": last_part2_prompt,
        "report": final_report,
        "part1_log": part1_log_content,
        "citation_registry": citation_registry,
        "filename_to_cite_id": filename_to_cite_id
    }


def run_pubcom_analysis(prompt_dir: Path, meta: Dict[str, Any], csv_path: Path, previous_report: str, cfg: RunConfig, use_checkpoint: bool = True, comparison_model: Optional[str] = None, prior_citation_registry: Optional[CitationRegistry] = None, max_map_batches: Optional[int] = None, prior_token_stats: Optional[Dict] = None) -> Dict[str, Any]:
    """
    pubcom_analysis:
    1. (Map) パブコメCSVの各コメントに対して個別分析を実行 (pubcom_map.md)
    2. (Reduce) 個別分析結果をまとめて統合レポートを作成 (pubcom_reduce.md)
    3. (Compare) 事前仮説(previous_report)と統合レポートを比較 (pubcom_comparison.md)

    Args:
        comparison_model: Comparisonフェーズで使用するモデル（指定なしでcfg.modelを使用）
        prior_citation_registry: 事前仮説生成時のCitation Registry（URL情報の引き継ぎ用）
        prior_token_stats: 事前仮説等、前段の処理でのトークン使用統計（レポート統合用）

    チェックポイント機能により、途中再開が可能。
    Citation Registry機能により、出典情報を追跡可能。
    """
    from .prompts import load_template
    from concurrent.futures import ThreadPoolExecutor
    from collections import defaultdict
    from .checkpoint import get_checkpoint

    # チェックポイント初期化
    checkpoint = get_checkpoint(csv_path, "pubcom_analysis", cfg.focus) if use_checkpoint else None

    # --- Citation Registry 構築 ---
    # 事前仮説からの引用レジストリを引き継ぎ（存在する場合）
    if prior_citation_registry:
        citation_registry = CitationRegistry()
        # 事前仮説のレジストリをコピー
        citation_registry._doc_counter = prior_citation_registry._doc_counter
        for cite_id, citation in prior_citation_registry.citations.items():
            citation_registry.citations[cite_id] = citation
    else:
        citation_registry = CitationRegistry()

    # パブコメID→引用IDのマッピング
    pubcom_to_cite_id: Dict[str, str] = {}

    # --- Phase 1.1: Map (Individual Analysis) ---
    df = load_messages_csv(csv_path)

    # session_id ごとにコンテンツをまとめる
    session_dict = defaultdict(list)
    for row in df:
        sid = row.get("session_id", "unknown")
        msg = row.get("message") or row.get("content") or row.get("text") or ""
        session_dict[sid].append(msg)

    session_contents = {sid: "\n".join(msgs) for sid, msgs in session_dict.items()}
    session_ids = list(session_contents.keys())

    # パブコメをCitation Registryに登録
    for sid in session_ids:
        cite_id = citation_registry.add_pubcom(comment_id=sid)
        pubcom_to_cite_id[sid] = cite_id
    
    # 動的バッチサイズ計算（トークン上限の80%を目標）
    MAP_BATCH_SIZE = calculate_dynamic_batch_size(
        session_contents=session_contents,
        session_ids=session_ids,
        prompt_template_tokens=2000,
        max_input_tokens=1_048_576,
        target_utilization=0.8
    )
    session_batches = [session_ids[i:i + MAP_BATCH_SIZE] for i in range(0, len(session_ids), MAP_BATCH_SIZE)]
    
    map_prompt_path = prompt_dir / "pubcom_map.md"
    
    # チェックポイントからMap結果を復元
    map_results = None
    if checkpoint and checkpoint.has_part1_checkpoint():
        map_results = checkpoint.load_part1()
        if map_results and len(map_results) == len(session_batches):
            print(f"[Checkpoint] Using cached Map results ({len(map_results)} batches)", flush=True)
        else:
            print(f"[Checkpoint] Map cache invalid. Re-running.", flush=True)
            map_results = None
    
    # 全バッチ完了していない場合、インクリメンタルチェックポイントを確認
    if map_results is None and checkpoint:
        consolidated = checkpoint.consolidate_map_batches(len(session_batches))
        if consolidated:
            map_results = consolidated
            print(f"[Checkpoint] Consolidated {len(map_results)} Map batches from incremental checkpoints", flush=True)
            # Part 1形式で保存（次回高速化のため）
            checkpoint.save_part1(map_results)
    
    if map_results is None:
        import threading
        lock = threading.Lock()
        
        # 完了済みバッチを取得
        completed_batches = checkpoint.load_partial_map_results() if checkpoint else {}
        remaining_count = len(session_batches) - len(completed_batches)
        if completed_batches:
            print(f"[Checkpoint] Resuming: {len(completed_batches)} batches already completed, {remaining_count} remaining", flush=True)
        
        def process_map_batch_with_checkpoint(args):
            idx, batch_ids = args
            
            # 既に完了していればスキップ
            if idx in completed_batches:
                return (completed_batches[idx][0], completed_batches[idx][1])
            
            combined_content = ""
            for sid in batch_ids:
                content = session_contents[sid]
                combined_content += f"=== Comment ID: {sid} ===\n{content}\n\n"
                
            print(f"Processing Pubcom Map Batch {idx+1}/{len(session_batches)} ({len(batch_ids)} comments)...", flush=True)
            
            ctx1 = build_context(meta, "", [], cfg.output_length_guidance, reference_documents=combined_content)
            ctx1["focus"] = cfg.focus
            prompt = load_and_render(map_prompt_path, ctx1)
            
            # リトライロジック: 429エラー時は待機して再試行
            import time
            MAX_RETRIES = 3
            for attempt in range(MAX_RETRIES):
                try:
                    output = _call_model(prompt, cfg, step_name="pubcom_map")
                    break  # 成功
                except Exception as e:
                    if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                        wait_time = 5 * (2 ** attempt)  # 5, 10, 20秒
                        print(f"[Retry {attempt+1}/{MAX_RETRIES}] Rate limited. Waiting {wait_time}s...", flush=True)
                        time.sleep(wait_time)
                        if attempt == MAX_RETRIES - 1:
                            raise  # 最終試行でも失敗なら再送出
                    else:
                        raise  # 429以外のエラーはそのまま送出

            batch_id_str = str(batch_ids)
            
            # チェックポイント保存（スレッドセーフ）
            if checkpoint:
                with lock:
                    checkpoint.save_map_batch(idx, batch_id_str, output)
            
            return (batch_id_str, output)

        # max_map_batches が指定されている場合、処理対象を制限
        batches_to_process = list(enumerate(session_batches))
        if max_map_batches is not None:
            # 未完了バッチのみをカウント
            remaining_batches = [(idx, batch) for idx, batch in batches_to_process if idx not in completed_batches]
            if len(remaining_batches) > max_map_batches:
                print(f"[Batch Limit] Processing {max_map_batches} batches (of {len(remaining_batches)} remaining)", flush=True)
                batches_to_process = [(idx, batch) for idx, batch in batches_to_process if idx in completed_batches]  # 完了済み
                batches_to_process += remaining_batches[:max_map_batches]  # + 新規処理分

        with ThreadPoolExecutor(max_workers=3) as executor:  # 並列処理
            map_results = list(executor.map(process_map_batch_with_checkpoint, batches_to_process))
        
        # 部分完了チェック
        if max_map_batches is not None:
            completed_after = checkpoint.load_partial_map_results() if checkpoint else {}
            if len(completed_after) < len(session_batches):
                print(f"[Batch Limit] Partial completion: {len(completed_after)}/{len(session_batches)} batches done. Run again to continue.", flush=True)
                return {"prompt": "", "report": f"Partial Map: {len(completed_after)}/{len(session_batches)} batches completed. Run again to continue."}
        
        if checkpoint:
            checkpoint.save_part1(map_results)
    
    map_reports = [output for _, output in map_results if output is not None]
    
    # ログ構築
    part1_log_content = "# Pubcom Phase 1 Outputs (Batched Analysis)\n\n"
    for i, (batch_id_str, output_text) in enumerate(map_results):
        part1_log_content += f"## Batch {i+1}\n\n### Analysis\n{output_text}\n\n---\n\n"
    
    if not map_reports:
        return {"prompt": "", "report": "No comments processed."}

    # --- Phase 1.2: Reduce (Tree-Based Parallel) ---
    reduce_prompt_path = prompt_dir / "pubcom_reduce.md"
    
    # Map結果を初期バッチとして使用（3つずつグループ化）
    INITIAL_BATCH_SIZE = 3
    initial_batches = []
    for i in range(0, len(map_reports), INITIAL_BATCH_SIZE):
        batch = map_reports[i:i + INITIAL_BATCH_SIZE]
        initial_batches.append("\n\n---\n\n".join(batch))
    
    print(f"Starting Pubcom Tree Reduce: {len(initial_batches)} initial batches", flush=True)
    
    # ツリー型Reduce用の統合関数を定義
    def reduce_pair(item1: str, item2: str) -> str:
        """2つのレポートを統合"""
        if not item2:
            return item1
        
        ctx2 = build_context(meta, "", [], cfg.output_length_guidance)
        ctx2.update({
            "currentReport": item1,
            "newInfo": item2,
            "focus": cfg.focus
        })
        
        prompt = load_and_render(reduce_prompt_path, ctx2)
        return _call_model(prompt, cfg, step_name="pubcom_reduce")
    
    # 動的マージサイズ計算（トークン上限の80%を目標）
    dynamic_merge_size = calculate_dynamic_merge_size(
        items=initial_batches,
        prompt_template_tokens=2000,
        max_input_tokens=1_048_576,
        target_utilization=0.8,
        max_merge_size=5  # 安全のため上限を抑制
    )
    
    # ツリー型並列Reduceを実行
    pubcom_consolidated_report, reduce_stats = tree_reduce(initial_batches, reduce_pair, max_workers=10, checkpoint=checkpoint, merge_size=dynamic_merge_size)

    # --- Phase 2: Compare (Synthesis) ---
    # 比較用モデルが指定されていれば使用
    compare_model_name = comparison_model if comparison_model else cfg.model
    print(f"Processing Pubcom Comparison (model: {compare_model_name})...", flush=True)
    compare_prompt_path = prompt_dir / "pubcom_comparison.md"
    
    # 複数のYAMLブロックがある場合は統合（1A+1B など）
    merged_prior_hypothesis = merge_prior_hypothesis_yamls(previous_report)
    
    ctx3 = build_context(meta, "", [], cfg.output_length_guidance)
    ctx3.update({
        "priorHypothesis": merged_prior_hypothesis,
        "pubcomReport": pubcom_consolidated_report,
        "focus": cfg.focus
    })
    
    compare_prompt = load_and_render(compare_prompt_path, ctx3)
    
    # 比較用の設定を作成（モデルと温度を変更）
    compare_cfg = RunConfig(
        mode=cfg.mode,
        model=compare_model_name,
        temperature=cfg.comparison_temperature,  # 比較フェーズ用の温度を使用
        comparison_temperature=cfg.comparison_temperature,
        max_output_tokens=cfg.max_output_tokens,
        top_p=cfg.top_p,
        top_k=cfg.top_k,
        output_length_guidance=cfg.output_length_guidance,
        focus=cfg.focus
    )
    final_insight = _call_model(compare_prompt, compare_cfg, step_name="pubcom_compare")

    # 処理メタデータを生成
    process_metadata = _build_process_metadata(
        pipeline_name="パブリックコメント分析 (pubcom_analysis)",
        data_sources=[
            {"name": "パブリックコメント", "path": str(csv_path), "count": len(session_ids), "unit": "コメント"}
        ],
        steps=[
            {
                "name": "Map (コメント分析)",
                "phase": "個別分析",
                "input": len(session_ids),
                "output": len(map_reports),
                "model": cfg.model,
                "details": f"{len(session_batches)}バッチ (並列5ワーカー)"
            },
            {
                "name": "Tree Reduce (統合)",
                "phase": "レポート統合",
                "input": len(initial_batches),
                "output": 1,
                "model": cfg.model,
                "details": f"{len(reduce_stats.get('levels', []))}レベル並列"
            },
            {
                "name": "Compare (比較分析)",
                "phase": "仮説との比較",
                "input": 2,
                "output": 1,
                "model": compare_model_name,
                "details": "事前仮説 + パブコメ統合 → 最終レポート"
            }
        ],
        tree_stats=reduce_stats,
        focus=cfg.focus
    )

    # Final Report Construction - メタ情報は最後に配置（読者はコンテンツを先に見たい）
    metadata_header = _build_combined_metadata(compare_cfg, len(session_ids), "Pubcom Analysis", "Comparison")

    # 事前仮説レポートからメタデータを抽出
    prior_metadata = _extract_prior_process_metadata(previous_report)

    # Combined Metadata
    combined_metadata = process_metadata
    if prior_metadata:
        combined_metadata = combined_metadata + "\n\n" + prior_metadata

    # Citation Registry: 出典一覧を生成 & リンク置換（実際に引用されている出典のみ）
    # previous_report (prior report or merged hypothesis) contains the source mapping
    final_report_content = finalize_report_citations(
        report_text=final_insight,
        citation_registries=[citation_registry],
        merged_hypothesis_content=previous_report
    )

    # --- Token Usage Statistics ---
    from .token_tracker import TokenTracker
    token_stats = TokenTracker.get_summary()
    

            
    # Merge prior token stats if provided
    if prior_token_stats:
        for key, stats in prior_token_stats.items():
            if key not in token_stats:
                token_stats[key] = stats
            else:
                # Assuming distinct keys like 'pre_hypothesis/...' vs 'pubcom_analysis/...'
                # If keys collide, we sum them
                token_stats[key]["input_tokens"] += stats.get("input_tokens", 0)
                token_stats[key]["output_tokens"] += stats.get("output_tokens", 0)
                token_stats[key]["total_tokens"] += stats.get("total_tokens", 0)
                token_stats[key]["cost"] += stats.get("cost", 0.0)

    token_stats_md = "\n\n# Token Usage Statistics\n\n| Process / Step | Model | Input Tokens | Output Tokens | Est. Cost (USD) |\n| :--- | :--- | ---: | ---: | ---: |\n"
    
    # Sort for consistent order
    total_input = 0
    total_output = 0
    total_cost = 0.0
    
    for key in sorted(token_stats.keys()):
        stats = token_stats[key]
        model_name = stats.get("model", "unknown")
        cost = stats.get("cost", 0.0)
        
        token_stats_md += f"| {key} | {model_name} | {stats['input_tokens']:,} | {stats['output_tokens']:,} | ${cost:,.2f} |\n"
        
        total_input += stats.get('input_tokens', 0)
        total_output += stats.get('output_tokens', 0)
        total_cost += cost
    
    token_stats_md += f"| **TOTAL** | | **{total_input:,}** | **{total_output:,}** | **${total_cost:,.2f}** |\n"

    # 最終的な構成: Insight -> (Appendix) Citation -> Combined Metadata (Token Stats含む)
    # finalize_report_citations returns text + appendix
    final_report = final_report_content + "\n\n" + token_stats_md + "\n\n" + combined_metadata + "\n\n" + metadata_header

    # 完了後、チェックポイントをクリア
    if checkpoint:
        checkpoint.clear()

    return {
        "prompt": compare_prompt,
        "report": final_report,
        "part1_log": part1_log_content,
        "pubcom_consolidated_report": pubcom_consolidated_report,
        "citation_registry": citation_registry,
        "pubcom_to_cite_id": pubcom_to_cite_id
    }


def run_pubcom_aggregate(prompt_dir: Path, meta: Dict[str, Any], csv_path: Path, cfg: RunConfig, use_checkpoint: bool = True, max_map_batches: Optional[int] = None) -> Dict[str, Any]:
    """
    pubcom_aggregate: パブコメ集約のみ（Map + Reduce）
    
    1. (Map) パブコメCSVの各コメントに対して個別分析を実行 (pubcom_map.md)
    2. (Reduce) 個別分析結果をまとめて統合レポートを作成 (pubcom_reduce.md)
    
    出力: pubcom_report.md（再利用可能なYAML形式の集約レポート）
    """
    from .prompts import load_template
    from concurrent.futures import ThreadPoolExecutor
    from collections import defaultdict
    from .checkpoint import get_checkpoint

    # チェックポイント初期化
    checkpoint = get_checkpoint(csv_path, "pubcom_aggregate", cfg.focus) if use_checkpoint else None

    # Citation Registry
    citation_registry = CitationRegistry()
    pubcom_to_cite_id: Dict[str, str] = {}

    # --- Phase 1: Map (Individual Analysis) ---
    df = load_messages_csv(csv_path)

    # session_id ごとにコンテンツをまとめる
    session_dict = defaultdict(list)
    for row in df:
        sid = row.get("session_id", "unknown")
        msg = row.get("message") or row.get("content") or row.get("text") or ""
        session_dict[sid].append(msg)

    session_contents = {sid: "\n".join(msgs) for sid, msgs in session_dict.items()}
    session_ids = list(session_contents.keys())

    # パブコメをCitation Registryに登録
    for sid in session_ids:
        cite_id = citation_registry.add_pubcom(comment_id=sid)
        pubcom_to_cite_id[sid] = cite_id
    
    # 動的バッチサイズ計算（トークン上限の80%を目標）
    MAP_BATCH_SIZE = calculate_dynamic_batch_size(
        session_contents=session_contents,
        session_ids=session_ids,
        prompt_template_tokens=2000,
        max_input_tokens=1_048_576,
        target_utilization=0.8
    )
    session_batches = [session_ids[i:i + MAP_BATCH_SIZE] for i in range(0, len(session_ids), MAP_BATCH_SIZE)]
    
    map_prompt_path = prompt_dir / "pubcom_map.md"
    
    # チェックポイントからMap結果を復元
    map_results = None
    if checkpoint and checkpoint.has_part1_checkpoint():
        map_results = checkpoint.load_part1()
        if map_results and len(map_results) == len(session_batches):
            print(f"[Checkpoint] Using cached Map results ({len(map_results)} batches)", flush=True)
        else:
            print(f"[Checkpoint] Map cache invalid. Re-running.", flush=True)
            map_results = None
    
    # 全バッチ完了していない場合、インクリメンタルチェックポイントを確認
    if map_results is None and checkpoint:
        consolidated = checkpoint.consolidate_map_batches(len(session_batches))
        if consolidated:
            map_results = consolidated
            print(f"[Checkpoint] Consolidated {len(map_results)} Map batches from incremental checkpoints", flush=True)
            checkpoint.save_part1(map_results)
    
    if map_results is None:
        import threading
        lock = threading.Lock()
        
        # 完了済みバッチを取得
        completed_batches = checkpoint.load_partial_map_results() if checkpoint else {}
        remaining_count = len(session_batches) - len(completed_batches)
        if completed_batches:
            print(f"[Checkpoint] Resuming: {len(completed_batches)} batches already completed, {remaining_count} remaining", flush=True)
        
        def process_map_batch_with_checkpoint(args):
            idx, batch_ids = args
            
            if idx in completed_batches:
                return (completed_batches[idx][0], completed_batches[idx][1])
            
            combined_content = ""
            for sid in batch_ids:
                content = session_contents[sid]
                combined_content += f"=== Comment ID: {sid} ===\n{content}\n\n"
                
            print(f"Processing Pubcom Map Batch {idx+1}/{len(session_batches)} ({len(batch_ids)} comments)...", flush=True)
            
            ctx1 = build_context(meta, "", [], cfg.output_length_guidance, reference_documents=combined_content)
            ctx1["focus"] = cfg.focus
            prompt = load_and_render(map_prompt_path, ctx1)
            
            output = _call_model(prompt, cfg, step_name="pubcom_aggregate_map")
            
            batch_id_str = str(batch_ids)
            
            if checkpoint:
                with lock:
                    checkpoint.save_map_batch(idx, batch_id_str, output)
            
            return (batch_id_str, output)

        batches_to_process = list(enumerate(session_batches))
        if max_map_batches is not None:
            remaining_batches = [(idx, batch) for idx, batch in batches_to_process if idx not in completed_batches]
            if len(remaining_batches) > max_map_batches:
                print(f"[Batch Limit] Processing {max_map_batches} batches (of {len(remaining_batches)} remaining)", flush=True)
                batches_to_process = [(idx, batch) for idx, batch in batches_to_process if idx in completed_batches]
                batches_to_process += remaining_batches[:max_map_batches]

        with ThreadPoolExecutor(max_workers=5) as executor:
            map_results = list(executor.map(process_map_batch_with_checkpoint, batches_to_process))
        
        if max_map_batches is not None:
            completed_after = checkpoint.load_partial_map_results() if checkpoint else {}
            if len(completed_after) < len(session_batches):
                print(f"[Batch Limit] Partial completion: {len(completed_after)}/{len(session_batches)} batches done. Run again to continue.", flush=True)
                return {"prompt": "", "report": f"Partial Map: {len(completed_after)}/{len(session_batches)} batches completed. Run again to continue."}
        
        if checkpoint:
            checkpoint.save_part1(map_results)
    
    # --- Phase 2: Reduce (Tree Reduce) ---
    map_reports = [output for batch_id_str, output in map_results if output]
    
    part1_log_content = "# Pubcom Map Output Log\n\n"
    for batch_id_str, output in map_results:
        if output:
            part1_log_content += f"## Batch: {batch_id_str}\n\n{output}\n\n---\n\n"
    
    reduce_prompt_path = prompt_dir / "pubcom_reduce.md"
    
    REDUCE_BATCH_SIZE = 5
    initial_batches = ["\n\n---\n\n".join(map_reports[i:i + REDUCE_BATCH_SIZE]) for i in range(0, len(map_reports), REDUCE_BATCH_SIZE)]
    
    # チェックポイントからPart 2途中経過を復元（API料金節約）
    if checkpoint:
        part2_data = checkpoint.load_part2_state()
        if part2_data:
            _, content = part2_data
            # NOTE: tree_reduceは結果を "\n---\n" で結合して保存している
            initial_batches = content.split("\n---\n")
            print(f"[Checkpoint] Resuming Part 2 from last saved state: {len(initial_batches)} items", flush=True)
    
    print(f"Starting Tree Reduce: {len(map_reports)} map reports -> {len(initial_batches)} initial batches", flush=True)
    
    # ツリー型Reduce用の統合関数を定義
    def reduce_pair(item1: str, item2: str) -> str:
        """2つのパブコメレポートを統合"""
        if not item2:
            return item1
        
        combined = f"{item1}\n\n---\n\n{item2}"
        ctx = build_context(meta, "", [], cfg.output_length_guidance)
        ctx.update({
            "currentReport": item1,
            "newInfo": item2,
            "focus": cfg.focus
        })
        
        prompt = load_and_render(reduce_prompt_path, ctx)
        return _call_model(prompt, cfg, step_name="pubcom_aggregate_reduce")
    
    # 動的マージサイズ計算（トークン上限の80%を目標）
    dynamic_merge_size = calculate_dynamic_merge_size(
        items=initial_batches,
        prompt_template_tokens=2000,
        max_input_tokens=1_048_576,
        target_utilization=0.8,
        max_merge_size=5  # 安全のため上限を抑制
    )
    
    pubcom_consolidated_report, reduce_stats = tree_reduce(
        initial_batches,
        reduce_pair,
        max_workers=5,
        checkpoint=checkpoint,
        merge_size=dynamic_merge_size
    )
    
    # YAMLコードブロックでラップ
    if not pubcom_consolidated_report.strip().startswith("```yaml"):
        pubcom_consolidated_report = f"```yaml\n{pubcom_consolidated_report}\n```"
    
    # --- Token Usage Statistics ---
    from .token_tracker import TokenTracker
    token_stats = TokenTracker.get_summary()
    
    token_stats_md = "\n\n# Token Usage Statistics\n\n| Process / Step | Model | Input Tokens | Output Tokens | Est. Cost (USD) |\n| :--- | :--- | ---: | ---: | ---: |\n"
    
    total_input = 0
    total_output = 0
    total_cost = 0.0
    
    for key in sorted(token_stats.keys()):
        stats = token_stats[key]
        model_name = stats.get("model", "unknown")
        cost = stats.get("cost", 0.0)
        
        token_stats_md += f"| {key} | {model_name} | {stats['input_tokens']:,} | {stats['output_tokens']:,} | ${cost:,.2f} |\n"
        
        total_input += stats.get('input_tokens', 0)
        total_output += stats.get('output_tokens', 0)
        total_cost += cost
    
    token_stats_md += f"| **TOTAL** | | **{total_input:,}** | **{total_output:,}** | **${total_cost:,.2f}** |\n"
    
    # レポートにToken Stats追加
    final_report = pubcom_consolidated_report + token_stats_md
    
    # チェックポイントをクリア
    if checkpoint:
        checkpoint.clear()

    return {
        "prompt": "",
        "report": final_report,
        "part1_log": part1_log_content,
        "pubcom_consolidated_report": pubcom_consolidated_report,
        "citation_registry": citation_registry,
        "pubcom_to_cite_id": pubcom_to_cite_id
    }


def run_pubcom_compare(prompt_dir: Path, meta: Dict[str, Any], pubcom_report: str, prior_hypothesis: str, cfg: RunConfig, comparison_model: Optional[str] = None, prior_token_stats_list: Optional[List[Tuple[str, Dict]]] = None) -> Dict[str, Any]:
    """
    pubcom_compare: 比較分析のみ
    
    入力:
        - pubcom_report: 集約済みパブコメレポート（YAML形式）
        - prior_hypothesis: 事前仮説レポート（複数YAMLブロック可）
        - prior_token_stats_list: 事前ステージのトークン統計 [(stage_name, stats_dict), ...]
    
    出力: 最終比較レポート
    """
    # 複数のYAMLブロックがある場合は統合（1A+1B など）
    merged_prior_hypothesis = merge_prior_hypothesis_yamls(prior_hypothesis)
    
    compare_model_name = comparison_model if comparison_model else cfg.model
    print(f"Processing Pubcom Comparison (model: {compare_model_name})...", flush=True)
    compare_prompt_path = prompt_dir / "pubcom_comparison.md"
    
    ctx = build_context(meta, "", [], cfg.output_length_guidance)
    ctx.update({
        "priorHypothesis": merged_prior_hypothesis,
        "pubcomReport": pubcom_report,
        "focus": cfg.focus
    })
    
    compare_prompt = load_and_render(compare_prompt_path, ctx)
    
    compare_cfg = RunConfig(
        mode=cfg.mode,
        model=compare_model_name,
        temperature=cfg.comparison_temperature,
        comparison_temperature=cfg.comparison_temperature,
        max_output_tokens=cfg.max_output_tokens,
        top_p=cfg.top_p,
        top_k=cfg.top_k,
        output_length_guidance=cfg.output_length_guidance,
        focus=cfg.focus
    )
    final_insight = _call_model(compare_prompt, compare_cfg, step_name="pubcom_compare")

    # --- Token Usage Statistics ---
    from .token_tracker import TokenTracker
    token_stats = TokenTracker.get_summary()
    
    token_stats_md = "\n\n# Token Usage Statistics\n\n| Stage | Process / Step | Model | Input Tokens | Output Tokens | Est. Cost (USD) |\n| :--- | :--- | :--- | ---: | ---: | ---: |\n"
    
    total_input = 0
    total_output = 0
    total_cost = 0.0
    
    # Prior stages (Stage 1: 事前仮説生成, Stage 2: パブコメ集約)
    if prior_token_stats_list:
        for stage_name, stage_stats in prior_token_stats_list:
            for key in sorted(stage_stats.keys()):
                stats = stage_stats[key]
                model_name = stats.get("model", "unknown")
                cost = stats.get("cost", 0.0)
                
                token_stats_md += f"| {stage_name} | {key} | {model_name} | {stats['input_tokens']:,} | {stats['output_tokens']:,} | ${cost:,.2f} |\n"
                
                total_input += stats.get('input_tokens', 0)
                total_output += stats.get('output_tokens', 0)
                total_cost += cost
    
    # Current stage (Stage 3: 比較分析)
    for key in sorted(token_stats.keys()):
        stats = token_stats[key]
        model_name = stats.get("model", "unknown")
        cost = stats.get("cost", 0.0)
        
        token_stats_md += f"| Stage 3 (比較分析) | {key} | {model_name} | {stats['input_tokens']:,} | {stats['output_tokens']:,} | ${cost:,.2f} |\n"
        
        total_input += stats.get('input_tokens', 0)
        total_output += stats.get('output_tokens', 0)
        total_cost += cost
    
    token_stats_md += f"| **TOTAL** | | | **{total_input:,}** | **{total_output:,}** | **${total_cost:,.2f}** |\n"
    
    # レポートにToken Stats追加（finalize_report_citationsはCLI側で一度だけ呼ぶ）
    final_report = final_insight + token_stats_md

    # CLI側で_with_references.mdを生成するためにcitation_registryを返す（空だがフロー維持）
    citation_registry = CitationRegistry()
    
    return {
        "prompt": compare_prompt,
        "report": final_report,
        "pubcom_consolidated_report": pubcom_report,
        "citation_registry": citation_registry,
        "merged_hypothesis_content": prior_hypothesis  # CLI側でfinalize_report_citationsに渡す
    }
