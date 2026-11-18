// Z2-33 — hadith-5ep leçon 28 «دعم وتطبيق» (pp.156-158, leçon de SYNTHÈSE sans encadré de hadith)
// — lectures VLM pleine page 150 dpi.
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-28';
const COMMON = `Page entière (150 dpi) d'un manuel scolaire marocain d'hadith (5e année primaire traditionnel), leçon 28 «دعم وتطبيق» (pp.156-158, leçon de consolidation et d'application, SANS encadré de hadith), sens de lecture droite→gauche.
TRANSCRIS TOUT ce qui est imprimé sur la page, rubrique par rubrique, mot à mot, avec la vocalisation. Balise les titres de rubrique comme [TITRE] ... [/TITRE]. Les hadiths et versets entre « » avec leurs références entre crochets. Précise pour chaque ligne du texte principal si elle est en GRAS/GROS caractères (titre) ou en corps normal. Les bandeaux décoratifs illisibles : [؟]. Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé.`;

const Q = {
  156: `Page 156 : le bandeau [TITRE] أهداف الدرس avec le numéro de leçon EXACT en chiffres arabes orientaux, les 3 objectifs numérotés mot à mot ; puis le bandeau النص ; puis DÉCRIS la mise en page du texte : la première ligne «جاء الإسلام لتربية الإنسان...» est-elle un TITRE en gras/gros caractères ou une phrase du corps ? Y a-t-il une phrase intermédiaire (عقيدة وعبادة من أجل استقامة أخلاقه...) ? Transcris ENSUITE tout le texte mot à mot avec la vocalisation : la phrase d'ouverture complète, le hadith «إنما بعثت...» avec SA RÉFÉRENCE EXACTE entre crochets, les phrases sur l'homme rahma, la phrase sur «وما قد يحدث من تصرفات سيئة...» jusqu'à «غير مستيم» EXACTEMENT, puis «يقول الرسول صلى الله عليه وسلم...» et le hadith «قد تركتكم على المحجة البيضاء...» MOT À MOT avec le mot qui suit «على» (المحجة ?) et sa référence [المستدرك للحاكم]. Transcris tout.`,
  157: `Page 157 : le bandeau [TITRE] الفهم avec ses 3 questions numérotées mot à mot (les mots à expliquer un à un — ATTENTION au mot الغضب الـمـ...م : lis lettre par lettre مذموم ou مدموم ? et المحجة البيضاء) ; puis le bandeau [TITRE] التحليل avec ses questions numérotées et sous-questions en tirets mot à mot, y compris la question 2 sur ثمرات الخلق الحسن, la question 3 complète (avec sa fin — في المجتمع ?) et la question 4 avec le VERSET coranique complet mot à mot et sa référence [الأنبياء : N] — donne le numéro EXACT imprimé. Transcris tout.`,
  158: `Page 158 : le bandeau [TITRE] de la section (التقويم ? التطبيق ? lis le mot EXACT du bandeau décoratif si lisible, sinon dis [؟]) ; puis la phrase d'introduction «أوظف مكتسباتي...» mot à mot ; puis les 2 questions numérotées mot à mot avec leurs sous-puces en tirets (في معاملة الأولاد لآبائهم وأمهاتهم — في علاقة الفرد بمجتمعه). Y a-t-il une rubrique الإعداد القبلي ou autre chose en bas de page ? Transcris tout.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const p of Object.keys(Q)) {
  const out = `${DIR}/vlm28-p-${p}.txt`;
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 3000,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 600 ? txt.slice(0, 350) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} p${p} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(3000);
}
