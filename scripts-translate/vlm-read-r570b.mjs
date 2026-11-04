import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

// R570 — pass 2 : arbitrages ponctuels (chiffres p.169 + āyas + passages exacts)
const C = '/home/z/my-project/tr-tmp/qa-crops-r570';
const qs = [
  { img: `${C}/b-p169-816a.png`, t: 500,
    ask: `Bande d'un manuel arabe. Elle contient un crochet de renvoi [الموطأ رقم: NNN] ou [الموطاء رقم: NNN]. Trouve ce crochet et transcris UNIQUEMENT le nombre NNN chiffre par chiffre (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9). Format :\nNUM: <chiffres>\nMOT_AVANT: <les 3 derniers mots avant le crochet>` },
  { img: `${C}/b-p169-816b.png`, t: 500,
    ask: `Bande d'un manuel arabe. Elle contient un crochet de renvoi [الموطأ رقم: NNN]. Trouve ce crochet et transcris UNIQUEMENT le nombre chiffre par chiffre. Format :\nNUM: <chiffres>\nMOT_AVANT: <les 3 derniers mots avant le crochet>` },
  { img: `${C}/b-p169-817.png`, t: 500,
    ask: `Bande d'un manuel arabe (passage sur un homme qui revient de voyage مفطر pendant que sa femme est purifiée des règles). Elle contient un crochet [الموطأ رقم: NNN]. Transcris le nombre chiffre par chiffre. Format :\nNUM: <chiffres>\nMOT_AVANT: <les 3 derniers mots avant le crochet>` },
  { img: `${C}/b-p169-haut-aya184.png`, t: 900,
    ask: `Haut d'une page d'un manuel arabe. Il y a une citation coranique entre guillemets « ... » suivie de [سورة البقرة الآية: NNN]. Transcris EXACTEMENT le texte coranique imprimé mot à mot (orthographe warš comme imprimée), puis le nombre. Format :\nAYA: <texte exact>\nNUM: <chiffres>` },
  { img: `${C}/b-p168-811-aya.png`, t: 900,
    ask: `Bande d'un manuel arabe. Elle contient : un crochet [الموطأ رقم: NNN], puis une phrase introductive (فإنه أفضل من الفطر لمن قدر عليه لقوله تعالى), puis une citation coranique courte entre guillemets « ... » suivie de [سورة البقرة الآية: NNN]. Transcris EXACTEMENT la citation coranique imprimée mot à mot, puis le nombre. Format :\nAYA: <texte exact>\nNUM: <chiffres>\nPHRASE_AVANT: <la phrase avant la citation>` },
  { img: `${C}/b-p165-intro-b-805.png`, t: 900,
    ask: `Bande d'un manuel arabe : suite d'une introduction sur le jeûne et le baiser (القبلة), avec un hadith de عائشة se terminant par un crochet [الموطأ رقم: NNN]. Transcris intégralement le texte arabe imprimé mot à mot, y compris la citation entre guillemets de عائشة et le crochet final. Format : transcription ligne à ligne, ne traduis pas.` },
  { img: `${C}/b-p166-had1-a.png`, t: 900,
    ask: `Haut de la rubrique الأحاديث d'un manuel arabe : chaîne de transmission d'un hadith (مالك عن ... عن ...) puis début du récit (un homme embrasse sa femme en jeûnant). Transcris intégralement le texte arabe imprimé mot à mot. Ne traduis pas.` },
  { img: `${C}/b-p166-had2-812.png`, t: 900,
    ask: `Bande d'un manuel arabe : fin d'un hadith dont la réponse du Prophète est «إن شئت فصم وإن شئت أفطر» suivie du crochet [الموطأ رقم: NNN]. Transcris intégralement le texte arabe imprimé mot à mot (y compris le début de la chaîne مالك عن هشام بن عروة عن أبيه عن حمزة بن عمرو الأسلمي si visible), la question posée, la réponse et le crochet. Ne traduis pas.` },
  { img: `${C}/b-p166-815.png`, t: 700,
    ask: `Bande d'un manuel arabe : passage rapporté de مالك (انه بلغه) sur عمر بن الخطاب qui rentre à Médine. Transcris intégralement le texte arabe imprimé mot à mot avec le crochet final [الموطأ رقم: NNN]. Ne traduis pas.` },
  { img: `${C}/b-p170-829.png`, t: 900,
    ask: `Bande d'un manuel arabe : passage (rubrique استدلال) citant l'avis des savants sur le jeûne continu (صيام الدهر) avec les jours interdits (الأضحى والفطر) et un crochet [الموطأ رقم: NNN] se terminant par «وذلك أحب ما سمعت إليه في ذلك». Transcris intégralement le texte arabe imprimé mot à mot, crochets inclus. Ne traduis pas.` },
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
