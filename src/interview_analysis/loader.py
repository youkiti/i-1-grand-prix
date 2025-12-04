import csv
from pathlib import Path
from typing import Dict, List, Tuple, Iterator
from collections import defaultdict

MESSAGE_CANDIDATE_COLUMNS = ["message", "content", "text", "body"]


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
            for page in reader.pages:
                text.append(page.extract_text())
            return "\n".join(text)
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

    # 隠しファイル以外を対象にする
    files = sorted([p for p in folder_path.iterdir() if p.is_file() and not p.name.startswith(".")])

    for file_path in files:
        content = read_file_content(file_path)
        yield file_path.name, content

