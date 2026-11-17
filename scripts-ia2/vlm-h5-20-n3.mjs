// Z2-23 — hadith-5ep leçon 20 — 3e vague adjudications VLM (n16-n19)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-20';

const COMMON = `Extrait 600 dpi agrandi d'un manuel scolaire marocain d'hadith (5e année primaire), leçon 20 « دَعْمٌ وَتَطْبِيقٌ » (pp.111-113), sens de lecture droite→gauche.
TRANSCRIS EXACTEMENT ce qui est imprimé, mot à mot, avec la vocalisation. Analyse LES LETTRES UNE À UNE pour les mots signalés : nomme chaque lettre de base et les points (0/1/2/3) au-dessus/dessous, plus les diacritiques (fatha, kasra, ḍamma, sukūn, shadda, tanwīn). Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé. Illisible : [؟]. Réponds par la transcription uniquement.`;

const Q = {
  n16: `Ligne de la citation de خديجة (sous la ligne إِنَّكَ لَتَصِلُ الرَّحِمَ وَتَحْمِلُ الْكَلَّ وَتُكْسِبُ). Transcris tout ce qui est visible. LETTRE PAR LETTRE le mot avant الضَّيْفَ : وَتُقْرِي (tāʾ+ḍamma, qāf+sukūn, rāʾ+KASRA, yāʾ 2 points dessous) ou وَتُقْرَى (rāʾ+FATHA, alif maqṣūra sans points) ? Décris les 2 dernières lettres du mot avec leurs points et diacritiques.`,
  n17: `Ligne de l'encadré خديجة : «...الَّتِي اشْتَهَرَ بِهَا [MOT] النُّبُوَّةِ...». Transcris tout. LETTRE PAR LETTRE le mot entre بِهَا et النُّبُوَّةِ : قَبْلَ (qāf 2 points AU-DESSUS, bāʾ 1 point DESSOUS, lām) ou فِيلَ (fāʾ 1 point au-dessus, yāʾ 2 points dessous) ou autre ? Décris chaque lettre : combien de points, au-dessus ou en dessous ?`,
  n18: `Début (droite) d'une ligne de la question 1 du التحليل : «أَذْكُرْ [NOMBRE] مِنْ أَنْوَاعِ...». LETTRE PAR LETTRE le nombre entre أَذْكُرْ et مِنْ : ثَلَاثًا (thāʾ+lām+alif+thāʾ+alif+tanwīn, SANS tāʾ marbūṭa) ou ثَلَاثَةً (avec tāʾ marbūṭa finale, 2 points au-dessus, tanwīn) ? Décris les lettres une à une avec points et diacritiques.`,
  n19: `Début (droite) de la 2e ligne de l'encadré خديجة. La ligne précédente se termine par أَنْ. Cette ligne commence par le verbe contesté, puis عَنِ النَّبِيِّ. Transcris les 4-6 premiers mots. LETTRE PAR LETTRE le premier mot : تُخَفِّفَ (tāʾ+ḍamma, khāʾ+fatha, fāʾ+shadda, fāʾ+fatha — 4 lettres de base) ou تَخْفَ (tāʾ+fatha, khāʾ+sukūn, fāʾ+fatha — 3 lettres) ou تَخِفَّ ou autre ? Décris chaque lettre de base, ses points et ses diacritiques.`,
};

const zai = await ZAI.create();
const keys = Object.keys(Q);
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of keys) {
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
        model: 'glm-5v-turbo',
        temperature: 0.1,
        max_tokens: 1024,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(`${DIR}/z20-${k}.txt`, txt);
      console.log(txt);
      done = true;
    } catch (e) {
      console.log(`tentative ${attempt} ${k} échec: ${e.message}`);
      await sleep(8000 * attempt);
    }
  }
  if (!done) console.log(`ABANDON ${k}`);
  await sleep(3000);
}
console.log('\n3e VAGUE TERMINÉE');
