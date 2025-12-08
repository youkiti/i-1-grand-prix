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

## Citation Registry（出典追跡機能）

スクレイピングで取得したメタデータ（URL等）を最終レポートまで維持し、クリック可能なリンクとして出力する機能。

### 仕組み

1. **スクレイピング時**: `metadata.json` にURL、ページタイトル等を記録
2. **PDF前処理時**: `[Document Info]` ヘッダーをドキュメント先頭に挿入
3. **分析時**: Citation Registry にファイル情報を登録
4. **最終出力時**: `[出典: ファイル名, p.X]` を `[出典: ファイル名, p.X](URL)` に変換

### 出力ファイル

| ファイル | 内容 |
|---------|------|
| `report.md` | 通常のレポート（引用タグのみ） |
| `report_with_links.md` | URLリンク展開版レポート |
| `citation_registry.json` | 全引用情報のJSON |

### 出典一覧（自動生成）

レポート末尾に以下の形式で出典一覧が自動追加されます：

```markdown
# 出典一覧

## 審議会資料
| ID | ファイル | ページ | URL |
|----|----------|--------|-----|
| D001 | 第3回議事録.pdf | - | [リンク](https://...) |

## パブリックコメント
| ID | コメントID |
|----|------------|
| P001 | 12345 |
```

## スクレイピング機能

審議会資料の取得に使用:

```bash
python scraping/scraper.py <URL> --output_dir <ダウンロード先> --path-prefix <パス> [--filter <キーワード>] [--link-text-filter <リンクテキスト>]
```

- 2階層までクロール
- 対象形式: txt, pptx, xlsx, doc, docx, pdf
- `--path-prefix` は必須（例: `/shingi1/` または `none`）
- `--link-text-filter` はリンクテキストでフィルタリング（depth=0のみ適用）

---

## べからず集（スクレイピング・データ処理）

### 1. 出力ファイルのデフォルト名を固定にするな
- **間違い**: `metadata.json` のような固定名を使うと、複数回実行で上書きされる
- **正解**: `metadata_{domain}_{timestamp}.json` のようにユニーク名を生成

### 2. 「賢いデフォルト」を安易に設定するな
- **間違い**: パスプレフィックスを自動検出（`/shingi1/` など）してデフォルトに
- **正解**: 必須オプションとして明示的に指定させる（間違いのもと）

### 3. 日本語サイトのエンコーディングを想定するな
- **間違い**: `response.text` をそのまま使う
- **正解**: `response.encoding = response.apparent_encoding` を設定してからパース

### 4. 全角・半角の違いを忘れるな
- **間違い**: `--link-text-filter "第194回"` （半角数字）
- **正解**: `--link-text-filter "第１９４回"` （全角数字）
- 日本語サイトは全角数字を使うことが多い

### 5. フィルター条件の適用範囲を限定しろ
- **間違い**: `link_text_filter` を全ての階層で適用 → 子ページからのファイル取得が全滅
- **正解**: `depth=0` のみに適用し、子ページからは通常通りクロール

### 6. パスプレフィックスの範囲を広げすぎるな
- **間違い**: `/list/` で制限 → `/list/balance_sheet/` の無関係ファイルも取得
- **正解**: より具体的なパス `/list/denshika-funani/` を使うか、事後クリーンアップを準備

### 7. クリーンアップスクリプトはプロジェクト内に残せ
- **間違い**: ワンオフでインラインPythonコードを実行
- **正解**: 履歴として残るよう、プロジェクト内に `.py` ファイルとして保存

### 8. メタデータを活用したクリーンアップを設計しろ
- **間違い**: ファイル名だけで削除対象を判断
- **正解**: メタデータの `page_url`, `page_title`, `link_text` を参照して正確に特定

### 9. 審議会「部会」と「総会」を混同するな
- **法制審議会の構造**:
  - **部会**: 専門的な審議を行う（例: 商法部会）→ 詳細な資料・議事録あり
  - **総会**: 各部会からの報告を受ける場 → 個別テーマの詳細資料は少ない
- **実例**: 船荷証券関連ファイルは「商法（船荷証券等関係）部会」に20件あるが、「総会（第194-200回）」からは0件

### 10. クリーンアップ後はメタデータも同期しろ
- **間違い**: ファイルだけ削除してメタデータはそのまま → カウント不整合
- **正解**: 以下のパターンでメタデータを同期:
```python
# 存在するファイルのみメタデータに残す
actual_files = set(f.name for f in dir.glob('*.pdf'))
metadata["files"] = {k: v for k, v in metadata["files"].items() if k in actual_files}
```

### 11. 空のメタデータファイルは削除しろ
- クリーンアップ後にファイル数が0になったメタデータは削除
- 残しておくとカウントスクリプトでノイズになる

### 12. READMEにソース情報と実行履歴を残せ
- 各ソースのURL、ファイル数、クリーンアップ内容を記録
- 再現可能なダウンロードコマンドを記載

