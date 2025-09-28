<Variables>
NUM_ARTICLES = 3
SITE = "ai-news.dev"
OUTPUT_DIR = "reports/{YYYY-MM-DD}"
OUTPUT_FILE = "report.json"
</Variables>

<Instructions>
1. Search the web for the latest {NUM_ARTICLES} articles from site:{SITE}.
2. For each article, extract:
   - Title
   - Publication date (if available)
   - Executive Summary (3–7 lines)
   - Key Findings (5–12 bullet points, each with a supporting footnote)
   - References
</Instructions>

<Output Constraints>
- Format: JSON only (Markdown not permitted).
- Save Path: {OUTPUT_DIR}/{OUTPUT_FILE}
</Output Constraints>
