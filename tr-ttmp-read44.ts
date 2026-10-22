import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  const urls = [
    "https://quranpedia.net/surah/1/17/book/350",
  ];
  for (const url of urls) {
    try {
      const r = await zai.functions.invoke("page_reader", { url });
      const txt = (r as any).text || (r as any).content || JSON.stringify(r).slice(0, 500);
      // Find the section on verses 41-44
      const idx = txt.indexOf("ولقد صرفنا");
      console.log("URL:", url, "total len:", txt.length, "idx صرفنا:", idx);
      if (idx > 0) {
        console.log(txt.slice(Math.max(0, idx - 200), idx + 3000));
      } else {
        console.log(txt.slice(0, 2000));
      }
    } catch (e) { console.log("ERR", (e as Error).message); }
  }
}
main();
