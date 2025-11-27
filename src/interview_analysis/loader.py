from pathlib import Path
from typing import Dict, List, Tuple
import pandas as pd

MESSAGE_CANDIDATE_COLUMNS = ["message", "content", "text", "body"]


def load_messages_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"CSVが見つかりません: {path}")
    df = pd.read_csv(path)
    if "session_id" not in df.columns:
        raise ValueError("CSVに session_id 列が必要です")
    return df


def pick_message_column(df: pd.DataFrame) -> str:
    for col in MESSAGE_CANDIDATE_COLUMNS:
        if col in df.columns:
            return col
    raise ValueError(f"メッセージ列が見つかりません。候補: {', '.join(MESSAGE_CANDIDATE_COLUMNS)}")


def build_sessions_data(df: pd.DataFrame) -> Tuple[List[str], str, Dict[str, int]]:
    message_col = pick_message_column(df)
    sessions: List[str] = []
    counts: Dict[str, int] = {}
    parts: List[str] = []
    for session_id, group in df.groupby("session_id"):
        sessions.append(str(session_id))
        counts[str(session_id)] = len(group)
        lines = []
        for _, row in group.iterrows():
            role_prefix = f"{row['role']}: " if "role" in row and not pd.isna(row["role"]) else ""
            content = str(row[message_col])
            lines.append(f"- {role_prefix}{content}")
        parts.append(f"#{session_id}\n" + "\n".join(lines))
    sessions_data = "\n\n".join(parts)
    return sessions, sessions_data, counts
