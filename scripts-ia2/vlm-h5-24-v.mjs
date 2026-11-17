// Z2-28 — zooms V VLM 600 dpi ciblés (points litigieux restants), leçon 24
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-24';
const R600 = `${DIR}/r600`;

const COMMON = `Recadrage haute résolution (600 dpi) d'un manuel scolaire marocain d'hadith, 5e primaire, leçon 24 «حفظ أوامر الله تعالى». Transcris mot à mot avec la vocalisation. Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé. Pour les points marqués ⟵ scrutiné : lis LETTRE PAR LETTRE en comptant les points des lettres.`;

// (page, y0, y1, tag, question)
const Q = [
  [131, 0.780, 0.868, 'A', `Fin de l'encadré du hadith p.131 : la ligne «إلا بشيء قد كتبه الله لك وإنِ اجتمعوا على أن يضروك...» puis «إلا بشيء قد كتبه الله عليك، رفعت الأقلام وجفت الصحف» puis LA RÉFÉRENCE entre crochets ⟵ scrutiné : la référence exacte lettre par lettre — [سنن الترمذي] ou [رواه الترمذي] ou autre ? Décris les premiers mots après le crochet. Donne aussi : وَإِنِ avec kasra ou وَإِنْ avec sukūn ⟵ scruté.`],
  [131, 0.512, 0.566, 'B', `La question de transition sous le تمهيد ⟵ scrutiné : transcris la ligne entière mot à mot — «فما معنى حفظ الله؟ وما ثمرته وعلاقته بالإيمان ب...» — comment se termine-t-elle EXACTEMENT : بِقَدَرِهِ ؟ بِقَدَرِ اللهِ ؟ autre ? Lettre par lettre sur les 3 derniers mots.`],
  [132, 0.380, 0.435, 'C', `Notice de ʿAbd Allāh b. ʿAbbās, 2e-3e lignes ⟵ scruté : «هو ابن عم النبي ﷺ، أحد ... من الصحابة» — le mot après أحد : الْعُلَمَاءُ ou الْأَعْلَامُ ou العَبَادِلَةُ ? Lis lettre par lettre. Puis «مَنَاقِبُهُ أَكْثَرُ مِنْ أَنْ تُحْصَرَ» — confirme mot à mot.`],
  [133, 0.075, 0.240, 'D', `Deux gloses du الشرح : (1) «جَفَّتِ الصُّحُفُ: المراد به أن ما ... الله لا تبديل له إلا بإذنه» ⟵ scrutiné : قَدَّرَ ou قَدَّرَهُ ? (2) «ما أخطأك لم يكن ليصيبك: ما قدر الله أن يخطئك ... يصيبك أبدا» ⟵ scrutiné : لَنْ ou أَنْ devant يصيبك ? Transcris les deux gloses en entier.`],
  [133, 0.538, 0.635, 'E', `Le bandeau/titre décoré entre la rubrique استخلاص المضامين et la phrase «يشتمل حديث الدرس...» ⟵ scrutiné : quel est CE TITRE EXACTEMENT lettre par lettre ? (التَّحْلِيلُ ? التَّطْبِيقُ ? autre ?). Puis transcris la phrase يشتمل حديث الدرس على وصايا... complète jusqu'à نُجْمِلُهَا فِي الْآتِي.`],
  [133, 0.803, 0.860, 'F', `Ligne «مَعْنَاهُ: اعْمَلْ لِلَّهِ بِالطَّاعَةِ، وَلَا ... فِي مُخَالَفَتِهِ» ⟵ scrutiné : le verbe après وَلَا — يَرْكَ ? يَرْكَنَ ? يُرِكْ ? autre ? Lettre par lettre avec les voyelles. Puis la ligne suivante «فَإِنَّكَ تَجِدُهُ ... فِي الشَّدَائِدِ» et «يَحْفَظُكَ بِحِفْظِهِ وَيَرْعَاكَ بِعِنَايَتِهِ» si visible.`],
  [134, 0.232, 0.320, 'G', `Récit des trois hommes dans la grotte, lignes 4-6 ⟵ scruté : «فذكر كل واحد منهم ... مع ربه» (quel mot après سابقة ?) puis le verbe : فَانْفَرَجَتْ ou فَانْفَتَحَتْ ou فَانْحَدَرَتْ — la pierre, lettre par lettre. Puis «فَخَرَجُوا يَمْشُونَ. وَقِصَّتُهُمْ مَشْهُورَةٌ فِي الصَّحِيحَيْنِ».`],
  [134, 0.303, 0.368, 'H', `Ligne «فَمَنْ كَانَ مُطِيعًا لِرَبِّهِ مُؤْتَمِرًا بِأَوَامِرِهِ مُنْتَهِيًا عَنْ نَوَاهِيهِ، كَانَ اللهُ لَهُ فِي دُنْيَاهُ بِ... وَفِي أُخْرَاهُ بِ... وَالرِّضْوَانِ» ⟵ scruté : le mot après دُنْيَاهُ بِ (إِصْلَاحِ + quel nom ?) et le mot après أُخْرَاهُ بِ (الْإِثَابَةِ ? الْإِتَابَةِ ?). Lettre par lettre.`],
  [134, 0.540, 0.628, 'I', `Le passage «...في جميع أموره ما قل منها ...» ⟵ scrutiné : comment continue la ligne après مَا قَلَّ مِنْهَا (وَمَا كَثُرَ ? أَوْ كَثُرَ ?). Puis «قَالَ اللهُ تَعَالَى:» + LE VERSET coranique complet ﴿وَمَنْ يَتَوَكَّلْ عَلَى اللهِ...﴾ ⟵ scruté : jusqu'où va le verset (فَهُوَ حَسْبُهُ ? + إِنَّ اللهَ بَالِغُ أَمْرِهِ ?) et LE CHIFFRE de la référence [الطلاق: ?] lettre par lettre. Puis le début «فَبِقَدْرِ مَا يَرْكَنُ...» si visible.`],
  [134, 0.623, 0.685, 'J', `Ligne «...يكون قد أعرض عن ربه والتجأ إلى ...» ⟵ scruté : la fin de la ligne lettre par lettre — «إلى من لا ...» (لا يَقْدِرُ ? لا يَمْلِكُ ? + لَهُ وَلَا عَلَيْهِ ? + نَفْعًا ?). Transcris toute la ligne.`],
  [134, 0.805, 0.868, 'K', `Verset coranique en bas de page ⟵ scruté : «كَمَا يَسْتَوْجِبُهُ قَوْلُهُ تَعَالَى: ﴿...﴾» — transcris le verset COMPLET mot à mot avec vocalisation + LE CHIFFRE de la référence [غافر: ?] lettre par lettre (١٣ ou ١٤ ?).`],
  [135, 0.272, 0.332, 'L', `Lignes «فِيهِ تَأْكِيدٌ أَنَّ الْإِيمَانَ بِقَضَاءِ اللهِ وَقَدَرِهِ رُكْنٌ أَسَاسِيٌّ مِنْ عَقَائِدِ الْإِيمَانِ، الَّتِي تُثْمِرُ أَنْ لَا يَخَافَ الْمُؤْمِنُ وَلَا ...» ⟵ scruté : le verbe après وَلَا (يَسْأَلَ ? يَرْجُوَ ? يَرْغَبَ ? يَخَافَ مِنْ ?) + «لِأَنَّهُ مُتَيَقِّنٌ أَنَّهُ لَا يَنَالَهُ نَفْعٌ أَوْ ضُرٌّ إِلَّا بِقَضَاءِ اللهِ». Lettre par lettre sur le verbe.`],
  [135, 0.348, 0.405, 'M', `Ligne «فَلَوِ اجْتَمَعَتِ الْأُمَّةُ عَلَى أَنْ تَنْفَعَكَ أَوْ تَضُرَّكَ ...» ⟵ scruté : les mots entre تَضُرَّكَ et إِلَّا بِإِذْنِ اللهِ (مَا قَدَّرَتْ ? لَمْ تَقْدِرْ ? مَا قَدَّرَ اللهُ ?) lettre par lettre. Transcris la ligne complète.`],
  [135, 0.408, 0.478, 'N', `Lignes «وَالْإِيمَانُ بِقَضَاءِ اللهِ وَقَدَرِهِ يُثْمِرُ عَدَمَ تَعَلُّقِ الْإِنْسَانِ بِغَيْرِهِ سُبْحَانَهُ، لِأَنَّهُ هُوَ الْفَاعِلُ فِي الْحَقِيقَةِ؛ فَالْكُلُّ بِقَدَرِهِ وَقَضَائِهِ الَّذِي يَجِبُ الرِّضَا بِهِ وَالتَّسْلِيمُ لَهُ» ⟵ scrutiné : y a-t-il d'autres mots ? سُبْحَانَهُ est-il bien là ? Transcris tout mot à mot.`],
  [136, 0.035, 0.238, 'O', `Bloc coranique ornementé en haut de page ⟵ scrutiné : (1) la FIN de la citation ﴿...صَلَوَاتٌ مِنْ رَبِّهِمْ وَرَحْمَةٌ وَأُولَئِكَ هُمُ الْمُهْتَدُونَ﴾ ; (2) LA RÉFÉRENCE [البقرة: ?-?] — les DEUX chiffres lettre par lettre ; (3) «وَقَوْلُهُ تَعَالَى:» + le DEUXIÈME verset complet ﴿إنما يوفى الصابرون...﴾ mot à mot ; (4) sa référence [الزمر: ?] — LE CHIFFRE lettre par lettre.`],
  [136, 0.256, 0.342, 'P', `Premier item de «ومما يستفاد من الحديث» ⟵ scruté : «الْيَقِينُ بِأَنَّ الْإِنْسَانَ لَنْ يَفُوتَهُ مَا قُدِّرَ لَهُ، وَأَنَّهُ لَنْ ... مَا لَمْ يُقَدَّرْ لَهُ، فَ... فِي الطَّلَبِ» — le verbe après فَ (فَلْيَجْمُلَ ? فَلْيَجْزَعْ ? فَلَا يُعْجِلَ ? فَلْيَتَّكِلْ ?) LETTRE PAR LETTRE, puis «كَمَا فِي وَصِيَّةِ لُقْمَانَ لِابْنِهِ: ﴿يَا بُنَيَّ إِنَّهَا إِنْ تَكُ مِثْقَالَ حَبَّةٍ مِنْ خَرْدَلٍ...﴾» — confirme le début du verset.`],
  [136, 0.378, 0.448, 'Q', `Fin du verset de Luqmān ⟵ scruté : «فَتَكُنْ فِي صَخْرَةٍ أَوْ فِي السَّمَاوَاتِ أَوْ فِي الْأَرْضِ يَأْتِ بِهَا اللهُ إِنَّ اللهَ لَطِيفٌ خَبِيرٌ» + LA RÉFÉRENCE [لقمان: ?] — LE CHIFFRE lettre par lettre (١٥ ou ١٦ ?).`],
  [136, 0.745, 0.855, 'R', `Rubrique تقويم questions 2-3 ⟵ scrutiné : (2) «أُبَيِّنُ كَيْفِيَّةَ التَّعَلُّقِ بِاللهِ.» ; (3) la question 3 COMPLÈTE : «أُبَيِّنُ مَعْنَى: «واعلم أن الأمة لو اجتمعت على أن ينفعوك بشيء لم ينفعوك إلا بشيء قد كتبه الله لك»، وَ...» — la fin exacte lettre par lettre (وَبَيْنَ تَفَاعُلِ النَّاسِ بَعْضِهِمْ مَعَ بَعْضٍ ? وَبَيْنَ نَفْعِ النَّاسِ بَعْضِهِمْ بَعْضًا ?).`],
  [137, 0.052, 0.188, 'S', `Encadré coranique ornementé de l'استثمار, partie 1 (haut) ⟵ scrutiné : y a-t-il une ligne d'intro «يَقُولُ اللهُ عَزَّ وَجَلَّ:» ? Puis les PREMIERS versets mot à mot — par quoi commence la citation ? (﴿وَكَذَلِكَ نُرِي إِبْرَاهِيمَ مَلَكُوتَ السَّمَاوَاتِ وَالْأَرْضِ...﴾ ? ﴿فَلَمَّا رَأَى الْقَمَرَ بَازِغًا...﴾ ? ﴿وَحَاجَّهُ قَوْمُهُ...﴾ ?). Transcris ce que tu vois.`],
  [137, 0.175, 0.325, 'T', `Encadré coranique ornementé, partie 2 (milieu) ⟵ scrutiné : transcris les versets visibles mot à mot avec vocalisation (attention : écriture coranique ornée —décris les lettres si doute).`],
  [137, 0.312, 0.468, 'U', `Encadré coranique ornementé, partie 3 (bas) ⟵ scrutiné : transcris les derniers versets (﴿وَتِلْكَ حُجَّتُنَا آتَيْنَاهَا إِبْرَاهِيمَ عَلَى قَوْمِهِ...﴾ ? ﴿...وَهُمُ الْمُهْتَدُونَ﴾ ?) + LA RÉFÉRENCE entre crochets [الأنعام: ?-?] — les DEUX chiffres lettre par lettre.`],
  [137, 0.750, 0.892, 'V', `Rubrique الإعداد القبلي ⟵ scruté : (1) la ligne-titre «أَحْفَظُ حَدِيثَ الدَّرْسِ الْآتِيَ وَأَقُومُ بِمَا يَلِي:» ; (2) l'item 1 EXACT : «أُشْرِحُ: كَلَامَ النُّبُوَّةِ الْأُولَى، ...» — y a-t-il إِذَا avant لَمْ تَسْتَحْيِ ? lettre par lettre + la ponctuation ; (3) l'item 2 : «أُبَيِّنُ فَضْلَ الْحَيَاءِ وَمَظَاهِرَ الْحَيَاءِ.» — mot à mot (الْحَيَاءِ deux fois ? ou وَمَظَاهِرَهُ ?).`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const [page, y0, y1, tag, question] of Q) {
  const out = `${DIR}/vlm24-V-${tag}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${tag}`); continue; }
  const png = `${DIR}/v24-${tag}.png`;
  if (!fs.existsSync(png)) {
    execSync(`python3 -c "from PIL import Image; im=Image.open('${R600}/p${page}.png'); w,h=im.size; im.crop((int(0.02*w),int(${y0}*h),int(0.98*w),int(${y1}*h))).save('${png}')"`);
  }
  const img = fs.readFileSync(png).toString('base64');
  console.log(`\n======== ${tag} p${page} y[${y0}-${y1}] ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + question },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1600,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 700 ? txt.slice(0, 350) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${tag} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(3000);
}
