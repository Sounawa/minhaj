// Z2-32 — VLM 4 derniers scrutins (leçon 27)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-27/crops';
const COMMON = `Recadrage ultra-net (1200 dpi ×N) d'un manuel scolaire marocain d'hadith (5e primaire), leçon 27, lecture droite→gauche.
TRANSCRIS les mots imprimés, puis réponds au scrutin lettre par lettre : forme, NOMBRE DE POINTS et leur place, voyelles. Ne complète JAMAIS par mémoire.`;

const Q = {
  'w1-p154': `Un segment de l'item : «الِاسْتِقَادَةُ(؟) مِنَ التَّطَوُّعَاتِ تَ...ِيمٌ لِلْفَرَائِضِ...». SCRUTIN : le mot entre «التَّطَوُّعَاتِ» et «لِلْفَرَائِضِ» — décompose sa 2e lettre APRÈS le ت initial : combien de points AU-DESSUS (1 = ن, 2 = ت, 3 = ث) ? Puis donne tout le mot lettre par lettre.`,
  'w2-p153': `Un segment : «...فِي اغْتِنَامِ ثَوَابِهَا وَتَ...ِيمِ الْفَرَائِضِ بِهَا تَحْقِيقًا...». SCRUTIN : le mot entre «وَ» et «الْفَرَائِضِ» — sa 2e lettre : combien de points au-dessus (1 = ن, 2 = ت, 3 = ث) ? Donne tout le mot lettre par lettre.`,
  'w3-p155': `La fin de l'encadré : «...وَأَمَّا اخْتِلَافُ مَرَاتِبِهَا فَبِحَسَبِ الْعَمَلِ، لَكِنْ لَا بُدَّ ...». SCRUTIN : transcris TOUT ce qui suit «لَا بُدَّ» jusqu'à la fin de la phrase, mot à mot avec les vocalisations (il peut y avoir 2-4 mots). Décompose le verbe éventuel lettre par lettre.`,
  'w4-p150': `L'en-tête du bandeau de l'encadré du hadith (mot unique centré, calligraphié). SCRUTIN : décompose-le ENTIEREMENT lettre par lettre — première lettre : alif+hamza ou alif+lām ? combien de lettres au total ? y a-t-il un د ? un ث final (3 points) ? Donne le mot.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of Object.keys(Q)) {
  const out = `${DIR}/vlm-${k}.txt`;
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1800,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 700 ? txt.slice(0, 550) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(2500);
}
