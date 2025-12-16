"""CSVのroleカラムを集計するスクリプト"""
import csv
import sys
from collections import Counter
from pathlib import Path

csv.field_size_limit(2**31 - 1)

csv_path = Path("data/ai-plan-test_messages.csv")

if not csv_path.exists():
    print(f"Error: {csv_path} not found")
    sys.exit(1)

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Total rows: {len(rows)}")
print(f"Columns: {list(rows[0].keys()) if rows else 'N/A'}")
print()

roles = Counter(row.get('role', 'N/A') for row in rows)
print("Role values:")
for k, v in roles.most_common():
    print(f"  {repr(k)}: {v}")
