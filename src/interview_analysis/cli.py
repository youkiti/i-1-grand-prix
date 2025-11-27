import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, List

import yaml

from .logger import create_run_dir, save_json, save_text
from .pipeline import (
    RunConfig,
    configure_genai,
    run_hypothesis,
    run_initial,
    run_merge,
    run_update,
)


def load_meta(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    if path.suffix.lower() in {".yml", ".yaml"}:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if path.suffix.lower() == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    raise ValueError("meta は yaml か json で指定してください")


def read_text_file(path: Path, required: bool = True) -> str:
    if not path.exists():
        if required:
            raise FileNotFoundError(f"ファイルが見つかりません: {path}")
        return ""
    return path.read_text(encoding="utf-8")


def load_batch_reports(paths: List[Path]) -> List[str]:
    reports: List[str] = []
    for p in paths:
        reports.append(read_text_file(p))
    return reports


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="インタビュー分析 CLI")
    parser.add_argument("--csv", type=Path, required=False, help="メッセージCSVのパス（hypothesis/initial/updateで使用）")
    parser.add_argument("--meta", type=Path, default=Path("config/meta.yaml"), help="メタ情報 YAML/JSON")
    parser.add_argument("--mode", choices=["hypothesis", "initial", "update", "merge"], required=True)
    parser.add_argument("--previous-report", type=Path, help="UPDATE 用の前回レポート")
    parser.add_argument("--batch-reports", type=Path, nargs="*", help="MERGE 用のレポートファイル群")
    parser.add_argument("--prompt-dir", type=Path, default=Path("prompts"))
    parser.add_argument("--model", default="gemini-flash-lite-latest")
    parser.add_argument("--temperature", type=float, default=0.3)
    parser.add_argument("--max-output-tokens", type=int, default=64000)
    parser.add_argument("--output-length-guidance", default="")
    parser.add_argument("--log-dir", type=Path, default=Path("doc"))
    parser.add_argument("--api-key", default=os.getenv("GOOGLE_API_KEY"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.api_key:
        raise SystemExit("GOOGLE_API_KEY が設定されていません (.env などで指定してください)")

    cfg = RunConfig(
        mode=args.mode,
        model=args.model,
        temperature=args.temperature,
        max_output_tokens=args.max_output_tokens,
        output_length_guidance=args.output_length_guidance,
    )

    meta = load_meta(args.meta)
    prompt_dir: Path = args.prompt_dir

    configure_genai(args.api_key)

    if cfg.mode == "hypothesis":
        if not args.csv:
            raise SystemExit("--csv を指定してください")
        prompt_path = prompt_dir / "hypothesis.md"
        result = run_hypothesis(prompt_path, meta, args.csv, cfg)
    elif cfg.mode == "initial":
        if not args.csv:
            raise SystemExit("--csv を指定してください")
        prompt_path = prompt_dir / "initial.md"
        result = run_initial(prompt_path, meta, args.csv, cfg)
    elif cfg.mode == "update":
        if not args.csv or not args.previous_report:
            raise SystemExit("--csv と --previous-report を指定してください")
        previous_report = read_text_file(args.previous_report)
        prompt_path = prompt_dir / "initial.md" if not (prompt_dir / "update.md").exists() else prompt_dir / "update.md"
        result = run_update(prompt_path, meta, args.csv, previous_report, cfg)
    else:  # merge
        if not args.batch_reports:
            raise SystemExit("--batch-reports を指定してください")
        prompt_path = prompt_dir / "merge.md"
        batch_reports = load_batch_reports(args.batch_reports)
        result = run_merge(prompt_path, meta, batch_reports, cfg)

    run_dir = create_run_dir(args.log_dir)

    # 保存
    save_json(
        run_dir / "config.json",
        {
            "mode": cfg.mode,
            "model": cfg.model,
            "temperature": cfg.temperature,
            "max_output_tokens": cfg.max_output_tokens,
            "output_length_guidance": cfg.output_length_guidance,
            "csv": str(args.csv) if args.csv else None,
            "meta": str(args.meta),
            "previous_report": str(args.previous_report) if args.previous_report else None,
            "batch_reports": [str(p) for p in args.batch_reports] if args.batch_reports else [],
        },
    )

    save_text(run_dir / "prompts" / "used_prompt.txt", result["prompt"])
    save_text(run_dir / "outputs" / "report.md", result["report"])

    print(f"✅ 完了: {run_dir}")


if __name__ == "__main__":
    main()
