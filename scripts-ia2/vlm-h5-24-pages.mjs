// Z2-28 — hadith-5ep leçon 24 «حفظ أوامر الله تعالى» (p.131+, hadith 19 Arbaʿūn, Ibn ʿAbbās) — lectures VLM pleine page 150 dpi (bornage + couche V)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-24';
const COMMON = `Page entière (150 dpi) d'un manuel scolaire marocain d'hadith (5e année primaire traditionnel), leçon 24 «حفظ أوامر الله تعالى» (p.131+), sens de lecture droite→gauche.
TRANSCRIS TOUT ce qui est imprimé sur la page, rubrique par rubrique, mot à mot, avec la vocalisation. Balise les titres de rubrique comme [TITRE] ... [/TITRE], les encadrés comme [CADRE] ... [/CADRE], les hadiths et versets entre « » avec leurs références entre crochets. Les bandeaux décoratifs illisibles : [؟]. Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé.`;

const Q = {
  131: `Page 131 : le bandeau de titre de la leçon (transcris le numéro EXACTEMENT — chiffres arabes orientaux — et le titre complet), أهداف الدرس (3 objectifs numérotés — transcris mot à mot), le texte d'introduction (تمهيد — avec sa phrase complète), la question de transition, l'en-tête الْأَحَادِيثُ et L'ENCADRÉ DU HADITH (sanad : Abū al-ʿAbbās ʿAbd Allāh b. ʿAbbās — transcris le récit-cadre «كنت...رسولَ الله ﷺ» PUIS le matn complet mot à mot : «يَا غُلَامُ...» jusqu'à la fin de la page, avec la référence si visible). Transcris tout.`,
  132: `Page 132 : suite de l'encadré du hadith d'Ibn ʿAbbās (اعلم أن الأمة لو اجتمعت... — transcris mot à mot jusqu'à la fin du matn et la référence entre crochets), puis la rubrique تَرْجَمَةُ الرَّاوِي (notice ʿAbd Allāh b. ʿAbbās : éloges, dates — transcris EXACTEMENT), puis le début de الْفَهْمُ (اَلشَّرْحُ : gloses en tirets — transcris chaque glose mot à mot ; اِسْتِنْتَاجُ الْمَضَامِينَ : questions numérotées). Transcris tout.`,
  133: `Page 133 : la suite (الشَّرْح suite ou التَّحْلِيل début — phrase d'intro يشتمل الحديث على... puis أولاً / ثانياً / ثالثاً si présents : transcris chaque titre numéroté et son paragraphe complet, avec toute citation prophétique ou coranique et sa référence). Transcris tout.`,
  134: `Page 134 : la suite du التَّحْلِيل (titres أولاً/ثانياً/ثالثاً... : transcris chaque titre et son paragraphe complet mot à mot, citations et références comprises). Transcris tout.`,
  135: `Page 135 : suite et éventuelle FIN de la leçon : rubriques وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ (items en TIRETS — transcris-les TOUS), اَلتَّقْوِيمُ (questions numérotées), et si présents الاِسْتِثْمَار (ENCADRÉ DU VERSET coranique vocalisé complet + référence EXACTE + activités numérotées) et الإِعْدَادُ الْقَبْلِيُ (items numérotés). Y a-t-il en bas de page le bandeau de la leçon SUIVANTE (الدَّرْسُ ٢٥) ? Transcris tout.`,
  136: `Page 136 : cette page contient-elle la FIN de la leçon «حفظ أوامر الله تعالى» (تقويم / استثمار / إعداد قبلي) ou le DÉBUT de la leçon suivante (bandeau الدَّرْسُ ٢٥ + titre + أهداف) ? Transcris tout, y compris tout bandeau de titre de leçon (الدَّرْسُ + numéro EXACT) et les rubriques visibles.`,
  137: `Page 137 : contenu de cette page — suite de quelle leçon ? Transcris tout, y compris tout bandeau de titre de leçon (الدَّرْسُ + numéro EXACT), les rubriques et leurs textes.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const p of Object.keys(Q)) {
  const out = `${DIR}/vlm24-p-${p}.txt`;
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
