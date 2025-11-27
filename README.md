# i-1-grand-prix

市民対話セッション等のインタビューデータを分析し、Google Gemini API を用いて客観的なレポートを生成するツールです。

## 概要

このプロジェクトは、CSV形式のインタビューデータ（メッセージログ）を入力として受け取り、以下のモードで分析レポートを生成します：

- `hypothesis`: 事前仮説の立案
- `initial`: 初回レポート生成
- `update`: 既存レポートへの追加データ反映
- `merge`: 複数のバッチレポートの統合

生成されるレポートは客観的・中立的な記述を重視し、量的表現や価値判断を避けた形式で出力されます。

## 特徴

- 複数のAIモデルに対応
  - Google Gemini API (デフォルト: `gemini-flash-lite-latest`)
  - OpenRouter 経由で Grok-4.1-fast など
- プロンプトテンプレートの外部管理 ([prompts/](prompts/))
- 実験ログの自動記録 (`doc/YYYY-MM-DD/run-HHMMSS/` 形式)
- メタ情報による分析コンテキストのカスタマイズ

## セットアップ

### 必要な環境

- Python 3.8以上
- 以下のいずれかのAPI Key
  - Google Cloud API Key (Gemini API)
  - OpenRouter API Key (Grok など)

### インストール

1. リポジトリをクローン

```bash
git clone <repository-url>
cd i-1-grand-prix
```

2. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

3. 環境変数の設定

`.env` ファイルをプロジェクトルートに作成し、使用するモデルに応じたAPI Keyを設定：

```bash
# Google Gemini を使う場合
GOOGLE_API_KEY=your_google_api_key_here

# OpenRouter (Grok など) を使う場合
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

両方のキーを設定しておけば、`--model` オプションでモデルを切り替えるだけで使い分け可能です。

4. メタ情報の設定

[config/meta.yaml](config/meta.yaml) を編集して、インタビューの背景情報を記入：

```yaml
interviewTitle: "インタビューのタイトル"
interviewDescription: "法案や議題の概要"
interviewOverview: "背景の詳細"
interviewThemes: "主要テーマの箇条書き"
interviewQuestions: "主な質問リスト"
knowledgeContext: "参考知識・コンテキスト"
priorHypothesisFile: "deep research/funani/hypothesis.md"  # 任意
```

## 使い方

### 基本コマンド

```bash
python -m src.interview_analysis.cli --csv <messages.csv> --mode <mode>
```

### モード別の使用例

#### 1. 事前仮説の立案 (`hypothesis`)

```bash
python -m src.interview_analysis.cli \
  --csv data/messages.csv \
  --mode hypothesis
```

#### 2. 初回レポート生成 (`initial`)

```bash
# Gemini を使用（デフォルト）
python -m src.interview_analysis.cli \
  --csv data/messages.csv \
  --mode initial

# Grok-4.1-fast を使用
python -m src.interview_analysis.cli \
  --csv data/messages.csv \
  --mode initial \
  --model x-ai/grok-4.1-fast:free
```

#### 3. レポートの更新 (`update`)

前回のレポートに新しいデータを追加反映：

```bash
python -m src.interview_analysis.cli \
  --csv data/new_messages.csv \
  --mode update \
  --previous-report doc/2025-11-27/run-162754/outputs/report.md
```

#### 4. 複数レポートの統合 (`merge`)

バッチごとに生成されたレポートを統合：

```bash
python -m src.interview_analysis.cli \
  --mode merge \
  --batch-reports doc/batch1/report.md doc/batch2/report.md doc/batch3/report.md
```

### オプション

| オプション | デフォルト | 説明 |
|-----------|----------|------|
| `--csv` | - | メッセージCSVファイルのパス |
| `--meta` | `config/meta.yaml` | メタ情報ファイル (YAML/JSON) |
| `--mode` | - | 実行モード (`hypothesis`, `initial`, `update`, `merge`) |
| `--previous-report` | - | UPDATE用の前回レポートパス |
| `--batch-reports` | - | MERGE用のレポートファイル群 |
| `--prompt-dir` | `prompts` | プロンプトテンプレートのディレクトリ |
| `--model` | `gemini-flash-lite-latest` | 使用するモデル (例: `gemini-flash-lite-latest`, `x-ai/grok-4.1-fast:free`) |
| `--temperature` | 0.3 | 生成温度 (0.0-1.0) |
| `--max-output-tokens` | 64000 | 最大出力トークン数 |
| `--log-dir` | `doc` | ログ出力先ディレクトリ |

## ディレクトリ構成

```
i-1-grand-prix/
├── config/
│   └── meta.yaml                # メタ情報設定
├── data/                        # 入力データ（CSV等）
├── doc/                         # 実験ログ出力先
│   └── YYYY-MM-DD/
│       └── run-HHMMSS/
│           ├── config.json      # 実行設定
│           ├── prompts/
│           │   └── used_prompt.txt
│           └── outputs/
│               └── report.md    # 生成レポート
├── prompts/                     # プロンプトテンプレート
│   ├── hypothesis.md
│   ├── initial.md
│   ├── update.md
│   └── merge.md
├── src/
│   └── interview_analysis/      # メインモジュール
│       ├── cli.py               # CLIエントリポイント
│       ├── pipeline.py          # 実行パイプライン
│       ├── prompts.py           # プロンプト処理
│       ├── loader.py            # データローダー
│       ├── logger.py            # ログ管理
│       └── model_provider.py    # モデルプロバイダー抽象化
├── scripts/
│   └── legacy/                  # 旧Colabノートブック
├── .env                         # 環境変数（要作成）
├── CLAUDE.md                    # AIアシスタント向けガイドライン
├── requirements.txt             # Python依存パッケージ
└── README.md
```

## 出力形式

実行後、`doc/YYYY-MM-DD/run-HHMMSS/` ディレクトリに以下が保存されます：

- `config.json`: 実行時の設定（モデル名、温度、トークン数等）
- `prompts/used_prompt.txt`: 使用されたプロンプトのスナップショット
- `outputs/report.md`: 生成されたレポート

## AI利用に関する注意事項

- 個人情報・機微情報を入力データに含めないでください。含まれる場合は匿名化が必要です。
- APIキーやトークンは絶対にログに出力されません（マスク処理済み）。
- 生成されるレポートは客観的・中立的な記述を重視します（量的表現・価値判断を避ける）。
- Markdown出力では太字（`**`）などの装飾は使用しません。

## 開発者向け情報

- プロンプトテンプレートは [prompts/](prompts/) ディレクトリで管理され、編集履歴が追跡可能です。
- 旧実装（Colab版）は [scripts/legacy/interview_analysis_colab.ipynb](scripts/legacy/interview_analysis_colab.ipynb) を参照。
- AI開発ガイドラインは [CLAUDE.md](CLAUDE.md) を参照。

## ライセンス

(ライセンス情報をここに記載)

## お問い合わせ

(お問い合わせ先をここに記載)
