import ZAI from 'z-ai-web-dev-sdk';
const queries = [
  "اقر ابن ببنت وبنت بابن فالإنكار من ثلاثة",
  "اقرار ابن ببنت وبنت بابن ستين فرائض",
  "مختصر خليل باب الاقرار اقتراض الورثة",
  "sharh mukhtasar khalil iqrar ibn bint inkar thalatha",
];
async function main() {
  const zai = await ZAI.create();
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 8 });
      console.log("\n=== QUERY:", q);
      for (const item of r.results || []) {
        console.log("-", (item.name || "").slice(0, 90));
        console.log(" ", (item.snippet || "").replace(/\n/g, " ").slice(0, 420));
      }
    } catch (e) { console.log("ERR", e.message); }
  }
}
main();
