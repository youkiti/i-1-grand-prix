# 議員定数削減プロジェクト（teisuu）

議員定数削減に関する調査資料を収集・整理するプロジェクト。

## 調査対象

### 1. 審議会資料

#### 衆議院選挙制度に関する調査会2014-2016

- **URL**: https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_index.html
- **保存先**: `shingikai/`（45ファイル）

### 2. 国会会議録

#### 検索キーワード

以下のキーワードでOR検索を実施：

- `議員定数削減`
- `議員定数の削減`

#### 検索結果（2011年〜2025年）

| 項目                             | 件数            |
| -------------------------------- | --------------- |
| 「議員定数削減」発言ヒット       | 152件           |
| 「議員定数の削減」発言ヒット     | 226件           |
| **ユニーク会議数（合計）** | **230件** |

- **メタデータ**: `diet_meetings_議員定数削減_OR_議員定数の削減_2011_2025_20251213_083638.tsv`
- **議事録本文**: `diet_meetings_議員定数削減_OR_議員定数の削減_2011_2025_20251213_083638/` (230ファイル)

### 3. 参考資料

- **立法調査資料**:
- each_project\teisuu\20221216003-1.pdf
- https://www.sangiin.go.jp/japanese/annai/chousa/rippou_chousa/backnumber/2022pdf/20221216003-1.pdf

## ディレクトリ構成

```
teisuu/
├── README.md                          # 本ファイル
├── 調査対象                            # 調査対象メモ
├── memo.md                            # 調査メモ
├── shingikai/                         # 審議会資料（スクレイピング済）
├── diet_meetings_*.tsv                # 国会会議録メタデータ
├── diet_meetings_*.../                # 国会議事録本文（230ファイル）
├── deep_research_*.md                 # Gemini Deep Research結果
└── image/                             # 関連画像
```

## 使用スクリプト

### 国会会議録検索

```bash
python scripts/diet_search.py \
  --keyword "議員定数削減" "議員定数の削減" \
  --from 2011-01-01 \
  --until 2025-12-13 \
  --output-dir each_project/teisuu \
  --download
```

### 審議会スクレイピング

```bash
python scraping/scraper.py \
  https://www.shugiin.go.jp/internet/itdb_annai.nsf/html/statics/shiryo/senkyoseido_index.html \
  --output-dir each_project/teisuu/shingikai
```
