# CLAUDE ガイドライン（i-1-grand-prix）

## このリポジトリの目的

**事前仮説（審議会での議論）とくらべて、パブリックコメント等に新しいビュー（視点・論点）がないかを見出すこと**

### 推奨パイプライン

```
Stage 1: pre_hypothesis_iterative（審議会資料 → 事前仮説）
                ↓
Stage 2: pubcom_analysis（パブコメ × 事前仮説 → 比較レポート）
```

## 推奨：2段階実行

### Stage 1: 事前仮説生成

審議会資料フォルダから構造化されたQ&A形式の事前仮説を生成。

```bash
python -m src.interview_analysis.cli \
  --mode pre_hypothesis_iterative \
  --source-dir "path/to/committee/documents" \
  --focus "船荷証券の電子化" \
  --model gemini-flash-latest
```

**処理フロー:**
- **Part 1 (Map)**: 各ドキュメントから論点を並列抽出
- **Part 2 (Tree Reduce)**: 階層的統合でQ&Aリスト生成

### Stage 2: パブコメ比較分析

パブコメを事前仮説と比較し、仮説の検証・新インサイトを抽出。

```bash
python -m src.interview_analysis.cli \
  --mode pubcom_analysis \
  --csv data/comments.csv \
  --previous-report doc/2025-12-05/run-111834/outputs/report.md \
  --focus "船荷証券の電子化" \
  --model gemini-flash-latest \
  --comparison-model gemini-3-pro-preview
```

**処理フロー:**
- **Map**: パブコメをバッチ分析（並列）
- **Tree Reduce**: 分析結果を階層的統合
- **Compare**: 事前仮説との比較レポート生成

**推奨モデル構成:**
- `--model gemini-flash-latest`: Map/Reduce（高速・低コスト）
- `--comparison-model gemini-3-pro-preview`: Compare（高品質）

## 環境設定

`.env` に必要なAPIキーを設定:
```bash
GOOGLE_API_KEY=your_google_api_key_here
```

## 重要なプロンプトファイル

| ファイル | 用途 |
|---------|------|
| `pre_hypothesis_part1.md` | 審議会資料からの論点抽出 |
| `pre_hypothesis_reduce.md` | Q&A形式への統合 |
| `pubcom_map.md` | パブコメ個別分析 |
| `pubcom_reduce.md` | パブコメ統合（**過度な統合を防ぐルール含む**） |
| `pubcom_comparison.md` | 事前仮説との比較分析 |

### pubcom_reduce.md の重要ルール

過度な統合を避けるため、異なる論点は別項目として維持するルールが明記されています：
- 効率化・コスト削減に関する意見
- 中小企業・弱者への負担に関する意見
- セキュリティ・リスクに関する意見
- 関係者間の力関係・公平性に関する意見
- 移行期間・並行運用に関する意見
- 国際標準・相互運用性に関する意見
- 環境・社会的影響に関する意見
- 既存の制度・業界への影響に関する意見

**具体的なキーワード（専門用語、固有名詞、技術用語）は省略せず維持**

## チェックポイント機能

処理が中断された場合、`doc/checkpoints/` から再開可能。

```bash
# チェックポイントをクリアして最初から実行
Remove-Item -Recurse -Force "doc\checkpoints\*"
```

## トラブルシューティング

### PDF処理時の警告
`Advanced encoding /90msp-RKSJ-H not implemented yet` は無視して問題なし。

### API レスポンスの警告
`Warning: there are non-text parts in the response` は軽微な警告で処理に影響なし。

### Gemini モデル指定
- 高速処理: `gemini-flash-latest`, `gemini-flash-lite-latest`
- 高品質: `gemini-3-pro-preview`

## 注意事項

- Markdown 出力では太字（`**`）を使わない等、プロンプト内のスタイル規約を守る
- 量的表現・価値判断を避け、客観的で中立な記述を徹底
- 出力は `doc/YYYY-MM-DD/run-HHMMSS/` に自動保存

## スクレイピング機能

審議会資料の取得に使用:

```bash
python scraping/scraper.py <URL> --output_dir <ダウンロード先> [--filter <キーワード>]
```

- 2階層までクロール
- 対象形式: txt, pptx, xlsx, doc, docx, pdf
