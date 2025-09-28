# 一括投入ユーティリティ
from typing import Iterable

REQUIRED_KEYS = {
    "report_id", "task_id", "topic", "report_date", "executive_summary",
    "key_findings", "deep_dive_sections", "risks_issues", "recommendations", "references"
}

def push_reports(dataset: Iterable[dict]) -> tuple[int, int]:
    """
    dataset: ReportData 互換の dict 群（あなたが示した形式）
    return: (成功件数, 失敗件数)
    """
    ok = fail = 0
    cur = conn.cursor()
    try:
        for i, d in enumerate(dataset, start=1):
            # 必須キーの簡易チェック
            missing = REQUIRED_KEYS - set(d.keys())
            if missing:
                raise ValueError(f"[item {i}] missing keys: {sorted(missing)}")

            # dataclass に落として型/デフォルトを揃える
            rd = ReportData(
                report_id=d["report_id"],
                task_id=d["task_id"],
                topic=d["topic"],
                report_date=d["report_date"],        # 例: "2025-09-28"
                audience=d.get("audience"),
                executive_summary=d["executive_summary"],
                key_findings=d.get("key_findings", []),
                deep_dive_sections=d.get("deep_dive_sections", []),
                risks_issues=d.get("risks_issues", []),
                recommendations=d.get("recommendations", {}),
                references=d.get("references", []),
                markdown_content=d.get("markdown_content"),
                created_at=d.get("created_at", time.time()),
                updated_at=d.get("updated_at"),
            )

            # 既存の save 関数で UPSERT
            _ = save_report_to_db(rd)
            ok += 1

        conn.commit()
        return ok, fail
    except Exception:
        conn.rollback()
        fail += 1
        raise
    finally:
        cur.close()



dataset = [
    {
        "report_id": "report-abc12345",  # 既存と被れば更新・初めてなら作成
        "task_id": "test-18675145",
        "topic": "Turso DB と Python 統合の技術調査",
        "report_date": datetime.now().strftime("%Y-%m-%d"),
        "audience": "開発チーム",
        "executive_summary": "・・・",
        "key_findings": key_findings,                 # ← あなたの配列をそのまま
        "deep_dive_sections": deep_dive_sections,     # ← そのまま
        "risks_issues": risks_issues,                 # ← そのまま
        "recommendations": recommendations,           # ← そのまま
        "references": references,                     # ← そのまま
        # 任意: "markdown_content": "..."（未指定なら自動生成）
    },
    # 複数件あれば続けて並べる
]

create_tables()  # 初回のみ
ok, fail = push_reports(dataset)
print(f"pushed: {ok}, failed: {fail}")