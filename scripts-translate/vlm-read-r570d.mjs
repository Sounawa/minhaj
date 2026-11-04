import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const C = '/home/z/my-project/tr-tmp/qa-crops-r570';
const qs = [
  { img: `${C}/q4-p165-aicha.png`, t: 700,
    ask: `Ligne très zoomée d'un manuel arabe : citation de عائشة entre guillemets, se terminant par «... من رسول الله ﷺ ...؟». Transcris la citation EXACTEMENT mot à mot. Si un mot suit رسول الله avant le ؟, transcris-le précisément. Format :\nCITATION: <texte exact>` },
  { img: `${C}/q4-p166-mithl.png`, t: 700,
    ask: `Bande zoomée d'un manuel arabe (récit de l'homme qui embrassa sa femme en jeûnant). Une ligne contient وقال: puis une phrase avec رسول الله et la comparaison (مِثل). Transcris EXACTEMENT cette phrase mot à mot. Format :\nPHRASE: <texte exact>` },
  { img: `${C}/q4-p166-hamza-full.png`, t: 900,
    ask: `Hadith complet d'un manuel arabe : مالك عن هشام بن عروة عن أبيه que حمزة بن عمرو الأسلمي demanda au Prophète ﷺ s'il peut jeûner en voyage, avec la réponse «إن شئت فصم وإن شئت أفطر» et le crochet [الموطأ رقم: ٨١٢]. Transcris intégralement mot à mot, du début de la chaîne au crochet. Format :\nHADITH: <texte exact>` },
  { img: `${C}/q4-p169-taala.png`, t: 800,
    ask: `Zone zoomée d'un manuel arabe : après «لقوله تعالى:» il y a une citation coranique entre guillemets puis [سورة البقرة الآية: ١٨٤]. Transcris EXACTEMENT la citation coranique mot à mot (orthographe warš imprimée) et le nombre. Format :\nAYA: <texte exact>\nNUM: <chiffres>` },
  { img: `${C}/q4-p170-fin-829.png`, t: 700,
    ask: `Ligne zoomée d'un manuel arabe : fin d'un passage cité de مالك se terminant par «... فيما عني؟» ou similaire, puis «وذلك أحب ما سمعت إليه في ذلك» puis le crochet [الموطأ رقم: ٨٢٩]. Transcris EXACTEMENT les derniers mots avant le crochet, la phrase وذلك أحب..., et le nombre. Format :\nFIN_PHRASE: <texte exact>\nNUM: <chiffres>` },
];
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
async function main() {
  const zai = await ZAI.create();
  for (const q of qs) {
    const b64 = fs.readFileSync(q.img).toString('base64');
    let res = null, attempt = 0;
    while (res === null && attempt < 4) {
      attempt++;
      try {
        res = await zai.createChatCompletionVision({
          messages: [{ role: 'user', content: [
            { type: 'text', text: q.ask },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
          ]}],
          model: 'glm-5v-turbo', max_tokens: q.t,
        });
      } catch (e) {
        console.error(`retry ${attempt} ${q.img.split('/').pop()} : ${e.message}`);
        await sleep(30000);
      }
    }
    console.log('=== ' + q.img.split('/').pop() + ' ===');
    console.log(res ? res.choices[0].message.content : 'ECHEC');
    console.log('');
    await sleep(3000);
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
