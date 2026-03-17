"""
Web Reader API — Token Compression
Reduce token count by 40-70% while preserving key information.
"""

import os
import requests

API_KEY = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "web-reader-api.p.rapidapi.com",
}

BASE_URL = "https://web-reader-api.p.rapidapi.com/api/read"


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Markdown"

    # Normal mode
    normal = requests.get(BASE_URL, headers=HEADERS, params={"url": url, "frontmatter": "false"}).json()

    # Compact mode
    compact = requests.get(BASE_URL, headers=HEADERS, params={"url": url, "mode": "compact", "frontmatter": "false"}).json()

    normal_len = len(normal["content"])
    compact_len = len(compact["content"])
    reduction = round((1 - compact_len / normal_len) * 100)

    print(f"URL: {url}")
    print(f"Normal:  {normal_len:,} chars")
    print(f"Compact: {compact_len:,} chars")
    print(f"Reduction: {reduction}%")
    print()
    print(f"Compression stats: {compact.get('compression', 'N/A')}")
