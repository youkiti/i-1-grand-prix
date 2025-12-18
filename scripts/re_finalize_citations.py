
import sys
from pathlib import Path
import json

# Add src to path
sys.path.append(str(Path(__file__).parent.parent))

from src.interview_analysis.citation import CitationRegistry, finalize_report_citations

def main():
    # Paths for the latest run
    run_dir = Path("doc/2025-12-19/run-071009")
    report_path = run_dir / "outputs" / "report_pubcom_compare.md"
    stage1_dir = Path("doc/2025-12-18/run-201918")
    stage2_dir = Path("doc/2025-12-18/run-233041")
    
    if not report_path.exists():
        print(f"Report not found: {report_path}")
        return

    # Load Stage 1 & 2 registries
    registries = []
    reg1_path = stage1_dir / "outputs" / "citation_registry.json"
    if reg1_path.exists():
        registries.append(CitationRegistry.from_json(reg1_path.read_text(encoding="utf-8")))
        print(f"Loaded Stage 1 registry")
    
    reg2_path = stage2_dir / "outputs" / "citation_registry.json"
    if reg2_path.exists():
        registries.append(CitationRegistry.from_json(reg2_path.read_text(encoding="utf-8")))
        print(f"Loaded Stage 2 registry")

    # Load report content
    report_text = report_path.read_text(encoding="utf-8")
    
    # Use Stage 1 report as merged hypothesis
    stage1_report_path = stage1_dir / "outputs" / "report_pre_hypothesis_iterative.md"
    
    # Finalize
    print("Finalizing citations...")
    refined_report = finalize_report_citations(
        report_text=report_text,
        citation_registries=registries,
        merged_hypothesis_path=stage1_report_path
    )
    
    # Save
    out_path = run_dir / "outputs" / "report_pubcom_compare_with_references_FIXED.md"
    out_path.write_text(refined_report, encoding="utf-8")
    print(f"Done! Saved to {out_path}")

if __name__ == "__main__":
    main()
