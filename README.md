# Web Reader API — Code Examples

Ready-to-run code examples for [Web Reader API](https://rapidapi.com/bitsap/api/web-reader-api), an AI-powered web scraping API for LLMs and RAG pipelines.

## Get Your API Key

1. Go to [RapidAPI](https://rapidapi.com/bitsap/api/web-reader-api)
2. Subscribe to a plan (Free tier: 100 requests/month)
3. Copy your `X-RapidAPI-Key`

## Examples

### Python
| File | Description |
|---|---|
| [basic.py](python/basic.py) | Simplest usage — URL to Markdown |
| [ai_summary.py](python/ai_summary.py) | AI-powered summary and keywords |
| [chunks.py](python/chunks.py) | RAG-ready chunked output |
| [batch.py](python/batch.py) | Process multiple URLs at once |
| [compact.py](python/compact.py) | Token compression mode |
| [firecrawl_compat.py](python/firecrawl_compat.py) | Firecrawl v1 compatible endpoint |
| [extract.py](python/extract.py) | AI-powered structured extraction |

### JavaScript
| File | Description |
|---|---|
| [basic.mjs](javascript/basic.mjs) | Simplest usage — URL to Markdown |
| [ai_summary.mjs](javascript/ai_summary.mjs) | AI-powered summary and keywords |
| [batch.mjs](javascript/batch.mjs) | Process multiple URLs at once |

### LangChain
| File | Description |
|---|---|
| [firecrawl_loader.py](langchain/firecrawl_loader.py) | Drop-in replacement for FireCrawlLoader |
| [rag_pipeline.py](langchain/rag_pipeline.py) | Full RAG pipeline: scrape → chunk → embed → query |

### Use Cases
| File | Description |
|---|---|
| [news_digest.py](usecases/news_digest.py) | Summarize multiple news articles into a daily digest |
| [competitor_monitor.py](usecases/competitor_monitor.py) | Monitor competitor pages for changes |
| [pdf_analyzer.py](usecases/pdf_analyzer.py) | Extract and summarize PDF documents |

## Setup

```bash
# Python
pip install requests

# For LangChain examples
pip install langchain langchain-openai faiss-cpu requests

# JavaScript
npm install node-fetch
```

## Configuration

Set your API key as an environment variable:

```bash
export RAPIDAPI_KEY="your-rapidapi-key-here"
```

## Links

- **API on RapidAPI**: https://rapidapi.com/bitsap/api/web-reader-api
- **Documentation**: https://rapidapi.com/bitsap/api/web-reader-api
- **Zenn Article (Japanese)**: https://zenn.dev/bitsap/articles/1c9edcda57b336
