// IA-2 — vlm-h6-17.mjs : passes VLM (glm-5v-turbo) sur les zones non tranchées
// de L17 «الأخوة الإسلامية» (تتمة) pp.95-99. Scrutins mot à mot.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();

const JOBS = [
  { id: 'v1-cartouche', img: 'z4-p95-cart-vlm.png',
    q: `Cartouche d'en-tête d'une leçon de manuel scolaire marocain (1200 dpi, couleur : fond bleu, texte blanc). Transcris-le en entier. SCRUTIN 1 : le numéro du «الدرس» — quels chiffres exacts sont imprimés et en quels glyphes (arabo-indiens ٠-٩ ou occidentaux) ? SCRUTIN 2 : le titre — est-ce «الأخوة الإسلامية» suivi de «(تتمة)» ? Les parenthèses sont-elles imprimées ? Décris précisément la zone du numéro (sous «الدرس») et le second mot du titre.` },
  { id: 'v2-matn-l1', img: 'z4-p95-matn-vlm.png',
    q: `Première ligne du corps d'un hadith (3600 dpi) : elle commence par «المسلم أخو المسلم؛ لا يظلمه...». Transcris-la mot à mot avec la vocalisation imprimée. SCRUTIN : après «ولا يخذله» y a-t-il une clause «ولا يكذبه» ? Décompose le 3e verbe lettre par lettre (radicales + points) : كاف؟ ذال؟ باء؟ تاءfk binding? Quel est le dernier mot de la ligne ?` },
  { id: 'v3-tamhid-verb', img: 'z2-p95-tamhid-l2.png',
    q: `Ligne d'un paragraphe de manuel (2400 dpi) : «على الآخر ... القيام بها خصوصا الحقوق الأساسية منها كالكف عن ظلمه». SCRUTIN : le verbe avant «القيام» — est-ce «يَحِبُّ» (hā'-bā') ou «يَجِبُ» (jīm-bā') ? Décris la première lettre du verbe : sa forme et ses points. Transcris la ligne entière.` },
  { id: 'v4-kayy', img: 'z4-p97-kayy-vlm.png',
    q: `Deux lignes d'un manuel (3600 dpi). Transcris-les mot à mot. SCRUTIN 1 : la 1re ligne contient-elle «وفي قوله ﷺ: بحسب امرئ من الشر أن يحقر أخاه المسلم» تحذير عظيم — le mot après le guillemet fermant : «تحذير» (avec ذال) ou autre ? SCRUTIN 2 : la 2e ligne — «من ذلك؛ لأن الله تعالى لم يحقره إذ خلقه ورزقه ثم أحسن ... خلقه وسخر له» — transcris exactement ce qui suit «ثم أحسن» et ce qui précède «وسخر».` },
  { id: 'v5-ahzar', img: 'z2-p97-ahzar.png',
    q: `Deux lignes d'un manuel (2400 dpi) : «... وأرسل إليه محمدا ﷺ فمن حقر مسلما من المسلمين فقد حقر ... الله عز وجل». SCRUTIN : les mots entre «حقر» (2e occurrence) et «الله عز وجل» — exactement lesquels ? «ما عظم» ? «ما عز» ? «ولي» ? Décris lettre par lettre. Transcris les deux lignes.` },
  { id: 'v6-item5', img: 'z4-p97-item5-l1.png',
    q: `Ligne d'un manuel (2400 dpi) débutant par «5 - التعرض أو التسبب...». Transcris-la mot à mot. SCRUTIN : après «لماله» vient «بالإتلاف ... الإيذاء» — quelle est la conjonction exacte entre «بالإتلاف» et le second nom : «أو» ou «و» ? Et le second nom exactement : «الإيذاء» ? «الإيداء» ? Décris les lettres du second nom (points du ذال/دال).` },
  { id: 'v7-taql', img: 'z4-p98-taql-vlm.png',
    q: `Trois lignes d'un manuel (3600 dpi), fin d'un paragraphe sur la التقوى. Transcris-les mot à mot avec vocalisation. La 1re ligne commence vers «التقوى لا تحصل وحدها بالأعمال الظاهرة وإنما يحصلها رسوخ الاعتقاد بعظمة...». SCRUTIN : la 3e ligne (peut-être en couleur plus claire) — transcris-la intégralement ; elle complète «ورسوخ الاعتقاد بأن رؤية الله تعالى ...».` },
  { id: 'v8-table', img: 'z4-p98-table-vlm.png',
    q: `Tableau d'exercice d'un manuel (1200 dpi, couleur). Décris sa structure : combien de colonnes, combien de rangées, qu'y a-t-il dans chaque cellule (transcris tout l'arabe visible). Les cellules de droite/droite sont-elles vides ? SCRUTIN : la colonne «من مظاهر المحافظة على حقوق الأخوة» contient quels items exactement («الصدق في التعامل مع الناس» ? «تجنب إيذاءهم في أموالهم وأعراضهم» ? «محبتهم وعدم احتقارهم» ?) — transcris chaque rangée.` },
  { id: 'v9-yashwush', img: 'z4-p99-yash-vlm.png',
    q: `Deux lignes d'une citation d'al-Ghazali (3600 dpi). Transcris-les mot à mot. SCRUTIN 1 : «...تحصنا به عن إيذاء من ... القلب ويصد عن العبادة» — le verbe après «من» : «يشوش» ? «يسوء» ? autre ? Décris ses lettres. SCRUTIN 2 : «...للاكتفاء به عن ... الأوقات في طلب القوت» — le mot entre «عن» et «الأوقات» : «تضييع» ? «تضبيع» ? Décris ses lettres (points).` },
  { id: 'v10-ahwal', img: 'z4-p99-ahwal-vlm.png',
    q: `Ligne d'une citation d'al-Ghazali (3600 dpi) : «المصائب وقوة في ...؛ ومنها التبرك بمجرد الدعاء؛ ومنها انتظار». SCRUTIN : le mot après «في» : «الأحوال» ou «الأهوال» ou autre ? Y a-t-il un point au-dessus de la première consonne ? Décris précisément la lettre. Transcris la ligne.` },
  { id: 'v11-aya', img: 'z3-p97-aya.png',
    q: `Zone d'un manuel (2400 dpi) contenant la fin d'un verset coranique et sa référence entre crochets. SCRUTIN : la référence imprimée «[التوبة: ...]» — quels chiffres EXACTEMENT (arabo-indiens) ? Décris chaque chiffre : forme, nombre de traits/points. Est-ce ١١٩ ou ١٢٠ ou autre ? Transcris aussi les mots arabes visibles au-dessus de la référence.` },
];

for (const job of JOBS) {
  const out = `${DIR}/vlm-h6-17-${job.id}.txt`;
  if (fs.existsSync(out)) { console.log(`${job.id}: déjà fait`); continue; }
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const img = fs.readFileSync(`${DIR}/${job.img}`).toString('base64');
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: job.q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1600,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(`=== ${job.id} OK (${txt.length} car) ===`);
      done = true;
    } catch (e) { console.log(`${job.id} tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 9000 * attempt)); }
  }
}
console.log('OK vlm-h6-17');
