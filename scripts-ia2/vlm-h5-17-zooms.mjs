// Z2-19 — zooms adjudication leçon 17
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-16';
const ASKS = [
  ['m-muhsin-p95.jpg', 'Haut de la page 95 (2-3 lignes après le hadith). Transcris mot à mot : «...تركه ما لا يعنيه». فهو المحسن ال...؟؛ لأنه ...». Questions : (1) le mot après المحسن : «الكف» ou «الحق» ou autre — décompose-le ; (2) la phrase après «لأنه» complète (il y a 2 lignes : ظاهرا وباطنا apparaît).'],
  ['m-yuaddu-p94.jpg', 'Bas de la page 94. Le verbe dans «من الإحسان الذي ... مرتبة عالية» : «يعبر» ou «يعد» ou «يعتبر» — décompose lettre par lettre (y a-t-il un ت après le ع ?).'],
  ['m-hadref-p93.jpg', 'Bas de la page 93 : encadré du hadith + ligne de référence. Transcris la référence exactement : [سنن الترمذي] ou [رواه الترمذي] ou autre ?'],
  ['m-fiqh-p96.jpg', 'Fin de la phrase de Luqmān. (1) Le mot après «يريدون» : «الفقه» ou «الفضل» — décompose lettre par lettre (ق-ه ou ض-ل ?). (2) Transcris toute la fin : «صدق الحديث وأداء الأمانة وترك ما لا يعنيني».'],
  ['m-yanfauhu-p96.jpg', 'La ligne «دل الحديث على أن من حسن إسلام المرء ...ه من الأمور». Le mot : «اشتغاله بما ينفعه» ou «اشتغاله بما يعنيه» — décompose le verbe lettre par lettre.'],
  ['m-zarqani-p96.jpg', 'Citation de l\\u2019imam الزرقاني (Sharḥ al-Muwaṭṭa\\u2019). Transcris-la mot à mot. Questions : (1) «فإن الذي ...ه الإسلام والإيمان» : يغنيه ou يعنيه ? (2) «من ... وري» : شبع وريّ ou مأكل ومشرب ? (3) «دون مزيد الت...م» : التنعم ou الترف ? (4) la fin : «أو قرب ربه من ...» : منه ou من عبده ?'],
  ['m-ghazali-p97.jpg', 'Citation de al-Ghazali dans l\\u2019encadré (calligraphie naskh vocalisée). Transcris-la mot à mot ENTIÈREMENT. Questions : (1) le premier mot : «حدّ» ou «دع» ou «حدث» ? (2) «ما لا ...ك في الكلام» : يعنيك ou يغنيك ? (3) «لم تأثم ولا تتضرر حالا ولا مآلا» exact ? (4) la fin : «ومن قدر على أن يأخذ كنزا من كنوز الجنة وأخذ بدله بدرة كان خاسرا» exact ?'],
  ['m-nuqila-p96.jpg', 'Le mot entre «ويتركون ما لا يعنيهم» et «عنهم في ذلك آثار كثيرة» : «ونقل» ou «وروي» ou «ونقبت» — décompose-le. Transcris la fin de la ligne.'],
  ['m-yughnika-p95.jpg', 'Fin de la citation de مالك بن دينار : «فاعلم بأنك تكلمت بما لا ...». Le dernier mot : «يغنيك» ou «يعنيك» — décompose-le lettre par lettre (غ un point au-dessus, ou ع sans point ?).'],
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
          { type: 'text', text: `Zoom très haute résolution d'un manuel marocain de hadith (5e primaire), leçon 17 «ترك ما لا يعني». ${ask}\n\nAnalyse les glyphes un par un. Réponds d'abord par les CHOIX retenus (numérotés), puis la transcription complète mot à mot vocalisée. Illisible : [؟].` },
          { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo', max_tokens: 1600, temperature: 0.1,
      });
      fs.writeFileSync(out, res?.choices?.[0]?.message?.content ?? JSON.stringify(res));
      console.log(`OK ${img}`);
    } catch (e) { console.error(`ÉCHEC ${img}: ${e.message}`); }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
