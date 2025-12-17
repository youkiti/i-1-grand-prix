import re
from pathlib import Path

path = Path("doc/2025-12-16/run-114126/outputs/report_pre_hypothesis_iterative.md")
content = path.read_text(encoding="utf-8")

# Original regex (known to work for ID/File)
regex_orig = r'source_doc_id:\s*"([^"]+)"\s*\n\s*source_filename:\s*"([^"]+)"'
matches_orig = re.findall(regex_orig, content)
print(f"Original regex matches: {len(matches_orig)}")

# New regex
regex_new = r'source_doc_id:\s*"([^"]+)"\s*\n\s*source_filename:\s*"([^"]+)"(?:\s*\n\s*source_url:\s*"([^"]+)")?'
matches_new = re.findall(regex_new, content)
print(f"New regex matches: {len(matches_new)}")

# Check specifically for the diji file
for m in matches_new:
    if "diji" in m[1]:
        print(f"Found diji: {m}")

# Print first few matches to see what's happening
print("First 5 new matches:")
for i, m in enumerate(matches_new[:5]):
    print(m)
