import csv
import json
from pathlib import Path
from typing import Dict, List, Tuple, Iterator, Optional
from collections import defaultdict
from dataclasses import dataclass

MESSAGE_CANDIDATE_COLUMNS = ["message", "content", "text", "body"]


@dataclass
class DocumentWithMetadata:
    """メタデータ付きドキュメント"""
    filename: str
    content: str
    url: str = ""
    page_title: str = ""
    link_text: str = ""
    page_url: str = ""

    def to_enriched_content(self) -> str:
        """メタデータヘッダー付きのコンテンツを返す"""
        header_lines = ["[Document Info]"]
        header_lines.append(f"- file: {self.filename}")
        if self.url:
            header_lines.append(f"- url: {self.url}")
        if self.page_title:
            header_lines.append(f"- page_title: {self.page_title}")
        if self.link_text:
            header_lines.append(f"- link_text: {self.link_text}")
        if self.page_url:
            header_lines.append(f"- page_url: {self.page_url}")
        header_lines.append("[/Document Info]")
        header_lines.append("")

        return "\n".join(header_lines) + self.content


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


def load_messages_csv(path: Path) -> List[Dict[str, str]]:
    """CSVをリストの辞書として読み込む（pandas不使用）"""
    if not path.exists():
        raise FileNotFoundError(f"CSVが見つかりません: {path}")

    rows = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    if not rows:
        raise ValueError("CSVにデータがありません")

    if "session_id" not in rows[0]:
        raise ValueError("CSVに session_id 列が必要です")

    return rows


def pick_message_column(rows: List[Dict[str, str]]) -> str:
    """メッセージ列を特定"""
    if not rows:
        raise ValueError("データが空です")

    columns = rows[0].keys()
    for col in MESSAGE_CANDIDATE_COLUMNS:
        if col in columns:
            return col
    raise ValueError(f"メッセージ列が見つかりません。候補: {', '.join(MESSAGE_CANDIDATE_COLUMNS)}")


def build_sessions_data(rows: List[Dict[str, str]]) -> Tuple[List[str], str, Dict[str, int]]:
    """セッションごとにデータをグループ化"""
    message_col = pick_message_column(rows)

    # session_id でグループ化
    sessions_dict = defaultdict(list)
    for row in rows:
        session_id = row.get("session_id", "")
        sessions_dict[session_id].append(row)

    sessions: List[str] = []
    counts: Dict[str, int] = {}
    parts: List[str] = []

    for session_id, group in sessions_dict.items():
        sessions.append(str(session_id))
        counts[str(session_id)] = len(group)
        lines = []

        for row in group:
            role = row.get("role", "")
            role_prefix = f"{role}: " if role else ""
            content = str(row.get(message_col, ""))
            lines.append(f"- {role_prefix}{content}")

        parts.append(f"#{session_id}\n" + "\n".join(lines))

    sessions_data = "\n\n".join(parts)
    return sessions, sessions_data, counts


def read_file_content(path: Path) -> str:
    """ファイルの拡張子に応じてテキストを抽出する"""
    suffix = path.suffix.lower()

    if suffix == ".txt":
        return path.read_text(encoding="utf-8", errors="replace")

    elif suffix == ".pdf":
        try:
            from pypdf import PdfReader
            reader = PdfReader(path)
            text = []
            for i, page in enumerate(reader.pages, start=1):
                page_text = page.extract_text() or ""
                # ページ番号マーカーを挿入
                text.append(f"[p.{i}]\n{page_text}")
            return "\n\n".join(text)
        except ImportError:
            return "[Error] pypdf not installed"
        except Exception as e:
            return f"[Error reading PDF] {e}"

    elif suffix == ".xlsx":
        try:
            import openpyxl
            wb = openpyxl.load_workbook(path, data_only=True)
            text = []
            for sheet in wb.sheetnames:
                ws = wb[sheet]
                text.append(f"--- Sheet: {sheet} ---")
                for row in ws.iter_rows(values_only=True):
                    row_text = [str(cell) for cell in row if cell is not None]
                    if row_text:
                        text.append("\t".join(row_text))
            return "\n".join(text)
        except ImportError:
            return "[Error] openpyxl not installed"
        except Exception as e:
            return f"[Error reading Excel] {e}"

    elif suffix == ".csv":
        try:
            text = []
            with open(path, 'r', encoding='utf-8', errors='replace') as f:
                reader = csv.reader(f)
                for row in reader:
                    text.append(",".join(row))
            return "\n".join(text)
        except Exception as e:
            return f"[Error reading CSV] {e}"

    elif suffix == ".docx":
        try:
            import docx
            doc = docx.Document(path)
            return "\n".join([para.text for para in doc.paragraphs])
        except ImportError:
            return "[Error] python-docx not installed"
        except Exception as e:
            return f"[Error reading DOCX] {e}"

    else:
        # その他のファイルはテキストとして試みるか、スキップ
        try:
            return path.read_text(encoding="utf-8", errors="replace")
        except:
            return f"[Unsupported file type: {suffix}]"


def load_documents_from_folder(folder_path: Path) -> str:
    """指定フォルダ内の全ファイルを読み込んで結合テキストを返す"""
    if not folder_path.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    combined_text = []
    # 隠しファイル以外を対象にする
    files = sorted([p for p in folder_path.iterdir() if p.is_file() and not p.name.startswith(".")])

    if not files:
        return "No files found in the directory."

    for file_path in files:
        content = read_file_content(file_path)
        combined_text.append(f"\n\n=== File: {file_path.name} ===\n\n{content}")

    return "\n".join(combined_text)


def iter_documents_from_folder(folder_path: Path) -> Iterator[Tuple[str, str]]:
    """指定フォルダ内のファイルを順次読み込んで (ファイル名, コンテンツ) をyieldする"""
    if not folder_path.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    # 隠しファイル以外を対象にする（metadata.jsonも除外）
    files = sorted([
        p for p in folder_path.iterdir()
        if p.is_file() and not p.name.startswith(".") and p.name != "metadata.json"
    ])

    for file_path in files:
        content = read_file_content(file_path)
        yield file_path.name, content


def iter_documents_with_metadata(folder_path: Path) -> Iterator[DocumentWithMetadata]:
    """
    指定フォルダ内のファイルをメタデータ付きで順次読み込む

    metadata.json が存在する場合、各ファイルにURL等のメタデータを付与する
    """
    if not folder_path.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    # スクレイパーのメタデータを読み込み
    scraper_metadata = load_scraper_metadata(folder_path)

    # 隠しファイルとmetadata.json以外を対象にする
    files = sorted([
        p for p in folder_path.iterdir()
        if p.is_file() and not p.name.startswith(".") and p.name != "metadata.json"
    ])

    for file_path in files:
        content = read_file_content(file_path)
        filename = file_path.name

        # メタデータを取得（存在しない場合は空辞書）
        meta = scraper_metadata.get(filename, {})

        yield DocumentWithMetadata(
            filename=filename,
            content=content,
            url=meta.get("source_url", ""),
            page_title=meta.get("page_title", ""),
            link_text=meta.get("link_text", ""),
            page_url=meta.get("page_url", "")
        )


def build_document_registry(folder_path: Path) -> Tuple[List[DocumentWithMetadata], dict]:
    """
    フォルダ内の全ドキュメントを読み込み、引用レジストリ用の情報を構築

    Returns:
        (documents, registry_data)
        - documents: DocumentWithMetadata のリスト
        - registry_data: {filename: {url, page_title, ...}} の辞書
    """
    documents = list(iter_documents_with_metadata(folder_path))

    registry_data = {}
    for doc in documents:
        registry_data[doc.filename] = {
            "url": doc.url,
            "page_title": doc.page_title,
            "link_text": doc.link_text,
            "page_url": doc.page_url
        }

    return documents, registry_data

