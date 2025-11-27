from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import google.generativeai as genai

from .loader import load_messages_csv, build_sessions_data
from .prompts import load_and_render


@dataclass
class RunConfig:
    mode: str  # hypothesis | initial | update | merge
    model: str
    temperature: float = 0.3
    max_output_tokens: int = 64000
    top_p: float = 0.95
    top_k: int = 40
    output_length_guidance: str = ""  # 任意


def configure_genai(api_key: str) -> None:
    genai.configure(api_key=api_key)


def _call_model(prompt: str, cfg: RunConfig) -> str:
    model = genai.GenerativeModel(cfg.model)
    result = model.generate_content(
        prompt,
        generation_config={
            "temperature": cfg.temperature,
            "max_output_tokens": cfg.max_output_tokens,
            "top_p": cfg.top_p,
            "top_k": cfg.top_k,
        },
    )
    return result.text


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
    prompt = load_and_render(prompt_path, ctx)
    output = _call_model(prompt, cfg)
    return {"prompt": prompt, "report": output}


def run_initial(prompt_path: Path, meta: Dict[str, Any], df_path: Path, cfg: RunConfig) -> Dict[str, Any]:
    df = load_messages_csv(df_path)
    session_ids, sessions_data, _ = build_sessions_data(df)
    ctx = build_context(meta, sessions_data, session_ids, cfg.output_length_guidance)
    prompt = load_and_render(prompt_path, ctx)
    output = _call_model(prompt, cfg)
    return {"prompt": prompt, "report": output}


def run_update(prompt_path: Path, meta: Dict[str, Any], df_path: Path, previous_report: str, cfg: RunConfig) -> Dict[str, Any]:
    df = load_messages_csv(df_path)
    session_ids, sessions_data, _ = build_sessions_data(df)
    ctx = build_context(meta, sessions_data, session_ids, cfg.output_length_guidance)
    ctx.update({
        "previousReport": previous_report,
        "newSessionCount": len(session_ids),
    })
    prompt = load_and_render(prompt_path, ctx)
    output = _call_model(prompt, cfg)
    return {"prompt": prompt, "report": output}


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
    prompt = load_and_render(prompt_path, ctx)
    output = _call_model(prompt, cfg)
    return {"prompt": prompt, "report": output}
