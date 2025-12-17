"""
Funani パイプライン一括実行スクリプト
- Stage 1-2: gemini-flash-latest
- Stage 3: gemini-3-pro-preview
"""
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# プロジェクトルート
PROJECT_ROOT = Path(__file__).parent.parent

# 設定
META = "each_project/funani/meta.yaml"
SOURCE_DIR = "each_project/funani/shingikai"
CSV = "data/bill-of-lading_messages.csv"
FOCUS = "電子船荷証券"

FLASH_MODEL = "gemini-flash-latest"
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


def find_latest_run_output(pattern: str, filename: str) -> Path:
    """doc配下の最新runディレクトリから指定ファイルを探す"""
    doc_dir = PROJECT_ROOT / "doc"
    today = datetime.now().strftime("%Y-%m-%d")
    today_dir = doc_dir / today
    
    if not today_dir.exists():
        # 日付ディレクトリがなければdoc直下を探す
        runs = sorted(doc_dir.glob("run-*"), reverse=True)
    else:
        runs = sorted(today_dir.glob("run-*"), reverse=True)
    
    for run_dir in runs:
        target = run_dir / "outputs" / filename
        if target.exists():
            return target
    
    raise FileNotFoundError(f"Could not find {filename} in any run directory")


def main():
    print(f"\n{'#'*60}")
    print("# Funani Pipeline: flash-latest (Stage 1-2) + pro-preview (Stage 3)")
    print(f"{'#'*60}")
    
    # Stage 1: 事前仮説生成
    run_command([
        sys.executable, "-m", "src.interview_analysis.cli",
        "--mode", "pre_hypothesis_iterative",
        "--source-dir", SOURCE_DIR,
        "--meta", META,
        "--model", FLASH_MODEL,
        "--temperature", "0.0",
        "--focus", FOCUS
    ], "Stage 1: pre_hypothesis_iterative (flash-latest)")
    
    stage1_output = find_latest_run_output("run-*", "report_pre_hypothesis_iterative.md")
    print(f"\n[OK] Stage 1 output: {stage1_output}")
    
    # Stage 2: パブコメ集約
    run_command([
        sys.executable, "-m", "src.interview_analysis.cli",
        "--mode", "pubcom_aggregate",
        "--csv", CSV,
        "--meta", META,
        "--model", FLASH_MODEL,
        "--temperature", "0.0",
        "--focus", FOCUS
    ], "Stage 2: pubcom_aggregate (flash-latest)")
    
    stage2_output = find_latest_run_output("run-*", "pubcom_report.md")
    print(f"\n[OK] Stage 2 output: {stage2_output}")
    
    # Stage 3: 比較分析
    run_command([
        sys.executable, "-m", "src.interview_analysis.cli",
        "--mode", "pubcom_compare",
        "--pubcom-report", str(stage2_output),
        "--prior-hypothesis", str(stage1_output),
        "--meta", META,
        "--model", PRO_MODEL,
        "--comparison-temperature", "1.0",
        "--focus", FOCUS
    ], "Stage 3: pubcom_compare (pro-preview)")
    
    stage3_output = find_latest_run_output("run-*", "report_pubcom_compare_with_references.md")
    print(f"\n[OK] Stage 3 output: {stage3_output}")
    
    print(f"\n{'#'*60}")
    print("# Pipeline Complete!")
    print(f"{'#'*60}")
    print(f"Final report: {stage3_output}")


if __name__ == "__main__":
    main()
