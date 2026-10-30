import ZAI from 'z-ai-web-dev-sdk';
async function main() {
  const zai = await ZAI.create();
  const r = await zai.functions.invoke("web_search", { query: "مختصر خليل الميراث", num: 5 });
  console.log('keys:', Object.keys(r || {}));
  console.log(JSON.stringify(r, null, 1).slice(0, 1500));
}
main().catch(e => console.log('ERR', e.message));
