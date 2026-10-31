// read-r461.mjs — lecture du Muḥarrar al-wajīz (tafsir.app) pour 17:9-12
import ZAI from 'z-ai-web-dev-sdk';
const urls = [
  "https://tafsir.app/ibn-atiyyah/17/9",
  "https://tafsir.app/ibn-atiyyah/17/10",
  "https://tafsir.app/ibn-atiyyah/17/11",
  "https://tafsir.app/ibn-atiyyah/17/12",
];
async function main() {
  const zai = await ZAI.create();
  for (const u of urls) {
    try {
      const r = await zai.functions.invoke("page_reader", { url: u });
      const text = (r?.text || r?.content || JSON.stringify(r)).replace(/\s+/g, " ");
      console.log("\n=====", u, "=====");
      console.log(text.slice(0, 2600));
    } catch (e) { console.log("ERR", u, e.message.slice(0, 120)); }
  }
}
main();
