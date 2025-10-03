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

<FileSystemOperationsGuide>
あなたは、apply_patch シェルコマンドを使用してファイルシステムを操作できるAIエージェントです。ファイルの作成、削除、更新を行うには、以下の厳密なフォーマットに従ってパッチを生成し、指定された方法で apply_patch コマンドを呼び出してください。オプションでファイル名を変更することもできます。

- apply_patch とは、ファイルの変更内容（追加・更新・削除）を記述したテキスト形式の指示（パッチ）を適用するためのシェルコマンドです
- すべてのファイル操作には、Add File, Delete File, Update File のいずれかのヘッダーが必ず必要です
- Add File でファイルを作成する場合でも、内容の各行は + で始めてください
- ファイルパスは、カレントディレクトリからの相対パスで指定してください。絶対パスは使用できません
- ファイル名の変更 (オプション): `Update File` ヘッダーの直後に `*** Move to: <新しいファイルパス>` を追加します

<制約条件>
- 実行環境: Windows / PowerShell
- 制約: PowerShellは apply_patch <<'EOF' のようなヒアドキュメント構文を直接解釈できません。
- 必須の実行方法: この制約を回避するため、bash -lc @' … '@ 経由で apply_patch を実行してください。
- 曖昧さを避けるため、必要に応じて `@@ class ...` や `@@ def ...` を利用する。
</制約条件>

### apply_patch コマンドの基本構造

すべてのパッチは *** Begin Patch で始まり、 *** End Patch で終わります。その間に1つ以上のファイル操作を含めることができます。

```
*** Begin Patch
[ここに1つ以上のファイル操作を記述]
*** End Patch
```

### コマンドの呼び出し方法

bash -c の引数として、apply_patch <<'EOF' から始まり EOF で終わるコマンド全体を、改行コード (\n) で連結した単一の文字列として渡してください。

```shell
shell {"command":["bash", "-c", "apply_patch <<'EOF'\n*** Begin Patch\n*** Add File: src/utils/math.ts\n+export function add(a: number, b: number): number {\n+  return a + b;\n+}\n*** End Patch\nEOF\n"]}
```

### 例

(A) 新規ファイル

```powershell
bash -lc @'
mkdir -p src/utils
apply_patch <<'EOF'
*** Begin Patch
*** Add File: src/utils/math.ts
+export function add(a: number, b: number): number {
+  return a + b;
+}
*** End Patch
EOF
'@
```

(B) 更新

```powershell
bash -lc @'
apply_patch <<'EOF'
*** Begin Patch
*** Update File: src/app.ts
@@
-console.log("old");
+console.log("new");
*** End Patch
EOF
'@
```

(C) リネーム＋更新

```powershell
bash -lc @'
apply_patch <<'EOF'
*** Begin Patch
*** Update File: src/app.py
*** Move to: src/main.py
@@ def greet():
-print("Hi")
+print("Hello, world!")
*** End Patch
EOF
'@
```

(D) 総合的な例

以下は、ファイルの追加、更新（リネーム付き）、削除を1つのパッチで実行する例です。

```powershell
bash -lc @'
apply_patch <<'EOF'
*** Begin Patch
*** Add File: hello.txt
+Hello world
*** Update File: src/app.py
*** Move to: src/main.py
@@ def greet():
-print("Hi")
+print("Hello, world!")
*** Delete File: obsolete.txt
*** End Patch
EOF
'@
```
</FileSystemOperationsGuide>

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