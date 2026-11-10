// R682-ter — lectures VLM ultra-zoom des 5 fenêtres restées divergentes.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/qa-crops-r682';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-408';

const BASE = `Image ultra-zoom d'une ou deux lignes d'un manuel scolaire arabe. Transcris la ligne EXACTEMENT, mot à mot, en arabe avec diacritiques. Ne devine JAMAIS : un mot illisible → [lettres lisibles?]. Transcris tout nombre CHIFFRE PAR CHIFFRE (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9) en NUM: <chiffres latins>.`;
const TASKS = [
  { tag: 'z130-ref', ask: `${BASE}\nUn renvoi bleu entre crochets [سورة ... الآية: N] est imprimé. Transcris-le AU COMPLET : le nom de la sourate lettre par lettre, le mot الآية, puis le chiffre N — décris la FORME de chaque chiffre (nombre de points en haut, boucle ouverte ou fermée) et transcris-le en NUM:. S'il n'y a AUCUN chiffre imprimé, dis-le explicitement.` },
  { tag: 'z133-ali', ask: `${BASE}\nTranscris le hadith d'ʿAlī EXACTEMENT : il commence par «فقد ثبت عن علي رضي الله عنه: أنّ رسول الله ﷺ نحر...» — transcris le complément de نحر (بيده ? بعض هديه ?) puis le second membre (ونحر ... : غيره ? بضعه ? بيده ? بعينه ?), et le renvoi [الموطأ رقم: N] en NUM:.` },
  { tag: 'z134-1185', ask: `${BASE}\nTranscris les lignes : «... قال رضي الله عنه: من ضفر(ضَفَّرَ) رأسه فليحلق، ولا تشبهوا بـ...» — le DERNIER mot après بـ EXACTEMENT lettre par lettre (التلبيد ? الملبدين ? الملبد ? النبي ?), puis le renvoi [الموطأ رقم: N] en NUM:, puis la phrase suivante (فإن من تشبه به وجب عليه...).` },
  { tag: 'z134-1186', ask: `${BASE}\nTranscris le hadith d'ʿUmar complet : «عن سعيد بن المسيب أن عمر بن الخطاب رضي الله عنه قال: من عقص(عَقَصَ) رأسه، أو ...، أو ...، فقد وجب عليه الحلاق» — transcris les DEUX mots après أو EXACTEMENT (ضَفَرَ ? حَلَقَهُ ? لَبَّدَ ?) et le renvoi [الموطأ رقم: N] en NUM:.` },
  { tag: 'z135-ath1', ask: `${BASE}\nTranscris la première ligne de l'athar : «عن عبد الله بن عمر: أنه لقي رجلاً من أهله بـ...» — transcris le mot qui suit بـ EXACTEMENT lettre par lettre (بالبقيع ? بعرفة ? بالمجبر ? بفال ?) et la fin de ligne (قد أفاض...?).` },
];

async function readOne(zai, t) {
  const out = `${OUTDIR}/r682c-${t.tag}.txt`;
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
  for (const t of TASKS) console.log(await readOne(zai, t));
}
main().catch(e => { console.error('FATAL', e); process.exit(1); });
