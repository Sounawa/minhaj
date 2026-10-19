import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  const queries = [
    "قراءة \"ليذكر\" الإسراء 41 ولقد صرفنا",
    "المحرر الوجيز ابن عطية سورة الإسراء قل لو كان معه آلهة",
    "قرأ حمزة والكسائي ليذكروا بسكون الذال",
  ];
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 6 });
      console.log("=== QUERY:", q.slice(0, 60));
      for (const item of (r as any).results || []) {
        console.log("-", (item.name || "").slice(0, 80));
        console.log(" ", (item.snippet || "").replace(/\n/g, " ").slice(0, 380));
      }
    } catch (e) { console.log("ERR", (e as Error).message); }
  }
}
main();
