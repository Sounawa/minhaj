// Z2-22 — hadith-5ep leçon pdf-20 — lectures VLM composites 600 dpi (z-c20-A1→C4)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-20';
const bands = ['A1','A2','A3','A4','B1','B2','B3','B4','C1','C2','C3','C4'];
const pagemap = { A1:111, A2:111, A3:111, A4:111, B1:112, B2:112, B3:112, B4:112, C1:113, C2:113, C3:113, C4:113 };

const ask = (tag, pg) => `Bande verticale (extrait haute résolution 600 dpi) de la page ${pg} d'un manuel scolaire marocain d'hadith, 5ᵉ année primaire, leçon « دَعْمٌ وَتَطْبِيقٌ » (consolidation). Bande ${tag}.

TRANSCRIS SANS INTERPRÉTER. Transcris uniquement ce qui est imprimé, mot à mot, en conservant la vocalisation. Structure attendue : bandeau de leçon, أهداف الدرس, النص (encadré), continuation du texte (paragraphe sur خديجة أم المؤمنين), الفهم, التحليل, التطبيق, الإعداد القبلي.
Règles :
- Chaque titre de rubrique : [TITRE] … [/TITRE].
- Mot ou passage illisible : [؟]. Ne complète JAMAIS par mémoire d'un texte connu.
- Les āyāt et citations : transcris uniquement les lettres visibles.
- Références entre crochets telles quelles.
Réponds UNIQUEMENT avec la transcription, sans commentaire.`;

async function main() {
  const zai = await ZAI.create();
  for (const tag of bands) {
    const img = `${DIR}/z-c20-${tag}.png`;
    const out = `${DIR}/vlm20-c-${tag}.txt`;
    if (fs.existsSync(out)) { console.log(`skip ${tag}`); continue; }
    const b64 = fs.readFileSync(img).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: ask(tag, pagemap[tag]) },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 4096,
        temperature: 0.1,
      });
      const txt = res?.choices?.[0]?.message?.content ?? JSON.stringify(res);
      fs.writeFileSync(out, txt);
      console.log(`OK ${tag} (${txt.length} car)`);
    } catch (e) {
      console.error(`ÉCHEC ${tag}: ${e.message}`);
    }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
