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
    load_scraper_metadata as load_citation_metadata
)


@dataclass
class RunConfig:
    mode: str  # hypothesis | initial | initial_auto | initial_part1 | initial_part2 | update | merge | pre_hypothesis_auto | pre_hypothesis_iterative
    model: str
    temperature: float = 0.3
    max_output_tokens: int = 64000
    top_p: float = 0.95
    top_k: int = 40
    output_length_guidance: str = ""
    focus: str = ""  # 分析のフォーカス（主眼）  # 任意


def _call_model(prompt: str, cfg: RunConfig) -> str:
    """
    モデル名から自動判定してプロバイダーを選択し、生成を実行

    - モデル名に "/" が含まれる → OpenRouter
    - それ以外 → Gemini
    """
    provider = create_provider(cfg.model)
    model_config = ModelConfig(
        model=cfg.model,
        temperature=cfg.temperature,
        max_output_tokens=cfg.max_output_tokens,
        top_p=cfg.top_p,
        top_k=cfg.top_k,
    )
    return provider.generate(prompt, model_config)


def tree_reduce(
    items: List[str],
    reduce_fn,
    max_workers: int = 10,
    checkpoint=None,
    checkpoint_prefix: str = "reduce"
) -> tuple:
    """
    ツリー型並列Reduce
    
    O(n) の逐次処理を O(log n) レベルの並列処理に変換。
    例: 34アイテム → 5レベル（各レベル並列実行）→ 約7倍高速化
    
    Args:
        items: 処理対象のリスト
        reduce_fn: 2つのアイテムを統合する関数 (item1, item2) -> merged
        max_workers: 並列ワーカー数
        checkpoint: チェックポイントオブジェクト（オプション）
        checkpoint_prefix: チェックポイントのプレフィックス
    
    Returns:
        (result, stats) のタプル
        - result: 最終的に統合された1つの結果
        - stats: {"initial_count": N, "levels": [pairs_per_level]}
    """
    from concurrent.futures import ThreadPoolExecutor
    
    stats = {"initial_count": len(items), "levels": []}
    
    if not items:
        return "", stats
    
    if len(items) == 1:
        return items[0], stats
    
    current_level = items
    level_num = 0
    
    while len(current_level) > 1:
        level_num += 1
        pairs = []
        
        # ペアを作成（奇数の場合、最後の1つはそのまま次レベルへ）
        for i in range(0, len(current_level), 2):
            if i + 1 < len(current_level):
                pairs.append((current_level[i], current_level[i + 1]))
            else:
                # 奇数の場合、最後のアイテムは空文字とペアにして次へ
                pairs.append((current_level[i], ""))
        
        stats["levels"].append(len(pairs))
        print(f"  Tree Reduce Level {level_num}: {len(pairs)} pairs (parallel)...", flush=True)
        
        # 並列実行
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(lambda p: reduce_fn(p[0], p[1]), pairs))
        
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
    output = _call_model(prompt, cfg)

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
    output = _call_model(prompt, cfg)

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
    output = _call_model(prompt, cfg)

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
    output = _call_model(prompt, cfg)

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
    output = _call_model(prompt, cfg)

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
    output = _call_model(prompt, cfg)

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
    part1_output = _call_model(part1_prompt, cfg)

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
    part2_output = _call_model(part2_prompt, cfg)

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


def run_pre_hypothesis_iterative(prompt_dir: Path, meta: Dict[str, Any], source_path: Path, cfg: RunConfig, use_checkpoint: bool = True) -> Dict[str, Any]:
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

    # 全ドキュメントをメタデータ付きで収集
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

    # 後方互換性のため items を作成（ただし enriched content を使用）
    items = [(doc.filename, doc.to_enriched_content()) for doc in documents]

    # チェックポイントからPart 1を復元
    part1_results = None
    if checkpoint and checkpoint.has_part1_checkpoint():
        part1_results = checkpoint.load_part1()
        # ファイル数が一致するか確認
        if part1_results and len(part1_results) == len(items):
            print(f"[Checkpoint] Using cached Part 1 results ({len(part1_results)} items)", flush=True)
        else:
            print(f"[Checkpoint] Part 1 cache invalid (expected {len(items)}, got {len(part1_results) if part1_results else 0}). Re-running.", flush=True)
            part1_results = None

    if part1_results is None:
        # Part 1を実行
        from concurrent.futures import ThreadPoolExecutor

        def process_document(item):
            filename, content = item
            print(f"Processing Part 1 for: {filename}...", flush=True)
            ctx1 = build_context(meta, "", [], cfg.output_length_guidance, reference_documents=f"=== File: {filename} ===\n\n{content}")
            ctx1["focus"] = cfg.focus
            part1_prompt = load_and_render(part1_prompt_path, ctx1)
            output = _call_model(part1_prompt, cfg)
            return (filename, output)

        with ThreadPoolExecutor(max_workers=10) as executor:
            part1_results = list(executor.map(process_document, items))

        # チェックポイント保存
        if checkpoint:
            checkpoint.save_part1(part1_results)

    if not part1_results:
        return {"prompt": "", "report": "No documents found or processed."}

    # Part 1レポート（出力のみ）のリストを作成
    part1_reports = [output for _, output in part1_results]

    # --- Phase 2: Reduce (Tree-Based Parallel) ---
    part2_prompt_path = prompt_dir / "pre_hypothesis_part2_iterative.md"
    part2_prompt_template = load_template(part2_prompt_path)
    
    # Part 1レポートを初期バッチとして使用（3つずつグループ化）
    INITIAL_BATCH_SIZE = 3
    initial_batches = []
    for i in range(0, len(part1_reports), INITIAL_BATCH_SIZE):
        batch = part1_reports[i:i + INITIAL_BATCH_SIZE]
        initial_batches.append("\n\n---\n\n".join(batch))
    
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
            "focus": cfg.focus
        })
        
        prompt = load_and_render(part2_prompt_path, ctx2)
        return _call_model(prompt, cfg)
    
    # ツリー型並列Reduceを実行
    import time
    reduce_start = time.time()
    final_qa, reduce_stats = tree_reduce(initial_batches, reduce_pair, max_workers=10, checkpoint=checkpoint)
    reduce_time = time.time() - reduce_start
    
    # 最終プロンプトを記録（代表としてラスト生成時のものを使用）
    ctx_final = build_context(meta, "", [], cfg.output_length_guidance)
    ctx_final.update({"currentQA": "(accumulated)", "newInfo": "(merged)", "focus": cfg.focus})
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
            {"name": "審議会資料", "path": str(source_path), "count": len(items), "unit": "ファイル"}
        ],
        steps=[
            {
                "name": "Part 1 (Map)",
                "phase": "論点抽出",
                "input": len(items),
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

    # Citation Registry: 出典一覧を生成
    citation_appendix = generate_citation_appendix(citation_registry)

    # Final Report Construction - メタ情報は最後に配置（読者はコンテンツを先に見たい）
    final_report = "# 最終成果物 (Q&Aリスト)\n\n" + final_qa + "\n\n---\n\n" + citation_appendix + process_metadata + "\n\n" + metadata_header

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


def run_pubcom_analysis(prompt_dir: Path, meta: Dict[str, Any], csv_path: Path, previous_report: str, cfg: RunConfig, use_checkpoint: bool = True, comparison_model: Optional[str] = None, prior_citation_registry: Optional[CitationRegistry] = None) -> Dict[str, Any]:
    """
    pubcom_analysis:
    1. (Map) パブコメCSVの各コメントに対して個別分析を実行 (pubcom_map.md)
    2. (Reduce) 個別分析結果をまとめて統合レポートを作成 (pubcom_reduce.md)
    3. (Compare) 事前仮説(previous_report)と統合レポートを比較 (pubcom_comparison.md)

    Args:
        comparison_model: Comparisonフェーズで使用するモデル（指定なしでcfg.modelを使用）
        prior_citation_registry: 事前仮説生成時のCitation Registry（URL情報の引き継ぎ用）

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
    
    MAP_BATCH_SIZE = 20
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
    
    if map_results is None:
        def process_map_batch(batch_ids):
            combined_content = ""
            for sid in batch_ids:
                content = session_contents[sid]
                combined_content += f"=== Comment ID: {sid} ===\n{content}\n\n"
                
            print(f"Processing Pubcom Map Batch ({len(batch_ids)} comments)...", flush=True)
            
            ctx1 = build_context(meta, "", [], cfg.output_length_guidance, reference_documents=combined_content)
            ctx1["focus"] = cfg.focus
            prompt = load_and_render(map_prompt_path, ctx1)
            
            output = _call_model(prompt, cfg)
            return (str(batch_ids), output)

        with ThreadPoolExecutor(max_workers=5) as executor:
            map_results = list(executor.map(process_map_batch, session_batches))
        
        if checkpoint:
            checkpoint.save_part1(map_results)
    
    map_reports = [output for _, output in map_results]
    
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
        return _call_model(prompt, cfg)
    
    # ツリー型並列Reduceを実行
    pubcom_consolidated_report, reduce_stats = tree_reduce(initial_batches, reduce_pair, max_workers=10, checkpoint=checkpoint)

    # --- Phase 2: Compare (Synthesis) ---
    # 比較用モデルが指定されていれば使用
    compare_model_name = comparison_model if comparison_model else cfg.model
    print(f"Processing Pubcom Comparison (model: {compare_model_name})...", flush=True)
    compare_prompt_path = prompt_dir / "pubcom_comparison.md"
    
    ctx3 = build_context(meta, "", [], cfg.output_length_guidance)
    ctx3.update({
        "priorHypothesis": previous_report,
        "pubcomReport": pubcom_consolidated_report,
        "focus": cfg.focus
    })
    
    compare_prompt = load_and_render(compare_prompt_path, ctx3)
    
    # 比較用の設定を作成（モデルのみ変更）
    compare_cfg = RunConfig(
        mode=cfg.mode,
        model=compare_model_name,
        temperature=cfg.temperature,
        max_output_tokens=cfg.max_output_tokens,
        top_p=cfg.top_p,
        top_k=cfg.top_k,
        output_length_guidance=cfg.output_length_guidance,
        focus=cfg.focus
    )
    final_insight = _call_model(compare_prompt, compare_cfg)

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

    # 統合メタデータセクションを構築
    combined_metadata = process_metadata
    if prior_metadata:
        combined_metadata = combined_metadata + "\n\n" + prior_metadata

    # Citation Registry: 出典一覧を生成
    citation_appendix = generate_citation_appendix(citation_registry)

    final_report = final_insight + "\n\n---\n\n# 参考: パブリックコメント集約レポート\n\n" + pubcom_consolidated_report + "\n\n---\n\n" + citation_appendix + combined_metadata + "\n\n" + metadata_header

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

