# CLAUDE ガイドライン（i-1-grand-prix）

## このリポジトリの目的

**事前仮説（審議会・国会での議論）とくらべて、パブリックコメント等に新しいビュー（視点・論点）がないかを見出すこと**

### 現在の分析対象

| プロジェクト | 審議会資料 | 国会審議 | AI対話 |
|-------------|-----------|---------|--------|
| **funani**（船荷証券） | `each_project/funani/shingikai/` (91 PDF) | - | `data/bill-of-lading_messages.csv` |
| **AI基本計画** | `each_project/ai-plan-test/shingikai/` (519 PDF) | `each_project/ai-plan-test/kokkai/diet_speeches.csv` | `data/ai-plan-test_messages.csv` |
| **議員定数削減** | `each_project/teisuu/shingikai/` (45 PDF) | `each_project/teisuu/diet_speeches.csv` | `data/teisuu_messages.csv` |

> **Note**: AI対話の分析には `*_messages.csv` を使用（`*_interview_sessions.csv` はセッションメタデータのみ）

### 推奨パイプライン（3段階構成）

```
┌─────────────────────────────────────────────────────────────────┐
│ データ取得フェーズ                                                │
├─────────────────────────────────────────────────────────────────┤
│  審議会資料         →  scraping/scraper.py                       │
│  国会審議           →  scripts/diet_search.py + diet_download.py │
│  パブコメ/AI対話    →  CSV形式で準備                              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Stage 1A: pre_hypothesis_iterative（審議会資料 → 事前仮説YAML）   │
│ Stage 1B: pre_hypothesis_iterative（国会審議 → 事前仮説YAML）     │
│                              ↓                                   │
│           テキスト連結（concat） → merged_hypothesis.md          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ Stage 2: pubcom_analysis（パブコメ × 事前仮説 → 比較レポート）    │
│   または分離実行:                                                 │
│     pubcom_aggregate（パブコメ集約のみ）                          │
│     pubcom_compare（比較分析のみ）                                │
└─────────────────────────────────────────────────────────────────┘
```

## データ取得

### 審議会資料のスクレイピング

```bash
python scraping/scraper.py <URL> \
  --output_dir <ダウンロード先> \
  --path-prefix <パス> \
  [--filter <キーワード>] \
  [--link-text-filter <リンクテキスト>]
```

- 2階層までクロール
- 対象形式: txt, pptx, xlsx, doc, docx, pdf
- `--path-prefix` は必須（例: `/shingi1/` または `none`）
- 出力: ドキュメントファイル + `metadata_*.json`

### 国会審議の取得

```bash
# 会議検索 + 議事録ダウンロード
python scripts/diet_search.py \
  --keyword "人工知能基本計画" \
  --from 2015-01-01 \
  --until 2025-12-10 \
  --output-dir each_project/ai-plan-test/kokkai \
  --output meetings.tsv \
  --download

# CSVに変換（pre_hypothesis_iterativeで使用するため）
python scripts/convert_transcripts_to_csv.py \
  --input-dir each_project/ai-plan-test/kokkai/meetings_* \
  --output each_project/ai-plan-test/kokkai/diet_speeches.csv
```

出力ファイル:
- `meetings_*.tsv`: 会議メタデータ
- `meetings_*/`: 議事録テキスト
- `diet_speeches.csv`: 分析用CSV（session_id, speech_id, speaker, speech列）

## Stage 1: 事前仮説生成

### Stage 1A: 審議会資料から事前仮説

```bash
python -m src.interview_analysis.cli \
  --mode pre_hypothesis_iterative \
  --source-dir "each_project/ai-plan-test/shingikai" \
  --focus "人工知能基本計画" \
  --model "gemini:gemini-flash-lite-latest"
```

### Stage 1B: 国会審議から事前仮説

```bash
python -m src.interview_analysis.cli \
  --mode pre_hypothesis_iterative \
  --source-dir "each_project/ai-plan-test/kokkai" \
  --focus "人工知能基本計画" \
  --model "gemini:gemini-flash-lite-latest"
```

**処理フロー:**
- **Part 1 (Map)**: 各ドキュメントから論点を並列抽出（`pre_hypothesis_part1.md`）
- **Part 2 (Tree Reduce)**: 階層的統合でYAML形式Q&Aリスト生成（`pre_hypothesis_part2_iterative.md`）

### 事前仮説の統合（Concat方式）

審議会と国会のレポートを**単純なテキスト連結**で統合:

```powershell
# PowerShell
Get-Content doc/2025-12-15/run-A/outputs/report.md, doc/2025-12-15/run-B/outputs/report.md | Set-Content merged_hypothesis.md
```

- `pubcom_comparison` は複数の YAML ブロックを入力として理解可能
- `merge` モードはインタビュー分析用であり、事前仮説統合には使用しない

## Stage 2: パブコメ比較分析

### 一括実行（pubcom_analysis）

```bash
python -m src.interview_analysis.cli \
  --mode pubcom_analysis \
  --csv data/comments.csv \
  --previous-report doc/2025-12-15/merged_hypothesis.md \
  --focus "人工知能基本計画" \
  --model "gemini:gemini-flash-lite-latest" \
  --comparison-model "gemini:gemini-2.0-flash"
```

**処理フロー:**
- **Map**: パブコメをバッチ分析（`pubcom_map.md`）
- **Tree Reduce**: 分析結果を階層的統合（`pubcom_reduce.md`）
- **Compare**: 事前仮説との比較レポート生成（`pubcom_comparison.md`）

### 分離実行（大量データ向け）

#### Step 2a: パブコメ集約のみ

```bash
python -m src.interview_analysis.cli \
  --mode pubcom_aggregate \
  --csv data/comments.csv \
  --focus "人工知能基本計画" \
  --model "gemini:gemini-flash-lite-latest" \
  --max-map-batches 50  # APIクォータ管理
```

出力: `pubcom_report.md`（YAML形式、再利用可能）

#### Step 2b: 比較分析のみ

```bash
python -m src.interview_analysis.cli \
  --mode pubcom_compare \
  --pubcom-report doc/2025-12-15/run-HHMMSS/outputs/pubcom_report.md \
  --prior-hypothesis doc/2025-12-15/merged_hypothesis.md \
  --focus "人工知能基本計画" \
  --comparison-model "gemini:gemini-2.0-flash"
```

**推奨モデル構成:**
- `--model "gemini:gemini-flash-lite-latest"`: Map/Reduce（高速・低コスト）
- `--comparison-model "gemini:gemini-2.0-flash"`: Compare（高品質）

## モデルプロバイダー指定

モデル名にプレフィックスを付けてプロバイダーを明示指定:

| プレフィックス | プロバイダー | 例 |
|---------------|------------|----|
| `gemini:` | Google Gemini API | `gemini:gemini-flash-lite-latest` |
| `openrouter:` | OpenRouter API | `openrouter:x-ai/grok-4.1-fast:free` |
| なし | Gemini（後方互換） | `gemini-flash-lite-latest` |

### Gemini モデル価格一覧（2024-12更新）

| モデル | 入力 ($/1M tokens) | 出力 ($/1M tokens) | 備考 |
|--------|-------------------:|-------------------:|------|
| `gemini-3-pro-preview` | $2.00 / $4.00 | $12.00 / $18.00 | 200kトークン閾値で段階制、思考トークン含む |
| `gemini-3-flash-preview` | $0.50 | $3.00 | 思考トークン含む |
| `gemini-2.5-flash` | $0.30 | $2.50 | |
| `gemini-2.5-flash-lite` | $0.10 | $0.40 | 推奨: Map/Reduce用 |

### 思考トークン（Thinking Tokens）

Gemini 3 シリーズ（Pro/Flash）は内部推論プロセスを持ち、その「思考トークン」が出力に含まれます:

- Token Usage Statistics テーブルに **Thinking Tokens** 列が表示されます
- 思考トークンは出力トークンと同じレートで課金されます
- `token_usage.jsonl` に `thinking_tokens` が記録されます

## 環境設定

`.env` に必要なAPIキーを設定:
```bash
GOOGLE_API_KEY=your_google_api_key_here
```

## 重要なプロンプトファイル

| ファイル | 用途 | 出力形式 |
|---------|------|----------|
| `pre_hypothesis_part1.md` | 審議会資料からの論点抽出 | **YAML** |
| `pre_hypothesis_part2_iterative.md` | 論点の統合 | **YAML** |
| `pubcom_map.md` | パブコメ個別分析 | **YAML** |
| `pubcom_reduce.md` | パブコメ統合 | **YAML** |
| `pubcom_comparison.md` | 事前仮説との比較分析 | Markdown |

### YAML出力形式（2024-12更新）

すべてのMap/Reduceプロンプトは**YAML形式**で出力:

```yaml
metadata:
  focus: "テーマ"
  source_documents: [...]

topics:
  - id: "topic_001"
    title: "論点タイトル"
    spectrum:  # 対立軸の可視化
      axis: "A案 ←→ B案"
      positions: [...]
      consensus_status: "継続検討"
    evidence_chunks:  # 原文引用（必須）
      - verbatim_quote: |  # 原文コピペ
          「引用文」
        source_doc_id: "doc_001"
```

**重要ルール:**
- `verbatim_quote` は原文をそのままコピペ（要約禁止）
- `spectrum` で対立軸を可視化
- `evidence_chunks` は各topicに最低1つ必須

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

### pubcom_comparison.md の出力形式（2024-12更新）

比較レポートは以下の構成で出力:

1. **用語解説（Glossary of Terms）**: 高校生にもわかる専門用語解説（5-10個）
2. **ニュートラルな記述**: 価値判断を含む表現（「強い反対」「大きな支持」等）を避ける
3. **原文引用必須**: `> 「原文」 [出典: ...]` 形式で根拠を明示
4. **対立軸の検証**: 審議会の `spectrum` に対するパブコメの反応を整理
5. **今後の対応方針案（国会アクションカード形式）**:
   - 論点マップ（何が問題か × どのレイヤーで動くか）
   - 推奨アクション（質問主意書、委員会質疑、修正案、請願等）
   - すぐ使える成果物（質問主意書案、委員会質問案3本セット、請願用要約）


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
- 高速処理: `gemini:gemini-flash-lite-latest`
- 高品質: `gemini:gemini-2.0-flash`

### focus フィルタリング

`--focus` 引数で指定したテーマに**直接関係のない論点は除外**される:
- 別テーマの政策議論（税制、社会保障、エネルギー等）
- 背景として軽く触れられているだけの論点
- 判断基準: その論点がfocusの実現・決定に**直接影響を与えるか**

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

