# CLAUDE ガイドライン（i-1-grand-prix）

## このリポジトリでのAI利用方針
- 生成系モデルは **Google Gemini 系** を標準とし、デフォルトは `gemini-flash-lite-latest`。`GOOGLE_API_KEY` を `.env` で渡す。
- 個人情報・機微情報をプロンプトに含めない。含まれる場合は匿名化してから投入する。
- ログにはAPIキーやトークンを絶対に書き出さない（マスク必須）。

## ディレクトリとファイル運用
- プロンプトは `prompts/` に Markdown で管理し、編集で履歴を追いやすくする。
  - `hypothesis.md`（仮説立案）
  - `initial.md`（初回レポート生成）
  - `merge.md`（バッチ統合レポート）
- 実験ログは `doc/YYYY-MM-DD/run-<HHMMSS>/` に保存し、次を必ず残す：
  - 使用したプロンプトのスナップショット
  - 最終レポート
  - モデル名・温度・max_tokens などの設定
  - 実行日時
- 各バッチの中間ログは不要（依頼に基づく）。

## 実行の流れ（VS Code / CLI 想定）
1. `.env` に `GOOGLE_API_KEY` を設定。
2. `python -m src.interview_analysis.cli --csv <messages.csv> --mode <initial|update|merge>` を実行。
3. 出力と設定が自動で `doc/` に保存される。

## 注意事項
- Markdown 出力では太字（`**`）を使わない等、プロンプト内のスタイル規約を守る。
- 量的表現・価値判断を避け、客観的で中立な記述を徹底する。
- 既存ノートブック（`scripts/legacy/interview_analysis_colab.ipynb`）のロジック・パラメータを参照しつつ、ローカル実行に最適化する。
