import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const b64 = fs.readFileSync('/home/z/my-project/tr-tmp/qa-crops-r557/p85-band2.png').toString('base64');
const zai = await ZAI.create();
const res = await zai.createChatCompletionVision({
  messages: [{ role: 'user', content: [
    { type: 'text', text: "Tu lis une bande d'une page d'un manuel scolaire marocain de hadith. Transcris TOUT le texte arabe imprimé visible, ligne par ligne, de haut en bas, mot à mot. Pour le renvoi entre crochets [الموطأ رقم: ...] transcris le chiffre DIGIT PAR DIGIT (ex. « cinq-huit-quatre »). Si un mot est illisible, écris [illisible]. N'invente RIEN." },
    { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
  ]}],
});
console.log(res.choices[0].message.content);
