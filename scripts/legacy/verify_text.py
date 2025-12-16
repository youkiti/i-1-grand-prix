
import csv
import sys

csv_path = r'c:\Users\youki\codes\i-1-grand-prix\each_project\ai-plan-test\kokkai\diet_speeches.csv'
target_text = "海外のサービスを活用するだけではデジタル赤字がますます拡大します。ＡＩを日本の中で開発するための開発力の強化についても、政策として取り組んでいくことが重要です。"

# Normalize target text
normalized_target = target_text.replace(" ", "").replace("　", "").replace("\n", "")

try:
    with open(csv_path, 'r', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f)
        for index, row in enumerate(reader):
            message = str(row.get('message', ''))
            normalized_message = message.replace(" ", "").replace("　", "").replace("\n", "")
            
            if normalized_target in normalized_message:
                print(f"Match found in row {index} (message_id: {row.get('message_id', 'N/A')})")
                
                # Find start index in normalized string (approximate location in original)
                # Since mapping back from normalized to original is hard not impossible, 
                # I'll just remove newlines from original for display purposes to find the substring
                
                clean_message = message.replace("\n", "")
                # remove spaces for search but keep original for display is tricky.
                # Let's just fuzzy find or print the whole thing if typically short?
                # No, speech can be long.
                
                # Let's searching in the non-normalized simplified version
                # (keep spaces but remove newlines)
                clean_target = target_text.replace("\n", "")
                
                if clean_target in clean_message:
                     start_idx = clean_message.find(clean_target)
                     end_idx = start_idx + len(clean_target)
                     context_start = max(0, start_idx - 50)
                     context_end = min(len(clean_message), end_idx + 50)
                     print("Context:")
                     print("..." + clean_message[context_start:context_end] + "...")
                else:
                    # Fallback if exact match failing due to whitespace diffs
                    print("Exact whitespace match failed, but normalized match succeeded.")
                    print("Printing 200 chars from message:")
                    print(message[:200])
                break

except Exception as e:
    print(f"Error: {e}")
