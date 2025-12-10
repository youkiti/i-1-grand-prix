"""
国会会議録検索スクリプト

国会会議録検索システム API を使用して、指定キーワードを含む会議を検索し、
会議メタデータを TSV ファイルとして出力する。

API ドキュメント: https://kokkai.ndl.go.jp/api.html

使用例:
    python scripts/diet_search.py --keyword "人工知能基本計画" --from 2015-01-01 --until 2025-12-10
"""

import argparse
import csv
import os
import sys
import time
from datetime import datetime
from typing import Optional

import requests


BASE_SPEECH_URL = "https://kokkai.ndl.go.jp/api/speech"
BASE_MEETING_URL = "https://kokkai.ndl.go.jp/api/meeting"

# API リクエストの設定
MAX_RECORDS_PER_REQUEST = 100
REQUEST_TIMEOUT = 30
RETRY_COUNT = 4
RETRY_DELAYS = [2, 4, 8, 16]  # 指数バックオフ


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
                print(f"  リクエスト失敗 (試行 {attempt + 1}/{RETRY_COUNT + 1}): {e}")
                print(f"  {delay}秒後にリトライ...")
                time.sleep(delay)
            else:
                print(f"  リクエスト失敗: {e}")
                return None
    return None


def collect_issue_ids(keyword: str, date_from: str, date_until: str) -> list[str]:
    """
    発言検索 API からキーワードを含む発言を検索し、
    ユニークな会議 ID (issueID) を収集する。
    """
    issue_ids = set()
    start_record = 1
    total_count = None

    print(f"発言検索中: '{keyword}' ({date_from} ~ {date_until})")

    while True:
        params = {
            "any": keyword,
            "from": date_from,
            "until": date_until,
            "recordPacking": "json",
            "maximumRecords": MAX_RECORDS_PER_REQUEST,
            "startRecord": start_record,
        }

        data = make_request_with_retry(BASE_SPEECH_URL, params)
        if data is None:
            print("  API リクエストに失敗しました。中断します。")
            break

        # 初回のみ総件数を取得
        if total_count is None:
            total_count = data.get("numberOfRecords", 0)
            print(f"  発言ヒット数: {total_count}")

        # ヒットがゼロのときのガード
        records = data.get("speechRecord", [])
        if not records:
            break

        for rec in records:
            issue_ids.add(rec["issueID"])

        # 進捗表示
        current_pos = start_record + len(records) - 1
        print(f"  処理中: {current_pos}/{total_count} (ユニーク会議数: {len(issue_ids)})")

        next_pos = data.get("nextRecordPosition")
        if not next_pos:
            break

        start_record = next_pos

        # API への負荷軽減のための待機
        time.sleep(0.5)

    print(f"  完了: ユニーク会議数 {len(issue_ids)}")
    return sorted(issue_ids)


def fetch_meeting_meta(issue_id: str, keyword: str) -> Optional[dict]:
    """
    会議単位出力 API から会議メタデータを取得する。
    """
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

    # speechRecord が配列で入っている場合の発言数取得
    speeches = rec.get("speechRecord", [])
    n_speeches = len(speeches)

    # 会議URLとPDF URLを取得（speechRecordから最初のものを使用）
    meeting_url = ""
    pdf_url = ""
    if speeches:
        first_speech = speeches[0]
        meeting_url = first_speech.get("meetingURL", "")
        pdf_url = first_speech.get("pdfURL", "")

    return {
        "issue_id": issue_id,
        "date": rec.get("date", ""),
        "house": rec.get("nameOfHouse", ""),
        "meeting_name": rec.get("nameOfMeeting", ""),
        "session": rec.get("session", ""),
        "issue_type": rec.get("issueType", ""),
        "issue_number": rec.get("issue", ""),
        "n_speeches": n_speeches,
        "meeting_url": meeting_url,
        "pdf_url": pdf_url,
        "keyword": keyword,
    }


def save_meetings_tsv(meetings: list[dict], output_path: str) -> None:
    """会議メタデータを TSV ファイルとして保存する。"""
    fieldnames = [
        "issue_id",
        "date",
        "house",
        "meeting_name",
        "session",
        "issue_type",
        "issue_number",
        "n_speeches",
        "meeting_url",
        "pdf_url",
        "keyword",
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for row in meetings:
            writer.writerow(row)

    print(f"TSV 保存完了: {output_path} ({len(meetings)} 会議)")


def generate_output_filename(keyword: str, date_from: str, date_until: str) -> str:
    """出力ファイル名を生成する。"""
    # キーワードをファイル名に使える形式に変換
    safe_keyword = keyword.replace(" ", "_").replace("/", "_")[:30]
    from_year = date_from[:4]
    until_year = date_until[:4]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"diet_meetings_{safe_keyword}_{from_year}_{until_year}_{timestamp}.tsv"


def main():
    parser = argparse.ArgumentParser(
        description="国会会議録から指定キーワードを含む会議を検索し、メタデータを TSV 出力する。"
    )
    parser.add_argument(
        "--keyword",
        required=True,
        help="検索キーワード（例: '人工知能基本計画'）",
    )
    parser.add_argument(
        "--from",
        dest="date_from",
        required=True,
        help="検索開始日 (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--until",
        dest="date_until",
        required=True,
        help="検索終了日 (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="出力ディレクトリ（デフォルト: カレントディレクトリ）",
    )
    parser.add_argument(
        "--output",
        help="出力ファイル名（省略時は自動生成）",
    )

    args = parser.parse_args()

    # 出力ディレクトリの作成
    if args.output_dir and not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    # Step 1: 発言検索から会議 ID を収集
    issue_ids = collect_issue_ids(args.keyword, args.date_from, args.date_until)

    if not issue_ids:
        print("該当する会議が見つかりませんでした。")
        sys.exit(0)

    # Step 2: 各会議のメタデータを取得
    print(f"\n会議メタデータ取得中: {len(issue_ids)} 件")
    meetings = []
    for i, issue_id in enumerate(issue_ids, 1):
        print(f"  [{i}/{len(issue_ids)}] {issue_id}")
        meta = fetch_meeting_meta(issue_id, args.keyword)
        if meta:
            meetings.append(meta)
        # API への負荷軽減
        time.sleep(0.3)

    # Step 3: TSV として保存
    if args.output:
        output_filename = args.output
    else:
        output_filename = generate_output_filename(
            args.keyword, args.date_from, args.date_until
        )

    output_path = os.path.join(args.output_dir, output_filename)
    save_meetings_tsv(meetings, output_path)

    # サマリー表示
    print("\n===== サマリー =====")
    print(f"検索キーワード: {args.keyword}")
    print(f"検索期間: {args.date_from} ~ {args.date_until}")
    print(f"該当会議数: {len(meetings)}")

    # 院別集計
    house_counts = {}
    for m in meetings:
        house = m.get("house", "不明")
        house_counts[house] = house_counts.get(house, 0) + 1

    print("院別内訳:")
    for house, count in sorted(house_counts.items()):
        print(f"  {house}: {count}")


if __name__ == "__main__":
    main()
