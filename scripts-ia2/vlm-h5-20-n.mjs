// Z2-23 — hadith-5ep leçon 20 — adjudications VLM lettre-niveau SÉRIE N (n01-n10)
// Cibles : 9 conflits résiduels après lecture des séries r/w/c. Strict anti-hallucination.
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-20';

const COMMON = `Extrait 600 dpi agrandi d'un manuel scolaire marocain d'hadith (5e année primaire), leçon 20 « دَعْمٌ وَتَطْبِيقٌ » (pp.111-113), sens de lecture droite→gauche.
TRANSCRIS EXACTEMENT ce qui est imprimé, mot à mot, avec la vocalisation. Analyse LES LETTRES UNE À UNE pour les mots signalés : nomme chaque lettre de base (alif, bāʾ, tāʾ, thāʾ, ǧīm, ḥāʾ, khāʾ, dāl, dhāl, rāʾ, zāy, sīn, shīn, ṣād, ḍād, ṭāʾ, ẓāʾ, ʿayn, ġayn, fāʾ, qāf, kāf, lām, mīm, nūn, hāʾ, wāw, yāʾ) et les points (0/1/2/3) au-dessus/dessous, plus les diacritiques (fatha, kasra, ḍamma, sukūn, shadda, tanwīn). Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé. Illisible : [؟]. Réponds par la transcription uniquement.`;

const Q = {
  n01: `Tuile droite d'une ligne. Transcris tout. Le mot le plus à GAUCHE de la tuile est contesté : est-ce le début de الدَّالَّةِ (avec dāl : dos anguleux SANS point) ou de اللَّهُ (lām+lām) ? Décris ses lettres visibles une à une.`,
  n02: `Tuile gauche d'une ligne du 2e paragraphe. Transcris tout. Le mot de DROITE suit عَلَامَاتِ الْإِيمَانِ : est-ce الدَّالَّةِ (alif+lām+dāl+alif+lām+lām+shadda+tāʾ marbūṭa avec 2 points) ou اللَّهُ (alif+lām+lām+shadda+hāʾ ouverte SANS point) ? Analyse CE MOT lettre par lettre en entier, puis transcris عَلَى كَمَالِهِ et la suite.`,
  n03: `Ligne de l'introduction خديجة : «... لَمَّا أَرَادَتْ أَنْ [VERBE] عَنِ النَّبِيِّ...». Transcris tout. LETTRE PAR LETTRE le verbe entre أَنْ et عَنِ : combien de lettres ? تُخَفِّفَ (tāʾ+ḍamma, khāʾ+fatha, fāʾ+shadda, fāʾ+fatha — 4 lettres avec shadda) ou تَخْفَ (3 lettres) ou autre ? Décris chaque lettre, ses points et ses diacritiques.`,
  n04: `Extrait de la citation de خديجة. Transcris tout. LETTRE PAR LETTRE le verbe avant الْمَعْدُومَ : وَتَكْسِبُ (tāʾ+fatha, kāf, sīn, bāʾ) ou وَتُكْسِبُ (tāʾ+ḍamma, kāf, sīn, bāʾ) ? Quel diacritique exact porte le tāʾ initial ?`,
  n05: `Fin gauche d'une ligne du texte : après اعْتَبَرَ جَمِيعَ النَّاسِ vient le mot contesté. Transcris tout ce fragment. Est-ce إِخْوَةً (alif-hamza dessous, khāʾ, wāw, tāʾ marbūṭa+tanwīn) ou إِخْوَانًا (avec alif+nūn final) ou أَخُوَّةً (hamza au-dessus, double wāw avec shadda) ? Lettre par lettre.`,
  n06: `Début (droite) de la question 1 de la rubrique التطبيق. Transcris le numéro et les 4-5 premiers mots. LETTRE PAR LETTRE le premier mot après le numéro : حَثَّ (ḥāʾ+thāʾ 3 points au-dessus+shadda) ou حَدَّثَ (ḥāʾ+dāl SANS point+shadda+thāʾ) ou حَضَّ (ḥāʾ+ḍād 1 point) ? Combien de points sur la 2e lettre de base ?`,
  n07: `Fin gauche de la ligne de la question 1 du التحليل : «... أَذْكُرْ [NOMBRE] مِنْ...». LETTRE PAR LETTRE le nombre : ثَلَاثًا (thāʾ+lām+alif+thāʾ+alif+tanwīn, SANS tāʾ marbūṭa) ou ثَلَاثَةً (avec tāʾ marbūṭa + 2 points + tanwīn) ? Décris les dernières lettres du mot une à une.`,
  n08: `Milieu de la question 1 du التطبيق. Transcris tout. LETTRE PAR LETTRE : (1) le mot après كَيْفَ : أُقْنِعُ (alif-hamza+ḍamma, qāf 2 points+sukūn, nūn, ʿayn) ou autre forme ? (2) le mot après : الْمُحْسِنَ (avec fatha finale) ou الْمُحْسِنِ (kasra) ? Décris les diacritiques des dernières lettres.`,
  n09: `Fin de la question 1 du التطبيق : «...بَلْ وَلَا [VERBE] إِحْسَانَهُ إِلَيْهِمْ؟». LETTRE PAR LETTRE le verbe : يَقْطَعَ (yāʾ+fatha, qāf, ṭāʾ, ʿayn+fatha) ou يَقُطِّعَ (ḍamma sur qāf, shadda sur ṭāʾ) ou يَقْطَعُ (ḍamma finale) ? Décris chaque diacritique.`,
  n10: `Ligne de l'introduction خديجة : «... الَّتِي اشْتَهَرَ بِهَا [MOT] النُّبُوَّةِ دَلِيلًا...». Transcris tout. LETTRE PAR LETTRE le mot avant النُّبُوَّةِ : قَبْلَ (qāf 2 points au-dessus, bāʾ 1 point dessous, lām) ou فِيلَ (fāʾ 1 point, yāʾ 2 points dessous) ou autre ? Décris les 3 lettres et leurs points.`,
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
console.log('\nN-SÉRIE TERMINÉE');
