"""
Web Reader API — RAG Chunking
Get content pre-split into semantic chunks with heading breadcrumbs.
"""

import os
import requests

API_KEY = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "web-reader-api.p.rapidapi.com",
}


def get_chunks(url, chunk_max=1000):
    """Fetch a URL and return RAG-ready chunks."""
    response = requests.get(
        "https://web-reader-api.p.rapidapi.com/api/read",
        headers=HEADERS,
        params={"url": url, "chunks": "true", "chunk_max": chunk_max, "output": "json"},
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = get_chunks("https://docs.python.org/3/tutorial/classes.html")

    print(f"Title: {data['metadata']['title']}")
    print(f"Total chunks: {len(data['chunks'])}")
    print()

    for chunk in data["chunks"][:5]:
        breadcrumb = " > ".join(chunk["headings"]) or "(root)"
        print(f"[Chunk {chunk['id']}] {breadcrumb} ({chunk['charCount']} chars)")
        print(f"  {chunk['content'][:100]}...")
        print()
