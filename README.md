https://github.com/smorce/Codex-ai-news-reports


### 指定したトピックについてニュースやブログ、フォーラムなどから情報を自動で収集し、レポートにしてまとめてくれるオープンソースのAI駆動情報管理ツール・「Revornix」

https://kachibito.net/useful-resource/revornix

Revornixは指定したトピックについてニュースやブログ、フォーラムなどから情報を自動で収集し、レポートにしてまとめてくれるオープンソースのAI駆動情報管理ツールです。

まとめたデータを元にマルチモーダルAIでMarkdownに変換しベクトルデータベースのMilvusに保存、複数ユーザーが独立した環境で同時利用可能、AIアシスタント内蔵で収集したデータを元に対話可能、複数AIモデルを切り替える事も可能、UIも多言語対応（今のところ英語と中国語のみ）となっています。

今のところはWeb版のみですが今後iOSなどにも対応していくそうです。AI時代の新しい情報収集法として提案する、という目的の元で開発されています。Apache2.0ライセンスの元でソースコードが公開されています。

同じ様なものがあった。


run_codex.bat
をテスト中

uv run scripts/codex_daily_with_agents.py
→tomlを読み込めてない気がする。それが原因でインターネットアクセスできていない気がする。
→読むようにしたらOKだった。プロンプトが原因だった可能性もあるけど。



Pythonの実行周りが冗長なので戦略を変更します。

Pythonコマンドを実行したい場合、一時的に利用するスクリプトを生成して
`powershell.exe -Command "uv run --link-mode=copy temp_build_report.py"` で実行して
`powershell.exe -Command 'Remove-Item temp_build_report.py'`
で片付けするようにしてください。
Python使うときはこのルールで強制したいので、該当箇所のプロンプトを最適化してください。




--full-auto じゃなくて yolo かも？
→full-auto でもコマンドが承認待ちになった。

codex --full-auto
codex --yolo



# Chrome DevTools MCP
以下はうまくいったプロンプト:
---
https://ai-news.dev/ を開いて安定するまで待って。
そこから最新の記事3件のURLを開いて各ページの要約を提示してください。                      
---
これで特定のURLを指定してスクレイピングできる。
"--headless=true" にするとMCPが使われないので注意。


========================================


# Web検索ありで起動
codex -m gpt-5-codex --yolo -c model_reasoning_effort="high" --search "$@"




# Codex AI News Reports

AIを活用したニュースレポート生成システム

## 概要

このプロジェクトは、AIを使用してニュースレポートを自動生成するシステムです。

## 機能

- ニュース記事の自動収集
- AI による記事の分析と要約
- レポートの自動生成

## 使用方法

詳細な使用方法は今後追加予定です。

## セットアップ

### 1. Tursoデータベースのセットアップ

インストールしたくなかったのでWebコンソール画面から対応した。

タスク管理のための永続化ストレージとしてTursoデータベースを使用します。

1.  **Turso CLIのインストール:**
    ```bash
    curl -sSfL https://get.tur.so/install.sh | bash
    ```
2.  **Tursoへのサインアップ/ログイン:**
    ```bash
    turso auth signup
    # またはログイン
    turso auth login
    ```
3.  **データベースの作成:** (例: 東京リージョン)
    ```bash
    turso db create Codex-ai-news-reports --location aws-ap-northeast-1
    # 例: 東京 (利用可能なリージョンを指定)
    # 利用可能なリージョンは `turso db locations` で確認
    ```
4.  **データベース情報の表示:**
    ```bash
    turso db show Codex-ai-news-reports
    ```
5.  **認証トークンの作成:**
    ```bash
    turso db tokens create Codex-ai-news-reports
    ```
    表示されたトークンを `.env` ファイルの `TURSO_AUTH_TOKEN` に設定する。
6.  **データベースURLの取得:**
    ```bash
    turso db show Codex-ai-news-reports --url
    ```
    表示されたURL (`libsql://...`) を `.env` ファイルの `TURSO_DATABASE_URL` に設定します。

## ライセンス

MIT License

## Generated Artifacts (2025-09-28)
- reports/2025-09-28/data/sources.json
- reports/2025-09-28/data/report.json
- reports/2025-09-28/report/2025-09-28-daily-ai-news-ai-news-dev.md
- reports/2025-09-28/logs/turso_push.log
