#!/usr/bin/env python
"""
Comparison Phase のみを再実行するスクリプト。
既存の pubcom_consolidated_report と prior_hypothesis を使用して、
比較レポートを再生成する。
"""
import sys
from pathlib import Path

# プロジェクトルートをパスに追加
sys.path.insert(0, str(Path(__file__).parent.parent))

# 環境変数をロード
from dotenv import load_dotenv
load_dotenv()

from src.interview_analysis.pipeline import (
    merge_prior_hypothesis_yamls, 
    build_context, 
    load_and_render, 
    _call_model,
    RunConfig
)


def extract_pubcom_report(report_path: Path) -> str:
    """report.md から pubcom_consolidated_report セクションを抽出"""
    import re
    content = report_path.read_text(encoding="utf-8")
    
    # "参考: パブリックコメント集約レポート" セクション内の ```yaml...``` ブロックを抽出
    start_marker = "# 参考: パブリックコメント集約レポート"
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        raise ValueError("pubcom_consolidated_report セクションが見つかりません")
    
    # セクション開始位置から ```yaml を探す
    section_content = content[start_idx:]
    
    # YAML ブロックを抽出
    pattern = r"```yaml\s*(.*?)```"
    match = re.search(pattern, section_content, re.DOTALL)
    
    if match:
        yaml_content = match.group(1).strip()
        return f"```yaml\n{yaml_content}\n```"
    
    # YAML ブロックが見つからない場合、セクション全体を返す
    end_marker = "\n---\n"
    end_idx = section_content.find(end_marker)
    if end_idx != -1:
        return section_content[:end_idx].strip()
    
    return section_content.strip()


def run_comparison_only(
    prior_hypothesis_path: Path,
    pubcom_report: str,
    focus: str,
    comparison_model: str,
    output_path: Path
):
    """Comparison フェーズのみを実行"""
    prompt_dir = Path("prompts")
    
    # Prior hypothesis を読み込み、複数YAMLをマージ
    prior_hypothesis = prior_hypothesis_path.read_text(encoding="utf-8")
    merged_prior = merge_prior_hypothesis_yamls(prior_hypothesis)
    
    print(f"Prior hypothesis loaded: {len(prior_hypothesis)} chars")
    print(f"After merge: {len(merged_prior)} chars")
    
    # Comparison プロンプトを構築
    compare_prompt_path = prompt_dir / "pubcom_comparison.md"
    
    ctx = {
        "priorHypothesis": merged_prior,
        "pubcomReport": pubcom_report,
        "focus": focus,
        "interviewTitle": "人工知能基本計画",
        "interviewDescription": "",
        "interviewOverview": "",
        "interviewThemes": "",
        "interviewQuestions": "",
        "knowledgeContext": "",
        "outputLengthGuidance": ""
    }
    
    compare_prompt = load_and_render(compare_prompt_path, ctx)
    
    # 設定
    cfg = RunConfig(
        mode="pubcom_analysis",
        model=comparison_model,
        temperature=0.0,
        comparison_temperature=0.0,
        max_output_tokens=64000,
        top_p=0.95,
        top_k=40,
        output_length_guidance="",
        focus=focus
    )
    
    print(f"Running Comparison with model: {comparison_model}...")
    result = _call_model(compare_prompt, cfg)
    
    # 結果を保存
    output_path.write_text(result, encoding="utf-8")
    print(f"Result saved to: {output_path}")
    
    return result


if __name__ == "__main__":
    # 前回の report.md から pubcom_report を抽出
    report_path = Path("doc/2025-12-15/run-084419/outputs/report.md")
    pubcom_report = extract_pubcom_report(report_path)
    print(f"Extracted pubcom_report: {len(pubcom_report)} chars")
    
    # Prior hypothesis
    prior_path = Path("doc/2025-12-15/merged_hypothesis.md")
    
    # 出力先
    output_path = Path("doc/2025-12-15/comparison_only_result.md")
    
    # 実行
    run_comparison_only(
        prior_hypothesis_path=prior_path,
        pubcom_report=pubcom_report,
        focus="人工知能基本計画",
        comparison_model="gemini-3-pro-preview",
        output_path=output_path
    )
