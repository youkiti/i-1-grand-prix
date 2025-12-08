"""
商事法務研究会のメタデータから不要ファイルを削除するスクリプト
船荷証券電子化研究会（denshika-funani）以外のURLからのファイルをクリーンアップ
"""

import json
from pathlib import Path

SHINGIKAI_DIR = Path(__file__).parent / "shingikai"

# 必要なURL（このパスを含むURLからのファイルは保持）
REQUIRED_URL_PATTERNS = [
    "denshika-funani",  # 電子化研究会資料
]

def main():
    # 商事法務研究会のメタデータファイルを検索
    meta_files = list(SHINGIKAI_DIR.glob("metadata_shojihomu*.json"))
    
    if not meta_files:
        print("商事法務研究会のメタデータファイルが見つかりません")
        return
    
    total_deleted = 0
    kept_files = 0
    
    for meta_file in meta_files:
        print(f"処理中: {meta_file.name}")
        
        with open(meta_file, "r", encoding="utf-8") as f:
            metadata = json.load(f)
        
        for filename, file_data in metadata.get("files", {}).items():
            page_url = file_data.get("page_url", "")
            
            # 必要なURLパターンを含む場合は保持
            is_required = any(pattern in page_url for pattern in REQUIRED_URL_PATTERNS)
            
            if is_required:
                kept_files += 1
                continue
            
            # 不要なファイルを削除
            filepath = SHINGIKAI_DIR / filename
            if filepath.exists():
                print(f"  削除: {filename} (from {page_url})")
                filepath.unlink()
                total_deleted += 1
    
    print(f"\n削除完了: {total_deleted}ファイル")
    print(f"保持: {kept_files}ファイル")

if __name__ == "__main__":
    main()
