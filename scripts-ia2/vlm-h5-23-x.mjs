// Z2-27 — VLM arbitrages finaux sur zooms X natifs 600 dpi
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-23';
const COMMON = `Recadrage natif 600 dpi d'un manuel scolaire marocain d'hadith (5e primaire), droite→gauche. Texte possiblement en BLANC sur fond décoré.
TRANSCRIS mot à mot, avec vocalisation, uniquement ce qui est imprimé. Ne complète JAMAIS par mémoire.`;

const Q = {
  X01: `Bandeau de titre de leçon, en trois parties : le mot الدَّرْسُ (à droite), un NUMÉRO en chiffres arabes orientaux (au centre, dans un médaillon), et le TITRE (à gauche). Donne les trois SÉPARÉMÉMENT, exactement comme imprimés : 1) mot de droite 2) numéro (lis chiffre par chiffre : ٢ ٣ ou ٢ ٤ ?) 3) titre complet. Attention : le titre a peut-être DEUX mots (التَّقْوَى ... ?) — transcris tout ce qui est imprimé dans le bandeau.`,
  X02: `Objectif n°3 de أهداف الدرس, ligne complète commençant par «3.». Trois lectures divergentes m'ont été proposées : (a) أَنْ أَتَمَثَّلَ تَقْوَى اللهِ وَالْمُحَافَظَةَ عَلَى الْحَسَّنَةِ (b) أَنْ أَتَمَثَّلَ تَقْوَى اللهِ وَالْمُحَافَظَةَ عَلَى أَخْلَاقِيَ (c) autre. Transcris la ligne MOT À MOT, surtout la fin après وَالْمُحَافَظَةَ.`,
  X03: `Glose du شرح : تَمْحُهَا : ... آثَارَهَا وَ... Transcris la glose complète. Le 1er verbe : تُذْهِبُ ou تُزِيلُ ou autre ? Le 2e : وَتُلْغِيهَا ou autre ?`,
  X04: `Encadré décoré de verset coranique (blanc sur fond). Transcris le texte vocalisé COMPLET ligne par ligne, et la référence [هود : ...]. Le cadre contient peut-être une ou deux phrases — tout transcrire.`,
  X05: `Activité n°1 : أَسْتَخْرِجُ مَا تَضَمَّنَتْهُ الْآيَاتُ مِنَ الْأَخْلَاقِ الَّتِي تُعْتَبَرُ مِنْ أَوْصَافِ ... Le DERNIER mot : الْمُتَّقِينَ ou الْمُنَافِقِينَ ou autre ? Transcris l'activité complète.`,
  X06: `Sous «1. أَحْفَظُ حَدِيثَ الدَّرْسِ الْآتِيَ وَأَقُومُ بِمَا يَلِي:» il y a un EXTRAIT du hadith à mémoriser (avant «2. أُشْرِحُ:»). Transcris CET EXTRAIT mot à mot — sans t'appuyer sur ta mémoire du hadith connu, seulement sur l'image.`,
  X07: `Premier groupe de mots du verset 133 après ﴿ : transcris-le exactement. سَابِقُوا ou سَارِعُوا ou وَسَارِعُوا ? Regarde bien : la 2e lettre (ب ou ا ?), la 4e lettre (ق ou ع ?), et s'il y a un wāw initial.`,
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1024,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 420 ? txt.slice(0, 210) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${t} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(2500);
}
