// Z2-31 — hadith-5ep leçon 26 «الاستقامة» (pp.144-149, hadith 21 Arbaʿūn, Sufyān ibn ʿAbd Allāh
// ath-Thaqafī «قُلْ آمَنْتُ بِاللهِ ثُمَّ اسْتَقِمْ») — lectures VLM pleine page 150 dpi.
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-26';
const COMMON = `Page entière (150 dpi) d'un manuel scolaire marocain d'hadith (5e année primaire traditionnel), leçon 26 «الاستقامة» (pp.144-149), sens de lecture droite→gauche.
TRANSCRIS TOUT ce qui est imprimé sur la page, rubrique par rubrique, mot à mot, avec la vocalisation. Balise les titres de rubrique comme [TITRE] ... [/TITRE], les encadrés comme [CADRE] ... [/CADRE], les hadiths et versets entre « » avec leurs références entre crochets. Les bandeaux décoratifs illisibles : [؟]. Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé.`;

const Q = {
  144: `Page 144 : le bandeau de titre de la leçon (transcris le numéro EXACTEMENT — chiffres arabes orientaux — et le titre complet), أهداف الدرس (3 objectifs numérotés — transcris mot à mot), le texte d'introduction (تمهيد — jusqu'aux questions finales). Transcris tout.`,
  145: `Page 145 : la rubrique تَرْجِمَةُ الرَّاوِي (notice du compagnon سفيان بن عبد الله الثقفي — transcris mot à mot : nom, surnom éventuel, origine, ce qui suit), puis L'ENCADRÉ DU HADITH (header الأحاديث + sanad — transcris le nom du rāwī EXACTEMENT mot à mot — PUIS le matn complet mot à mot avec la vocalisation, avec la référence si visible), puis اَلْفَهْمُ (اَلشَّرْحُ : gloses en tirets — transcris chaque glose mot à mot), puis اِسْتِخْلَاصُ الْمَضَامِينِ (questions numérotées), puis le début du التَّحْلِيل si visible (phrase d'intro + أولاً: مَعْنَى الِاسْتِقَامَةِ وَعَلَاقَتِهَا بِالْإِيمَانِ + 1. مَعْنَى الِاسْتِقَامَةِ — لغةً et شرعاً). Transcris tout.`,
  146: `Page 146 : suite du التَّحْلِيل أولاً 1. مَعْنَى الِاسْتِقَامَةِ (suite لغةً/شرعاً, explication de قَوْلُ السَّائِلِ «هَلْ لِي فِي الْإِسْلَامِ قَوْلٌ لَا أَسْأَلُ عَنْهُ أَحَدًا غَيْرَكَ» et de la réponse «قُلْ آمَنْتُ بِاللهِ ثُمَّ اسْتَقِمْ», جَوَامِعُ الْكَلِمِ, le verset [فصلت: ...] AVEC SA RÉFRENCE EXACTE telle qu'imprimée, le commentaire de ʿUmar ibn al-Khaṭṭāb, le dire d'Ibn ʿAbbās avec sa référence), puis 2. عَلَاقَةُ الِاسْتِقَامَةِ بِالْإِيمَانِ si visible. Transcris tout.`,
  147: `Page 147 : 2. عَلَاقَةُ الِاسْتِقَامَةِ بِالْإِيمَانِ (تلازم...العطف بـ «ثم»...), puis ثانياً: فَضْلُ الِاسْتِقَامَةِ وَثَمَرَاتُهَا (citation d'al-Qushayrī, hadith de [الموطأ] «اسْتَقِيمُوا...», citation d'al-Wāsiṭī, la liste des ثمرات, le verset [فصلت: ...] complet AVEC SA RÉFRENCE EXACTE telle qu'imprimée — transcris chaque ligne du verset mot à mot), puis وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ (items en tirets). Transcris tout.`,
  148: `Page 148 : suite et fin de وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ (items en tirets — transcris-les TOUS), puis اَلتَّقْوِيمُ (questions numérotées — transcris-les toutes), puis الاِسْتِثْمَارُ (l'ENCADRÉ du hadith d'Anas ibn Mālik complet mot à mot avec sa référence, PUIS les activités numérotées). Transcris tout.`,
  149: `Page 149 : la fin des activités de الاِسْتِثْمَارُ si visible, puis la rubrique الاِعْدَادُ الْقَبْلِيُّ (items numérotés — transcris-les tous mot à mot), PUIS le bandeau de la leçon SUIVANTE s'il est visible (الدَّرْسُ + numéro EXACT + titre) et ses أهداف, sinon la ligne de séparation. Transcris tout.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const p of Object.keys(Q)) {
  const out = `${DIR}/vlm26-p-${p}.txt`;
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
