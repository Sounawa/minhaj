import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/tr-tmp/qa-crops-r684';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-408';
const TASKS = [
  { tag: 't135-bandeau2', ask: `Image 900 dpi d'un bandeau-titre d'encadré d'un manuel scolaire arabe (page 135) : une pastille ou bande verte porte un ou plusieurs mots bleus. Transcris TOUS les mots visibles LETTRE PAR LETTRE. Pour chaque lettre : nombre de points (ش = 3 points, ث = 4 points, م = boucle fermée, ه = boucle) puis conclus : est-ce الاستشهاد ou الاستثمار ou autre ? Ne devine pas : décris ce que tu vois.` },
];
async function readOne(zai, t) {
  const out = `${OUTDIR}/r684c-${t.tag}.txt`;
  for (let k = 1; k <= 4; k++) {
    try {
      const b64 = fs.readFileSync(`${DIR}/${t.tag}.png`).toString('base64');
      const res = await zai.chat.completions.createVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: t.ask },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ] }],
        thinking: { type: 'disabled' },
      });
      const txt = res.choices[0]?.message?.content || '(vide)';
      fs.writeFileSync(out, txt, 'utf-8');
      return `${t.tag}: OK (${txt.length} car)`;
    } catch (e) {
      const msg = String(e?.message || e);
      if (k === 4) return `${t.tag}: ERREUR ${msg}`;
      await new Promise(r => setTimeout(r, msg.includes('429') ? 20000 * k : 5000));
    }
  }
}
async function main() { const zai = await ZAI.create(); for (const t of TASKS) console.log(await readOne(zai, t)); }
main().catch(e => { console.error('FATAL', e); process.exit(1); });
