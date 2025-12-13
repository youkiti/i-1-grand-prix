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

    ## 審議会資料
    | ID | 資料名 | 審議会/出典 | URL |
    |----|--------|-------------|-----|
    | D001 | 第3回議事録 | 商事法務研究会（電子船荷証券） | [リンク](https://...) |

    ## パブリックコメント
    | ID | コメントID |
    |----|------------|
    | P001 | 12345 |
    """
    doc_citations = []
    pubcom_citations = []

    for cite_id, citation in sorted(registry.citations.items()):
        if citation.cite_type == "document":
            doc_citations.append(citation)
        else:
            pubcom_citations.append(citation)

    lines = ["# 出典一覧\n"]

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
