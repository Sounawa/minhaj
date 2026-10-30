// search-r447-matn.mjs — vérification du matn المتعدد contre l'édition canonique (Muḫtaṣar)
import ZAI from 'z-ai-web-dev-sdk';
const queries = [
  "\"وإن أقر ابن ببنت\" \"وبنت بابن\" مختصر خليل الإقرار",
  "مختصر خليل \"أقر ابن ببنت وبنت بابن\" \"فالإنكار من ثلاثة\"",
  "\"فتضرب أربعة في خمسة\" مختصر خليل الإقرار ستين",
  "المنح الجليل \"وإن أقر ابن ببنت وبنت بابن\" الإقرار",
];
async function main() {
  const zai = await ZAI.create();
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 6 });
      console.log("\n=== QUERY:", q);
      for (const item of r.results || []) {
        console.log("-", (item.name || "").slice(0, 90));
        console.log(" ", (item.snippet || "").replace(/\n/g, " ").slice(0, 420));
      }
    } catch (e) { console.log("ERR", e.message); }
  }
}
main();
