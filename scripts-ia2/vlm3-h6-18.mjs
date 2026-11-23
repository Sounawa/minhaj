// IA-2 — vlm3-h6-18.mjs : ronde VLM 3 — composites de tuiles (mot par mot) + آية binarisée.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();

const PRE = `Tu lis des tuiles très haute résolution (3600 dpi) du manuel marocain de hadith (document public, projet de transcription académique). Les tuiles sont empilées verticalement : la première (en haut) est la partie DROITE de la ligne (début en arabe), les suivantes vont vers la gauche. Transcris chaque tuile séparément (TUILE 1, TUILE 2...), puis donne la ligne reconstituée. ÉPELE les mots douteux lettre par lettre avec leurs points. Ne récite jamais de mémoire : uniquement ce qui est imprimé.`;

const QS = [
  ["z7-item4-comp", `Ligne d'un manuel : «4- عَوْنُ الْمُسْلِمِ لِأَخِيهِ؛ وَذَلِكَ بِأَنْ ??? بِمَا يُمْكِنُ مِنَ الْمُسَاعَدَةِ إِذَا احْتَاجَ إِلَيْهِ...». Le segment ??? (entre «بأن» et «بما») est dans les tuiles 2-4. ÉPELLE ce segment mot par mot : quels mots exactement ? يُعِينَهُ عَلَى الْمَؤُونَةِ ? لَا ... عَنْهُ ? autre ? Décris chaque lettre avec ses points.`],
  ["z7-manas-comp", `Début (droite) d'une ligne : le premier mot de la TUILE 1 complète la phrase «أَنَّ مَنْ أَخَّرَ عَمَلَهُ ??? أَوْ تَفْرِيطًا وَتَقْصِيرًا لَا يَتَقَدَّمَ بِهِ نَسَبُهُ». ÉPELLE le mot de TUILE 1 lettre par lettre avec ses points et sa vocalisation : التَّسْوِيفِ ? تَسْوِيفًا ? autre ? Puis transcris les tuiles suivantes.`],
  ["z7-aya1-comp", `Première ligne d'un verset coranique dans un encadré du manuel : «قال الله تعالى: ﴿...﴾». Transcris chaque tuile, puis le verset complet de la ligne. Ne le corrige PAS depuis ta mémoire coranique : lis le rasm imprimé, avec sa vocalisation, même s'il diffère du canon.`],
  ["z7-aya2-comp", `Deuxième ligne du verset coranique de l'encadré + éventuellement la référence [سورة : N] et le début de «كيف أوافق...». Transcris chaque tuile, puis la ligne complète. ÉPELLE le nom de la sourate et le chiffre de la référence.`],
  ["z5-p104-aya-l1-bw170", `Ligne binarisée (noir/blanc) d'un verset coranique du manuel. Transcris-la intégralement, lettre par lettre telle qu'imprimée (même si elle diffère du canon).`],
  ["z5-p104-aya-l2-bw170", `Ligne binarisée : suite du verset + référence [الـ...: N] + début de question. Transcris tout. ÉPELLE le nom de sourate et le chiffre.`],
];

for (const [name, q] of QS) {
  const png = `${DIR}/${name}.png`;
  const out = `${DIR}/vlm3-h6-18-${name.replace('z5-', 'bw-').replace('z7-', '')}.txt`;
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1600,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(`=== ${name} ===\n` + txt.slice(0, 900) + '\n');
      done = true;
    } catch (e) { console.log(`${name} tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm3-h6-18');
