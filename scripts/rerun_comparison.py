"""
Re-run pubcom comparison phase only (to regenerate report with filtered citations)
"""
import json
import sys
from pathlib import Path
from datetime import datetime

# Add src to path (run from project root)
sys.path.insert(0, ".")

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

from src.interview_analysis.pipeline import (
    build_context, load_and_render, RunConfig, _call_model, 
    _build_combined_metadata, _build_process_metadata, _extract_prior_process_metadata,
    merge_prior_hypothesis_yamls
)
from src.interview_analysis.citation import CitationRegistry, generate_citation_appendix
from src.interview_analysis.token_tracker import TokenTracker

# Configuration
run_dir = Path("doc/2025-12-17/run-101807")
prior_report_path = Path("doc/2025-12-16/run-114126/outputs/report_pre_hypothesis_iterative.md")
pubcom_report_path = run_dir / "outputs/pubcom_report.md"
citation_registry_path = run_dir / "outputs/citation_registry.json"
output_path = run_dir / "outputs/report_pubcom_analysis.md"
meta_path = Path("each_project/funani/meta.yaml")
prompt_dir = Path("prompts")

# Load meta
import yaml
with open(meta_path, 'r', encoding='utf-8') as f:
    meta = yaml.safe_load(f)

# Load reports
prior_report = prior_report_path.read_text(encoding='utf-8')
pubcom_report = pubcom_report_path.read_text(encoding='utf-8')

# Load citation registry
citation_registry = CitationRegistry.from_json(citation_registry_path.read_text(encoding='utf-8'))

# Build context
focus = "電子船荷証券"
output_length_guidance = ""

merged_prior_hypothesis = merge_prior_hypothesis_yamls(prior_report)

ctx = {
    "projectName": meta.get("研究会名", ""),
    "discussionPoints": meta.get("主要論点", ""),
    "sessionsSummary": "",
    "sessionsDetail": "",
    "outputLengthGuidance": output_length_guidance,
    "priorHypothesis": merged_prior_hypothesis,
    "pubcomReport": pubcom_report,
    "focus": focus
}

# Load and render prompt
compare_prompt_path = prompt_dir / "pubcom_comparison.md"
compare_prompt = load_and_render(compare_prompt_path, ctx)

# Build config
cfg = RunConfig(
    mode="pubcom_analysis",
    model="gemini-3-pro-preview",  # Use flash for comparison
    temperature=1,  # comparison_temperature
    comparison_temperature=1,
    max_output_tokens=64000,
    top_p=0.95,
    top_k=64,
    output_length_guidance=output_length_guidance,
    focus=focus
)

print("Running comparison phase...")
print(f"Model: {cfg.model}")
print(f"Temperature: {cfg.temperature}")

# Call model
final_insight = _call_model(compare_prompt, cfg, step_name="pubcom_compare")

print(f"Comparison output length: {len(final_insight)} chars")

# Generate citation appendix (using finalize_report_citations for robust linking)
from src.interview_analysis.citation import finalize_report_citations

# Use prior_report_path as merged_hypothesis_path since it contains the source info
final_report_content = finalize_report_citations(
    report_text=final_insight,
    citation_registries=[citation_registry],
    merged_hypothesis_path=prior_report_path
)

print(f"Final report length: {len(final_report_content)} chars")

# Token stats
token_stats = TokenTracker.get_summary()
token_stats_md = "\n\n# Token Usage Statistics\n\n| Process / Step | Model | Input Tokens | Output Tokens | Est. Cost (USD) |\n| :--- | :--- | ---: | ---: | ---: |\n"

total_input = 0
total_output = 0
total_cost = 0.0

for key in sorted(token_stats.keys()):
    stats = token_stats[key]
    model_name = stats.get("model", "unknown")
    cost = stats.get("cost", 0.0)
    
    token_stats_md += f"| {key} | {model_name} | {stats['input_tokens']:,} | {stats['output_tokens']:,} | ${cost:,.2f} |\n"
    
    total_input += stats.get('input_tokens', 0)
    total_output += stats.get('output_tokens', 0)
    total_cost += cost

token_stats_md += f"| **TOTAL** | | **{total_input:,}** | **{total_output:,}** | **${total_cost:,.2f}** |\n"

# Build metadata
now = datetime.now()
metadata_header = f"""---
# 実験メタ情報
- 実行日時: {now.strftime('%Y-%m-%d %H:%M:%S')} (Compare再実行)
- モード: pubcom_analysis (Comparisonのみ再実行)
- モデル: {cfg.model}
- 温度: {cfg.temperature}
---

"""

# Build final report
# finalize_report_citations already includes the appendix and replaced links
final_report = final_report_content + "\n\n" + token_stats_md + "\n\n" + metadata_header

# Save
output_path.write_text(final_report, encoding='utf-8')
print(f"\nReport saved to: {output_path}")
print(f"Report size: {len(final_report):,} chars")

# Count citations in appendix (simple check)
doc_count = final_report.count("| D") + final_report.count("| 20") # approximate
pubcom_count = final_report.count("| P")
print(f"Report generated with updated citations.")
