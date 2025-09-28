"""
レポートJSON（reports/{REPORT_DATE}/data/report.json）を読み込み、
Turso(libsql)へUPSERTし、Markdownを生成して保存、ログを記録するスクリプト。

実行例 (PowerShell):
  $REPORT_DATE = Get-Date -Format 'yyyy-MM-dd'
  uv run turso_push.py --date $REPORT_DATE

前提:
  - .env に TURSO_DATABASE_URL, （必要なら）TURSO_AUTH_TOKEN
  - レポートJSON は単一オブジェクトで AGENTS.md 6-1 のスキーマに準拠
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from dotenv import load_dotenv

# TURSO_script の既存実装を利用（DB接続・UPSERT・MD生成）
from TURSO_script import (
    ReportData,
    create_tables,
    save_report_to_db,
    generate_markdown_report,
)


REQUIRED_FIELDS = {
    "report_id",
    "task_id",
    "topic",
    "report_date",
    "audience",
    "executive_summary",
    "key_findings",
    "deep_dive_sections",
    "risks_issues",
    "recommendations",
    "references",
}


def slugify(text: str) -> str:
    """トピックから簡易スラッグを生成（ASCII, kebab-case）。"""
    text_ascii = (
        text.lower()
        .strip()
        .replace("/", " ")
        .replace("\\", " ")
    )
    # 非英数字を区切りへ
    text_ascii = re.sub(r"[^a-z0-9]+", "-", text_ascii)
    text_ascii = text_ascii.strip("-")
    return text_ascii or "report"


def ensure_dirs(base: Path) -> None:
    (base / "data").mkdir(parents=True, exist_ok=True)
    (base / "figs").mkdir(parents=True, exist_ok=True)
    (base / "imgs").mkdir(parents=True, exist_ok=True)
    (base / "logs").mkdir(parents=True, exist_ok=True)
    (base / "report").mkdir(parents=True, exist_ok=True)


def read_report_json(path: Path) -> Dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("report.json must be a single JSON object.")
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"report.json not found: {path}")


def validate_fields(d: Dict[str, Any]) -> None:
    missing = [k for k in sorted(REQUIRED_FIELDS) if k not in d]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")


def write_markdown(md_content: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md_content, encoding="utf-8")


def append_log(log_path: Path, message: str) -> None:
    timestamp = datetime.utcnow().isoformat(timespec="seconds") + "Z"
    line = f"{timestamp} {message}\n"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(line)


def to_report_data(d: Dict[str, Any]) -> ReportData:
    return ReportData(
        report_id=d["report_id"],
        task_id=d["task_id"],
        topic=d["topic"],
        report_date=d["report_date"],
        audience=d.get("audience"),
        executive_summary=d["executive_summary"],
        key_findings=d.get("key_findings", []),
        deep_dive_sections=d.get("deep_dive_sections", []),
        risks_issues=d.get("risks_issues", []),
        recommendations=d.get("recommendations", {}),
        references=d.get("references", []),
        markdown_content=d.get("markdown_content"),
        created_at=d.get("created_at") or datetime.utcnow().timestamp(),
        updated_at=d.get("updated_at"),
    )


def main() -> int:
    load_dotenv(dotenv_path=".env", override=False)

    parser = argparse.ArgumentParser(description="Push report.json to Turso and write Markdown")
    parser.add_argument(
        "--date",
        dest="report_date",
        default=datetime.now().strftime("%Y-%m-%d"),
        help="REPORT_DATE (YYYY-MM-DD). Defaults to today.",
    )
    parser.add_argument(
        "--input",
        dest="input_path",
        default=None,
        help="Override input JSON path. If not set, uses reports/{REPORT_DATE}/data/report.json",
    )
    args = parser.parse_args()

    report_date = args.report_date
    base = Path("reports") / report_date
    ensure_dirs(base)

    json_path = Path(args.input_path) if args.input_path else (base / "data" / "report.json")
    log_path = base / "logs" / "turso_push.log"

    try:
        # JSON 読み込み・検証
        d = read_report_json(json_path)
        validate_fields(d)

        # DB テーブル確保とUPSERT
        create_tables()
        report_data = to_report_data(d)
        markdown_content = save_report_to_db(report_data)

        # Markdown 書き出し
        slug = slugify(report_data.topic)
        md_out = base / "report" / f"{report_date}-{slug}.md"
        if not markdown_content:
            markdown_content = generate_markdown_report(report_data)
        write_markdown(markdown_content, md_out)

        append_log(
            log_path,
            f"SUCCESS task_id={report_data.task_id} report_id={report_data.report_id} md={md_out.as_posix()}",
        )
        print(f"PUSH SUCCESS: report_id={report_data.report_id} -> {md_out}")
        return 0
    except Exception as e:
        append_log(log_path, f"FAIL reason={e}")
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())


