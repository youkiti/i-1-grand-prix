import csv
from pathlib import Path
from typing import Dict, List, Tuple
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
