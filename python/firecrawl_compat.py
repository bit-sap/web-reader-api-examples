"""
Web Reader API — Firecrawl v1 Compatible Mode
Same request/response format as Firecrawl. Just swap the URL.
"""

import os
import requests

API_KEY = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "webreader-ai.p.rapidapi.com",
    "Content-Type": "application/json",
}


def scrape(url, formats=None):
    """Firecrawl-compatible /v1/scrape endpoint."""
    response = requests.post(
        "https://webreader-ai.p.rapidapi.com/v1/scrape",
        headers=HEADERS,
        json={
            "url": url,
            "formats": formats or ["markdown"],
        },
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    result = scrape(
        "https://zenn.dev/zenn/articles/markdown-guide",
        formats=["markdown", "summary", "links"],
    )

    print(f"Success: {result['success']}")
    print(f"Title: {result['data']['metadata']['title']}")
    print(f"Language: {result['data']['metadata']['language']}")
    print(f"Quality: {result['data']['quality']['grade']}")
    print(f"Chunks: {len(result['data']['chunks'])}")
    print()

    if result["data"].get("summary"):
        print(f"Summary: {result['data']['summary'][:200]}")
    print()

    if result["data"].get("links"):
        print(f"Links found: {len(result['data']['links'])}")
        for link in result["data"]["links"][:5]:
            print(f"  {link}")
