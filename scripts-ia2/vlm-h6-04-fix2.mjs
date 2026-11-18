// Z2-38 — hadith-6ep leçon 3 «التنافس في الخير» — Round 3 : relectures r600 ×2 LANCZOS
// (protocole Z2-37 : les crops r600 ×2 sont fiables là où le VLM a halluciné sur r1200)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04';

const COMMON = `Recadrage (grossi ×2) d'un manuel scolaire marocain d'hadith (6e primaire, arabe), leçon «التنافس في الخير». TRANSCRIS UNIQUEMENT ce qui est imprimé, mot à mot, avec les voyelles visibles. Pour chaque point demandé, DÉCRIS les lettres (points, boucles, hampes) AVANT de conclure. Si un candidat proposé NE CORRESPOND PAS aux pixels, dis-le explicitement (protocole CONCORDE / NE CORRESPOND PAS). Ne complète jamais par mémoire d'un texte connu.`;

const ZONES = [
  ['p24-ban-hadith2', 24, 55, 505, 605, 565,
   `Zone au-dessus du hadith: y a-t-il un bandeau-titre avec un mot calligraphié (comme «الحديث الشريف»), ou seulement un cadre décoratif ? TRANSCRIS tout texte visible lettre par lettre. Si c'est un cadre sans texte, décris-le.`],
  ['p24-hadith-isnad', 24, 55, 560, 605, 655,
   `Début du hadith: l'isnad complet. TRANSCRIS mot à mot: «عن أبي ... رضي الله عنه ... أن ناسا من أصحاب رسول الله ﷺ قالوا للنبي ﷺ: يا رسول الله، ذهب أهل الدثور بالأجور...». Le narrateur est-il أبو ذر (ذ 1 point) ou أبو هريرة ? Le mot après «عنه» est-il أَيْضًا (أ ي ض ا) ? Transcris jusqu'à «بالأجور».`],
  ['p24-hadith-end', 24, 55, 650, 605, 745,
   `Fin du hadith sur cette page: 2-3 lignes après «قال: أوليس قد جعل الله لكم ما تصدقون؟». TRANSCRIS TOUTES les lignes mot à mot jusqu'en bas (attendu: «إنَّ بكُلِّ تسبيحةٍ صدقة، وكلُّ تكبيرةٍ صدقة، وكلُّ...» puis peut-être un fragment avant le pied de page). Y a-t-il quoi que ce soit ressemblant à «فمن كنز في الأرض» ? CONFIRME ou INFIRME mot à mot ce qui est imprimé.`],
  ['p24-tamhid-mid', 24, 55, 365, 605, 430,
   `Lignes 2-3 du paragraphe تمهيد. TRANSCRIS mot à mot: attendu «فَيُهْمِلُ أَعْمَالًا أُخْرَى وَلَا يَحْرِصُ عَلَيْهَا، مَعَ أَنَّهَا مِنَ الصَّدَقَاتِ الَّتِي يُثَابُ عَلَيْهَا كَمَا يُثَابُ عَلَى التَّصَدُّقِ بِالْمَالِ» — vérifie chaque mot (فيُهمل ou فيهمل ? التَّصَدُّقِ ou الصَّدَقَةِ ?).`],
  ['p25-glose-dathur2', 25, 140, 400, 570, 450,
   `Glose noire de la rubrique الشرح: «الدُّثُورُ: بِضَمِّ ... جَمْعُ ... بِفَتْحِهَا، وَهُوَ الْمَالُ الْكَثِيرُ.» Deux points: (1) après بضم: الدَّالِ (ل sans point au-dessus) ou الذَّالِ (ل avec 1 point au-dessus) ? (2) après جمع: دَثْرٍ (2e lettre = ث 3 points) ou autre ? CONCORDE/NE CORRESPOND PAS.`],
  ['p25-glose-tahlila', 25, 260, 550, 570, 615,
   `Glose: «التَّهْلِيلَةُ: قَوْلُ لَا إِلَٰهَ إِلَّا اللهُ.» (ou une autre glose). TRANSCRIS le mot rouge (headword) lettre par lettre: التَّهْلِيلَةُ (ت+هـ+ل+ي+ل+ة, deux lām) ou تَحْمِيدَةُ (ت+ح+م+ي+د+ة, aucun lām) ou autre ? Puis la définition noire exacte.`],
  ['p25-glose-wazr2', 25, 340, 615, 570, 660,
   `Glose: «وِزْرٌ: ...». TRANSCRIS la définition exacte mot à mot. Le mot défini est-il إِثْمٌ (alif-hamza INITIALE avec hamza SOUS l'alif) ou آثِمٌ (alif avec madda AU-DESSUS) ? Décris la 1re lettre précisément. CONCORDE/NE CORRESPOND PAS.`],
  ['p26-awwalan-dhalika', 26, 55, 385, 605, 435,
   `Deux lignes de la section أولاً: «ذَهَبَ أَهْلُ الْأَمْوَالِ بِالْأَجْرِ كُلِّهِ؛ ذَلِكَ أَنَّ... يُصَلُّونَ كَمَا نُصَلِّي، وَيَصُومُونَ كَمَا نَصُومُ،». Après «ذلك أنَّ»: le mot est-il هُ (hāʾ seule, PAS de mīm) ou هُمْ (hāʾ + mīm bouclée) ? CONCORDE/NE CORRESPOND PAS. Puis transcris la fin de la ligne suivante («يتصدقون بفضول أموالهم»...).`],
  ['p26-thani-start2', 26, 370, 532, 580, 580,
   `Début du paragraphe de la section ثانياً: «... فِي قَوْلِهِ ﷺ: «... بِكُلِّ تَسْبِيحَةٍ صَدَقَةٌ...». Donne le premier verbe EXACT de la ligne (avant «في قوله»): تَبَيَّنَ (ت 2pts + ب + ي + ن + shadda?) ou بَيَّنَ (ب + ي + ن + shadda, sans ت initial) ? Décris si la 1re lettre du mot est un ت (2 points au-dessus) ou un ب (1 point en dessous). Puis: le mot après ﷺ et le guillemet ouvrant est-il إِنَّ (avec shadda) ou إِنْ (sans shadda) ?`],
  ['p26-thani-irshad2', 26, 55, 650, 605, 705,
   `Ligne de la section ثانياً: «فَذِكْرُ اللهِ بِالتَّسْبِيحِ وَالتَّكْبِيرِ وَالتَّحْمِيدِ وَالتَّهْلِيلِ، وَإِرْشَادُ النَّاسِ وَتَوْجِيهُهُمْ إِلَى الْخَيْرِ ... صَدَقَةٌ مِنَ الصَّدَقَاتِ يُثَابُ عَلَيْهَا الْإِنْسَانُ كَمَا يُثَابُ عَلَى الصَّدَقَةِ بِالْمَالِ.» Donne le groupe EXACT après «إلى الخير»: (A) وَتَجَنُّبُ الشَّرِّ (ج 1 point sous, ب 1 point sous, ش 3 points) ; (B) وَتَحْذِيرُهُمْ (ح sans point + ذ 1 point + ر + هم) ; (C) autre. CONCORDE/NE CORRESPOND PAS pour chaque candidat, avec description des lettres vues.`],
  ['p27-diag-title2', 27, 55, 380, 605, 460,
   `Consigne/titre au-dessus d'un organigramme (après la rubrique مما يستفاد). TRANSCRIS tout ce qui est imprimé mot à mot. Candidats possibles: «أُلَاحِظُ...» / «أُقَارِنُ بَيْنَ...» / «أُمَيِّزُ...» / une phrase avec «الصَّحَابَة». Donne le texte EXACT ligne par ligne.`],
  ['p27-diag-bleus', 27, 55, 455, 605, 585,
   `Organigramme: deux boîtes bleues côte à côte (droite et gauche), reliées par des traits. TRANSCRIS le texte de la boîte bleue DE DROITE puis celui de la boîte bleue DE GAUCHE, mot à mot. Candidats pour la droite: «الْمُدَاوَمَةُ» / «الْعَزِيمَةُ» / «أَدَاءُ الْفَرَائِضِ وَالنَّوَافِلِ» / autre ; pour la gauche: «تَرْكُ الْفَرَائِضِ» / «الْإِفْرَاطُ» / autre. Décris chaque boîte (couleur, position, liens).`],
  ['p27-diag-jaunes', 27, 55, 545, 605, 640,
   `Organigramme: deux boîtes jaunes sous les boîtes bleues. TRANSCRIS le texte de la boîte jaune DE DROITE puis DE GAUCHE, mot à mot. Candidats: «أَدَاءُ الْفَرَائِضِ وَالنَّوَافِلِ» / «أَدَاءُ الْفَرَائِضِ» / «تَرْكُ الْفَرَائِضِ» / autre. CONCORDE/NE CORRESPOND PAS.`],
  ['p27-diag-lastright', 27, 330, 660, 605, 745,
   `Cellule du bas de la colonne DROITE de l'organigramme (sous «التنافس في الخير»). TRANSCRIS son texte complet mot à mot. Candidats: «التَّمَتُّعُ بِالْمُبَاحَاتِ بِقَصْدِ التَّقَرُّبِ إِلَى اللهِ» / «تَحْوِيلُ الْعَادَةِ عِبَادَةً» / autre. Le mot clé: بِقَصْدِ (ب 1 point sous + ق 2 points) ou دُونَ (د + و + ن) ? CONCORDE/NE CORRESPOND PAS.`],
  ['p27-diag-lastleft', 27, 55, 660, 320, 745,
   `Cellule du bas de la colonne GAUCHE de l'organigramme (sous «الكسل والخمول»). TRANSCRIS son texte complet mot à mot. Candidats: «التَّمَتُّعُ بِالْمُبَاحَاتِ دُونَ قَصْدِ التَّقَرُّبِ إِلَى اللهِ» / autre. Le mot clé: دُونَ ou بِقَصْدِ ? CONCORDE/NE CORRESPOND PAS.`],
  ['p28-t1-end', 28, 80, 108, 570, 150,
   `Item 1 de التقويم, fin de ligne: «... رَضِيَ اللهُ عَنْهُمْ ...». TRANSCRIS les 3-4 derniers mots. La fin est-elle «لِلَاقْتِدَاءِ» (ل+ل+ا+ق) ou «لِلِاقْتِدَاءِ» ou «لِلَاقْتِدَاءِ بِهِمْ» (avec بِهِمْ: ب 1 point sous + هـ + م bouclée) ? Décris les lām/alif et la présence ou non de بهم. CONCORDE/NE CORRESPOND PAS.`],
  ['p28-t3', 28, 55, 180, 570, 235,
   `Item 3 de التقويم: «3- ... أَمْثِلَةً أُخْرَى لِلْمُبَاحَاتِ الَّتِي تَتَحَوَّلُ بِالنِّيَّةِ إِلَى عِبَادَاتٍ.». Donne le premier verbe EXACT: أَذْكُرُ (أ 1 point + ذ 1 point + ك + ر, SANS shadda sur ك) ou أُذَكِّرُ (avec shadda sur ك) ? Décris la présence de shadda. CONCORDE/NE CORRESPOND PAS.`],
  ['p28-cit-anta2', 28, 55, 372, 570, 425,
   `Citation d'Abû Ḏarr, lignes: «قُلْتُ: يَتَصَدَّقُونَ وَلَا نَتَصَدَّقُ. قَالَ: ... فِيكَ صَدَقَةٌ؛ رَفْعُكَ الْعَظْمَ عَنِ الطَّرِيقِ صَدَقَةٌ، وَ... الطَّرِيقَ صَدَقَةٌ، وَعَوْنُكَ الضَّعِيفَ بِفَضْلِ قُوَّتِكَ صَدَقَةٌ...». Donne: (1) le mot avant «فيك»: وَأَنْتَ (ت 2pts finale) ou وَأَنْتُمْ (ت + م) ? (2) فِيكَ ou فِيكُمْ ? (3) le mot après «وَ»: هُدَاكَ (هـ+د+ا+ك) ou هِدَايَتُكَ (هـ+د+ا+ي+ة+ك) ? (4) الضَّعِيفَ ou الضَّعِيفِ ? (5) le mot après بِفَضْلِ. CONCORDE/NE CORRESPOND PAS pour chacun.`],
  ['p28-cit-ref2', 28, 170, 422, 570, 468,
   `Référence entre crochets: «[عَوْنُ الْمَعْبُودِ شَرْحُ سُنَنِ أَبِي دَاوُودَ، ... بِتَصَرُّفٍ]». Transcris la partie chiffrée EXACTEMENT: quels chiffres, dans quel ordre de droite à gauche, quels séparateurs (barre oblique /) ? Y a-t-il 6/121 ou 121/6 ou autre ? Les chiffres sont-ils arabes (٦ ١٢١) ou occidentaux ? Décris chaque chiffre avant de conclure.`],
  ['p28-ex1b', 28, 80, 478, 570, 522,
   `Item 1 de l'استثمار: «1- أَسْتَخْرِجُ مِنَ النَّصِّ الصَّدَقَاتِ الَّتِي لَمْ ... ذِكْرُهَا فِي حَدِيثِ الدَّرْسِ.». Le verbe après «لم» est-il يَرِدْ (ي 2pts sous + ر + د) ou يُرَدْ (damma sur ي) ? Décris. CONCORDE/NE CORRESPOND PAS.`],
  ['p28-iqbal2', 28, 55, 520, 605, 710,
   `Bas de page: rubrique الإعداد القبلي. TRANSCRIS tout: (1) le bandeau décoratif ; (2) la consigne: «... حَدِيثَ الدَّرْسِ الْمُوَالِي وَأُنْجِزُ مَا يَأْتِي:» — le premier verbe: أَحْفَظُ (ح + ف + ظ 1 point) ou أُحَافِظُ (ح + ا + ف + ظ) ? décris la longueur; (3) item 1 «أُشْرِحُ: سَلَامَى - ... بَيْنَ اثْنَيْنِ - ... الْأَذَى» — le 3e terme: أُمَيِّطُ (أ+م+ي+ط avec shadda) ou تُمِيطُ (ت) ou أَمِيطُ ? ; (4) item 2 complet «... الصَّدَقَاتِ الْوَارِدَةَ فِي الْحَدِيثِ». CONCORDE/NE CORRESPOND PAS pour chaque point.`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

fs.mkdirSync(`${DIR}/crops`, { recursive: true });
for (const [nom, pg, x0, y0, x1, y1] of ZONES) {
  const fp = `${DIR}/crops/vlm-${nom}.png`;
  if (!fs.existsSync(fp)) {
    execSync(`python3 -c "
from PIL import Image
S=600/72.0
im=Image.open('${DIR}/r600/p${pg}.png')
c=im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S)))
c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
c.save('${fp}')
"`);
  }
}

for (const [nom, , , , , , Q] of ZONES) {
  const out = `${DIR}/vlm-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  const img = fs.readFileSync(`${DIR}/crops/vlm-${nom}.png`).toString('base64');
  console.log(`\n======== ${nom} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 3 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1500,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${nom} échec: ${e.message}`); await sleep(5000*attempt); }
  }
  if (!done) console.log(`ECHEC ${nom} — quota ?`);
  await sleep(2000);
}
