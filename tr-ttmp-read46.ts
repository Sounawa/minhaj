import ZAI from 'z-ai-web-dev-sdk';
import * as fs from 'fs';

async function main() {
  const zai = await ZAI.create();
  const r = await zai.functions.invoke("web_search", { query: "التحرير والتنوير الطاهر ابن عاشور سورة الإسراء", num: 5 });
  for (const item of (r as any).results || []) {
    console.log("-", (item.name || "").slice(0, 90), "|", item.url);
  }
  // try quranpedia book for Tahrir (guessing book id via search url)
  try {
    const r2 = await zai.functions.invoke("page_reader", { url: "https://quranpedia.net/surah/1/17/book/357.md" });
    const txt = typeof r2 === 'string' ? r2 : JSON.stringify(r2);
    fs.writeFileSync('/home/z/my-project/tr-tmp/tahrir-isra17.md', txt);
    console.log("357 saved len:", txt.length);
  } catch (e) { console.log("ERR 357:", (e as Error).message.slice(0, 150)); }
}
main();
