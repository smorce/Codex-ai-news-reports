import json
from pathlib import Path

data_path = Path("reports/2025-10-06/rss_sources.json")
output_path = Path("articles_dump.txt")

with data_path.open("r", encoding="utf-8") as f:
    data = json.load(f)

lines: list[str] = []
for idx, item in enumerate(data.get("sources", []), start=1):
    text = (item.get("text") or "")
    lines.append(f"[{idx}] {item.get('title')}")
    lines.append(f"URL: {item.get('url')}")
    lines.append(f"Date: {item.get('date')}")
    lines.append(f"Text ({len(text)} chars): {text}")
    lines.append("")

output_path.write_text("\n".join(lines), encoding="utf-8")
