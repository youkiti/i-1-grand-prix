"""
National Diet Library API Wrapper
国会会議録APIを操作するためのモジュール

- 会議単位出力 API (meeting)
- 発言単位出力 API (speech)
"""

import json
import time
import requests
from pathlib import Path
from typing import Optional, Dict, Any, List

# API Constants
BASE_MEETING_URL = "https://kokkai.ndl.go.jp/api/meeting"
BASE_SPEECH_URL = "https://kokkai.ndl.go.jp/api/speech"
REQUEST_TIMEOUT = 30
RETRY_COUNT = 4
RETRY_DELAYS = [2, 4, 8, 16]

# Cache
CACHE_DIR = Path(".cache/diet_api")
CACHE_DIR.mkdir(parents=True, exist_ok=True)


def make_request_with_retry(url: str, params: dict) -> Optional[dict]:
    """リトライ付きの API リクエスト"""
    for attempt in range(RETRY_COUNT + 1):
        try:
            response = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt < RETRY_COUNT:
                delay = RETRY_DELAYS[attempt]
                # print(f"  [DietAPI] Request failed (attempt {attempt + 1}/{RETRY_COUNT + 1}): {e}")
                # print(f"  [DietAPI] Retrying in {delay}s...")
                time.sleep(delay)
            else:
                print(f"  [DietAPI] Request failed after {RETRY_COUNT + 1} attempts: {e}")
                return None
    return None


def fetch_meeting_meta(issue_id: str, use_cache: bool = True) -> Optional[Dict[str, Any]]:
    """
    会議単位出力 API から会議メタデータを取得する。
    
    Args:
        issue_id (str): 会議録ID (例: "121704889X01420250416")
        use_cache (bool): キャッシュを使用するかどうか
        
    Returns:
        Optional[Dict]: 会議メタデータ（失敗時は None）
    """
    if not issue_id:
        return None
        
    cache_path = CACHE_DIR / f"{issue_id}.json"
    
    # Check cache
    if use_cache and cache_path.exists():
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    params = {
        "issueID": issue_id,
        "recordPacking": "json",
    }

    data = make_request_with_retry(BASE_MEETING_URL, params)
    if data is None:
        return None

    records = data.get("meetingRecord", [])
    if not records:
        return None

    rec = records[0]
    
    # Extract useful fields
    meta = {
        "issue_id": issue_id,
        "date": rec.get("date", ""),
        "house": rec.get("nameOfHouse", ""),
        "meeting_name": rec.get("nameOfMeeting", ""),
        "session": rec.get("session", ""),
        "meeting_number": rec.get("issue", ""),
        "image_kind": rec.get("imageKind", ""),  # 会議録/目次/索引 etc
        "pdf_url": rec.get("pdfURL", ""),
        "page_url": rec.get("meetingURL", ""),
        # Raw record if needed
        # "raw": rec 
    }
    
    # Save cache
    if use_cache:
        try:
            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(meta, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Warning: Failed to save cache for {issue_id}: {e}")
            
    return meta


def search_speech(keyword: str, start_record: int = 1, max_records: int = 10) -> Optional[Dict[str, Any]]:
    """発言検索（簡易版）"""
    params = {
        "any": keyword,
        "recordPacking": "json",
        "maximumRecords": max_records,
        "startRecord": start_record,
    }
    return make_request_with_retry(BASE_SPEECH_URL, params)
