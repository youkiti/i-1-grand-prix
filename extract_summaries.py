import re

files = [
    r"C:\Users\youki\codes\i-1-grand-prix\doc\2025-12-17\run-101807\outputs\report_pubcom_analysis_with_references.md",
    r"C:\Users\youki\codes\i-1-grand-prix\doc\2025-12-19\run-103551\outputs\report_pubcom_compare_with_references.md",
    r"C:\Users\youki\codes\i-1-grand-prix\doc\2025-12-19\run-054154\outputs\report_pubcom_compare_with_references.md"
]

def extract_summary(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        return f"Error reading {filepath}: {e}"

    # Get first 5 headers
    headers = [l.strip() for l in lines if l.startswith('#')][:5]
    
    # Get first 5 citations
    citations = []
    for l in lines:
        c = re.findall(r'\[(?:出典|パブコメ):?\s*([^\]]+)\]', l)
        if c:
            citations.extend(c)
        if len(citations) >= 5:
            break
            
    summary_text = ""
    # Look for "Analysis" or "Result" header and take following lines
    capture = False
    for l in lines:
        if re.search(r'##\s*(?:最終|分析|結論|Insight)', l):
            capture = True
        if capture:
            summary_text += l
            if len(summary_text) > 500:
                break
    
    return f"FILE: {filepath}\nHEADERS: {headers}\nCITATIONS: {citations}\nSUMMARY_SNIPPET:\n{summary_text}\n" + "="*40 + "\n"

for p in files:
    print(extract_summary(p))
