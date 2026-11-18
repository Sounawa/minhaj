import ZAI from 'z-ai-web-dev-sdk';
import * as fs from 'fs';

async function main() {
  const zai = await ZAI.create();
  const url = "https://quranpedia.net/surah/1/17/book/350.md";
  try {
    const r = await zai.functions.invoke("page_reader", { url });
    const txt = typeof r === 'string' ? r : ((r as any).data?.markdown || (r as any).data?.text || (r as any).text || JSON.stringify(r));
    fs.writeFileSync('/home/z/my-project/tr-tmp/ibn-atiyya-isra17.md', txt);
    console.log("saved, len:", txt.length);
    const idx = txt.indexOf("صرفنا");
    console.log("idx صرفنا:", idx);
    if (idx > 0) console.log(txt.slice(Math.max(0, idx - 300), idx + 400));
  } catch (e) { console.log("ERR", (e as Error).message); }
}
main();
