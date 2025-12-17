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
from .citation import CitationRegistry, expand_citations_to_links, finalize_report_citations


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
    parser.add_argument("--mode", choices=["hypothesis", "initial", "initial_auto", "initial_part1", "initial_part2", "update", "merge", "pre_hypothesis_auto", "pre_hypothesis_iterative", "pubcom_analysis", "pubcom_aggregate", "pubcom_compare"], required=True)
    parser.add_argument("--previous-report", type=Path, help="UPDATE 用の前回レポート")
    parser.add_argument("--part1-report", type=Path, help="initial_part2 用の Part1 レポート")
    parser.add_argument("--batch-reports", type=Path, nargs="*", help="MERGE 用のレポートファイル群")
    parser.add_argument("--prompt-dir", type=Path, default=Path("prompts"))
    parser.add_argument("--model", default="gemini-flash-lite-latest")
    parser.add_argument("--temperature", type=float, default=0.0, help="Map/Reduceフェーズの温度（デフォルト: 0.0）")
    parser.add_argument("--comparison-temperature", type=float, default=1.0, help="Comparisonフェーズの温度（デフォルト: 1.0）")
    parser.add_argument("--max-output-tokens", type=int, default=64000)
    parser.add_argument("--output-length-guidance", default="")
    parser.add_argument("--log-dir", type=Path, default=Path("doc"))
    parser.add_argument("--focus", type=str, default="", help="分析のフォーカス（主眼）。指定された場合、このテーマに関連しない内容は除外されます。")
    parser.add_argument("--comparison-model", type=str, default=None, help="pubcom_analysisの比較フェーズで使用するモデル")
    parser.add_argument("--max-map-batches", type=int, default=None, help="pubcom_analysis Map フェーズで1回の実行で処理する最大バッチ数（API クォータ管理用）")
    parser.add_argument("--pubcom-report", type=Path, default=None, help="pubcom_compare用: 集約済みパブコメレポートのパス")
    parser.add_argument("--prior-hypothesis", type=Path, default=None, help="pubcom_compare用: 事前仮説レポートのパス（--previous-reportと同義）")
    parser.add_argument("--merged-hypothesis", type=Path, default=None, help="引用ID解決用の統合仮説ファイル（オプション）")
    parser.add_argument("--thinking-level", type=str, default=None, choices=["low", "high"], help="Gemini 3モデルの思考レベル (low/high)")

    return parser.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()

    cfg = RunConfig(
        mode=args.mode,
        model=args.model,
        temperature=args.temperature,
        comparison_temperature=args.comparison_temperature,
        max_output_tokens=args.max_output_tokens,
        output_length_guidance=args.output_length_guidance,
        focus=args.focus,  # focus を設定
        thinking_level=args.thinking_level,  # Gemini 3 thinking level
    )

    meta = load_meta(args.meta)
    prompt_dir: Path = args.prompt_dir

    # 実行IDとディレクトリを先に作成（TokenTrackerのため）
    run_dir = create_run_dir(args.log_dir)
    print(f"Run directory created: {run_dir}")

    # TokenTracker 初期化
    from .token_tracker import TokenTracker
    TokenTracker.initialize(run_dir / "token_usage.jsonl")

    # Config保存（実行前に行う）
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
        # 前回のレポートと同階層にある citation_registry.json を探す
        prev_report_path = Path(args.previous_report)
        prev_registry_path = prev_report_path.parent / "citation_registry.json"
        prior_citation_registry = None
        if prev_registry_path.exists():
            try:
                from .citation import CitationRegistry
                prev_registry_data = json.loads(prev_registry_path.read_text(encoding="utf-8"))
                prior_citation_registry = CitationRegistry.from_dict(prev_registry_data)
                print(f"Loaded prior citation registry from {prev_registry_path} ({len(prior_citation_registry.citations)} items)")
            except Exception as e:
                print(f"[WARNING] Failed to load prior citation registry from {prev_registry_path}: {e}")

        # 前回のレポートと同階層にある token_usage.jsonl を探す
        prev_token_log_path = prev_report_path.parent.parent / "token_usage.jsonl"
        
        prior_token_stats = None
        if prev_token_log_path.exists():
            try:
                from .token_tracker import TokenTracker
                prior_token_stats = TokenTracker.get_summary(prev_token_log_path)
                print(f"Loaded prior token stats from {prev_token_log_path} ({len(prior_token_stats)} items)")
            except Exception as e:
                print(f"[WARNING] Failed to load prior token stats from {prev_token_log_path}: {e}")

        from .pipeline import run_pubcom_analysis
        result = run_pubcom_analysis(prompt_dir, meta, args.csv, previous_report, cfg, comparison_model=args.comparison_model, max_map_batches=args.max_map_batches, prior_citation_registry=prior_citation_registry, prior_token_stats=prior_token_stats)
    elif cfg.mode == "pubcom_aggregate":
        if not args.csv:
            raise SystemExit("--csv を指定してください")
        from .pipeline import run_pubcom_aggregate
        result = run_pubcom_aggregate(prompt_dir, meta, args.csv, cfg, max_map_batches=args.max_map_batches)
    elif cfg.mode == "pubcom_compare":
        # --pubcom-report と --prior-hypothesis (または --previous-report) が必要
        pubcom_report_path = args.pubcom_report
        prior_hypothesis_path = args.prior_hypothesis or args.previous_report
        if not pubcom_report_path or not prior_hypothesis_path:
            raise SystemExit("--pubcom-report と --prior-hypothesis (または --previous-report) を指定してください")
        pubcom_report = read_text_file(pubcom_report_path)
        prior_hypothesis = read_text_file(prior_hypothesis_path)
        
        # Load prior token stats from prior hypothesis and pubcom aggregate runs
        prior_token_stats_list = []
        
        # Stage 1: prior_hypothesis の token_usage.jsonl
        prior_hypo_token_path = Path(prior_hypothesis_path).parent.parent / "token_usage.jsonl"
        if prior_hypo_token_path.exists():
            try:
                from .token_tracker import TokenTracker
                stats = TokenTracker.get_summary(prior_hypo_token_path)
                prior_token_stats_list.append(("Stage 1 (事前仮説生成)", stats))
                print(f"Loaded Stage 1 token stats from {prior_hypo_token_path}")
            except Exception as e:
                print(f"[WARNING] Failed to load Stage 1 token stats: {e}")
        
        # Stage 2: pubcom_report の token_usage.jsonl
        pubcom_token_path = Path(pubcom_report_path).parent.parent / "token_usage.jsonl"
        if pubcom_token_path.exists():
            try:
                from .token_tracker import TokenTracker
                stats = TokenTracker.get_summary(pubcom_token_path)
                prior_token_stats_list.append(("Stage 2 (パブコメ集約)", stats))
                print(f"Loaded Stage 2 token stats from {pubcom_token_path}")
            except Exception as e:
                print(f"[WARNING] Failed to load Stage 2 token stats: {e}")
        
        from .pipeline import run_pubcom_compare
        result = run_pubcom_compare(prompt_dir, meta, pubcom_report, prior_hypothesis, cfg, comparison_model=args.comparison_model, prior_token_stats_list=prior_token_stats_list)
    else:
        raise ValueError(f"Unknown mode: {cfg.mode}")

    # 結果保存
    save_text(run_dir / "prompts" / "used_prompt.txt", result["prompt"])
    save_text(run_dir / "outputs" / f"report_{cfg.mode}.md", result["report"])
    if "part1_log" in result:
        save_text(run_dir / "outputs" / "part1_log.md", result["part1_log"])
    
    # パブコメ集約レポートの独立保存（再利用可能）
    if "pubcom_consolidated_report" in result:
        save_text(run_dir / "outputs" / "pubcom_report.md", result["pubcom_consolidated_report"])

    # Citation Registry の保存
    if "citation_registry" in result:
        citation_registry: CitationRegistry = result["citation_registry"]
        save_json(run_dir / "outputs" / "citation_registry.json", citation_registry.to_dict())

        # URLリンク展開版レポートを生成
        # finalize_report_citations を使用して、国会API連携や出典一覧生成を含む完全版を作成
        report_with_references = finalize_report_citations(
            result["report"], 
            [citation_registry], # finalize_report_citations expects a list
            merged_hypothesis_path=args.merged_hypothesis,
            merged_hypothesis_content=result.get("merged_hypothesis_content")  # pubcom_compare等から渡される
        )
        save_text(run_dir / "outputs" / f"report_{cfg.mode}_with_references.md", report_with_references)
        
        # Legacy support (optional, or just use references as links)
        # report_with_links = expand_citations_to_links(result["report"], citation_registry)
        # save_text(run_dir / "outputs" / "report_with_links.md", report_with_links)

    print(f"[OK] Complete: {run_dir}")


if __name__ == "__main__":
    main()
