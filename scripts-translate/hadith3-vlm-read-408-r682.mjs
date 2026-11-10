// R682 — lectures VLM des crops de preuve leçon 408 hadith-3es (p.129-136).
// Usage: node scripts-translate/hadith3-vlm-read-408-r682.mjs
// Chaque renvoi Muwaṭṭaʾ et chaque renvoi coranique est tranché CHIFFRE PAR CHIFFRE à l'image.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/qa-crops-r682';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-408';
fs.mkdirSync(OUTDIR, { recursive: true });

const BASE = `Zone d'un manuel scolaire arabe (hadith, 3e année secondaire) à très fort zoom. Transcris EXACTEMENT tout le texte visible, ligne par ligne, en arabe, en conservant diacritiques, crochets [] et guillemets « ». Pour tout renvoi de la forme [الموطأ رقم: N], transcris le nombre N CHIFFRE PAR CHIFFRE (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9) sous la forme NUM: <chiffres latins>. Pour tout renvoi coranique [سورة X الآية: N], transcris N chiffre par chiffre en NUM:. Ne devine rien : transcris ce qui est visible.`;

const TASKS = [
  { tag: 'b0-p129-contenu', ask: `${BASE}\nTranscris tout le texte visible de cette page : l'invite أتأمل النص..., la consigne أحفظ أحاديث الدرس المقبل, et les trois questions numérotées 1- 2- 3- de préparation (iʿdād).` },
  { tag: 'b4-p136-objectifs', ask: `${BASE}\nTranscris les objectifs de la leçon (numérotés 1- 2- 3-) sous la rubrique أهداف الدرس, et le titre de la leçon s'il est visible.` },
  { tag: 'm1-p130-medallion', ask: `${BASE}\nTranscris le numéro DANS le médaillon (chiffre par chiffre en NUM:), la bannière du titre de la leçon (calligraphié) et la rubrique + les objectifs 1- 2- 3- si visibles.` },
  { tag: 'v1-p130-aya', ask: `${BASE}\nTranscris la citation coranique ﴿...﴾ COMPLÈTE ligne par ligne et son renvoi [سورة التوبة الآية: N] — NUM: chiffre par chiffre. Chaque mot du verset compte.` },
  { tag: 'h1-p130-malik', ask: `${BASE}\nTranscris la question d'ouverture (فما هي...؟) puis la citation de مالك entre « » complète (chaque mot : أن يحلق رأسه حتى ينحر هديه... الذبح، ولبس الثياب، وإلقاء التفث، والحلاق/الحلق — transcris exactement ce qui est imprimé) et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'h2-p131-isa', ask: `${BASE}\nTranscris le hadith complet (isnad + matn, les verbes فحلقت/فتحلقت exactement tels qu'imprimés pour les deux hommes) et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'h3-p131-hafsa', ask: `${BASE}\nTranscris le hadith de حَفْصَة (isnad + matn) : transcris le verbe « لبّدتُ/لبَدتُ رأسي » EXACTEMENT tel qu'imprimé (avec ou sans تشديد), et le renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'n1-p131-annees', ask: `${BASE}\nTranscris les deux années de la mort de حفصة (توفيت سنة N هـ / وقيل سنة M هـ) — chaque année CHIFFRE PAR CHIFFRE en NUM:.` },
  { tag: 'f1-p132-recit', ask: `${BASE}\nTranscris la re-citation du rapport d'عمرو بن العاص (وقف رسول الله للناس بمنى...) : les deux verbes exactement imprimés (فحلقت... قبل أن أنحر / ف... قبل أن أرمي), les trois citations « انحر ولا حرج » « ارم ولا حرج » « افعل ولا حرج » et la phrase وأجمع العلماء على الإجزاء في...` },
  { tag: 'k1-p133-makan', ask: `${BASE}\nTranscris le titre -ب مكان النحر, la citation entre « » (هذا المنحر...) et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre, puis la phrase المراد: ...` },
  { tag: 'k2-p133-mubashara', ask: `${BASE}\nTranscris le titre -ج, la phrase sur l'الأفضل, le hadith d'علي (نحر... بيده) avec son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre, et la phrase وفي هذا العصر...` },
  { tag: 'q1-p133-umr', ask: `${BASE}\nTranscris le titre ثانيا: أحكام التحلل, le titre 1- وقت التحلل et le début du hadith d'عمر بن الخطاب (خطب الناس بعرفة...) — transcris exactement « ما حرم عليكم من الحاجّ/الإحرام » tel qu'imprimé.` },
  { tag: 'q2-p134-umrfin', ask: `${BASE}\nTranscris la fin du hadith d'عمر (لا يمسّ أحدٌ نساءه ولا طيباً حتى يطوف بالبيت) avec son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre ; puis l'analyse (فأول التحلل...) et la citation coranique ﴿لا تقتلوا الصيد وأنتم حرم﴾ avec son renvoi [سورة المائدة الآية: N] — NUM: chiffre par chiffre.` },
  { tag: 'l1-p134-lubd', ask: `${BASE}\nTranscris le titre 2- (تحلل من لبّد شعره أو عقصه أو ...) EXACTEMENT, la règle (وجب عليه الحلاق ولا يجوز له التقصير), le hadith de سعيد بن المسيب (من عقص رأسه أو حلقه أو لبّد فقد وجب عليه الحلق) avec son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre, et وإلى هذا ذهب الجمهور.` },
  { tag: 'l2-p134-1185', ask: `${BASE}\nTranscris la phrase ويجوز التقصير عند عمر..., la citation « من ضفّر رأسه فليحلق ولا تشبهوا بالتلبيد/بالملبّدين — transcris EXACTEMENT ce qui est imprimé » avec son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre, puis فإن من تشبه به...` },
  { tag: 'w1-p134-taqwim', ask: `${BASE}\nTranscris le titre التقويم et les trois questions numérotées 1- 2- 3- COMPLÈTES (la 3e se termine par ...؟), et le numéro de page (folio) en bas — NUM: chiffre par chiffre.` },
  { tag: 'b2-p135-fatwa', ask: `${BASE}\nTranscris le rapport/athar complet (عن أبي...) : transcris l'isnad EXACTEMENT (noms complets) et le matn (رجلاً أفاض ولم يحلق ولم يقصر...) avec son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'b3-p135-cloture', ask: `${BASE}\nTranscris l'invite أستعين بشرح الزرقاني..., la consigne أحفظ أحاديث الدرس المقبل وأجيب عن الآتي, et les trois questions numérotées 1- 2- 3- de préparation (iʿdād) COMPLÈTES.` },
];

async function readOne(zai, t) {
  const out = `${OUTDIR}/r682-${t.tag}.txt`;
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
  const todo = TASKS.filter(t => !fs.existsSync(`${OUTDIR}/r682-${t.tag}.txt`));
  console.log(`tâches: ${todo.length}/${TASKS.length}`);
  const res = [];
  for (const t of todo) {
    res.push(await readOne(zai, t));
    console.log(res[res.length - 1]);
    await new Promise(r => setTimeout(r, 3000));
  }
  console.log('VLM-R682 terminé');
}
main().catch(e => { console.error('VLM_ERR: ' + (e?.message || e)); process.exit(1); });
