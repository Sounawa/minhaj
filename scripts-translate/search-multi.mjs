import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const queries = process.argv.slice(2);
  try {
    const zai = await ZAI.create();
    for (const q of queries) {
      console.log('=== QUERY: ' + q + ' ===');
      const results = await zai.functions.invoke('web_search', { query: q, num: 8 });
      const items = Array.isArray(results) ? results : (results)?.results || [];
      for (const r of items) {
        console.log(`- ${r.name}\n  ${r.url}\n  ${(r.snippet || '').slice(0, 220)}`);
      }
    }
  } catch (e) {
    console.error('ERROR:', e?.message || String(e));
    process.exit(1);
  }
}
main();
