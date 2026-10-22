import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  // Search for the Tahrir text on 17:42 directly
  const queries = [
    "ابن عاشور التحرير والتنوير \"وللاهتمام بها افتتحت بقل\" الإسراء",
    "التحرير والتنوير \"جملة {كما يقولون} معترضة\"",
  ];
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 5 });
      console.log("\n=== QUERY:", q.slice(0, 80));
      for (const item of (r as any).results || []) {
        console.log("-", (item.name || "").slice(0, 90), "|", (item.url || '').slice(0, 80));
        console.log(" ", (item.snippet || "").replace(/\n/g, " ").slice(0, 350));
      }
    } catch (e) { console.log("ERR:", (e as Error).message.slice(0, 120)); }
  }
}
main();
