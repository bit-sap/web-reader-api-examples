"""
Web Reader API — Full RAG Pipeline
Scrape → Chunk → Embed → Query in under 30 lines.

pip install langchain langchain-openai faiss-cpu requests
"""

import os
import requests
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langchain.chains import RetrievalQA

API_KEY = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "web-reader-api.p.rapidapi.com",
}


def scrape_and_chunk(url):
    """Fetch URL with RAG-ready chunks."""
    response = requests.get(
        "https://web-reader-api.p.rapidapi.com/api/read",
        headers=HEADERS,
        params={"url": url, "chunks": "true", "ai_summary": "true", "output": "json"},
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # Step 1: Scrape with chunks
    url = "https://docs.python.org/3/tutorial/classes.html"
    data = scrape_and_chunk(url)

    print(f"Title: {data['metadata']['title']}")
    print(f"Quality: {data['quality']['grade']}")
    print(f"Chunks: {len(data['chunks'])}")

    if data.get("aiSummary", {}).get("summary"):
        print(f"Summary: {data['aiSummary']['summary'][:150]}...")
    print()

    # Step 2: Convert to LangChain Documents
    documents = [
        Document(
            page_content=chunk["content"],
            metadata={
                "source": data["url"],
                "headings": " > ".join(chunk["headings"]),
                "chunk_id": chunk["id"],
            },
        )
        for chunk in data["chunks"]
    ]

    # Step 3: Build vector store
    print("Building vector store...")
    vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())

    # Step 4: Query
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4o-mini"),
        retriever=vectorstore.as_retriever(),
    )

    question = "What is the difference between class and instance variables?"
    print(f"Q: {question}")
    answer = qa.invoke(question)
    print(f"A: {answer['result']}")
