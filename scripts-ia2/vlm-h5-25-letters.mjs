// Z2-30 — VLM scruterins lettre par lettre (recadrages serrés ×4) — leçon 25
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-25/crops';
const COMMON = `Recadrage serré haute résolution (600 dpi agrandi ×4) d'un manuel scolaire marocain d'hadith, 5e année primaire, lecture droite→gauche.
TRANSCRIS le(s) mot(s) imprimé(s) LETTRE PAR LETTRE : pour chaque lettre donne sa forme ET SON NOMBRE DE POINTS (0, 1, 2, 3, au-dessus ou en dessous), puis conclus. Compte aussi les dents. Ne complète JAMAIS par mémoire d'un texte connu.`;

const Q = {
  't1-p139': `Le mot cible (fin de glose) : مَا يُسْتَ...ـرُ — après «فَعَلَ كُلَّ». Décompose le mot ENTIER lettre par lettre avec points et dents. Candidats à départager : يُسْتَقْبَحُ / يُسْتَكْرَهُ / يُسْتَتْكَرُ / يُسْتَحْقَرُ / autre. Donne aussi les voyelles.`,
  't2-p140': `Le mot cible (fin de ثانيهما) : مَا يُسْتَ...ـرُ — après «فَعَلَ كُلَّ». Décompose lettre par lettre avec points et dents. Mêmes candidats : يُسْتَقْبَحُ / يُسْتَكْرَهُ / يُسْتَتْكَرُ / يُسْتَحْقَرُ / autre.`,
  't3-p140': `Le mot cible : le mot entre «لَهُمْ مَا» et «وَمَا يَتْرُكُونَ» (fin : ـونَ). Décompose-le lettre par lettre avec points et dents. Candidats : يَفْعَلُونَ / يَنْهَوْنَ / يَنْوُونَ / يَأْمُرُونَ / autre.`,
  't4-p140': `Le mot cible : DERNIER mot de la définition lexicale (après وَالْمُتْنَاعِ وَالتَّرْكُ) : وَالِاسْتَ...ـاءُ. Décompose lettre par lettre avec points et dents. Candidats : الِاسْتِحْيَاءُ / الِاسْتِبْقَاءُ / الِاسْتِيفَاءُ / الِاسْتِحْفَاءُ / autre.`,
  't5-p141': `Le mot cible : dans «وَلَيْسَ مِنَ الْحَيَاءِ فِعْلُ الْمَعَاصِي وَتَ...ـيلُ» — le mot après وَ. Décompose lettre par lettre avec points et dents. Candidats : وَتَحْلِيلُ / وَتَخْلِيلُ / وَتَكْلِيلُ / وَتَقْلِيلُ / autre.`,
  't6-p141': `Le mot cible : entre «وَتَـ...يلُ» et «حَرَّمَات» — décompose lettre par lettre. S'agit-t-il de «الْمُحَرَّمَاتِ» complet ? Y a-t-il un mot ou des lettres entre (comme لِأَمْ / لِحِلِّ / autre) ?`,
  't8-p138': `Le mot cible : dans la 2e ligne du تمهيد, entre «مَأْثُورِ كُلِّ الْأُمَمِ،» et «الشَّرِيعَةُ الْإِسْلَامِيَّةُ» — le mot qui commence par وَ. Décompose lettre par lettre avec points et dents. Candidats : وَأَكَّدَتْهَا / وَكَانَتْهَا / autre. Donne aussi ce qui précède et suit.`,
  'u01-p138': `C'est le 3e objectif de la leçon (après «3. أَنْ أَتَمَثَّلَ الْمَقَاصِدَ ...»). Transcris le RESTE de la ligne lettre par lettre (entre الْمَقَاصِدَ et تَشْرِيعِ). Candidats pour le segment médian : الشَّرْعِيَّةَ / الرُّوحِيَّةَ / عَبْرَ / النَّشِرَ عِبْرَةً / autre. Décompose avec points et dents.`,
  'u08-p141': `Fin du passage «ليس من الحياء» : «فَهَذَا لَا يُسَمَّى حَيَاءً ...». Transcris TOUT lettre par lettre : le mot après حَيَاءً (شَرْعًا / شَرْعِيًّا ?), puis أَوْ هُوَ حَيَاءٌ مَذْمُومٌ، puis بَلْ هُوَ خَجَلٌ ... — le DERNIER mot : مَذْمُومٌ / مَبْذُولٌ / مَوْرُوطٌ / autre ? Décompose le dernier mot avec points.`,
  'u09-p142': `Les 2 premiers mots de la question 3 du تقويم : «... نَصِيحَةً لِطَالِبِ الْعِلْمِ». Décompose le PREMIER mot lettre par lettre avec points et dents. Candidats : أَعْطِ / أُعْطِي / أُقَدِّمُ / أُبْدِي / autre. Et le tanwīn de نَصِيحَةً (fatḥ ou ḍamm) ?`,
  'u10-p142': `Ligne de l'encadré الاستثمار après «إِذَا رَأَتِ الْمَاءَ». Transcris TOUTE la ligne lettre par lettre : le verbe (فَغَطَّتْ ?), QUI (أُمُّ سَلَمَةَ / أُمُّ سُلَيْمٍ ?), le mot suivant (تَعْنِي ? وَجْهَهَا ?), puis وَقَالَتْ... jusqu'à أَوَتَحْتَلِمُ الْمَرْأَةُ.`,
  'u11-p142': `Fin de l'encadré : «قَالَ: نَعَمْ، ...». Transcris tout lettre par lettre : تَرِبَتْ يَمِينُكِ (kasra ou fatḥa sur ك ?), puis فَبِمَ يُشْبِهُهَا وَلَدُهَا (ou فَبِمَ يُشْبِهُ وَلَدُهَا ?) et la référence [صحيح البخاري].`,
  'u12-p138': `L'en-tête au-dessus de l'encadré du hadith (bandeau décoré noir). Transcris-le lettre par lettre : الْحَدِيثُ ou الْأَحَادِيثُ ? Décompose.`,
  'u13-p143': `Item 1 de l'إعداد القبلي : «أُشْرِحُ: ...». La 3e expression : اسْتَقِمْ ou اسْتَقِيمْ ? Décompose lettre par lettre (y a-t-il un ي médian ?). Donne les 3 expressions complètes.`,
  'u14-p142': `Le 2e item de وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ (commence par الْحَيَاءُ تَرْبِيَةٌ...). Transcris la ligne ENTIÈRE lettre par lettre — y a-t-il un mot entre وَسُلُوكٌ et لَا يَأْتِي (comme خُلُقٌ / هُوَ / autre) ?`,
  'u15-p141': `Le passage : «وَتَجَنُّبُ ... الْفِعْلِ وَالْكَلَامِ». Décompose le mot entre وَتَجَنُّبُ et الْفِعْلِ : فَحْشِ / فُحْشِ / فَاحِشِ / autre ? Et الْفِعْلِ (avec ʿayn) confirmé ?`,
  'u16-p142': `Activité 1 : «هَلْ يُعْتَبَرُ سُؤَالُ الْمَرْأَةِ لِلْعَالِمِ فِي ... دِينِهَا». Le mot entre فِي et دِينِهَا : أُمُورِ / أَمْرِ / أُمُرِ ? Décompose lettre par lettre.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of Object.keys(Q)) {
  const out = `${DIR}/vlmt-${k}.txt`;
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1800,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 450 ? txt.slice(0, 350) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(2500);
}
