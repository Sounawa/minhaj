// Z2-18 — zooms finaux passe 4
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-16';
const ASKS = [
  ['f-ref-p88.jpg', 'Ligne de référence sous l\'encadré du hadith (couleur, entre crochets). Transcris-la EXACTEMENT. Le premier mot : est-ce «رواه» (ر-و-ا-ه) ou «رواية» (ر-و-ا-ي-ة) ou «رواة» (ر-و-ا-ة) ? Décompose-le glyphe par glyphe : combien de lettres avant la lettre finale ? La lettre finale porte-t-elle deux points (ة) ou non (ه) ? Y a-t-il un ي médian ?'],
  ['f-watajjah-p90.jpg', 'Le premier mot complet à droite de cette ligne (après le point-final de la ligne précédente). Il commence par واو. Décompose-le glyphe par glyphe : après le واو et l\u2019alif, viennent combien de lettres dentales (ن ou ت ou تت) avant le جيم ? Est-ce «واتّجه» (ت مكررة avec chadda) ou «وانجه» (نون puis جيم) ou «وانته» ? Y a-t-il une chadda ? Transcris la ligne entière.'],
  ['f-quote-p88.jpg', 'Citation prophétique en naskh vocalisé (droite de la ligne). Transcris-la EXACTEMENT. (1) Y a-t-il «قد» avant «تركتكم» ? (2) Entre «على» et «البيضاء» y a-t-il le mot «المحجة» ou rien ? (3) La suite après «البيضاء» jusqu\'à «هالك».'],
];
async function main() {
  const zai = await ZAI.create();
  for (const [img, ask] of ASKS) {
    const out = `${DIR}/vlm-${img.replace('.jpg', '.txt')}`;
    if (fs.existsSync(out)) { console.log(`skip ${img}`); continue; }
    const b64 = fs.readFileSync(`${DIR}/${img}`).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: `Zoom extrême d'un manuel marocain de hadith (5e primaire), leçon 16. ${ask}\n\nRéponds par les CHOIX retenus (numérotés) avec justification glyphique, puis la transcription exacte. Illisible : [؟].` },
          { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo', max_tokens: 1200, temperature: 0.1,
      });
      fs.writeFileSync(out, res?.choices?.[0]?.message?.content ?? JSON.stringify(res));
      console.log(`OK ${img}`);
    } catch (e) { console.error(`ÉCHEC ${img}: ${e.message}`); }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
