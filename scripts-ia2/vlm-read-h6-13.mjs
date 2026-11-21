// Z2-48 — lectures VLM des 20 bandes pp.71-75 (600 dpi, 4 bandes/page, chevauchement 90 px).
// Méthode Z2-45/46/47 : prompt verbatim, NUM: pour tout chiffre, [؟] si illisible.
import ZAI from '/tmp/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-13/bands';
const OUTDIR = '/home/z/my-project/scripts-ia2/tmp/h6-13/vlm';
fs.mkdirSync(OUTDIR, { recursive: true });

const BASE = `Image : bande horizontale d'une page d'un manuel scolaire marocain de hadith (6e année, trad. du livre des Arba'īn nawawiyya avec commentaire d'Ibn Daqīq al-'Īd). Transcris TOUT le texte arabe visible, dans l'ordre de lecture (droite → gauche, haut → bas), mot à mot, AVEC la voyellalisation imprimée. Inclus : titres de sections (bandeaux colorés), lignes du corps, renvois entre crochets [سورة ...: N], références de hadith [رواه ...]. Pour un TABLEAU : une ligne par rangée, cellules séparées par | . Ne devine JAMAIS : un mot illisible → [؟]. Les bords haut/bas peuvent être coupés au milieu d'une ligne (chevauchement entre bandes) : transcris quand même les fragments. Tout nombre → NUM: <chiffres latins 0-9> en le décrivant chiffre par chiffre (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9). ATTENTION aux lettres-point : ض a un point au-dessus, ص une boucle ouverte, د sans point, ذ un point, ر sans point, ز un point, ط fermé, ظ fermé+point. Le mot du hadith de la leçon est ضَرَر (dād). Réponds UNIQUEMENT par la transcription.`;

const TASKS = [];
for (let p = 71; p <= 75; p++) for (let b = 1; b <= 4; b++) TASKS.push(`p${p}-b${b}`);

async function readOne(zai, tag) {
  const out = `${OUTDIR}/${tag}.txt`;
  if (fs.existsSync(out) && fs.statSync(out).size > 100) return `${tag}: déjà lu`;
  for (let k = 1; k <= 4; k++) {
    try {
      const b64 = fs.readFileSync(`${DIR}/${tag}.png`).toString('base64');
      const res = await zai.chat.completions.createVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: BASE },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
          ] }],
        thinking: { type: 'disabled' },
      });
      const txt = res.choices[0]?.message?.content || '(vide)';
      fs.writeFileSync(out, txt, 'utf-8');
      return `${tag}: OK (${txt.length} car)`;
    } catch (e) {
      const msg = String(e?.message || e);
      if (k === 4) { fs.writeFileSync(out, `ERREUR ${msg}`, 'utf-8'); return `${tag}: ERREUR ${msg.slice(0, 80)}`; }
      const wait = msg.includes('429') ? 20000 * k : 5000 * k;
      await new Promise(r => setTimeout(r, wait));
    }
  }
}

async function main() {
  const zai = await ZAI.create();
  for (const t of TASKS) console.log(await readOne(zai, t));
}
main().catch(e => { console.error('FATAL', e); process.exit(1); });
