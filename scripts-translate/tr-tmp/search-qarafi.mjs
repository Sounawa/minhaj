import ZAI from 'z-ai-web-dev-sdk';
async function main() {
  const zai = await ZAI.create();
  const queries = [
    "قواعد القرافي العشرين في المواريث كل من لا يرث لا يحجب",
    "كلية القرافي كل من ورث ورث منه إلا الجدة لأم والعمة وبنت الأخ وبنت العم",
  ];
  for (const q of queries) {
    const r = await zai.functions.invoke("web_search", { query: q, num: 6 });
    console.log('====== ' + q.slice(0, 50) + ' ======');
    const items = r?.result || r?.results || r || [];
    for (const it of (Array.isArray(items) ? items : [items])) {
      const name = it?.name || it?.title || '';
      const snip = (it?.snippet || it?.content || '').replace(/\s+/g, ' ').slice(0, 300);
      console.log('• ' + name);
      console.log('  ' + snip);
    }
    console.log();
  }
}
main().catch(e => { console.log('ERR', e.message); process.exit(1); });
