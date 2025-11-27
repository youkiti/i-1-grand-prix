# 使用例

## 基本的な使い方

### 1. Gemini でレポート生成（デフォルト）

```bash
python -m src.interview_analysis.cli \
  --csv data/messages.csv \
  --mode initial
```

### 2. Grok でレポート生成

```bash
python -m src.interview_analysis.cli \
  --csv data/messages.csv \
  --mode initial \
  --model x-ai/grok-4.1-fast:free
```

### 3. 他の OpenRouter モデルを使用

OpenRouter で提供されているモデルなら何でも使えます:

```bash
# Claude Sonnet
python -m src.interview_analysis.cli \
  --csv data/messages.csv \
  --mode initial \
  --model anthropic/claude-3.5-sonnet

# GPT-4
python -m src.interview_analysis.cli \
  --csv data/messages.csv \
  --mode initial \
  --model openai/gpt-4-turbo
```

## モデル選択の仕組み

- **モデル名に `/` が含まれる → OpenRouter** (`OPENROUTER_API_KEY` を使用)
- **モデル名に `/` が含まれない → Gemini** (`GOOGLE_API_KEY` を使用)

例:
- `gemini-flash-lite-latest` → Gemini
- `x-ai/grok-4.1-fast:free` → OpenRouter
- `anthropic/claude-3.5-sonnet` → OpenRouter

## テストスクリプト

プロバイダーの動作確認:

```bash
python3 test_grok.py
```

出力例:
```
✅ OPENROUTER_API_KEY が設定されています
   Key prefix: sk-or-v1-f8a805...

📤 プロンプト送信中...
   Model: x-ai/grok-4.1-fast:free
   Temperature: 0.7

✅ レスポンス受信:
--------------------------------------------------
私はGrokです。xAIが開発したAIアシスタントで、役立つ情報を楽しくお届けします。
--------------------------------------------------
```

## パラメータの調整

### 温度 (temperature)

創造性を調整します (0.0-1.0):

```bash
# 安定した出力 (デフォルト)
--temperature 0.3

# より創造的な出力
--temperature 0.8
```

### 最大トークン数

出力の長さを制御:

```bash
# より詳細なレポート
--max-output-tokens 100000

# 短めのレポート
--max-output-tokens 30000
```

## トラブルシューティング

### API キーが設定されていない

```
ValueError: OPENROUTER_API_KEY が設定されていません
```

`.env` ファイルに該当するキーを追加してください:

```bash
OPENROUTER_API_KEY=your_key_here
```

### モデル名のタイポ

モデル名は正確に入力してください。OpenRouter のダッシュボードで正しいモデル ID を確認できます:
https://openrouter.ai/models

### レート制限

無料モデル (`:free` サフィックス付き) にはレート制限があります。制限に達した場合は時間をおいて再試行してください。
