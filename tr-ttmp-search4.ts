import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  const queries = [
    "فيكون السبيل على هذا التأويل بمعناه في قوله لابتغوا إلى ذي العرش سبيلا",
    "المحرر الوجيز ابن عطية \"لابتغوا إلى ذي العرش سبيلا\" الزلفى والقربة",
    "ابن عطية المحرر الوجيز \"بيانا للمانع\" أو \"بيانا للتمانع\" لو كان فيهما آلهة إلا الله لفسدتا",
    "المحرر الوجيز تسبيح السماوات والأرض عكرمة الشجرة تسبح والأسطوانة لا تسبح",
    "\"علوا كبيرا\" اسم مصدر \"نباتا\" المحرر الوجيز ابن عطية",
  ];
  for (const q of queries) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 6 });
      console.log("\n=== QUERY:", q.slice(0, 70));
      for (const item of (r as any).results || []) {
        console.log("-", (item.name || "").slice(0, 90));
        console.log(" ", (item.snippet || "").replace(/\n/g, " ").slice(0, 400));
      }
    } catch (e) { console.log("ERR", (e as Error).message); }
  }
}
main();
