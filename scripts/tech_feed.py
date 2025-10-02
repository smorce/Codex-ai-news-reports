#!/usr/bin/env python3
# scripts/tech_feed.py

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, List, Optional

import feedparser
import requests
from bs4 import BeautifulSoup


@dataclass
class FeedEntry:
    feed_name: str
    title: str
    url: str
    published_at: Optional[datetime]
    text: str
    category: str


def _read_feed_config(feed_file: Path) -> Dict[str, List[str]]:
    import tomllib

    with open(feed_file, "rb") as f:
        data = tomllib.load(f)
    # 各カテゴリは配列前提
    normalized: Dict[str, List[str]] = {}
    for key, value in data.items():
        if isinstance(value, list):
            normalized[str(key)] = [str(u) for u in value]
    return normalized


def _parse_entry_datetime(entry) -> Optional[datetime]:
    try:
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            return datetime(*entry.published_parsed[:6])
        if hasattr(entry, "updated_parsed") and entry.updated_parsed:
            return datetime(*entry.updated_parsed[:6])
    except Exception:
        pass
    return None


def _extract_article_text(entry, url: str, session: requests.Session) -> str:
    # 1) エントリの summary
    if hasattr(entry, "summary") and entry.summary:
        return BeautifulSoup(entry.summary, "html.parser").get_text(" ", strip=True)

    # 2) 本文ページから抽出（meta description → pタグ前方）
    try:
        resp = session.get(url, timeout=15)
        if resp.status_code != 200:
            return ""
        soup = BeautifulSoup(resp.text, "html.parser")

        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc and meta_desc.get("content"):
            return str(meta_desc.get("content")).strip()

        paragraphs = soup.find_all("p")
        if paragraphs:
            texts = [p.get_text(" ", strip=True) for p in paragraphs[:6]]
            return "\n".join([t for t in texts if t])
    except Exception:
        return ""

    return ""


def _split_sentences(text: str, max_sentences: int) -> List[str]:
    if not text:
        return []
    # 英日混在の簡易分割
    sentences = re.split(r"(?<=[。！？!?\.!])\s+|\n+", text)
    cleaned = [s.strip() for s in sentences if s and len(s.strip()) > 0]
    return cleaned[:max_sentences]


def collect_tech_feed_report(
    feed_file: Path,
    days: int = 1,
    limit_per_feed: int = 3,
) -> Dict[str, object]:
    """技術ブログ RSS を収集し、レポートJSON（本プロジェクトのスキーマ）を返す。"""
    config = _read_feed_config(feed_file)

    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        }
    )

    cutoff = datetime.now() - timedelta(days=days)
    collected: List[FeedEntry] = []

    for category, feed_urls in config.items():
        for feed_url in feed_urls:
            try:
                parsed = feedparser.parse(feed_url)
                feed_name = (
                    parsed.feed.title if hasattr(parsed, "feed") and hasattr(parsed.feed, "title") else feed_url
                )
                entries = list(getattr(parsed, "entries", []))

                # 日付フィルタ → 新しい順にして limit
                filtered: List = []
                for e in entries:
                    dt = _parse_entry_datetime(e)
                    if dt is None or dt >= cutoff:
                        filtered.append((dt or datetime.now(), e))
                filtered.sort(key=lambda x: x[0], reverse=True)
                filtered = [e for _dt, e in filtered[:limit_per_feed]]

                for e in filtered:
                    url = getattr(e, "link", None)
                    if not url:
                        continue
                    title = getattr(e, "title", "無題")
                    published_at = _parse_entry_datetime(e)
                    text = _extract_article_text(e, url, session)

                    collected.append(
                        FeedEntry(
                            feed_name=feed_name,
                            title=title,
                            url=url,
                            published_at=published_at,
                            text=text,
                            category=category,
                        )
                    )
            except Exception:
                # フィード単位の失敗は握り潰し
                continue

    # JSON スキーマへ整形
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    articles: List[Dict[str, object]] = []

    for item in collected:
        # Executive Summary: 本文先頭から 3–5 行を目安に生成
        summary_lines = _split_sentences(item.text, max_sentences=5)
        if not summary_lines:
            summary_lines = [f"{item.feed_name} の記事。カテゴリ: {item.category}"]

        # Key Findings: 重要そうな先頭3文を point に（簡易）
        kfs: List[Dict[str, str]] = []
        for s in summary_lines[:3]:
            kfs.append({"point": s, "footnote": item.url})

        articles.append(
            {
                "url": item.url,
                "title": item.title,
                "date": item.published_at.strftime("%Y-%m-%dT%H:%M:%S") if item.published_at else None,
                "executive_summary": summary_lines[:7],
                "key_findings": kfs,
                "references": [item.url],
                "retrieved_at": now_utc,
            }
        )

    report_obj: Dict[str, object] = {
        "generated_at": now_utc,
        "site": "tech-blogs",
        "num_articles": len(articles),
        "articles": articles,
    }

    return report_obj


def collect_rss_sources(
    feed_file: Path,
    days: int = 1,
    limit_per_feed: int = 3,
) -> Dict[str, object]:
    """RSSソースを機械的に収集して生データJSONを返す。LLM処理は含まない。"""
    config = _read_feed_config(feed_file)

    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        }
    )

    cutoff = datetime.now() - timedelta(days=days)
    sources: List[Dict[str, object]] = []

    for category, feed_urls in config.items():
        for feed_url in feed_urls:
            try:
                parsed = feedparser.parse(feed_url)
                feed_name = (
                    parsed.feed.title if hasattr(parsed, "feed") and hasattr(parsed.feed, "title") else feed_url
                )
                entries = list(getattr(parsed, "entries", []))

                filtered: List = []
                for e in entries:
                    dt = _parse_entry_datetime(e)
                    if dt is None or dt >= cutoff:
                        filtered.append((dt or datetime.now(), e))
                filtered.sort(key=lambda x: x[0], reverse=True)
                filtered = [e for _dt, e in filtered[:limit_per_feed]]

                for e in filtered:
                    url = getattr(e, "link", None)
                    if not url:
                        continue
                    title = getattr(e, "title", "無題")
                    published_at = _parse_entry_datetime(e)
                    text = _extract_article_text(e, url, session)

                    sources.append(
                        {
                            "feed_name": feed_name,
                            "category": category,
                            "title": title,
                            "url": url,
                            "date": published_at.strftime("%Y-%m-%dT%H:%M:%S") if published_at else None,
                            "text": text,
                        }
                    )
            except Exception:
                continue

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "generated_at": now_utc,
        "site": "tech-blogs/rss-sources",
        "num_articles": len(sources),
        "sources": sources,
    }


