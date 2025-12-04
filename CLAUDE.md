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

### 推奨: initial_auto モード（2段階自動実行）

**最も推奨される実行方法**です。出力トークン制限を回避し、完全なレポートを1コマンドで生成します。

```bash
python -m src.interview_analysis.cli \
  --csv data/messages.csv \
  --mode initial_auto \
  --meta config/meta.yaml \
  --prompt-dir prompts \
  --log-dir doc \
  --model "x-ai/grok-4.1-fast" \
  --focus "船荷証券の電子化に伴う法制度改正"
```

**特徴**:
- Part1（新規論点発見）とPart2（事前仮説検証）を自動的に順次実行
- **`--focus` オプション**: 分析の主眼を指定することで、関連性の低い情報（会議運営等）を除外し、重要な論点に集中させます。
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

## スクレイピング機能

指定したURLから2階層までクロールし、特定のファイル形式（txt, pptx, xlsx, doc, docx, pdf）をダウンロードします。

### 実行方法

```bash
python scraping/scraper.py <URL> --output_dir <ダウンロード先ディレクトリ> [--filter <キーワード>]
```

- `<URL>`: クロールを開始するURL
- `--output_dir`: ダウンロードしたファイルを保存するディレクトリ（デフォルト: `downloads`）
- `--filter`: URLにこのキーワードが含まれる場合のみクロール・ダウンロードします（オプション）

## トラブルシューティング & Tips

### 1. スクリプト実行時の `ModuleNotFoundError`
`scripts/` フォルダ内のスクリプトを実行する際、`src` モジュールのインポートエラーが発生する場合は、ルートディレクトリから `-m` オプションを使用して実行してください。

```bash
# NG: python scripts/summarize_report.py
# OK: python -m scripts.summarize_report
```

### 2. 大量ファイルの処理（`pre_hypothesis_iterative`）
ファイル数が多い（例: 100ファイル以上）場合、順次処理では時間がかかります。`ThreadPoolExecutor` を使用した並列処理の実装を検討してください。

### 3. Grok (OpenRouter) のモデル指定
`model_provider.py` はモデル名に `"/"` または `"grok"` が含まれる場合、自動的に OpenRouter 経由でリクエストします。
例: `x-ai/grok-4.1-fast:free`

### 4. PDF処理時の警告
PDF処理時に `Advanced encoding /90msp-RKSJ-H not implemented yet` 等の警告が出ることがありますが、処理自体が止まらなければ無視しても問題ありません。
