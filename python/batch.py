"""
Web Reader API — Batch Processing
Process multiple URLs in a single request.
"""

import os
import requests

API_KEY = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "webreader-ai.p.rapidapi.com",
    "Content-Type": "application/json",
}


def batch_read(urls, options=None):
    """Fetch multiple URLs in one request (max 10)."""
    response = requests.post(
        "https://webreader-ai.p.rapidapi.com/api/batch",
        headers=HEADERS,
        json={"urls": urls, "options": options or {}},
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://en.wikipedia.org/wiki/Web_scraping",
        "https://zenn.dev/zenn/articles/markdown-guide",
    ]

    result = batch_read(urls, options={"mode": "compact", "frontmatter": False})

    print(f"Total: {result['total']}  OK: {result['succeeded']}  Failed: {result['failed']}")
    print()

    for r in result["results"]:
        if r["status"] == "ok":
            title = r["data"]["metadata"]["title"]
            quality = r["data"]["quality"]["grade"]
            length = len(r["data"]["content"])
            print(f"  OK  {r['url']}")
            print(f"      Title: {title}  Quality: {quality}  Length: {length}  Time: {r['duration_ms']}ms")
        else:
            print(f"  ERR {r['url']} — {r['error']['message']}")
        print()
