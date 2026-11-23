// IA-2 — vlm3-h6-17.mjs : ponctuation/guillemets de l'encadré du hadith p.95.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();
const Q = `Encadré d'un hadith de manuel (2400 dpi), 5 lignes :
1: عن أبي هريرة رضي الله عنه قال: قال رسول الله ﷺ: «...
2: المسلم أخو المسلم؛ لا يظلمه، ولا يخذله، ولا يكذبه، ولا يحقره. التقوى
3: هاهنا» ويشير إلى صدره ثلاث مرات؛ بحسب امرئ من الشر أن يحقر
4: أخاه المسلم. كل المسلم على المسلم حرام: دمه وماله وعرضه».
5: [رواه مسلم]
SCRUTIN : décris TOUTE la ponctuation imprimée : (a) où s'ouvrent et se ferment les guillemets « » exactement (à quel mot) ? y a-t-il une paire INTERNE autour de «التقوى هاهنا» ou autour de «ويشير إلى صدره ثلاث مرات» ? (b) y a-t-il un point après «يحقره» sur la ligne 2 ? (c) la ligne 4 commence-t-elle directement par «أخاه المسلم» ? (d) le «؛» après «مرات» existe-t-il ? Décris chaque signe que tu vois, ligne par ligne, avec sa position exacte par rapport aux mots.`;
const img = fs.readFileSync(`${DIR}/z6-p95-matn-full.png`).toString('base64');
let done = false;
for (let attempt = 1; attempt <= 4 && !done; attempt++) {
  try {
    const r = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
          { type: 'text', text: Q },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
      ] }],
      model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1800,
    });
    const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
    fs.writeFileSync(`${DIR}/vlm3-h6-17-matn-punct.txt`, txt);
    console.log(txt);
    done = true;
  } catch (e) { console.log(`tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 9000 * attempt)); }
}
console.log('OK vlm3-h6-17');
