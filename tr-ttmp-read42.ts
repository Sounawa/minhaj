import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  // Try the working URL pattern with verse anchors: /surah/{r}/17/book/350 loaded fully
  const r = await zai.functions.invoke("page_reader", { url: "https://quranpedia.net/surah/1/17/book/350" });
  const raw: any = r as any;
  const html = raw?.data?.html || raw?.html || JSON.stringify(raw);
  console.log("HTML len:", html.length);
  // find verse 41 tafsir section
  let idx = html.indexOf("ولقد صرفنا");
  if (idx < 0) idx = html.indexOf("صَرَّفْنَا");
  if (idx < 0) idx = html.indexOf("صرفنا");
  console.log("idx:", idx);
  if (idx >= 0) {
    const chunk = html.slice(Math.max(0, idx - 500), idx + 3000);
    // strip tags roughly
    console.log(chunk.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").slice(0, 2500));
  } else {
    console.log(html.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").slice(0, 1500));
  }
}
main();
