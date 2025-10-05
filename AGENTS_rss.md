<Variables>
- INPUT_FILE = "reports/{YYYY-MM-DD}/rss_sources.json"  # 既に収集済みの生データ
- OUTPUT_DIR = "reports/{YYYY-MM-DD}"
- OUTPUT_FILE = "report.json"
- GENERATED_AT = "{utc_timestamp}"  # UTC タイムスタンプ（スクリプトから埋め込み）
</Variables>

<CurrentEnvironment>
- AI実行環境: Codex
- システムシェル: PowerShell
</CurrentEnvironment>

<Instructions>
以下のステップを順番に実行してください。

1. `temp_tasklist.md` をチェックリスト形式で作成してください。各ステップが終了するごとにチェックボックスを埋めてください。

2. `{INPUT_FILE}` を読み込んでください（存在がなければ失敗して終了してください）。

3. `{INPUT_FILE}` の `sources` 配列の各記事を要約し JSONSchema に従って  `{OUTPUT_FILE}` を作成してください。
  - 各記事: タイトル、URL、日付（可能なら ISO-8601）、取得時刻（UTC）を含める
   - `executive_summary`: 日本語 3–7 行（短文で要点）
   - `key_findings`: 5–12 項目（各 point は重要な知見、footnote は記事URLや根拠）
   - `references`: 最低1件は記事URL（permalink または url）
   - ディレクトリ自動作成、UTF-8・改行 `\n`
   - `generated_at` は "{utc_timestamp}" を使用

4. 成果物を報告し、`temp_tasklist.md` を片付けてください。
</Instructions>

<Constraints>
- ファイル操作: apply_patch を使用する
- Webアクセスやブラウジングは不要（ローカルの `{INPUT_FILE}` のみを使用）
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