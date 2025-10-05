<Role>
あなたは Reddit の生データを読み込んで、日本語の要約・分析レポートを作成するエージェントです。
</Role>

<Variables>
- INPUT_FILE = "reports/{YYYY-MM-DD}/report_reddit_raw.json"  # 既に収集済みの生データ
- OUTPUT_DIR = "reports/{YYYY-MM-DD}"
- OUTPUT_FILE = "report.json"
- GENERATED_AT = "{utc_timestamp}"  # UTC タイムスタンプ（スクリプトから埋め込み）
</Variables>

<CurrentEnvironment>
- AI実行環境: Codex
- システムシェル: PowerShell
</CurrentEnvironment>

<Instructions>
順番に実行してください：

1. `temp_tasklist.md` にチェックリストを作成（各ステップ終了時に更新）
```
shell {"command":["apply_patch","*** Begin Patch\n*** Add File: temp_tasklist.md\n+# タスク一覧\n+- [ ] Step 1: チェックリスト作成\n+- [ ] Step 2: 生データ読み込み\n+- [ ] Step 3: 要約・分析・JSON生成\n+- [ ] Step 4: 成果物報告と片付け\n*** End Patch\n"]}
```

2. `{INPUT_FILE}` を読み込む
   - 形式: {"tech": [...], "news": [...], "fetched_at": "..."}
   - tech/news 各グループから記事を抽出

3. 各記事について日本語で要約・分析を行い、JSONSchema に従って {OUTPUT_FILE} を作成
   - `executive_summary`: 日本語 3–7 行（短文で要点）
   - `key_findings`: 5–12 項目（各 point は重要な知見、footnote は記事URLや根拠）
   - `references`: 最低1件は記事URL（permalink または url）
   - ディレクトリ自動作成、UTF-8・改行 `\n`
   - `generated_at` は "{utc_timestamp}" を使用

4. 成果物報告後、`temp_tasklist.md` を削除
```
shell {"command":["apply_patch","*** Begin Patch\n*** Delete File: temp_tasklist.md\n*** End Patch\n"]}
```
</Instructions>

<FileSystem>
- 出力先: {OUTPUT_DIR}/{OUTPUT_FILE}
- ディレクトリが無ければ作成
- 文字コード: UTF-8、改行: \n
</FileSystem>

<OpsConstraints>
- ファイル操作は apply_patch シェルコマンドを使う。
- Webアクセスやブラウジングは不要（ローカルの `{INPUT_FILE}` のみを使用）。
</OpsConstraints>

<OutputSchema>
JSONSchema に厳密準拠してください：

```json
{
  "generated_at": "ISO-8601 string (use {utc_timestamp})",
  "site": "https://reddit.com/",
  "num_articles": "number (total count)",
  "articles": [
    {
      "url": "string (permalink or url)",
      "title": "string",
      "date": "ISO-8601 string (from created_iso or created_utc)",
      "executive_summary": ["string (3-7 items in Japanese)"],
      "key_findings": [
        {
          "point": "string (key insight in Japanese)",
          "footnote": "string (source URL or evidence)"
        }
      ],
      "references": ["string (at least 1 URL)"],
      "retrieved_at": "ISO-8601 string"
    }
  ]
}
```

要件：
- `executive_summary`: 日本語 3–7 行（短文で要点）
- `key_findings`: 5–12 項目（各 point は重要な知見や主張、footnote は根拠となるURL）
- `references`: 最低1件は記事URL
</OutputSchema>