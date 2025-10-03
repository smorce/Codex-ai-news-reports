<Variables>
- NUM_ARTICLES = 2
- OUTPUT_DIR = "reports/{YYYY-MM-DD}"
- OUTPUT_FILE = "report.json"
- SUBREDDITS_TECH = ["artificial", "compsci", "coding"]
- SUBREDDITS_NEWS = ["technology", "Futurology"]
- REDDIT_API = "https://www.reddit.com/r/{subreddits}/top.json?t=day&limit={limit}"
</Variables>

<CurrentEnvironment>
- AI実行環境: Codex
- システムシェル: PowerShell
</CurrentEnvironment>

<Instructions>
1. `temp_tasklist.md` にチェックリストを作成（各ステップ終了時に更新）

2. Reddit JSON API から直接取得（User-Agent 必須、リトライ最大3回、タイムアウト30秒）
   - tech グループ: artificial+compsci+coding から {NUM_ARTICLES} 件
   - news グループ: technology+Futurology から {NUM_ARTICLES} 件

3. JSONSchema に従って {OUTPUT_FILE} を作成
   - `executive_summary`: 日本語 3–7 行
   - `key_findings`: 5–12 項目（point + footnote）
   - ディレクトリ自動作成、UTF-8・改行 `\n`

4. 成果物報告後、`temp_tasklist.md` を削除

※ Python実行は `uv run temp_script.py`（実行後に削除）
</Instructions>

<Constraints>
- Web検索: Chrome DevTools MCPサーバーを使用する
- ファイル操作: apply_patch を使用する
</Constraints>

<JSONSchema>
```json
{
  "generated_at": "ISO-8601",
  "site": "https://reddit.com/",
  "num_articles": 4,
  "articles": [
    {
      "url": "投稿の恒久リンク",
      "title": "投稿タイトル",
      "date": "created_utc を ISO-8601 変換",
      "executive_summary": ["日本語", "3–7行"],
      "key_findings": [{"point": "主張", "footnote": "根拠URL"}],
      "references": ["関連URL"],
      "retrieved_at": "ISO-8601"
    }
  ]
}
```
</JSONSchema>