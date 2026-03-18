"""
Web Reader API — LangChain FireCrawlLoader Integration
Drop-in replacement: just change the base URL.

pip install langchain-community requests
"""

import os
from langchain_community.document_loaders import FireCrawlLoader

API_KEY = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")


def load_with_firecrawl_loader(url):
    """Use LangChain's built-in FireCrawlLoader with Web Reader API."""
    loader = FireCrawlLoader(
        url=url,
        api_key=API_KEY,
        api_url="https://webreader-ai.p.rapidapi.com",
        mode="scrape",
    )
    return loader.load()


if __name__ == "__main__":
    documents = load_with_firecrawl_loader("https://example.com")

    for doc in documents:
        print(f"Source: {doc.metadata.get('source', 'N/A')}")
        print(f"Content: {doc.page_content[:300]}")
        print("---")
