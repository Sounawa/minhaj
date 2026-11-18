// Z2-32 — hadith-5ep leçon 27 «مما يدخل الجنة» (pp.150-155, hadith 22 Arbaʿūn, Jābir) —
// lectures VLM pleine page 150 dpi.
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-27';
const COMMON = `Page entière (150 dpi) d'un manuel scolaire marocain d'hadith (5e année primaire traditionnel), leçon 27 «مما يدخل الجنة» (pp.150-155), sens de lecture droite→gauche.
TRANSCRIS TOUT ce qui est imprimé sur la page, rubrique par rubrique, mot à mot, avec la vocalisation. Balise les titres de rubrique comme [TITRE] ... [/TITRE], les encadrés comme [CADRE] ... [/CADRE], les hadiths et versets entre « » avec leurs références entre crochets. Les bandeaux décoratifs illisibles : [؟]. Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé.`;

const Q = {
  150: `Page 150 : le bandeau de titre de la leçon (numéro EXACT en chiffres arabes orientaux + titre complet), أهداف الدرس (3 objectifs numérotés — mot à mot), puis le texte d'introduction (تمهيد — jusqu'aux questions finales incluses). Transcris tout.`,
  151: `Page 151 : L'ENCADRÉ DU HADITH (fond ornementé) avec son en-tête, le sanad complet (le nom du rāwī EXACTEMENT — mot à mot), le matn complet mot à mot avec la vocalisation (la question de l'homme et la réponse), et la référence ; puis تَرْجِمَةُ الرَّاوِي (notice de Jābir — mot à mot : nom, lignée, mort, nombre de hadiths), puis اِسْتِخْلَاصُ الْمَضَامِينِ (questions numérotées), puis le début du التَّحْلِيل (phrase d'intro sur le questionneur + أولاً si visible). Transcris tout.`,
  152: `Page 152 : le début du التَّحْلِيل (la phrase sur le questionneur النعمان بن قوقل et ce qu'il mentionne comme farā'iḍ), puis أولاً: مَعْنَى «أَحْلَلْتُ الْحَلَالَ وَحَرَّمْتُ الْحَرَامَ» (le commentaire d'an-Nawawī et d'Ibn aṣ-Ṣalāḥ — mot à mot), puis ثانياً: حُكْمُ الِاكْتِفَاءِ بِالْفَرَائِضِ (l'explication + le récit de Ṭalḥa ibn ʿUbayd Allāh — l'homme venu questionner sur l'islam, les cinq prières, le jeûne, la zakāt, «هل علي غيرهن؟»... — transcris le hadith complet mot à mot avec sa référence). Transcris tout.`,
  153: `Page 153 : la suite de ثانياً (المفهوم: ce que indique la réponse du Prophète sur les tatavvu'āt), puis ثالثاً: فَضْلُ الِاسْتِزَادَةِ مِنَ الْمُتَطَوُّعَات (mot à mot : ce que indiquent «نعم» et «لا إلا أن تطوع» et «أفلح الرجل إن صدق», les Compagnons et les sunan, l'avis du Prophète sur le questionneur récent à l'islam, la crainte du tanfīr), puis le الخلاصة (la somme sur la محافظة sur les farā'iḍ et l'ajout des tatavvu'āt), puis la phrase finale sur la shari'a et la miséricorde. Transcris tout.`,
  154: `Page 154 : وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ (items en tirets — transcris-les TOUS), puis اَلتَّقْوِيمُ (questions numérotées — transcris-les toutes), puis le début de الاِسْتِثْمَارُ (l'en-tête et le début de l'encadré du hadith si visible — mot à mot). Transcris tout.`,
  155: `Page 155 : l'encadré du hadith de الاِسْتِثْمَارُ (matn complet mot à mot avec TOUTES les références et notes imprimées entre crochets — y compris les mentions d'ouvrages), puis les activités numérotées, puis الاِعْدَادُ الْقَبْلِيُّ (items numérotés — mot à mot). Transcris tout.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const p of Object.keys(Q)) {
  const out = `${DIR}/vlm27-p-${p}.txt`;
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
