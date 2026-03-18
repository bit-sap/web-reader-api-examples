"""
Use Case: Daily News Digest
Fetch multiple news articles, summarize each with AI, and generate a digest.
"""

import os
import requests

API_KEY = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "webreader-ai.p.rapidapi.com",
    "Content-Type": "application/json",
}


def create_digest(urls):
    """Fetch and summarize multiple articles."""
    response = requests.post(
        "https://webreader-ai.p.rapidapi.com/api/batch",
        headers=HEADERS,
        json={
            "urls": urls,
            "options": {
                "mode": "compact",
                "frontmatter": False,
            },
        },
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    news_urls = [
        "https://example.com",
        # Add your news URLs here:
        # "https://news.yahoo.co.jp/articles/...",
        # "https://www3.nhk.or.jp/news/html/...",
    ]

    print("=" * 60)
    print("  DAILY NEWS DIGEST")
    print("=" * 60)
    print()

    result = create_digest(news_urls)

    for i, r in enumerate(result["results"], 1):
        if r["status"] != "ok":
            print(f"{i}. [ERROR] {r['url']}: {r['error']['message']}")
            continue

        data = r["data"]
        title = data["metadata"]["title"]
        quality = data["quality"]["grade"]

        print(f"{i}. {title}")
        print(f"   Quality: {quality} | Time: {r['duration_ms']}ms")
        print(f"   {data['content'][:150]}...")
        print()

    print(f"Total: {result['total']} articles | OK: {result['succeeded']} | Failed: {result['failed']}")
