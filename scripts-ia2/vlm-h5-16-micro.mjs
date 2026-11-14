// Z2-18 — adjudication microcrops leçon 16 hadith-5ep
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-16';

const ASKS = [
  ['mc-obj3-p88.jpg', 'Objectif n°3 du cours. Transcris-le mot à mot. Question précise : quel est le verbe après «أن» (أتجنب؟ أبتعد؟ غير) et y a-t-il une préposition «عن» ? Le mot final est-il «عبادتي ومعامتي» (singulier) ou «عباداتي ومعاملاتي» (pluriel) ?'],
  ['mc-tamhid1-p88.jpg', 'Début du تمهيد. Transcris mot à mot : la première phrase (طريق الإسلام محجة...) puis la citation du Prophète entre guillemets SANS EN RIEN ABRÉGER, et la référence entre crochets [سنن ابن ماجه؟ ...].'],
  ['mc-tamhid2-p88.jpg', 'Suite du تمهيد. Transcris mot à mot : «لكنه قد تعرض...». Question précise : après «ولا الحلال من الحرام» y a-t-il «ولا أن الشيء من الواجبات أم لا؟» et «ولا أنه من المعروف أو من المنكر؟» — transcris exactement les mots interrogatifs (أم / أو).'],
  ['mc-hadithbox-p88.jpg', 'Encadré du hadith (isnād + matn + référence). Transcris tout, y compris la ligne de référence sous l\'encadré : [رواه الترمذي والنسائي...] exactement (y a-t-il «وقال: حديث حسن صحيح» ?).'],
  ['mc-rawi2-p89.jpg', 'Fin de la traduction du rapporteur. Transcris mot à mot : «وُلد منتصف رمضان...». Question précise : «ومات سنة...» — quel est le chiffre exact (أربع وأربعين؟ تسع وأربعين؟) ?'],
  ['mc-sharh-p89.jpg', 'Encadré الفهم/الشرح. Transcris mot à mot les trois gloses : «سبط: ...»، «دع: ...»، «يريبك/يُريبك: بفتح... وضم...، من راب وأراب، ... مشتق من الريب/الريبة وهو/هي الشك». Précise la vocalisation du mot-vedette de la 3e glose.'],
  ['mc-awwalan-p89.jpg', 'Passage أولا: معنى الشبهات. Transcris mot à mot. Question précise : les deux termes définis sont-ils «الحلال اليقين» et «الحرام البين» ou «الحلال البين» et «الحرام البين» ? Et la définition de الشبهة se termine par quoi exactement ?'],
  ['mc-warajtinib-p90.jpg', 'Haut de page 90. Transcris mot à mot : la ligne «فالورع اجتناب...» (اجتنابها؟ اجتنابه؟) et la référence entre crochets (عمدة القاري للعيني بتصرف؟).'],
  ['mc-thaniya-p90.jpg', 'Ouverture de ثانيا. Transcris mot à mot. Questions précises : (1) le premier verbe est-il «حثّ النبيُّ» ? (2) après «للتباسها» y a-t-il «وخفائها» ou «وحفاظها» ou «وحذرها» ? (3) «وذلك أن الأحكام الشرعية على قسمين» ou «ذلك أن...» ?'],
  ['mc-ay-p90.jpg', 'Passage du sens du hadith. Transcris mot à mot : «أي: ...». Question précise : après «من الأقوال والأعمال» quel est le verbe exact avant «إلى ما لا تشك فيه منها» (وننجز؟ ونجت؟ وننتقل؟ وننتهي؟) ?'],
  ['mc-tirmidhi-p90.jpg', 'Hadith de Tirmidhī. Transcris-le mot à mot. Questions précises : (1) «حتى يتّرك» ou «حتى يدع» ? (2) le mot après «ما لا بأس به» : «محافظة» / «مخافة» / «محاذرة» ? (3) la fin : «لما به بأس» / «ما به البأس» / «لما فيه بأس» ? (4) référence exacte.'],
  ['mc-mayufa-p91.jpg', 'Introduction de «2. ما يعفى عنه من الشبهات». Transcris mot à mot. Questions précises : (1) après «لكنها» : «لم تتحقق فيها» ou autre chose (غلب على الظن حلها؟) ? (2) «لم تغير حكمها» ou «لم تعط حكمها» ou autre ? (3) «وصارت من المعفو عنها» exact ?'],
  ['mc-wswas-p91.jpg', 'Deuxième item de ما يعفى عنه. Transcris mot à mot. Questions précises : (1) «فإنه يبني على اليقين» ou «ينبغي أن يبني» ou «ينبني» ? (2) «ولا يلتفت إلى الشك» ou «ولا يفت للشك» ? (3) «كمن غلب عليه الشك» ou «أغلب عليه الشك» ?'],
  ['mc-bukhari-p91.jpg', 'Hadith de Bukhārī (l\'homme qui s\'imagine avoir rompu ses ablutions). Transcris mot à mot, exactement comme imprimé : «شكى إلى النبي ﷺ الرجل الذي...؟ يجد الشيء في الصلاة... أيقطع الصلاة؟ فقال: لا، حتى يجد ريحا أو يسمع صوتا. وهو محمول على الذي...». Y a-t-il «يُخيَّل إليه أنه» dans le texte imprimé ?'],
  ['mc-yustafad-p91.jpg', 'Premier item de «ومما يستفاد من الحديث». Transcris mot à mot. Questions précises : (1) «أن الحلال المحض» ou «الحلال المحضّ» ? (2) «لا يحصل للمؤمن في قلبه منه ريب أو حرج» exact ? (3) «بل تسكن إليه النفس ويطمئن به القلب» exact ?'],
  ['mc-taqwim-p92.jpg', 'Rubrique التقويم. Transcris mot à mot les DEUX questions, et surtout la fin de la question 1 : «وأمثل لكل نوع منها بمثال» exact ? Y a-t-il une ligne ou un mot supplémentaire ?'],
  ['mc-wara3-1-p92.jpg', 'Première division de l\'encadré «الورع أقسام». Transcris mot à mot : «ورع الصديقين، وهو: ترك ما لا ...؟... نية القوة على العبادة». Question précise : «ما لا يتناول» ou «ما يتناول» ou «ما لا يتناوله» ?'],
  ['mc-tafar3-p92.jpg', 'Consigne sous l\'encadré de l\'استثمار. Transcris-la mot à mot. Question précise : quel est le premier mot (أستخرج؟ متفرع؟ غيره) et la construction complète «... مع بيان ما يعد منها وما لا يعد من ...؟» ?'],
  ['mc-idad-p92.jpg', 'Rubrique الإعداد القبلي complète. Transcris mot à mot la consigne d\'ouverture (أحفظ حديث الدرس المقبل وأقوم بما يلي؟) et les items 1 et 2 (avec le verbe exact de l\'item 2 et le mot أضرار/أصرار).'],
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
          { type: 'text', text: `Extrait très haute résolution d'un manuel scolaire marocain de hadith (5e année primaire), leçon 16 «التورع عن الشبهات». ${ask}\n\nTranscris fidèlement, mot à mot, avec la vocalisation imprimée. Un mot illisible : [؟]. Réponds UNIQUEMENT avec la transcription (et si la question demande un choix, mets le choix retenu en tête, puis la transcription).` },
          { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 1600,
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
