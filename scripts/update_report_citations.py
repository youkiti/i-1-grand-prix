#!/usr/bin/env python3
"""
既存レポートの出典情報を更新するスクリプト

メタデータファイルからlink_text/page_titleを読み込み、
レポート内のfilenameをより分かりやすい資料名に更新する。
"""
import json
import re
from pathlib import Path


def load_metadata(shingikai_dir: Path) -> dict:
    """メタデータファイルを読み込んでfilename->infoのマッピングを作成"""
    file_info = {}
    
    for meta_file in shingikai_dir.glob("metadata_*.json"):
        print(f"Loading metadata: {meta_file.name}")
        data = json.load(open(meta_file, encoding="utf-8"))
        
        for filename, info in data.get("files", {}).items():
            file_info[filename] = {
                "link_text": info.get("link_text", ""),
                "page_title": info.get("page_title", ""),
                "source_url": info.get("source_url", ""),
            }
    
    return file_info


def update_report_yaml(report_path: Path, file_info: dict) -> str:
    """レポートのYAMLメタデータセクションを更新"""
    content = report_path.read_text(encoding="utf-8")
    
    # source_documentsセクションを探して更新
    # filename行の後にtitle行を追加
    lines = content.split("\n")
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)
        
        # filename: "xxxx.pdf" を検出
        match = re.match(r'^(\s*)filename:\s*"([^"]+)"', line)
        if match:
            indent = match.group(1)
            filename = match.group(2)
            
            if filename in file_info:
                info = file_info[filename]
                link_text = info.get("link_text", "")
                page_title = info.get("page_title", "")
                
                # 次の行がtitleでなければ追加
                if i + 1 < len(lines) and not lines[i + 1].strip().startswith("title:"):
                    if link_text:
                        new_lines.append(f'{indent}title: "{link_text}"')
                    if page_title:
                        new_lines.append(f'{indent}source: "{page_title}"')
        
        i += 1
    
    return "\n".join(new_lines)


def update_citation_appendix(report_path: Path, file_info: dict) -> str:
    """レポートの出典一覧セクションを更新"""
    content = report_path.read_text(encoding="utf-8")
    
    # # 出典一覧 セクションを探す
    citation_start = content.find("# 出典一覧")
    if citation_start == -1:
        print("出典一覧セクションが見つかりません")
        return content
    
    # 審議会資料テーブルを探して更新
    # | D001 | filename | ... | を | D001 | title | source | ... | に変更
    
    def replace_citation_row(match):
        cite_id = match.group(1)
        filename = match.group(2)
        page = match.group(3)
        url = match.group(4)
        
        if filename in file_info:
            info = file_info[filename]
            title = info.get("link_text") or filename
            source = info.get("page_title") or "-"
            return f"| {cite_id} | {title} | {source} | {url} |"
        
        return match.group(0)
    
    # パターン: | D001 | filename.pdf | page | [リンク](...) |
    pattern = r'\|\s*(D\d+)\s*\|\s*([^\|]+)\s*\|\s*([^\|]+)\s*\|\s*([^\|]+)\s*\|'
    updated_content = re.sub(pattern, replace_citation_row, content)
    
    return updated_content


def main():
    shingikai_dir = Path("each_project/funani/shingikai")
    report_paths = [
        Path("doc/2025-12-13/run-163728/outputs/report.md"),
        Path("doc/2025-12-13/run-174907/outputs/report.md"),
    ]
    
    # メタデータ読み込み
    file_info = load_metadata(shingikai_dir)
    print(f"Loaded metadata for {len(file_info)} files")
    
    # サンプル表示
    for filename, info in list(file_info.items())[:3]:
        print(f"  {filename}: {info.get('link_text', '(no title)')}")
    
    # レポート更新
    for report_path in report_paths:
        if not report_path.exists():
            print(f"Skipping (not found): {report_path}")
            continue
        
        print(f"\nUpdating: {report_path}")
        
        # YAMLメタデータ更新
        updated = update_report_yaml(report_path, file_info)
        
        # 出典一覧更新
        updated = update_citation_appendix(Path(report_path), file_info)
        
        # バックアップ作成
        backup_path = report_path.with_suffix(".md.bak")
        if not backup_path.exists():
            report_path.rename(backup_path)
            print(f"  Backup created: {backup_path}")
        
        # 更新版を保存
        report_path.write_text(updated, encoding="utf-8")
        print(f"  Updated: {report_path}")


if __name__ == "__main__":
    main()
