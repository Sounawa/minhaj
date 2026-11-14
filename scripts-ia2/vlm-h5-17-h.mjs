import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-16';
const ASKS = [
  ['h-single-word-p97.jpg', 'UN SEUL MOT arabe calligraphié (naskh vocalisé), extrait d\\u2019une citation. Il fait 4 lettres : يـ + [LETTER X]ـ + ـنـ + ـيك. La QUESTION UNIQUE : la lettre X (la 2e lettre, entre le يـ et le ن) est-elle ع (ʿayn : AUCUN point) ou غ (ghayn : UN point au-dessus) ? Zoom au maximum sur cette lettre : y a-t-il un point, oui ou non ? Ne réponds que par : ع (aucun point) ou غ (un point), avec justification, puis le mot entier.'],
  ['h-hadd-word-p97.jpg', 'UN SEUL MOT arabe calligraphié : transcris-le (2 lettres + shadda).'],
];
async function main() {
  const zai = await ZAI.create();
  for (const [img, ask] of ASKS) {
    const out = `${DIR}/vlm-${img.replace('.jpg', '.txt')}`;
    if (fs.existsSync(out)) { console.log(`skip ${img}`); continue; }
    const b64 = fs.readFileSync(`${DIR}/${img}`).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: ask },
        { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
      ] }],
      model: 'glm-5v-turbo', max_tokens: 700, temperature: 0.1,
    });
    fs.writeFileSync(out, res?.choices?.[0]?.message?.content ?? JSON.stringify(res));
    console.log(`OK ${img}`);
  }
}
main().catch(e => { console.error(e); process.exit(1); });
