// R682-bis — lectures VLM ciblées des zones à trancher (leçon 408).
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/qa-crops-r682';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-408';

const BASE = `Zone d'un manuel scolaire arabe (hadith, 3e année secondaire) à très fort zoom. Transcris EXACTEMENT tout le texte visible, ligne par ligne, en arabe, avec diacritiques. Pour tout nombre imprimé, transcris-le CHIFFRE PAR CHIFFRE (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9) en NUM: <chiffres latins>. Ne devine rien, n'invente aucun mot : si un mot est flou, transcris-le entre [?] en indiquant les lettres lisibles.`;

const TASKS = [
  { tag: 'y130-aya-ref', ask: `${BASE}\nTranscris la citation coranique ﴿...﴾ COMPLÈTE telle qu'imprimée (chaque mot exactement, la citation est peut-être partielle : elle commence peut-être par وَأَذَانٌ et s'arrête à وَرَسُولُهُ), puis le renvoi [سورة ... الآية: N] — transcris le NOM de la sourate et N chiffre par chiffre en NUM:. Puis la ligne suivante (فيه يقوم الحاج...).` },
  { tag: 'y130-aya-left', ask: `${BASE}\nTranscris le RENVOI imprimé [سورة ... الآية: N] en entier : nom de la sourate EXACTEMENT (lettre par lettre) et N chiffre par chiffre en NUM:. Indique la forme exacte de chaque chiffre arabe imprimé.` },
  { tag: 'y131-hafsa1', ask: `${BASE}\nTranscris l'isnad (قال مالك عن نافع عن عبد الله بن عمر عن حفصة...) et les DEUX premières lignes du matn : «يا رسول الله، ما شأن الناس...» — transcris le verbe et le pronom EXACTEMENT (حَلُّوا... وَلَمْ... أَنْتَ مِنْ...؟) et le mot final (عُمْرَتِكَ ?).` },
  { tag: 'y133-ali', ask: `${BASE}\nTranscris le hadith d'علي رضي الله عنه EXACTEMENT mot à mot : «أنّ رسول الله ﷺ نحر ...» — transcris le complément du premier نحر (بعض هديه ? بيده ?) et le second membre (ونحر غيره ... : بيده ? بغيره ? بعينه ?) tel qu'imprimé, puis le renvoi [الموطأ رقم: N] chiffre par chiffre en NUM:.` },
  { tag: 'y134-talbid', ask: `${BASE}\nTranscris le hadith d'عمر : «من ضفر(ضَفَّرَ) رأسه فليحلق، ولا تشبهوا بـ...» — transcris le DERNIER MOT EXACTEMENT lettre par lettre (بالتلبيد ? بالملبدين ? بالملبد ?), puis le renvoi [الموطأ رقم: N] chiffre par chiffre en NUM:, puis la phrase suivante (فإن من تشبه به...).` },
  { tag: 'y135-athar', ask: `${BASE}\nTranscris TOUT le texte visible : l'éventuel en-tête/titre de section en haut, puis l'athar complet عن عبد الله بن عمر (isnad exact, matn : لقي رجلا من أهله... أفاض ولم يحلق ولم يقصر جاهلا... فأمره عبد الله أن يرجع فيحلق أو يقصر ثم يرجع فيطوف بالبيت فيفيض ? — transcris EXACTEMENT ce qui est imprimé) avec son renvoi [الموطأ رقم: N] chiffre par chiffre en NUM:.` },
  { tag: 'y135-i3dada', ask: `${BASE}\nTranscris tout le texte visible : les questions numérotées de préparation (أحفظ أحاديث الدرس المقبل) — s'il y a une question 3, transcris-la COMPLÈTEMENT ; transcris aussi tout autre texte visible (bannière, folio en bas de page en NUM:).` },
];

async function readOne(zai, t) {
  const out = `${OUTDIR}/r682b-${t.tag}.txt`;
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
      await new Promise(r => setTimeout(r, wait));
    }
  }
}

async function main() {
  const zai = await ZAI.create();
  for (const t of TASKS) {
    console.log(await readOne(zai, t));
  }
}
main().catch(e => { console.error('FATAL', e); process.exit(1); });
