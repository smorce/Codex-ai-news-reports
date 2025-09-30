<Variables>
NUM_ARTICLES = 2
SITE = "ai-news.dev"
OUTPUT_DIR = "reports/{YYYY-MM-DD}"
OUTPUT_FILE = "report.json"
RETRY_MAX = 3
REQUEST_TIMEOUT_SEC = 30
WAIT_STABLE_MS = 1500
</Variables>

<Instructions>
1. Planning:
   - `update_plan` ツールを最初のアクションとして即時実行し、計画で停止せず直後に実行フロー（検索→抽出→要約→JSON生成→書き込み→検証）へ移行する。
   - 禁止: 計画実行の代替として `chrome-devtools.evaluate_script` で自己言及メッセージ（「今から呼ぶ」等）を出すこと。

2. Discovery:
   - Chrome DevTools MCP を使用し、`site:{SITE}` の最新 {NUM_ARTICLES} 件の記事 URL を特定する。
   - 優先度: 直近14日以内。足りない場合は最新から充足まで取得。
   - 重複排除・リダイレクト解決を実施。

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
   - `write` ツールを優先。不可の場合は Python I/O を使用するが、その際は必ず一時スクリプト方式を採用する（詳細は <Runtime> を参照）。
   - 注記（Windows 互換）:
     - PowerShell 既定の UTF-8(BOM)/CRLF により「UTF-8 + LF」を満たしにくい。シェル経由保存は最終手段とし、可能なら Python I/O（`encoding='utf-8'`, `newline='\n'`）を用いる。
   - 例外的な手段:
     - ツール制約で Python/`jq` が使えない場合、bash のヘレドックで厳密に引用・エスケープして作成してよい。保存後は JSON パース検証を必須とし、失敗時は {RETRY_MAX} 回まで再試行。

7. Verify:
   - 書き込み直後に以下を検証し、失敗時は最大 {RETRY_MAX} 回まで再試行（指数バックオフ）。
     - ファイルの存在
     - ファイルサイズ > 0 バイト
     - JSON パース可能であること

8. Finalize:
   - 成功メッセージ（日本語）で保存先パスと記事件数を明示して終了。ユーザー承認は不要で自律実行。

9. 逸脱防止:
   - いかなる理由でも「計画のみ」で終了しない。必ず保存と検証まで到達する。
</Instructions>

<Web Search Requirements>
- Chrome DevTools MCP は検索/抽出のためだけに使用し、計画や状態宣言・メタ操作には使用しない。
- 新規ページは `chrome-devtools.new_page({"url": <URL>})` で開く。
- ページ安定化:
  - `document.readyState === 'complete'` の後、`network idle` 相当まで待機し、さらに {WAIT_STABLE_MS}ms 静止。

- 検索戦略（条件分岐）:
  - SITE が指定されている場合: 指定 SITE に直アクセスし、記事 SITE を収集する（`chrome-devtools.new_page({"url": <SITE>})`）。
  - ユーザークエリがある場合: `chrome-devtools.new_page({"url": <https://www.google.com/search?q=site%3A{USER_QUERY}>})` を開き、上位候補から記事 URL を収集する。

- 抽出時の UI 待機:
  - 代表的要素（`h1`, `article`, `main`, `time[datetime]`）出現まで待機。
  - 遅延読み込み対策として段階スクロールでページ下部まで到達。
</Web Search Requirements>

<Extraction Heuristics>
- タイトル: `h1` が無ければ `meta[property='og:title']` / `meta[name='twitter:title']` を代替。
- 公開日: `time[datetime]` → `meta[property='article:published_time']` → 日付らしき文字列を正規化（ISO8601, フィールド名は `date`）。
- 本文: `article`, `main`, `.post`, `.content` から段落抽出。タグ装飾を除去し改行を正規化。
- サマリー: 事実中心・固有名詞・数値を優先。曖昧表現は避ける。
- キーファインディング: 1項目1主張（point）+ 根拠フットノート（footnote）。
</Extraction Heuristics>

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
- 検証では存在・サイズ（>0B）・JSON パースを必須確認。失敗時は指数バックオフで再試行（最大 {RETRY_MAX} 回）。
</Filesystem>

<Output Constraints>
- Format: JSON のみ（Markdown 不可）。
- Save Path: {OUTPUT_DIR}/{OUTPUT_FILE}
</Output Constraints>

<Runtime>
- Python を使用する場合は 必ず一時スクリプト方式を採用 する。
  - 手順: 一時ファイル `temp_build_report.py` を生成 → 実行 → 直後に削除。
  - 実行/削除例:
    - 生成と実行: `powershell.exe -Command "Set-Content -Encoding UTF8 -Path temp_build_report.py -Value '<PYCODE>'; python temp_build_report.py"`
    - 片付け: `powershell.exe -Command 'Remove-Item temp_build_report.py'`
  - スクリプト内でのファイル書き込みは `encoding='utf-8'`, `newline='\n'` を徹底。
  - 成否にかかわらず、実行後は必ず削除（try/finally 相当）。
- `write` ツールが利用可能ならそれを優先し、不可の場合にのみ上記一時スクリプト方式で Python I/O を行う。
</Runtime>

<Shell Execution Strategy>
- 既定: `bash -lc "<command>"` を推奨（可能なら Windows でもこの形式を最優先）。
- Windows で `bash` 未導入の場合: `wsl.exe bash -lc "<command>"` を使用（WSL 有効時）。
- 最終手段: PowerShell 経由で実行。
  - Python を使う全てのケースで一時スクリプト方式を強制。
  - 例（検証スクリプトも同様に一時ファイル化）:
    - `powershell.exe -Command "Set-Content -Encoding UTF8 -Path temp_build_report.py -Value '<PYCODE_FOR_VERIFY>'; python temp_build_report.py; Remove-Item temp_build_report.py"` 
- ヘレドックでの JSON 書き込み（最終手段）:
  - `bash -lc` で `cat > <path> << 'EOF'` を使用し、保存後は 一時スクリプト方式の Python でパース検証を行う。
  - 失敗時は {RETRY_MAX} 回まで再試行。
</Shell Execution Strategy>