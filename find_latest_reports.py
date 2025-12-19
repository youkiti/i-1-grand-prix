import os
import glob
import datetime

root_dir = r"C:\Users\youki\codes\i-1-grand-prix\doc"

targets = {
    "AI_PLAN": ["AI基本計画", "AI事業者ガイドライン", "AISI"],
    "TEISUU": ["定数削減", "議員定数", "小選挙区", "一票の格差"]
}

latest_reports = {}

print("Searching for reports...")

for topic, keywords in targets.items():
    found_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.startswith("report") and file.endswith(".md"):
                filepath = os.path.join(root, file)
                try:
                    # Quick check on filename/path first to avoid unrelated files if possible, 
                    # but keywords check is safer.
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        # Check if ANY keyword is in content
                        if any(k in content for k in keywords):
                            mtime = os.path.getmtime(filepath)
                            found_files.append((filepath, mtime))
                except Exception as e:
                    # Ignore errors
                    pass
    
    # Sort descending
    found_files.sort(key=lambda x: x[1], reverse=True)
    
    if found_files:
        latest = found_files[0][0]
        latest_reports[topic] = latest
        # print(f"LATEST {topic}: {latest}")
    else:
        # print(f"No report found for {topic}")
        latest_reports[topic] = "None"

with open("latest_reports_list.txt", "w", encoding="utf-8") as f:
    for topic, path in latest_reports.items():
        f.write(f"{topic}={path}\n")
print("Written to latest_reports_list.txt")

