#!/usr/bin/env python3
"""
比較フェーズのみを再実行するスクリプト

既存のレポートを使用して、比較フェーズのみを新しい設定（temperature=1）で実行する。
"""
import sys
sys.path.insert(0, ".")

from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from src.interview_analysis.pipeline import RunConfig, _call_model, build_context
from src.interview_analysis.prompts import load_and_render
from src.interview_analysis.logger import create_run_dir, save_text, save_json


def extract_pubcom_yaml_from_report(report_path: Path) -> str:
    """レポートから参考セクションのパブコメYAMLを抽出"""
    content = report_path.read_text(encoding="utf-8")
    
    # "# 参考: パブリックコメント集約レポート" 以降を抽出
    marker = "# 参考: パブリックコメント集約レポート"
    if marker in content:
        idx = content.find(marker)
        return content[idx:]
    
    # マーカーがなければ yaml セクションを探す
    yaml_start = content.find("```yaml")
    if yaml_start != -1:
        yaml_end = content.rfind("```")
        if yaml_end > yaml_start:
            return content[yaml_start:yaml_end + 3]
    
    return ""


def main():
    # 入力ファイル
    prior_hypothesis_path = Path("doc/2025-12-13/run-163728/outputs/report.md")
    previous_pubcom_report_path = Path("doc/2025-12-13/run-174907/outputs/report.md")
    prompt_dir = Path("prompts")
    log_dir = Path("doc")
    
    # 前回のレポートからパブコメ統合YAMLを抽出
    print("Loading prior hypothesis...", flush=True)
    prior_hypothesis = prior_hypothesis_path.read_text(encoding="utf-8")
    
    print("Loading previous pubcom report...", flush=True)
    previous_report = previous_pubcom_report_path.read_text(encoding="utf-8")
    pubcom_yaml = extract_pubcom_yaml_from_report(previous_pubcom_report_path)
    
    if not pubcom_yaml:
        print("Error: パブコメ統合YAMLが見つかりません")
        return
    
    print(f"Pubcom YAML extracted: {len(pubcom_yaml)} characters", flush=True)
    
    # 設定
    cfg = RunConfig(
        mode="pubcom_analysis",
        model="gemini-3-pro-preview",  # 比較用モデル
        temperature=1.0,  # 新しい温度設定
        max_output_tokens=64000,
        focus="船荷証券の電子化"
    )
    
    print(f"Running comparison phase with model={cfg.model}, temperature={cfg.temperature}...", flush=True)
    
    # 比較プロンプト
    compare_prompt_path = prompt_dir / "pubcom_comparison.md"
    
    meta = {}
    ctx = build_context(meta, "", [], "")
    ctx.update({
        "priorHypothesis": prior_hypothesis,
        "pubcomReport": pubcom_yaml,
        "focus": cfg.focus
    })
    
    compare_prompt = load_and_render(compare_prompt_path, ctx)
    
    # 比較実行
    final_insight = _call_model(compare_prompt, cfg)
    
    # 保存
    run_dir = create_run_dir(log_dir)
    save_text(run_dir / "prompts" / "comparison_prompt.txt", compare_prompt)
    save_text(run_dir / "outputs" / "report.md", final_insight)
    save_json(run_dir / "config.json", {
        "mode": "comparison_only",
        "model": cfg.model,
        "temperature": cfg.temperature,
        "prior_hypothesis": str(prior_hypothesis_path),
        "previous_pubcom_report": str(previous_pubcom_report_path),
    })
    
    print(f"[OK] Complete: {run_dir}", flush=True)


if __name__ == "__main__":
    main()
