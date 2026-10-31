// search-r461.mjs — arbitrage des zones OCR corrompues de la leçon 712 (Muḥarrar 17:9-12)
import ZAI from 'z-ai-web-dev-sdk';
const queries = [
  "المحرر الوجيز ابن عطية \"للتي هي أقوم\" أعدل لا إله إلا الله",
  "المحرر الوجيز \"ويدع الإنسان بالشر دعاءه بالخير\"",
  "المحرر الوجيز ابن عطية \"فمحونا آية الليل\" مضيئين",
  "\"ابن الكواء\" \"السواد الذي في القمر\" علي بن أبي طالب",
  "المحرر الوجيز \"وكان الإنسان عجولا\" آدم نفخ الروح عطس",
];
async function main() {
  const zai = await ZAI.create();
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 6 });
      console.log("\n=== QUERY:", q);
      for (const item of r.results || []) {
        console.log("-", (item.name || "").slice(0, 90));
        console.log("  ", (item.url || ""));
        console.log("  ", (item.snippet || "").replace(/\n/g, " ").slice(0, 400));
      }
    } catch (e) { console.log("ERR", q.slice(0, 40), e.message); }
  }
}
main();
