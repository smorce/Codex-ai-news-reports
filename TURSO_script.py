# 実行方法
# uv run TURSO_script.py

# メモ
# libsql でリモート URL を直接指定して動かす前提に合わせ、ORM 層（SQLModel/SQLAlchemy）を外し、すべて libsql の生クエリで完結するようにリファクタしました。JSON は SQLite では TEXT に保存し、入出力時に json.dumps / json.loads で扱います。テーブル作成もリモートに対して実行します。
# すべてのクエリがリモートで実行され、余計なファイルや接続の衝突(WAL衝突)を起こしません。

import os
import time
import json
import uuid
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from datetime import datetime
from dotenv import load_dotenv
import libsql

# ====== .env 読み込み ======
# 同ディレクトリ直下の .env を読み込みます。既存の環境変数は優先（override=False）。
# 例)
load_dotenv(dotenv_path=".env", override=False)

# ====== 設定（.env / 環境変数から取得） ======
TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL", "")
TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN", "")

if not TURSO_DATABASE_URL:
    raise RuntimeError(
        "TURSO_DATABASE_URL が未設定です。.env に TURSO_DATABASE_URL=... を記載してください。"
    )
# 認証不要の DB なら空でも動作可。必要なら以下を有効化
# if not TURSO_AUTH_TOKEN:
#     raise RuntimeError("TURSO_AUTH_TOKEN が未設定です。.env に TURSO_AUTH_TOKEN=... を記載してください。")

# ====== 接続（リモート直結） ======
# リモート URL を直に渡すと、すべてのクエリがリモートで実行されます
conn = libsql.connect(TURSO_DATABASE_URL, auth_token=TURSO_AUTH_TOKEN)

# ====== スキーマ（reports のみ） ======
DDL_REPORTS = """
CREATE TABLE IF NOT EXISTS reports (
  report_id TEXT PRIMARY KEY,
  task_id TEXT NOT NULL,
  topic TEXT NOT NULL,
  report_date TEXT NOT NULL,
  audience TEXT,
  executive_summary TEXT NOT NULL,
  key_findings_json TEXT NOT NULL,
  deep_dive_sections_json TEXT NOT NULL,
  risks_issues_json TEXT NOT NULL,
  recommendations_json TEXT NOT NULL,
  references_json TEXT NOT NULL,
  markdown_content TEXT,
  created_at REAL NOT NULL,
  updated_at REAL
);
"""

def create_tables() -> None:
    """必要なテーブル（reports のみ）を作成"""
    conn.execute(DDL_REPORTS)
    conn.commit()
    print("テーブル作成: 完了（reports）")

# ====== データモデル ======
@dataclass
class ReportData:
    report_id: str
    task_id: str
    topic: str
    report_date: str
    audience: Optional[str]
    executive_summary: str
    key_findings: List[Dict[str, Any]] = field(default_factory=list)
    deep_dive_sections: List[Dict[str, Any]] = field(default_factory=list)
    risks_issues: List[str] = field(default_factory=list)
    recommendations: Dict[str, List[Dict[str, Any]]] = field(default_factory=dict)
    references: List[Dict[str, Any]] = field(default_factory=list)
    markdown_content: Optional[str] = None
    created_at: float = field(default_factory=lambda: time.time())
    updated_at: Optional[float] = None

# ====== レポート Markdown 生成 ======
def generate_markdown_report(report_data: ReportData) -> str:
    md = []
    md.append(f"# {report_data.topic} / {report_data.report_date}\n")
    md.append("## Executive Summary\n")
    md.append(f"{report_data.executive_summary}\n")

    md.append("## Key Findings\n")
    for i, finding in enumerate(report_data.key_findings, 1):
        text = finding.get("text", "")
        ref = finding.get("reference", "")
        md.append(f"{i}. {text}" + (f" [{ref}]" if ref else "") + "\n")
    md.append("\n")

    if report_data.deep_dive_sections:
        md.append("## Deep Dive\n")
        for section in report_data.deep_dive_sections:
            title = section.get("title", "")
            content = section.get("content", "")
            figures = section.get("figures", [])
            md.append(f"### {title}\n\n{content}\n\n")
            for fig in figures:
                path = fig.get("path", "")
                cap = fig.get("caption", "")
                if path:
                    md.append(f"![{cap}]({path})\n\n")

    if report_data.risks_issues:
        md.append("## Risks & Open Issues\n")
        for risk in report_data.risks_issues:
            md.append(f"- {risk}\n")
        md.append("\n")

    if report_data.recommendations:
        md.append("## Recommendations\n")
        for audience, recs in report_data.recommendations.items():
            md.append(f"### {audience}\n\n")
            for rec in recs:
                action = rec.get("action", "")
                priority = rec.get("priority", "")
                cost = rec.get("cost", "")
                md.append(f"- **{action}** (優先度: {priority}, コスト: {cost})\n")
            md.append("\n")

    if report_data.references:
        md.append("## References\n")
        for i, ref in enumerate(report_data.references, 1):
            url = ref.get("url", "")
            title = ref.get("title", "")
            published = ref.get("published", "")
            accessed = ref.get("accessed", "")
            md.append(f"{i}. [{title}]({url}) (発行日: {published}, アクセス日: {accessed})\n")

    return "".join(md)

# ====== DB I/O（reports のみ） ======
def save_report_to_db(report_data: ReportData) -> str:
    """reports に UPSERT"""
    markdown_content = generate_markdown_report(report_data)
    now = time.time()
    report_data.markdown_content = markdown_content
    report_data.updated_at = now

    conn.execute(
        """
        INSERT INTO reports (
          report_id, task_id, topic, report_date, audience, executive_summary,
          key_findings_json, deep_dive_sections_json, risks_issues_json,
          recommendations_json, references_json, markdown_content,
          created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(report_id) DO UPDATE SET
          task_id=excluded.task_id,
          topic=excluded.topic,
          report_date=excluded.report_date,
          audience=excluded.audience,
          executive_summary=excluded.executive_summary,
          key_findings_json=excluded.key_findings_json,
          deep_dive_sections_json=excluded.deep_dive_sections_json,
          risks_issues_json=excluded.risks_issues_json,
          recommendations_json=excluded.recommendations_json,
          references_json=excluded.references_json,
          markdown_content=excluded.markdown_content,
          updated_at=excluded.updated_at
        """,
        (
            report_data.report_id,
            report_data.task_id,
            report_data.topic,
            report_data.report_date,
            report_data.audience,
            report_data.executive_summary,
            json.dumps(report_data.key_findings, ensure_ascii=False),
            json.dumps(report_data.deep_dive_sections, ensure_ascii=False),
            json.dumps(report_data.risks_issues, ensure_ascii=False),
            json.dumps(report_data.recommendations, ensure_ascii=False),
            json.dumps(report_data.references, ensure_ascii=False),
            report_data.markdown_content,
            report_data.created_at,
            report_data.updated_at,
        ),
    )
    conn.commit()
    return markdown_content

def get_report_from_db(report_id: str) -> Optional[ReportData]:
    cur = conn.execute(
        """
        SELECT report_id, task_id, topic, report_date, audience, executive_summary,
               key_findings_json, deep_dive_sections_json, risks_issues_json,
               recommendations_json, references_json, markdown_content,
               created_at, updated_at
        FROM reports WHERE report_id = ?
        """,
        (report_id,),
    )
    row = cur.fetchone()
    if not row:
        return None

    return ReportData(
        report_id=row[0],
        task_id=row[1],
        topic=row[2],
        report_date=row[3],
        audience=row[4],
        executive_summary=row[5],
        key_findings=json.loads(row[6]) if row[6] else [],
        deep_dive_sections=json.loads(row[7]) if row[7] else [],
        risks_issues=json.loads(row[8]) if row[8] else [],
        recommendations=json.loads(row[9]) if row[9] else {},
        references=json.loads(row[10]) if row[10] else [],
        markdown_content=row[11],
        created_at=row[12],
        updated_at=row[13],
    )

def list_reports_from_db() -> List[ReportData]:
    cur = conn.execute(
        """
        SELECT report_id, task_id, topic, report_date, audience, executive_summary,
               key_findings_json, deep_dive_sections_json, risks_issues_json,
               recommendations_json, references_json, markdown_content,
               created_at, updated_at
        FROM reports
        ORDER BY created_at DESC
        """
    )
    rows = cur.fetchall()
    results: List[ReportData] = []
    for row in rows:
        results.append(
            ReportData(
                report_id=row[0],
                task_id=row[1],
                topic=row[2],
                report_date=row[3],
                audience=row[4],
                executive_summary=row[5],
                key_findings=json.loads(row[6]) if row[6] else [],
                deep_dive_sections=json.loads(row[7]) if row[7] else [],
                risks_issues=json.loads(row[8]) if row[8] else [],
                recommendations=json.loads(row[9]) if row[9] else {},
                references=json.loads(row[10]) if row[10] else [],
                markdown_content=row[11],
                created_at=row[12],
                updated_at=row[13],
            )
        )
    return results

# ====== サンプルデータ作成 ======
def create_sample_report_data() -> ReportData:
    current_date = datetime.now().strftime("%Y-%m-%d")
    report_id = f"report-{uuid.uuid4().hex[:8]}"

    key_findings = [
        {"text": "Turso DBは分散SQLiteデータベースとして高いパフォーマンスを提供", "reference": "1", "confidence": "high"},
        {"text": "libsql-experimentalライブラリによりPythonから簡単にアクセス可能", "reference": "2", "confidence": "high"},
        {"text": "同期機能により複数のレプリカ間でデータの整合性を保持", "reference": "3", "confidence": "medium"},
        {"text": "SQLModelとの統合により型安全なデータベース操作が可能", "reference": "4", "confidence": "high"},
        {"text": "クラウドとローカルの両方でシームレスな動作を実現", "reference": "5", "confidence": "medium"},
    ]

    deep_dive_sections = [
        {
            "title": "Turso DB アーキテクチャ",
            "content": "Turso DBは分散SQLiteアーキテクチャを採用し、複数のレプリカ間でデータの同期を行います。libsql-experimentalライブラリを使用することで、Pythonアプリケーションから直接アクセスが可能になります。",
            "figures": [{"path": "../figs/turso-architecture.png", "caption": "Turso DB アーキテクチャ図"}],
        },
        {
            "title": "パフォーマンス特性",
            "content": "ベンチマークテストの結果、Turso DBは従来のPostgreSQLと比較して読み取り操作で約30%の性能向上を示しました。特に分散環境での同期処理において優れた性能を発揮します。",
            "figures": [{"path": "../figs/performance-comparison.png", "caption": "パフォーマンス比較グラフ"}],
        },
    ]

    risks_issues = [
        "実験的ライブラリ（libsql-experimental）のため、本番環境での安定性に不確実性がある",
        "ドキュメンテーションが限定的で、トラブルシューティングが困難な場合がある",
        "大規模なデータセットでの性能特性が未検証",
        "エコシステムの成熟度が他のデータベースソリューションと比較して低い",
    ]

    recommendations = {
        "開発者": [
            {"action": "小規模なプロトタイプでTurso DBの動作を検証する", "priority": "高", "cost": "低（1-2日）"},
            {"action": "既存のSQLiteアプリケーションからの移行パスを調査する", "priority": "中", "cost": "中（1週間）"},
        ],
        "プロダクトマネージャー": [
            {"action": "ビジネス要件とTurso DBの機能マッチングを評価する", "priority": "高", "cost": "中（3-5日）"},
            {"action": "競合データベースソリューションとのコスト比較を実施する", "priority": "中", "cost": "中（1週間）"},
        ],
        "DevOpsエンジニア": [
            {"action": "Turso DBの監視・運用手順を策定する", "priority": "中", "cost": "高（2-3週間）"}
        ],
    }

    references = [
        {"url": "https://turso.tech/docs", "title": "Turso Database Documentation", "published": "2024-09-20", "accessed": current_date},
        {"url": "https://github.com/tursodatabase/libsql-experimental-python", "title": "libsql-experimental Python Library", "published": "2024-09-15", "accessed": current_date},
        {"url": "https://blog.turso.tech/introducing-turso-db", "title": "Introducing Turso: The Edge Database", "published": "2024-08-30", "accessed": current_date},
        {"url": "https://sqlmodel.tiangolo.com/", "title": "SQLModel Documentation", "published": "2024-09-10", "accessed": current_date},
        {"url": "https://benchmarks.turso.tech/", "title": "Turso Performance Benchmarks", "published": "2024-09-25", "accessed": current_date},
    ]

    return ReportData(
        report_id=report_id,
        task_id="test-18675145",
        topic="Turso DB と Python 統合の技術調査",
        report_date=current_date,
        audience="開発チーム",
        executive_summary=(
            "Turso DBは分散SQLiteデータベースとして、Pythonアプリケーションとの統合において優れた性能と柔軟性を提供します。"
            "libsql-experimentalライブラリを使用することで、型安全なデータベース操作が可能になり、クラウドとローカル環境でのシームレスな動作を実現できます。"
            "ただし、実験的な性質により本番環境での採用には慎重な検討が必要です。"
        ),
        key_findings=key_findings,
        deep_dive_sections=deep_dive_sections,
        risks_issues=risks_issues,
        recommendations=recommendations,
        references=references,
    )

# ====== 動作テスト ======
def test_report_generation():
    try:
        create_tables()
        sample_report = create_sample_report_data()
        markdown_content = save_report_to_db(sample_report)

        print("=== 生成されたMarkdownレポート（先頭500文字） ===")
        print(markdown_content[:500] + ("..." if len(markdown_content) > 500 else ""))

        print("\n=== データベースへの保存完了 ===")
        print(f"レポートID: {sample_report.report_id}")
        print(f"タスクID: {sample_report.task_id}")
        print(f"トピック: {sample_report.topic}")
        print(f"作成日時: {datetime.fromtimestamp(sample_report.created_at)}")

        saved_report = get_report_from_db(sample_report.report_id)
        if saved_report:
            print(f"データベース読み取りテスト: 成功 (ID: {saved_report.report_id})")
        else:
            print("データベース読み取りテスト: 失敗")

        reports = list_reports_from_db()
        print(f"保存されているレポート数: {len(reports)}")

        return sample_report, markdown_content

    except Exception as e:
        print(f"テスト実行中にエラーが発生しました: {e}")
        import traceback
        traceback.print_exc()
        return None, None


# テスト実行
if __name__ == "__main__":
    test_report_generation()