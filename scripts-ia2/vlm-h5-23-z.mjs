// Z2-27 — hadith-5ep leçon 23 — VLM sur zooms 600 dpi (série V) : bandeaux/cadres illisibles par tesseract
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-23';
const COMMON = `Recadrage haute résolution (600 dpi) d'un manuel scolaire marocain d'hadith (5e année primaire), sens de lecture droite→gauche.
TRANSCRIS mot à mot, avec la vocalisation, uniquement ce qui est imprimé. Ne complète JAMAIS par mémoire d'un texte connu.`;

const Q = {
  V01: `Bandeau décoré de titre de leçon. Donne : 1) le mot الدَّرْسُ ; 2) le NUMÉRO en chiffres arabes orientaux (٢٣ ou ٢٤ ou autre — lis attentivement les chiffres du médaillon) ; 3) le TITRE complet de la leçon qui suit. Format : الدرس / numéro / titre`,
  V02: `Les trois objectifs numérotés de أَهْدَافُ الدَّرْسِ. Transcris les 3 lignes COMPLÈTES mot à mot avec vocalisation (1. أَنْ أَتَعَرَّفَ... 2. ... 3. ...).`,
  V03: `Une ligne de question du تمهيد : فَمَا التَّقْوَى؟ ... Transcris la ligne complète — attention au verbe appliqué aux gens (نُخَالِطُ / نُحَافِظُ / autre ?) : «وَمَا الْخُلُقُ الْحَسَنُ الَّذِي ... بِهِ النَّاسُ؟»`,
  V04: `Trois gloses du الشرح (الفهم). Transcris les 3 entrées MOT À MOT : la première commence par اتَّقِ اللهَ, la deuxième est le mot du hadith تَمْحُهَا suivi de deux verbes, la troisième خَالِقِ النَّاسَ. Attention à la 2e glose : deux verbes après تَمْحُهَا: (تُزِيلُ ... وَ...).`,
  V05: `Encadré décoré contenant un verset coranique avec sa référence. Transcris le texte vocalisé complet + la référence [هود : ...] exactement.`,
  V06: `Deux lignes sur les manifestations du bon caractère. Transcris mot à mot : ... وَتَوْقِيرُ كَبِيرِهِمْ... ثم la ligne avec كَفِّ/كُفِّ الْأَذَى... et الْكَذِب... Transcris tout ce qui est imprimé.`,
  V07: `La rubrique وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ en entier : les items sont précédés de tirets (pas de numéros). Transcris CHAQUE item complètement mot à mot — je crois qu'il y a 4 items. Le 2e contient يُحَقِّقُ ... بَعْضِهِمْ لِبَعْضٍ... et le 3e commence par أَنَّ مِنْ ... اللهِ (رحمة ? نعمة ?) أَنْ جَعَلَ الْحَسَنَاتِ يُذْهِبْنَ السَّيِّئَاتِ...`,
  V08: `Encadré décoré contenant un passage coranique [آل عمران] de plusieurs versets (133 à 136). Transcris le texte coranique vocalisé COMPLET mot à mot, avec les numéros de versets entre accolades s'ils sont imprimés, et la référence finale [آل عمران : ...] exactement.`,
  V09: `Trois activités numérotées de la rubrique اِسْتِثْمَار. Transcris les 3 items complets (1. أَسْتَخْرِجُ... 2. أُبَيِّنُ... 3. ...) mot à mot.`,
  V10: `La rubrique الإِعْدَادُ الْقَبْلِيُّ complète : l'item 1 (أَحْفَظُ حَدِيثَ الدَّرْسِ الْآتِي...) suivi de ses sous-items (un extrait du hadith à mémoriser contenant ...أَخْطَأَكَ... ثم أَبَيِّنُ مَعْنَى حِفْظِ اللهِ...), l'item 2 et l'item 3. Transcris TOUT mot à mot.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const t of Object.keys(Q)) {
  const out = `${DIR}/vlm23-${t}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${t}`); continue; }
  const img = fs.readFileSync(`${DIR}/z23-${t}.png`).toString('base64');
  console.log(`\n======== ${t} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q[t] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 2048,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 500 ? txt.slice(0, 250) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${t} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(3000);
}
