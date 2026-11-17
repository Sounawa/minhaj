import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-20';
const zai = await ZAI.create();
const img = fs.readFileSync(`${DIR}/z20-n23.png`).toString('base64');
const Q = `Partie gauche d'une ligne de l'encadré خديجة (manuel hadith 5e primaire, p.112, lecture droite→gauche). La ligne contient : «...عَنْهَا لَمَّا أَرَادَتْ أَنْ [VERBE CONTESTÉ] عَنِ النَّبِيِّ...». Transcris TOUT ce qui est visible, mot à mot, avec la vocalisation.
LETTRE PAR LETTRE le verbe entre أَنْ et عَنِ : décris chaque lettre de base (nom), ses points (combien, au-dessus/dessous) et ses diacritiques (fatha, kasra, ḍamma, sukūn, shadda). Candidats : تُخَفِّفَ (tāʾ+ḍamma, khāʾ+fatha, fāʾ+shadda, fāʾ+fatha — 4 lettres) / تَخْفِفَ (tāʾ+fatha, khāʾ+sukūn, fāʾ+kasra, fāʾ+fatha) / تَخْفَ (3 lettres) / autre. Ne complète jamais par mémoire : seulement ce qui est imprimé. Illisible : [؟].`;
for (let attempt = 1; attempt <= 4; attempt++) {
  try {
    const r = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: Q },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
      ] }],
      model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1024,
    });
    const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
    fs.writeFileSync(`${DIR}/z20-n23.txt`, txt);
    console.log(txt);
    break;
  } catch (e) { console.log(`échec ${attempt}: ${e.message}`); await new Promise(r => setTimeout(r, 8000*attempt)); }
}
