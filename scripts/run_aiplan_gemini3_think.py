"""
AI基本計画 パイプライン一括実行スクリプト (Gemini 3 + Thinking版)
- Stage 1-2: gemini-3-flash-preview, temp=0.0, thinking=high
- Stage 3: gemini-3-pro-preview, temp=1.0, thinking=high
"""
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# プロジェクトルート
PROJECT_ROOT = Path(__file__).parent.parent

# 設定
META = "each_project/ai-plan-test/meta.yaml"
SOURCE_DIR = "each_project/ai-plan-test/shingikai"
CSV = "data/ai-plan-test_messages.csv"
LOG_DIR = "doc"
FOCUS = "人工知能基本計画"

# Gemini 3 モデル
FLASH_MODEL = "gemini-3-flash-preview"
PRO_MODEL = "gemini-3-pro-preview"


def run_command(args: list[str], description: str):
    """コマンドを実行し、結果を表示"""
    print(f"\n{'='*60}")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {description}")
    print(f"{'='*60}")
    print(f"Command: {' '.join(args)}\n")
    
    result = subprocess.run(args, cwd=PROJECT_ROOT)
    if result.returncode != 0:
        print(f"[ERROR] {description} failed with code {result.returncode}")
        sys.exit(1)
    return result


def find_latest_run_output(base_dir: Path, filename: str) -> Path:
    """指定ディレクトリ配下の最新runディレクトリから指定ファイルを探す"""
    # 日付ディレクトリ（YYYY-MM-DD）を最新順に取得
    date_dirs = sorted([d for d in base_dir.iterdir() if d.is_dir() and d.name.count("-") == 2], reverse=True)
    
    for date_dir in date_dirs:
        runs = sorted(date_dir.glob("run-*"), reverse=True)
        for run_dir in runs:
            target = run_dir / "outputs" / filename
            if target.exists():
                return target
    
    raise FileNotFoundError(f"Could not find {filename} in any run directory under {base_dir}")


def main():
    print(f"\n{'#'*60}")
    print("# AI基本計画 Pipeline: Gemini 3 + Thinking")
    print("# Stage 1-2: gemini-3-flash-preview (temp=0, think=high)")
    print("# Stage 3: gemini-3-pro-preview (temp=1, think=high)")
    print(f"{'#'*60}")
    
    log_base = PROJECT_ROOT / LOG_DIR
    
    # Stage 1: 事前仮説生成 (temp=0, think=high)
    run_command([
        sys.executable, "-m", "src.interview_analysis.cli",
        "--mode", "pre_hypothesis_iterative",
        "--source-dir", SOURCE_DIR,
        "--meta", META,
        "--model", FLASH_MODEL,
        "--temperature", "0.0",
        "--thinking-level", "high",
        "--focus", FOCUS,
        "--log-dir", LOG_DIR
    ], f"Stage 1: pre_hypothesis_iterative ({FLASH_MODEL}, temp=0, think=high)")
    
    stage1_output = find_latest_run_output(log_base, "report_pre_hypothesis_iterative.md")
    print(f"\n[OK] Stage 1 output: {stage1_output}")
    
    # Stage 2: パブコメ集約 (temp=0, think=high)
    run_command([
        sys.executable, "-m", "src.interview_analysis.cli",
        "--mode", "pubcom_aggregate",
        "--csv", CSV,
        "--meta", META,
        "--model", FLASH_MODEL,
        "--temperature", "0.0",
        "--thinking-level", "high",
        "--focus", FOCUS,
        "--log-dir", LOG_DIR
    ], f"Stage 2: pubcom_aggregate ({FLASH_MODEL}, temp=0, think=high)")
    
    stage2_output = find_latest_run_output(log_base, "pubcom_report.md")
    print(f"\n[OK] Stage 2 output: {stage2_output}")
    
    # Stage 3: 比較分析 (temp=1, think=high)
    run_command([
        sys.executable, "-m", "src.interview_analysis.cli",
        "--mode", "pubcom_compare",
        "--pubcom-report", str(stage2_output),
        "--prior-hypothesis", str(stage1_output),
        "--merged-hypothesis", str(stage1_output),
        "--meta", META,
        "--model", PRO_MODEL,
        "--comparison-temperature", "1.0",
        "--thinking-level", "high",
        "--focus", FOCUS,
        "--log-dir", LOG_DIR
    ], f"Stage 3: pubcom_compare ({PRO_MODEL}, temp=1, think=high)")
    
    stage3_output = find_latest_run_output(log_base, "report_pubcom_compare_with_references.md")
    print(f"\n[OK] Stage 3 output: {stage3_output}")
    
    print(f"\n{'#'*60}")
    print("# Pipeline Complete!")
    print(f"{'#'*60}")
    print(f"Final report: {stage3_output}")


if __name__ == "__main__":
    main()
