// Z2-31 — VLM bandes 1200 dpi natives, leçon 26 «الاستقامة» (pp.144-149)
// Prompts NEUTRES (leçon Z2-30 : ne jamais offrir de candidats — biais démontré).
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-26/bands';
const COMMON = `Bande pleine largeur à 1200 dpi NATIF (très net) d'un manuel scolaire marocain d'hadith, 5e année primaire traditionnel, leçon 26 «الاستقامة», lecture droite→gauche.
TRANSCRIS TOUT ce qui est imprimé sur la bande, ligne par ligne, mot à mot, AVEC LA VOCALISATION. Les nombres en chiffres arabes orientaux : transcris-les EXACTEMENT.
Pour CHAQUE mot dont la lecture est incertaine ou amusante, ajoute une note [?] avec la décomposition lettre par lettre (forme, nombre de points, place des points).
Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé.`;

const Q = {
  'b01-p144': `Le bandeau de titre de la leçon (le numéro EXACT en chiffres arabes orientaux + le titre), puis أهداف الدرس (3 objectifs numérotés — mot à mot, vocalisation exacte, en particulier le premier mot de l'objectif 1 et le premier mot de l'objectif 3).`,
  'b02-p144': `Le texte d'introduction (تمهيد — toutes les lignes mot à mot, jusqu'aux questions finales ; note [?] sur le mot après «أَمْرٍ جَامِعٍ فِي الدِّينِ» et sur le dernier mot de la dernière question).`,
  'b03-p144': `L'ENCADRÉ DU HADITH (fond ornementé) : l'en-tête du cadre s'il est imprimé (décompose-le lettre par lettre), le sanad complet (le nom du rāwī EXACTEMENT mot à mot, y compris l'éventuel ethnique), le matn complet mot à mot avec la vocalisation, et la référence entre crochets. Note [?] sur tout mot incertain.`,
  'b04-p145': `La rubrique تَرْجِمَةُ الرَّاوِي (notice du compagnon — mot à mot : la kunya, le nom, l'ethnique, l'origine, l'islam avec le wafd, ce qu'il a (صحبة/سماع/رواية — décompose le 2e mot de cette série lettre par lettre), et qui l'a employé et sur quoi).`,
  'b05-p145': `Les rubriques اَلْفَهْمُ et اَلشَّرْحُ avec TOUTES les gloses en tirets (chaque tête de glose et son explication, mot à mot ; note [?] sur le premier mot de la 2e glose et sur ce qui suit «أَيْ» dans la 2e glose).`,
  'b06-p145': `اِسْتِخْلَاصُ الْمَضَامِينِ (questions numérotées), puis اَلتَّحْلِيلُ (phrase d'intro — mot à mot, en particulier le mot entre «عَلَى» et «بِالْإِيمَانِ»), puis أولاً et 1. مَعْنَى الِاسْتِقَامَةِ (لغةً et شرعاً, mot à mot).`,
  'b07-p146': `Les premières lignes de la page : la fin de la définition (لُزُومُ الطَّاعَةِ...) puis «وَمَعْنَى قَوْلِ السَّائِلِ...» et la phrase qui glose la demande (mot à mot — note [?] sur le 1er mot de la glose après les deux points, sur le mot après «جَامِعًا لِمَعَانِي الْإِسْلَامِ», et sur le dernier verbe avant «بِهِ»), puis «فَأَجَابَهُ...».`,
  'b08-p146': `Le paragraphe جَوَامِعِ الْكَلِمِ (mot à mot — note [?] sur le mot entre «الْكَلِمِ» et «صَلَّى اللهُ», sur la structure «فَإِنَّهُ أَمَرَهُ أَنْ... بِلِسَانِهِ مُتَذَكِّرًا...», et sur le verbe de «إِذْ لَا ... الِاسْتِقَامَةُ مَعَ شَيْءٍ مِنَ الِاعْوِجَاجِ»).`,
  'b09-p146': `La citation coranique avec SA RÉFRENCE EXACTE (sourate + numéro en chiffres arabes orientaux — décompose le numéro chiffre par chiffre), puis le commentaire de ʿUmar ibn al-Khaṭṭāb (mot à mot — note [?] sur le 1er verbe entre «وَ» et «رَوْغَانَ», et sur le DERNIER mot de la citation, décompose-le lettre par lettre), puis «وَمَعْنَاهُ...».`,
  'b10-p146': `«وَهَذَا مَعْنَى...» (mot à mot), puis la 2e citation coranique [هود: ...] avec le numéro EXACT, puis le dire d'Ibn ʿAbbās (mot à mot — note [?] sur le 2e mot «مَا ... عَلَى رَسُولِ اللهِ», et sur le 1er mot du hadith final «... هُودٌ وَأَخَوَاتُهَا») et sa référence.`,
  'b11-p147': `La section 2. عَلَاقَةُ الِاسْتِقَامَةِ بِالْإِيمَانِ (mot à mot, TOUTES les lignes — note [?] sur la 2e moitié de la 1re phrase après «إِلَّا بَعْدَ الْإِيمَانِ», sur ce qui suit «فَالْإِيمَانُ» dans la phrase conditionnelle, et sur le mot avant «اسْتِقَامَةٍ لَا يَكْفِي»).`,
  'b12-p147': `ثانياً: فَضْلُ الِاسْتِقَامَةِ وَثَمَرَاتُهَا — la citation d'al-Qushayrī (mot à mot — note [?] sur le titre exact de l'auteur, sur le mot entre «وُجُودِهَا» et «الْخَيْرَاتِ», et sur les mots de «مَنْ لَمْ يَكُنْ مُسْتَقِيمًا فِي ... سَعْيِهِ ... سَعْيُهُ وَ... جَدُّهُ»).`,
  'b13-p147': `La suite «وَقِيلَ: الِاسْتِقَامَةُ لَا يُطِيقُهَا...» (mot à mot — note [?] sur le mot après «عَنِ الْمَعْ...»), puis le hadith cité avec sa référence [الموطأ] et son explication «أَيْ...» (mot à mot — décompose lettre par lettre le verbe entre «اسْتَقِيمُوا وَ» et la fin, et la série après «أَيْ»).`,
  'b14-p147': `La citation d'al-Wāsiṭī (mot à mot — note [?] sur le 3e mot après «هِيَ»), puis «وَمِنْ فَضَائِلِ الِاسْتِقَامَةِ وَثَمَرَاتِهَا:» et le PREMIER item en tiret (mot à mot jusqu'au bas de la bande — note [?] sur le verbe après «وَالْمَوْتِ»).`,
  'b15-p148': `La suite du 1er item (2 lignes), puis les items 2 et 3 en tirets (mot à mot).`,
  'b16-p148': `«يَقُولُ اللهُ تَعَالَى...» puis la citation coranique COMPLÈTE mot à mot, avec les numéros de versets entre parenthèses tels qu'imprimés (décompose-les chiffre par chiffre) et la référence finale EXACTE. Note [?] sur tout mot incertain — surtout les verbes.`,
  'b17-p148': `وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ (les 3 items en tirets, mot à mot — note [?] sur le mot après «وَنِدَاؤُهُ» dans l'item 2, et sur toute la fin de l'item 3 après «لَا كَمَا»).`,
  'b18-p148': `اَلتَّقْوِيمُ (les 3 questions numérotées, mot à mot — en particulier ce qui suit «بِ» dans la question 2).`,
  'b19-p149': `L'ENCADRÉ du hadith d'Anas ibn Mālik (fond ornementé) : le sanad, le matn COMPLET mot à mot avec la vocalisation (note [?] sur le verbe de «وَلَا ... الْجَنَّةَ», sur le mot «جَار...» et sa voyelle, et sur le DERNIER mot), et la référence.`,
  'b20-p149': `Les activités numérotées de l'استثمار (mot à mot — note [?] sur la série après «عَلَى» dans l'activité 1, et sur le mot après «أُبَيِّنُهَا» dans l'activité 2).`,
  'b21-p149': `La rubrique الاِعْدَادُ الْقَبْلِيُّ et ses items numérotés (mot à mot — note [?] sur le mot après «الْمُرَتَّبَةَ» dans l'item 2).`,
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 3000,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 500 ? txt.slice(0, 350) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(2500);
}
