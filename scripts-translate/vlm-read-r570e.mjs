import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const C = '/home/z/my-project/tr-tmp/qa-crops-r570';
const qs = [
  { img: `${C}/q5-p169-aya-line.png`, t: 800,
    ask: `Ligne(s) très zoomée(s) d'un manuel arabe : après «... وجوبا؛ لقوله تعالى:» vient une citation coranique entre guillemets « ... » puis [سورة البقرة الآية: ١٨٤] en rouge. Transcris EXACTEMENT la citation coranique mot à mot telle qu'imprimée (orthographe warš maghrébine), puis le nombre. Format :\nAYA: <texte exact mot à mot>\nNUM: <chiffres>` },
];
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
async function main() {
  const zai = await ZAI.create();
  for (const q of qs) {
    const b64 = fs.readFileSync(q.img).toString('base64');
    let res = null, attempt = 0;
    while (res === null && attempt < 5) {
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
        console.error(`retry ${attempt} : ${e.message}`);
        await sleep(25000);
      }
    }
    console.log('=== ' + q.img.split('/').pop() + ' ===');
    console.log(res ? res.choices[0].message.content : 'ECHEC');
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
