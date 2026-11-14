// Z2-19 — ultra-zooms ×6 : arbitrage غ/ع + المحسن
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-16';
const ASKS = [
  ['g-malik-word-p95.jpg', 'Fin de la citation de مالك بن دينار : «فاعلم بأنك تكلمت بما لا ...ك». Regarde le mot final au scrutation MAXIMALE : la lettre médiane (la 2e lettre du verbe, après le ي) porte-t-elle UN POINT AU-DESSUS (غ = ġayn) ou AUCUN POINT (ع = ʿayn) ? Attention : les signes diacritiques (chadda, kasra, sukūn) NE SONT PAS des points de lettre. Réponds : غ (point) ou ع (sans point), puis transcris.'],
  ['g-obj3-word-p93.jpg', 'Objectif n°3 : «أن أشتغل بما ...ني وأترك ما لا يعنيني». Le verbe après «بما» : la lettre médiane porte-t-elle UN POINT AU-DESSUS (غ) ou AUCUN (ع) ? Réponds : غ ou ع, puis transcris la ligne.'],
  ['g-ghazali-word-p97.jpg', 'Début de la citation de al-Ghazali : «... ما لا ...ك في الكلام». La lettre médiane du verbe porte-t-elle UN POINT AU-DESSUS (غ) ou AUCUN (ع) ? Réponds : غ ou ع, puis transcris la ligne entière.'],
  ['g-ihsan-word-p94.jpg', 'La ligne : «... ترك المسلم ما لا ...ه من الإحسان الذي يعتبر مرتبة عالية». La lettre médiane du verbe après «ما لا» porte-t-elle UN POINT AU-DESSUS (غ) ou AUCUN (ع) ? Réponds : غ ou ع, puis transcris la ligne.'],
  ['g-yanfauhu2-p96.jpg', 'La fin de la ligne : «دل الحديث على أن من حسن إسلام المرء [слово] من الأمور». Transcris le ou les mots entre «المرء» et «من الأمور» lettre par lettre (اشغاله؟ بما ينفعه؟ بما يعنيه؟ autre ?).'],
  ['g-zarqani-word-p96.jpg', 'Début de la citation de الزرقاني : «فإن الذي ...ه الإسلام والإيمان العمل...». La lettre médiane du verbe porte-t-elle UN POINT AU-DESSUS (غ) ou AUCUN (ع) ? Réponds : غ ou ع, puis transcris le début de la ligne.'],
  ['g-muhsin2-p95.jpg', 'Les 3-4 lignes après le hadith encadré. Transcris-les mot à mot : «فمن اشتغل بما يعنيه وترك ما لا يعنيه فهو المحسن ال...؛ لأنه ...». Question : (1) المحسن الحق ou الكف ? (2) la phrase complète après «لأنه» (il y a peut-être deux lignes : ظاهرا وباطنا ou autre chose) ?'],
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
          { type: 'text', text: `Zoom extrême ×6 d'un manuel marocain de hadith (5e primaire), leçon 17 «ترك ما لا يعني». ${ask}\n\nRéponds d'abord par le CHOIX (غ ou ع), puis la transcription. Illisible : [؟].` },
          { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo', max_tokens: 1300, temperature: 0.1,
      });
      fs.writeFileSync(out, res?.choices?.[0]?.message?.content ?? JSON.stringify(res));
      console.log(`OK ${img}`);
    } catch (e) { console.error(`ÉCHEC ${img}: ${e.message}`); }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
