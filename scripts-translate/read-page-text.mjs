import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

async function main() {
  const url = process.argv[2];
  const out = process.argv[3] || '/tmp/page.txt';
  try {
    const zai = await ZAI.create();
    const res = await zai.functions.invoke('page_reader', { url, mode: 'read' });
    const data = res?.data ?? res;
    const html = data?.html || data?.text || JSON.stringify(data);
    // extraction texte
    let t = String(html);
    t = t.replace(/<script[\s\S]*?<\/script>/gi, ' ');
    t = t.replace(/<style[\s\S]*?<\/style>/gi, ' ');
    t = t.replace(/<[^>]+>/g, '\n');
    t = t.replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#\d+;/g, ' ');
    t = t.replace(/[ \t]+/g, ' ');
    t = t.replace(/\n\s*\n+/g, '\n');
    fs.writeFileSync(out, t, 'utf-8');
    console.log('OK', t.length, 'chars ->', out);
  } catch (e) {
    console.error('ERROR:', e?.message || String(e));
    process.exit(1);
  }
}
main();
