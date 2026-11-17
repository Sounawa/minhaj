// Z2-26 — hadith-5ep leçon 22 «الإحسان في كل شيء» (pp.120-124) — lectures VLM pleine page 150 dpi
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-22';
const COMMON = `Page entière (150 dpi) d'un manuel scolaire marocain d'hadith (5e année primaire traditionnel), leçon 22 (pp.120-124), sens de lecture droite→gauche.
TRANSCRIS TOUT ce qui est imprimé sur la page, rubrique par rubrique, mot à mot, avec la vocalisation. Balise les titres de rubrique comme [TITRE] ... [/TITRE], les encadrés comme [CADRE] ... [/CADRE], les hadiths et versets entre « » avec leurs références entre crochets. Les bandeaux décoratifs illisibles : [؟]. Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé.`;

const Q = {
  120: `Page 120 : le bandeau de titre de la leçon (transcris numéro + titre EXACTEMENT — le numéro en chiffres arabes orientaux et le titre complet), أهداف الدرس (3 objectifs numérotés), le texte d'introduction (تمهيد), la question de transition, l'en-tête de la section du hadith et L'ENCADRÉ DU HADITH COMPLET (sanad + matn + référence) — c'est un encadré important. Transcris tout.`,
  121: `Page 121 : la notice du transmetteur (ترجمة الراوي — Shaddād ibn Aws), la glose du الشرح (كتب الإحسان...), la rubrique استخلاص المضامين (2 questions), et le début du التحليل : la phrase d'intro (يشتمل الحديث على فقه عظيم...) puis le titre أولاً (معنى الإحسان في كل شيء) et ses premières lignes (قول الرسول ﷺ..., مبنى الإحسان...). Transcris tout.`,
  122: `Page 122 : suite de أولاً (معنى الإحسان في كل شيء) : le hadith de Ǧibrīl ou l'extrait « أن تعبد الله... », la phrase sur المعاملات (البيع والشراء, hadith رحم الله رجلاً...), le verset sur الحوار والجدال [العنكبوت], le hadith « إن الله يحب إذا عمل أحدكم عملاً أن يتقنه » ; puis le titre ثانياً (الإحسان إلى الحيوان) et son développement (hadith « في كل ذات كبد رطبة », hadith de la femme et la chatte...). Transcris tout avec les références.`,
  123: `Page 123 : suite de ثانياً : le passage sur le sacrifice (فإذا قتلتم فأحسنوا القتلة..., les règles détaillées : يحد الشفرة, يوجهها إلى القبلة, يقطع الحلقوم والودجين...), la phrase sur ضوابط ذبح البهائم, puis la fin de la leçon : الإحسان في عقيدته وسلوكه..., الإحسان في معاملة الجار, الإحسان إلى الوالدين, le passage sur المحسن يستحق محبة الله + verset [الرحمن], et la conclusion (الإحسان مبدأ إسلامي عام...). Transcris tout.`,
  124: `Page 124 : la rubrique التقويم (3 questions), puis l'encadré du verset [النساء: 36] avec ses gloses numérotées (بين نوعين من الإحسان... / لاحظ...), et la rubrique الإعداد القبلي (2 items). Transcris tout.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const p of Object.keys(Q)) {
  const out = `${DIR}/vlm22-p-${p}.txt`;
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
