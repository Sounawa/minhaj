// Z2-6 — hadith-5ep leçon pdf-5 (بُنِيَ الإسلامُ على خمسٍ) — lectures VLM pages 42-48
// Convention IA-2 (méthode consolidée Z2) : SDK depuis /home/z/node_modules/z-ai-web-dev-sdk
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-06';
const pages = ['042', '043', '044', '045', '046', '047', '048'];

const ask = (p) => `Page ${p} d'un manuel scolaire marocain d'hadith (arabe, sens de lecture droite→gauche), 5ᵉ année primaire. Il s'agit de la leçon « أَطْوَارُ خَلْقِ الإِنْسَانِ » (l'islam est bâti sur cinq), quatrième hadīth des Quarante nawawiyya rapporté par Ibn Mas'ūd.

Transcris la page ENTIÈRE en arabe, fidèlement, mot à mot :
- Respecte la structure : titres de rubriques (أهداف الدرس، التمهيد، ترجمة الراوي، الفهم، الاستخلاص، التحليل، التقويم، الاستثمار، الأعداد القبلية …), paragraphes, listes numérotées, encadrés.
- Marque chaque titre de rubrique avec [TITRE] … [/TITRE].
- Marque chaque encadré/décoration avec [CADRE] … [/CADRE].
- Ne saute AUCUNE phrase. Un mot illisible : écris [؟]. Ne devine pas au-delà de ce qui est imprimé.
- Garde la vocalisation diacritique telle qu'imprimée.

Réponds UNIQUEMENT avec la transcription structurée, sans commentaire.`;

async function main() {
  const zai = await ZAI.create();
  for (const pg of pages) {
    const img = `${DIR}/p-${pg}.png`;
    const b64 = fs.readFileSync(img).toString('base64');
    const out = `${DIR}/vlm-p-${pg}.txt`;
    if (fs.existsSync(out)) { console.log(`skip ${pg} (déjà lu)`); continue; }
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: ask(pg) },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 4096,
        temperature: 0.1,
      });
      const txt = res?.choices?.[0]?.message?.content ?? JSON.stringify(res);
      fs.writeFileSync(out, txt);
      console.log(`OK p-${pg} (${txt.length} car)`);
    } catch (e) {
      console.error(`ÉCHEC p-${pg}: ${e.message}`);
    }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
