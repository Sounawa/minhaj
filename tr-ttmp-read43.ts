import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  const r = await zai.functions.invoke("page_reader", { url: "https://quranpedia.net/surah/1/17/book/350" });
  const raw: any = r as any;
  const html = raw?.data?.html || raw?.html || "";
  // find the section around verse 41 marker
  let idx = html.indexOf("(٤١)");
  if (idx < 0) idx = html.indexOf("﴿٤١﴾");
  console.log("idx (41):", idx);
  if (idx >= 0) {
    const chunk = html.slice(Math.max(0, idx - 1500), idx + 900);
    console.log(chunk.replace(/<[^>]+>/g, " ").replace(/\s+/g, " "));
  }
}
main();
