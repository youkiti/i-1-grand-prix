"""
議員定数削減 パイプライン一括実行スクリプト (Gemini 3 + Thinking版)
- Stage 1-2: gemini-3-flash-preview, temp=0.0, thinking=high
- Stage 3: gemini-3-pro-preview, temp=1.0, thinking=high

ソースデータ:
- 審議会資料 (shingikai/): PDFから抽出したテキスト
- 国会会議録 (diet_meetings_*/): 議事録テキスト
"""
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# プロジェクトルート
PROJECT_ROOT = Path(__file__).parent.parent

# 設定
META = "each_project/teisuu/meta.yaml"
SOURCE_DIR_SHINGIKAI = "each_project/teisuu/shingikai"
SOURCE_DIR_DIET = "each_project/teisuu/diet_meetings_議員定数削減_OR_議員定数の削減_2011_2025_20251213_083638"
CSV = "data/teisuu_messages.csv"
LOG_DIR = "doc"
FOCUS = "議員定数削減"

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


def find_all_run_outputs(base_dir: Path, filename: str, count: int = 2) -> list[Path]:
    """指定ディレクトリ配下の最新N個のrunディレクトリから指定ファイルを探す"""
    today = datetime.now().strftime("%Y-%m-%d")
    today_dir = base_dir / today
    
    if today_dir.exists():
        runs = sorted(today_dir.glob("run-*"), reverse=True)
    else:
        runs = sorted(base_dir.glob("run-*"), reverse=True)
    
    results = []
    for run_dir in runs:
        target = run_dir / "outputs" / filename
        if target.exists():
            results.append(target)
            if len(results) >= count:
                break
    
    return results


def merge_hypothesis_files(files: list[Path], output_path: Path):
    """複数の仮説ファイルをマージして1つにまとめる"""
    print(f"\n[INFO] Merging {len(files)} hypothesis files...")
    
    combined_content = []
    for i, f in enumerate(files):
        content = f.read_text(encoding="utf-8")
        source_type = "審議会資料" if "shingikai" in str(f).lower() or i == 1 else "国会会議録"
        combined_content.append(f"# ソース: {source_type}\n\n{content}")
    
    merged = "\n\n---\n\n".join(combined_content)
    output_path.write_text(merged, encoding="utf-8")
    print(f"[OK] Merged hypothesis saved to: {output_path}")
    return output_path


def main():
    print(f"\n{'#'*60}")
    print("# 議員定数削減 Pipeline: Gemini 3 + Thinking")
    print("# Stage 1-2: gemini-3-flash-preview (temp=0, think=high)")
    print("# Stage 3: gemini-3-pro-preview (temp=1, think=high)")
    print("# Sources: shingikai + diet_meetings")
    print(f"{'#'*60}")
    
    log_base = PROJECT_ROOT / LOG_DIR
    
    # Stage 1a: 事前仮説生成 - 審議会資料 (temp=0, think=high)
    run_command([
        sys.executable, "-m", "src.interview_analysis.cli",
        "--mode", "pre_hypothesis_iterative",
        "--source-dir", SOURCE_DIR_SHINGIKAI,
        "--meta", META,
        "--model", FLASH_MODEL,
        "--temperature", "0.0",
        "--thinking-level", "high",
        "--focus", FOCUS,
        "--log-dir", LOG_DIR
    ], f"Stage 1a: pre_hypothesis_iterative - Shingikai ({FLASH_MODEL}, temp=0, think=high)")
    
    stage1a_output = find_latest_run_output(log_base, "report_pre_hypothesis_iterative.md")
    print(f"\n[OK] Stage 1a (Shingikai) output: {stage1a_output}")
    
    # Stage 1b: 事前仮説生成 - 国会会議録 (temp=0, think=high)
    run_command([
        sys.executable, "-m", "src.interview_analysis.cli",
        "--mode", "pre_hypothesis_iterative",
        "--source-dir", SOURCE_DIR_DIET,
        "--meta", META,
        "--model", FLASH_MODEL,
        "--temperature", "0.0",
        "--thinking-level", "high",
        "--focus", FOCUS,
        "--log-dir", LOG_DIR
    ], f"Stage 1b: pre_hypothesis_iterative - Diet Transcripts ({FLASH_MODEL}, temp=0, think=high)")
    
    stage1b_output = find_latest_run_output(log_base, "report_pre_hypothesis_iterative.md")
    print(f"\n[OK] Stage 1b (Diet) output: {stage1b_output}")
    
    # Merge Stage 1 outputs
    merged_hypothesis_path = stage1b_output.parent / "merged_hypothesis.md"
    merge_hypothesis_files([stage1a_output, stage1b_output], merged_hypothesis_path)
    
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
        "--prior-hypothesis", str(merged_hypothesis_path),
        "--merged-hypothesis", str(merged_hypothesis_path),
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

