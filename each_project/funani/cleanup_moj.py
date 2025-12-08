"""
法務省のメタデータから不要ファイルを削除するスクリプト
船荷証券・運送・海商関連以外のファイルをクリーンアップ
"""

import json
from pathlib import Path

SHINGIKAI_DIR = Path(__file__).parent / "shingikai"

# 必要なキーワード（これらを含むlink_textのファイルは保持）
REQUIRED_KEYWORDS = [
    "船荷",
    "運送",
    "海商",
]

def main():
    # 法務省のメタデータファイルを検索
    meta_files = list(SHINGIKAI_DIR.glob("metadata_moj.go.jp*.json"))
    
    if not meta_files:
        print("法務省のメタデータファイルが見つかりません")
        return
    
    total_deleted = 0
    kept_files = 0
    
    for meta_file in meta_files:
        print(f"処理中: {meta_file.name}")
        
        with open(meta_file, "r", encoding="utf-8") as f:
            metadata = json.load(f)
        
        for filename, file_data in metadata.get("files", {}).items():
            link_text = file_data.get("link_text", "")
            
            # 必要なキーワードを含む場合は保持
            is_required = any(keyword in link_text for keyword in REQUIRED_KEYWORDS)
            
            if is_required:
                kept_files += 1
                print(f"  保持: {filename} ({link_text[:40]})")
                continue
            
            # 不要なファイルを削除
            filepath = SHINGIKAI_DIR / filename
            if filepath.exists():
                print(f"  削除: {filename} ({link_text[:40] if link_text else 'リンクテキストなし'})")
                filepath.unlink()
                total_deleted += 1
    
    print(f"\n削除完了: {total_deleted}ファイル")
    print(f"保持: {kept_files}ファイル")

if __name__ == "__main__":
    main()
