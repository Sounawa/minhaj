import ZAI from 'z-ai-web-dev-sdk';
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
const queries = [
  "المحرر الوجيز ابن عطية سورة الإسراء",
  "ابن الكواء السواد الذي في القمر",
  "تفسير ابن عطية للتي هي أقوم",
];
async function main() {
  const zai = await ZAI.create();
  for (const q of queries) {
    for (let attempt = 1; attempt <= 2; attempt++) {
      try {
        const r = await zai.functions.invoke("web_search", { query: q, num: 8 });
        const n = (r.results || []).length;
        console.log(`\n=== QUERY (${attempt}): ${q} — ${n} résultats`);
        for (const item of r.results || []) {
          console.log("*", (item.name || "").slice(0, 80), "|", (item.host_name || ""));
          console.log("  ", (item.url || "").slice(0, 110));
          console.log("  ", (item.snippet || "").replace(/\s+/g, " ").slice(0, 450));
        }
        if (n > 0) break;
      } catch (e) { console.log("ERR", q.slice(0, 30), e.message.slice(0, 80)); }
      await sleep(2500);
    }
    await sleep(2000);
  }
}
main();
