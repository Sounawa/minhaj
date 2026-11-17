// Z2-24 — hadith-5ep leçon 21 — lectures VLM m-série (recadrages ligne-étroits, adjudication)
// Usage: node vlm-h5-21-m.mjs m03 m04 m05 ...   (tags séparés par espaces)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-21';

const COMMON = `Recadrage fin (600 dpi agrandi) d'un manuel scolaire marocain d'hadith (5e année primaire), leçon 21 «النهي عن الغضب» (pp.114-119), sens de lecture droite→gauche. Une ou deux lignes imprimées seulement.
TRANSCRIS EXACTEMENT ce qui est imprimé, mot à mot, avec TOUTE la vocalisation. Pour les mots signalés, analyse LES LETTRES UNE À UNE : nomme chaque lettre de base, les points (0/1/2/3) au-dessus/dessous, et les diacritiques (fatha, kasra, ḍamma, sukūn, shadda, tanwīn). Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé. Illisible : [؟]. Réponds en deux parties : TRANSCRIPTION (droite→gauche) puis RÉPONSES aux questions.`;

const M = {
  m01: `ZONE : haut DROIT du cadre vert du hadith (p.114) — texte blanc sur fond vert.
TRANSCRIS tout ce qui est imprimé dans cette zone (en-tête éventuel «النص», début du sanad).
QUESTIONS : (1) l'en-tête au-dessus du cadre : quel mot exact ? (2) le sanad : transcris-le mot à mot — «عَنْ أَبِي هُرَيْرَةَ رَضِيَ اللهُ عَنْهُ...» puis quoi exactement ? LETTRE PAR LETTRE le mot après عَنْهُ : «أَنَّ رَجُلًا» (alif+nūn+shadda, puis rāʾ+ǧīm+lām+tanwīn) ou «أَنَّ رَسُولَ» ou «قَالَ» ou autre ? (3) la fin de la ligne (bord gauche de la zone).`,
  m02: `ZONE : haut GAUCHE du cadre vert du hadith (p.114) — texte blanc sur fond vert.
TRANSCRIS tout.
QUESTIONS : (1) la fin de la ligne du sanad : après «قَالَ لِلنَّبِيِّ ﷺ» (si visible) vient quoi ? (2) LETTRE PAR LETTRE le premier mot de la ligne suivante si visible. (3) toute autre inscription (décor, numéro).`,
  m03: `ZONE : bas DROIT du cadre vert du hadith (p.114) — LE MATN, texte blanc sur fond vert.
TRANSCRIS tout le matn mot à mot.
QUESTIONS : (1) LETTRE PAR LETTRE le premier mot : «أَوْصِنِي» (alif+wāw+ṣād+kasra+nūn+yāʾ) ? (2) ensuite quoi : «فَقَالَ:» ou «قَالَ:» ? LETTRE PAR LETTRE. (3) combien de fois «لَا تَغْضَبْ» est-il imprimé dans ce cadre ? Y a-t-il entre deux occurrences un mot comme «فَرَدَّدَ مِرَارًا» ou «فَرَدَّدْتُ مِرَارًا» ? DÉCRIS chaque ligne du cadre une par une. (4) la référence entre crochets : laquelle ?`,
  m04: `ZONE : bas GAUCHE du cadre vert du hadith (p.114) — fin du matn + référence, blanc sur vert.
TRANSCRIS tout.
QUESTIONS : (1) la dernière ligne du cadre : mot à mot. (2) la référence exacte entre crochets : «[صحيح البخاري]» ou autre ? (3) s'il y a «فَرَدَّدَ مِرَارًا» ou similaire, LETTRE PAR LETTRE : shadda sur le dāl ? un tāʾ final avant le م ?`,
  m05: `ZONE : DROITE de la 3e ligne du تمهيد (p.114) — phrase difficile.
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE le début (droite) : «وَالشَّرَّ بِمِثْلِهِ.» ou «بِمِثْلِهَا» (tāʾ marbūṭa) ? (2) LETTRE PAR LETTRE ce qui suit le point : «وَدِفَاعًا لِذَلِكَ» (wāw+dāl+kasra+fatha+ʿayn+tanwīn fatha... ou «وَدَفْعًا») ? (3) ensuite : «وَضَعَ الشَّرْعُ» ou «جَعَلَ الشَّرْعُ» ou «شَرَعَ» ? LETTRE PAR LETTRE le verbe et son sujet. (4) la suite jusqu'au bord gauche de la zone.`,
  m06: `ZONE : GAUCHE de la 3e ligne du تمهيد (p.114) — fin de la phrase difficile.
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE le verbe après «مِنَ الْغَضَبِ» : «يَدْفَعُ بِهِ» ? (2) LETTRE PAR LETTRE le mot entre «بِهِ» et «فِي» : «آثَارَ الْوَجِيعَةِ» ou «آثَارَ الْغَضْبَةِ» ou «انْتِظَارَ الْوَخِيمَةِ» ou autre — décris chaque lettre du 2e mot (alif? wāw? ǧīm? ḥāʾ? ḍād? yāʾ?). (3) le dernier mot avant «الْفَرْدِ» sur la ligne suivante si visible : «نَفْسِيَّةِ» ?`,
  m07: `ZONE : ligne des questions (p.114) — moitié gauche.
TRANSCRIS la ligne entière visible.
QUESTIONS : (1) LETTRE PAR LETTRE le mot entre «أَثَرُ» et «النَّفْسِ» : «تَمَلُّكِ» (tāʾ+fatha, mīm+fatha, lām+SHADDA+kasra, kāf+kasra — 4 lettres de base, AUCUN alif) ou «تَمَالُكِ» (avec alif après mīm) ou «مَلْكِ» ou «تَمَالَكِ» ? Décris chaque lettre ET chaque diacritique. (2) «عِنْدَ الْغَضَبِ» — confirme. (3) le début de la ligne à droite si visible.`,
  m08: `ZONE : الشَّرْح item 1 (p.115) — le mot et le début de sa définition.
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE le mot expliqué : «أَوْصِنِي» ? (2) LETTRE PAR LETTRE les 3-4 premiers mots de la définition (elle peut commencer par «أَمَرَنِي» ou «أَوْصَانِي» ou similaire) — chaque lettre et diacritique. (3) la fin de la définition si visible.`,
  m09: `ZONE : الشَّرْح item 2 (p.115) — «فَرَدَّدَ مِرَارًا...».
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE le mot en tête : «فَرَدَّدَ» (fāʾ+rāʾ+dāl+SHADDA+dāl+fatha, SANS tāʾ final) ou «فَرَّدَّدْتُ» (avec tāʾ+sukūn... ) ou «فَرَدَدَ» (sans shadda) ? (2) «مِرَارًا» (avec alif après rāʾ) ou «مَرَّةً» ? (3) LETTRE PAR LETTRE le verbe de la définition : «كَرَّرَ» (kāf+shadda+rāʾ+fatha, 3e personne) ou «كَرَّرْتُ» (1re personne) ? (4) la fin : «عَدَّةَ مَرَّاتٍ» ou «عِدَّةَ مَرَّاتٍ» ?`,
  m10: `ZONE : الشَّرْح item 3 (p.115) — «لَا تَغْضَبْ : ...».
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE le mot expliqué : «لَا تَغْضَبْ» ? (2) LETTRE PAR LETTRE les premiers mots de la définition (peut être «لَا تُنَفِّذْ غَضَبَكَ...» ou «لَا تُمْضِ غَضَبَكَ...» ou autre) — chaque lettre. (3) la fin de la définition : «ضِدَّ مَنْ أَغْضَبَكَ» ou «فِي مَنْ أَغْضَبَكَ» ou autre ?`,
  m11: `ZONE : استخلاص المضامين questions 1 et 2 (p.115).
TRANSCRIS les deux questions complètes.
QUESTIONS : (1) Q1 : LETTRE PAR LETTRE le verbe d'ouverture : «أُحَدِّدُ» ? puis LETTRE PAR LETTRE ce qui suit «سَبَبَ» : «تَكْرَارِ قَوْلِهِ» ou «حِرْصِهِ عَلَى...» ou directement «قَوْلِهِ» ? (2) Q2 : LETTRE PAR LETTRE le verbe d'ouverture : «أَسْتَنْتِجُ» (alif+fatha, sīn, tāʾ, nūn, tāʾ, ǧīm+ḍamma) ou «أَسْتَوْجِهُ» ou «أَسْتَخْرِجُ» ou autre ? puis LETTRE PAR LETTRE : «سَبَبَ حَصْرِ الْجَوَابِ» (ḥāʾ+ṣād+rāʾ) ou «حَضْرِ» (ḍād) ? puis «فِي كَلِمَةٍ» ou «فِي كَلِمَةٍ وَاحِدَةٍ» ? (3) la fin exacte des deux questions.`,
  m12: `ZONE : DROITE de la ligne dense «فَفِيهَا...» (haut p.116).
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE le mot après «النَّهْيُ عَنْ» : «تَثْبِيطِ» (thāʾ 3 points+bāʾ+yāʾ+ṭāʾ) ou «تَحْرِيكِ» (ḥāʾ+rāʾ+kāf) ou «تَسْخِينِ» ou autre ? chaque lettre. (2) LETTRE PAR LETTRE après «بِضَبْطِ» : «اللِّسَانِ وَالْعَيْنِ» ou «الثَّغْرِ وَالْعَيْنِ» ou autre ? (3) la suite jusqu'au bord gauche de la zone.`,
  m13: `ZONE : GAUCHE de la ligne dense «فَفِيهَا...» (haut p.116).
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE ce qui suit «الْعَيْنِ» (ou équivalent) : le mot «الَّذِي هُوَ مِنْ أَفْعَالِ الْمُحْسِنِينَ» ? (2) LETTRE PAR LETTRE la suite : «الَّذِينَ مَلَكُوا...» — puis quoi exactement (2-3 mots) ? (3) la fin de la ligne.`,
  m14: `ZONE : ligne suivante (p.116, ~2e ligne) — la suite «وَعَلَى...».
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE le début : «وَعَلَى سَبِيلِهِمْ» ou «وَأَجْرُوا» ou autre ? (2) la fin de la phrase et le mot final.`,
  m15: `ZONE : ligne «مَعْنَى قَوْلِهِ ﷺ لَا تَغْضَبْ...» (p.116).
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE le verbe après «أَيْ:» : «تَسْتَحِبَّ» (tāʾ+sīn+tāʾ+ḥāʾ+bāʾ 2 shadda?) ou «تُثِرْ» ou «تُحَرِّكْ» ? chaque lettre + diacritiques. (2) «دَاعِيَ الْغَضَبِ» ou «دَاعِيَةَ الْغَضَبِ» (tāʾ marbūṭa) ? (3) la fin de ligne : «فِي نَفْسِكَ» ?`,
  m16: `ZONE : hadith de عَطِيَّةَ السَّعْدِيِّ — 2e moitié (p.116).
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE ce qui suit «وَإِنَّمَا» : «تُطْفَأُ النَّارُ بِالْمَاءِ» ou «الْمَاءُ يُطْفِئُ النَّارَ» ou autre ? (2) LETTRE PAR LETTRE le mot final du hadith après «فَإِذَا غَضِبَ أَحَدُكُمْ» : «فَلْيَتَوَضَّأْ» (wāw+ḍād+dāl+shadda) ou «فَلْيَغْتَسِلْ» (ġayn+tāʾ+sīn+lām) ou autre ? Décris chaque lettre. (3) le mot entre l'intro «عَنْ عَطِيَّةَ السَّعْدِيِّ رَضِيَ اللهُ عَنْهُ» et le début du matn (peut-être «عَنِ النَّبِيِّ ﷺ قَالَ:» ou «قَالَ رَسُولُ اللهِ ﷺ:»).`,
  m17: `ZONE : «وَلِهَذَا يَخْرُجُ الْإِنْسَانُ...» + verbes consécutifs (p.116).
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE «مِنِ اعْتِدَالِ حَالِهِ» ou «مِنْ اعْتِدَالِ حَالِهِ». (2) les trois verbes : «فَيَقُولُ [X] وَيَرْتَكِبُ [Y] وَيَنْتَهِكُ [Z]» — LETTRE PAR LETTRE [X], [Y], [Z] (candidats : الْبَاطِلَ / الْمَآثِمَ / الْحُدُودَ). (3) LETTRE PAR LETTRE le mot entre «الْحُدُودَ وَ» et «وَغَيْرَ» : «الْحُرُمَاتِ» ou «الْأَعْرَاضَ» ou «الْبَيْضَاءَ» ou autre ? (4) «وَغَيْرَ ذَلِكَ مِنَ الْمُحَرَّمَاتِ» — confirme.`,
  m18: `ZONE : «فَالشَّيْطَانُ هُوَ الَّذِي زَيَّنَ...» + الِاسْتِعَاذَة (p.116, bas).
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE le verbe : «زَيَّنَ» (zāy+yāʾ+shadda+nūn) ? puis «لَهُ» ? puis le mot suivant jusqu'à «الْغَضَبِ». (2) «وَيَدْفَعُ» — transcris son complément. (3) LETTRE PAR LETTRE la fin : «مِنْ أَقْوَى الْحِيَلِ» ou «الْحِيَلَةِ» (tāʾ marbūṭa) ? puis «دَفْعُ كَيْدِهِ» ou «لِدَفْعِ كَيْدِهِ» ou «فِي دَفْعِ كَيْدِهِ» ?`,
  m19: `ZONE : titre ثَانِيًا + phrase d'intro des الثَّمَرَات (p.117, haut).
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE le titre : «ثَانِيًا: فَضْلُ مَلْكِ النَّفْسِ عِنْدَ الْغَضَبِ» — «مَلْكِ» SANS alif ou «مَالِكِ» ? (2) LETTRE PAR LETTRE l'intro : «لَا يَخْفَى أَنَّ فِي [X] عِنْدَ الْغَضَبِ [Y]» — [X] = «عَزْمِ الْإِنَاةِ وَالتَّجَلُّدِ» ou «تَمَلُّكِ النَّفْسِ» ou autre ? [Y] = «جِمَاعَ الْخَيْرِ وَالْفَضْلِ وَزَكَاةَ الثَّمَرَاتِ» ou «جَمِيعَ الْخَيْرِ...» ou autre ? chaque mot lettre par lettre. (3) l'en-tête de liste : «الثَّمَرَاتُ مِنْ ذَلِكَ:» ?`,
  m20: `ZONE : الثمرة 4 (p.117) — contenu inconnu, référence [للطبراني] probable.
TRANSCRIS tout INTÉGRALEMENT, chaque mot.
QUESTIONS : (1) LETTRE PAR LETTRE le début après «4.» : chaque mot (candidats possibles : «مَلْءُ...», «نَيْلُ...», «إِرَاثَةُ...» — je ne devine pas : décris). (2) la fin de l'item avant la référence. (3) la référence exacte : «[للطبراني]» ou «[رواه الطبراني]» ou autre ?`,
  m21: `ZONE : rubrique وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ (p.118) — header + item 1.
TRANSCRIS tout.
QUESTIONS : (1) le titre de rubrique exact (avec ou sans «وَ» initial, avec ou sans «مِنَ الْحَدِيثِ»). (2) item 1 : transcris-le INTÉGRALEMENT lettre par lettre — chaque mot (il concerne le compagnon qui a demandé la وَصِيَّة). (3) s'il y a «حَيْثُ نَاصَحَهُ» ou «حَيْثُ لَجَأَ», LETTRE PAR LETTRE ce qui suit jusqu'au «؛».`,
  m22: `ZONE : التَّقْوِيم question 1 (p.118).
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE le début de Q1 : «1. أُحَدِّدُ الْمُرَادَ» ou «1. مَا الْمُرَادُ» ou «1. أُبَيِّنُ الْمُرَادَ» ou autre ? (2) la suite : «بِقَوْلِهِ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ لَا تَغْضَبْ» — confirme mot à mot. (3) le début de Q2 si visible.`,
  m23: `ZONE : التَّقْوِيم question 3 (p.118, dernière).
TRANSCRIS tout INTÉGRALEMENT.
QUESTIONS : (1) LETTRE PAR LETTRE le début : «3. أَذْكُرُ...» ou «3. أُحَدِّدُ...» ou «وَأُذَكِّرُ...» ou autre ? (2) chaque mot de la question (candidats de sens : آثَارَ كَظْمِ الْغَيْظِ / الْوَسَائِلَ الشَّرْعِيَّةَ — je ne devine pas). (3) la ponctuation finale.`,
  m24: `ZONE : hadith 1 de الِاسْتِثْمَارُ (p.119) — sanad + début.
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE «عَنْ سُلَيْمَانَ بْنِ صُرْدٍ» (ṣād+rāʾ+dāl+tanwīn) puis la suite du sanad. (2) «كُنْتُ جَالِسًا عِنْدَ النَّبِيِّ ﷺ» ou «مَعَ النَّبِيِّ ﷺ» ? (3) LETTRE PAR LETTRE «وَرَجُلَانِ يَسْتَبَّانِ» (bāʾ+shadda) ? puis ce qui suit jusqu'à «قَالَ ﷺ» ou équivalent : chaque mot (peut contenir «فَاحْمَرَّ وَجْهُ أَحَدِهِمَا» ou similaire). (4) «إِنِّي لَأَعْلَمُ كَلِمَةً لَوْ قَالَهَا ذَهَبَ عَنْهُ مَا يَجِدُ» — confirme, puis la formule finale «أَعُوذُ بِاللهِ مِنَ الشَّيْطَانِ» — y a-t-il «الرَّجِيمِ» ?`,
  m25: `ZONE : question de synthèse après les deux hadiths (p.119).
TRANSCRIS tout.
QUESTIONS : (1) LETTRE PAR LETTRE le verbe d'ouverture : «أَسْتَخْرِجُ» ou «أَسْتَنْتِجُ» ou autre ? (2) «مِنَ الْحَدِيثَيْنِ» puis quoi : «أَهَمَّ الْوَسَائِلِ» ou «أَنَّهُمَا الْوَسِيلَتَانِ» ? LETTRE PAR LETTRE. (3) après «إِلَى» : «دَفْعِ الْغَضَبِ» ou «تَخْفِيفِ الْغَضَبِ» ? (4) la fin «عَنِ الْإِنْسَانِ.» — confirme.`,
  m26: `ZONE : الْإِعْدَادُ الْقَبْلِيُّ (p.119, bas).
TRANSCRIS tout.
QUESTIONS : (1) le titre : «الْإِعْدَادُ الْقَبْلِيُّ» (SINGULIER) — confirme lettre par lettre. (2) «أَحْفَظُ حَدِيثَ الدَّرْسِ [X]، ثُمَّ [Y]:» — LETTRE PAR LETTRE [X] : «الْمُقْبِلِ» ou «الْآتِيَ» ? et [Y] : «أُجِيبُ» ou «أُلَازِمُ» ou autre ? (3) item 1 : transcris-le lettre par lettre (peut être «أَعْرِفُ الْإِحْسَانَ...» — ne devine pas). (4) item 2 : transcris-le intégralement.`,
};

const tags = process.argv.slice(2);
if (!tags.length) { console.log('usage: node vlm-h5-21-m.mjs m03 m04 ...'); process.exit(1); }
const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of tags) {
  if (!M[k]) { console.log(`inconnu: ${k}`); continue; }
  const out = `${DIR}/z21-${k}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${k}`); continue; }
  const img = fs.readFileSync(`${DIR}/z21-${k}.png`).toString('base64');
  console.log(`\n======== ${k} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 3 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: COMMON + '\n\n' + M[k] },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1200,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 500 ? txt.slice(0, 350) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(15000 * attempt); }
  }
  if (!done) console.log(`ABANDON ${k}`);
  await sleep(25000); // cadence prudente anti-429
}
console.log('\nVAGUE M TERMINÉE');
