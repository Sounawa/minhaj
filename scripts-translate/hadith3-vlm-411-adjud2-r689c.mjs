import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/tr-tmp/qa-crops-r689c';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-411';
const TASKS = [
  { tag: 'a2-1263-anaq', ask: `Zoom 900 dpi (hadith n° 1263). La phrase « ومثل ذلك القوم يقتلون الرجل خطأ فتكون كفارة ذلك ... رقبة على كل إنسان منهم » : le mot avant رقبة est-il « عَنْقُ » (ع ن ق — point SUR le ق : cou) ou « عَتْقُ » (ع ت ق — point SUR le ت : affranchissement) ? Décris les points du ق et du ت. Transcris la phrase entière lettre par lettre. Ne devine pas.` },
  { tag: 'd2-1255-fin', ask: `Zoom 900 dpi (fin du hadith n° 1255, début de page). La phrase finit par « ... أذى في رأسه فعليه فدية ... » : la suite exacte est-elle « كما مُرَّ الله به » ou « كما أمره الله تعالى » ou « كما مَرَّ الله به » ? Décris lettre par lettre après الفدية. Transcris les 2 dernières lignes complètes. Ne devine pas.` },
  { tag: 'f2-dhimm', ask: `Zoom 900 dpi (bas de p.149). Dans « ... حلق أو تطيب أو لبس عامدا من غير ضرورة فعليه ... » le mot final est-il « ذِمٌ » (ذ م) ou « ذِمَامٌ » (ذ م ا م) ou autre ? Décris les lettres. Transcris la phrase entière + la phrase suivante (وحجة الإمام مالك...). Ne devine pas.` },
  { tag: 'h2-maida-verset', ask: `Zoom 900 dpi (p.151). QUATRE transcriptions lettre par lettre : 1) « وقد استغرب السائل من فعل عمر هذا؛ فقال: ... » — transcris la phrase complète qui suit (قال الرجل وهو يقول: هذا أمير المؤمنين لا يستطيع أن يحكم في ... حتى دعا رجلا يحكم معه) — le mot après في : « ظبي » ? 2) « وفي رواية الحاكم، قال: ... » la phrase complète ? 3) Le VERSE entre accolades {يَحْكُمُ بِهِ ...} : transcris-le ENTIÈREMENT lettre par lettre (y a-t-il « ذوا عدل منكم هديا بلغ/بالغ الكعبة » ?) et le NUMÉRO après [سورة المائدة الآية: N] — N = 95 ou 97 ? Regarde les chiffres un par un. 4) Le début du dialogue : « وفي الموطأ: فسمع عمر قول الرجل فدعاه فسأله: هل ... » — le verbe : « تحفظ » ou « تقرأ » ? et la suite complète jusqu'à « ثُمَّ قَالَ: إِنَّ اللهَ ... ». Ne devine pas.` },
];
async function readOne(zai, t) {
  const out = `${OUTDIR}/r689c2-${t.tag}.txt`;
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
