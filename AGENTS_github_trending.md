<Variables>
- NUM_ARTICLES = 10
- SITE = "https://github.com/trending"
- OUTPUT_DIR = "reports/{YYYY-MM-DD}"
- OUTPUT_FILE = "report.json"
- RETRY_MAX = 3
- REQUEST_TIMEOUT_SEC = 30

# GitHub Trending収集設定
- LANGUAGES_FILE = "scripts/languages.toml"
- GENERAL_LIMIT = 10
- SPECIFIC_LIMIT = 5
</Variables>

<CurrentEnvironment>
- AI実行環境: Codex
- システムシェル: PowerShell
</CurrentEnvironment>

<Instructions>
以下のステップを順番に実行してください。

1. `temp_tasklist.md` をチェックリスト形式で作成してください。各ステップが終了するごとにチェックボックスを埋めてください。

2. 既存の `report_github_trending_raw.json` から収集済みのGitHub Trendingリポジトリデータを読み込む。
   - このファイルには、リポジトリ名、description、スター数、URLが含まれています。

3. トップ `{NUM_ARTICLES}` 件のリポジトリについて、各リポジトリの詳細を調査し `{OUTPUT_FILE}` を作成する。
   - 各リポジトリのREADMEページを `chrome-devtools.new_page({"url": <REPO_URL>})` で開いて内容を確認
   - 日本語でエグゼクティブサマリー（3–7行）を作成
     * リポジトリの主要機能と目的
     * 技術スタック（主要な使用言語・フレームワーク）
     * 特徴的な機能やユースケース
     * スター数
   - Key Findings を5–12項目作成し、各項目は主張(point)と根拠フットノート(footnote)で構成
     * 主要機能の詳細
     * 技術的な特徴
     * 利用シーン
     * コミュニティの活発さ（スター数、最近の更新など）
     * ライセンス情報

4. 成果物を報告し、`temp_tasklist.md` を片付けてください。
</Instructions>

<Constraints>
- Web検索: Chrome DevTools MCPサーバーを使用する
- ファイル操作: apply_patch を使用する
- README取得時は適切な `User-Agent` を使用
</Constraints>

<JSONSchema>
```json
{
  "generated_at": "ISO-8601 string",
  "site": "string",
  "num_articles": "number",
  "articles": [
    {
      "url": "string",
      "title": "string",
      "date": "ISO-8601 string or null",
      "executive_summary": ["string", "string"],
      "key_findings": [
        {
          "point": "string",
          "footnote": "string"
        }
      ],
      "references": ["string"],
      "retrieved_at": "ISO-8601 string"
    }
  ]
}
```
</JSONSchema>

<Filesystem>
- 入力: `{OUTPUT_DIR}/report_github_trending_raw.json`（機械的に収集されたリポジトリデータ）
- 出力先: `{OUTPUT_DIR}/{OUTPUT_FILE}`（`{YYYY-MM-DD}` は実行日のローカル日付でゼロパディング置換）
- ディレクトリが無い場合は作成
- 書き込みは UTF-8・改行は `\n`
</Filesystem>

<Runtime>
- Python を使用する場合は簡単なタスクでも必ず一時スクリプトを作成する（実行後に片付け）
- スクリプトを実行する場合は `uv run temp_script.py`
- README取得時は `RETRY_MAX` と `REQUEST_TIMEOUT_SEC` を遵守
</Runtime>

