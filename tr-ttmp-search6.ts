import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  const queries = [
    "وهذا الرأي هو الذي يتناسب مع قوله تعالى بعد ذلك الإسراء",
    "\"لأن في الآية فرض المحال\" \"وجارية نظير قوله\" الإسراء ابن عطية",
    "التحرير والتنوير الإسراء 42 \"افتتحت بقل\" أو \"افتتحت بقوله قل\" جملة كما يقولون معترضة",
  ];
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 5 });
      console.log("\n=== QUERY:", q.slice(0, 80));
      for (const item of (r as any).results || []) {
        console.log("-", (item.name || "").slice(0, 90));
        console.log(" ", (item.snippet || "").replace(/\n/g, " ").slice(0, 400));
      }
    } catch (e) { console.log("ERR", (e as Error).message); }
  }
}
main();
