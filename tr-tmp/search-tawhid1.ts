import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  const queries = [
    "رسالة ابن أبي زيد القيرواني خطبة المصنف ونببه بآثار صنعته",
    "كفاية الطالب الرباني شرح الرسالة",
  ];
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 8 });
      console.log("\n=== QUERY:", q.slice(0, 80));
      for (const item of (r as any).results || []) {
        console.log("-", (item.name || "").slice(0, 90));
        console.log("URL:", (item.url || item.link || "").slice(0, 120));
        console.log(" ", (item.snippet || "").replace(/\n/g, " ").slice(0, 350));
      }
    } catch (e) { console.log("ERR", (e as Error).message.slice(0, 200)); }
  }
}
main();
