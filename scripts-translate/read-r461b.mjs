import ZAI from 'z-ai-web-dev-sdk';
const enc = encodeURIComponent;
const urls = [
  `https://html.duckduckgo.com/html/?q=${enc('"ومعنى أقوم" "لا إله إلا الله" المحرر الوجيز ابن عطية')}`,
  `https://www.bing.com/search?q=${enc('المحرر الوجيز ابن عطية "للتي هي أقوم" "لا إله إلا الله"')}`,
];
async function main() {
  const zai = await ZAI.create();
  for (const u of urls) {
    try {
      const r = await zai.functions.invoke("page_reader", { url: u });
      const text = (r?.text || r?.content || JSON.stringify(r));
      console.log("\n=====", decodeURIComponent(u).slice(0, 80), "=====");
      // extraire les segments pertinents
      const clean = text.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');
      const idx = clean.indexOf('أقوم');
      console.log(idx >= 0 ? clean.slice(Math.max(0, idx - 800), idx + 1600) : clean.slice(0, 1200));
    } catch (e) { console.log("ERR", e.message.slice(0, 120)); }
  }
}
main();
