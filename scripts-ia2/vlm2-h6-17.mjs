// IA-2 — vlm2-h6-17.mjs : 2e vague VLM — scrutins restants L17.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();

const JOBS = [
  { id: 'w1-yakdhib', img: 'z5-p95-matn-l1.png',
    q: `Ligne d'un hadith dans un encadré de manuel (2400 dpi). Transcris-la mot à mot. Elle doit contenir QUATRE clauses négatives : «المسلم أخو المسلم؛ لا يظلمه، ولا يخذله، ولا ...، ولا يحقره. التقوى». SCRUTIN : la 3e clause — décompose le verbe lettre par lettre : yā' + quelle 2e lettre (kāf ?) + quelle 3e lettre (dhāl avec point au-dessus, ou dāl sans point, ou ḥā') ? Le mot est-il «يكذبه» ? Décris les points de la 2e et 3e lettre. Transcris ensuite le dernier mot de la ligne.` },
  { id: 'w2-ahsana', img: 'z5-p97-ahsana.png',
    q: `Une ligne de manuel (3600 dpi) contenant : «من ذلك؛ لأن الله تعالى لم يحقره إذ خلقه ورزقه ثم أحسن ... وسخر له». SCRUTIN : transcris EXACTEMENT ce qui est imprimé entre «ثم أحسن» et «وسخر» : est-ce «تقويم خلقه» ou «إليه في خلقه» ou autre ? Décompose le mot après «أحسن» lettre par lettre (تاء؟ قاف avec 2 points ? واو؟ ياء؟ ميم؟). Puis transcris la ligne entière.` },
  { id: 'w3-myst', img: 'z5-p98-myst-col.png',
    q: `Zone d'un manuel (1200 dpi, couleur — texte peut-être en couleur claire). Cette ligne est la DERNIÈRE d'un paragraphe qui se termine par «ورسوخ الاعتقاد بأن رؤية الله تعالى ...». SCRUTIN : transcris cette ligne mot à mot. Elle peut mentionner «محيطة بكل شيء» ou autre chose (الآخرة ? الجنة ? جزاء ?). Donne chaque mot imprimé avec sa vocalisation.` },
  { id: 'w4-yash', img: 'z5-p99-yash.png',
    q: `Deux lignes d'une citation d'al-Ghazali (2400 dpi) : «...ومنها الاستفادة من الجاه تحصنا به عن إيذاء من ... القلب ويصد عن العبادة، ومنها استفادة المال للاكتفاء به عن ... الأوقات في طلب القوت». SCRUTIN 1 : le mot après «من» (fin de la 1re ligne) : décompose-le lettre par lettre — «يشوش» ? «يسوء» ? autre ? SCRUTIN 2 : le mot entre «عن» et «الأوقات» (fin de la 2e ligne) : «تضييع» ? décompose lettre par lettre (points). Transcris les deux lignes en entier.` },
  { id: 'w5-thead', img: 'z6-p98-thead2.png',
    q: `Tête d'un tableau d'exercice de manuel (1200 dpi, couleur : texte probablement blanc/crème sur fond coloré). SCRUTIN : transcris la rangée d'en-tête mot à mot. Elle devrait contenir DEUX intitulés de colonnes (séparés) : l'un ressemblant à «من مظاهر المحافظة على حقوق الأخوة», l'autre à «آثارها الإيجابية في الواقع». Donne le texte ARABE exact de chaque cellule d'en-tête.` },
  { id: 'w6-tatimma', img: 'z5-p95-tatimma.png',
    q: `Bandeau-titre d'une leçon de manuel (1200 dpi, couleur : fond bleu, texte jaune/blanc) : «الأخوة الإسلامية» suivi d'un second élément. SCRUTIN : le mot après «الإسلامية» est-il «تتمة» ? Quels signes l'entourent : des parenthèses ( ) ou des chevrons « » ou rien ? Décris les glyphes avant et après «تتمة». Transcris le titre entier.` },
  { id: 'w7-raqaba', img: 'z5-p98-raqaba2.png',
    q: `Une ligne d'un manuel (3600 dpi) : «رقابة الله وشهود... وإحاطته بما عليه العباد من الأعمال والنيات والمقاصد». SCRUTIN 1 : le mot après «الله و» — «شهوده» (avec hā' final) ou «شهود» (sans) ? Y a-t-il une lettre hā' (boucle avec 2 points au-dessus) à la fin ? SCRUTIN 2 : après «بما» — «عليه العباد» ou «للعباد» ou autre ? Transcris la ligne entière.` },
  { id: 'w8-matn-paren', img: 'z6-p95-matn-l2.png',
    q: `Deuxième ligne d'un hadith encadré (2400 dpi) : «هاهنا» ويشير إلى صدره ثلاث مرات؛ بحسب امرئ من الشر أن يحقر». SCRUTIN : des parenthèses ( ) sont-elles imprimées autour de «ويشير إلى صدره ثلاث مرات» ou d'une autre partie ? Où s'ouvrent et se ferment-elles exactement ? Décris chaque signe de ponctuation imprimé sur la ligne. Transcris la ligne.` },
];

for (const job of JOBS) {
  const out = `${DIR}/vlm2-h6-17-${job.id}.txt`;
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
console.log('OK vlm2-h6-17');
