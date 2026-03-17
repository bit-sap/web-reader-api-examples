/**
 * Web Reader API — Batch Processing (JavaScript)
 * Run: node batch.mjs
 */

const API_KEY = process.env.RAPIDAPI_KEY || "YOUR_RAPIDAPI_KEY";

async function batchRead(urls, options = {}) {
  const response = await fetch(
    "https://web-reader-api.p.rapidapi.com/api/batch",
    {
      method: "POST",
      headers: {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "web-reader-api.p.rapidapi.com",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ urls, options }),
    }
  );
  return response.json();
}

const result = await batchRead(
  [
    "https://example.com",
    "https://en.wikipedia.org/wiki/Web_scraping",
    "https://zenn.dev/zenn/articles/markdown-guide",
  ],
  { mode: "compact", frontmatter: false }
);

console.log(`Total: ${result.total}  OK: ${result.succeeded}  Failed: ${result.failed}\n`);

for (const r of result.results) {
  if (r.status === "ok") {
    console.log(`  OK  ${r.url} (${r.duration_ms}ms)`);
    console.log(`      Title: ${r.data.metadata.title}  Quality: ${r.data.quality.grade}`);
  } else {
    console.log(`  ERR ${r.url} — ${r.error.message}`);
  }
}
