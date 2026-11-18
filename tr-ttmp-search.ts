import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  const queries = [
    "ابن عطية المحرر الوجيز سورة الإسراء آية 41 \"ولقد صرفنا\" ليذكر قراءة الجمهور أصله يتذكروا",
    "\"ولقد صرفنا في هذا القرآن\" الإسراء 41 قراءة \"ليذكر\" حمزة الكسائي للناس",
  ];
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 6 });
      console.log("=== QUERY:", q.slice(0, 60));
      for (const item of (r as any).results || []) {
        console.log("-", (item.name || "").slice(0, 90));
        console.log(" ", (item.snippet || "").replace(/\n/g, " ").slice(0, 400));
      }
    } catch (e) { console.log("ERR", (e as Error).message); }
  }
}
main();
