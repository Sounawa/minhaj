import ZAI from 'z-ai-web-dev-sdk';
const queries = [
  "تفسير ابن عطية الإسراء آية 9",
  "تفسير ابن عطية الإسراء آية 12",
  "ابن الكواء القمر",
  "سلمان الفارسي كان الإنسان عجولا",
  "habous.gov.ma تفسير الإسراء المحرر الوجيز",
];
async function main() {
  const zai = await ZAI.create();
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 7 });
      console.log("\n=== QUERY:", q);
      for (const item of r.results || []) {
        console.log("*", (item.name || "").slice(0, 80), "|", (item.host_name || ""));
        console.log("  ", (item.snippet || "").replace(/\s+/g, " ").slice(0, 450));
      }
    } catch (e) { console.log("ERR", q.slice(0, 30), e.message.slice(0, 80)); }
  }
}
main();
