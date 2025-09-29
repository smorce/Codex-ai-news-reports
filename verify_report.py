import json

with open("reports/2025-09-29/report.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(repr(data["articles"][0]["executive_summary"][0]))
print(repr(data["articles"][1]["executive_summary"][0]))
