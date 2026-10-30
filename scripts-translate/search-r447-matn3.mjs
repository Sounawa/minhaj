import ZAI from 'z-ai-web-dev-sdk';
const queries = [
  "\"وإن أقر ابن ببنت وبنت بابن\" مختصر خليل",
  "مختصر خليل الإقرار \"وإن أقرب الأقرباء فصدق\" الاقرار",
  "\"فتضرب أربعة في خمسة\" ثم \"بستين\" الإقرار فرائض",
  "al-mukhtasar khalil \"aqarra ibn bint\" iqrar inheritance",
  "مختصر خليل باب الاقرار \"يرجع\" عشرة ثمانية",
];
async function main() {
  const zai = await ZAI.create();
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 8 });
      console.log("\n=== QUERY:", q);
      for (const item of (Array.isArray(r) ? r : (r.results || []))) {
        console.log("-", (item.name || "").slice(0, 90), "|", (item.host_name || ""));
        console.log(" ", (item.snippet || "").replace(/\n/g, " ").slice(0, 400));
      }
    } catch (e) { console.log("ERR", e.message); }
  }
}
main();
