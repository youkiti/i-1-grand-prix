from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from .loader import load_messages_csv, build_sessions_data
from .prompts import load_and_render
from .model_provider import create_provider, ModelConfig


@dataclass
class RunConfig:
    mode: str  # hypothesis | initial | update | merge
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
