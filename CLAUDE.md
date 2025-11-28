# CLAUDE ガイドライン（i-1-grand-prix）

## このリポジトリの目的

**事前仮説とくらべて、パブリックコメント等に新しいビュー（視点・論点）がないかを見出すこと**

### 「事前仮説」の定義

- **真の事前仮説**: パブコメデータを見る前に、政策文書・先行研究・専門家意見などから立てた仮説
- **重要**: データから逆算して作った仮説は「事前仮説」ではない
- **目的**: 事前仮説と実際のパブコメを比較することで、予想外の視点や見落としていた論点を発見する

### `hypothesis` モードの位置づけ

- **役割**: データから主要テーマを抽出する探索的分析
- **制約**: このモードで生成した仮説は「事前仮説」ではないため、新しいビュー発見には適さない
- **用途**: 事前知識が全くない場合の初期探索や、真の事前仮説を立てる際の参考資料として使用
- **推奨ワークフロー**: 可能な限り真の事前仮説を用意してから `initial` モードで分析開始

## このリポジトリでのAI利用方針
- 生成系モデルは **Google Gemini 系** を標準とし、デフォルトは `gemini-flash-lite-latest`。`GOOGLE_API_KEY` を `.env` で渡す。
- **推奨モデル**:
  - `initial_auto` モード: `x-ai/grok-4.1-fast:free` (OpenRouter経由・無料) または `gemini-flash-lite-latest`
  - 大量データ処理: 出力トークン制限に達する場合は必ず `initial_auto` モードを使用
- 個人情報・機微情報をプロンプトに含めない。含まれる場合は匿名化してから投入する。
- ログにはAPIキーやトークンを絶対に書き出さない（マスク必須）。

## ディレクトリとファイル運用
- プロンプトは `prompts/` に Markdown で管理し、編集で履歴を追いやすくする。
  - `initial_part1.md`（新規論点発見・第1部専用）**← initial_auto で使用**
  - `initial_part2.md`（事前仮説検証・第2部専用）**← initial_auto で使用**
  - `initial.md`（初回レポート生成・一括版）
  - `hypothesis.md`（データからテーマ抽出・探索的分析）
  - `update.md`（既存レポートへの追加データ反映）
  - `merge.md`（バッチ統合レポート）
  - `pre_hypothesis_example.md`（真の事前仮説作成用テンプレート）
- 実験ログは `doc/YYYY-MM-DD/run-<HHMMSS>/` に保存し、次を必ず残す：
  - 使用したプロンプトのスナップショット
  - 最終レポート
  - モデル名・温度・max_tokens などの設定
  - 実行日時
- 各バッチの中間ログは不要（依頼に基づく）。

## 実行の流れ（VS Code / CLI 想定）

### 推奨: initial_auto モード（2段階自動実行）

**最も推奨される実行方法**です。出力トークン制限を回避し、完全なレポートを1コマンドで生成します。

```bash
python -m src.interview_analysis.cli \
  --csv data/messages.csv \
  --mode initial_auto \
  --meta config/meta.yaml \
  --prompt-dir prompts \
  --log-dir doc \
  --model "x-ai/grok-4.1-fast:free"  # または gemini-flash-lite-latest
```

**特徴**:
- Part1（新規論点発見）とPart2（事前仮説検証）を自動的に順次実行
- 1つの統合レポートを生成（メタデータ → 第1部 → 第2部 → プロンプト）
- 出力トークン制限に達しないよう設計
- Grok無料版など、出力制限が厳しいモデルでも完全なレポートを生成可能

**出力構造**:
```
report.md
├─ メタデータ（実行情報）
├─ まとめ
├─ 第1部: 新しい切り口（事前仮説になかった論点）
├─ 第2部: 事前仮説の検証
├─ よくある質問と市民の疑問
└─ 使用プロンプト（Part1 + Part2）
```

### 代替: 従来の実行方法

出力トークン制限が緩いモデル（Gemini Pro等）を使用する場合、または特定のパートのみ生成したい場合:

```bash
# 一括生成（従来モード）
python -m src.interview_analysis.cli --csv <messages.csv> --mode initial --meta config/meta.yaml

# Part1のみ生成
python -m src.interview_analysis.cli --csv <messages.csv> --mode initial_part1 --meta config/meta.yaml

# Part2のみ生成（Part1の結果を指定）
python -m src.interview_analysis.cli --csv <messages.csv> --mode initial_part2 --part1-report <part1.md> --meta config/meta.yaml
```

### 環境設定

1. `.env` に必要なAPIキーを設定:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   OPENROUTER_API_KEY=your_openrouter_api_key_here  # Grok等を使用する場合
   ```

2. 出力と設定が自動で `doc/YYYY-MM-DD/run-HHMMSS/` に保存される。

## 注意事項
- Markdown 出力では太字（`**`）を使わない等、プロンプト内のスタイル規約を守る。
- 量的表現・価値判断を避け、客観的で中立な記述を徹底する。
- 既存ノートブック（`scripts/legacy/interview_analysis_colab.ipynb`）のロジック・パラメータを参照しつつ、ローカル実行に最適化する。
