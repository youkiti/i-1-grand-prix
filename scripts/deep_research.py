"""
Gemini Deep Research Agent 実行スクリプト

Gemini Deep Research エージェントを使用して、複数ステップのリサーチタスクを
自律的に計画・実行し、引用文献付きの詳細レポートを生成する。

API ドキュメント: https://ai.google.dev/gemini-api/docs/deep-research

使用例:
    # 基本的なリサーチ
    python scripts/deep_research.py "Research the history of Google TPUs."
    
    # 出力ファイルを指定
    python scripts/deep_research.py "EVバッテリーの競争環境を調査" --output report.md
    
    # ストリーミングモード（進捗表示）
    python scripts/deep_research.py "量子コンピュータの最新動向" --stream
    
    # 出力形式を指定
    python scripts/deep_research.py "AI規制の国際比較" --format "技術レポート形式で、1.概要 2.主要国の政策 3.比較表 を含む"

必要なパッケージ:
    pip install google-genai
"""

import argparse
import os
import sys
import time
from datetime import datetime
from pathlib import Path

# Add project root to sys.path to import src
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.interview_analysis.token_tracker import TokenTracker, TokenUsage

try:
    from google import genai
except ImportError:
    print("エラー: google-genai パッケージがインストールされていません。")
    print("インストール: pip install google-genai")
    sys.exit(1)

from dotenv import load_dotenv

# .env ファイルを読み込み
load_dotenv()

# 設定
AGENT_NAME = "deep-research-pro-preview-12-2025"
POLL_INTERVAL_SECONDS = 10
MAX_WAIT_MINUTES = 60


def create_client() -> genai.Client:
    """Gemini API クライアントを作成する。"""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("エラー: GOOGLE_API_KEY が設定されていません。")
        print("  .env ファイルに GOOGLE_API_KEY=your_key を追加してください。")
        sys.exit(1)
    
    return genai.Client(api_key=api_key)


def _log_interaction_usage(interaction, mode: str):
    """インタラクションのトークン使用量を記録する"""
    try:
        # Check if usage metadata is available (structure depends on SDK version)
        # Assuming it might be in interaction.usage_metadata or similar
        # For now, we try to access it safely.
        usage_metadata = getattr(interaction, "usage_metadata", None)
        if usage_metadata:
            usage = TokenUsage(
                input_tokens=getattr(usage_metadata, "prompt_token_count", 0) or 0,
                output_tokens=getattr(usage_metadata, "candidates_token_count", 0) or 0,
                total_tokens=getattr(usage_metadata, "total_token_count", 0) or 0
            )
            TokenTracker.track(
                pipeline="deep_research",
                step=mode,
                model=AGENT_NAME,
                usage=usage
            )
            print(f"[TokenUsage] Total: {usage.total_tokens} (In: {usage.input_tokens}, Out: {usage.output_tokens})", flush=True)
    except Exception as e:
        print(f"[Warning] Failed to log token usage: {e}", flush=True)


def run_research_polling(client: genai.Client, prompt: str) -> tuple[str, dict]:
    """
    ポーリング方式でリサーチを実行する。
    長時間タスクに対応し、完了まで待機する。
    
    Returns:
        tuple: (結果テキスト, メタデータ辞書)
    """
    print(f"リサーチ開始...", flush=True)
    print(f"  プロンプト: {prompt[:100]}{'...' if len(prompt) > 100 else ''}", flush=True)
    print(f"  エージェント: {AGENT_NAME}", flush=True)
    print(flush=True)
    
    try:
        interaction = client.interactions.create(
            input=prompt,
            agent=AGENT_NAME,
            background=True
        )
    except Exception as e:
        print(f"エラー: インタラクション作成に失敗しました: {e}", flush=True)
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    interaction_id = interaction.id
    print(f"インタラクション ID: {interaction_id}")
    print(f"ステータスをポーリング中 (最大 {MAX_WAIT_MINUTES} 分)...")
    print()
    
    start_time = time.time()
    max_seconds = MAX_WAIT_MINUTES * 60
    
    while True:
        interaction = client.interactions.get(interaction_id)
        elapsed = time.time() - start_time
        
        if interaction.status == "completed":
            print(f"\n✓ リサーチ完了 ({elapsed:.1f} 秒)")
            _log_interaction_usage(interaction, "polling")
            metadata = {
                "interaction_id": interaction_id,
                "agent": AGENT_NAME,
                "status": interaction.status,
                "execution_time_seconds": round(elapsed, 1),
                "execution_mode": "polling",
            }
            return interaction.outputs[-1].text, metadata
            
        elif interaction.status == "failed":
            error_msg = getattr(interaction, 'error', 'Unknown error')
            print(f"\n✗ リサーチ失敗: {error_msg}")
            sys.exit(1)
            
        elif elapsed > max_seconds:
            print(f"\n✗ タイムアウト: {MAX_WAIT_MINUTES} 分経過")
            sys.exit(1)
        
        # 進捗表示
        status = getattr(interaction, 'status', 'in_progress')
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        print(f"\r  [{minutes:02d}:{seconds:02d}] ステータス: {status}", end="", flush=True)
        
        time.sleep(POLL_INTERVAL_SECONDS)


def run_research_streaming(client: genai.Client, prompt: str) -> tuple[str, dict]:
    """
    ストリーミング方式でリサーチを実行する。
    進捗状況と思考プロセスをリアルタイムで表示する。
    
    Returns:
        tuple: (結果テキスト, メタデータ辞書)
    """
    print(f"リサーチ開始 (ストリーミングモード)...")
    print(f"  プロンプト: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")
    print(f"  エージェント: {AGENT_NAME}", flush=True)
    print()
    print("=" * 60)
    
    start_time = time.time()
    
    stream = client.interactions.create(
        input=prompt,
        agent=AGENT_NAME,
        background=True,
        stream=True,
        agent_config={
            "type": "deep-research",
            "thinking_summaries": "auto"
        }
    )
    
    interaction_id = None
    last_event_id = None
    result_text = []
    
    try:
        for chunk in stream:
            if chunk.event_type == "interaction.start":
                interaction_id = chunk.interaction.id
                print(f"[開始] インタラクション ID: {interaction_id}\n")
            
            if hasattr(chunk, 'event_id') and chunk.event_id:
                last_event_id = chunk.event_id
            
            if chunk.event_type == "content.delta":
                if chunk.delta.type == "text":
                    text = chunk.delta.text
                    print(text, end="", flush=True)
                    result_text.append(text)
                elif chunk.delta.type == "thought_summary":
                    thought = chunk.delta.content.text
                    print(f"\n💭 思考: {thought}\n", flush=True)
            
            elif chunk.event_type == "interaction.complete":
                print("\n" + "=" * 60)
                print("✓ リサーチ完了")
                
    except Exception as e:
        print(f"\n接続が切断されました: {e}")
        if interaction_id:
            print(f"再接続を試みます...")
            # 再接続ロジック
            result_text.append(_reconnect_and_resume(client, interaction_id, last_event_id))
    
    # ストリーミング完了後、最終的なUsageを取得するために一度Getする
    if interaction_id:
        try:
             completed_interaction = client.interactions.get(interaction_id)
             _log_interaction_usage(completed_interaction, "streaming")
        except Exception as e:
             print(f"[Warning] Failed to fetch final interaction stats: {e}")

    elapsed = time.time() - start_time
    metadata = {
        "interaction_id": interaction_id,
        "agent": AGENT_NAME,
        "status": "completed",
        "execution_time_seconds": round(elapsed, 1),
        "execution_mode": "streaming",
    }
    
    return "".join(result_text), metadata


def _reconnect_and_resume(client: genai.Client, interaction_id: str, last_event_id: str) -> str:
    """接続が切断された場合に再接続してストリームを再開する。"""
    max_retries = 3
    result_text = []
    
    for attempt in range(max_retries):
        try:
            time.sleep(2)
            resume_stream = client.interactions.get(
                id=interaction_id,
                stream=True,
                last_event_id=last_event_id
            )
            
            for chunk in resume_stream:
                if hasattr(chunk, 'event_id') and chunk.event_id:
                    last_event_id = chunk.event_id
                
                if chunk.event_type == "content.delta":
                    if chunk.delta.type == "text":
                        text = chunk.delta.text
                        print(text, end="", flush=True)
                        result_text.append(text)
                        
                elif chunk.event_type in ['interaction.complete', 'error']:
                    break
            
            return "".join(result_text)
            
        except Exception as e:
            print(f"再接続失敗 (試行 {attempt + 1}/{max_retries}): {e}")
    
    print("再接続に失敗しました。")
    return "".join(result_text)


def build_prompt(query: str, format_instruction: str = None) -> str:
    """プロンプトを構築する。"""
    prompt = query
    
    if format_instruction:
        prompt = f"{query}\n\n出力形式:\n{format_instruction}"
    
    return prompt


def save_report(content: str, output_path: str, metadata: dict = None) -> None:
    """レポートをファイルに保存する（メタデータ付き）。"""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
        
        if metadata:
            f.write("\n\n")
            f.write("---\n")
            f.write("<!-- Metadata -->\n")
            for key, value in metadata.items():
                if value is None:
                    f.write(f"{key}: null\n")
                elif isinstance(value, str):
                    # 文字列に特殊文字が含まれる場合はクォート
                    if any(c in value for c in [':', '#', '"', "'", '\n']):
                        f.write(f'{key}: "{value}"\n')
                    else:
                        f.write(f"{key}: {value}\n")
                else:
                    f.write(f"{key}: {value}\n")
            f.write("---\n")
    
    print(f"\nレポート保存: {output_path}")


def generate_output_filename(query: str) -> str:
    """出力ファイル名を自動生成する。"""
    # クエリの最初の30文字をファイル名に使用
    safe_query = "".join(c if c.isalnum() or c in "_ -" else "_" for c in query[:30])
    safe_query = safe_query.strip("_").replace(" ", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"deep_research_{safe_query}_{timestamp}.md"


def main():
    parser = argparse.ArgumentParser(
        description="Gemini Deep Research エージェントを使用してリサーチを実行する。",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
    使用例:
      python scripts/deep_research.py "EVバッテリーの競争環境を調査"
      python scripts/deep_research.py "量子コンピュータの最新動向" --stream
      python scripts/deep_research.py "AI規制の国際比較" --output reports/ai_regulation.md
        """
    )
    parser.add_argument(
        "query",
        help="リサーチのクエリ（質問・指示）",
    )
    parser.add_argument(
        "--output", "-o",
        help="出力ファイルパス（省略時は自動生成）",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="出力ディレクトリ（デフォルト: カレントディレクトリ）",
    )
    parser.add_argument(
        "--stream", "-s",
        action="store_true",
        help="ストリーミングモードで実行（進捗をリアルタイム表示）",
    )
    parser.add_argument(
        "--format", "-f",
        dest="format_instruction",
        help="出力形式の指示（例: '技術レポート形式で'）",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="結果をファイルに保存しない（標準出力のみ）",
    )
    
    args = parser.parse_args()
    
    # 出力パス決定 (TokenTracker 初期化のため先行)
    if args.output:
        output_path = Path(args.output)
    else:
        output_filename = generate_output_filename(args.query)
        output_path = Path(args.output_dir) / output_filename

    # TokenTracker 初期化 (出力ファイルと同じディレクトリに token_usage.jsonl を作成)
    if not args.no_save:
       token_log_path = output_path.parent / "token_usage.jsonl"
       TokenTracker.initialize(token_log_path)
    
    # クライアント作成
    client = create_client()
    
    # プロンプト構築
    prompt = build_prompt(args.query, args.format_instruction)
    
    # リサーチ実行
    if args.stream:
        result, metadata = run_research_streaming(client, prompt)
    else:
        result, metadata = run_research_polling(client, prompt)
    
    # 結果表示・保存
    if not args.stream:
        print("\n" + "=" * 60)
        print("リサーチ結果:")
        print("=" * 60)
        print(result)
    
    if not args.no_save:
        # メタデータに追加情報を付与
        metadata["query"] = args.query
        metadata["format_instruction"] = args.format_instruction
        metadata["generated_at"] = datetime.now().isoformat()
        metadata["output_file"] = str(output_path)
        
        save_report(result, output_path, metadata)


if __name__ == "__main__":
    main()
