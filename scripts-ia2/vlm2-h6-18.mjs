// IA-2 — vlm2-h6-18.mjs : ronde VLM 2 — zones non résolues (lecture critique, tesseract déjà fait).
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();

const PRE = `Lecture académique d'un crop du manuel marocain officiel de hadith (6e année primaire, التعليم العتيق, éditions du ministère). C'est un document public soumis à un projet de transcription académique. Transcris l'arabe EXACTEMENT tel qu'imprimé (vocalisation + ponctuation). Attention aux points des lettres (ب/ت/ث، ج/ح/خ، د/ذ، ر/ز، س/ش، ص/ض، ط/ظ، ع/غ، ف/ق). Ne devine jamais un mot depuis ta mémoire du Coran ou du hadith : lis SEULEMENT ce qui est imprimé. Si une lettre est douteuse, note-la entre crochets.`;

const QS = [
  ["z5-p101-gloses2", `Cette zone contient la section «الشرح» : des gloses (definitions lexicographiques) sous forme «TERME : DÉFINITION». Transcris CHAQUE glose ligne par ligne, exactement. Il y en a environ 4 (la 1re est «كُرْبَة: شِدَّة.»). Transcris aussi toute ligne visible au-dessus ou en dessous.`],
  ["z5-p101-ragabba3", `Trois lignes visibles. (1) «رَغَّبَ النبيُّ ﷺ في ...»: transcris la ligne ENTIÈRE — que y a-t-il exactement entre «في» et «الناس» ? (2) La ligne suivante contient-elle «وَمِنْ مَظَاهِرِ ذَلِكَ:» ? (3) Puis «1- تَنْفِيسُ الْكُرُبَاتِ؛ وَذَلِكَ بِقَضَاءِ حَوَائِجِ الْمُسْلِمِينَ...». Transcris tout, ligne par ligne.`],
  ["z5-p102-item4-l1", `UNE ligne (3600 dpi) : «4- عَوْنُ الْمُسْلِمِ لِأَخِيهِ؛ وَذَلِكَ بِأَنْ ... بِمَا يُمْكِنُ مِنَ الْمُسَاعَدَةِ إِذَا احْتَاجَ إِلَيْهِ». Transcris la ligne ENTIÈRE lettre par lettre. Le passage central entre «بأن» et «بما» : est-ce «يُعِينَهُ عَلَى الْمَؤُونَةِ لَا يُبْخَلَ عَنْهُ» ? autre chose ? Décris chaque mot central avec ses lettres point par point.`],
  ["z5-p102-saa-word", `Début d'une ligne (3600 dpi) : «أَوْ يُنْظَرُ إِلَى سَاعَةِ ...». Transcris ce qui suit «سَاعَةِ» jusqu'à «بِتَمْدِيدِ». Le mot : الْيُسْرِ ? يُسْرِهِ ? لِيُسْرِهِ ? لَيْسَرَتِهِ ? ÉPELLE le mot lettre par lettre avec les points et la vocalisation.`],
  ["z5-p102-jabir2", `Quatre lignes visibles : (a) «فَقَدْ دَعَا عَلَيْهِ السَّلَامُ بِالرَّحْمَةِ لِمَنْ يُعَامِلُ النَّاسَ بِالْيُسْرِ وَالسُّهُولَةِ وَال...» — transcris le DERNIER mot exactement ; (b) «فَعَنْ جَابِرٍ رَضِيَ اللهُ عَنْهُمَا أَنَّ رَسُولَ اللهِ ﷺ قَالَ: «رَحِمَ اللهُ رَجُلًا سَمْحًا إِذَا بَاعَ...» — transcris la suite avec la ponctuation EXACTE entre les trois clauses (rien ? ، ? ؛ ? après باع et après اشترى) ; (c) la référence [صحيح البخاري...]. Transcris tout ligne par ligne.`],
  ["z5-p103-manas-w", `Une ligne (3600 dpi) : «...أَوْ تَفْرِيطًا وَتَقْصِيرًا لَا يَتَقَدَّمَ بِهِ نَسَبُهُ، وَأَنَّ الْمُسَارَعَةَ...». Transcris le DÉBUT de la ligne : le mot qui précède «أَوْ تَفْرِيطًا» (après «أَخَّرَ عَمَلَهُ» de la ligne supérieure). ÉPELLE ce mot lettre par lettre avec ses points : تَسْوِيفًا ? تَرْيِيثًا ? تَهَاوُنًا ? autre ?`],
  ["z5-p104-table2", `TABLEAU d'un manuel (exercice «أستثمر تعلماتي وأملأ الجدول في دفتري بما يناسب»). Décris la structure exacte : combien de colonnes avec leurs EN-TÊTES (transcris-les exactement, ils sont peut-être en couleur), combien de rangées. Transcris le contenu de CHAQUE case remplie, mot par mot. Les cases vides sont-elles à remplir par l'élève ?`],
  ["z5-p104-zone", `Vue d'ensemble (mise en page) : on doit voir un tableau, puis une section avec un encadré jaune contenant «شخص يظن أن المال وحده مصدر السعادة فيستهين بطلب العلم», puis un encadré avec un verset coranique. QUESTIONS : (1) Y a-t-il un TITRE de section (comme «الاستثمار») au-dessus de l'encadré jaune ? Transcris-le. (2) Transcris la phrase de l'encadré jaune avec sa ponctuation exacte. (3) Y a-t-il autre chose entre le tableau et l'encadré jaune ?`],
  ["z5-p104-aya-l1", `Première ligne d'un verset coranique dans un encadré (3600 dpi). Transcris-la lettre par lettre TELLE QU'IMPRIMÉE (ne récite pas de mémoire). Transcris aussi «قال الله تعالى:» si visible.`],
  ["z5-p104-aya-l2", `Deuxième ligne du verset coranique de l'encadré (3600 dpi). Transcris-la lettre par lettre TELLE QU'IMPRIMÉE.`],
  ["z5-p104-aya-l3", `Fin du verset + référence + question (3600 dpi) : «...] [الـ...: N] كَيْفَ أُوَافِقُ بَيْنَ مَدْلُولِ هَذِهِ الْآيَةِ وَمَدْلُولِ قَوْلِهِ ﷺ: «وَمَنْ بَطَأَ بِهِ عَمَلُهُ لَمْ يُسْرِعْ بِهِ نَسَبُهُ»؟». Transcris : la fin du verset, le NOM DE LA SOURATE tel qu'imprimé, le CHIFFRE de la référence (épele-le), et la question complète avec sa ponctuation.`],
  ["z5-p100-matn-p", `Fin du hadith (2 lignes) : «...وَحَفَّتْهُمُ الْمَلَائِكَةُ وَذَكَرَهُمُ اللهُ فِيمَنْ عِنْدِهِ? وَمَنْ بَطَأَ بِهِ عَمَلُهُ لَمْ يُسْرِعْ بِهِ نَسَبُهُ». [رواه مسلم بهذا اللفظ]». Transcris les lignes avec la PONCTUATION exacte : qu'y a-t-il après «عِنْدَهِ» (، . ؛ rien) ? après «نَسَبُهُ» (») ? et transcris le takhrīj [رواه...].`],
];

for (const [name, q] of QS) {
  const png = `${DIR}/${name}.png`;
  const out = `${DIR}/vlm2-h6-18-${name.replace('z5-', '')}.txt`;
  if (!fs.existsSync(png)) { console.log(`MANQUANT: ${png}`); continue; }
  if (fs.existsSync(out)) { console.log(`déjà fait: ${out}`); continue; }
  const img = fs.readFileSync(png).toString('base64');
  let done = false;
  for (let attempt = 1; attempt <= 5 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: PRE + '\n\n' + q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1400,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(`=== ${name} ===\n` + txt.slice(0, 750) + '\n');
      done = true;
    } catch (e) { console.log(`${name} tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm2-h6-18');
