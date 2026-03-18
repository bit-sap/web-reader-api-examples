"""
Web Reader API — Basic Usage
Fetch a URL and get clean Markdown content.
"""

import os
import requests

API_KEY = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
BASE_URL = "https://webreader-ai.p.rapidapi.com"
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "webreader-ai.p.rapidapi.com",
}


def read_url(url):
    """Fetch a URL and return structured content."""
    response = requests.get(
        f"{BASE_URL}/api/read",
        headers=HEADERS,
        params={"url": url, "output": "json"},
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = read_url("https://example.com")

    print(f"Title:   {data['metadata']['title']}")
    print(f"Quality: {data['quality']['score']}/100 ({data['quality']['grade']})")
    print(f"Lang:    {data['language']['language']}")
    print(f"Engine:  {data['engine']}")
    print()
    print("--- Content ---")
    print(data["content"][:500])
