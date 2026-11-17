// Z2-26 — hadith-5ep leçon 22 — départages finaux T1-T8 (zooms ×5-×8)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-22';

const COMMON = `Zoom très agrandi (600 dpi ×5-×8) d'un manuel scolaire marocain d'hadith (5e année primaire), leçon 22, sens de lecture droite→gauche.
Analyse LES LETTRES UNE À UNE : nomme chaque lettre de base, les points (0/1/2/3) au-dessus/dessous, les diacritiques (fatha, kasra, ḍamma, sukūn, shadda, tanwīn). Ne complète JAMAIS par mémoire : seulement ce qui est imprimé. Illisible : [؟]. Réponds : TRANSCRIPTION puis RÉPONSES.`;

const R = {
  T1: `ZONE : fins des lignes 3-4 du paragraphe تمهيد (p.120) — deux mots à départager.
QUESTIONS : (1) Le mot « فِي ... » en fin de ligne 3 (avant la virgule) : est-ce « الإِيمَانِ » (alif-lām-alif+YĀʾ à 2 points DESSOUS puis MĪM 0 point puis alif-nūn) ou « الإِتْقَانِ » (alif-lām-alif+TĀʾ à 2 points DESSUS puis QĀF à 2 points DESSUS puis alif-nūn) ? Décris la 4e lettre (points au-dessus ou en dessous ? combien ?) et la 5e lettre (points ?). (2) Le mot final de la ligne 4 « فِي الْجَـ... » : LETTRE PAR LETTRE — « الْجِنَانِ » (jīm+kasra, nūn, alif, nūn — 4 lettres sans shadda) ou « الْجَنَّانِ » (jīm, nūn+SHADDA, alif, nūn) ? Y a-t-il une shadda sur le nūn ? Quelle voyelle sur le jīm (kasra ou fatha) ? (3) Transcris tout ce qui est visible.`,
  T2: `ZONE : début de ligne (p.122) — un mot à départager.
QUESTIONS : (1) Le premier mot complet (après « وَفِي ») : est-ce « الْحِوَارِ » (ḤĀʾ = 0 point, boucle ouverte) ou « الْجِوَارِ » (JĪM = 1 point DESSOUS) ou « الْجُوَارِ » ? Décris la lettre après l'alif-lām : sa forme, ses points (combien, où). (2) Le mot suivant : « وَالْجِدَالِ » — confirme la 3e lettre (ǧīm 1 point dessous ?). (3) Transcris tout ce qui est visible de la ligne.`,
  T3: `ZONE : référence entre crochets (p.122, fin de la citation « ...فَإِنَّهُ يَرَاكَ »).
QUESTIONS : (1) Transcris la référence complète entre crochets, lettre par lettre. (2) Le premier mot après le crochet : « صحيح » (ṣād-ḥāʾ-yāʾ-ḥāʾ, SANS alif final) ou « صحيحا » (AVEC un alif après le ḥāʾ final, ou tanwīn fatha) ? Décris ce qui suit la dernière consonne. (3) Les mots suivants : « البخاري ومسلم » ou autre ?`,
  T4: `ZONE : milieu de ligne dense (p.123) — « وَذَلِكَ بِأَنْ ... الذَّابِحُ ».
QUESTIONS : (1) Le verbe entre « بِأَنْ » et « الذَّابِحُ » : LETTRE PAR LETTRE — combien de lettres ? Est-ce « يُتْقِنَ » (YĀʾ+ḍamma, TĀʾ+sukūn 2 points dessus, QĀF+kasra 2 points dessus, NŪN+fatha) ou « يُقْنَ » (sans tāʾ) ou « يُنْقَنَ » (nūn au milieu) ? Décris CHAQUE lettre du mot, ses points et son diacritique. (2) Le mot suivant : « الذَّابِحُ » (avec shadda sur dhāl ?) ou « الدَّابِحُ » ? (3) Transcris tout ce qui est visible.`,
  T5: `ZONE : énumération des animaux nuisibles (p.123) — « كَالْأَفَاعِي وَالْعَقَارِبِ وَ... ».
QUESTIONS : (1) Après « وَالْعَقَارِبِ » : y a-t-il UN AUTRE MOT avant « الَّتِي/أَوِ الَّتِي » ? Si oui : LETTRE PAR LETTRE — est-ce « وَالْفَئْرَانِ » (fāʾ+alif+HAMZA-YĀʾ 2 points dessous+rāʾ+alif+nūn) ou « وَالْفَأْرَانِ » (fāʾ+alif+ALIF simple+rāʾ+alif+nūn) ? Décris la 3e lettre. (2) Le mot qui suit : « أَوِ الَّتِي » (wāw KASRA — « ou celle que... ») ou « وَالَّتِي » (wāw simple) ? Décris la voyelle sur le wāw. (3) Transcris tout ce qui est visible.`,
  T6: `ZONE : en-tête « وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ: » et le PREMIER item qui suit (p.123).
QUESTIONS : (1) Transcris l'en-tête complet. (2) Le premier item après l'en-tête : quel numéro est imprimé au début (1. ? 2. ? rien ?) — décris le chiffre. (3) Transcris le premier item INTÉGRALEMENT lettre par lettre (il commence peut-être par « إِحْسَانُ الْمُسْلِمِ فِي عَقِيدَتِهِ... »). (4) Le deuxième item : quel numéro porte-t-il et comment commence-t-il ?`,
  T7: `ZONE : les chiffres de la référence ﴿الرَّحْمَن: ...﴾ (p.123).
QUESTIONS : (1) Transcris la référence complète. (2) Décris CHAQUE chiffre imprimé après « الرَّحْمَن: » — le premier chiffre : forme de « ٦ » (comme un 7, crochet ouvert) ou « ٥ » (boucle fermée ronde comme un o) ou « ٩ » (boucle avec hampe descendante) ? le deuxième chiffre : « ٠ » (point/petit ovale) ou « ٩ » ou autre ? (3) Donc le nombre imprimé est ٦٠, ٥٩, ٩٠ ou autre ?`,
  T8: `ZONE : ligne d'instruction de la rubrique الْإِعْدَادُ الْقَبْلِيُّ (p.124).
QUESTIONS : (1) Transcris la ligne complète lettre par lettre. (2) Entre « حَدِيثَ الدَّرْسِ » et « أُجِيبُ » : y a-t-il le mot « الْآتِيَ » (alif-lām+alif+hamza+tāʾ+yāʾ) ? Décris ce qui sépare exactement « الدَّرْسِ » du verbe suivant. (3) Le verbe : « أُجِيبُ » (hamza avec ḌAMMA) ou « أَجِيبُ » (hamza avec FATHA) ? Décris la voyelle sur la hamza initiale. (4) Le premier mot : « أَحْفَظُ » (ḍamma sur ḍād) — confirme.`,
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
console.log('\nDÉPARTAGES TERMINÉS');
