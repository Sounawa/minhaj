// R690 — lectures VLM pages pleines leçon 412 hadith-3es (la 'umra, p.152-158).
// Usage: node scripts-translate/r690-vlm-412-pages.mjs
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/pages-412';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-412';
fs.mkdirSync(OUTDIR, { recursive: true });

const BASE = `Page d'un manuel scolaire arabe (hadith, 3e année secondaire, Muwaṭṭaʾ de l'imam Mālik). Transcris EXACTEMENT tout le texte visible, ligne par ligne, en arabe, en conservant diacritiques, crochets [] et guillemets « ». Pour tout renvoi entre crochets de la forme [الموطأ رقم: N] ou [سورة X آية: N], transcris le nombre N CHIFFRE PAR CHIFFRE (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9) sous la forme NUM: <chiffres latins>. Ne devine rien : transcris ce qui est visible, marque [?] l'illisible.`;

const PAGES = [
  { tag: 'p152', ask: `${BASE}\nTranscris TOUTE la page (fin de leçon précédente : exploitation, préparation).` },
  { tag: 'p153', ask: `${BASE}\nTranscris TOUTE la page (ouverture de leçon : médaillon, objectifs, تمهيد, définition, premiers textes).` },
  { tag: 'p154', ask: `${BASE}\nTranscris TOUTE la page (hadiths et textes avec renvois [الموطأ رقم: N] — chiffre par chiffre).` },
  { tag: 'p155', ask: `${BASE}\nTranscris TOUTE la page (textes, notice biographique, début du commentaire الشرح).` },
  { tag: 'p156', ask: `${BASE}\nTranscris TOUTE la page (commentaire الشرح suite).` },
  { tag: 'p157', ask: `${BASE}\nTranscris TOUTE la page (commentaire suite, résumé ou fiqh).` },
  { tag: 'p158', ask: `${BASE}\nTranscris TOUTE la page (fin : résumé, fiqh du hadith, évaluation, exploitation, préparation — renvois chiffre par chiffre).` },
];

async function readOne(zai, t) {
  const out = `${OUTDIR}/${t.tag}.txt`;
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
      const wait = msg.includes('429') ? 20000 * k : 5000;
      console.log(`  retry ${t.tag} (${k}) dans ${wait}ms`);
      await new Promise(r => setTimeout(r, wait));
    }
  }
}

async function main() {
  const zai = await ZAI.create();
  const todo = PAGES.filter(t => !fs.existsSync(`${OUTDIR}/${t.tag}.txt`));
  console.log(`tâches: ${todo.length}/${PAGES.length}`);
  for (const t of todo) {
    const r = await readOne(zai, t);
    console.log(r);
    await new Promise(r => setTimeout(r, 4000));
  }
}
main().catch(e => { console.error('FATAL', e); process.exit(1); });
