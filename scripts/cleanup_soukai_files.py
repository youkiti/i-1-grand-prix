"""
第194〜200回以外の総会ファイルを削除するスクリプト
メタデータを参照し、page_titleやpage_urlに第190〜193回が含まれるファイルを削除
"""

import json
import os
from pathlib import Path

SHINGIKAI_DIR = Path("each_project/funani/shingikai")

# 削除対象の会議番号（全角）
MEETINGS_TO_DELETE = ["第１９０回", "第１９１回", "第１９２回", "第１９３回"]

# 保持対象の会議番号（確認用）
MEETINGS_TO_KEEP = ["第１９４回", "第１９５回", "第１９６回", "第１９７回", "第１９８回", "第１９９回", "第２００回"]

def main():
    files_to_delete = []
    files_to_keep = []
    
    # すべてのメタデータファイルを処理
    for meta_file in SHINGIKAI_DIR.glob("metadata_*.json"):
        with open(meta_file, "r", encoding="utf-8") as f:
            metadata = json.load(f)
        
        # 総会関連のメタデータのみ処理（soukai.htmlから）
        base_url = metadata.get("scrape_info", {}).get("base_url", "")
        if "shingikai_soukai" not in base_url:
            continue
        
        print(f"\n処理中: {meta_file.name}")
        print(f"  元ファイル数: {metadata['scrape_info']['total_files']}")
        
        files_info = metadata.get("files", {})
        
        for filename, file_data in files_info.items():
            page_title = file_data.get("page_title", "")
            page_url = file_data.get("page_url", "")
            link_text = file_data.get("link_text", "")
            
            # 削除対象かどうかを判定
            should_delete = False
            for meeting in MEETINGS_TO_DELETE:
                if meeting in page_title or meeting in page_url or meeting in link_text:
                    should_delete = True
                    break
            
            if should_delete:
                files_to_delete.append(filename)
            else:
                # 保持対象の会議に含まれているか確認
                is_kept = False
                for meeting in MEETINGS_TO_KEEP:
                    if meeting in page_title or meeting in page_url or meeting in link_text:
                        is_kept = True
                        break
                if is_kept:
                    files_to_keep.append(filename)
    
    print(f"\n削除対象ファイル数: {len(files_to_delete)}")
    print(f"保持対象ファイル数: {len(files_to_keep)}")
    
    # 削除実行
    deleted_count = 0
    for filename in files_to_delete:
        filepath = SHINGIKAI_DIR / filename
        if filepath.exists():
            print(f"  削除: {filename}")
            filepath.unlink()
            deleted_count += 1
        else:
            print(f"  見つからない: {filename}")
    
    print(f"\n削除完了: {deleted_count}ファイル")

if __name__ == "__main__":
    main()
