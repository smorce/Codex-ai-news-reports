https://github.com/smorce/Codex-ai-news-reports

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
