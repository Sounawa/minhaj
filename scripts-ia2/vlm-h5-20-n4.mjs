import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-20';
const COMMON = `Extrait 600 dpi agrandi d'un manuel scolaire marocain d'hadith (5e année primaire), leçon 20 « دَعْمٌ وَتَطْبِيقٌ » (pp.111-113), sens de lecture droite→gauche.
TRANSCRIS EXACTEMENT ce qui est imprimé, mot à mot, avec la vocalisation. Analyse LES LETTRES UNE À UNE pour les mots signalés : nomme chaque lettre de base et les points (0/1/2/3) au-dessus/dessous, plus les diacritiques. Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé. Illisible : [؟]. Réponds par la transcription uniquement.`;
const Q = {
  n20: `Fin gauche d'une ligne de la question 1 du التحليل : la séquence imprimée est «أَذْكُرْ [NOMBRE] مِنْ». LETTRE PAR LETTRE le nombre : ثَلَاثًا (thāʾ+lām+alif+thāʾ+alif+tanwīn, SANS tāʾ marbūṭa) ou ثَلَاثَةً (avec tāʾ marbūṭa finale 2 points+tanwīn) ou autre ? Décris les 4-5 lettres du nombre une à une.`,
  n21: `Deux lignes de l'encadré خديجة (haut du cadre). Transcris TOUT ce qui est visible. LETTRE PAR LETTRE le verbe entre أَنْ et عَنِ : تُخَفِّفَ (tāʾ+ḍamma, khāʾ+fatha, fāʾ+shadda, fāʾ+fatha) ou تَخْفِفَ (tāʾ+fatha, khāʾ+sukūn, fāʾ+kasra, fāʾ+fatha) ou تَخْفَ (3 lettres) ou autre ? Décris chaque lettre de base, ses points et ses diacritiques.`,
};
const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of Object.keys(Q)) {
  const img = fs.readFileSync(`${DIR}/z20-${k}.png`).toString('base64');
  console.log(`\n======== ${k} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: COMMON + '\n\n' + Q[k] },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1024,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(`${DIR}/z20-${k}.txt`, txt);
      console.log(txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(3000);
}
