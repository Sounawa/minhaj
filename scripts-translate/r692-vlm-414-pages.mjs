// R692 — lectures VLM pages pleines leçon 414 hadith-3es (شروط الأضحية, p.164-169).
// Usage: node scripts-translate/r692-vlm-414-pages.mjs
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/pages-414';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-414';
fs.mkdirSync(OUTDIR, { recursive: true });

const BASE = `Page d'un manuel scolaire arabe (hadith, 3e année secondaire, Muwaṭṭaʾ de l'imam Mālik). Transcris EXACTEMENT tout le texte visible, ligne par ligne, en arabe, en conservant diacritiques, crochets [] et guillemets « ». Pour tout renvoi entre crochets de la forme [الموطأ رقم: N] ou [سورة X آية: N], transcris le nombre N CHIFFRE PAR CHIFFRE (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9) sous la forme NUM: <chiffres latins>. Ne devine rien : transcris ce qui est visible, marque [?] l'illisible.`;

const PAGES = [
  { tag: 'p164', ask: `${BASE}\nTranscris TOUTE la page (fin de leçon précédente p.164 en haut s'il y a : hadith n° 1352 de البراء « العرجاء البين ظلعها », puis ouverture de leçon : médaillon درس 25 « شروط الأضحية وحكم الشركة فيها », les trois objectifs numérotés, le تمهيد avec questions, début du hadith n° 1352 — chiffres chiffre par chiffre).` },
  { tag: 'p165', ask: `${BASE}\nTranscris TOUTE la page (suite des hadiths : الجذعاء التي تفصد من خلفها avec قال يحيى فأما الجذعاء, le hadith n° 1350 de جابر « تحرنا مع رسول الله كل عام الحديبية البدنة عن سبعة والبقرة عن سبعة », la notice biographique de جابر بن عبد الله, la rubrique الشرح avec ses trois gloses ظلعها/العجفاء/لا تنقي, la rubrique استخلاص المضامين).` },
  { tag: 'p166', ask: `${BASE}\nTranscris TOUTE la page (استخلاص المضامين items 2 et 3, rubrique أولا: شروط الأضحية / سلامتها من العيوب avec les quatre défauts détaillés أ- العرجاء ب- العوراء ج- المريضة د- الجفاء, les citations entre « » et les mots du Prophète ﷺ).` },
  { tag: 'p167', ask: `${BASE}\nTranscris TOUTE la page (fin des عيوب avec le hadith d'أبو داود والنسائي عن علي « أمرنا رسول الله أن نستشرف العين ولا نضحي بالمنابلة ولا بالمضابرة ولا شرقاء ولا حرقاء » avec ses définitions, puis بلوغها سن الإجزاء avec le texte de الموطأ عن نافع عن عبد الله بن عمر sur les âges : الضأن سنة, المعز سنة, البقر ثلاث, الإبل خمس).` },
  { tag: 'p168', ask: `${BASE}\nTranscris TOUTE la page (كمال خلقها avec « ما تفسد من خلَقِها », ثم ثانيا: الشركة في الأضحية : le avis de مالك, la citation du Muwaṭṭaʾ sur « أن يشتري الناقر البدنة أو البقرة أو الشاة » avec son numéro [الموطأ رقم: N], le hadith d'أبو أيوب « كنا نضحي بالشاة الواحدة », les propos de مالك sur le بيت البدنة, le texte d'ابن شهاب « ما تحر رسول الله عنه وعن أهل بيته إلا بدنة واحدة », le texte de عبد الله بن عمر « لم يكن يضحي عما في بطن المرأة », chiffres chiffre par chiffre).` },
  { tag: 'p169', ask: `${BASE}\nTranscris TOUTE la page (rubrique استخلاص المضامين ou التقويم avec items numérotés, l'athar d'أم سلمة sur تَدْخِير les ضحايا « ادخروا لثلاث سنوات وتصدقوا بما بقي... الدافة », الاستثمار, الإعداد القبلي avec ses items numérotés sur العقيقة, chiffres chiffre par chiffre).` },
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
        model: 'glm-5v-turbo',
        temperature: 0.1,
      });
      const txt = res.choices?.[0]?.message?.content || '';
      if (txt.trim().length < 100) throw new Error('réponse trop courte');
      fs.writeFileSync(out, txt);
      console.log(t.tag, 'OK', txt.length, 'car');
      return;
    } catch (e) {
      console.log(t.tag, 'essai', k, 'échec:', e.message);
      await new Promise(r => setTimeout(r, 1500 * k));
    }
  }
  console.log(t.tag, 'ABANDON');
}

const zai = await ZAI.create();
for (const t of PAGES) await readOne(zai, t);
console.log('VLM 414 terminé');
