# AI News Report (https://ai-news.dev/)

- Generated at: 2025-10-05T19:21:15+09:00
- Articles: 2

## Managing context on the Claude Developer Platform
- Date: 2025-09-30

### Executive Summary
- AnthropicがClaude Developer Platform向けにコンテキスト編集とメモリツールを追加。
- Claude Sonnet 4.5と組み合わせ、長時間タスクでも文脈維持と性能向上を狙う。
- 内部評価で39%性能向上やトークン消費84%削減などの効果を確認。
- 機能はパブリックベータとしてClaude、Bedrock、Vertex AI経由で提供開始。

### Key Findings
- コンテキスト編集とメモリツールの2機能をClaude Developer Platformに追加。 [^]
  - Footnote: 出典: "Today, we're introducing new capabilities for managing your agents' context on the Claude Developer Platform: context editing and the memory tool."
- Claude Sonnet 4.5と併用することで長時間のエージェント実行を高性能のまま維持できると説明している。 [^]
  - Footnote: 出典: "With our latest model, Claude Sonnet 4.5, these capabilities enable developers to build AI agents capable of handling long-running tasks at higher performance and without hitting context limits or losing critical information."
- コンテキスト編集はトークン上限に近づくと古いツール実行結果を自動で削除し会話の流れを保つ。 [^]
  - Footnote: 出典: "Context editing automatically clears stale tool calls and results from within the context window when approaching token limits... preserving the conversation flow."
- メモリツールは開発者管理のファイルベース領域に情報を保存し、セッションをまたいで参照できる。 [^]
  - Footnote: 出典: "The memory tool enables Claude to store and consult information outside the context window through a file-based system... that persists across conversations."
- 内部評価でメモリツールとコンテキスト編集の併用はベースライン比39%の性能向上を示し、編集単体でも29%向上した。 [^]
  - Footnote: 出典: "combining the memory tool with context editing improved performance by 39% over baseline. Context editing alone delivered a 29% improvement."
- 100ターンのウェブ検索評価ではコンテキスト編集が失敗を防ぎトークン消費を84%削減した。 [^]
  - Footnote: 出典: "In a 100-turn web search evaluation, context editing enabled agents to complete workflows... while reducing token consumption by 84%."
- 新機能はClaude Developer PlatformのパブリックベータとしてBedrockとVertex AI経由でも利用可能になった。 [^]
  - Footnote: 出典: "These capabilities are available today in public beta on the Claude Developer Platform, natively and in Amazon Bedrock and Google Cloud's Vertex AI."

### References
- https://www.anthropic.com/news/context-management

## Googleの次世代AIチャットボット「Gemini 3 Pro(仮)」がGoogle AI Studioでテスト中、出力結果はこんな感じ
- Date: 2025-10-03T22:00:00+09:00

### Executive Summary
- Google AI StudioのA/BテストでGemini 3 Proが試験運用されているとユーザーが報告。
- Chetaslua氏がGemini 3 Proで2D物理シミュレーターや高精度SVG生成をデモした。
- ベクター描画やUI再現の改善が共有され、テストモデルが7種類存在するとの証言が出た。
- 同氏はGemini 3 Proがフロントエンド開発で最強モデルになると評価した。

### Key Findings
- Gemini 3はGoogle AI StudioのA/Bテストで登場し利用者が結果を公開していると伝えた。 [^]
  - Footnote: 出典: "Googleが提供するAIモデルの無料開発環境「Google AI Studio」のA／BテストでこのGemini 3が登場しているといわれており、その結果をGoogle AI Studioのユーザーが公開しています。"
- Chetaslua氏はGemini 3 Proで六角形を使った2D物理シミュレーターをコーディングした例を示した。 [^]
  - Footnote: 出典: "AIクリエイターであるChetaslua氏が公開しているのは、Gemini 3 Proでコーディングした「六角形を使った2D物理シミュレーター」のムービーです。"
- 同氏はGoogle AI Studioが毎回7つのモデルをテストしていると述べた。 [^]
  - Footnote: 出典: "Chetaslua氏によれば、Google AI Studioでは合計7つのモデルがテストされているとのこと。"
- Gemini 3 ProはSVG形式の画像出力精度が向上し、ペリカンベンチマークで正確な造形を見せた。 [^]
  - Footnote: 出典: "Gemini 3の上位モデルであるGemini 3 Proは、特にSVG形式の画像出力の精度が向上しているそうです。別のユーザーによる、自転車に乗ったペリカンをSVG形式で出力させる「ペリカンベンチマーク」の結果が以下で、かなり正確に造形できていることがわかります。"
- Xbox 360コントローラーなどの生成例も共有され、形状を細部まで描けていると示した。 [^]
  - Footnote: 出典: "Xbox 360のコントローラーだとこんな感じ。"
- 同記事はmacOSのUIまで再現できた事例を取り上げた。 [^]
  - Footnote: 出典: "また、macOSのUIも再現できています。"
- Chetaslua氏はGemini 3 Proが史上最高のフロントエンド・ウェブ開発モデルになると強調した。 [^]
  - Footnote: 出典: "Chetaslua氏はGemini 3 Proについて、「Googleは圧倒的に勝っています。覚えておいてください、これは史上最高のフロントエンドとウェブ開発モデルになるでしょう」と述べています。"

### References
- https://gigazine.net/news/20251003-gemini-3-pro-rumor/
