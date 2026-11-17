// Z2-24 — hadith-5ep leçon 21 — lectures VLM pleine page 150 dpi (pp.114-119)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-21';
const COMMON = `Page entière (150 dpi) d'un manuel scolaire marocain d'hadith (5e année primaire traditionnel), leçon 21 (pp.114-119), sens de lecture droite→gauche.
TRANSCRIS TOUT ce qui est imprimé sur la page, rubrique par rubrique, mot à mot, avec la vocalisation. Balise les titres de rubrique comme [TITRE] ... [/TITRE], les encadrés comme [CADRE] ... [/CADRE], les hadiths entre « ». Les bandeaux décoratifs illisibles : [؟]. Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé.`;

const Q = {
  114: `Page 114 : bandeau de titre de la leçon 21 (transcris-le), أهداف الدرس (objectifs numérotés), puis le début du texte d'introduction (تمهيد/تهيئة). Transcris tout.`,
  115: `Page 115 : suite de l'introduction (si présente), la notice du transmetteur (ترجمة الراوي), l'encadré du hadith (النص), la rubrique الشرح (gloses), استخلاص المضامين, et le début du التحليل (أولاً: النهي عن الغضب...). Transcris tout.`,
  116: `Page 116 : suite du التحليل : la suite de أولاً (المراد بقوله ﷺ «لا تغضب»، hadith عطية السعدي، الاستعاذة بالله من الشيطان) puis ثانياً (ملك النفس عند الغضب، الثمرات، آية). Transcris tout avec les refs entre crochets.`,
  117: `Page 117 : suite des الثمرات (آيات, hadiths) et la fin du التحليل. Transcris tout avec les refs.`,
  118: `Page 118 : fin du التحليل (الأغراض السلبية...) , la partie sur الصحابي والنصيحة (مما يستفاد?), la rubrique التقويم (questions numérotées). Transcris tout.`,
  119: `Page 119 : la rubrique الاستثمار (hadiths avec refs), la rubrique الإعداد القبلي, et le début de la leçon 22 (أهداف: الإحسان) s'il est visible. Transcris tout.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const p of Object.keys(Q)) {
  const out = `${DIR}/vlm21-p-${p}.txt`;
  if (fs.existsSync(out)) { console.log(`skip p${p}`); continue; }
  const img = fs.readFileSync(`${DIR}/r150/p${p}.png`).toString('base64');
  console.log(`\n======== p${p} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: COMMON + '\n\n' + Q[p] },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 2048,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 600 ? txt.slice(0, 300) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} p${p} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(3000);
}
