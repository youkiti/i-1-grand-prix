#!/usr/bin/env python3
"""
モデル評価スクリプト

指定したモデルでレポート生成を実行し、実行時間と出力情報を記録する。
"""
import argparse
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict

from dotenv import load_dotenv

from src.interview_analysis.cli import load_meta
from src.interview_analysis.logger import create_run_dir, save_json, save_text
from src.interview_analysis.pipeline import RunConfig, run_initial

load_dotenv()


@dataclass
class EvalResult:
    """評価結果"""
    model_name: str
    execution_time_sec: float
    report_length_chars: int
    report_length_lines: int
    success: bool
    error_message: str = ""


def run_evaluation(
    csv_path: Path,
    meta_path: Path,
    prompt_path: Path,
    model: str,
    temperature: float,
    max_output_tokens: int,
    output_dir: Path,
) -> None:
    """指定したモデルで評価を実行"""

    print("\n" + "="*60)
    print("モデル評価")
    print("="*60)
    print(f"モデル: {model}")
    print(f"データ: {csv_path}")
    print(f"温度: {temperature}")
    print(f"最大トークン: {max_output_tokens}")

    meta = load_meta(meta_path)

    cfg = RunConfig(
        mode="initial",
        model=model,
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )

    start_time = time.time()

    try:
        result = run_initial(prompt_path, meta, csv_path, cfg)
        execution_time = time.time() - start_time

        report = result["report"]
        report_lines = report.count("\n") + 1
        report_chars = len(report)

        print(f"\n✅ 成功")
        print(f"   実行時間: {execution_time:.2f}秒")
        print(f"   レポート長: {report_chars:,}文字 / {report_lines}行")

        eval_result = EvalResult(
            model_name=model,
            execution_time_sec=execution_time,
            report_length_chars=report_chars,
            report_length_lines=report_lines,
            success=True,
        )

        # 結果を保存
        run_dir = create_run_dir(output_dir)

        # レポート保存
        save_text(run_dir / "outputs" / "report.md", report)
        save_text(run_dir / "prompts" / "used_prompt.txt", result["prompt"])

        # 評価結果（JSON）
        summary = {
            "timestamp": run_dir.name,
            "config": {
                "csv": str(csv_path),
                "meta": str(meta_path),
                "model": model,
                "temperature": temperature,
                "max_output_tokens": max_output_tokens,
            },
            "result": asdict(eval_result),
        }
        save_json(run_dir / "evaluation_result.json", summary)

        # 評価結果（Markdown）
        markdown_summary = generate_markdown_summary(eval_result, summary["config"])
        save_text(run_dir / "evaluation_result.md", markdown_summary)

        print(f"\n{'='*60}")
        print(f"✅ 評価完了: {run_dir}")
        print(f"{'='*60}\n")
        print(markdown_summary)

    except Exception as e:
        execution_time = time.time() - start_time
        print(f"\n❌ エラー: {e}")
        print(f"   実行時間: {execution_time:.2f}秒")

        import traceback
        traceback.print_exc()

        eval_result = EvalResult(
            model_name=model,
            execution_time_sec=execution_time,
            report_length_chars=0,
            report_length_lines=0,
            success=False,
            error_message=str(e),
        )

        # エラー情報も保存
        run_dir = create_run_dir(output_dir)
        summary = {
            "timestamp": run_dir.name,
            "config": {
                "csv": str(csv_path),
                "meta": str(meta_path),
                "model": model,
                "temperature": temperature,
                "max_output_tokens": max_output_tokens,
            },
            "result": asdict(eval_result),
        }
        save_json(run_dir / "evaluation_result.json", summary)


def generate_markdown_summary(result: EvalResult, config: Dict[str, Any]) -> str:
    """Markdown形式の評価サマリーを生成"""
    lines = [
        "# モデル評価結果",
        "",
        "## 設定",
        f"- モデル: `{result.model_name}`",
        f"- データ: `{config['csv']}`",
        f"- 温度: {config['temperature']}",
        f"- 最大トークン: {config['max_output_tokens']}",
        "",
        "## 結果",
        "",
    ]

    if result.success:
        lines.extend([
            f"- ステータス: ✅ 成功",
            f"- 実行時間: {result.execution_time_sec:.2f}秒",
            f"- レポート文字数: {result.report_length_chars:,}文字",
            f"- レポート行数: {result.report_length_lines}行",
        ])
    else:
        lines.extend([
            f"- ステータス: ❌ 失敗",
            f"- 実行時間: {result.execution_time_sec:.2f}秒",
            "",
            "## エラー詳細",
            "",
            "```",
            result.error_message,
            "```",
        ])

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="モデル評価")
    parser.add_argument("--csv", type=Path, required=True, help="メッセージCSV")
    parser.add_argument("--meta", type=Path, default=Path("config/meta.yaml"), help="メタ情報")
    parser.add_argument("--prompt", type=Path, default=Path("prompts/initial.md"), help="プロンプト")
    parser.add_argument("--model", default="x-ai/grok-4.1-fast:free", help="評価対象モデル")
    parser.add_argument("--temperature", type=float, default=0.3)
    parser.add_argument("--max-output-tokens", type=int, default=64000)
    parser.add_argument("--output-dir", type=Path, default=Path("evaluation"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    run_evaluation(
        csv_path=args.csv,
        meta_path=args.meta,
        prompt_path=args.prompt,
        model=args.model,
        temperature=args.temperature,
        max_output_tokens=args.max_output_tokens,
        output_dir=args.output_dir,
    )


if __name__ == "__main__":
    main()
