import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

// R570 — pdf-25 (leçon 24, القبلة للصائم والصيام في السفر, p.165-170)
// Passe d'arbitrage : nombres Muwaṭṭaʾ + transcriptions des bandes composites.
const C = '/home/z/my-project/tr-tmp/qa-crops-r570';
const qs = [
  { img: `${C}/nums-165.png`,
    ask: `Chaque bloc de cette image (empilement vertical, fond rose pâle) contient un crochet de renvoi d'un manuel arabe : [الموطأ. رقم: NNN] (ou similaire). Transcris le nombre NNN chiffre par chiffre pour CHAQUE bloc, de haut en bas (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9). Format :\nBLOC1: <chiffres>\nBLOC2: <chiffres>` },
  { img: `${C}/nums-166.png`,
    ask: `Chaque bloc de cette image (empilement vertical) contient soit un crochet [الموطأ. رقم: NNN] soit une année (سنة NN هـ). Transcris chaque nombre chiffre par chiffre, de haut en bas. Format :\nBLOC1: <chiffres>\nBLOC2: ...\n(indique aussi le mot juste avant le nombre : رقم ou سنة)` },
  { img: `${C}/nums-167.png`,
    ask: `Bloc unique : crochet [الموطأ. رقم: NNN]. Transcris le nombre chiffre par chiffre. Format :\nNUM: <chiffres>` },
  { img: `${C}/nums-168.png`,
    ask: `Chaque bloc contient soit [الموطأ رقم: NNN] soit [سورة البقرة الآية: NNN]. Transcris chaque nombre chiffre par chiffre de haut en bas, en indiquant الموطأ ou البقرة. Format :\nBLOC1: <mot> <chiffres>\nBLOC2: ...` },
  { img: `${C}/nums-169.png`,
    ask: `Chaque bloc contient soit [الموطأ رقم: NNN] soit [سورة البقرة الآية: NNN]. Transcris chaque nombre chiffre par chiffre de haut en bas, en indiquant الموطأ ou البقرة. Format :\nBLOC1: <mot> <chiffres>\nBLOC2: ...` },
  { img: `${C}/nums-170.png`,
    ask: `Bloc unique : crochet [الموطأ. رقم: NNN]. Transcris le nombre chiffre par chiffre. Format :\nNUM: <chiffres>` },
  { img: `${C}/comp-A.jpg`,
    ask: `Trois bandes superposées (fond rose) d'une page de manuel arabe : 1) bandeau أهداف الدرس (objectifs numérotés), 2) introduction, 3) suite de l'introduction avec un hadith et son crochet [الموطأ رقم: NNN]. Transcris intégralement le texte arabe imprimé de chaque bande, mot à mot, séparées par ===. Illisible → transcris ce que tu vois et marque ⟨?⟩. Ne traduis pas.` },
  { img: `${C}/comp-B.jpg`,
    ask: `Trois bandes superposées d'un manuel arabe : le hadith n°1 de la leçon (un homme embrasse sa femme en ramadan, histoire avec أم سلمة). Transcris intégralement le texte arabe imprimé des trois bandes mot à mot, séparées par ===, y compris la chaîne de transmission (عن ... عن ...) et le crochet final [الموطأ رقم: NNN]. Illisible → ⟨?⟩. Ne traduis pas.` },
  { img: `${C}/comp-C.jpg`,
    ask: `Trois bandes superposées d'un manuel arabe : 1) fin d'un hadith + un deuxième hadith court se terminant par «إن شئت فصم وإن شئت أفطر» avec crochet [الموطأ رقم: NNN], 2) un passage sur عمر بن الخطاب avec crochet [الموطأ رقم: NNN], 3) rubrique ترجمة الراوي (biographie de عروة). Transcris intégralement mot à mot, bandes séparées par ===, crochets inclus. Illisible → ⟨?⟩. Ne traduis pas.` },
  { img: `${C}/comp-D.jpg`,
    ask: `Trois bandes superposées d'un manuel arabe : 1) sous-titre ثانيا : الصيام في السفر, 2) passage d'analyse citant عائشة avec crochet [الموطأ رقم: NNN], 3) passage citant ابن عباس (année de la conquête, الكديد) avec crochet [الموطأ رقم: NNN]. Transcris intégralement mot à mot, séparées par ===. Illisible → ⟨?⟩. Ne traduis pas.` },
  { img: `${C}/comp-E.jpg`,
    ask: `Trois bandes superposées d'un manuel arabe : 1) passage citant أنس avec crochet [الموطأ رقم: NNN] puis une citation coranique [سورة البقرة الآية: NNN], 2) une citation coranique en haut de page [سورة البقرة الآية: NNN] + suite, 3) passage de مالك avec crochet [الموطأ رقم: NNN]. Transcris intégralement mot à mot, séparées par ===, versets coraniques exacts comme imprimés. Illisible → ⟨?⟩. Ne traduis pas.` },
  { img: `${C}/comp-F.jpg`,
    ask: `Trois bandes superposées d'un manuel arabe : 1) suite d'un passage de مالك (entrer chez soi avant l'aube) avec crochet [الموطأ رقم: NNN], 2) passage de مالك sur celui qui veut voyager (طلع له الفجر بأرضه) avec crochet [الموطأ رقم: NNN], 3) passage avec crochet [الموطأ رقم: NNN] (fin : وقد أحب ما سمعت إليه في ذلك) + rubrique التقويم. Transcris intégralement mot à mot, séparées par ===. Illisible → ⟨?⟩. Ne traduis pas.` },
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
          model: 'glm-5v-turbo', max_tokens: 1600,
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
