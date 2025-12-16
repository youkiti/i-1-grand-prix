
import sys
from pathlib import Path
import json

# Add src to path
sys.path.append(str(Path(__file__).parent.parent))

from src.interview_analysis.citation import CitationRegistry, finalize_report_citations

def test_enrichment():
    print("Testing citation enrichment...")
    
    # Mock Registry
    registry = CitationRegistry()
    registry.add_document(
        file="test_doc.pdf",
        page_title="Test Council",
        link_text="議事概要",
        url="http://example.com/test.pdf"
    )
    registry.add_pubcom("test-comment-id-123")
    
    # Mock Report Text
    report_text = """
    Test Report
    
    > Quote [出典: D001]
    
    > Another quote [出典: 2011-01-24_117715254X00120110124]
    
    > Pubcom [パブコメ: test-comment-id-123]
    """
    
    # Run
    enriched = finalize_report_citations(report_text, [registry], merged_hypothesis_path=None)
    
    print("Enriched Report Preview:")
    print(enriched)
    
    # Assertions
    assert "Test Council 議事概要" in enriched, "Generic title expansion failed"
    assert "出典一覧" in enriched, "Appendix generation failed"
    # Note: 2011-01-24... might fail if API fails or network issue, but logic should handle it gracefully
    print("Test Passed!")

if __name__ == "__main__":
    test_enrichment()
