// Z2-38 — Round 3j : 2 derniers crops du titre décoratif p27
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04';
const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

const QS = [
  ['p27-topR', `Partie DROITE (début de lecture) d'une ligne calligraphiée claire sur fond bleu, dans une boîte-titre d'organigramme (leçon «التنافس في الخير»). Cette partie précède le mot «بِالصَّحَابَةِ» (à gauche, hors cadre). TRANSCRIS ce fragment mot à mot. Est-ce «وَلَقَدْ...» ? «مَوَدَّةُ...» ? «وَمَا...» ? autre ? Décris chaque mot.`],
  ['p27-topL2', `Ligne inférieure d'une boîte-titre d'organigramme (calligraphie claire sur fond bleu). La couche texte montre des fragments «ص...ار» vers le centre. TRANSCRIS la ligne complète mot à mot. Candidats: «وَالتَّنَافُسُ فِي الْخَيْرِ» / «وَاللِّاقَةُ فِي الْخَيْرِ» / «صَحْبَةٌ...» / autre.`],
];

for (const [nom, Q] of QS) {
  const out = `${DIR}/vlm-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  const img = fs.readFileSync(`${DIR}/crops/vlm-${nom}.png`).toString('base64');
  console.log(`\n======== ${nom} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 3 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: `Calligraphie maghrébine d'un manuel scolaire marocain d'hadith. TRANSCRIS UNIQUEMENT ce qui est imprimé. Décris les lettres avant de conclure. Ne complète jamais par mémoire.\n\n${Q}` },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 900,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} échec: ${e.message}`); await sleep(5000*attempt); }
  }
  await sleep(2000);
}
