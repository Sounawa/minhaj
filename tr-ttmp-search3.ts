import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const zai = await ZAI.create();
  const r = await zai.functions.invoke("web_search", { query: "المحرر الوجيز لابن عطية سورة الإسراء", num: 5 });
  console.log("RAW TYPE:", typeof r);
  console.log(JSON.stringify(r, null, 1).slice(0, 1500));
}
main();
