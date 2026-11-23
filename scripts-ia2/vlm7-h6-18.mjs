// IA-2 — vlm7-h6-18.mjs : ronde VLM 7 — les 3 dernières zones.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();

const PRE = `Tu lis un micro-crop très haute résolution (3600 dpi) du manuel marocain de hadith (document public, transcription académique). Transcris UNIQUEMENT ce qui est imprimé, mot par mot, avec vocalisation et ponctuation. ÉPELLE les mots contestés. Ne récite pas de mémoire.`;

const QS = [
  ["z11-manas-first", `Les 3-4 PREMIERS mots (droite) d'une ligne. La phrase complète est : «ومعنى قوله ﷺ: «ومن بطأ به عمله لم يسرع به نسبه» أن من أخره عمله ... لا يتقدم به نسبه، وأن المسارعة إنما هي بالأعمال لا بالأنساب». Transcris les premiers mots de CETTE ligne dans l'ordre exact. ÉPELLE le premier mot (التَّسْوِيفُ ? السَّيِّئُ ? autre ?) et le deuxième (عَنْ ? عَنْهُ ? بِتَفْرِيطِهِ ? autre ?). Y a-t-il un point-virgule ou une virgule quelque part ?`],
  ["z11-p101-glose4", `UNE glose lexicographique (terme rouge : définition noire). Le terme commence par «وَغْشِيَتْهُمْ» (du hadith). Transcris la glose ENTIÈRE exactement : le terme ET la définition complète avec sa vocalisation. La définition semble avoir deux verbes (نَزَلَتْ/نَزَلْنَا... + un second verbe).`],
  ["z11-p104-table-hdr2", `Le HAUT d'un tableau d'exercice, y compris la possible rangée d'EN-TÊTES (texte éventuellement blanc/crème sur fond coloré) et la rangée 1 de contenu. (1) Transcris tout texte d'EN-TÊTE de colonne (il peut être blanc sur fond coloré — cherche-le). (2) Transcris la rangée 1 de contenu. (3) Combien de colonnes ?`],
];

for (const [name, q] of QS) {
  const png = `${DIR}/${name}.png`;
  const out = `${DIR}/vlm7-h6-18-${name}.txt`;
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
      console.log(`=== ${name} ===\n` + txt.slice(0, 900) + '\n');
      done = true;
    } catch (e) { console.log(`${name} tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm7-h6-18');
