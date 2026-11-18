// Z2-30 — VLM zooms 600 dpi sur points contested leçon 25 (méthode série : lettre par lettre)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-25/crops';
const COMMON = `Recadrage haute résolution (600 dpi) d'un manuel scolaire marocain d'hadith, 5e année primaire, sens de lecture droite→gauche.
TRANSCRIS la ligne imprimée MOT À MOT avec la vocalisation. Pour le(s) mot(s) signalé(s) ci-dessous, décompose LETTRE PAR LETTRE (avec les points des lettres) avant de conclure. Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé.`;

const Q = {
  'z01b-p138': `C'est le 3e objectif (أهداف الدرس) de la leçon 25 «الحياء». Transcris-le mot à mot au complet (commence par أَنْ أَتَمَثَّلَ... ?). Les deux objectifs précédents étaient: 1. أَنْ أَتَعَرَّفَ مَعْنَى الْحَيَاءِ وَثَمَرَتَهُ / 2. أَنْ أُمَيِّزَ مَظَاهِرَ الْمَحْمُودِ وَالْمَذْمُومِ مِنَ الْحَيَاءِ.`,
  'z02-p138': `Ligne du تمهيد. QUESTION PRÉCISE : (a) après مِنَ الأَخْلَاقِ — le mot est-il الْجَامِعَةِ ou الْجَمِيلَةِ ? décompose lettre par lettre. (b) la fin de la 2e ligne: مِنْ ضَمَّنِ الْمَحَامِدِ فِي مَأْثُورِ كُلِّ ... — كلِّ AUMMA (أُمَّةٍ, singulier) ou كلِّ الْأُمَمِ (pluriel) ? (c) 3e ligne: وَأَكَّدَتْهَا ou وَكَانَتْهَا ? Transcris tout le passage.`,
  'z03-p138': `ENCADRÉ DU HADITH (orné). Transcris mot à mot: le sanad (عَنْ أَبِي مَسْعُودٍ + NOM DU COMPAGNON lettre par lettre: عُقْبَةَ بْنِ عَمْرٍو ? casse et diacritiques exacts), puis le matn complet «إِنَّ مِمَّا أَدْرَكَ النَّاسُ...» jusqu'à la référence [صحيح البخاري].`,
  'z05-p139': `Glose du الشرح. QUESTION PRÉCISE : après «لَمْ تَسْتَحْيِ:» — la première expression est-elle «مُضَارِعُ اسْتَحْيَا» ? autre chose ? décompose lettre par lettre. Puis transcris le reste: وَفِي رِوَايَةٍ «تَسْتَحِ» بِدُونِ يَاءٍ مِنْ «اسْتَحَى» بِمَعْنَى خَجِلَ وَاحْتَشَمَ.`,
  'z06b-p139': `Fin d'une glose du الشرح: «... مَنْ لَمْ يَكُنْ عِنْدَهُ حَيَاءٌ فَعَلَ كُلَّ مَا ...». QUESTION PRÉCISE : le DERNIER mot (yousse-...) : يُسْتَقْبَحُ ? يُسْتَكْرَهُ ? يُسْتَحْقَرُ ? Décompose LETTRE PAR LETTRE avec les points.`,
  'z06-p139': `Glose «فَاصْنَعْ مَا شِئْتَ». Transcris tout : هُوَ أَمْرٌ بِمَعْنَى ... + بِمَعْنَى: افْعَلْ مَا شِئْتَ وَاللهُ مُجَازِيكَ + أَوْ هُوَ خَبَرٌ بِمَعْنَى: مَنْ لَمْ يَكُنْ عِنْدَهُ حَيَاءٌ فَعَلَ كُلَّ مَا ... (dernier mot lettre par lettre).`,
  'z07b-p140': `Définition lexicale. QUESTION PRÉCISE : le DERNIER mot de la ligne (après وَالامْتِنَاعُ وَالتَّرْكُ وَال...) : الاسْتِ... ? décompose lettre par lettre (الاستبقاء ? الاستحفاء ? الاستحياء ? autre ?).`,
  'z07-p140': `Définition lexicale complète : الْحَيَاءُ لُغَةً: بِالْمَدِّ ... Transcris la ligne entière mot à mot.`,
  'z08b-p140': `Ligne : ... فَإِنَّهُ وَعِيدٌ لِأَنَّهُ قَدْ بَيَّنَ لَهُمْ مَا ... QUESTION PRÉCISE : le mot après مَا (yaf-...) : يَفْعَلُونَ ? يَنْهَوْنَ ? يَأْمُرُونَ ? يَنْفَعُ ? Décompose lettre par lettre.`,
  'z08-p140': `Passage : كَقَوْلِهِ ﴿...﴾ [فصلت: ...] + la phrase qui suit (فَإِنَّهُ وَعِيدٌ...). Transcris tout mot à mot, avec la référence EXACTE telle qu'imprimée.`,
  'z09-p140': `ثانيهما: أَنَّهُ أَمْرٌ بِمَعْنَى الْخَبَرِ... Transcris tout, DERNIER mot lettre par lettre (يُسْتَقْبَحُ/يُسْتَكْرَهُ/...).`,
  'z09b-p140': `Le DERNIER mot de la ligne (ما يُسْتَ-...): décompose LETTRE PAR LETTRE avec les points.`,
  'z10-p141': `Rubrique ثالثاً: مَظَاهِرُ الْحَيَاءِ. QUESTION PRÉCISE : le mot après الْحَيَاءِ (al-ma...): الْمَمْدُوحِ ou الْمَحْمُودِ ? décompose lettre par lettre (combien de م ?). Puis transcris la ligne.`,
  'z11b-p141': `QUESTION PRÉCISE : dans «وَطَاعَةِ الْوَالِدَيْنِ وَالـ... بِهِمَا» — le mot contesté: وَالْبِرُّ ou وَالْبُرُورُ ? décompose lettre par lettre.`,
  'z12-p141': `Passage «وَلَيْسَ مِنَ الْحَيَاءِ: ...». Transcris TOUT mot à mot (la liste complète des actions qui ne sont pas du hayāʾ: فعل المعاصي و... المحرمات وعدم سؤال أهل العلم فيما ينفع وعدم طلب العلم بدعوى الحياء وترك ... وعدم الكلام فيما ...).`,
  'z13-p141': `Fin du passage: «فَهَذَا لَا يُسَمَّى حَيَاءً شَرْعِيًّا أَوْ هُوَ حَيَاءٌ مَذْمُومٌ...» — transcris TOUT ce qui suit jusqu'à la ligne de séparation, mot à mot (le mot après بَلْ هُوَ خَجَلٌ ... ? décompose le dernier mot lettre par lettre).`,
  'z14b-p142': `Début du 1er item de وَمِمَّا يُسْتَفَادُ: «الْحَيَاءُ سُلْطَةٌ ...». QUESTION PRÉCISE : le mot après سُلْطَةٌ — décompose lettre par lettre (ذَائِيَّةٌ ? رَادِعَةٌ ? دَافِعَةٌ ? وَازِعَةٌ ? autre ?).`,
  'z14-p142': `Les items de وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ. Transcris-les TOUS mot à mot (2 items avec tirets).`,
  'z15b-p142': `Début de la question 3 du تقويم. QUESTION PRÉCISE : les 2 premiers mots (a'... naṣīḥa...): أُعْطِي نَصِيحَةً ? أُقَدِّمُ نَصِيحَةً ? أَعُودُ نَصِيحَةً ? أُبْدِي نَصِيحَةً ? Décompose lettre par lettre.`,
  'z15-p142': `Les questions 2 et 3 du تقويم. Transcris-les mot à mot.`,
  'z16b-p142': `Ligne de l'encadré الاستثمار. QUESTION PRÉCISE : après «إِذَا رَأَتِ الْمَاءَ» — transcris lettre par lettre: فَغَطَّتْ ? فَغَسَلَتْ ? + qui ? أُمُّ سَلَمَةَ ? + تَعْنِي وَجْهَهَا ? Transcris la ligne entière.`,
  'z16-p142': `L'ENCADRÉ DU HADITH (الاستثمار) — Umm Salama / Umm Sulaym. Transcris TOUT mot à mot depuis جَاءَتْ jusqu'à أَوَتَحْتَلِمُ الْمَرْأَةُ.`,
  'z17b-p142': `Fin de l'encadré: قَالَ: نَعَمْ ... QUESTION : تَرِبَتْ يَمِينُكِ (kasra) ou يَمِينُكَ ? + فَبِمَ يُشْبِهُهَا وَلَدُهَا ? décompose lettre par lettre. Transcris la ligne.`,
  'z17-p142': `Les activités numérotées après l'encadré الاستثمار (2 activités). Transcris-les mot à mot.`,
  'z18-p143': `الاِعْدَادُ الْقَبْلِيُّ item 1: «أُشْرِحُ: ...». Transcris les TROIS expressions mot à mot lettre par lettre (elles préparent la leçon 26 sur l'istiqāma: quelque chose comme لَا أَسْأَلُ عَنْهُ أَحَدًا غَيْرَكَ / آمَنْتُ بِاللهِ / اسْتَقِمْ — mais ne complète pas par mémoire : seulement ce qui est imprimé).`,
  'z19-p144': `Bandeau de la leçon SUIVANTE. Transcris le numéro EXACT (chiffres arabes orientaux) et le titre complet lettre par lettre.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of Object.keys(Q)) {
  const out = `${DIR}/vlmz-${k}.txt`;
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1600,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 500 ? txt.slice(0, 400) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(2500);
}
