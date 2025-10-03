<Variables>
- NUM_ARTICLES = 2
- SITE = "https://ai-news.dev/"
- OUTPUT_DIR = "reports/{YYYY-MM-DD}"
- OUTPUT_FILE = "report.json"
- RETRY_MAX = 3
- REQUEST_TIMEOUT_SEC = 30
- WAIT_STABLE_MS = 1500
</Variables>

<CurrentEnvironment>
- AI実行環境: Codex
- システムシェル: PowerShell
</CurrentEnvironment>

<Instructions>
以下のステップを順番に実行してください。

1. `temp_tasklist.md` をチェックリスト形式で作成してください。各ステップが終了するごとにチェックボックスを埋めてください。

2. `chrome-devtools.new_page({"url": <URL>})` で開いて安定するまで待ってください。

3. 最新の記事 `{NUM_ARTICLES}` 件分の `{OUTPUT_FILE}` を作成する。
  - 日本語でエグゼクティブサマリー（3–7行）を作成
  - Key Findings を5–12項目作成し、各項目は主張(point)と根拠フットノート(footnote)で構成

4. 成果物を報告し、`temp_tasklist.md` を片付けてください。
</Instructions>

<Constraints>
- Web検索: Chrome DevTools MCPサーバーを使用する
- ファイル操作: apply_patch を使用する
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
- 出力先: `{OUTPUT_DIR}/{OUTPUT_FILE}`（`{YYYY-MM-DD}` は実行日のローカル日付でゼロパディング置換）
- ディレクトリが無い場合は作成
- 書き込みは UTF-8・改行は `\n`
</Filesystem>

<Runtime>
- Python を使用する場合は簡単なタスクでも必ず一時スクリプトを作成する（実行後に片付け）
- スクリプトを実行する場合は `uv run temp_script.py`
</Runtime>