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
1. Planning: `update_plan` ツールで計画を作成・更新する。ただし計画で停止しないこと。計画直後に実行フロー（検索→抽出→要約→JSON生成→書き込み→検証）へ自動移行する。
2. Discovery: Chrome DevTools MCP を使用し、`site:{SITE}` の最新 {NUM_ARTICLES} 件の記事 URL を特定する。
   - 優先: 直近14日以内の記事。該当が足りない場合は最新から充足するまで取得。
   - 重複排除・リダイレクト解決を実施。
3. Extraction: 各記事 URL を開き、ページ安定化を待ってから内容を抽出する。
   - 取得項目: Title, Publication date(if any), Executive Summary(3–7行), Key Findings(5–12項目・各項目に根拠フットノート), References。
   - 安定化条件: `network idle` 相当 + DOM 定常化 (下記 Web Search Requirements を参照)。
   - セレクタの優先例: タイトル `h1, meta[property="og:title"]`、公開日 `time[datetime], meta[property="article:published_time"]`、本文 `article, main, .post, .content`。
   - 代替: 主要本文が取れない場合は `readability`/`textContent` ベースで本文を再構成。
4. Summarization: 日本語でエグゼクティブサマリー(3–7行)を作成。Key Findings を5–12項目作成し、各項目は主張(point)と根拠フットノート(footnote)で構成する。
5. JSON Build: 下記 <JSON Schema> に準拠した JSON を構築する。空値は `null` を使用し、型の一貫性を守る。
6. Write: 本日の日付(ローカルタイム)で `{YYYY-MM-DD}` を置換したディレクトリを作成し、 `{OUTPUT_DIR}/{OUTPUT_FILE}` に JSON を保存する。`write` ツールを優先使用。利用不可の場合は Python のファイル I/O を用いる。
   - 注記(Windows 互換): Windows PowerShell の既定では UTF-8(BOM 付き)や CRLF となることがあり、要件「UTF-8 + LF」を満たしづらい。従って shell 経由の保存は最終手段とし、可能であれば Python のファイル I/O（`encoding='utf-8'`, `newline='\n'`）を用いること。
   - 例外的な手段: ツール制約で Python/`jq` 等が使えない場合に限り、bash のヘレドックで厳密に引用・エスケープを行いファイルを作成してよい。この場合も保存後に JSON パース検証を必須とし、失敗時は {RETRY_MAX} 回まで再試行する。
   - CodexCLI 実行例(推奨): Python I/O を行う際は `uv run` を用いる。
     - PowerShell(現在の PS セッション内): `uv run --link-mode=copy generate_report.py`
     - PowerShell(現在の PS セッション内・最小確認): `uv run python -c "print('Hello from uv')"`
     - PowerShell(外部/プログラムから呼び出す場合): `powershell.exe -Command "uv run --link-mode=copy generate_report.py"`
     - 最小確認(外部/プログラムから): `powershell.exe -Command "uv run python -c \"print('Hello from uv')\""`
     - 直接書き込み(例・外部/プログラムから): `powershell.exe -Command "uv run python -c \"from pathlib import Path, PurePath; import datetime; today=datetime.date.today().strftime('%Y-%m-%d'); out=Path(f'reports/{today}'); out.mkdir(parents=True, exist_ok=True); (out/'report.json').write_text('{}', encoding='utf-8')\""`
       - 注: 上記 `{}` は実際の JSON 文字列に置換。大きな JSON はコマンド長制限・引用エスケープの複雑化に注意。必要なら小さな Python スクリプトに分離して実行すること。
       - PowerShell の二重引用符エスケープに注意し、LF を強制する場合は `open(..., newline='\n')` を利用。
7. Verify: 書き込み直後に以下を検証し、失敗時は最大 {RETRY_MAX} 回まで再試行する。
   - ファイルの存在確認
   - ファイルサイズ > 0 バイト
   - JSON としてパース可能
8. Finalize: 成功メッセージ(日本語)で保存先パスと記事件数を明示して終了する。ユーザー承認は不要で自律実行すること。
9. 逸脱防止: いかなる理由でも「計画のみ」で終了しない。必ず保存と検証まで到達する。
</Instructions>

<Web Search Requirements>
- Chrome DevTools MCP を必ず使用する。
- 新規ページを開く際は: `chrome-devtools.new_page({"url": <URL>})` を使用。
- ページ安定化: `document.readyState === 'complete'` 後、`network idle` に相当するまで待機し、更に {WAIT_STABLE_MS}ms の静止を加える。
- 検索戦略:
  - `https://www.google.com/search?q=site%3A{SITE}` を開く → 上位候補から記事 URL を収集。
  - 併せて `https://{SITE}/` 直アクセスで最新記事一覧を確認。
- 抽出時の UI 待機:
  - 代表的な要素出現まで待機: `h1`, `article`, `main`, `time[datetime]`。
  - ページ下部まで段階スクロールし、遅延読み込みに対応。
</Web Search Requirements>

<Extraction Heuristics>
- タイトル: `h1` がなければ `meta[property='og:title']`/`meta[name='twitter:title']` を代替。
- 公開日: `time[datetime]` → `meta[property='article:published_time']` → 日付らしき文字列の正規化(ISO8601)、フィールド名は`date`。
- 本文: `article, main, .post, .content` から段落抽出。タグ装飾除去・改行正規化。
- サマリー: 事実中心・固有名詞・数値を優先。曖昧表現を避ける。
- キーファインディング: 1項目につき1つの主張(point) + 根拠フットノート(footnote)の構造で記録。
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
- 出力先: `{OUTPUT_DIR}/{OUTPUT_FILE}`。`{YYYY-MM-DD}` は実行日のローカル日付でゼロパディングして置換する。
- ディレクトリが無ければ作成する。
- 書き込みは UTF-8, 改行は `\n`。
- 検証では存在・サイズ(>0B)・JSONパースを必須確認。失敗時は指数バックオフで再試行(最大 {RETRY_MAX} 回)。
</Filesystem>

<Output Constraints>
- Format: JSON only (Markdown not permitted).
- Save Path: {OUTPUT_DIR}/{OUTPUT_FILE}
</Output Constraints>

<Runtime>
- Python が利用可能。
- Python 実行例: `uv run --link-mode=copy generate_report.py`
- `write` ツールが利用可能ならそれを優先し、不可の場合に Python I/O を使用する。
 - CodexCLI での PowerShell 実行例:
   - 現在の PowerShell セッション内: `uv --version`
   - 現在の PowerShell セッション内: `uv run python -c "print('Hello from uv')"`
   - 現在の PowerShell セッション内: `uv run --link-mode=copy generate_report.py`
   - 外部/プログラムから PowerShell を呼ぶ場合:
     - `powershell.exe -Command "uv --version"`
     - `powershell.exe -Command "uv run python -c \"print('Hello from uv')\""`
     - `powershell.exe -Command "uv run --link-mode=copy generate_report.py"`
</Runtime>

<Shell Execution Strategy>
- 既定: シェル実行は `bash -lc "<command>"` を推奨（Windows でも可能な場合はこの形式を最優先）。
- Windows で `bash` が未導入の場合: `wsl.exe bash -lc "<command>"` を使用（WSL が有効な場合）。
- 最終手段: PowerShell 経由で実行。引用規則・エンコーディング差異に注意し、長いワンライナーは避ける。
  - 例: `powershell.exe -Command "uv run python -c \"print('Hello from uv')\""`
- 既に PowerShell セッション内で実行している場合は `powershell.exe -Command` のプレフィックスは不要（例: `uv run python -c "print('Hello from uv')"`）。
- パスの取り扱い: 絶対パスを推奨。WSL 経由では `C:\...` を `/mnt/c/...` に変換（例: `wslpath -a 'C:\Users\...\Codex_ai_news_reports'`）。
- ヘレドックでの JSON 書き込み（最終手段）:
  - `bash -lc` で `cat > <path> << 'EOF'` を用い、引用・展開無効化。保存後に JSON パース検証を必須化。
  - Python/`jq` が使えない場合でも、可能なら CodexCLI の `uv run python -c "import json,sys; json.load(open('<path>', 'r', encoding='utf-8')); print('OK')"` で検証する。
  - 失敗時は {RETRY_MAX} 回まで再試行。
</Shell Execution Strategy>