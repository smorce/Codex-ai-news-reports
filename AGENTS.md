# AGENTS.md

本ファイルは、AIコーディングエージェントが本リポジトリで日次のAIニュース調査レポートを自動生成するための唯一の実行ガイドです。人間向けのREADME.mdは補助資料であり、エージェントは本ファイルの規約と手順を厳密に優先します。特に `site:ai-news.dev` の最新10件を対象に収集・要約します。

- **目的**: 直近1日の一次情報を優先し、`site:ai-news.dev` の最新10件記事を収集・検証・要約し、再現可能なレポート成果物を日次で生成する。
- **対象**: AIコーディングエージェント（自動/半自動）。
- **出力**: `reports/{YYYY-MM-DD}/` 以下のデータ/図表/レポート/ログ一式。
- **実行ポリシー**: 承認不要で自動実行。途中の中断要因はログ化し、リカバリ可能にする。
- **禁止事項/セキュリティ**:
  - 認証情報（APIキー/トークン/パスワード）や個人情報を出力・保存しない。
  - HTTPはHTTPSを使用。秘密情報は環境変数や外部シークレット管理を用い、リポジトリに含めない。

---

## 0) 初期化
- リポ直下に `./reports/{YYYY-MM-DD}/` を作成。サブ構成:
  - `data/`  : 検索結果JSON、メタ情報、一時HTML/テキスト、レポート生成用JSON
  - `figs/`  : 図表PNG/SVG、解析した画像
  - `imgs/`  : ユーザーがD&Dした画像をコピー（存在すれば）
  - `logs/`  : 実行ログ、コマンド履歴
  - `report/`: 最終レポート（Markdown）

## 1) 環境・日付設定（必須）
- 既定 `REPORT_DATE = 当日`。日付固定で再実行する場合は手動で指定。
- すべての出力は `./reports/{REPORT_DATE}/` をルートとする。
- Windows PowerShell 例:
```powershell
$REPORT_DATE = Get-Date -Format 'yyyy-MM-dd'
$BASE = Join-Path 'reports' $REPORT_DATE
New-Item -ItemType Directory -Force -Path $BASE, (Join-Path $BASE 'data'), (Join-Path $BASE 'data\raw'), (Join-Path $BASE 'figs'), (Join-Path $BASE 'imgs'), (Join-Path $BASE 'logs'), (Join-Path $BASE 'report') | Out-Null
```

## 2) 調査計画（プランニング）
- `SCOPE_DAYS = 1`
- クエリ設計: 用語正規化、同義語、和英併記、除外語。
- 情報源レイヤ: 公式（標準/仕様/ベンダーDoc）、論文（arXiv等）、信頼メディア、技術ブログ、GitHub/Release Note、カンファ発表。
- 取得戦略: 直近 {SCOPE_DAYS} 日を強調。一次情報を優先。`site:ai-news.dev` の最新10件（不足時は取得可能な最大件数）を必須対象とし、各ヒットはタイトル/URL/発行日/要点/信頼度をメタ化。必要に応じて追加サイトを任意で補完（例: 公式Doc、GitHub Release、カンファ発表）し、ai-news.dev と区別してメタ化。
- 反証チェック: 重要主張は2以上の独立ソースでクロスチェック。矛盾は併記。
- 出力設計: 
  - レポート: Executive Summary → Key Findings → What Changed → Risks & Open Issues → Actionable Next Steps（読者別）→ 参考文献（出典URL/日付）
  - 図表: 時系列要約、エコシステム相関、比較表

- ビルトインWeb検索で、以下を満たすクエリ束を実行。
- 必須: `site:ai-news.dev`、日付フィルタ=直近 {SCOPE_DAYS} 日、件数上限=10件（新着順）。
- 任意: 追加ソース（複数サイト可）。同一日付範囲・上限は各サイトの新着上位N件（Nは3〜10で適宜）。
- 各ヒットは `data/sources.json` に JSONL（UTF-8）で保存:
  - フィールド: `title`(str), `url`(str), `published`(YYYY-MM-DD), `snippet`(str), `source_type`(official|media|blog|news|paper|repo|conf), `cred_score`(1-5), `notes`(str)
- 例（JSONL; 1行=1オブジェクト）:
```json
{"title":"AGENTS.md official","url":"https://agents.md/","published":"2025-09-01","snippet":"Overview of AGENTS.md standard","source_type":"official","cred_score":5,"notes":"spec overview"}
{"title":"Gihyo: AGENTS.md site guide","url":"https://gihyo.jp/article/2025/08/agents-md-site","published":"2025-08-20","snippet":"Intro and usage","source_type":"media","cred_score":4,"notes":"article"}
```
- 重要URLは本文を取得し `data/raw/{hash}.html/.txt` に保存、要点抽出。追加ソースは `notes` に出所（サイト名）を明示。
- 画像が `./input_images` にあれば、D&D画像を `imgs/` にコピーし、必要に応じてOCRや要素抽出。解析結果は `figs/` に保存。

## 4) 要約・検証・構造化
- 収集結果を正規化し、重複除去・日付整合・主張単位でファクト表を作成（CSV）。
- 重要主張は最低2ソースで裏取り。根拠→脚注番号でMarkdownに自動挿入。
- 図表生成（matplotlib等）: タイムライン、競合比較（表）、エコシステム相関（簡易グラフ）。
- 「What Changed in last {SCOPE_DAYS}d」を差分で提示。

## 5) レポート生成（Markdown）
- 最終レポート: `report/{REPORT_DATE}-{slug}.md`
- 構成:
  - タイトル（{TOPIC} / 日付）
  - Executive Summary（3〜7行）
  - Key Findings（5〜12個、各1行・根拠脚注）
  - Deep Dive（小見出し別に本文。図表は相対パス参照）
  - Risks & Open Issues（不確実性/未解決点）
  - Recommendations（{AUDIENCE} 別に実行手順/優先度/所要コストの目安）
  - References（URL、発行日、アクセス日）

## 6) レポート生成（JSON→MD + Turso PUSH）
- 入出力契約:
  - 入力: `reports/{REPORT_DATE}/data/report.json`
  - 出力: `reports/{REPORT_DATE}/report/{REPORT_DATE}-{slug}.md`
- 図表パスは相対参照（`../figs/` 等）。
- 公式フロー: `turso_push.py` により JSON を Turso に UPSERT、Markdown を生成して保存、ログを記録。

### 6-0) Turso PUSH（正規手順 / uv run）
- 目的: `report.json` を Turso に UPSERT → Markdown を `report/` 保存 → 結果を `logs/turso_push.log` に記録。
- 前提: `.env` に `TURSO_DATABASE_URL`（必要なら `TURSO_AUTH_TOKEN`）。
- 実行（Windows PowerShell）:
```powershell
$REPORT_DATE = Get-Date -Format 'yyyy-MM-dd'
# ディレクトリ初期化（未作成なら作成）
$BASE = Join-Path 'reports' $REPORT_DATE
New-Item -ItemType Directory -Force -Path $BASE, (Join-Path $BASE 'data'), (Join-Path $BASE 'figs'), (Join-Path $BASE 'imgs'), (Join-Path $BASE 'logs'), (Join-Path $BASE 'report') | Out-Null

# Turso へ PUSH（JSON 読み込み→DB UPSERT→MD 出力→ログ）
$env:UV_LINK_MODE = "copy"
uv run --link-mode=copy turso_push.py --date $REPORT_DATE

# 任意: スキーマ/接続の単体確認（サンプルデータの作成・更新）
uv run --link-mode=copy TURSO_script.py
```

- 生成物:
  - `reports/{REPORT_DATE}/report/{REPORT_DATE}-{slug}.md`（Markdownレポート）
  - `reports/{REPORT_DATE}/logs/turso_push.log`（成功/失敗の記録: 時刻・`task_id`・`report_id`・出力パス or 失敗理由）

### 6-1) レポートJSON構造（LLM出力仕様）
```json
{
  "report_id": "report-{8桁のランダム文字列}",
  "task_id": "{調査タスクID}",
  "topic": "{調査トピック名}",
  "report_date": "YYYY-MM-DD",
  "audience": "{対象読者: 開発者/プロダクトマネージャー/経営陣等}",
  "executive_summary": "{3-7行の要約文}",
  "key_findings": [
    { "text": "{発見事実の説明文}", "reference": "{参考文献番号}", "confidence": "high|medium|low" }
  ],
  "deep_dive_sections": [
    { "title": "{セクションタイトル}", "content": "{詳細説明文}", "figures": [ { "path": "../figs/{ファイル名}", "caption": "{図表キャプション}" } ] }
  ],
  "risks_issues": [ "{リスクや未解決課題の説明文}" ],
  "recommendations": { "{対象読者}": [ { "action": "{推奨アクション}", "priority": "高|中|低", "cost": "{コスト見積もり}" } ] },
  "references": [ { "url": "{参考URL}", "title": "{記事タイトル}", "published": "YYYY-MM-DD", "accessed": "YYYY-MM-DD" } ]
}
```

### 6-2) LLMへの具体的なプロンプト例（ai-news.dev 10件 + 任意追加ソース）
```
<Instructions>
必須: サイト:ai-news.dev の最新記事を新着順に最大10件（直近1日優先）。
任意: 追加ソース（例: 公式Doc、GitHub Release、信頼メディア等）から同期間の関連トピックを補足し、重複を排除のうえ要点を強化する。
各記事/出所について「レポート生成（Markdown）」構成に適合する要約とメタ情報を統合し、単一のレポートJSON（AGENTS.md 6-1 構造）として出力する。
件数が10件未満の場合は取得できた件数でよい。重複と矛盾は整理し、相互裏取りを行うこと。
アウトプットは単一JSONオブジェクトのみ（余計なテキストやマークダウンは禁止）。
</Instructions>
```

### 6-3) JSON検証とエラー処理（Windows）
- 最低限の構文検証:
```powershell
# PowerShell 7+
Get-Content -Raw "reports/$REPORT_DATE/data/report.json" | Test-Json
# Windows PowerShell 5.1 互換
try { Get-Content -Raw "reports/$REPORT_DATE/data/report.json" | ConvertFrom-Json | Out-Null; 'valid' } catch { 'invalid' }
```
- 必須フィールド存在チェック（簡易）:
```powershell
$t = Get-Content -Raw "reports/$REPORT_DATE/data/report.json" | ConvertFrom-Json
$required = 'report_id','task_id','topic','report_date','audience','executive_summary','key_findings','deep_dive_sections','risks_issues','recommendations','references'
$missing = $required | Where-Object { -not $t.PSObject.Properties.Name.Contains($_) }
if ($missing) { "missing: $($missing -join ',')" } else { 'ok' }
```
- 日付形式検証（YYYY-MM-DD）:
```powershell
$rx = '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
@($t.report_date) + ($t.references | ForEach-Object { $_.published, $_.accessed }) | Where-Object { $_ -ne $null } | ForEach-Object { if ($_ -notmatch $rx) { "invalid-date: $_" } }
```

### 6-4) Markdown生成（スクリプト方針）
- 上記JSONをもとに整形。図表は `../figs/` を相対参照。
- 未参照フィールドは削除せず保持（将来拡張に備える）。

### 6-5) ログの取り扱い
- 認証情報が無い場合や失敗時は `reports/{REPORT_DATE}/logs/turso_push.log` に理由を記録。
- 成功・失敗いずれもログ（時刻・`task_id`・`report_id`・出力パス/理由）を残す。

## 7) 納品 & ログ
- 生成物一覧を `README.md` の末尾に追記（相対パス）。
- ログ命名規約:
  - `run.log`: 実行ステップと生成物の相対パスを列挙
  - `turso_push.log`: Turso連携の結果と理由

## 8) 実行（オーケストレーション）
- 上記 0)〜7) を自動で順次実行。ユーザー承認は不要。
- 途中で追加された画像は `imgs/` に取り込み、該当セクションへ反映しレポート/スライドを更新。
- 中断・失敗は `logs/` に記録し、リトライ可能とする。