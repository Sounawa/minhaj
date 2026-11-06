// R633 — lecture d'image VLM (backend only) : transcrit une page/zone du manuel hadith-3es.
// Usage: node tr-tmp/vlm-read-r633.mjs <image.png> "<instruction>" [outfile]
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const [img, prompt, outfile] = process.argv.slice(2);
if (!img || !prompt) { console.error('usage: node vlm-read-r633.mjs <image> "<prompt>" [outfile]'); process.exit(2); }

async function main() {
  const zai = await ZAI.create();
  const b64 = fs.readFileSync(img).toString('base64');
  const mime = img.endsWith('.jpg') ? 'image/jpeg' : 'image/png';
  const res = await zai.chat.completions.createVision({
    messages: [{
      role: 'user',
      content: [
        { type: 'text', text: prompt },
        { type: 'image_url', image_url: { url: `data:${mime};base64,${b64}` } }
      ],
    }],
    thinking: { type: 'disabled' }
  });
  const out = res.choices[0]?.message?.content || '(vide)';
  if (outfile) fs.writeFileSync(outfile, out, 'utf-8');
  console.log(out);
}
main().catch(e => { console.error('VLM_ERR: ' + (e?.message || e)); process.exit(1); });
