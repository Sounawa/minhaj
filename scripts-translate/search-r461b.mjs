import ZAI from 'z-ai-web-dev-sdk';
async function main() {
  const zai = await ZAI.create();
  // 1) test sanité
  try {
    const r = await zai.functions.invoke("web_search", { query: "tafsir Ibn Atiyya al-Muharrar al-wajiz", num: 6 });
    console.log("TEST EN:", JSON.stringify(r).slice(0, 600));
  } catch (e) { console.log("ERR-EN", e.message); }
  // 2) arabe simple
  try {
    const r = await zai.functions.invoke("web_search", { query: "المحرر الوجيز ابن عطية سورة الإسراء", num: 8 });
    console.log("\nTEST AR:", JSON.stringify(r).slice(0, 800));
  } catch (e) { console.log("ERR-AR", e.message); }
}
main();
