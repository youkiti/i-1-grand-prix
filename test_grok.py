#!/usr/bin/env python3
"""
Grok 連携のクイックテスト
"""
import os
from dotenv import load_dotenv

load_dotenv()

# model_provider をインポート
from src.interview_analysis.model_provider import create_provider, ModelConfig

def test_grok():
    """Grok-4.1-fast:free のテスト"""

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ OPENROUTER_API_KEY が設定されていません")
        return

    print("✅ OPENROUTER_API_KEY が設定されています")
    print(f"   Key prefix: {api_key[:15]}...")

    # プロバイダー作成
    provider = create_provider("x-ai/grok-4.1-fast:free")

    # モデル設定
    config = ModelConfig(
        model="x-ai/grok-4.1-fast:free",
        temperature=0.7,
        max_output_tokens=500,
    )

    # 簡単なプロンプト
    prompt = "日本語で簡潔に自己紹介してください（1-2文）"

    print("\n📤 プロンプト送信中...")
    print(f"   Model: {config.model}")
    print(f"   Temperature: {config.temperature}")

    try:
        response = provider.generate(prompt, config)
        print("\n✅ レスポンス受信:")
        print("-" * 50)
        print(response)
        print("-" * 50)
    except Exception as e:
        print(f"\n❌ エラー: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_grok()
