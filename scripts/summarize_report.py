import os
from pathlib import Path
from dotenv import load_dotenv
from src.interview_analysis.model_provider import create_provider, ModelConfig

def main():
    load_dotenv()
    
    report_path = Path(r"c:\Users\youki\codes\i-1-grand-prix\doc\2025-12-04\run-141624\outputs\report.md")
    output_path = report_path.parent / "summary.md"
    
    print(f"Reading report from: {report_path}")
    content = report_path.read_text(encoding="utf-8")
    
    # Use Grok-4.1-fast as requested
    model_name = "x-ai/grok-4.1-fast"
    print(f"Summarizing using model: {model_name}")
    
    provider = create_provider(model_name)
    config = ModelConfig(
        model=model_name,
        temperature=0.3,
        max_output_tokens=8000
    )
    
    prompt = f"""
以下のレポートを要約してください。
**「船荷証券に関わる法制度の改正に寄与するQ&A」**に焦点を当ててまとめてください。
会議体の運営（委員の選任、リモート開催ルール、議事録公開など）に関する内容は**除外**してください。

重要な論点（発行、効力、電子化の技術要件、強制執行など）、新たな仮説、懸念点を中心に、構造化してまとめてください。

---
{content}
"""
    
    try:
        summary = provider.generate(prompt, config)
        
        print(f"Writing summary to: {output_path}")
        output_path.write_text(summary, encoding="utf-8")
        print("Done!")
        
    except Exception as e:
        print(f"Error during summarization: {e}")

if __name__ == "__main__":
    main()
