import re
from pathlib import Path

mh = Path('doc/2025-12-19/run-075827/outputs/merged_hypothesis.md').read_text(encoding='utf-8')

# Test new regex with URL prioritization
topic_blocks = re.split(r'(?=\s*-\s*id:\s*["\']?topic_)', mh)
print(f"Found {len(topic_blocks)} blocks")

topic_url_map = {}
for block in topic_blocks:
    topic_id_match = re.search(r'id:\s*["\']?(topic_\d+)["\']?', block)
    if topic_id_match:
        topic_id = topic_id_match.group(1)
        url_match = re.search(r'source_url:\s*["\']?(https?://[^\s"\'\n]+)', block)
        if url_match:
            # Always update if we find a URL (prioritize entries with URLs)
            topic_url_map[topic_id] = url_match.group(1)
        elif topic_id not in topic_url_map:
            topic_url_map[topic_id] = ""

print(f"Found {len(topic_url_map)} topics:")
has_url = sum(1 for v in topic_url_map.values() if v)
print(f"  With URL: {has_url}, Without: {len(topic_url_map) - has_url}")
for tid, url in list(topic_url_map.items())[:5]:
    print(f"  {tid}: {url[:60] if url else 'NO_URL'}...")
