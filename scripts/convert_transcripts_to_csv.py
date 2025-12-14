import csv
import glob
import os
import re
from pathlib import Path

def convert_transcripts_to_csv(transcript_dir: str, output_csv: str):
    """
    指定ディレクトリ内の議事録テキストファイル (*.txt) を読み込み、
    pubcom_analysis 用の CSV ファイルを作成する。
    
    CSVカラム: session_id, message
    """
    transcript_path = Path(transcript_dir)
    files = list(transcript_path.glob("*.txt"))
    
    if not files:
        print(f"No transcript files found in {transcript_dir}")
        return

    print(f"Found {len(files)} transcript files.")
    
    rows = []
    
    for file_path in files:
        content = file_path.read_text(encoding="utf-8")
        
        # ファイル名からメタデータを抽出 (例: 2025-04-09_121704889X01220250409.txt)
        # session_id としては issue_id を使用するのが適切
        filename = file_path.stem
        # 日付_ID の形式を想定
        parts = filename.split("_")
        if len(parts) >= 2:
            issue_id = parts[1]
        else:
            issue_id = filename
            
        # 発言ごとの分割などは行わず、会議全体を1つのメッセージとして扱うか、
        # あるいは発言ごとに分割するか。
        # diet_download.py の出力フォーマット:
        # ----------------------------------------
        # 【発言者】
        # 
        # 内容
        # 
        
        # pubcom_analysis は「1行1コメント」的な粒度を想定していることが多いが、
        # 会議録全体を1つのコンテキストとして扱う方が文脈が切れなくて良い場合もある。
        # しかし、tokens制限があるため、発言単位の方が安全かもしれない。
        # ここでは、簡易的に「発言単位」で分割してCSVにする。
        
        # Split by separator
        # diet_download.py uses "-" * 40 as separator before speaker info
        sections = content.split("-" * 40)
        
        # Header is the first section (before first separator)
        # subsequent sections start with \n【Speaker】...
        
        # header = sections[0] 
        
        for i, section in enumerate(sections[1:], 1):
            if not section.strip():
                continue
            
            # Extract speaker and text
            # Format:
            # \n【Speaker】\n\nText\n\n
            
            lines = section.strip().split("\n")
            if not lines:
                continue
                
            speaker_line = lines[0]
            text = "\n".join(lines[1:]).strip()
            
            if not text:
                continue
                
            # Create a unique ID for this speech chunk: issue_id + index
            speech_id = f"{issue_id}_{i:03d}"
            
            # 誰の発言かを含めて message にする
            full_message = f"{speaker_line}\n{text}"
            
            rows.append({
                "session_id": issue_id, # 同じ会議の発言は同じ session_id でグルーピングされる (pipeline.py の仕様)
                "message_id": speech_id,
                "message": full_message
            })

    # Save to CSV
    fieldnames = ["session_id", "message_id", "message"]
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Saved {len(rows)} speeches to {output_csv}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True, help="Directory containing transcript txt files")
    parser.add_argument("--output", required=True, help="Output CSV file path")
    args = parser.parse_args()
    
    convert_transcripts_to_csv(args.input_dir, args.output)
