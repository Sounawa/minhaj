// Z2-1 — hadith-5ep leçon pdf-1 (التعريف بالمؤلف والمؤلف) — lectures VLM pages 13-22
// Convention IA-1 : SDK importé depuis /home/z/node_modules/z-ai-web-dev-sdk/dist/index.js
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-01';
const pages = ['013','014','015','016','017','018','019','020','021','022'];

const ask = (p) => `Page ${p} d'un manuel scolaire marocain d'hadith (arabe, sens de lecture droite→gauche), 5ᵉ année primaire. Il s'agit de la leçon « التعريف بالمؤلف والمؤلف » (présentation de l'auteur al-Nawawī et de l'ouvrage al-Arbaʿūn al-nawawiyya avec le commentaire d'Ibn Daqīq al-ʿĪd).

Transcris la page ENTIÈRE en arabe, fidèlement, mot à mot :
- Respecte la structure : titres de rubriques (أهداف الدرس، التمهيد، ترجمة الإمام النووي، المعجم، أتعلم وأمت供 …), paragraphes, listes numérotées, encadrés.
- Numérote les rubriques rencontrées avec [TITRE] … [/TITRE].
- Numérote les encadrés/décorations avec [CADRE] … [/CADRE].
- Ne saute AUCUNE phrase. Un mot illisible : écris [؟]. Ne devine pas au-delà de ce qui est imprimé.
- Garde la vocalisation diacritique telle qu'imprimée.

Réponds UNIQUEMENT avec la transcription structurée, sans commentaire.`;

async function main() {
  const zai = await ZAI.create();
  const out = [];
  for (const pg of pages) {
    const img = `${DIR}/p-${pg}.png`;
    const b64 = fs.readFileSync(img).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: ask(pg) },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ]}],
        model: 'glm-5v-turbo', max_tokens: 2400,
      });
      const txt = res.choices[0].message.content;
      out.push(`\n\n========== PAGE ${pg} ==========\n` + txt);
      console.log(`PAGE ${pg} OK (${txt.length} car)`);
      fs.writeFileSync(`${DIR}/reads.md`, out.join(''));
    } catch (e) {
      console.log(`PAGE ${pg} FAIL: ${e.message}`);
      out.push(`\n\n========== PAGE ${pg} = FAIL: ${e.message} ==========\n`);
    }
  }
  fs.writeFileSync(`${DIR}/reads.md`, out.join(''));
  console.log('Écrit:', `${DIR}/reads.md`);
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
