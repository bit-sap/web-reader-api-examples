/**
 * Web Reader API — Basic Usage (JavaScript)
 * Run: node basic.mjs
 */

const API_KEY = process.env.RAPIDAPI_KEY || "YOUR_RAPIDAPI_KEY";

async function readUrl(url) {
  const params = new URLSearchParams({ url, output: "json" });
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

const data = await readUrl("https://example.com");

console.log(`Title:   ${data.metadata.title}`);
console.log(`Quality: ${data.quality.score}/100 (${data.quality.grade})`);
console.log(`Lang:    ${data.language.language}`);
console.log(`Engine:  ${data.engine}`);
console.log();
console.log("--- Content ---");
console.log(data.content.slice(0, 500));
