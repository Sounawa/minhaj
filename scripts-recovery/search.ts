import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const query = process.argv[2] || 'المنهاج النموذجي للتعليم العتيق المغرب';
  const num = parseInt(process.argv[3] || '10', 10);
  try {
    const zai = await ZAI.create();
    const results = await zai.functions.invoke('web_search', { query, num });
    const items = Array.isArray(results) ? results : (results as any)?.results || [];
    for (const r of items) {
      console.log(`- ${(r as any).name}\n  ${(r as any).url}\n  ${(r as any).snippet?.slice(0, 150)}`);
    }
  } catch (e: any) {
    console.error('ERROR:', e?.message || String(e));
    process.exit(1);
  }
}
main();
