# AI News Report (https://ai-news.dev/)

- Generated at: 2025-10-03T11:15:12+09:00
- Articles: 2

## Claude Code卒業！GitHub Copilotに乗り換えます！
- Date: 2025-10-02

### Executive Summary
- 社内AI利用レポートで従量課金の負担を意識し、Claude CodeからGitHub Copilotへの乗り換えを決断した。
- モブプロでカスタム指示やMCP連携を知り、Copilotで開発フロー全体を自動化する構想を得た。
- 準備・実装・MR作成の各工程に専用プロンプトを用意し、JiraチケットからMR下書きまでを一貫処理できるよう設計した。
- ワークフロー指示書がタスク選択と再開を制御し、定型作業の手戻りと判断負荷を大幅に削減した。
- 創造的業務へ集中する余白が生まれた一方で、複雑案件には人間の判断が必要と位置づけ、Claudeとの相互レビューも併用している。

### Key Findings
- 社内のAI利用ランキングで上位に入ったことがコスト最適化への危機感を呼び起こし、ツール移行を検討するきっかけになった。 [^]
  - Footnote: 出典: Zenn「Claude Code卒業！GitHub Copilotに乗り換えます！」（2025年10月2日, https://zenn.dev/flinters_blog/articles/db9e9e90ea8dde）
- Copilotのカスタム指示とスラッシュコマンドを組み合わせ、Jiraチケット入力だけでワークフローを自動進行させる構造を設計した。 [^]
  - Footnote: 出典: Zenn「Claude Code卒業！GitHub Copilotに乗り換えます！」（2025年10月2日, https://zenn.dev/flinters_blog/articles/db9e9e90ea8dde）
- 準備・実装・MR作成の各工程で異なるプロンプトと制約を定義し、`.github/TODOS.md`を介して作業順序と完了報告を自動化した。 [^]
  - Footnote: 出典: Zenn「Claude Code卒業！GitHub Copilotに乗り換えます！」（2025年10月2日, https://zenn.dev/flinters_blog/articles/db9e9e90ea8dde）
- 定型作業をCopilotへ委譲した結果、認知負荷が軽減し、設計検討やレビューなど高付加価値業務に時間を投資できるようになった。 [^]
  - Footnote: 出典: Zenn「Claude Code卒業！GitHub Copilotに乗り換えます！」（2025年10月2日, https://zenn.dev/flinters_blog/articles/db9e9e90ea8dde）
- 複雑なビジネスロジックや前例のない開発ではAI任せにせず、人間判断とCopilotの併用が不可欠だと結論づけている。 [^]
  - Footnote: 出典: Zenn「Claude Code卒業！GitHub Copilotに乗り換えます！」（2025年10月2日, https://zenn.dev/flinters_blog/articles/db9e9e90ea8dde）

### References
- https://zenn.dev/flinters_blog/articles/db9e9e90ea8dde

## Langfuse の Datasets 機能を利用した AIエージェント機能の性能評価のためのデータセット構築
- Date: 2025-10-02

### Executive Summary
- LayerXはバクラクAI申請レビューの性能評価に向け、LangfuseのDatasets機能を活用したデータセット構築の手順を解説した。
- レビュー対象は経費精算申請であり、レビュー対象・申請内容・結果・理由を扱う入出力スキーマを定義している。
- 開発初期はChatGPTで典型例とエッジケースを生成し、人間が確認して偏りを抑える運用を推奨している。
- 運用フェーズでは実環境ログとユーザーの明示的・暗黙的フィードバックをLangfuse Scoresで収集し、データセットに反映する。
- 誤ったデータセットはリリース判断を誤らせるため、目的別のデータ分割と継続的な評価改善が不可欠だと強調した。

### Key Findings
- AI申請レビューではレビュー対象と経費精算申請の入出力を定義し、LLMが理由付きの判定を返すスキーマを採用している。 [^]
  - Footnote: 出典: LayerXエンジニアブログ「Langfuse の Datasets 機能を利用した AIエージェント機能の性能評価のためのデータセット構築」（2025年10月2日, https://tech.layerx.co.jp/entry/2025/10/02/200000）
- Langfuse Datasetsは各アイテムにIDと追加日を付与し、JSON形式の入力・期待出力を記録して再現性を担保する設計になっている。 [^]
  - Footnote: 出典: LayerXエンジニアブログ「Langfuse の Datasets 機能を利用した AIエージェント機能の性能評価のためのデータセット構築」（2025年10月2日, https://tech.layerx.co.jp/entry/2025/10/02/200000）
- ChatGPTを用いたサンプル生成で王道ケースと異常ケースを網羅しつつ、人間が最終判断してデータの偏りを抑制するプロセスを紹介している。 [^]
  - Footnote: 出典: LayerXエンジニアブログ「Langfuse の Datasets 機能を利用した AIエージェント機能の性能評価のためのデータセット構築」（2025年10月2日, https://tech.layerx.co.jp/entry/2025/10/02/200000）
- 実運用ではユーザーのExplicit/ImplicitフィードバックをScores機能で捕捉し、誤判定トレースをデータセットへ追加して改善サイクルを作っている。 [^]
  - Footnote: 出典: LayerXエンジニアブログ「Langfuse の Datasets 機能を利用した AIエージェント機能の性能評価のためのデータセット構築」（2025年10月2日, https://tech.layerx.co.jp/entry/2025/10/02/200000）
- 評価目的に応じたデータセット設計を怠ると誤ったリリース判断につながるとして、実態を反映した継続的改善の必要性を警鐘している。 [^]
  - Footnote: 出典: LayerXエンジニアブログ「Langfuse の Datasets 機能を利用した AIエージェント機能の性能評価のためのデータセット構築」（2025年10月2日, https://tech.layerx.co.jp/entry/2025/10/02/200000）

### References
- https://tech.layerx.co.jp/entry/2025/10/02/200000
