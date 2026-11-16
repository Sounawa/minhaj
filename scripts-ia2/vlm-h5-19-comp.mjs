// Z2-21 — hadith-5ep leçon 19 — lectures VLM composites 600 dpi (z-c19-*)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-19';
const items = [
  ['A1', 104], ['A2', 104], ['A3', 104],
  ['B1', 105], ['B2', 105], ['B3', 105], ['B4', 105],
  ['C1', 106], ['C2', 106], ['C3', 106], ['C4', 106],
  ['D1', 107], ['D2', 107], ['D3', 107], ['D4', 107],
  ['E1', 108], ['E2', 108], ['E3', 108], ['E4', 108],
  ['F1', 109], ['F2', 109], ['F3', 109], ['F4', 109],
  ['G1', 110], ['G2', 110], ['G3', 110],
];

const ask = (tag, page) => `Bande haute résolution (600 dpi) de la page ${page} d'un manuel scolaire marocain d'hadith, 5ᵉ primaire, leçon 19 « مِنْ خِصَالِ الْإِيمَانِ » (hadith 14 des Arbaʿūn : « مَنْ كَانَ يُؤْمِنُ بِاللهِ وَالْيَوْمِ الْآخِرِ فَلْيَقُلْ خَيْرًا أَوْ لِيَصْمُتْ... فَلْيُكْرِمْ جَارَهُ... فَلْيُكْرِمْ ضَيْفَهُ »).

TRANSCRIPTION STRICTE, lettre à lettre, sans interprétation ni correction :
- Transcris UNIQUEMENT ce qui est imprimé, avec la vocalisation diacritique exacte telle qu'imprimée (fatha, damma, kasra, sukun, shadda, tanwin).
- Recopie les lettres point par point : ب ت ث / ج ح خ / د ذ / ر ز / س ش / ص ض / ط ظ / ع غ / ف ق — fais très attention au NOMBRE DE POINTS et à leur position.
- Les références entre crochets [صحيح البخاري ومسلم]، [سنن الترمذي]، [فتح الباري، ونسبه للطبراني]، [الجامع الصغير للسيوطي]، [المعجم الكبير للطبراني] et les références de versets [الإسراء: 36]، [ق: 18]، [النساء: 36]، [الذاريات: 24] etc. doivent être transcrites EXACTEMENT (chiffres compris).
- La bande peut couper des lignes en haut/bas : transcris les lignes complètes visibles, indique [COUPÉ] pour une ligne tronquée.
- Ne saute aucune ligne. Mot illisible : [؟].

Réponds UNIQUEMENT avec la transcription arabe, sans commentaire.`;

async function main() {
  const zai = await ZAI.create();
  for (const [tag, page] of items) {
    const img = `${DIR}/z-c19-${tag}.png`;
    const out = `${DIR}/z-c19-${tag}.txt`;
    if (fs.existsSync(out)) { console.log(`skip ${tag}`); continue; }
    const b64 = fs.readFileSync(img).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: ask(tag, page) },
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
