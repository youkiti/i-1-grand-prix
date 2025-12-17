"""
Funani パイプライン一括実行スクリプト (Gemini 3 版 - Creative Flash)
- Stage 1-2: gemini-3-flash-preview (temperature=1.0, thinking=low)
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
LOG_DIR = "each_project/funani"
FOCUS = "電子船荷証券法案"

# Gemini 3 モデル
FLASH_MODEL = "gemini-3-flash-preview"
PRO_MODEL = "gemini-3-pro-preview"

# Flash model parameters for creative mode
FLASH_TEMPERATURE = "1.0"
FLASH_THINKING_LEVEL = "low"


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
    today = datetime.now().strftime("%Y-%m-%d")
    today_dir = base_dir / today
    
    if today_dir.exists():
        runs = sorted(today_dir.glob("run-*"), reverse=True)
    else:
        runs = sorted(base_dir.glob("run-*"), reverse=True)
    
    for run_dir in runs:
        target = run_dir / "outputs" / filename
        if target.exists():
            return target
    
    raise FileNotFoundError(f"Could not find {filename} in any run directory under {base_dir}")


def main():
    print(f"\n{'#'*60}")
    print("# Funani Pipeline: Gemini 3 Hybrid (Creative Flash)")
    print(f"# Stage 1-2: {FLASH_MODEL} (temp={FLASH_TEMPERATURE}, thinking={FLASH_THINKING_LEVEL})")
    print(f"# Stage 3: {PRO_MODEL}")
    print(f"{'#'*60}")
    
    log_base = PROJECT_ROOT / LOG_DIR
    
    # Stage 1: 事前仮説生成 (Creative Flash)
    run_command([
        sys.executable, "-m", "src.interview_analysis.cli",
        "--mode", "pre_hypothesis_iterative",
        "--source-dir", SOURCE_DIR,
        "--meta", META,
        "--model", FLASH_MODEL,
        "--temperature", FLASH_TEMPERATURE,
        "--thinking-level", FLASH_THINKING_LEVEL,
        "--focus", FOCUS,
        "--log-dir", LOG_DIR
    ], f"Stage 1: pre_hypothesis_iterative ({FLASH_MODEL}, temp={FLASH_TEMPERATURE}, thinking={FLASH_THINKING_LEVEL})")
    
    stage1_output = find_latest_run_output(log_base, "report_pre_hypothesis_iterative.md")
    print(f"\n[OK] Stage 1 output: {stage1_output}")
    
    # Stage 2: パブコメ集約 (Creative Flash)
    run_command([
        sys.executable, "-m", "src.interview_analysis.cli",
        "--mode", "pubcom_aggregate",
        "--csv", CSV,
        "--meta", META,
        "--model", FLASH_MODEL,
        "--temperature", FLASH_TEMPERATURE,
        "--thinking-level", FLASH_THINKING_LEVEL,
        "--focus", FOCUS,
        "--log-dir", LOG_DIR
    ], f"Stage 2: pubcom_aggregate ({FLASH_MODEL}, temp={FLASH_TEMPERATURE}, thinking={FLASH_THINKING_LEVEL})")
    
    stage2_output = find_latest_run_output(log_base, "pubcom_report.md")
    print(f"\n[OK] Stage 2 output: {stage2_output}")
    
    # Stage 3: 比較分析 (Pro)
    run_command([
        sys.executable, "-m", "src.interview_analysis.cli",
        "--mode", "pubcom_compare",
        "--pubcom-report", str(stage2_output),
        "--prior-hypothesis", str(stage1_output),
        "--merged-hypothesis", str(stage1_output),
        "--meta", META,
        "--model", PRO_MODEL,
        "--comparison-temperature", "1.0",
        "--focus", FOCUS,
        "--log-dir", LOG_DIR
    ], f"Stage 3: pubcom_compare ({PRO_MODEL})")
    
    stage3_output = find_latest_run_output(log_base, "report_pubcom_compare_with_references.md")
    print(f"\n[OK] Stage 3 output: {stage3_output}")
    
    print(f"\n{'#'*60}")
    print("# Pipeline Complete!")
    print(f"{'#'*60}")
    print(f"Final report: {stage3_output}")


if __name__ == "__main__":
    main()
