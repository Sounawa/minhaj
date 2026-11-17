// Z2-26 — hadith-5ep leçon 22 — adjudication VLM bandes (15 zones ouvertes)
// Usage: node vlm-h5-22-b.mjs [start] [end]   (numéros de bandes 1..15)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-22';

const COMMON = `Extrait 600 dpi d'un manuel scolaire marocain d'hadith (5e année primaire), leçon 22 «الإحسان في كل شيء» (pp.120-124), sens de lecture droite→gauche.
TRANSCRIS EXACTEMENT ce qui est imprimé, mot à mot, avec la vocalisation. Pour les mots signalés, analyse LES LETTRES UNE À UNE : nomme chaque lettre de base (alif, bāʾ, tāʾ, thāʾ, ǧīm, ḥāʾ, khāʾ, dāl, dhāl, rāʾ, zāy, sīn, shīn, ṣād, ḍād, ṭāʾ, ẓāʾ, ʿayn, ġayn, fāʾ, qāf, kāf, lām, mīm, nūn, hāʾ, wāw, yāʾ), les points (0/1/2/3) au-dessus/dessous, et les diacritiques (fatha, kasra, ḍamma, sukūn, shadda, tanwīn). Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé. Illisible : [؟]. Réponds en deux parties : TRANSCRIPTION (lignes dans l'ordre, droite→gauche) puis RÉPONSES aux questions.`;

const R = {
  1: `ZONE : les 3 objectifs de أهداف الدرس (p.120).
TRANSCRIS les 3 objectifs complets avec la vocalisation.
QUESTIONS : (1) objectif 1 : LETTRE PAR LETTRE le verbe après « أَنْ » — « أَعْرِفَ » (alif+ʿayn+rāʾ+fāʾ, 4 lettres) ou « أَتَعَرَّفَ » (avec tāʾ après alif et shadda sur ʿayn+rāʾ) ? Décris chaque lettre du verbe. (2) objectif 2 : transcris-le — le verbe est « أُدْرِكَ » ou « أَذْكُرُ » ? et le mot après le verbe : « فَضْلَ الإِحْسَانِ » ou « فَضْلَ الإِنْسَانِ » ? LETTRE PAR LETTRE ce mot (ḥāʾ 1 point ou nūn 1 point). (3) objectif 3 : transcris-le intégralement — LETTRE PAR LETTRE le mot après « مَقَاصِدَ » : « الأَمْرِ » (alif+lām+alif+mīm+rāʾ) ou « الأَمِيرِ » (avec yāʾ avant le rāʾ final) ? et le premier verbe : « أَتَمَثَّلَ » ?`,
  2: `ZONE : le paragraphe تمهيد (p.120), 4 lignes.
TRANSCRIS tout le paragraphe mot à mot.
QUESTIONS : (1) après « مِنْ إِنْسَانٍ وَحَيَوَانٍ وَغَيْرِهِمَا » : LETTRE PAR LETTRE le verbe — « فَشَرَعَ » (fāʾ+shīn+rāʾ+ʿayn, 4 lettres) ou « فَشُرِّعَ » (shadda sur rāʾ) ? (2) la phrase « وَجَعَلَهُ مِنْ أَعْلَى الدَّرَجَاتِ فِي ... » : LETTRE PAR LETTRE le dernier mot avant la virgule — « الإِيمَانِ » (alif+lām+alif+yāʾ+mīm+alif+nūn) ou « الإِتْقَانِ » (alif+lām+alif+tāʾ+qāf+alif+nūn) ? Décris la 4e lettre : yāʾ (2 points dessous) ou tāʾ (2 points dessus) ? et la 5e : mīm (0 point) ou qāf (2 points dessus) ? (3) la fin : « وَرَتَّبَ عَلَيْهِ عَظِيمَ الأَجْرِ فِي ... » : LETTRE PAR LETTRE le mot final — « الْجِنَانِ » (jīm 1 point dessous) ou « الْجَنَّانِ » (shadda) ? (4) la 2e ligne : « فَشَرَعَ الإِحْسَانَ فِي كُلِّ شَيْءٍ وَإِلَى كُلِّ شَيْءٍ » — confirme ce qui suit « وَأَمَرَ بِهِ مَعَ » : « الْقَرِيبِ وَالْبَعِيدِ » puis « وَمَعَ الْحَيَوَانِ » ?`,
  3: `ZONE : encadré du hadith (p.120), INVERSÉ (blanc sur vert → noir sur blanc).
TRANSCRIS le sanad complet, le matn complet et la référence.
QUESTIONS : (1) sanad : LETTRE PAR LETTRE le nom du Compagnon — « أَبِي يَعْلَى شَدَّادِ بْنِ أَوْسٍ » ? puis ce qui suit « رَضِيَ اللهُ » : « تَعَالَى عَنْهُ » ou seulement « عَنْهُ » ? (2) matn : « فَإِذَا قَتَلْتُمْ فَأَحْسِنُوا الْقِتْلَةَ، وَإِذَا ذَبَحْتُمْ فَأَحْسِنُوا ... » — LETTRE PAR LETTRE le mot après « فَأَحْسِنُوا » : « الذَّبْحَ » (sans tāʾ marbūṭa finale) ou « الذَّبْحَةَ » (avec tāʾ marbūṭa = 2 points dessus) ? Décris la dernière lettre du mot. (3) la fin du matn : « وَلْيُحِدَّ أَحَدُكُمْ شَفْرَتَهُ، وَلْيُرِحْ ذَبِيحَتَهُ » — confirme LETTRE PAR LETTRE « وَلْيُحِدَّ » (ḥāʾ 1 point dessous) et « وَلْيُرِحْ » (rāʾ 0 point). (4) la référence exacte.`,
  4: `ZONE : haut de la p.122 — début de la liste des domaines.
TRANSCRIS tout.
QUESTIONS : (1) la 1re ligne : LETTRE PAR LETTRE les deux premiers mots — « وَفِي الْعِبَادَاتِ » (wāw+fāʾ) ou « فَفِي الْعِبَادَاتِ » (fāʾ+fāʾ) ou autre ? Décris la première lettre. (2) la suite : « يَقُولُ الرَّسُولُ ﷺ: « أَنْ تَعْبُدَ اللهَ كَأَنَّكَ تَرَاهُ، فَإِنْ لَمْ تَكُنْ تَرَاهُ فَإِنَّهُ يَرَاكَ » — transcris le tout. (3) la référence exacte : « [صحيح البخاري ومسلم] » ou « [صحيحا البخاري ومسلم] » ou autre ? LETTRE PAR LETTRE le mot après le crochet ouvrant.`,
  5: `ZONE : le verset du dialogue (p.122), 2-3 lignes.
TRANSCRIS tout.
QUESTIONS : (1) la 1re ligne : LETTRE PAR LETTRE les mots d'ouverture — « وَفِي الْحِوَارِ وَالْجِدَالِ » (ḥāʾ 1 point dans الحوار) ou « وَفِي الْجِوَارِ وَالْجِدَالِ » (jīm 1 point dessous dans الجوار) ? Décris la lettre. (2) le verset : « وَلَا تُجَادِلُوا أَهْلَ الْكِتَابِ إِلَّا بِالَّتِي هِيَ أَحْسَنُ » — LETTRE PAR LETTRE le verbe : « تُجَادِلُوا » (pluriel, wāw final) ou « تُجَادِلْ » (singulier) ? (3) la référence exacte : [العنكبوت: 46] ? en quels chiffres (arabe/indien) ?`,
  6: `ZONE : titre ثانياً + phrase d'ouverture (p.122).
TRANSCRIS tout.
QUESTIONS : (1) le titre : « ثَانِيًا: الْإِحْسَانُ إِلَى الْحَيَوَانِ » — confirme. (2) la phrase d'ouverture : elle commence par quoi ? LETTRE PAR LETTRE les 2 premiers mots — « حَثَّ الْإِسْلَامُ » (ḥāʾ+thāʾ+thāʾ) ou « أَمَرَ الْإِسْلَامُ » ou « أَكَّدَ الْإِسْلَامُ » ou autre ? Décris chaque lettre des 2 mots. (3) la suite : « ... عَلَى الْإِحْسَانِ إِلَى الْحَيَوَانَاتِ وَالرِّفْقِ بِهَا، وَرَتَّبَ عَلَيْهِ ... » — LETTRE PAR LETTRE ce qui suit « وَرَتَّبَ عَلَيْهِ » : « الْأَجْرُ الْعَظِيمُ وَالثَّوَابُ الْجَزِيلُ » ou autre enchaînement ?`,
  7: `ZONE : le hadith de la confinement des bêtes (p.122) — LE PASSAGE LE PLUS DIFFICILE.
TRANSCRIS tout ce qui est visible, ligne par ligne.
QUESTIONS : (1) la ligne d'introduction : « وَفِي نَهْيِهِ ﷺ عَنْ ... » — transcris-la : quels sont les mots après « عَنْ » ? (2) le sanad : « كَمَا فِي حَدِيثِ ... رَضِيَ اللهُ عَنْهُ » — LETTRE PAR LETTRE le nom du Compagnon : « أَنَسٍ » (ʿayn+nūn+sīn, 3 lettres) ou « ابْنِ عُمَرَ » (6 lettres) ou autre ? (3) le matn : « نَهَى أَنْ ... » — LETTRE PAR LETTRE le verbe qui suit « أَنْ » : « تُصَبَّرَ » (ṣād+bāʾ+shadda+rāʾ, passif) ou « تُصَبِّرَ » (actif) ou « تُعَذِّبَ » ou autre ? Décris chaque lettre. puis le mot sujet : « الْبَهِيمَةُ » ou « الْبَهَائِمُ » ? (4) la référence entre crochets. (5) la glose qui suit : « وَمَعْنَى ... : أَنْ تُحْبَسَ بِلَا طَعَامٍ وَلَا شَرَابٍ » — LETTRE PAR LETTRE le mot entre « وَمَعْنَى » et « : ».`,
  8: `ZONE : hadith de la femme et la chatte (p.122), fin.
TRANSCRIS tout.
QUESTIONS : (1) le début du matn : « دَخَلَتِ امْرَأَةٌ النَّارَ فِي هِرَّةٍ رَبَطَتْهَا » — confirme lettre par lettre « دَخَلَتِ ». (2) le milieu : « فَلَا هِيَ أَطْعَمَتْهَا وَلَا هِيَ أَرْسَلَتْهَا تَأْكُلُ مِنْ خَشَاشِ الْأَرْضِ » — confirme. (3) la fin exacte après « الْأَرْضِ » : LETTRE PAR LETTRE — « حَتَّى مَاتَتْ » seul, ou « حَتَّى مَاتَتْ مِنْ جُوعِهَا », ou autre ? (4) la référence entre crochets exacte : [صحيح البخاري] / [متفق عليه] / [سنن ابن ماجة] / autre ? LETTRE PAR LETTETRE ce qui est imprimé entre les crochets.`,
  9: `ZONE : les règles du sacrifice (p.123), lignes denses.
TRANSCRIS tout.
QUESTIONS : (1) après « وَذَلِكَ بِأَنْ » : LETTRE PAR LETTRE le verbe — « يُتْقِنَ » (yāʾ+alif+tāʾ+qāf+nūn — 5 lettres, avec tāʾ) ou « يُقْنَ » (4 lettres, sans tāʾ) ? Décris chaque lettre. (2) la suite : « وَيَرْفُقَ بِالْبَهِيمَةِ فَلَا يَصْرَعَهَا بَغْتَةً وَلَا يَجُرَّهَا مِنْ مَوْضِعٍ إِلَى مَوْضِعٍ » — confirme « بَغْتَةً » (ġayn) et « يَجُرَّهَا ». (3) « وَيَتْرُكُهَا ... » : LETTRE PAR LETTRE ce qui suit « وَيَتْرُكُهَا » — « حَتَّى تَبْرُدَ » ou « إِلَى أَنْ تَبْرُدَ » ? (4) la phrase « وَأَنْ لَا ... السِّكِّينَ أَمَامَهَا » : LETTRE PAR LETTRE le verbe — « يُشْحَذَ » (passif : le couteau n'est pas aiguisé) ou « يَشْحَذْ » (actif : il n'aiguise pas) ? (5) « وَأَنْ لَا يُذْبَحَ/يَذْبَحَ ذَبِيحَةً أُخْرَى أَمَامَهَا » : passif ou actif ? (6) la dernière règle : « وَأَنْ لَا يُقْطَعَ/يَقْطَعَ شَيْئًا مِنْهَا حَتَّى تَمُوتَ » — transcris-la.`,
  10: `ZONE : transition animaux nuisibles + en-tête + item 1 (p.123).
TRANSCRIS tout, ligne par ligne.
QUESTIONS : (1) la 1re phrase : « وَالْإِحْسَانُ/وَكَمَا يُطْلَبُ الْإِحْسَانُ فِي ذَبْحِ بَهِيمَةِ الْأَنْعَامِ الَّتِي أَحَلَّ اللهُ أَكْلَهَا ... » — LETTRE PAR LETTRE les tout premiers mots de la zone (elle peut commencer au milieu d'une phrase) et l'enchaînement exact : quels mots précèdent « يُطْلَبُ » et que suit-il ? (2) « كَالْأَفَاعِي وَالْعَقَارِبِ وَ... » : LETTRE PAR LETTRE le 3e mot — « الْفَئْرَانِ » (fāʾ+alif+hamza+yāʾ+rāʾ+alif+nūn) ou « الْفَأْرَانِ » (fāʾ+alif+alif+rāʾ+alif+nūn, sans yāʾ) ? Décris la 3e lettre : hamza+yāʾ (2 points dessous) ou alif ? (3) « أَوِ الَّتِي نَزَلَ/يُنْقَلَ بِهَا بَعْضُ الْأَمْرَاضِ الَّتِي يَسْتَحِيلُ بُرْؤُهَا » : LETTRE PAR LETTRE le verbe — « نَزَلَ » (nūn+zāy+lām) ou « يُنْقَلَ » ? (4) l'en-tête de liste : « وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ: » — confirme. (5) le premier item numéroté : quel est son numéro imprimé (1 ou 2) et son texte complet ? S'il y a un item numéroté « 1 », transcris-le intégralement.`,
  11: `ZONE : items de la liste ومما يستفاد (p.123) — جار et والدين.
TRANSCRIS tout.
QUESTIONS : (1) item du جار : « الْإِحْسَانُ فِي مُعَامَلَةِ الْجَارِ وَالتَّحَبُّبِ ... كَمَا يُتَحَبَّبُ إِلَى الْأَقَارِبِ » — LETTRE PAR LETTRE la préposition après « وَالتَّحَبُّبِ » : « لَهُ » (lām+hāʾ) ou « إِلَيْهِ » (alif+lām+yāʾ+hāʾ) ? (2) la suite : « وَرِعَايَةُ حَقِّهِ فِي مَشْهَدِهِ وَ... » — LETTRE PAR LETTRE le 2e mot : « مَغِيبِهِ » (ĠAYN 1 point) ou « مَعْبَدِهِ » (ʿayn 0 point) ? (3) item du والدين : « الْإِحْسَانُ إِلَى الْوَالِدَيْنِ بِإِدَامَةِ مَحَبَّتِهِمْ وَبِرِّهِمْ وَصِلَتِهِمْ وَإِكْرَامِهِمْ، وَالدُّعَاءِ ... » — LETTRE PAR LETTRE le pronom après « وَالدُّعَاءِ » : « لَهُمَا » ou « لَهُمْ » ? (4) « وَالصَّدَقَةِ ... » — LETTRE PAR LETTRE le pronom après « وَالصَّدَقَةِ » : « عَنْهُمَا » ou « عَنْهُمْ » ? (5) la fin : « وَصِلَةِ أَهْلِ وُدِّهِمْ » — confirme.`,
  12: `ZONE : le verset final + référence (p.123).
TRANSCRIS tout.
QUESTIONS : (1) le verset entre « » : transcris-le LETTRE PAR LETTRE — commence-t-il par « هَلْ جَزَاءُ الْإِحْسَانِ إِلَّا الْإِحْسَانُ » ou autre chose ? (2) la référence entre crochets : « [الرَّحْمَن: ٦٠] » ou « [الرَّحْمَن: ٥٩] » ? Donne les chiffres EXACTS imprimés (chiffres arabes-indiens) et décris chaque chiffre. (3) la ligne au-dessus : « ... وَيَسْتَوْجِبُ مَحَبَّةَ النَّاسِ جَزَاءَ إِحْسَانِهِ فِي أَخْلَاقِهِ وَتَصَرُّفَاتِهِ. قَالَ تَعَالَى: » — confirme « وَيَسْتَوْجِبُ » (wāw+sīn+tāʾ+wāw+ǧīm+bāʾ).`,
  13: `ZONE : les 3 questions du تقويم (p.124).
TRANSCRIS les 3 questions complètes.
QUESTIONS : (1) question 1 : « أَذْكُرُ خَمْسَةَ أَشْيَاءَ ... فِي عُمُومِ الْإِحْسَانِ فِي كُلِّ شَيْءٍ » — LETTRE PAR LETTRE le verbe après « أَشْيَاءَ » : « تَدْخُلُ » (tāʾ+dāl+khāʾ+lām — 4 lettres, khāʾ 1 point dessus) ou « تَدُلُّ » (tāʾ+dāl+lām+shadda — 3 lettres) ? Décris chaque lettre. (2) question 2 : transcris-la — le mot après « مِنَ » : « الْإِحْسَانِ » (ḥāʾ) ou « الْإِنْسَانِ » (nūn) ? (3) question 3 : transcris-la intégralement — le verbe d'ouverture : « أُبَيِّنُ » ou « أُبَيِّنْ » ? et la fin : « بِنُصُوصٍ شَرْعِيَّةٍ » ?`,
  14: `ZONE : la glose 2 de l'exploitation (p.124), 1-2 lignes.
TRANSCRIS tout.
QUESTIONS : (1) la ligne : « 2. ... » — LETTRE PAR LETTRE le/les mot(s) entre le numéro « 2. » et « الْجَارِ » : « أُبَيِّنُ مَعْنَى » ou « أُوَضِّحُ مَعْنَى » ou autre chose ? Décris chaque lettre de ce qui précède « الْجَارِ ». (2) transcris la suite complète : « الْجَارِ ذِي الْقُرْبَى وَالْجَارِ ... » — LETTRE PAR LETTRE le mot après « وَالْجَارِ » : « الْجُنُبِ » (jīm+nūn+bāʾ) ou « الْمُجَاوِرِ » ou autre ? (3) la fin de ligne : « وَالصَّاحِبِ بِالْجَنْبِ وَابْنِ السَّبِيلِ » — confirme.`,
  15: `ZONE : la préparation الإعداد القبلي (p.124).
TRANSCRIS tout (en-tête + 2 items).
QUESTIONS : (1) l'en-tête de la rubrique. (2) la ligne d'instruction : « أَحْفَظُ حَدِيثَ الدَّرْسِ ... » — LETTRE PAR LETTRE ce qui suit « الدَّرْسِ » : y a-t-il « الْآتِيَ » puis « ثُمَّ أُجِيبُ عَنِ الْآتِي: » ou seulement « وَأُجِيبُ عَنِ الْآتِي: » ? Décris l'enchaînement exact des mots. (3) item 1 : « أَشْرَحُ: ... » — transcris-le ; LETTRE PAR LETTRE le mot après « أَشْرَحُ: » : « اتَّقِ اللهَ » ? (shadda sur tāʾ) puis « تَمْحُهَا » (tāʾ 2 points dessus) ou « نَمْحَهَا » (nūn 1 point dessous) ? (4) item 2 : transcris-le intégralement.`,
};

const zai = await ZAI.create();
const a = parseInt(process.argv[2] || '1', 10);
const b = parseInt(process.argv[3] || '15', 10);
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (let i = a; i <= b; i++) {
  if (!R[i]) continue;
  const k = 'b' + String(i).padStart(2, '0');
  const out = `${DIR}/z22-${k}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${k}`); continue; }
  const img = fs.readFileSync(`${DIR}/z22-${k}.png`).toString('base64');
  console.log(`\n======== ${k} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + R[i] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo',
        temperature: 0.1,
        max_tokens: 1600,
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
console.log('\nVAGUE B TERMINÉE');
