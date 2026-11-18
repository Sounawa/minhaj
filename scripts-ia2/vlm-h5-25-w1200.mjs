// Z2-30 — VLM scruterins finaux à 1200 dpi natif (leçon 25)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-25/crops';
const COMMON = `Recadrage NATIF 1200 dpi (très net) d'un manuel scolaire marocain d'hadith, 5e année primaire, lecture droite→gauche.
TRANSCRIS le(s) mot(s) imprimé(s) LETTRE PAR LETTRE : pour chaque lettre donne sa forme, SON NOMBRE DE POINTS (0/1/2/3, dessus/dessous) et ses dents, puis conclus. Ne complète JAMAIS par mémoire d'un texte connu.`;

const Q = {
  'w1-p139': `Fin de glose du الشرح : «... أَوْ هُوَ خَبَرٌ بِمَعْنَى: مَنْ لَمْ يَكُنْ عِنْدَهُ حَيَاءٌ فَعَلَ كُلَّ مَا ...». Le DERNIER mot : décompose-le lettre par lettre. Candidats : يُسْتَقْبَحُ / يُسْتَكْرَهُ / يُسْتَتْكَرُ / يُسْتَحْقَرُ / يُسْتَكْثَرُ / autre. Attention : compte les points de CHAQUE lettre (le ق a 2 points AU-DESSUS, le ت 2 points AU-DESSUS, le ب 1 point EN DESSOUS, le ح 0 point, le ك marque en selle, le خ 1 point AU-DESSUS).`,
  'w2-p140': `Fin de ثانيهما : «... وَالْمُرَادُ: مَنْ لَمْ يَكُنْ عِنْدَهُ حَيَاءٌ فَعَلَ كُلَّ مَا ...». Le DERNIER mot : même scrutin lettre par lettre. Candidats : يُسْتَقْبَحُ / يُسْتَكْرَهُ / يُسْتَتْكَرُ / يُسْتَحْقَرُ / يُسْتَكْثَرُ / autre.`,
  'w3-p140': `Dernier mot de la définition lexicale (après وَالِامْتِنَاعِ وَالتَّرْكِ) : وَالِاسْتَ...ـاءُ. Décompose lettre par lettre. Candidats : الِاسْتِحْيَاءُ / الِاسْتِبْقَاءُ / الِاسْتِيفَاءُ / الِاسْتِحْفَاءُ / autre.`,
  'w4-p141': `Dans «وَلَيْسَ مِنَ الْحَيَاءِ فِعْلُ الْمَعَاصِي وَتَ...ـيلَ(؟) ...الْمُحَرَّمَاتِ» — le mot entre وَ et (éventuelles lettres avant) الْمُحَرَّمَاتِ. Décompose lettre par lettre. Candidats : وَتَحْلِيلُ / وَتَخْلِيلُ / وَتَكْلِيلُ / وَتَقْلِيلُ / autre. Et s'il y a des lettres/mots entre ce mot et الْمُحَرَّمَاتِ, transcris-les aussi.`,
  'w5-p138': `2e ligne du تمهيد : «... ضَمَّنِ الْمَحَامِدِ فِي مَأْثُورِ كُلِّ ...، وَ...ـهَا الشَّرِيعَةُ الْإِسْلَامِيَّةُ، وَعَدَّتْهَا مِنْ...». Deux scrutins : (a) après كُلِّ : الْأُمَمِ (pluriel) ou أُمَّةٍ (singulier) ? (b) le mot entre «، وَ» et «الشَّرِيعَةُ» : أَكَّدَتْهَا (kāf avec shadda, pas d'alif après) ou كَانَتْهَا (kāf + alif, pas de shadda) ? Décompose les DEUX mots lettre par lettre.`,
  'w6-p138': `3e objectif (أهداف) — segment entre «أَتَمَثَّلَ الْمَقَاصِدَ» et «مِنْ تَشْرِيعِ الْحَيَاءِ». Transcris le(s) mot(s) du segment médian lettre par lettre. Candidats : الشَّرْعِيَّةَ / الرُّوحِيَّةَ / عَبْرَ / عِبْرَةً / النَّشِرَ / autre.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of Object.keys(Q)) {
  const out = `${DIR}/vlmw-${k}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${k}`); continue; }
  const img = fs.readFileSync(`${DIR}/${k}.png`).toString('base64');
  console.log(`\n======== ${k} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q[k] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 2000,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 500 ? txt.slice(0, 400) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(2500);
}
