import ZAI from 'z-ai-web-dev-sdk';

async function main() {
  const url = process.argv[2];
  const mode = process.argv[3] || 'read';
  try {
    const zai = await ZAI.create();
    const out = await zai.functions.invoke('page_reader', { url, mode });
    const text = typeof out === 'string' ? out : JSON.stringify(out);
    console.log(text.slice(0, parseInt(process.argv[4] || '12000', 10)));
  } catch (e) {
    console.error('ERROR:', e?.message || String(e));
    process.exit(1);
  }
}
main();
