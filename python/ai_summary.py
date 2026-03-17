"""
Web Reader API — AI Summary
Get Claude-powered summaries and keywords from any page.
"""

import os
import requests

API_KEY = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "web-reader-api.p.rapidapi.com",
}


def summarize_url(url):
    """Fetch a URL with AI-generated summary."""
    response = requests.get(
        "https://web-reader-api.p.rapidapi.com/api/read",
        headers=HEADERS,
        params={"url": url, "ai_summary": "true"},
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # Works great with Japanese articles too
    urls = [
        "https://en.wikipedia.org/wiki/Large_language_model",
        "https://zenn.dev/zenn/articles/markdown-guide",
    ]

    for url in urls:
        data = summarize_url(url)
        print(f"URL: {url}")
        print(f"Title: {data['metadata']['title']}")

        if data.get("aiSummary") and "summary" in data["aiSummary"]:
            print(f"Summary: {data['aiSummary']['summary']}")
            print(f"Keywords: {', '.join(data['aiSummary']['keywords'])}")
        else:
            print("Summary: (AI summary not available)")

        print(f"Quality: {data['quality']['grade']}")
        print()
