import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, List

import yaml
from dotenv import load_dotenv

from .logger import create_run_dir, save_json, save_text
from .pipeline import (
    RunConfig,
    run_hypothesis,
    run_initial,
    run_initial_auto,
    run_initial_part1,
    run_initial_part2,
    run_merge,
    run_update,
)
from .citation import CitationRegistry, expand_citations_to_links


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
    parser.add_argument("--source-dir", type=Path, required=False, help="ドキュメントフォルダのパス（pre_hypothesisで使用）")
    parser.add_argument("--meta", type=Path, default=Path("config/meta.yaml"), help="メタ情報 YAML/JSON")
    parser.add_argument("--mode", choices=["hypothesis", "initial", "initial_auto", "initial_part1", "initial_part2", "update", "merge", "pre_hypothesis_auto", "pre_hypothesis_iterative", "pubcom_analysis"], required=True)
    parser.add_argument("--previous-report", type=Path, help="UPDATE 用の前回レポート")
    parser.add_argument("--part1-report", type=Path, help="initial_part2 用の Part1 レポート")
    parser.add_argument("--batch-reports", type=Path, nargs="*", help="MERGE 用のレポートファイル群")
    parser.add_argument("--prompt-dir", type=Path, default=Path("prompts"))
    parser.add_argument("--model", default="gemini-flash-lite-latest")
    parser.add_argument("--temperature", type=float, default=0.3)
    parser.add_argument("--max-output-tokens", type=int, default=64000)
    parser.add_argument("--output-length-guidance", default="")
    parser.add_argument("--log-dir", type=Path, default=Path("doc"))
    parser.add_argument("--focus", type=str, default="", help="分析のフォーカス（主眼）。指定された場合、このテーマに関連しない内容は除外されます。")
    parser.add_argument("--comparison-model", type=str, default=None, help="pubcom_analysisの比較フェーズで使用するモデル")

    return parser.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()

    cfg = RunConfig(
        mode=args.mode,
        model=args.model,
        temperature=args.temperature,
        max_output_tokens=args.max_output_tokens,
        output_length_guidance=args.output_length_guidance,
        focus=args.focus,  # focus を設定
    )

    meta = load_meta(args.meta)
    prompt_dir: Path = args.prompt_dir

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
    elif cfg.mode == "initial_auto":
        if not args.csv:
            raise SystemExit("--csv を指定してください")
        result = run_initial_auto(prompt_dir, meta, args.csv, cfg)
    elif cfg.mode == "initial_part1":
        if not args.csv:
            raise SystemExit("--csv を指定してください")
        prompt_path = prompt_dir / "initial_part1.md"
        result = run_initial_part1(prompt_path, meta, args.csv, cfg)
    elif cfg.mode == "initial_part2":
        if not args.csv or not args.part1_report:
            raise SystemExit("--csv と --part1-report を指定してください")
        part1_report = read_text_file(args.part1_report)
        prompt_path = prompt_dir / "initial_part2.md"
        result = run_initial_part2(prompt_path, meta, args.csv, part1_report, cfg)
    elif cfg.mode == "update":
        if not args.csv or not args.previous_report:
            raise SystemExit("--csv と --previous-report を指定してください")
        previous_report = read_text_file(args.previous_report)
        prompt_path = prompt_dir / "initial.md" if not (prompt_dir / "update.md").exists() else prompt_dir / "update.md"
        result = run_update(prompt_path, meta, args.csv, previous_report, cfg)
    elif cfg.mode == "merge":
        if not args.batch_reports:
            raise SystemExit("--batch-reports を指定してください")
        prompt_path = prompt_dir / "merge.md"
        batch_reports = load_batch_reports(args.batch_reports)
        result = run_merge(prompt_path, meta, batch_reports, cfg)
    elif cfg.mode == "pre_hypothesis_auto":
        if not args.source_dir:
            raise SystemExit("--source-dir を指定してください")
        from .pipeline import run_pre_hypothesis_auto
        result = run_pre_hypothesis_auto(prompt_dir, meta, args.source_dir, cfg)
    elif cfg.mode == "pre_hypothesis_iterative":
        if not args.source_dir:
            raise SystemExit("--source-dir を指定してください")
        from .pipeline import run_pre_hypothesis_iterative
        result = run_pre_hypothesis_iterative(prompt_dir, meta, args.source_dir, cfg)
    elif cfg.mode == "pubcom_analysis":
        if not args.csv or not args.previous_report:
            raise SystemExit("--csv と --previous-report を指定してください")
        previous_report = read_text_file(args.previous_report)
        from .pipeline import run_pubcom_analysis
        result = run_pubcom_analysis(prompt_dir, meta, args.csv, previous_report, cfg, comparison_model=args.comparison_model)
    else:
        raise ValueError(f"Unknown mode: {cfg.mode}")

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
            "source_dir": str(args.source_dir) if args.source_dir else None,
            "meta": str(args.meta),
            "previous_report": str(args.previous_report) if args.previous_report else None,
            "part1_report": str(args.part1_report) if args.part1_report else None,
            "batch_reports": [str(p) for p in args.batch_reports] if args.batch_reports else [],
        },
    )

    save_text(run_dir / "prompts" / "used_prompt.txt", result["prompt"])
    save_text(run_dir / "outputs" / "report.md", result["report"])
    if "part1_log" in result:
        save_text(run_dir / "outputs" / "part1_log.md", result["part1_log"])

    # Citation Registry の保存
    if "citation_registry" in result:
        citation_registry: CitationRegistry = result["citation_registry"]
        save_json(run_dir / "outputs" / "citation_registry.json", citation_registry.to_dict())

        # URLリンク展開版レポートを生成
        report_with_links = expand_citations_to_links(result["report"], citation_registry)
        save_text(run_dir / "outputs" / "report_with_links.md", report_with_links)

    print(f"[OK] Complete: {run_dir}")


if __name__ == "__main__":
    main()
