// Z2-26 — hadith-5ep leçon 22 — rattrapage T3b/T4b/T5b/T7b + T8
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-22';

const COMMON = `Zoom très agrandi d'un manuel scolaire marocain d'hadith (5e année primaire), leçon 22, sens de lecture droite→gauche.
Analyse LES LETTRES UNE À UNE : nomme chaque lettre de base, les points (0/1/2/3) au-dessus/dessous, les diacritiques. Ne complète JAMAIS par mémoire : seulement ce qui est imprimé. Illisible : [؟]. Réponds : TRANSCRIPTION puis RÉPONSES.`;

const R = {
  T3b: `ZONE : fin d'une ligne (p.122) avec une référence entre crochets après un guillemet fermant ».
QUESTIONS : (1) Transcris la référence complète entre crochets, lettre par lettre. (2) Le premier mot : « صحيح » ou « صحيحا » (avec alif ou tanwīn après le ḥāʾ final) ? Décris la fin du mot. (3) Les mots suivants.`,
  T4b: `ZONE : une ligne dense (p.123) qui contient la séquence « وَذَلِكَ بِأَنْ ... الذَّابِحُ ذَلِكَ ».
QUESTIONS : (1) Transcris la ligne complète mot à mot. (2) Le verbe entre « بِأَنْ » et « الذَّابِحُ » : LETTRE PAR LETTRE avec le nombre exact de lettres — « يُتْقِنَ » (yāʾ, tāʾ 2 points DESSUS+sukūn, qāf 2 points DESSUS+kasra, nūn+fatha — 4 lettres) ou « يُنْقَنَ » (avec nūn au milieu, 1 point dessus) ou « يُقْنَ » (3 lettres) ? Décris la 2e lettre : combien de points et où ? (3) Le mot après le verbe : « الذَّابِحُ » — confirme le point du dhāl.`,
  T5b: `ZONE : une ligne (p.123) contenant « كَالْأَفَاعِي وَالْعَقَارِبِ ... الَّتِي نَزَلَ بِهَا بَعْضُ الْأَمْرَاضِ ... ».
QUESTIONS : (1) Transcris la ligne complète. (2) Entre « وَالْعَقَارِبِ » et « الَّتِي » : y a-t-il un autre mot ? Si oui LETTRE PAR LETTRE : « وَالْفَأْرَانِ » (fāʾ, alif, ALIF-hamza, rāʾ, alif, nūn) ou « وَالْفَئْرَانِ » (avec yāʾ-hamza 2 points dessous) ? Décris la 3e lettre du mot. (3) Le mot avant « الَّتِي » : « أَوِ » (wāw avec KASRA dessous) ou « وَ » (wāw avec fatha) ? Décris la voyelle du wāw.`,
  T7b: `ZONE : fin de ligne (p.123) avec ﴿الرَّحْمَن: ...﴾ — les chiffres du numéro de verset.
QUESTIONS : (1) Transcris ce qui est visible (le mot الرَّحْمَن si visible, les deux-points, les chiffres). (2) Décris CHAQUE chiffre : le premier — forme de ٥ (boucle fermée ronde), ٦ (crochet ouvert type « 7 ») ou ٩ (boucle avec hampe) ? le second — ٠ (petit ovale/point), ٩, ٥ ou autre ? (3) Le nombre imprimé : ٦٠, ٥٩, ٩٥ ou autre ?`,
  T8: `ZONE : ligne d'instruction de la rubrique الْإِعْدَادُ الْقَبْلِيُّ (p.124).
QUESTIONS : (1) Transcris la ligne complète lettre par lettre. (2) Entre « حَدِيثَ الدَّرْسِ » et « أُجِيبُ » : y a-t-il le mot « الْآتِيَ » ? Décris ce qui sépare exactement « الدَّرْسِ » du verbe suivant. (3) Le verbe : « أُجِيبُ » (hamza avec ḍamma) ou « أَجِيبُ » (fatha) ? (4) Le premier mot : « أَحْفَظُ » — confirme la voyelle du ḍād.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of Object.keys(R)) {
  const out = `${DIR}/z22-${k}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${k}`); continue; }
  const img = fs.readFileSync(`${DIR}/z22-${k}.png`).toString('base64');
  console.log(`\n======== ${k} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + R[k] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo',
        temperature: 0.1,
        max_tokens: 1400,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
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
console.log('\nRATTRAPAGE TERMINÉ');
