// IA-2 — vlm-h6-14 : lecture VLM des zones résiduelles de la leçon 13 (hadith-6ep).
// Usage : node vlm-h6-14.mjs sonde | node vlm-h6-14.mjs <label...> | node vlm-h6-14.mjs tous
// Doctrine série : le VLM ne devine JAMAIS (mot illisible → [؟]) ; chaque lecture
// est recoupée par tesseract/zooms ou par les sources canoniques (shamela, etc.).
import ZAI from '/tmp/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/pdf-work/h6-14/vlm';
const BASE = `Image : bande horizontale d'une page d'un manuel scolaire marocain de hadith (6e année, tirage des Arba'īn nawawiyya avec commentaire d'Ibn Daqīq al-'Īd). Transcris TOUT le texte arabe visible, dans l'ordre de lecture (droite → gauche, haut → bas), mot à mot, AVEC la voyellisation imprimée. Ne devine JAMAIS : un mot illisible → [؟]. Réponds UNIQUEMENT par la transcription.`;
const FOCUS = {
  'v01-cartouche-p76': `${BASE}\nAttention : c'est un cartouche calligraphique doré/décoré avec le numéro et le titre de la leçon.`,
  'v03-gloses-p77': `${BASE}\nAttention : le texte est sur fond coloré (bandeaux/cellules) — concentrate-toi sur les lettres.`,
  'v08-yubayyin-p78': `${BASE}\nIndique précisément les DEUX PREMIERS MOTS de la ligne (à droite) puis le reste.`,
  'v05-liali-p78': `${BASE}\nIndique précisément le mot entre «بيّنةٍ» et «بدعواه» (avec ses lettres et points).`,
  'v06-lahiqqi-p78': `${BASE}\nIndique précisément le mot entre «استحقاقه» et «الذي يدّعيه».`,
  'v07-malam-p78': `${BASE}\nIndique précisément le verbe après «ما لم» (تقم ou تكن ?).`,
  'v09-thalithan-p79': `${BASE}\nEst-ce un sous-titre rouge ? Transcris-le.`,
  'v10-istithmar-p79': `${BASE}\nLe bandeau coloré et la ligne d'appel avant le hadith.`,
};

async function read(zai, label) {
  const file = `${DIR}/${label}.png`;
  if (!fs.existsSync(file)) { console.log(`== ${label} : ABSENT`); return; }
  const b64 = fs.readFileSync(file).toString('base64');
  const res = await zai.chat.completions.createVision({
    messages: [{ role: 'user', content: [
      { type: 'text', text: FOCUS[label] || BASE },
      { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
    ] }],
    thinking: { type: 'disabled' },
  });
  console.log(`\n== ${label} ==\n` + (res.choices[0]?.message?.content || '(vide)'));
}

async function main() {
  const args = process.argv.slice(2);
  const zai = await ZAI.create();
  if (args[0] === 'sonde') { await read(zai, 'v04-istikhlal-p77'); return; }
  const all = ['v01-cartouche-p76','v02-objectifs-p76','v03-gloses-p77','v04-istikhlal-p77',
    'v05-liali-p78','v06-lahiqqi-p78','v07-malam-p78','v08-yubayyin-p78','v09-thalithan-p79',
    'v10-istithmar-p79','v11-bayyina-p78','v12-yustafad-p79'];
  for (const l of (args[0] === 'tous' ? all : args)) {
    try { await read(zai, l); }
    catch (e) { console.log(`\n== ${l} : ERREUR ${String(e?.message || e).slice(0, 200)}`); }
  }
}
main().catch(e => { console.error('FATAL', String(e?.message || e).slice(0, 300)); process.exit(1); });
