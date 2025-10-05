import json
from pathlib import Path

path = Path('reports/2025-10-05/rss_sources.json')
data = json.loads(path.read_text(encoding='utf-8'))

for idx, item in enumerate(data.get('sources', []), start=1):
    title = item.get('title', '')
    url = item.get('url', '')
    date = item.get('date')
    text = item.get('text', '')
    text_repr = text.encode('unicode_escape').decode()
    title_repr = title.encode('unicode_escape').decode()
    print(f'#{idx} title repr: {title_repr}')
    print(f'   url: {url}')
    print(f'   date: {date}')
    print(f'   text repr: {text_repr}')
    print('-' * 40)
