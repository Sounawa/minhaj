// Z2-49 — sondes VLM ciblées de la leçon 13 (les 4 probes exécutées du tour,
// consolidées) : (a) zone الشرح complète + queue ; (b) gloses isolées x1/x2 ;
// (c) bandeau bleu p.77 (التَّفَهُّم) ; (d) bas de p.79 (aucune ligne d'appel).
// Doctrine : recoupement systématique (tesseract/zooms/sources canoniques).
import ZAI from '/tmp/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-14/vlm';
const BASE = `Image : extrait d'un manuel scolaire marocain de hadith (leçon 13 : «البينة على المدعي واليمين على من أنكر», hadith 33 des Arba'īn). Transcris TOUT le texte arabe visible mot à mot avec sa voyellisation, dans l'ordre de lecture (droite → gauche). Ne devine JAMAIS : un mot illisible → [؟]. Réponds UNIQUEMENT par la transcription.`;
const PROBES = {
  'w1-sharh-full-p77': `${BASE}\nCorps de la section «الشرح» (probablement DEUX gloses mot : synonyme).`,
  'w2-tail-p77': `${BASE}\nDernière ligne de la section, avant «استخلاص المضامين».`,
  'x1-glos1-p77': `${BASE}\nUne seule ligne de glose.`,
  'x2-glos2-p77': `${BASE}\nUne seule ligne de glose.`,
  'y1-bandeau-p77': `${BASE}\nBande décorative bleue à ornements dorés : y a-t-il du TEXTE ? Si purement décoratif : (décoratif, sans texte lisible).`,
  'z1-bas-p79': `${BASE}\nSous le hadith encadré : ligne d'appel éventuelle. Si rien de lisible (ornements/pied de page) : (rien de lisible).`,
};
const zai = await ZAI.create();
for (const [label, prompt] of Object.entries(PROBES)) {
  const file = `${DIR}/${label}.png`;
  if (!fs.existsSync(file)) { console.log(`== ${label} : ABSENT`); continue; }
  try {
    const b64 = fs.readFileSync(file).toString('base64');
    const res = await zai.chat.completions.createVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: prompt },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
      ] }],
      thinking: { type: 'disabled' },
    });
    console.log(`\n== ${label} ==\n` + (res.choices[0]?.message?.content || '(vide)'));
  } catch (e) { console.log(`\n== ${label} : ERREUR ${String(e?.message || e).slice(0, 200)}`); }
}
