#!/usr/bin/env python3
# scripts/github_trending.py

import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup


@dataclass
class Repository:
    name: str
    description: Optional[str]
    link: str
    stars: int


def _read_languages_config(languages_file: Path) -> Dict[str, List[str]]:
    """languages.toml を読み込む。

    Python 3.11+ の tomllib を使う（追加依存を増やさない）。
    """
    import tomllib

    with open(languages_file, "rb") as f:
        data = tomllib.load(f)
    general = data.get("general", []) or []
    specific = data.get("specific", []) or []
    # 型をだいたい保証
    general = [str(x) for x in general]
    specific = [str(x) for x in specific]
    return {"general": general, "specific": specific}


def _retrieve_repositories(language: str, limit: int) -> List[Repository]:
    """GitHub Trending から指定言語のリポジトリを取得。"""
    base_url = "https://github.com/trending"
    url = base_url + (f"/{language}" if language else "")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    }

    try:
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        print(f"Error retrieving repositories for language {language}: {e}")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    repositories: List[Repository] = []

    for article in soup.select("article.Box-row")[: limit if limit and limit > 0 else None]:
        # Name
        name_el = article.select_one("h2 a")
        if not name_el:
            continue
        raw_name = name_el.text.strip().replace("\n", " ")
        # Normalize spaces around '/'
        name = "/".join(part.strip() for part in raw_name.split("/") if part.strip())
        link = f"https://github.com{name_el.get('href', '').strip()}"

        # Description
        desc_el = article.select_one("p")
        description = desc_el.text.strip() if desc_el and desc_el.text else None

        # Stars
        stars = 0
        # Common selector for stargazers link
        star_link = article.select_one("a[href$='/stargazers']")
        if star_link and star_link.text:
            digits = star_link.text.strip().replace(",", "").replace(".", "")
            if digits.isdigit():
                stars = int(digits)
        else:
            # Fallback: try to find any number near star svg
            possible = article.select("a")
            for a in possible:
                txt = (a.text or "").strip().replace(",", "").replace(".", "")
                if txt.isdigit():
                    stars = int(txt)
                    break

        repositories.append(
            Repository(name=name, description=description, link=link, stars=stars)
        )

    return repositories


def _dedupe_repositories(repos_by_lang: List[Tuple[str, List[Repository]]]) -> List[Repository]:
    """言語横断で重複（同一リンク）を排除。"""
    seen: Dict[str, Repository] = {}
    for _lang, repos in repos_by_lang:
        for r in repos:
            if r.link not in seen:
                seen[r.link] = r
            else:
                # Prefer higher star count if duplicate appears
                if r.stars > seen[r.link].stars:
                    seen[r.link] = r
    return list(seen.values())


def collect_github_trending_report(
    languages_file: Path,
    general_limit: int = 10,
    specific_limit: int = 5,
) -> Dict[str, object]:
    """GitHub Trending をクロールし、プロジェクト用レポートJSONを返す。"""
    config = _read_languages_config(languages_file)

    repos_by_language: List[Tuple[str, List[Repository]]] = []

    for language in config.get("general", []):
        repos_by_language.append((language or "all", _retrieve_repositories(language, general_limit)))

    for language in config.get("specific", []):
        repos_by_language.append((language, _retrieve_repositories(language, specific_limit)))

    deduped = _dedupe_repositories(repos_by_language)
    # Sort by stars desc
    deduped.sort(key=lambda r: r.stars, reverse=True)

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    now_local = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    articles: List[Dict[str, object]] = []
    for r in deduped:
        executive_summary: List[str] = []
        if r.description:
            executive_summary.append(r.description)
        executive_summary.append(f"スター数: {r.stars}")

        articles.append(
            {
                "url": r.link,
                "title": r.name,
                "date": None,
                "executive_summary": executive_summary,
                "key_findings": [],
                "references": [r.link],
                "retrieved_at": now_utc,
            }
        )

    report_obj: Dict[str, object] = {
        "generated_at": now_utc,
        "site": "github-trending",
        "num_articles": len(articles),
        "articles": articles,
    }

    return report_obj



