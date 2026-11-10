// R679 — lectures VLM des crops de preuve leçon 408 hadith-3es (p.129-134).
// Usage: node scripts-translate/hadith3-vlm-read-408-r679.mjs
// Chaque renvoi Muwaṭṭaʾ et chaque renvoi coranique est tranché CHIFFRE PAR CHIFFRE à l'image.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/qa-crops-r679';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-408';
fs.mkdirSync(OUTDIR, { recursive: true });

const BASE = `Zone d'un manuel scolaire arabe (hadith, 3e année secondaire) à très fort zoom. Transcris EXACTEMENT tout le texte visible, ligne par ligne, en arabe, en conservant diacritiques, crochets [] et guillemets « ». Pour tout renvoi de la forme [الموطأ رقم: N], transcris le nombre N CHIFFRE PAR CHIFFRE (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9) sous la forme NUM: <chiffres latins>. Pour tout renvoi coranique [سورة X الآية: N], transcris N chiffre par chiffre en NUM:. Ne devine rien : transcris ce qui est visible.`;

const TASKS = [
  { tag: 'x0-p129-annonce', ask: `${BASE}\nTranscris l'invite (أتأمل النص...) et les questions numérotées 1- 2- 3- de préparation.` },
  { tag: 'x1-p130-aya', ask: `${BASE}\nTranscris le paragraphe d'introduction et la citation coranique complète avec son renvoi [سورة التوبة الآية: N] — NUM: chiffre par chiffre.` },
  { tag: 'x2-p130-h1173', ask: `${BASE}\nTranscris la citation de مالك entre « » complète et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'x3-p131-h1267', ask: `${BASE}\nTranscris le hadith complet (isnad + matn) et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'x4-p131-hafsa', ask: `${BASE}\nTranscris le hadith de حَفْصَة (isnad + matn) et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'x5-p131-notice', ask: `${BASE}\nTranscris la notice biographique de حفصة بنت عمر بن الخطاب (qualité, mari, dates d'années) avec CHAQUE année CHIFFRE PAR CHIFFRE en NUM:.` },
  { tag: 'x6-p132-gloses', ask: `${BASE}\nTranscris les deux gloses (إِلقَاءُ التفث... et لَبَدْتُ: رَأسي...), le titre استخلاص المضامين et ses trois items 1- 2- 3-.` },
  { tag: 'x7-p132-fiqh1', ask: `${BASE}\nTranscris le titre أولا: et le titre 1-, la liste des actions du jour du sacrifice, et le début de وقد سئل النبي...` },
  { tag: 'x8-p132-amr', ask: `${BASE}\nTranscris le rapport de عمرو بن العاص رضي الله عنه (قصة بمنى...) complet avec les deux citations « انحر ولا خرج » et « ارم ولا خرج » et « افعل ولا حرج » — transcris ce qui est visible, marque [?] l'illisible.` },
  { tag: 'x9-p133-taqdim', ask: `${BASE}\nTranscris le passage sur التقديم والتأخير (اختلفوا في الدم...) avec les avis de مالك.` },
  { tag: 'x10-p133-makan', ask: `${BASE}\nTranscris le titre -ب مكان النحر, la citation entre « » et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre, et la phrase المراد: ...` },
  { tag: 'x11-p133-mubashara', ask: `${BASE}\nTranscris le titre -ج مباشرة نحر الهدي et le hadith d'علي (isnad + matn) avec son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'x12-p133-khutba', ask: `${BASE}\nTranscris le titre ثانيا: أحكام التحلل, le titre 1- وقت التحلل, et le début du hadith عن عمر بن الخطاب (خطب الناس بعرفة...) — transcris ce qui est visible, marque [?] l'illisible.` },
  { tag: 'x13-p134-khutba2', ask: `${BASE}\nTranscris la suite du sermon d'عمر (فأول التحلل رمي...) avec sa citation et le renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'x14-p134-aya', ask: `${BASE}\nTranscris le passage وَيُحَرِّمُ الصَّيْدَ لقوله تعالى et la citation coranique complète avec son renvoi [سورة المائدة الآية: N] — NUM: chiffre par chiffre.` },
  { tag: 'x15-p134-tahlul2', ask: `${BASE}\nTranscris tout le titre 2- وال passages : التحلل من لبد شعره أو عقصه أو ظفره, l'avis الجمهور, les citations d'عمر (« فَقَدْ وَجَبَ عَلَيْهِ الْحَلْقُ » et « مَنْ صَفَّرَ رَأْسَهُ... ») avec leurs renvois [الموطأ رقم: N] — NUM: chiffre par chiffre pour chacun. Marque [?] l'illisible.` },
  { tag: 'x16-p134-taqwim', ask: `${BASE}\nTranscris les trois questions numérotées 1- 2- 3- de l'évaluation finale.` },
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
  const todo = TASKS.filter(t => !fs.existsSync(`${OUTDIR}/${t.tag}.txt`));
  console.log(`tâches: ${todo.length}/${TASKS.length}`);
  const res = [];
  for (const t of todo) {
    res.push(await readOne(zai, t));
    await new Promise(r => setTimeout(r, 4000));
  }
  console.log(res.join('\n'));
  console.log('VLM-408 terminé');
}
main().catch(e => { console.error('VLM_ERR: ' + (e?.message || e)); process.exit(1); });
