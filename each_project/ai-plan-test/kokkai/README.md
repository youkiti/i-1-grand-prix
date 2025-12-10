# 国会会議録検索データ

## 概要
「人工知能基本計画」に関する国会審議の会議録データセット。

## ファイル構成

```
kokkai/
├── meetings_jinkochino_kihon_keikaku_2015_2025.tsv  # 会議メタデータ
└── meetings_jinkochino_kihon_keikaku_2015_2025/     # 議事録テキスト
    ├── 2025-04-08_121705254X01720250408.txt
    ├── 2025-04-09_121704889X01220250409.txt
    └── ...
```

TSVファイル名とフォルダ名が紐づいている。

## 検索条件

| 項目 | 値 |
|------|-----|
| 検索日 | 2025年12月10日 |
| 検索期間 | 2015-01-01 ～ 2025-12-10 |
| 検索キーワード | `人工知能基本計画` |
| データソース | [国会会議録検索システム API](https://kokkai.ndl.go.jp/api.html) |

## 検索結果

- ユニーク会議数: **9**（衆議院4、参議院5）
- 議事録テキスト: **約1.9MB**

## 実行コマンド

```bash
python scripts/diet_search.py \
    --keyword "人工知能基本計画" \
    --from 2015-01-01 \
    --until 2025-12-10 \
    --output-dir each_project/ai-plan-test/kokkai \
    --output meetings_jinkochino_kihon_keikaku_2015_2025.tsv \
    --download
```

`--download` オプションで議事録も同時取得される。

## TSVカラム

| カラム | 説明 |
|--------|------|
| issue_id | 会議ID（一意キー） |
| date | 開催日 |
| house | 院 |
| meeting_name | 会議名 |
| session | 国会回次 |
| meeting_number | 号数 |
| n_speeches | 発言数 |
| keyword | 検索キーワード |
