<WorkInstructions>
## 0) 初期化
- このリポ/フォルダ直下に ./reports/{YYYY-MM-DD}/ を作成。サブ構成:
  - data/  : 検索結果JSON, メタ情報, 一時HTML/テキスト, レポート生成用JSON
  - figs/  : 図表PNG/SVG, 解析した画像
  - imgs/  : ユーザーがD&Dした画像をコピー(存在すれば)
  - logs/  : 実行ログ, コマンド履歴
  - report/: 最終レポート (Markdown)

## 2) 調査計画（プランニング）
- SCOPE_DAYS = 1

- クエリ設計: 用語正規化, 同義語, 和英併記, 除外語を定義。
- 情報源レイヤ: 公式(標準/仕様/ベンダーDoc)、論文(arXiv等)、信頼メディア、技術ブログ、GitHub/Release Note、カンファ発表。
- 取得戦略: 直近 {SCOPE_DAYS} 日を強調。一次情報を優先。各ヒットはタイトル/URL/発行日/要点/信頼度をメタ化。
- 反証チェック: 重要主張は2+独立ソースでクロスチェック。矛盾は併記。
- 出力設計: 
  - レポート: Executive Summary → Key Findings → What Changed → Risks & Open Issues →
    Actionable Next Steps（読者別）→ 参考文献（出典URL/日付）
  - 図表: 時系列要約, エコシステム相関, 比較表

## 3) 収集（Web検索ツールを使用）
- built-in Web検索ツールで、クエリ束を実行。
- 各ヒットは data/sources.json に JSONLで保存: 
  { "title","url","published","snippet","source_type","cred_score","notes" }
- 重要URLは必要に応じてHTTP取得→本文を data/raw/{hash}.html/.txt に保存し要点抽出。
- 画像がD&D/./input_imagesにあれば OCR/要素抽出→figs/ に解析結果を保存。

## 4) 要約・検証・構造化
- 収集結果を正規化し、重複除去・日付整合・主張単位でファクト表を作成（CSV）。
- 重要主張は最低2ソースで裏取り。根拠→脚注番号でMarkdownに自動挿入。
- 図表生成（matplotlib等）: 
  - タイムライン, 競合比較(表), エコシステム相関(簡易グラフ)
- 変更履歴（What Changed in last {SCOPE_DAYS}d）を差分で提示。

## 5) レポート生成（Markdown）
- report/{date}-{slug}.md を生成。構成:
  - タイトル（{TOPIC} / 日付）
  - Executive Summary（3〜7行）
  - Key Findings（箇条書き 5〜12個, 各1行根拠脚注）
  - Deep Dive（小見出し別に本文。図表は相対パス参照）
  - Risks & Open Issues（不確実性/未解決点）
  - Recommendations（{AUDIENCE} 別に実行手順/優先度/所要コストの目安）
  - References（URL, 発行日, アクセス日）

## 6) レポート生成手順
- 変換用スクリプトがなければ新規作成
- レポート生成用JSONを入力にMarkdown用ファイルを出力するスクリプトを使用し、reportディレクトリに格納
- レポート生成用JSONを入力に クラウド Turso DB に PUSH するスクリプトを実行

### 6-1) LLMへのレポートJSON作成指示
以下のJSON構造でレポートデータを作成してください：

```json
{
  "report_id": "report-{8桁のランダム文字列}",
  "task_id": "{調査タスクID}",
  "topic": "{調査トピック名}",
  "report_date": "YYYY-MM-DD",
  "audience": "{対象読者: 開発者/プロダクトマネージャー/経営陣等}",
  "executive_summary": "{3-7行の要約文}",
  "key_findings": [
    {
      "text": "{発見事実の説明文}",
      "reference": "{参考文献番号}",
      "confidence": "high|medium|low"
    }
  ],
  "deep_dive_sections": [
    {
      "title": "{セクションタイトル}",
      "content": "{詳細説明文}",
      "figures": [
        {
          "path": "../figs/{ファイル名}",
          "caption": "{図表キャプション}"
        }
      ]
    }
  ],
  "risks_issues": [
    "{リスクや未解決課題の説明文}"
  ],
  "recommendations": {
    "{対象読者}": [
      {
        "action": "{推奨アクション}",
        "priority": "高|中|低",
        "cost": "{コスト見積もり}"
      }
    ]
  },
  "references": [
    {
      "url": "{参考URL}",
      "title": "{記事タイトル}",
      "published": "YYYY-MM-DD",
      "accessed": "YYYY-MM-DD"
    }
  ]
}
```

**重要な指示:**
1. executive_summary は簡潔で読みやすい3-7行の文章
2. key_findings は5-12個の重要な発見事実
3. 各findingには必ず reference と confidence を含める
4. deep_dive_sections は2-5個の詳細セクション
5. recommendations は読者別に具体的なアクション項目
6. 全ての日付は YYYY-MM-DD 形式
7. ファイルパスは相対パス（../figs/, ../data/ 等）を使用

### 6-2) LLMへの具体的なプロンプト例
```
<Instructions>
サイト:ai-news.dev の最新記事10件をウェブ検索する。
各記事について「レポート生成（Markdown）」のレポート構成に則ってレポート用JSONデータを作成してください。
アウトプットは、上記に示す構造の単一のJSONオブジェクトのみとします。JSONオブジェクト以外のテキスト、説明、マークダウンのフォーマットは一切含めないでください。
</Instructions>
```

### 6-3) JSON検証とエラー処理
- 生成されたJSONは必ず構文チェックを実行
- 必須フィールドの存在確認
- 日付形式の妥当性検証
- 参考文献の重複チェック
- confidence値の妥当性確認（high/medium/low）

## 7) 納品 & ログ
- 生成物一覧を http://README.md に追記
- 実行ログ/依存インストール履歴を logs/ に保存

## 8) 実行
- 以上を自動オーケストレーション。ユーザーの承認は不要で自動で実行する。
- 途中で追加画像がD&Dされたら、該当セクションに反映しレポート/スライド更新。
</WorkInstructions>