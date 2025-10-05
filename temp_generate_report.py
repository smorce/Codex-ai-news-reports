import json
import re
from pathlib import Path

INPUT_PATH = Path('reports/2025-10-05/rss_sources.json')
GENERATED_AT = '2025-10-05T17:16:57Z'


def remove_emoji(text: str) -> str:
    def _is_emoji(ch: str) -> bool:
        code = ord(ch)
        return (
            0x1F000 <= code <= 0x1FAFF
            or 0x1F300 <= code <= 0x1F6FF
            or 0x1F900 <= code <= 0x1F9FF
            or 0x2600 <= code <= 0x27BF
            or 0xFE00 <= code <= 0xFE0F
        )

    return ''.join(ch for ch in text if not _is_emoji(ch))


def sanitize_text(text: str) -> str:
    if not text:
        return ''
    text = text.replace('\r', '\n')
    text = text.replace('\u3000', ' ')
    text = remove_emoji(text)
    # 正規化: 連続空白を1つに、改行前後の空白を除去
    text = re.sub(r'[\t\f\v]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    lines = [line.strip() for line in text.split('\n')]
    lines = [line for line in lines if line]
    return '\n'.join(lines)


SENTENCE_PATTERN = re.compile(r'[^。！？!?]+[。！？!?]?')


def split_sentences(text: str) -> list[str]:
    sentences: list[str] = []
    for line in text.split('\n'):
        line = line.strip(' ・*\u2022\u25cf\u25a0\u25e6\u3001')
        if not line:
            continue
        for fragment in SENTENCE_PATTERN.findall(line):
            frag = fragment.strip()
            if not frag:
                continue
            if frag[-1] not in '。！？!?':
                frag += '。'
            if len(frag) < 4:
                continue
            if frag not in sentences:
                sentences.append(frag)
    if len(sentences) < 3:
        extra_parts = re.split(r'[、,]', text)
        for part in extra_parts:
            frag = part.strip()
            if len(frag) < 4:
                continue
            if frag[-1] not in '。！？!?':
                frag += '。'
            if frag not in sentences:
                sentences.append(frag)
            if len(sentences) >= 3:
                break
    return sentences


def build_summary(sentences: list[str]) -> list[str]:
    if not sentences:
        return ['情報が不足しているため詳細不明。'] * 3
    count = min(max(3, len(sentences)), 7)
    return sentences[:count]


def build_key_findings(sentences: list[str], url: str, exclude: set[str]) -> list[dict]:
    if not sentences:
        sentences = ['記事本文の情報が取得できませんでした。'] * 5
    max_len = 12
    min_len = 5
    desired = max(min_len, min(len(sentences), max_len))
    findings: list[dict] = []
    used_points: set[str] = set()

    def add_sentence(sentence: str) -> None:
        point_text = sentence.rstrip('。！？!?')
        if point_text in used_points:
            return
        used_points.add(point_text)
        footnote_text = f"{sentence} 出典: {url}" if url else sentence
        findings.append({
            'point': point_text,
            'footnote': footnote_text,
        })

    for sentence in sentences:
        if sentence in exclude:
            continue
        add_sentence(sentence)
        if len(findings) >= desired:
            break

    if len(findings) < desired:
        for sentence in sentences:
            add_sentence(sentence)
            if len(findings) >= desired:
                break

    if len(findings) < min_len and sentences:
        fallback = sentences[-1]
        while len(findings) < min_len:
            add_sentence(fallback)

    return findings


def main() -> None:
    data = json.loads(INPUT_PATH.read_text(encoding='utf-8'))
    site = data.get('site', '')
    sources = data.get('sources', [])
    articles_output = []

    for item in sources:
        url = item.get('url', '')
        title = item.get('title', '')
        date = item.get('date') or None
        raw_text = item.get('text', '')
        sanitized = sanitize_text(raw_text)
        sentences = split_sentences(sanitized)
        summary = build_summary(sentences)
        key_findings = build_key_findings(sentences, url, exclude=set(summary))

        articles_output.append({
            'url': url,
            'title': title,
            'date': date,
            'executive_summary': summary,
            'key_findings': key_findings,
            'references': [url] if url else [],
            'retrieved_at': GENERATED_AT,
        })

    report = {
        'generated_at': GENERATED_AT,
        'site': site,
        'num_articles': len(articles_output),
        'articles': articles_output,
    }

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
