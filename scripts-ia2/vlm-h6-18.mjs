// IA-2 — vlm-h6-18.mjs : ronde VLM 1 — zones critiques L18 (pp.100-104), transcription lettre à lettre.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();

const PRE = `Tu lis un crop haute résolution (2400 dpi) du manuel marocain de hadith (6e année, التعليم العتيق). Transcris l'arabe EXACTEMENT tel qu'imprimé, avec la vocalisation complète et la ponctuation (، ؛ . ؟ « »). Attention aux points des lettres (ب/ت/ث، ج/ح/خ، د/ذ، ر/ز، س/ش، ص/ض، ط/ظ، ع/غ، ف/ق). Ne devine pas : si une lettre est douteuse, note-la entre crochets. Réponds en arabe uniquement.`;

const QS = [
  ["z3-p100-tamhid-vlm", `Ligne courte isolée sous le تمهيد, avant la ligne «فما هذه الأعمال الفاضلة؟...». Transcris-la en entier. Le DERNIER mot se termine par ـه : est-ce بُغْيَتَهُ (ghayn pointé) ? بُعَيْنَهُ ? بُغْيَنَهُ ? Décris les points de la 2e lettre.`],
  ["z3-p100-hadith-vlm", `Zone entre la ligne-question et le début du hadith. Y a-t-il un titre de section «الحديث» ? Transcris-le tel quel (avec son encadrement éventuel). Puis transcris la première ligne du hadith (sanad) : commence-t-elle par «عن أبي هريرة رضي الله عنه» ? La suite dit «عن النبي ﷺ قال» ou «أن النبي ﷺ قال» ? Transcris aussi la 2e ligne (كربة من كرب...) avec SA PONCTUATION exacte après القيامة (، ou . ou rien).`],
  ["z3-p100-matn-awn-vlm", `Deux lignes du matn : «ومن سلك طريقا يلتمس فيه علما...» et la suivante. Transcris-les avec la ponctuation exacte. Vérifie : يَلْتَمِسُ (sīn final) et la séquence «...في عون أخيه ؛ ومن سلك» — y a-t-il un guillemet » après أخيه ou un point-virgule ؟`],
  ["z3-p101-gloses-vlm", `Zone du manuel après «ترجمة الراوي : تقدمت ترجمة الراوي في الدرس الرابع». Transcris le titre «الشرح :» puis TOUTES les gloses ligne par ligne (format : MOT : définition). Il y en a probablement 2 à 4 (ex. كربة : شدة). Transcris aussi ce qui suit : le titre de section suivant (الاستخلاص ?) et ses deux questions numérotées, avec leur vocalisation exacte.`],
  ["z3-p101-intro-vlm", `Une ligne : «...هذا الحديث مجموعة من الأعمال الفاضلة ينبغي للمسلم...». Transcris-la en entier. Le mot après ينبغي للمسلم : إِدْرَاكُ (dāl sans point) ou إِذْرَاكُ ? Le premier mot : يَتَضَمَّنُ ou يَتَصَمَنُ ? Décris les points.`],
  ["z3-p101-ragabba2-vlm", `Une ligne : «رَغَّبَ النبي ﷺ في ... الناس وبذل النفع إليهم والإحسان إليهم، ومن مظاهر ذلك:». Transcris-la en entier. Le passage après «في» et avant «الناس» : «الإكثار من الإحسان إلى» ? autre ? Transcris mot par mot.`],
  ["z3-p102-saa-vlm", `Une ligne : «...أو ينظر إلى ساعة ... بتأجيل الأجل له ونحو ذلك؛ قال الله تعالى: (وإن كان ذو عسرة...». Transcris le début exact : «إلى ساعة X» — X = الْيُسْرِ ? يُسْرِهِ ? لَيْسَرَتِهِ ? لِيُسْرِهِ ? Décris les lettres de X une par une (avec leurs points).`],
  ["z3-p102-aya-vlm", `Ligne de verset coranique entre parenthèses + référence entre crochets. Transcris le verset ET la référence chiffre par chiffre : [البقرة : N N N] — les chiffres sont-ils ٢٧٩ ou ٢٨٠ ? Décris chaque chiffre arabe-indien.`],
  ["z3-p102-item4-vlm", `Une ligne : «4- عون المسلم لأخيه؛ وذلك بأن ... بما يمكن من المساعدة إذا احتاج إليه». Transcris le passage entre «بأن» et «بما» MOT PAR MOT avec les points de chaque lettre. Est-ce «لا عنه» (lām-alif puis ʿayn-nūn-hāʾ) ? «يُعِينَهُ» ? «يُبْخَلَ عنه» ? autre ? Décris précisément la 1re lettre : lām ou yāʾ (points en dessous ?).`],
  ["z3-p102-zumar2-vlm", `Ligne : verset «...قال الله تعالى: (قل هل يستوي الذين يعلمون والذين لا يعلمون) [الزمر : N]». Transcris le verset entier avec son début (قُلْ ?) ET la référence chiffre par chiffre : ٩ ou ١٠ ou autre ?`],
  ["z3-p102-jabir-vlm", `Ligne de hadith : «فعن جابر رضي الله عنهما أن رسول الله ﷺ قال: «رحم الله رجلا سمحا إذا باع... وإذا اشترى وإذا اقتضى». Transcris-la avec la PONCTUATION exacte entre les clauses (، ؛ ou rien après باع et بعد اشترى).`],
  ["z3-p102-yusr-vlm", `Deux lignes : «فمن يسر في معاملاته مع الناس يسر الله عليه في الدنيا والآخرة؛ وحصلت له بركة دعاء النبي صلى الله عليه وسلم؛ / فقد دعا عليه السلام بالرحمة لمن يعامل الناس بال...». Transcris les deux lignes. Le dernier mot de la 2e ligne : وَالسَّمَاحَةِ ? وَالسَّمَاحَ ? Décris sa fin (ة ou rien).`],
  ["z3-p103-hafoof-vlm", `Deux items d'une liste. Transcris-les : «- ... الملائكة للمجتمعين؛ وذلك دليل على أفضلية وخيرية هذا المجلس. / - ذكر الله لهم في الملأ الأعلى؛ تكريما لمثل هذه المجالس وتشريفا لها.» Le premier mot du 1er item : حَفُّ (fāʾ shadda) ou حُفُوفٌ ou حِفَافٌ ? Décris la racine lettre par lettre.`],
  ["z3-p103-manas-vlm", `Une ligne : «ومعنى قوله ﷺ: «ومن بطأ به عمله لم يسرع به نسبه» أن من أخر عمله X أو تفريطا وتقصيرا...». Transcris le passage de «أن من أخر عمله» jusqu'à «نسبه» MOT PAR MOT. Le X : تَسْوِيفًا ? تَرْيِيثًا ? تَهَاوُنًا ? autre ? Décris ses lettres avec leurs points.`],
  ["z3-p104-table-vlm", `TABLEAU d'exercice (تقويم 3 : أستثمر تعلماتي وأملأ الجدول في دفتري بما يناسب). Décris sa structure : combien de colonnes, quels en-têtes (transcris-les exactement), combien de rangées, et transcris TOUT le contenu visible de chaque case. Une case est-elle vide (à remplir par l'élève) ?`],
  ["z3-p104-istithmar-vlm", `Zone استثمار : «شخص يظن أن المال وحده مصدر السعادة فيستهين بـ...». Transcris le passage en entier : que suit «فيستهين» (بـ + quel mot) ? Y a-t-il un titre «الاستثمار» au-dessus ? Transcris tout ce qui est visible.`],
  ["z3-p104-aya-vlm", `Zone : verset coranique dans un encadré + référence + question «كيف أوافق بين مدلول هذه الآية ومدلول قوله ﷺ: «ومن بطأ به عمله لم يسرع به نسبه»؟». Transcris le verset EN ENTIER lettre par lettre, la référence [الطور : N] ou autre sourate (décris le nom de la sourate et le chiffre), et la question complète.`],
  ["z3-p104-idad-vlm", `Zone إعداد قبلي : «أحفظ حديث الدرس الموالي وأبين سبب مضاعفة الحسنة إلى عشر وإلى ...». Transcris le passage entier : le mot après «وإلى» : سَبْعِمِائَةٍ ? سَبْعِمِئَةٍ ? و la fin «أضعاف كثيرة». Transcris le titre «الإعداد القبلي» s'il est visible.`],
];

for (const [name, q] of QS) {
  const png = `${DIR}/${name}.png`;
  const out = `${DIR}/vlm-h6-18-${name.replace('z3-', '')}.txt`;
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1200,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(`=== ${name} ===\n` + txt.slice(0, 800) + '\n');
      done = true;
    } catch (e) { console.log(`${name} tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm-h6-18');
