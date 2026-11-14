import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-16';
const ASKS = [
  ['i-zarqani-word-p96.jpg', 'Extrait : «فإن الذي [VERBE] الإسلام والإيمان». Le VERBE (4 lettres : يـ + X + ـنـ + ـيه) : la 2e lettre X est-elle ع (AUCUN point — juste le diacritique) ou غ (UN POINT net au-dessus) ? Réponds : ع ou غ avec justification, puis transcris.'],
  ['i-afat-dunya-p96.jpg', 'Extrait de la fin de citation de الزرقاني : «يسلم من جميع الآفات ...». Les deux mots après «الآفات» : «دنيا وأخرى» ou «دينا وآخرة» ou autre ? Décompose le premier mot lettre par lettre (y a-t-il un ن dans دنيا ?). Transcris.'],
  ['i-muhsin3-p95.jpg', 'Deux lignes de commentaire après le hadith : «فمن اشتغل بما يعنيه وترك ما لا يعنيه فهو المحسن الحق؛ لأنه ...». Transcris les DEUX lignes mot à mot, en t\\u2019appuyant sur le sens (la phrase se termine probablement par ظاهرًا وباطنًا). Question : le mot après «لأنه» — décompose-le lettre par lettre.'],
];
async function main() {
  const zai = await ZAI.create();
  for (const [img, ask] of ASKS) {
    const out = `${DIR}/vlm-${img.replace('.jpg', '.txt')}`;
    if (fs.existsSync(out)) { console.log(`skip ${img}`); continue; }
    const b64 = fs.readFileSync(`${DIR}/${img}`).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: `Zoom extrême, manuel marocain de hadith (5e primaire), leçon 17. ${ask}\nRéponds par les CHOIX d'abord, puis la transcription. Illisible : [؟].` },
        { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
      ] }],
      model: 'glm-5v-turbo', max_tokens: 1200, temperature: 0.1,
    });
    fs.writeFileSync(out, res?.choices?.[0]?.message?.content ?? JSON.stringify(res));
    console.log(`OK ${img}`);
  }
}
main().catch(e => { console.error(e); process.exit(1); });
