from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from .loader import load_messages_csv, build_sessions_data, load_documents_from_folder, iter_documents_from_folder
from .prompts import load_and_render
from .model_provider import create_provider, ModelConfig


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


def run_pre_hypothesis_iterative(prompt_dir: Path, meta: Dict[str, Any], source_path: Path, cfg: RunConfig) -> Dict[str, Any]:
    """
    pre_hypothesis_iterative:
    1. (Map) 各ドキュメントに対して Part1 (論点抽出) を実行
    2. (Reduce) 抽出された論点群をバッチごとに Part2 (Q&A生成・更新) にかけて、最終的なQ&Aリストを作成
    """
    if not source_path.is_dir():
        raise ValueError("pre_hypothesis_iterative requires a directory path for documents")

    from .loader import iter_documents_from_folder
    from .prompts import load_template

    # --- Phase 1: Map (Extract Points from each document) ---
    part1_reports = []
    part1_prompt_path = prompt_dir / "pre_hypothesis_part1.md"
    # テンプレート読み込みは1回で良いが、load_and_render内で都度行われる設計なのでループ内で呼ぶか、
    # ここではプロンプト内容の記録用にテンプレートだけロードしておく
    part1_prompt_template = load_template(part1_prompt_path)

    # 全ドキュメントを走査
    # ※ ファイル数が多い場合はここで時間がかかる。進捗表示等はCLI側で行うのが理想だが、ここではシンプルに実装。
    # Parallel processing for Part 1
    from concurrent.futures import ThreadPoolExecutor
    
    def process_document(item):
        filename, content = item
        print(f"Processing Part 1 for: {filename}...", flush=True)
        ctx1 = build_context(meta, "", [], cfg.output_length_guidance, reference_documents=f"=== File: {filename} ===\n\n{content}")
        ctx1["focus"] = cfg.focus
        part1_prompt = load_and_render(part1_prompt_path, ctx1)
        return _call_model(part1_prompt, cfg)

    # Collect all items first
    items = list(iter_documents_from_folder(source_path))
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        part1_reports = list(executor.map(process_document, items))

    if not part1_reports:
        return {"prompt": "", "report": "No documents found or processed."}

    # --- Phase 2: Reduce (Iteratively build Q&A) ---
    current_qa = "（まだQ&Aはありません）"
    part2_prompt_path = prompt_dir / "pre_hypothesis_part2_iterative.md"
    part2_prompt_template = load_template(part2_prompt_path)
    
    # バッチサイズ (一度にまとめるPart1レポートの数)
    BATCH_SIZE = 5
    
    # レポートをバッチに分割
    batches = [part1_reports[i:i + BATCH_SIZE] for i in range(0, len(part1_reports), BATCH_SIZE)]
    
    last_part2_prompt = ""

    for i, batch in enumerate(batches):
        print(f"Processing Part 2 Batch {i+1}/{len(batches)}...", flush=True)
        # バッチ内のレポートを結合
        new_info = "\n\n---\n\n".join(batch)
        
        # コンテキスト構築
        # referenceDocumentsは使わず、currentQA と newInfo を使う
        # build_context は汎用的なので、追加のキーは update で入れる
        ctx2 = build_context(meta, "", [], cfg.output_length_guidance)
        ctx2.update({
            "currentQA": current_qa,
            "newInfo": new_info,
            "focus": cfg.focus
        })
        
        # プロンプト生成 & 実行
        part2_prompt = load_and_render(part2_prompt_path, ctx2)
        last_part2_prompt = part2_prompt # 記録用に保持
        
        output = _call_model(part2_prompt, cfg)
        
        # 結果を追記 (Append Only)
        # 最初のイテレーション以外は区切り線を入れるなどの工夫が可能だが、
        # ここでは単純に追記していく。プロンプト側で「新規分のみ」と指示している前提。
        if current_qa == "（まだQ&Aはありません）":
            current_qa = output
        else:
            current_qa += "\n\n" + output

    # --- Final Report Construction ---
    # メタデータ + 最終Q&A + プロンプト(代表)
    metadata_header = _build_combined_metadata(cfg, len(part1_reports), part1_prompt_template, part2_prompt_template)
    
    prompts_section = _build_combined_prompts_section(
        part1_prompt_template, # テンプレートを表示 (個別のプロンプトは多すぎるため)
        last_part2_prompt # 最後の更新に使ったプロンプトを表示
    )

    final_report = metadata_header + "\n\n# 最終成果物 (Q&Aリスト)\n\n" + current_qa + prompts_section

    # Part 1 Log Construction
    part1_log_content = "# Part 1 Outputs (Individual Document Analysis)\n\n"
    for i, report in enumerate(part1_reports):
        filename = items[i][0]
        part1_log_content += f"## File: {filename}\n\n{report}\n\n---\n\n"

    return {"prompt": last_part2_prompt, "report": final_report, "part1_log": part1_log_content}

    return {"prompt": last_part2_prompt, "report": final_report, "part1_log": part1_log_content}


def run_pubcom_analysis(prompt_dir: Path, meta: Dict[str, Any], csv_path: Path, previous_report: str, cfg: RunConfig) -> Dict[str, Any]:
    """
    pubcom_analysis:
    1. (Map) パブコメCSVの各コメントに対して個別分析を実行 (pubcom_map.md)
    2. (Reduce) 個別分析結果をまとめて統合レポートを作成 (pubcom_reduce.md)
    3. (Compare) 事前仮説(previous_report)と統合レポートを比較 (pubcom_comparison.md)
    """
    from .loader import load_messages_csv, build_sessions_data
    from .prompts import load_template
    from concurrent.futures import ThreadPoolExecutor

    # --- Phase 1.1: Map (Individual Analysis) ---
    df = load_messages_csv(csv_path)
    
    # session_id ごとにコンテンツをまとめる
    from collections import defaultdict
    session_dict = defaultdict(list)
    for row in df:
        sid = row.get("session_id", "unknown")
        # メッセージ列を特定（簡易的）
        msg = row.get("message") or row.get("content") or row.get("text") or ""
        session_dict[sid].append(msg)
    
    # 文字列に結合
    session_contents = {sid: "\n".join(msgs) for sid, msgs in session_dict.items()}
    session_ids = list(session_contents.keys())
    
    # --- Phase 1.1: Map (Batched Analysis) ---
    # コメントをバッチ（チャンク）にまとめる
    MAP_BATCH_SIZE = 20
    session_batches = [session_ids[i:i + MAP_BATCH_SIZE] for i in range(0, len(session_ids), MAP_BATCH_SIZE)]
    
    map_prompt_path = prompt_dir / "pubcom_map.md"
    
    def process_map_batch(batch_ids):
        # バッチ内のコメントを結合
        combined_content = ""
        for sid in batch_ids:
            content = session_contents[sid]
            combined_content += f"=== Comment ID: {sid} ===\n{content}\n\n"
            
        print(f"Processing Pubcom Map Batch ({len(batch_ids)} comments)...", flush=True)
        
        # コンテキスト構築
        ctx1 = build_context(meta, "", [], cfg.output_length_guidance, reference_documents=combined_content)
        ctx1["focus"] = cfg.focus
        prompt = load_and_render(map_prompt_path, ctx1)
        
        output = _call_model(prompt, cfg)
        return output, batch_ids, combined_content

    # 並列実行
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(process_map_batch, session_batches))
    
    # Reduceフェーズに渡すために整形
    map_reports = []
    part1_log_content = "# Pubcom Phase 1 Outputs (Batched Analysis)\n\n"
    
    for i, r in enumerate(results):
        output_text, batch_ids, batch_content = r
        # Reduce用
        map_reports.append(output_text)
        
        # ログ用
        part1_log_content += f"## Batch {i+1} (IDs: {batch_ids[0]} - {batch_ids[-1]})\n\n"
        part1_log_content += f"### Original Content (First 500 chars)\n{batch_content[:500]}...\n\n"
        part1_log_content += f"### Analysis\n{output_text}\n\n---\n\n"
    
    if not map_reports:
        return {"prompt": "", "report": "No comments processed."}

    # --- Phase 1.2: Reduce (Iterative Summary) ---
    current_report = "（まだレポートはありません）"
    reduce_prompt_path = prompt_dir / "pubcom_reduce.md"
    
    BATCH_SIZE = 5
    batches = [map_reports[i:i + BATCH_SIZE] for i in range(0, len(map_reports), BATCH_SIZE)]
    
    for i, batch in enumerate(batches):
        print(f"Processing Pubcom Reduce Batch {i+1}/{len(batches)}...", flush=True)
        new_info = "\n\n---\n\n".join(batch)
        
        ctx2 = build_context(meta, "", [], cfg.output_length_guidance)
        ctx2.update({
            "currentReport": current_report,
            "newInfo": new_info,
            "focus": cfg.focus
        })
        
        prompt = load_and_render(reduce_prompt_path, ctx2)
        output = _call_model(prompt, cfg)
        
        if current_report == "（まだレポートはありません）":
            current_report = output
        else:
            current_report += "\n\n" + output

    pubcom_consolidated_report = current_report

    # --- Phase 2: Compare (Synthesis) ---
    print("Processing Pubcom Comparison...", flush=True)
    compare_prompt_path = prompt_dir / "pubcom_comparison.md"
    
    ctx3 = build_context(meta, "", [], cfg.output_length_guidance)
    ctx3.update({
        "priorHypothesis": previous_report,
        "pubcomReport": pubcom_consolidated_report,
        "focus": cfg.focus
    })
    
    compare_prompt = load_and_render(compare_prompt_path, ctx3)
    final_insight = _call_model(compare_prompt, cfg)

    # Final Report Construction
    metadata_header = _build_combined_metadata(cfg, len(session_ids), "Pubcom Analysis", "Comparison")
    
    final_report = metadata_header + "\n\n# パブリックコメント分析・統合レポート\n\n" + final_insight + "\n\n---\n\n# 参考: パブリックコメント集約レポート\n\n" + pubcom_consolidated_report

    return {
        "prompt": compare_prompt, 
        "report": final_report, 
        "part1_log": part1_log_content,
        "pubcom_consolidated_report": pubcom_consolidated_report
    }
