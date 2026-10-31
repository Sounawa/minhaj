import ZAI from 'z-ai-web-dev-sdk';
const queries = [
  "ابن عطية المحرر الوجيز سورة الإسراء يهدي للتي هي أقوم أعدل ابن عباس",
  "المحرر الوجيز ويدع الإنسان بالشر دعاءه بالخير نزلت في",
  "ابن الكواء السواد الذي في القمر محوه الله",
  "وكان الإنسان عجولا آدم نفخ الروح عطس ساقيه",
  "ابن عطية فمحونا آية الليل آيات أربع الممحو القمر المبصرة الشمس",
];
async function main() {
  const zai = await ZAI.create();
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 7 });
      console.log("\n=== QUERY:", q);
      for (const item of r.results || []) {
        console.log("*", (item.name || "").slice(0, 80), "|", (item.host_name || ""));
        console.log("  ", (item.snippet || "").replace(/\s+/g, " ").slice(0, 500));
      }
    } catch (e) { console.log("ERR", q.slice(0, 30), e.message.slice(0, 80)); }
  }
}
main();
