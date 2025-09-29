<Variables>
NUM_ARTICLES = 2
SITE = "ai-news.dev"
OUTPUT_DIR = "reports/{YYYY-MM-DD}"
OUTPUT_FILE = "report.json"
</Variables>

<Instructions>
1. Generate a SOW (Statement of Work) before starting the task.
2. Search the web for the latest {NUM_ARTICLES} articles from site:{SITE}.
3. For each article, extract:
   - Title
   - Publication date (if available)
   - Executive Summary (3–7 lines)
   - Key Findings (5–12 bullet points, each with a supporting footnote)
   - References
4. **CRITICAL**: After completing the analysis, you MUST create and save the JSON file to the specified path.
5. **MANDATORY**: Use the `write` tool to create the JSON file at {OUTPUT_DIR}/{OUTPUT_FILE} with the complete report data.
6. **VERIFICATION**: Confirm the JSON file has been created successfully before ending the task.
</Instructions>

<Web Search Requirements>
- Use Chrome DevTools MCP for web searches
- This ensures proper browser automation and content extraction capabilities
- When a URL is specified, open the URL and wait until the page is stable before proceeding
- To open a specific URL, use: chrome-devtools.new_page({"url":{SITE}})
</Web Search Requirements>

<Output Constraints>
- Format: JSON only (Markdown not permitted).
- Save Path: {OUTPUT_DIR}/{OUTPUT_FILE}
- Required JSON Structure:
```json
{
  "site": "ai-news.dev",
  "generated_at": "YYYY-MM-DD HH:MM:SS",
  "num_articles": 2,
  "articles": [
    {
      "title": "Article Title",
      "date": "YYYY-MM-DD",
      "executive_summary": [
        "Summary line 1",
        "Summary line 2",
        "Summary line 3"
      ],
      "key_findings": [
        {
          "point": "Key finding description",
          "footnote": "Supporting footnote"
        }
      ],
      "references": [
        "Reference 1",
        "Reference 2"
      ]
    }
  ]
}
```
</Output Constraints>

Python is available in the current environment.
To use Python, execute the command as follows:
`uv run --link-mode=copy script.py`