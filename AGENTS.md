<Variables>
- NUM_ARTICLES = 2
- SITE = "ai-news.dev"
- OUTPUT_DIR = "reports/{YYYY-MM-DD}"
- OUTPUT_FILE = "report.json"
- RETRY_MAX = 3
- REQUEST_TIMEOUT_SEC = 30
- WAIT_STABLE_MS = 1500
</Variables>

<Instructions>
1. Planning:
   - SOWで実行計画を立てます。計画で停止せず直後に実行フロー（検索→抽出→要約→JSON生成→書き込み→検証）へ移行。

2. Discovery:
   - Chrome DevTools MCP を使用し、`site:{SITE}` の最新 {NUM_ARTICLES} 件の記事 URL を特定する。

3. Extraction:
   - 各記事 URL を開き、ページ安定化後に内容を抽出する。
   - 取得項目: Title, Publication date(if any), Executive Summary(3–7行), Key Findings(5–12項目・各項目に根拠フットノート), References。
   - 安定化条件: `network idle` 相当 + DOM 定常化（下記「Web Search Requirements」を参照）。
   - セレクタ優先例:
     - タイトル: `h1`, `meta[property="og:title"]`
     - 公開日: `time[datetime]`, `meta[property="article:published_time"]`
     - 本文: `article`, `main`, `.post`, `.content`
   - 代替: 主要本文が取得できない場合は `readability`/`textContent` ベースで再構成。

4. Summarization:
   - 日本語でエグゼクティブサマリー（3–7行）を作成。
   - Key Findings を5–12項目作成し、各項目は主張(point)と根拠フットノート(footnote)で構成する。

5. JSON Build:
   - 下記 <JSON Schema> に準拠した JSON を構築する。
   - 空値は `null` を用い、型の一貫性を保持する。

6. Write:
   - 本日（ローカルタイム）の日付で `{YYYY-MM-DD}` を置換し、`{OUTPUT_DIR}/{OUTPUT_FILE}` に保存。

7. Finalize:
   - 成功メッセージ（日本語）で保存先パスと記事件数を明示して終了。ユーザー承認は不要で自律実行。

9. 逸脱防止:
   - いかなる理由でも「計画のみ」で終了しない。必ず保存と検証まで到達する。
</Instructions>

<Web Search Requirements>
- Chrome DevTools MCP は検索/抽出のためだけに使用し、計画や状態宣言・メタ操作には使用しない。
- 新規ページは `chrome-devtools.new_page({"url": <URL>})` で開く。
- ページ安定化:
  - `document.readyState === 'complete'` の後、`network idle` 相当まで待機し、さらに {WAIT_STABLE_MS}ms 静止。
</Web Search Requirements>

<JSON Schema>
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
</JSON Schema>

<Filesystem>
- 出力先: `{OUTPUT_DIR}/{OUTPUT_FILE}`（`{YYYY-MM-DD}` は実行日のローカル日付でゼロパディング置換）。
- ディレクトリが無い場合は作成。
- 書き込みは UTF-8・改行は `\n`。
</Filesystem>

<Output Constraints>
- Format: JSON のみ（Markdown 不可）。
- Save Path: {OUTPUT_DIR}/{OUTPUT_FILE}
</Output Constraints>

<Runtime>
- Python を使用する場合は 必ず一時スクリプト方式を採用 する。

一時的に利用するスクリプトを生成して
`powershell.exe -Command "uv run --link-mode=copy temp_filename.py"` で実行して
`powershell.exe -Command 'Remove-Item temp_filename.py'`
で片付けするようにしてください。
</Runtime>

あなたは、発見 → 抽出 → 要約 → JSON生成 → ファイル書き込み → 検証という一連のワークフローを完全に実行します。計画段階で停止することなく、直ちに完全な実行に移らなければなりません。
既存のWeb検索ツールの利用は禁止。Web検索は常にChrome DevTools MCPを利用すること。