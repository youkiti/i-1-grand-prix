# 船荷証券電子化関連資料

## 概要
船荷証券の電子化に関する審議会・研究会資料を収集したフォルダ。
**現在のファイル数: 88件**

## ダウンロード情報

### 1. 商事法の電子化に関する研究会
- **URL**: https://www.shojihomu.or.jp/list/denshika-funani
- **主催**: 公益財団法人商事法務研究会
- **ファイル数**: 68件

### 2. 法制審議会 商法（船荷証券等関係）部会
- **URL**: https://www.moj.go.jp/shingi1/housei02_003007_00002
- **主催**: 法務省
- **ファイル数**: 20件（第1回〜第16回会議の資料・議事録）

## ダウンロード日時
2025-12-08

## クリーンアップ履歴

### 1. 商事法務 不要ファイル削除
`each_project/funani/cleanup_balance_sheet.py`
- denshika-funani以外のURLからのファイルを削除
- 削除対象: 貸借対照表、規程・定款、個人情報保護方針など
- **削除: 9件**

### 2. 重複ファイル削除
`_1`, `_2` などのサフィックス付き重複ファイルをワンライナーで削除
- **削除: 134件**

### 3. 法務省 不要ファイル削除
`each_project/funani/cleanup_moj.py`
- 船荷証券・運送・海商に関連しないファイルを削除
- 削除対象: 民事訴訟IT化、区分所有法、家族法制、仲裁法など
- **削除: 122件**

## ダウンロードコマンド

```powershell
# 1. 商事法務研究会
python scraping/scraper.py "https://www.shojihomu.or.jp/list/denshika-funani" --output_dir "each_project\funani\shingikai" --path-prefix "/list/"

# 2. 法制審議会 商法部会
python scraping/scraper.py "https://www.moj.go.jp/shingi1/housei02_003007_00002" --output_dir "each_project\funani\shingikai" --path-prefix "/shingi1/"

# 3. クリーンアップ
python each_project/funani/cleanup_balance_sheet.py
python each_project/funani/cleanup_moj.py
```

## メタデータ
各ソースのメタデータは `metadata_{domain}_{timestamp}.json` ファイルを参照。
