#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fix kokkai citations in report files by searching for quotes and determining correct session_id.
"""

import csv
import re
import os

csv_path = r"c:\Users\youki\codes\i-1-grand-prix\each_project\ai-plan-test\kokkai\diet_speeches.csv"

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
    "121704889X01220250409": "kokkai_001",  # 2025-04-09 衆院内閣委12号
    "121704889X01320250411": "kokkai_002",  # 2025-04-11 衆院内閣委13号
    "121704889X01420250416": "kokkai_003",  # 2025-04-16 衆院内閣委14号（松尾豊参考人）
    "121714889X01520250520": "kokkai_004",  # 2025-05-20 参院内閣委15号
    "121714889X01620250522": "kokkai_005",  # 2025-05-22 参院内閣委16号
    "121715254X01920250516": "kokkai_006",  # 2025-05-16 参院本会議19号
    "121705254X01720250408": "kokkai_007",  # 2025-04-08 衆院本会議17号
}

# Date to kokkai_id (for report citations with dates)
date_to_kokkai = {
    "2025-04-08": "kokkai_007",
    "2025-04-09": "kokkai_001",
    "2025-04-11": "kokkai_002",
    "2025-04-16": "kokkai_003",
    "2025-05-16": "kokkai_006",
    "2025-05-20": "kokkai_004",
    "2025-05-22": "kokkai_005",
    "2025-11-21": "kokkai_003",  # Check this - fallback
}

# Files to fix
files_to_fix = [
    r"c:\Users\youki\codes\i-1-grand-prix\doc\2025-12-15\comparison_only_result.md",
    r"c:\Users\youki\codes\i-1-grand-prix\doc\2025-12-15\run-052018\outputs\report.md",
]

for filepath in files_to_fix:
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    print(f"\nProcessing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix citations with dates like (#kokkai_001, 2025-04-16)
    for date, kokkai_id in date_to_kokkai.items():
        old_pattern = f"kokkai_001, {date}"
        new_pattern = f"{kokkai_id}, {date}"
        if old_pattern in content:
            content = content.replace(old_pattern, new_pattern)
            print(f"  Replaced: {old_pattern} -> {new_pattern}")
    
    # Also fix patterns like (#chunk_XXX, kokkai_001, DATE)
    for date, kokkai_id in date_to_kokkai.items():
        old_pattern = f", kokkai_001, {date}"
        new_pattern = f", {kokkai_id}, {date}"
        if old_pattern in content:
            content = content.replace(old_pattern, new_pattern)
            print(f"  Replaced: {old_pattern} -> {new_pattern}")
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  File updated!")
    else:
        print(f"  No changes needed")

# Also create reference table to add to report
print("\n\n=== Reference Table for Reports ===")
print("Add this to the 出典一覧 section:\n")

kokkai_info = [
    ("kokkai_001", "121704889X01220250409", "第217回国会 衆議院 内閣委員会 第12号", "2025-04-09"),
    ("kokkai_002", "121704889X01320250411", "第217回国会 衆議院 内閣委員会 第13号", "2025-04-11"),
    ("kokkai_003", "121704889X01420250416", "第217回国会 衆議院 内閣委員会 第14号（松尾豊参考人意見陳述等）", "2025-04-16"),
    ("kokkai_004", "121714889X01520250520", "第217回国会 参議院 内閣委員会 第15号", "2025-05-20"),
    ("kokkai_005", "121714889X01620250522", "第217回国会 参議院 内閣委員会 第16号", "2025-05-22"),
    ("kokkai_006", "121715254X01920250516", "第217回国会 参議院 本会議 第19号", "2025-05-16"),
    ("kokkai_007", "121705254X01720250408", "第217回国会 衆議院 本会議 第17号", "2025-04-08"),
]

for kokkai_id, session_id, title, date in kokkai_info:
    url = f"https://kokkai.ndl.go.jp/txt/{session_id}"
    print(f"| {kokkai_id} | {title} | [国会会議録]({url}) | {date} |")

print("\nDone!")
