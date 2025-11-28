# i-1-grand-prix

市民対話セッション等のインタビューデータを分析し、Google Gemini API を用いて客観的なレポートを生成するツールです。

## 概要

このプロジェクトは、CSV形式のインタビューデータ（メッセージログ）を入力として受け取り、以下のモードで分析レポートを生成します：

- `initial_auto`: **【推奨】** 2段階自動実行（出力トークン制限を回避）
- `hypothesis`: データからの主要テーマ抽出（探索的分析）
- `initial`: 初回レポート生成（事前仮説と比較して新しいビューを発見）
- `update`: 既存レポートへの追加データ反映
- `merge`: 複数のバッチレポートの統合

生成されるレポートは客観的・中立的な記述を重視し、量的表現や価値判断を避けた形式で出力されます。

### 処理フロー（initial_auto モード）

```mermaid
graph TB
    Start([ユーザー実行: initial_auto モード]) --> LoadData[CSVデータ読込<br/>869セッション]
    LoadData --> LoadMeta[メタ情報読込<br/>事前仮説ファイル含む]

    LoadMeta --> Part1Start[Part 1 実行開始]

    subgraph Part1 ["Part 1: 新規論点発見"]
        Part1Start --> BuildPrompt1[プロンプト生成<br/>initial_part1.md]
        BuildPrompt1 --> CallModel1[AI呼び出し<br/>Grok/Gemini]
        CallModel1 --> Generate1[レポート生成<br/>まとめ + 第1部]
    end

    Generate1 --> Part2Start[Part 2 実行開始<br/>Part1結果を渡す]

    subgraph Part2 ["Part 2: 事前仮説検証"]
        Part2Start --> BuildPrompt2[プロンプト生成<br/>initial_part2.md]
        BuildPrompt2 --> CallModel2[AI呼び出し<br/>Grok/Gemini]
        CallModel2 --> Generate2[レポート生成<br/>第2部 + FAQ]
    end

    Generate2 --> Combine[統合処理]

    subgraph Combine ["統合レポート生成"]
        Combine --> AddMeta[メタデータ追加]
        AddMeta --> Merge[Part1 + Part2 統合]
        Merge --> AddPrompts[プロンプト追加]
    end

    AddPrompts --> Save[ファイル保存<br/>report.md]
    Save --> End([完了])

    style Part1 fill:#e1f5ff
    style Part2 fill:#fff4e1
    style Combine fill:#f0f0f0
    style Start fill:#c8e6c9
    style End fill:#c8e6c9
```

**出力トークン制限対策**: 1つの大きなレポートではなく、Part1とPart2を分けて生成することで、各パートが制限内に収まります。最終的に1つの統合レポートとして保存されます。

### このツールの目的

**事前仮説とくらべて、パブリックコメント等に新しいビュー（視点・論点）がないかを見出すこと**を主眼としています。そのため、分析を開始する前に「真の事前仮説」を用意することが推奨されます。

### 2つのワークフローパターン

#### パターンA: 事前仮説がある場合（推奨）

1. **事前準備**: パブコメデータを見る前に、政策文書・先行研究・専門家意見などから事前仮説を作成
   - [prompts/pre_hypothesis_example.md](prompts/pre_hypothesis_example.md) をテンプレートとして使用
   - `config/meta.yaml` の `priorHypothesisFile` にファイルパスを指定
2. **initial モード**: 事前仮説と比較してレポート生成（新しいビューを発見）
3. **update モード**: 追加データを反映（必要に応じて）
4. **merge モード**: 複数バッチを統合（大量データの場合）

#### パターンB: 事前仮説がない場合（探索的アプローチ）

1. **hypothesis モード**: データから主要テーマを抽出（探索）
   - ⚠️ 注意: このモードはデータから仮説を生成するため、「新しいビューの発見」という本来の目的には適しません
   - 用途: 事前知識が全くない場合の初期探索や、仮説立案の参考資料作成
2. **手動で事前仮説を作成**: hypothesis モードの出力を参考に、分析者が事前仮説を整理
3. **initial モード以降**: パターンAと同様

**推奨**: 可能な限り**パターンA**を採用してください。真の事前仮説があることで、データに埋もれている新しい視点を見逃さずに発見できます。

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

#### 1. 【推奨】2段階自動実行 (`initial_auto`)

**最も推奨される方法**です。大量データや出力トークン制限が厳しいモデル（Grok無料版等）でも完全なレポートを生成できます。

```bash
# Grok-4.1-fast を使用（推奨・無料）
python -m src.interview_analysis.cli \
  --csv data/messages.csv \
  --mode initial_auto \
  --meta config/meta.yaml \
  --prompt-dir prompts \
  --model "x-ai/grok-4.1-fast:free"

# Gemini を使用
python -m src.interview_analysis.cli \
  --csv data/messages.csv \
  --mode initial_auto \
  --meta config/meta.yaml \
  --prompt-dir prompts \
  --model "gemini-flash-lite-latest"
```

**特徴**:
- Part1（新規論点発見）とPart2（事前仮説検証）を自動的に順次実行
- 1つの統合レポートを生成（メタデータ → 第1部 → 第2部 → プロンプト）
- 出力トークン制限を回避

**出力構造**:
```
report.md
├─ メタデータ（実行情報）
├─ まとめ
├─ 第1部: 新しい切り口（事前仮説になかった論点）
├─ 第2部: 事前仮説の検証
├─ よくある質問と市民の疑問
└─ 使用プロンプト（Part1 + Part2の全文）
```

#### 2. データからのテーマ抽出 (`hypothesis`)

⚠️ このモードは探索的分析用です。真の事前仮説作成には [prompts/pre_hypothesis_example.md](prompts/pre_hypothesis_example.md) を参照してください。

```bash
python -m src.interview_analysis.cli \
  --csv data/messages.csv \
  --mode hypothesis
```

#### 3. 初回レポート生成 (`initial`)

出力トークン制限が緩いモデルを使用する場合、または一括生成を希望する場合:

```bash
# Gemini を使用（デフォルト）
python -m src.interview_analysis.cli \
  --csv data/messages.csv \
  --mode initial

# 注意: 大量データでは出力が途切れる可能性があります
# その場合は initial_auto モードを使用してください
```

#### 4. レポートの更新 (`update`)

前回のレポートに新しいデータを追加反映：

```bash
python -m src.interview_analysis.cli \
  --csv data/new_messages.csv \
  --mode update \
  --previous-report doc/2025-11-27/run-162754/outputs/report.md
```

#### 5. 複数レポートの統合 (`merge`)

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
| `--mode` | - | 実行モード (`initial_auto`, `hypothesis`, `initial`, `initial_part1`, `initial_part2`, `update`, `merge`) |
| `--previous-report` | - | UPDATE用の前回レポートパス |
| `--part1-report` | - | `initial_part2` 用の Part1 レポートパス |
| `--batch-reports` | - | MERGE用のレポートファイル群 |
| `--prompt-dir` | `prompts` | プロンプトテンプレートのディレクトリ |
| `--model` | `gemini-flash-lite-latest` | 使用するモデル (例: `x-ai/grok-4.1-fast:free`, `gemini-flash-lite-latest`) |
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
│   ├── initial_part1.md         # ← initial_auto で使用
│   ├── initial_part2.md         # ← initial_auto で使用
│   ├── initial.md
│   ├── hypothesis.md
│   ├── update.md
│   ├── merge.md
│   └── pre_hypothesis_example.md
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
