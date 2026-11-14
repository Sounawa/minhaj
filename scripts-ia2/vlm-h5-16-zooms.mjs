// Z2-18 — zooms serrés ×4 : arbitrages finaux leçon 16
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-16';

const ASKS = [
  ['z-obj3-p88.jpg', 'Objectif n°3 du cours (une seule ligne). Trois lectures divergentes ont été faites : (a) «أن أبتعد عن الشبهات في عباداتي ومعاملاتي»، (b) «أن أتجنب الشبهات في عبادتي ومعاملي»، (c) «أن أبتعد الشبهات في عباداتي ومعاملاتي». Regarde les lettres UNES PAR UNES : quel est le verbe ? Y a-t-il la préposition «عن» entre le verbe et «الشبهات» ? Les deux derniers mots sont-ils au singulier (عبادتي/معامتي) ou au pluriel (عباداتي/معاملاتي) ? Donne la transcription définitive lettre par lettre.'],
  ['z-quote-p88.jpg', 'Citation du Prophète dans le تمهيد. Transcris-la lettre par lettre. Question : après «تركتكم» y a-t-il «على المحجة البيضاء» ou «على البيضاء» seulement ? Y a-t-il «قد» avant «تركتكم» ?'],
  ['z-tamhid2-p88.jpg', 'Suite du تمهيد. Transcris lettre par lettre : «لكنه قد تعرض أمور ملتبسة ... الحكم فيها على المكلف». Question : le verbe est-il «يلتبس» ou «يختلط» ? Puis «فلا يميز حقه من حق غيره ولا الحلال من الحرام» ? Puis les deux questions finales exactes («ولا أن الشيء من الواجبات أم لا؟» et «ولا أنه من المعروف أو/أم من المنكر؟»).'],
  ['z-hadithref-p88.jpg', 'Bas de l\'encadré du hadith. Transcris la dernière ligne de l\'encadré (la référence entre crochets) lettre par lettre : [رواه ...]. Y a-t-il «وقال: حديث حسن صحيح» ou autre ?'],
  ['z-halalbayyin-p89.jpg', 'Début de la définition dans أولا. Transcris lettre par lettre : «ففي الممتلكات مثلا: الحلال ...: ما علمت ملكه يقينا لنفسك». Question : le premier terme est-il «الحلال اليقين» ou «الحلال البين» ?'],
  ['z-shubha-def-p89.jpg', 'Fin de la définition de الشبهة (bas de page 89). Transcris lettre par lettre : «والحرام البين: ما علمت ملكه لغيرك يقينا؛ والشبهة: ما لا ...». Comment se termine exactement la définition ?'],
  ['z-ijtinab-p90.jpg', 'Première ligne de la page 90. Transcris-la lettre par lettre : «فالورع اجتناب...» — le dernier mot est-il «اجتنابها» (ha final) ou «اجتنابه» (waw-ha) ? Puis la référence entre crochets exactement.'],
  ['z-khafaiaha-p90.jpg', 'Ouverture de ثانيا. Transcris lettre par lettre : «حث النبي ﷺ في الحديث على ترك الشبهات ل...ها و...ها، ذلك أن الأحكام الشرعية على قسمين». Questions : (1) premier mot : «حثّ» ou «حدث» ? (2) le mot après «للتباسها» : «وخفائها» / «وحفاظها» / «وحذرها» ? (3) y a-t-il «و» devant «ذلك» ?'],
  ['z-ay-natak-p90.jpg', 'Explication du hadith. Transcris lettre par lettre : «أي: ...». Questions : (1) «نترك» ou «اترك» ou «أترك» ? (2) «في حرمته» ou «في حرماته» ou «في حرمانه» ? (3) le verbe après «والأعمال» : «وننتقل» / «ونجتنب» / «وننتهي» / autre — décompose-le lettre par lettre.'],
  ['z-tirmidhi2-p90.jpg', 'Hadith de Tirmidhī (2 lignes). Transcris lettre par lettre. Questions : (1) «حتى يتّرك» (avec chadda) ou «حتى يتروك» ? (2) le mot : «مخافة» / «محافظة» / «محاذرة» ? (3) la fin : «لما به بأس» ou «ما به البأس» ou «لما فيه بأس» ? (4) référence exacte entre crochets.'],
  ['z-mayufa2-p91.jpg', 'Introduction de «2. ما يعفى عنه». Transcris lettre par lettre : «هناك أمور فيها معنى الشبهة لكنها ...؛ لذلك لم ... حكمها وصارت من المعفو عنها». Questions : (1) que vient-il exactement après «لكنها» ? (2) le verbe après «لم» : «تتغير» / «تغير» / «نغير» / autre ?'],
  ['z-bukhari2-p91.jpg', 'Hadith de Bukhārī. Transcris lettre par lettre : «شكا إلى النبي ﷺ ... يجد الشيء في الصلاة...». Questions : (1) entre «النبي ﷺ» et «يجد» : y a-t-il «الرجل الذي» ou «الرجل» seul ou autre ? (2) avant «الصلاة» : «في الصلاة» simple ? (3) la question : «أيقطع الصلاة» exactement ?'],
  ['z-tafar3-2-p92.jpg', 'Consigne sous l\'encadré الورع أقسام (une ligne). Transcris-la lettre par lettre. Deux lectures divergentes : (a) «أستخرج أنواع الورع الواردة في النص مع بيان ما يعد منها وما لا يعد من ترك الشبهات»، (b) «متفرع؟...». Quel est le VRAI premier mot — décompose-le lettre par lettre.'],
  ['z-idad2-p92.jpg', 'Rubrique الإعداد القبلي complète. Transcris tout lettre par lettre : la consigne d\'ouverture et les items 1 et 2. Questions : (1) «وأقوم بما يلي» ou «وأنجز ما يلي» ou autre ? (2) item 2 : «أذكر أضرار» ou «أعدد أضرار» ou autre ?'],
];

async function main() {
  const zai = await ZAI.create();
  for (const [img, ask] of ASKS) {
    const p = `${DIR}/${img}`;
    if (!fs.existsSync(p)) { console.log(`ABSENT ${img}`); continue; }
    const out = `${DIR}/vlm-${img.replace('.jpg', '.txt')}`;
    if (fs.existsSync(out)) { console.log(`skip ${img}`); continue; }
    const b64 = fs.readFileSync(p).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: `Zoom très haute résolution d'une ligne ou deux d'un manuel scolaire marocain de hadith, 5e année primaire, leçon 16 «التورع عن الشبهات». ${ask}\n\nAnalyse les glyphes un par un avant de répondre. Réponds d'abord par les CHOIX retenus (numérotés), puis la transcription complète mot à mot avec vocalisation. Un mot illisible : [؟].` },
          { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 1400,
        temperature: 0.1,
      });
      const txt = res?.choices?.[0]?.message?.content ?? JSON.stringify(res);
      fs.writeFileSync(out, txt);
      console.log(`OK ${img} (${txt.length} car)`);
    } catch (e) {
      console.error(`ÉCHEC ${img}: ${e.message}`);
    }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
