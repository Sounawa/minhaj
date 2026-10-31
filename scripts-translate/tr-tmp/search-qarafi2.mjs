import ZAI from 'z-ai-web-dev-sdk';
async function main() {
  const zai = await ZAI.create();
  const queries = [
    "\"كل من ورث ورث منه\" القرافي كليات الفرائض",
    "كليات القرافي \"بنت العم\" \"الجدة لأم\" يرث ولا يورث منه",
  ];
  for (const q of queries) {
    const r = await zai.functions.invoke("web_search", { query: q, num: 6 });
    console.log('====== ' + q.slice(0, 50) + ' ======');
    const items = r?.result || r?.results || r || [];
    for (const it of (Array.isArray(items) ? items : [items])) {
      const name = it?.name || it?.title || '';
      const snip = (it?.snippet || it?.content || '').replace(/\s+/g, ' ').slice(0, 350);
      console.log('• ' + name);
      console.log('  ' + snip);
    }
    console.log();
  }
}
main().catch(e => { console.log('ERR', e.message); process.exit(1); });
