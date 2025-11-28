from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from .loader import load_messages_csv, build_sessions_data
from .prompts import load_and_render
from .model_provider import create_provider, ModelConfig


@dataclass
class RunConfig:
    mode: str  # hypothesis | initial | initial_auto | initial_part1 | initial_part2 | update | merge
    model: str
    temperature: float = 0.3
    max_output_tokens: int = 64000
    top_p: float = 0.95
    top_k: int = 40
    output_length_guidance: str = ""  # 任意


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


def build_context(meta: Dict[str, Any], sessions_data: str, session_ids: List[str], output_length_guidance: str) -> Dict[str, Any]:
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
