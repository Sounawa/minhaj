import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  const urls = [
    "https://quranpedia.net/surah/17/41/book/350",
    "https://quranpedia.net/ayah/17/41/book/350",
  ];
  for (const u of urls) {
    try {
      const r = await zai.functions.invoke("page_reader", { url: u });
      const text = (r as any).text || (r as any).content || JSON.stringify(r);
      console.log("=== URL:", u, "len:", text.length);
      // find the qiraa discussion
      const idx = text.indexOf("صرفنا");
      if (idx >= 0) console.log(text.slice(Math.max(0, idx - 600), idx + 2200));
      else console.log(text.slice(0, 1200));
      break;
    } catch (e) { console.log("ERR", u, (e as Error).message); }
  }
}
main();
