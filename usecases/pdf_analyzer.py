"""
Use Case: PDF Document Analyzer
Extract text from PDF URLs and get AI summaries.
"""

import os
import requests

API_KEY = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "web-reader-api.p.rapidapi.com",
}


def analyze_pdf(url):
    """Fetch a PDF and return extracted text with AI summary."""
    response = requests.get(
        "https://web-reader-api.p.rapidapi.com/api/read",
        headers=HEADERS,
        params={
            "url": url,
            "ai_summary": "true",
            "chunks": "true",
            "frontmatter": "false",
            "output": "json",
        },
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # Example: a public PDF document
    pdf_url = "https://www.w3.org/WAI/WCAG21/Techniques/pdf/PDF1"

    print(f"Analyzing: {pdf_url}")
    print()

    data = analyze_pdf(pdf_url)

    print(f"Title: {data['metadata']['title']}")
    print(f"Quality: {data['quality']['score']}/100 ({data['quality']['grade']})")
    print(f"Language: {data['language']['language']}")

    if data.get("aiSummary", {}).get("summary"):
        print(f"\nAI Summary: {data['aiSummary']['summary']}")
        print(f"Keywords: {', '.join(data['aiSummary']['keywords'])}")

    if data.get("chunks"):
        print(f"\nChunks: {len(data['chunks'])}")
        print(f"First chunk: {data['chunks'][0]['content'][:200]}...")

    print(f"\nFull content length: {len(data['content'])} chars")
