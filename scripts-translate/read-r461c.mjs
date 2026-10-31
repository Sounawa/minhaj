import ZAI from 'z-ai-web-dev-sdk';
const enc = encodeURIComponent;
const urls = [
  `https://lite.duckduckgo.com/lite/?q=${enc('المحرر الوجيز ابن عطية للتي هي أقوم لا إله إلا الله')}`,
  `https://lite.duckduckgo.com/lite/?q=${enc('تفسير ابن عطية سورة الإسراء آية 9')}`,
];
async function main() {
  const zai = await ZAI.create();
  for (const u of urls) {
    try {
      const r = await zai.functions.invoke("page_reader", { url: u });
      const d = r?.data || {};
      const html = d.html || r?.text || JSON.stringify(r);
      const clean = html.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');
      console.log("\n=====", decodeURIComponent(u).slice(50, 120), "=====");
      console.log(clean.slice(0, 3000));
    } catch (e) { console.log("ERR", e.message.slice(0, 120)); }
  }
}
main();
