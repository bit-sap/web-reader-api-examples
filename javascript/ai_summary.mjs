/**
 * Web Reader API — AI Summary (JavaScript)
 * Run: node ai_summary.mjs
 */

const API_KEY = process.env.RAPIDAPI_KEY || "YOUR_RAPIDAPI_KEY";

async function summarize(url) {
  const params = new URLSearchParams({ url, ai_summary: "true", output: "json" });
  const response = await fetch(
    `https://web-reader-api.p.rapidapi.com/api/read?${params}`,
    {
      headers: {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "web-reader-api.p.rapidapi.com",
      },
    }
  );
  return response.json();
}

const data = await summarize("https://zenn.dev/zenn/articles/markdown-guide");

console.log(`Title: ${data.metadata.title}`);
console.log(`Quality: ${data.quality.grade}`);

if (data.aiSummary?.summary) {
  console.log(`\nSummary: ${data.aiSummary.summary}`);
  console.log(`Keywords: ${data.aiSummary.keywords.join(", ")}`);
}
