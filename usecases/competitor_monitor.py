"""
Use Case: Competitor Page Monitor
Track changes on competitor pages using content hashes.
"""

import os
import json
import requests

API_KEY = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "web-reader-api.p.rapidapi.com",
}

HASH_FILE = "page_hashes.json"


def load_hashes():
    try:
        with open(HASH_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_hashes(hashes):
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=2)


def check_page(url):
    """Fetch page and return content hash."""
    response = requests.get(
        "https://web-reader-api.p.rapidapi.com/api/read",
        headers={**HEADERS, "Accept": "application/json"},
        params={"url": url, "mode": "compact", "frontmatter": "false"},
    )
    response.raise_for_status()
    data = response.json()
    return data.get("contentHash", ""), data["metadata"]["title"]


if __name__ == "__main__":
    urls_to_monitor = [
        "https://example.com",
        # Add competitor URLs:
        # "https://competitor.com/pricing",
        # "https://competitor.com/features",
    ]

    previous = load_hashes()
    current = {}
    changes = []

    for url in urls_to_monitor:
        content_hash, title = check_page(url)
        current[url] = content_hash

        if url in previous and previous[url] != content_hash:
            changes.append({"url": url, "title": title})
            print(f"  CHANGED: {title} ({url})")
        elif url not in previous:
            print(f"  NEW:     {title} ({url})")
        else:
            print(f"  OK:      {title} ({url})")

    save_hashes(current)

    if changes:
        print(f"\n{len(changes)} page(s) changed since last check!")
        # Send notification (Slack, email, etc.)
    else:
        print("\nNo changes detected.")
