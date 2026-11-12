import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/tr-tmp/qa-crops-r688';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-410';
fs.mkdirSync(OUTDIR, { recursive: true });

const PAGES = [
  { tag: 'm410-p141', ctx: 'Page 141 du manuel (début de la leçon 21 « أحكام الفدية في الحج ») : bandeau-titre de leçon, cadre des objectifs (الأهداف), puis le تمهيد (hadith d\'ouverture).' },
  { tag: 'm410-p142', ctx: 'Page 142 : suite du تمهيد, textes du Muwaṭṭa\' (numérotés رقم: [الموطأ …]), puis la notice du transmetteur (ترجمة) et le شرح (gloses).' },
  { tag: 'm410-p143', ctx: 'Page 143 : section fiqh « أنواع الفدية » (les types de la fidya) — définitions et règles.' },
  { tag: 'm410-p144', ctx: 'Page 144 : suite des types de fidya — animaux et cas.' },
  { tag: 'm410-p145', ctx: 'Page 145 : suite — la chasse et le محرم, cas divers.' },
  { tag: 'm410-p146', ctx: 'Page 146 : fin de la leçon (évaluation تقويم, exploitation استثمار, préparation إعداد قبلي).' },
];

const ZOOMS = [
  { tag: 'z410-1-p141-textes', ctx: 'Zoom page 141 : les textes (نصوص) de la leçon — hadiths du Muwaṭṭa\' avec numéros.' },
  { tag: 'z410-2-p142-textes-notice', ctx: 'Zoom page 142 : textes du Muwaṭṭa\' + notice du transmetteur أبو الزبير.' },
  { tag: 'z410-3-p143-fiqh1', ctx: 'Zoom page 143 : section fiqh أنواع الفدية, première partie.' },
  { tag: 'z410-4-p144-types', ctx: 'Zoom page 144 : les types d\'animaux de la fidya (الظباء، الوخش، البعناق…).' },
  { tag: 'z410-5-p144-145-hunt', ctx: 'Zoom pages 144-145 : la chasse (الصيد) au mihram et ses règles.' },
  { tag: 'z410-6-p145-tayr', ctx: 'Zoom page 145 : le hadith des oiseaux (الطير) et cas connexes.' },
  { tag: 'z410-7-p146-fin', ctx: 'Zoom page 146 : fin de leçon (تقويم، استثمار، إعداد قبلي).' },
];

const pagePrompt = (c) => `Image d'une page d'un manuel scolaire arabe saoudo-marocain (enseignement traditionnel) imprimée. ${c.ctx}

TRANSCRIPTION FIDÈLE EXIGÉE :
1. Transcris TOUT le texte arabe en ordre de lecture (droite → gauche, haut → bas), en arabe UNICODE avec ses harakat quand ils sont visibles.
2. Conserve la STRUCTURE : marque chaque bloc avec [TITRE], [OBJECTIFS], [TEXTE], [GLOSSAIRE], [FIQH], [ÉVALUATION], [NOTICE] selon sa nature.
3. Les numéros de hadith apparaissent comme « رقم: [الموطأ 3421] » — transcris le numéro TEL QUE imprimé (chiffres arabes orientaux ٣٤٢١ ou latins 3421).
4. NE DEVINE JAMAIS : si un mot est flou, écris le mot suivi de [?]. Décris ce que tu vois lettre par lettre pour les mots ambigus (points, boucles).
5. Ne traduis PAS, ne commente PAS, ne reformule PAS : transcris uniquement.`;

const zoomPrompt = (c) => `Image zoomée (haute résolution) d'une page d'un manuel scolaire arabe imprimé. ${c.ctx}

TRANSCRIPTION EXIGÉE : transcris TOUT le texte visible en arabe UNICODE (avec harakat visibles), bloc par bloc, avec la structure ([TEXTE]/[GLOSSAIRE]/[FIQH]/…). Chiffres TELS QUE imprimés. Mots flous → mot + [?]. Ne devine pas, ne traduis pas. Ne commente pas.`;

async function readOne(zai, t, isPage) {
  const out = `${OUTDIR}/${t.tag}.txt`;
  if (fs.existsSync(out) && fs.statSync(out).size > 200) return `${t.tag}: déjà présent (cache)`;
  const ask = isPage ? pagePrompt(t.ctx) : zoomPrompt(t.ctx);
  for (let k = 1; k <= 4; k++) {
    try {
      const b64 = fs.readFileSync(`${DIR}/${t.tag}.png`).toString('base64');
      const res = await zai.chat.completions.createVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: ask },
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
  for (const p of PAGES) console.log(await readOne(zai, p, true));
  for (const z of ZOOMS) console.log(await readOne(zai, z, false));
}
main().catch(e => { console.error('FATAL', e); process.exit(1); });
