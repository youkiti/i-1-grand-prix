"""
Citation Registry - 出典情報の管理と追跡

引用ID形式:
- 審議会資料: [D001], [D002], ... (Document)
- パブコメ: [P001], [P002], ... (Public Comment)

レジストリ構造:
{
    "D001": {
        "type": "document",
        "file": "第3回議事録.pdf",
        "page": 5,
        "url": "https://example.go.jp/doc/3rd.pdf",
        "page_title": "船荷証券電子化検討会",
        "link_text": "第3回議事録",
        "excerpt": "電子化により業務効率が30%向上すると試算"
    },
    "P001": {
        "type": "pubcom",
        "comment_id": "12345",
        "excerpt": "中小企業への配慮が必要"
    }
}
"""

import json
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple


@dataclass
class Citation:
    """引用情報"""
    cite_id: str  # D001, P001 など
    cite_type: str  # "document" or "pubcom"
    file: str = ""
    page: Optional[int] = None
    url: str = ""
    page_title: str = ""
    link_text: str = ""
    comment_id: str = ""
    excerpt: str = ""

    def to_dict(self) -> dict:
        return {k: v for k, v in asdict(self).items() if v}

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return cls(**data)


@dataclass
class CitationRegistry:
    """引用レジストリ"""
    citations: Dict[str, Citation] = field(default_factory=dict)
    _doc_counter: int = 0
    _pubcom_counter: int = 0

    def add_document(
        self,
        file: str,
        page: Optional[int] = None,
        url: str = "",
        page_title: str = "",
        link_text: str = "",
        excerpt: str = ""
    ) -> str:
        """ドキュメント引用を追加し、引用IDを返す"""
        self._doc_counter += 1
        cite_id = f"D{self._doc_counter:03d}"
        self.citations[cite_id] = Citation(
            cite_id=cite_id,
            cite_type="document",
            file=file,
            page=page,
            url=url,
            page_title=page_title,
            link_text=link_text,
            excerpt=excerpt
        )
        return cite_id

    def add_pubcom(
        self,
        comment_id: str,
        excerpt: str = ""
    ) -> str:
        """パブコメ引用を追加し、引用IDを返す"""
        self._pubcom_counter += 1
        cite_id = f"P{self._pubcom_counter:03d}"
        self.citations[cite_id] = Citation(
            cite_id=cite_id,
            cite_type="pubcom",
            comment_id=comment_id,
            excerpt=excerpt
        )
        return cite_id

    def get(self, cite_id: str) -> Optional[Citation]:
        """引用IDから引用情報を取得"""
        return self.citations.get(cite_id)

    def merge(self, other: "CitationRegistry") -> "CitationRegistry":
        """
        2つのレジストリをマージ

        他のレジストリの引用IDはリナンバリングされる
        戻り値: (マージ後のレジストリ, IDマッピング {旧ID: 新ID})
        """
        id_mapping = {}

        for old_id, citation in other.citations.items():
            if citation.cite_type == "document":
                new_id = self.add_document(
                    file=citation.file,
                    page=citation.page,
                    url=citation.url,
                    page_title=citation.page_title,
                    link_text=citation.link_text,
                    excerpt=citation.excerpt
                )
            else:  # pubcom
                new_id = self.add_pubcom(
                    comment_id=citation.comment_id,
                    excerpt=citation.excerpt
                )
            id_mapping[old_id] = new_id

        return id_mapping

    def to_dict(self) -> dict:
        """辞書形式に変換"""
        return {
            "citations": {k: v.to_dict() for k, v in self.citations.items()},
            "_doc_counter": self._doc_counter,
            "_pubcom_counter": self._pubcom_counter
        }

    def to_json(self, indent: int = 2) -> str:
        """JSON文字列に変換"""
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    @classmethod
    def from_dict(cls, data: dict) -> "CitationRegistry":
        """辞書から復元"""
        registry = cls()
        registry._doc_counter = data.get("_doc_counter", 0)
        registry._pubcom_counter = data.get("_pubcom_counter", 0)
        for cite_id, cite_data in data.get("citations", {}).items():
            registry.citations[cite_id] = Citation.from_dict(cite_data)
        return registry

    @classmethod
    def from_json(cls, json_str: str) -> "CitationRegistry":
        """JSON文字列から復元"""
        return cls.from_dict(json.loads(json_str))

    def save(self, path: Path) -> None:
        """ファイルに保存"""
        path.write_text(self.to_json(), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "CitationRegistry":
        """ファイルから読み込み"""
        return cls.from_json(path.read_text(encoding="utf-8"))


def load_scraper_metadata(folder_path: Path) -> Dict[str, dict]:
    """
    スクレイパーが生成したmetadata.jsonを読み込む

    Returns:
        {filename: metadata_dict} の辞書
    """
    metadata_path = folder_path / "metadata.json"
    if not metadata_path.exists():
        return {}

    with open(metadata_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get("files", {})


def build_document_header(filename: str, metadata: dict) -> str:
    """
    ドキュメント先頭に付与するメタデータヘッダーを構築

    出力例:
    [Document Info]
    - file: 第3回議事録.pdf
    - url: https://example.go.jp/doc/3rd.pdf
    - page_title: 船荷証券電子化検討会
    - link_text: 第3回議事録
    [/Document Info]
    """
    lines = ["[Document Info]"]
    lines.append(f"- file: {filename}")

    if metadata.get("source_url"):
        lines.append(f"- url: {metadata['source_url']}")
    if metadata.get("page_title"):
        lines.append(f"- page_title: {metadata['page_title']}")
    if metadata.get("link_text"):
        lines.append(f"- link_text: {metadata['link_text']}")
    if metadata.get("page_url"):
        lines.append(f"- page_url: {metadata['page_url']}")

    lines.append("[/Document Info]")
    return "\n".join(lines)


def remap_citations_in_text(text: str, id_mapping: Dict[str, str]) -> str:
    """
    テキスト内の引用IDをマッピングに従って置換

    例: [D001] → [D015] (マッピングに従って)
    """
    def replace_cite(match):
        old_id = match.group(1)
        new_id = id_mapping.get(old_id, old_id)
        return f"[{new_id}]"

    # [D001] や [P001] のパターンにマッチ
    pattern = r'\[([DP]\d{3})\]'
    return re.sub(pattern, replace_cite, text)


def expand_citations_to_links(text: str, registry: CitationRegistry) -> str:
    """
    テキスト内の引用をURLリンクに展開

    対応形式:
    - [D001] → [出典: ファイル名, p.X](URL)
    - [P001] → [パブコメ: コメントID]
    - [出典: ファイル名, p.X] → [出典: ファイル名, p.X](URL) (ファイル名がレジストリにある場合)
    """
    # まず [D001], [P001] 形式を処理
    def replace_cite_id(match):
        cite_id = match.group(1)
        citation = registry.get(cite_id)

        if not citation:
            return match.group(0)  # 見つからない場合はそのまま

        if citation.cite_type == "document":
            # ドキュメント引用
            label_parts = [f"出典: {citation.file}"]
            if citation.page:
                label_parts.append(f"p.{citation.page}")
            label = ", ".join(label_parts)

            if citation.url:
                return f"[{label}]({citation.url})"
            else:
                return f"[{label}]"
        else:
            # パブコメ引用
            return f"[パブコメ: {citation.comment_id}]"

    pattern_cite_id = r'\[([DP]\d{3})\]'
    text = re.sub(pattern_cite_id, replace_cite_id, text)

    # 次に従来形式 [出典: ファイル名, p.X] を処理
    # ファイル名→URLのマッピングを構築
    file_to_url = {}
    for citation in registry.citations.values():
        if citation.cite_type == "document" and citation.url:
            file_to_url[citation.file] = citation.url

    def replace_legacy_citation(match):
        full_match = match.group(0)
        filename = match.group(1).strip()
        page_part = match.group(2) if match.group(2) else ""

        # URLが存在するか確認
        url = file_to_url.get(filename)
        if url:
            # URLリンク形式に変換
            label = f"出典: {filename}"
            if page_part:
                label += f", {page_part}"
            return f"[{label}]({url})"
        else:
            # URLがない場合はそのまま
            return full_match

    # [出典: ファイル名, p.X] または [出典: ファイル名] にマッチ
    pattern_legacy = r'\[出典:\s*([^,\]\n]+)(?:,\s*(p\.\d+))?\]'
    text = re.sub(pattern_legacy, replace_legacy_citation, text)

    return text


def generate_citation_appendix(registry: CitationRegistry) -> str:
    """
    引用一覧（Appendix）を生成
    
    出力例:
    # 出典一覧
    
    ## 国会会議録
    | ID | 資料名 | URL | 日付 |
    |----|--------|-----|------|
    | kokkai_001 | 第217回国会 衆議院 内閣委員会 第14号 | [会議録](https://...) | 2025-04-16 |

    ## 審議会資料
    | ID | 資料名 | 審議会/出典 | URL |
    |----|--------|-------------|-----|
    | D001 | 第3回議事録 | 商事法務研究会（電子船荷証券） | [リンク](https://...) |

    ## パブリックコメント
    | ID | コメントID |
    |----|------------|
    | P001 | 12345 |
    """
    from .diet_api import fetch_meeting_meta

    doc_citations = []
    pubcom_citations = []
    kokkai_citations = []

    for cite_id, citation in sorted(registry.citations.items()):
        if citation.cite_type == "document":
            # Kokkai detection heuristic
            is_kokkai = False
            if "kokkai" in cite_id.lower():
                is_kokkai = True
            else:
                # Check for session_id format in filename
                # Formats: "121704889X01420250416", "2011-01-24_117705254X00120110124.txt"
                filename = citation.file
                if "_" in filename:
                    # Extract potential issue_id after the underscore
                    parts = filename.split("_")
                    for part in parts:
                        # Remove .txt if present
                        part_clean = part.replace(".txt", "")
                        if len(part_clean) >= 18 and "X" in part_clean and part_clean[0].isdigit():
                            is_kokkai = True
                            break
                elif len(filename) >= 20 and "X" in filename and filename[0].isdigit():
                    is_kokkai = True
            
            if is_kokkai:
                kokkai_citations.append(citation)
            else:
                doc_citations.append(citation)
        else:
            pubcom_citations.append(citation)

    lines = ["# 出典一覧\n"]

    if kokkai_citations:
        lines.append("## 国会会議録\n")
        lines.append("| ID | 資料名 | URL | 日付 |")
        lines.append("|----|--------|-----|------|")
        
        for c in kokkai_citations:
            # Try to resolve session_id from file or extract it
            session_id = None
            # If the filename itself is the session ID or contains it
            filename = c.file
            if len(filename) >= 20 and "X" in filename:
                # Extract issue_id from various formats:
                # - "117705254X00120110124" (just the ID)
                # - "2011-01-24_117705254X00120110124.txt" (date prefix + ID + extension)
                # - "117705254X00120110124.txt" (ID + extension)
                
                # Remove .txt extension if present
                if filename.endswith(".txt"):
                    filename = filename[:-4]
                
                # Check for date prefix pattern: YYYY-MM-DD_
                if "_" in filename:
                    parts = filename.split("_")
                    # Take the part that contains 'X' (the issue_id)
                    for part in parts:
                        if "X" in part and len(part) >= 18:
                            session_id = part
                            break
                else:
                    session_id = filename
            
            display_title = c.link_text if c.link_text else c.file
            url_str = f"[リンク]({c.url})" if c.url else "-"
            date_str = "-"
            
            if session_id:
                meta = fetch_meeting_meta(session_id)
                if meta:
                    # Construct detailed name
                    display_title = f"{meta.get('house', '')} {meta.get('meeting_name', '')} 第{meta.get('meeting_number', '')}号 (第{meta.get('session')}回国会)"
                    
                    if meta.get('date'):
                        date_str = meta.get('date')
                    
                    if meta.get('page_url'):
                        url_str = f"[会議録]({meta.get('page_url')})"

            lines.append(f"| {c.cite_id} | {display_title} | {url_str} | {date_str} |")

        lines.append("")

    if doc_citations:
        lines.append("## 審議会資料\n")
        lines.append("| ID | 資料名 | 審議会/出典 | URL |")
        lines.append("|----|--------|-------------|-----|")
        for c in doc_citations:
            # 資料名: link_text > file をフォールバック
            title = c.link_text if c.link_text else c.file
            # 審議会名: page_title を使用
            source = c.page_title if c.page_title else "-"
            url_str = f"[リンク]({c.url})" if c.url else "-"
            lines.append(f"| {c.cite_id} | {title} | {source} | {url_str} |")
        lines.append("")

    if pubcom_citations:
        lines.append("## パブリックコメント\n")
        lines.append("| ID | コメントID |")
        lines.append("|----+------------|")
        for c in pubcom_citations:
            lines.append(f"| {c.cite_id} | {c.comment_id} |")
        lines.append("")

    return "\n".join(lines)


def parse_legacy_citation(text: str) -> List[Tuple[str, Optional[int]]]:
    """
    従来形式の引用をパース

    [出典: ファイル名, p.X] → [("ファイル名", X)]
    [パブコメ: ID] → [("ID", None)]
    """
    results = []

    # [出典: ファイル名, p.X] パターン
    doc_pattern = r'\[出典:\s*([^,\]]+)(?:,\s*p\.(\d+))?\]'
    for match in re.finditer(doc_pattern, text):
        filename = match.group(1).strip()
        page = int(match.group(2)) if match.group(2) else None
        results.append(("document", filename, page))

    # [パブコメ: ID] パターン
    pubcom_pattern = r'\[パブコメ:\s*([^\]]+)\]'
    for match in re.finditer(pubcom_pattern, text):
        comment_id = match.group(1).strip()
        results.append(("pubcom", comment_id, None))

    return results


def finalize_report_citations(
    report_text: str,
    citation_registries: List[CitationRegistry],
    merged_hypothesis_path: Optional[Path] = None
) -> str:
    """
    レポートの引用を最終化する（一般化されたロジック）
    
    1. 複数のレジストリを統合
    2. merged_hypothesis.md があればスキャンしてID解決
    3. 国会会議録APIでメタデータをエンリッチ
    4. 本文中の [出典: ...] をリンクに変換
    5. 出典一覧（Appendix）を生成して付与
    """
    from .diet_api import fetch_meeting_meta

    # 1. Merge Registries
    citation_map = {}
    
    # helper to add to map
    def add_to_map(c_data):
        # ID, File, LinkText map
        cid = c_data.get("cite_id")
        if cid: citation_map[cid] = c_data
        
        filename = c_data.get("file")
        if filename:
            citation_map[filename] = c_data
            citation_map[filename.replace(".txt", "")] = c_data
            
        link_text = c_data.get("link_text")
        if link_text:
            citation_map[link_text] = c_data

    for reg in citation_registries:
        data = reg.to_dict()
        for cid, c in data.get("citations", {}).items():
            add_to_map(c)

    # 2. Scan merged_hypothesis.md for ID -> Filename mapping
    if merged_hypothesis_path and merged_hypothesis_path.exists():
        print(f"Scanning {merged_hypothesis_path} for ID mappings...")
        mh_content = merged_hypothesis_path.read_text(encoding="utf-8")
        matches = re.findall(r'source_doc_id:\s*"([^"]+)"\s*\n\s*source_filename:\s*"([^"]+)"', mh_content)
        
        id_to_filename = {doc_id: filename for doc_id, filename in matches}
        
        for doc_id, filename in id_to_filename.items():
            if doc_id not in citation_map:
                 # Try to find info for filename
                 key_candidates = [filename, filename.replace(".txt", "")]
                 found_info = None
                 for k in key_candidates:
                     if k in citation_map:
                         found_info = citation_map[k]
                         break
                 
                 if found_info:
                     citation_map[doc_id] = found_info.copy()
                     citation_map[doc_id]["cite_id"] = doc_id # Override ID for lookup
                 else:
                     # Create a dummy info if not in registry (fallback)
                     citation_map[doc_id] = {
                         "cite_id": doc_id,
                         "file": filename,
                         "cite_type": "kokkai" if "X" in filename else "shingikai", # heuristic
                         "link_text": f"{filename} (ID: {doc_id})"
                     }
                     add_to_map(citation_map[doc_id])

    # Cache for API calls within this execution
    meta_cache = {}

    def get_meta(issue_id):
        if issue_id in meta_cache:
            return meta_cache[issue_id]
        try:
            print(f"Fetching meta for {issue_id}...")
            meta = fetch_meeting_meta(issue_id)
            meta_cache[issue_id] = meta
            return meta
        except Exception as e:
            print(f"Error fetching meta for {issue_id}: {e}")
            return None

    used_citations = {} # id -> info
    used_pubcoms = set()

    def replace_citation(match):
        full_text = match.group(0)
        content_inner = match.group(1).strip()
        
        # Direct match or Map lookup
        info = citation_map.get(content_inner)
        
        # Fuzzy match strategies
        if not info:
             clean_inner = content_inner.replace(".txt", "")
             if clean_inner in citation_map:
                 info = citation_map[clean_inner]
             else:
                 # Try matching by checking if content_inner is part of filename
                 # Only if content_inner is long enough to be unique
                 for k, v in citation_map.items():
                     if len(k) > 10 and (k in content_inner or content_inner in k):
                         info = v
                         break
        
        # If still no info but looks like Kokkai file
        if not info and re.match(r'\d{4}-\d{2}-\d{2}_\d+X', content_inner):
            filename = content_inner if content_inner.endswith(".txt") else content_inner + ".txt"
            info = {
                "cite_id": content_inner,
                "file": filename,
                "cite_type": "kokkai",
                "url": f"https://kokkai.ndl.go.jp/txt/{filename.split('_')[-1].replace('.txt','')}" 
            }

        if info:
            # Use original ID as key for uniqueness in table
            used_citations[info.get("cite_id", content_inner)] = info
            
            page_title = info.get("page_title", "")
            link_text = info.get("link_text", "")
            filename = info.get("file", "")
            url = info.get("url")
            
            # Title Logic
            generic_terms = ["議事概要", "答申", "参考資料", "説明", "委員名簿", "協議員名簿", "設置要綱"]
            title = link_text or page_title or filename
            
            if link_text and page_title:
                if any(term == link_text.strip() for term in generic_terms):
                    title = f"{page_title} {link_text}"
                elif len(link_text) < 10 and page_title not in link_text:
                    title = f"{page_title} {link_text}"

            # Enrich Kokkai Information
            is_kokkai = "kokkai" in info.get("cite_type", "") or \
                        "diet" in str(info.get("file", "")).lower() or \
                        re.search(r'\d+X\d+', str(info.get("file", "")))
            
            if is_kokkai:
                file_val = info.get("file", "")
                issue_id = None
                
                match_id = re.search(r'_(\d+X\d+)', file_val)
                if match_id:
                    issue_id = match_id.group(1)
                elif "X" in file_val:
                     # fallback logic
                     issue_id = file_val.replace(".txt", "")
                
                if issue_id:
                     meta = get_meta(issue_id)
                     if meta:
                         date_str = meta.get('date', "")
                         house = meta.get('house', "")
                         meeting = meta.get('meeting_name', "")
                         
                         title = f"{house} {meeting} ({date_str})"
                         if meta.get('page_url'):
                             url = meta.get('page_url')
            
            # Save for appendix
            info["display_title"] = title
            info["display_url"] = url
            
            if url:
                return f"[{title}]({url})"
            else:
                return f"[{title}]"
        
        return full_text

    # Replace [出典: ...]
    new_content = re.sub(r'\[出典:\s*([^\]]+)\]', replace_citation, report_text)
    
    # Replace bare filenames [YYYY-MM-DD_...X...]
    def replace_bare_citation(match):
        content_inner = match.group(1).strip()
        class MockMatch:
            def group(self, i):
                return f"[出典: {content_inner}]" if i == 0 else content_inner
        return replace_citation(MockMatch())

    new_content = re.sub(r'\[(\d{4}-\d{2}-\d{2}_\d+X[^\]]+)\]', replace_bare_citation, new_content)

    # Collect Pubcoms
    def replace_pubcom(match):
        pid = match.group(1).strip()
        used_pubcoms.add(pid)
        return match.group(0)
    
    new_content = re.sub(r'\[パブコメ:\s*([^\]]+)\]', replace_pubcom, new_content)
    
    # Generate Appendix
    appendix = "\n\n---\n\n# 出典一覧\n\n"
    
    if used_citations:
        appendix += "## 審議会・国会資料\n"
        appendix += "| ID | 資料名 / 会議名 | リンク |\n"
        appendix += "|----|-----------------|--------|\n"
        
        sorted_citations = sorted(used_citations.values(), key=lambda x: str(x.get("cite_id", "")))
        
        for info in sorted_citations:
            cid = info.get("cite_id")
            title = info.get("display_title") or info.get("link_text") or info.get("file")
            url = info.get("display_url") or info.get("url")
            
            url_str = f"[Link]({url})" if url else "-"
            # Ensure title is string
            if not title: title = "(No Title)"
            appendix += f"| {cid} | {title} | {url_str} |\n"
            
    if used_pubcoms:
        appendix += "\n## 引用されたパブリックコメント\n"
        appendix += "| コメントID |\n"
        appendix += "|------------|\n"
        for pid in sorted(used_pubcoms):
             appendix += f"| {pid} |\n"

    return new_content + appendix
