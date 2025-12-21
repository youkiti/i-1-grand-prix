import os
import glob
import datetime

root_dir = r"C:\Users\youki\codes\i-1-grand-prix\doc"
search_term = "船荷"
search_term2 = "Bill of Lading"

found_files = []

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.startswith("report") and file.endswith(".md"):
            filepath = os.path.join(root, file)
            try:
                mtime = os.path.getmtime(filepath)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if search_term in content or search_term2 in content:
                        found_files.append((filepath, mtime))
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

# Sort by mtime descending
found_files.sort(key=lambda x: x[1], reverse=True)

if found_files:
    latest_file = found_files[0][0]
    print(f"LATEST_REPORT: {latest_file}")
else:
    print("No matching reports found.")
