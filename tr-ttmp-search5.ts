import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  const queries = [
    "المحرر الوجيز ابن عطية الإسراء 41",
    "ابن عطية تفسير الإسراء 41 42 43 44",
    "لو كان فيهما الهة الا الله لفسدتا التمانع ابن عطية",
    "تفسير ابن عطية سبحانه وتعالى عما يقولون علوا كبيرا",
    "تفسير ابن عطية تسبيح السماوات والارض عكرمة",
  ];
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 5 });
      console.log("\n=== QUERY:", q.slice(0, 70));
      for (const item of (r as any).results || []) {
        console.log("-", (item.name || "").slice(0, 90));
        console.log(" ", (item.snippet || "").replace(/\n/g, " ").slice(0, 400));
      }
    } catch (e) { console.log("ERR", (e as Error).message); }
  }
}
main();
