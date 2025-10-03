<Variables>
- NUM_ARTICLES = 2
- SITE = "https://reddit.com/"
- OUTPUT_DIR = "reports/{YYYY-MM-DD}"
- OUTPUT_FILE = "report.json"
- RETRY_MAX = 3
- REQUEST_TIMEOUT_SEC = 30
- WAIT_STABLE_MS = 1500

# 収集対象（グルーピング）
- SUBREDDITS_TECH = ["artificial", "compsci", "coding"]
- SUBREDDITS_NEWS = ["technology", "Futurology"]

# Reddit API（非認証のJSONエンドポイント）
- REDDIT_TOP_JSON = "https://www.reddit.com/r/{SUBREDDITS}/top.json?t=day&limit={LIMIT}"
</Variables>

<CurrentEnvironment>
- AI実行環境: Codex
- システムシェル: PowerShell (シェルコマンド実行時のみ使用)
</CurrentEnvironment>

<Instructions>
以下のステップを順番に実行してください。

1. `temp_tasklist.md` をチェックリスト形式で作成してください。各ステップが終了するごとにチェックボックスを埋めてください。

2. Reddit のトップ投稿ページを `chrome-devtools.new_page({"url": <URL>})` で開き、安定するまで待ってください。
   - tech グループ（複合ビュー）: `https://www.reddit.com/r/artificial+compsci+coding/top/?t=day`
   - news グループ（複合ビュー）: `https://www.reddit.com/r/technology+Futurology/top/?t=day`

3. 最新の人気投稿を収集し `{OUTPUT_FILE}` を作成する。
   - 対象: tech グループから `{NUM_ARTICLES}` 件、news グループから `{NUM_ARTICLES}` 件（合計 `{NUM_ARTICLES} * 2` 件）。
   - 取得方法: `REDDIT_TOP_JSON` を利用し、適切な `User-Agent` を付与。`RETRY_MAX` と `REQUEST_TIMEOUT_SEC` を適用。
   - 整形: 次の JSONSchema に準拠して記事配列を構築する。
     - `url`: 投稿の恒久リンク（permalink を `SITE` で前置）
     - `title`: 投稿タイトル
     - `date`: `created_utc` を ISO-8601 に変換（タイムゾーンはローカルまたは UTC で可、統一する）
     - `executive_summary`: 日本語 3–7 行
     - `key_findings`: 5–12 項目（各 `point` と、その根拠 `footnote`。フットノートには投稿 URL や外部リンクを使用）
     - `references`: 関連 URL（投稿 URL、外部リンクがある場合はそれも含める）
     - `retrieved_at`: 取得日時（ISO-8601）
   - 出力先: `{OUTPUT_DIR}/{OUTPUT_FILE}`（`{YYYY-MM-DD}` は実行日のローカル日付でゼロパディング置換）。ディレクトリが無い場合は作成。
   - 文字コード/改行: UTF-8・`\n`。

4. 成果物を報告し、`temp_tasklist.md` を片付けてください。
</Instructions>

<Constraints>
- Web検索: Chrome DevTools MCPサーバーを使用
- ファイル操作: Codexの標準ツール apply_patch を使用
- 注意: ファイル読み書きは必ずCodexのツールを使用し、エラーが頻発する場合はPowerShellのecho/cat/heredoc等を使用すること
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
- Reddit 取得時は `User-Agent` を必ず明示し、`RETRY_MAX` と `REQUEST_TIMEOUT_SEC` を遵守
</Runtime>