import ZAI from 'z-ai-web-dev-sdk';
async function main() {
  const zai = await ZAI.create();
  for (const q of ["Ibn Atiyya al-Muharrar al-Wajiz Surah Isra verse 9 aqwam tafsir", "Ibn al-Kawwa Ali blackness moon effaced night tafsir Tabari"]) {
    try {
      const r = await zai.functions.invoke("web_search", { query: q, num: 6 });
      console.log("\n=== QUERY:", q);
      for (const item of r.results || []) {
        console.log("*", (item.name || "").slice(0, 80), "|", (item.host_name || ""));
        console.log("  ", (item.url || "").slice(0, 100));
        console.log("  ", (item.snippet || "").replace(/\s+/g, " ").slice(0, 350));
      }
    } catch (e) { console.log("ERR", e.message.slice(0, 80)); }
  }
}
main();
