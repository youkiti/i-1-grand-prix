"""
国会会議録ダウンロードスクリプト

TSVファイルから会議IDを読み込み、各会議の議事録（発言内容）をテキストファイルとして保存する。

使用例:
    python scripts/diet_download.py --input each_project/ai-plan-test/kokkai/meetings_jinkochino_kihon_keikaku_2015_2025.tsv --output-dir each_project/ai-plan-test/kokkai/transcripts
"""

import argparse
import csv
import os
import time
from typing import Optional

import requests


BASE_MEETING_URL = "https://kokkai.ndl.go.jp/api/meeting"

# API リクエストの設定
REQUEST_TIMEOUT = 60
RETRY_COUNT = 4
RETRY_DELAYS = [2, 4, 8, 16]


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


def fetch_meeting_transcript(issue_id: str) -> Optional[dict]:
    """会議単位出力 API から会議全文を取得する。"""
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

    return records[0]


def format_transcript(meeting: dict) -> str:
    """会議録をプレーンテキストに整形する。"""
    lines = []

    # ヘッダー情報
    lines.append("=" * 80)
    lines.append(f"国会会議録")
    lines.append("=" * 80)
    lines.append(f"会議ID: {meeting.get('issueID', '')}")
    lines.append(f"日付: {meeting.get('date', '')}")
    lines.append(f"院: {meeting.get('nameOfHouse', '')}")
    lines.append(f"会議名: {meeting.get('nameOfMeeting', '')}")
    lines.append(f"国会回次: 第{meeting.get('session', '')}回")
    lines.append(f"号数: {meeting.get('issue', '')}")
    lines.append("=" * 80)
    lines.append("")

    # 発言内容
    speeches = meeting.get("speechRecord", [])
    for speech in speeches:
        speaker = speech.get("speaker", "")
        speaker_group = speech.get("speakerGroup", "")
        speaker_role = speech.get("speakerRole", "")
        speech_text = speech.get("speech", "")

        # 発言者情報
        speaker_info = speaker
        if speaker_role:
            speaker_info = f"{speaker}（{speaker_role}）"
        elif speaker_group:
            speaker_info = f"{speaker}（{speaker_group}）"

        lines.append("-" * 40)
        lines.append(f"【{speaker_info}】")
        lines.append("")
        lines.append(speech_text.strip())
        lines.append("")

    return "\n".join(lines)


def save_transcript(text: str, output_path: str) -> None:
    """議事録をテキストファイルとして保存する。"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)


def load_meeting_ids(tsv_path: str) -> list[dict]:
    """TSVファイルから会議情報を読み込む。"""
    meetings = []
    with open(tsv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            meetings.append(row)
    return meetings


def main():
    parser = argparse.ArgumentParser(
        description="TSVファイルから会議IDを読み込み、議事録をダウンロードする。"
    )
    parser.add_argument(
        "--input",
        required=True,
        help="入力TSVファイルのパス",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="議事録を保存するディレクトリ",
    )

    args = parser.parse_args()

    # 出力ディレクトリの作成
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    # 会議情報の読み込み
    meetings = load_meeting_ids(args.input)
    print(f"対象会議数: {len(meetings)}")

    # 各会議の議事録をダウンロード
    success_count = 0
    for i, meeting in enumerate(meetings, 1):
        issue_id = meeting.get("issue_id", "")
        date = meeting.get("date", "")
        meeting_name = meeting.get("meeting_name", "")

        print(f"[{i}/{len(meetings)}] {date} {meeting_name} ({issue_id})")

        # 既存ファイルのスキップ
        output_filename = f"{date}_{issue_id}.txt"
        output_path = os.path.join(args.output_dir, output_filename)
        if os.path.exists(output_path):
            print(f"  スキップ（既存）")
            success_count += 1
            continue

        # 議事録の取得
        transcript_data = fetch_meeting_transcript(issue_id)
        if transcript_data is None:
            print(f"  エラー: 取得失敗")
            continue

        # テキストに整形して保存
        text = format_transcript(transcript_data)
        save_transcript(text, output_path)

        n_speeches = len(transcript_data.get("speechRecord", []))
        print(f"  保存完了: {n_speeches}件の発言")
        success_count += 1

        # API への負荷軽減
        time.sleep(1)

    print(f"\n===== 完了 =====")
    print(f"成功: {success_count}/{len(meetings)} 会議")


if __name__ == "__main__":
    main()
