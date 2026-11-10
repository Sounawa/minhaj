// R684-bis — deux lectures décisives p.135 (bandeau + dernière ligne).
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/tr-tmp/qa-crops-r684';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-408';
const TASKS = [
  { tag: 't135-bandeau', ask: `Ultra-zoom sur un MOT unique imprimé en bleu sur une pastille verte d'un manuel scolaire arabe (bandeau-titre d'un encadré, page 135). Transcris ce mot LETTRE PAR LETTRE. Est-ce الاستشهاد (ا-ل-ا-س-ت-ش-ه-ا-د : ش = 3 points en haut) ou الاستثمار (ا-ل-ا-س-ت-ث-م-ا-ر : ث = 4 points en haut, م = boucle fermée) ou autre ? Décris chaque lettre (nombre de points, boucle ouverte/fermée) puis donne le mot et sa voyellation.` },
  { tag: 't135-lastline', ask: `Ultra-zoom sur la DERNIÈRE ligne d'un athar dans un encadré de manuel arabe (page 135). La ligne contient environ 4-6 mots arabes puis un renvoi bleu [الموطأ رقم: N]. Transcris CHAQUE mot lettre par lettre avec sa voyellation. Pour l'AVANT-DERNIER et le DERNIER mot arabe (avant [الموطأ]) : décris les lettres une à une (points, boucles). Le dernier mot commence-t-il par فَ ? Est-ce فَيُفِيضُ (fa-yufīḍu : ف-ي-ف-ي-ض) ou فَيُطِيفُ (fa-yuṭīfu : ف-ي-ط-ي-ف, ط = boucle plate large) ou فَيَرْجِعُ ? Le mot avant le dernier : البيت (ب-ي-ت) ou الذي (ل-ذ-ي) ? Transcris aussi le renvoi [الموطأ رقم: N] chiffre par chiffre en NUM:.` },
];
async function readOne(zai, t) {
  const out = `${OUTDIR}/r684b-${t.tag}.txt`;
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
async function main() {
  const zai = await ZAI.create();
  for (const t of TASKS) console.log(await readOne(zai, t));
}
main().catch(e => { console.error('FATAL', e); process.exit(1); });
