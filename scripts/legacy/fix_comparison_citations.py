#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fix comparison_only_result.md by finding each quote in CSV and assigning correct kokkai_XXX
"""

import csv
import re
import os

csv_path = r"c:\Users\youki\codes\i-1-grand-prix\each_project\ai-plan-test\kokkai\diet_speeches.csv"
report_path = r"c:\Users\youki\codes\i-1-grand-prix\doc\2025-12-15\comparison_only_result.md"

# Load CSV
print("Loading CSV...")
csv_data = []
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        csv_data.append(row)

def find_session_id(quote_fragment):
    """Find session_id for a quote fragment"""
    for row in csv_data:
        if quote_fragment in row['message']:
            return row['session_id']
    return None

# Session ID to kokkai_XXX mapping
session_to_kokkai = {
    "121704889X01220250409": "kokkai_001",  # 2025-04-09
    "121704889X01320250411": "kokkai_002",  # 2025-04-11
    "121704889X01420250416": "kokkai_003",  # 2025-04-16
    "121714889X01520250520": "kokkai_004",  # 2025-05-20
    "121714889X01620250522": "kokkai_005",  # 2025-05-22
    "121715254X01920250516": "kokkai_006",  # 2025-05-16
    "121705254X01720250408": "kokkai_007",  # 2025-04-08
}

# Read the report
with open(report_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all quotes with [出典: kokkai_001]
pattern = r'「([^」]+)」\s*\[出典: kokkai_001\]'
matches = list(re.finditer(pattern, content))

print(f"Found {len(matches)} quotes with [出典: kokkai_001]")

replacements = []
for match in matches:
    quote = match.group(1)
    full_match = match.group(0)
    
    # Try to find session_id using parts of the quote
    # Use first 30 chars as search key
    search_key = quote[:min(30, len(quote))]
    session_id = find_session_id(search_key)
    
    if not session_id:
        # Try with different part of quote
        search_key = quote[10:40] if len(quote) > 40 else quote
        session_id = find_session_id(search_key)
    
    if session_id:
        kokkai_id = session_to_kokkai.get(session_id, "kokkai_001")
        new_text = f"「{quote}」 [出典: {kokkai_id}]"
        replacements.append((full_match, new_text, kokkai_id))
        print(f"Quote: {quote[:50]}... -> {kokkai_id}")
    else:
        print(f"NOT FOUND: {quote[:50]}...")

# Apply replacements
for old, new, kokkai_id in replacements:
    content = content.replace(old, new)
    
# Save
with open(report_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nUpdated {len(replacements)} citations")
print("Done!")
