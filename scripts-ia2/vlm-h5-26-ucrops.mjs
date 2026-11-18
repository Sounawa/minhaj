// Z2-31 — VLM scrutins finaux, recadrages natifs 1200 dpi (leçon 26)
// Questions NEUTRES : jamais de listes de candidats (leçon Z2-30).
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-26/crops';
const COMMON = `Recadrage NATIF 1200 dpi (très net) d'une ou deux lignes d'un manuel scolaire marocain d'hadith (5e primaire), leçon 26 «الاستقامة», lecture droite→gauche. La ligne est ENTIÈRE (jamais coupée).
TRANSCRIS la ligne entière mot à mot avec la vocalisation. Puis pour les mots signalés : décompose lettre par lettre (forme de chaque lettre, NOMBRE DE POINTS et leur place, dents), et décris les VOYELLES imprimées (fatḥa/kasra/ḍamma/sukūn/shadda/tanwīn) lettre par lettre. Ne complète JAMAIS par mémoire d'un texte connu.`;

const Q = {
  'u01-p144': `Les 3 objectifs (أهداف). Transcris-les. SCRUTIN 1 : le verbe de l'objectif 1 (2e mot) — décris la voyelle de la hamza initiale et la shadda éventuelle. SCRUTIN 2 : le verbe de l'objectif 2 (2e mot) — décris la voyelle de la hamza initiale ET la voyelle de la lettre médiane (rāʾ). SCRUTIN 3 : le verbe de l'objectif 3 (2e mot) — décris la voyelle de la hamza initiale et la voyelle du rāʾ.`,
  'u02-p144': `Les 2 premières lignes du تمهيد. Transcris-les. SCRUTIN 1 : le mot après «فِي الدِّينِ» — décompose-le lettre par lettre avec ses voyelles ET décris s'il porte une shadda, et sur quelle lettre. SCRUTIN 2 : la ponctuation imprimée après «نَافِعَةٌ» (point, virgule, point-virgule ?).`,
  'u03-p144': `L'en-tête de l'encadré du hadith (le bandeau au-dessus du sanad) et le sanad complet. SCRUTIN 1 : transcris l'en-tête MOT À MOT et décompose-le lettre par lettre. SCRUTIN 2 : dans le sanad, décompose le mot entre «وَقِيلَ» et «سُفْيَانُ» lettre par lettre avec ses voyelles (hamza initiale et voyelles internes). SCRUTIN 3 : y a-t-il un ethnique (mot avec shadda sur la 2e lettre) entre «عَبْدِ اللهِ» et «رَضِيَ» ? Si oui, décompose-le lettre par lettre.`,
  'u04-p144': `Le matn de l'encadré et sa référence. Transcris tout mot à mot. SCRUTIN : entre «قَالَ» et «آمَنْتُ» y a-t-il un mot imperatif «قُلْ» ? Décompose la séquence entre ces deux mots lettre par lettre, avec la ponctuation (deux-points ? guillemets ?).`,
  'u05-p146': `La ligne «... أَعْمَلُ عَلَيْهِ وَ... بِهِ. فَأَجَابَهُ ...». Transcris-la. SCRUTIN : le verbe entre «عَلَيْهِ وَ» et «بِهِ» — décompose-le lettre par lettre : forme de chaque lettre, nombre de points (0/1/2/3, dessus/dessous), shadda éventuelle, voyelles.`,
  'u06-p146': `La ligne du جَوَامِع des débuts : «وَهَذَا مِنْ جَوَامِعِ الْكَلِمِ ...». Transcris-la. SCRUTIN : le mot relatif après «الْكَلِمِ» — décompose-le lettre par lettre (compte les points de la 4e lettre) et décris le mot suivant avec ses voyelles.`,
  'u08-p146': `La citation de ʿUmar : «قَالَ عُمَرُ بْنُ الْخَطَّابِ...». Transcris-la entière. SCRUTIN 1 : le verbe entre «وَلَمْ» et «رَوْغَانَ» — décompose-le lettre par lettre, en comptant les points de la lettre médiane (dessus ? dessous ? combien ?). SCRUTIN 2 : le DERNIER mot de la citation — décompose-le lettre par lettre en comptant les points de la 3e lettre (2 ou 3 ?).`,
  'u09-p147': `La ligne «... لِقَوْلِهِ ﷺ : «...» وَلِقَوْلِهِ عَزَّ وَجَلَّ ...». Transcris-la. SCRUTIN : le premier mot DANS les guillemets — y a-t-il un و (wāw) ou une autre lettre avant «آمَنْتُ» ? Décompose la séquence lettre par lettre.`,
  'u11-p147': `La citation d'al-Wāsiṭī (fin). Transcris la ligne. SCRUTIN : le verbe entre «وَبِفَقْدِهَا» et «الْمَحَاسِنُ» — décompose-le lettre par lettre : compte les points de la 3e lettre (0, 1, 2 ? dessus ou dessous ?) et donne les voyelles.`,
  'u12-p147': `La ligne d'en-tête «وَمِنْ فَضَائِلِ ...». Transcris-la. SCRUTIN : le DERNIER mot — décompose-le lettre par lettre : y a-t-il un alif entre le rāʾ et le tāʾ final ? Décris les deux dernières lettres avec leurs points.`,
  'u13-p147': `Le premier item en tiret des ثمرات. Transcris-le. SCRUTIN 1 : le mot après «وَالْمَوْتِ» — décompose-le lettre par lettre avec voyelles (2e lettre : points ? shadda ?). SCRUTIN 2 : le mot après «الْمُسْتَقِيمِينَ» — décris-le lettre par lettre (un seul mot ou deux ? hamza ?). SCRUTIN 3 : le premier mot du tiret — décris ses voyelles.`,
  'u14a-p148': `Première ligne de la citation coranique encadrée (avec l'introduction «يَقُولُ اللهُ تَعَالَى...» si visible). Transcris TOUT mot à mot avec la vocalisation, y compris les lettres ouvertes/muqattaʿāt et tout numéro de verset dans son médaillon.`,
  'u14b-p148': `Deuxième ligne de la citation coranique encadrée. Transcris TOUT mot à mot avec la vocalisation et les numéros de versets dans leurs médaillons.`,
  'u14c-p148': `Troisième ligne de la citation coranique encadrée. Transcris TOUT mot à mot avec la vocalisation et les numéros de versets dans leurs médaillons.`,
  'u14d-p148': `Quatrième ligne de la citation coranique + la référence entre crochets. Transcris TOUT mot à mot avec la vocalisation, les numéros dans leurs médaillons, et la référence finale (sourate + numéros, chiffre par chiffre).`,
  'u15-p148': `Le 3e item en tiret du يُسْتَفَاد («الِاسْتِقَامَةُ تَكُونُ كَمَا...»). Transcris-le. SCRUTIN 1 : le mot après «لَا كَمَا» — décris sa première lettre (points ?) et ses voyelles. SCRUTIN 2 : le mot suivant (حَسْبَ/حَسَبَ) — voyelle du sīn.`,
  'u16-p149': `La fin du hadith d'Anas dans l'encadré («... وَلَا يَدْخُلُ الْجَنَّةَ ...»). Transcris tout. SCRUTIN 1 : le mot «جَار...» — décris sa voyelle finale (ḍamma ou fatḥa sur le rāʾ) et le pronom qui suit. SCRUTIN 2 : le DERNIER mot — décompose-le lettre par lettre (nombre de lettres, points, alif médian ?). SCRUTIN 3 : la référence.`,
  'u17-p149': `L'activité 3 avec sa citation. Transcris tout. SCRUTIN : dans la citation entre guillemets, le mot «جَار...» (voyelle du rāʾ) et le dernier mot (décomposition lettre par lettre).`,
  'u18-p147': `La ligne «فِي الْحَدِيثِ بِـ«ثُمَّ» الَّتِي... التَّرْتِيبَ...». Transcris-la. SCRUTIN : le mot relatif après les guillemets fermants — compte les points de sa 4e lettre — et le verbe qui suit : décris sa 2e lettre (points) et sa 4e lettre.`,
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 2200,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 500 ? txt.slice(0, 400) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(2500);
}
