import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const C = '/home/z/my-project/tr-tmp/qa-crops-r570';
const qs = [
  { img: `${C}/q3-p165-kilta.png`, t: 700,
    ask: `Ligne(s) d'un manuel arabe à très haute résolution : un hadith de عائشة زوج النبي ﷺ avec sa citation entre guillemets « ... ? » et le crochet [الموطأ، رقم: 805]. Transcris EXACTEMENT la citation de عائشة mot à mot, en particulier le(s) mot(s) entre رسول الله ﷺ et le ؟. Format :\nCITATION: <texte exact entre guillemets>\nAPRES: <mot(s) exacts entre رسول الله et ؟>` },
  { img: `${C}/q3-p166-mithl.png`, t: 700,
    ask: `Bande d'un manuel arabe à haute résolution (récit d'un homme qui a embrassé sa femme en jeûnant, retour de la femme, réaction de l'époux). Transcris UNIQUEMENT la phrase contenant رسول الله et يَحِل/يحل (la réaction de l'époux, environ : وقال ... رسول الله ... يحل لرسوله ما شاء). Format :\nPHRASE: <texte exact mot à mot>` },
  { img: `${C}/q3-p166-hamza.png`, t: 800,
    ask: `Bande d'un manuel arabe à haute résolution : hadith complet de حمزة بن عمرو الأسلمي (chaîne مالك عن هشام بن عروة عن أبيه, sa question au Prophète ﷺ, la réponse, le crochet [الموطأ رقم: NNN]). Transcris intégralement mot à mot. Format :\nHADITH: <texte exact complet>` },
  { img: `${C}/q3-p166-hamza-bracket.png`, t: 500,
    ask: `Fin de hadith d'un manuel arabe à très haute résolution, avec le crochet final [الموطأ رقم: NNN]. Transcris la fin de la réponse prophétique (entre guillemets) et le nombre chiffre par chiffre. Format :\nFIN: <fin exacte de la citation>\nNUM: <chiffres>` },
  { img: `${C}/q3-p169-aya-1152.png`, t: 800,
    ask: `Zone d'un manuel arabe à très haute résolution : une phrase introductive (ومن أراد الخروج لسفر في رمضان...), puis «لقوله تعالى:», puis une citation coranique entre guillemets, puis [سورة البقرة الآية: NNN]. Transcris EXACTEMENT la citation coranique mot à mot (orthographe warš imprimée) puis le nombre. Format :\nAYA: <texte exact>\nNUM: <chiffres>` },
  { img: `${C}/q3-p170-829-864.png`, t: 800,
    ask: `Zone d'un manuel arabe haute résolution : passage de la rubrique استدلال sur le jeûne de l'année entière (صيام الدهر). Transcris intégralement le texte arabe imprimé mot à mot depuis le début de la phrase (après le titre الاستدلال) jusqu'au crochet [الموطأ رقم: NNN], y compris «وذلك أحب ما سمعت إليه في ذلك». Format : transcription continue mot à mot.` },
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
