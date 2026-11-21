// Z2-48 — adjudication VLM des 19 crops ciblés L12 «لا ضرر ولا ضرار» (docId 692).
// Questions spécifiques par zone, méthode Z2-45/46/47.
import ZAI from '/tmp/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-13/crops';
const OUTDIR = '/home/z/my-project/scripts-ia2/tmp/h6-13/vlm-crops';
fs.mkdirSync(OUTDIR, { recursive: true });

const BASE = `Image : extrait d'une page d'un manuel scolaire marocain de hadith (6e année, Arba'īn nawawiyya + commentaire d'Ibn Daqīq al-'Īd), 1200 dpi. Transcris le texte arabe visible MOT À MOT avec sa voyellisation imprimée, dans l'ordre droite→gauche. Ne devine jamais : illisible → [؟]. Tout chiffre → NUM: <0-9> chiffre par chiffre. ATTENTION ض (point dessus) ≠ ص ≠ د ; ر ≠ ز ; ق (boucle haute) ≠ ف (boucle avec point). Après la transcription, réponds aux QUESTIONS en citant les lettres que tu vois.`;

const QS = {
  'c01-objectifs': `QUESTIONS : 1) Transcris les 3 objectifs numérotés ENTIERS. 2) Objectif 1 : «أن أتعرف» ou «أنّ تعرف» ? Y a-t-il un alef après «أن» (أَنْ أَتَعَرِّفَ) ou pas ? 3) Objectif 2 : «أُمَيِّز» (shadda sur le ya) ou «أَمِيز» ? 4) Objectif 3 : après «أن» vient «أستشعر خطورة» ou «أستنتج حكم» ?`,
  'c02-tamhid': `QUESTIONS : 1) Transcris le bandeau calligraphié du haut (titre de section). 2) Ligne 1 : «جاء الإسلام ليرفع ...» : le mot après «ليرفع» est-il «الشرَّ» (shin-râ') ou «الضررَ» (dâd-râ'-râ') ? CRUCIAL. 3) Transcris la ligne 2 «... كان من مبادئه التيسير ورفع الحرج ومن قواعده رفع الضرر والضرار» exactement. 4) Transcris les 3 questions «فما حكم...؟ وما معنى...؟ وما مظاهرهما في...؟» : le dernier mot de la 3e question exactement. 5) Y a-t-il un médaillon/bandeau «الحديث» visible en bas de l'extrait ?`,
  'c03-hadith-takh': `QUESTIONS : 1) Transcris la chaîne du hadith «عن أبي سعيد سعد بن مالك بن سنان الخدري...» + le texte «لا ضرر ولا ضرار» ENTIERS avec voyelles. 2) Transcris le takhrij entre crochets EN ENTIER mot à mot : après «رواه ابن ماجه والدارقطني وغيرهما» vient «مسندا» ou «مستندا» ? lettre par lettre. 3) La fin du takhrij : «وله طرق يقرر بعضها بعضا» ou «يقوي» ? lettre par lettre (ق-ر-ر ou ق-و-ي). 4) Comment est imprimé «فأسقط أبا سعيد» ?`,
  'c04-tarjama': `QUESTIONS : 1) Transcris la notice ENTIÈRE. 2) Après «أبو سعيد الخدري رضي الله عنه» y a-t-il «هو:» ? 3) La chaîne : «سعد بن مالك بن سنان» — «سنان» exactement ? 4) Le mot après «الأنصاري» : «الخزرجي» ? 5) Le nombre de hadiths : NUM: chiffre par chiffre. 6) L'année de décès entre guillemets : NUM:. 7) «توفي بالمدينة سنة...» ou «توفي بالمدينة سنة:» ?`,
  'c05-sharh': `QUESTIONS : 1) Transcris le titre du bandeau (الشرح ?). 2) Entrée 1 : «ضرر: ...» entière. 3) Entrée 2 : «ضرار: ...» entière — le dernier mot est-il «مُجَارَاةً» (râ') ou «مُجَازَاةً» (zay) ? CRUCIAL — regarde la lettre : ر ou ز ?`,
  'c06-intro-tahlil': `QUESTIONS : 1) Transcris la ligne d'introduction du التحليل : «يت... هذا الدرس على ما يأتي:» — le verbe exactement : «يتضمن» (dâd-mîm-nûn) ou «يتشمل» (shîn-mîm-lâm) ou autre ? CRUCIAL lettre par lettre. 2) Transcris «أولا: تعريف الضرر والضرار» exactement. 3) Y a-t-il un bandeau «التحليل» au-dessus ?`,
  'c07-glose': `QUESTIONS : 1) Transcris «الضرر: أن تضر من لا يضرك. والضرار: أن تضر من أضر بك من غير جهة ...» : le mot après «جهة» est-il «الاعتداء» ('ayn-tâ'-dâl) ou «الاغتداء» (ghayn-tâ'-dâl) ou «الاغتذاء» (ghayn-dhâl) ? CRUCIAL lettre par lettre. 2) Transcris «وهذا نحو قوله ﷺ: أد الأمانة إلى من ائتمنك ولا تخن من خانك» + la référence entre crochets. 3) Transcris la phrase qui suit la référence («وهذا معناه عند...») jusqu'en bas de l'extrait.`,
  'c08-waqil': `QUESTIONS : 1) Transcris «وقيل: الضرر والضرار لفظان بمعنى واحد جاءا معا على وجه التأكيد» exactement. 2) «فمعنى لا ضرر ولا ضرار: لا يدخل أحد على أحد ضررا» — le mot à la fin : «ضررا» ou «ضررا» avec shadda (ضَرَّراً) ? regarde la shadda au-dessus du râ'. 3) «أي لا ينزل به ضررا» : même question (shadda ?). 4) «لا يدخل» : jussif (لا يُدْخِلْ) sans sukûn marqué ou autre ?`,
  'c09-ya-ibadi': `QUESTIONS : 1) Transcris «ومن أضر بأخيه فقد ظلمه والظلم حرام كما تقدم في حديث أبي ذر» exactement. 2) Transcris le hadith qudsi «يا عبادي إني حرمت الظلم على نفسي وجعلته بينكم محرما فلا تظالموا...» : «جعلته» ou «جعله» ? 3) Transcris «وكما قال النبي ﷺ: إن دماءكم وأموالكم وأعراضكم عليكم حرام» + la référence entre crochets EN ENTIER.`,
  'c10-thaniya': `QUESTIONS : 1) Transcris «ثانيا: الأمر برفع الضرر والضرار». 2) Transcris «الحديث خبر معناه النهي عن الضرر والضرار والأمر برفعهما بعد وقوعهما أي لا يحصل من المرء ضرر ولا إضرار ولا إيقاع...» : la fin exacte — «ولا إيقاع لهما» (avec lâm) ou «ولا إيقاعهما» (sans lâm) ? CRUCIAL.`,
  'c11-yadullu': `QUESTIONS : 1) Transcris «والحديث يدل على وجوب حرص المسلم على ألا يحصل منه ضرر ولا ضرار لغيره وعلى رفع الضرر عند العلم به...» puis la suite immédiate : commence-t-elle par «والضرار بالوقوف عند الحق فيه» ou «ودفع الضرر بالوقوف» ou autre ? CRUCIAL mot à mot. 2) Transcris «وظاهره تحريم جميع أنواع الضرر ما قل منه أو كثر». 3) «وقد بني على هذا الحديث قاعدة من القواعد الشرعية الكبرى وهي الضرر يزال» : «قاعدة» avec qâf ou «فاعدة» avec fâ' ? CRUCIAL. 4) Transcris «والضرر لفظ عام يشمل كل ما فيه ضرر على الإنسان في نفسه أو بدنه أو ماله أو عرضه أو بيئته أو علاقته بغيره» exactement.`,
  'c12-yustafad': `QUESTIONS : 1) Transcris le bandeau «مما يستفاد من هذا الحديث». 2) Item 1 entier : «تحريم جميع أنواع الإضرار إلا بالحق ووجوب رفع الضرر والضرار» ? 3) Item 2 entier — la fin : «وتفاعل الغير» ou «ونفع الغير» ? CRUCIAL : après «والتعاون» vient «ونفع» (nûn-fâ'-'ayn) ou «وتفاعل» (tâ'-fâ'-'ayn-lâm) ?`,
  'c13-tab-haut': `QUESTIONS : 1) Transcris le titre du bandeau coloré du haut s'il y en a un. 2) Décris la structure du tableau : combien de colonnes, quels en-têtes (حق النفس / حق الغير / حق البيئة ?). 3) Transcris TOUTES les cellules du tableau mot à mot, rangée par rangée, cellule par cellule, en précisant la colonne de chaque cellule. 4) Certaines cellules sont-elles vides (à remplir par l'élève) ?`,
  'c14-items-123': `QUESTIONS : 1) Transcris l'item 1 : «أبين الفرق بين الضرر والضرار» — «أبين» avec fatha (أَبَيِّنُ) ou damma (أُبَيِّنُ) ? 2) Transcris l'item 2 ENTIER : «أمثل بأمثلة لرفع الضرر من واقعي» — «أمثل» ou «أمثل» : la voyelle du mîm ? Et la fin «من واقعي» exactement ? 3) Transcris l'item 3 ENTIER.`,
  'c15-tab-bas': `QUESTIONS : 1) Décris la structure du tableau : en-têtes de colonnes exacts (السلوك / صحيح ou خطأ / التعليل ?). 2) Transcris TOUTES les rangées de la première colonne mot à mot (il y en a peut-être 4 ou 5 : إيذاء الجيران ? تناول المخدرات ? احترام قانون السير ? رحمة الحيوان في الشارع ? autre chose comme رمي...?). 3) Les autres colonnes sont-elles vides ? 4) La rangée 4 ou 5 : «رحمة» + quoi exactement («الحيوان» ou «الأنجاب» ou autre) ? lettre par lettre.`,
  'c16-verset': `QUESTIONS : 1) Transcris la citation coranique ENTIÈRE mot à mot avec sa voyellisation (c'est an-Nisāʾ 29 : يَا أَيُّهَا الَّذِينَ آمَنُوا لَا تَأْكُلُوا أَمْوَالَكُمْ بَيْنَكُمْ بِالْبَاطِلِ إِلَّا أَنْ تَكُونَ تِجَارَةً عَنْ تَرَاضٍ مِنْكُمْ وَلَا تَقْتُلُوا أَنْفُسَكُمْ إِنَّ اللَّهَ كَانَ بِكُمْ رَحِيمًا). 2) Y a-t-il des médaillons de fin de verset ۝ ? Combien ? 3) Transcris la référence entre crochets [النساء: NUM:]. 4) La citation commence par «قال الله تعالى:» ?`,
  'c17-hadiths': `QUESTIONS : 1) Transcris «وقال ﷺ: أد الأمانة إلى من ائتمنك ولا تخن من خانك» + sa référence [سنن الترمذي...] : le numéro du باب = NUM:. 2) Transcris le hadith «اتقوا ... الثلاث: البراز في الموارد وقارعة الطريق والظل» EN ENTIER — le mot après «اتقوا» exactement lettre par lettre («اللعنين» ? «الملاعن» ? «اللاعنات» ?) et «الثلاث» ou «الثلاثة» ? 3) Transcris sa référence [أخرجه أبو داود...] ENTIÈRE avec le numéro = NUM:. 4) Le dernier mot du 2e hadith : «والظل» exactement ?`,
  'c18-item-enr': `QUESTIONS : 1) Transcris l'item entier : «أتأمل النصوص وأستخرج منها صورا للضرر المحرم وأميز منها ما هو حق للنفس وما هو حق للغير» — vérifie : «للضرر المحرم» ou «للضرر المحرم» ? et «وأميز» ou «وأميز» (damma sur le waw ?) ? 2) La ligne commence par quoi exactement ?`,
  'c19-iidad': `QUESTIONS : 1) Transcris le bandeau titre (الإعداد القبلي ?). 2) Transcris l'item EN ENTIER : «أحفظ حديث الدرس الموالى وأبين معنى: البينة على المدعي واليمين على من أنكر». 3) Le premier mot : «أحفظ» avec fatha ou damma ?`,
};

const TASKS = Object.keys(QS);

async function readOne(zai, tag) {
  const out = `${OUTDIR}/${tag}.txt`;
  if (fs.existsSync(out) && fs.statSync(out).size > 100) return `${tag}: déjà lu`;
  for (let k = 1; k <= 4; k++) {
    try {
      const b64 = fs.readFileSync(`${DIR}/${tag}.png`).toString('base64');
      const res = await zai.chat.completions.createVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: `${BASE}\n\n${QS[tag]}` },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
          ] }],
        thinking: { type: 'disabled' },
      });
      const txt = res.choices[0]?.message?.content || '(vide)';
      fs.writeFileSync(out, txt, 'utf-8');
      return `${tag}: OK (${txt.length} car)`;
    } catch (e) {
      const msg = String(e?.message || e);
      if (k === 4) { fs.writeFileSync(out, `ERREUR ${msg}`, 'utf-8'); return `${tag}: ERREUR ${msg.slice(0, 80)}`; }
      const wait = msg.includes('429') ? 20000 * k : 5000 * k;
      await new Promise(r => setTimeout(r, wait));
    }
  }
}

async function main() {
  const zai = await ZAI.create();
  for (const t of TASKS) console.log(await readOne(zai, t));
}
main().catch(e => { console.error('FATAL', e); process.exit(1); });
