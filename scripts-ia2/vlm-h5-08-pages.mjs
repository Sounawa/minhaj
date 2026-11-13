// Z2-8 — hadith-5ep leçon pdf-8 (القضاء والقدر) — lectures VLM pages 50-55
// Convention IA-2 (méthode consolidée Z2) : SDK depuis /home/z/node_modules/z-ai-web-dev-sdk
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/minhaj/scripts-ia2/tmp/h5-08';
const pages = ['050', '051', '052', '053', '054', '055'];

const ask = (p) => `Page ${p} d'un manuel scolaire marocain d'hadith (arabe, sens de lecture droite→gauche), 5ᵉ année primaire. Il s'agit de la leçon 8 « القضاء والقدر » (le décret et la prédestination), fondée sur la suite du hadith d'Ibn Mas'ūd des Quarante d'al-Nawawī (hadith 4) : la partie « يُؤْمَرُ بِأَرْبَعِ كَلِمَاتٍ: بِكَتْبِ رِزْقِهِ وَأَجَلِهِ وَعَمَلِهِ وَشَقِيٍّ أَوْ سَعِيدٍ » et la fin du hadith (فَيَسْبِقُ عَلَيْهِ الْكِتَابُ… فَيَدْخُلُهَا), avec le commentaire (شرح) d'Ibn Daqīq al-ʿīd.

Transcris la page ENTIÈRE en arabe, fidèlement, mot à mot :
- Respecte la structure : titres de rubriques (أهداف الدرس، التمهيد، نصوص الدروس، المصطلحات/المفردات، الفهم، التحليل، التقويم، الاستثمار، الأعداد القبلية …), paragraphes, listes numérotées, encadrés, tableaux.
- Marque chaque titre de rubrique avec [TITRE] … [/TITRE].
- Marque chaque encadré/décoration avec [CADRE] … [/CADRE].
- Ne saute AUCUNE phrase. Un mot illisible : écris [؟]. Ne devine pas au-delà de ce qui est imprimé.
- Garde la vocalisation diacritique telle qu'imprimée.
- Les citations coraniques et hadiths : transcris-les telles qu'imprimées, avec leur référence imprimée entre crochets si présente (ex. [النحل : 3]).

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
