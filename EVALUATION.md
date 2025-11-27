# モデル評価ガイド

## 概要

`evaluate_models.py` を使用して、指定したモデルでレポート生成を実行し、実行時間と出力情報を記録します。

## 基本的な使い方

### 1. Grok で評価（デフォルト）

```bash
python evaluate_models.py --csv data/messages.csv
```

デフォルトで `x-ai/grok-4.1-fast:free` を使用します。

### 2. 他のモデルで評価

```bash
# Gemini
python evaluate_models.py \
  --csv data/messages.csv \
  --model gemini-flash-lite-latest

# Claude
python evaluate_models.py \
  --csv data/messages.csv \
  --model anthropic/claude-3.5-sonnet

# GPT-4
python evaluate_models.py \
  --csv data/messages.csv \
  --model openai/gpt-4-turbo
```

### 3. パラメータ調整

```bash
python evaluate_models.py \
  --csv data/messages.csv \
  --model x-ai/grok-4.1-fast:free \
  --temperature 0.7 \
  --max-output-tokens 100000
```

## 出力ファイル

評価結果は `evaluation/YYYY-MM-DD/run-HHMMSS/` に保存されます：

```
evaluation/2025-11-27/run-143022/
├── evaluation_result.json           # 評価結果（JSON形式）
├── evaluation_result.md             # 評価サマリー（Markdown形式）
├── outputs/
│   └── report.md                    # 生成されたレポート
└── prompts/
    └── used_prompt.txt              # 使用したプロンプト
```

## 評価結果の見方

### evaluation_result.md の例

```markdown
# モデル評価結果

## 設定
- モデル: `x-ai/grok-4.1-fast:free`
- データ: `data/messages.csv`
- 温度: 0.3
- 最大トークン: 64000

## 結果
- ステータス: ✅ 成功
- 実行時間: 18.76秒
- レポート文字数: 14,821文字
- レポート行数: 328行
```

## 評価指標

### 自動計測される指標

1. **実行時間**: プロンプト送信からレスポンス受信までの時間
2. **文字数**: 生成されたレポートの文字数
3. **行数**: 生成されたレポートの行数
4. **成功/失敗**: API呼び出しの成功可否

### 手動での品質評価

生成されたレポート（`outputs/report.md`）を確認して、以下をチェック：

1. **構造の完全性**
   - 必要なセクションが全て含まれているか
   - セクション見出しが適切か

2. **内容の正確性**
   - データから正しく情報を抽出できているか
   - 事実に基づいた記述になっているか

3. **日本語の自然さ**
   - 文法的に正しいか
   - 読みやすい表現になっているか

4. **分析の深さ**
   - 表面的な記述にとどまっていないか
   - 洞察が含まれているか

## 利用可能なモデル

### Gemini (GOOGLE_API_KEY)

```bash
--models gemini-flash-lite-latest gemini-2.0-flash-exp gemini-1.5-pro
```

### OpenRouter (OPENROUTER_API_KEY)

```bash
# Grok
--models x-ai/grok-4.1-fast:free x-ai/grok-2-1212

# Claude
--models anthropic/claude-3.5-sonnet anthropic/claude-3-haiku

# GPT
--models openai/gpt-4-turbo openai/gpt-3.5-turbo
```

詳細は [OpenRouter Models](https://openrouter.ai/models) を参照。

## トラブルシューティング

### APIキーエラー

```
ValueError: OPENROUTER_API_KEY が設定されていません
```

`.env` ファイルに該当するキーを追加：

```bash
GOOGLE_API_KEY=your_google_key
OPENROUTER_API_KEY=your_openrouter_key
```

### レート制限

無料モデル (`:free` サフィックス) にはレート制限があります。

```
Error: Rate limit exceeded
```

対処法：
1. 時間をおいて再実行
2. 有料モデルに切り替え
3. 評価するモデル数を減らす

### メモリ不足

大量のデータや長いmax_output_tokensでメモリ不足になる場合：

```bash
# トークン数を減らす
--max-output-tokens 30000

# データを分割して評価
```

## 評価のベストプラクティス

### 1. 複数回実行して安定性を確認

temperatureが0でない場合、出力が毎回変わる可能性があります：

```bash
# 3回実行して結果を比較
for i in {1..3}; do
  python evaluate_models.py \
    --csv data/messages.csv \
    --model x-ai/grok-4.1-fast:free
done
```

### 2. 代表的なデータで評価

評価用データは本番と同じ特性を持つものを使用：

```bash
# ✅ 良い例：本番と同じ形式・分量のデータ
python evaluate_models.py \
  --csv data/sample_messages.csv \
  --model x-ai/grok-4.1-fast:free

# ❌ 悪い例：極端に少ない/多いデータ
python evaluate_models.py \
  --csv data/tiny_test.csv \
  --model x-ai/grok-4.1-fast:free
```

## 使用例

### 例1: Grok で評価

```bash
python evaluate_models.py \
  --csv data/messages.csv \
  --model x-ai/grok-4.1-fast:free
```

### 例2: 異なるtemperatureで試す

```bash
# 安定した出力
python evaluate_models.py \
  --csv data/messages.csv \
  --model x-ai/grok-4.1-fast:free \
  --temperature 0.0

# より創造的な出力
python evaluate_models.py \
  --csv data/messages.csv \
  --model x-ai/grok-4.1-fast:free \
  --temperature 0.7
```

### 例3: 短いレポートで試す

```bash
python evaluate_models.py \
  --csv data/messages.csv \
  --model x-ai/grok-4.1-fast:free \
  --max-output-tokens 30000
```

## まとめ

`evaluate_models.py` を使うことで：

- 指定したモデルの性能を客観的に評価できる
- 実行時間やレポート長を記録できる
- 複数の設定でテストして最適なパラメータを見つけられる

評価結果を確認して、プロジェクトに最適な設定を決定してください。
