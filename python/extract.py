"""
Web Reader API — AI-Powered Structured Extraction
Tell the API what you want in natural language, get structured JSON back.
"""

import os
import json
import requests

API_KEY = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "webreader-ai.p.rapidapi.com",
    "Content-Type": "application/json",
}


def extract(url, prompt, schema=None):
    """Extract structured data using AI."""
    response = requests.post(
        "https://webreader-ai.p.rapidapi.com/v1/scrape",
        headers=HEADERS,
        json={
            "url": url,
            "formats": ["json"],
            "prompt": prompt,
            "schema": schema,
        },
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # Example: Extract article metadata
    result = extract(
        url="https://zenn.dev/zenn/articles/markdown-guide",
        prompt="Extract the article title, author, publication date, and a list of the main topics covered",
    )

    print("Extracted data:")
    print(json.dumps(result["data"].get("json"), indent=2, ensure_ascii=False))
