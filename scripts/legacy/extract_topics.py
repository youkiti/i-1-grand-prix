import re
import sys
from pathlib import Path

def extract_topics_section(input_path: str, output_path: str):
    print(f"Reading {input_path}...")
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    # topics: セクションを探す
    match = re.search(r'(topics:.*)', content, re.DOTALL)
    
    if match:
        extracted_content = match.group(1)
        
        # 末尾の ``` を削除（もしあれば）
        if extracted_content.strip().endswith("```"):
            extracted_content = extracted_content.strip()[:-3].strip()
            
        print(f"Found 'topics:' section. Writing to {output_path}...")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(extracted_content)
        print("Done.")
    else:
        print("Error: 'topics:' section not found in the input file.")
        
        # デバッグ: ファイルの先頭を表示
        print("Head of file:")
        print(content[:500])
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_topics.py <input_file> <output_file>")
        sys.exit(1)
    
    extract_topics_section(sys.argv[1], sys.argv[2])
