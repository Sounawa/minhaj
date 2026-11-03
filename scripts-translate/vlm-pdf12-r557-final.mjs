import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const b64 = fs.readFileSync('/home/z/my-project/tr-tmp/qa-crops-r555/composite-p80.png').toString('base64');
const zai = await ZAI.create();
const res = await zai.createChatCompletionVision({
  messages: [{ role: 'user', content: [
    { type: 'text', text: "Image d'un manuel de hadith marocain. Deux questions ONLY: (1) En HAUT de l'image, transcris l'isnād COMPLET du hadith qui commence par « عن/مالك » et se termine par « أبي هريرة أن رسول الله ﷺ قال: يَنْزِلُ?? ربُّنا... » — mot à mot, y compris les noms intermédiaires (ex. مالك عن... بن... عن... عن...). Si un nom est coupé, écris [coupé]. (2) En BAS, transcris le bloc « ترجمة الراوي » : le nom du raoui, sa description, et TOUS les chiffres de sa biographie DIGIT PAR DIGIT (ex. « neuf-deux »). N'invente RIEN." },
    { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
  ]}],
});
fs.writeFileSync('/home/z/my-project/tr-tmp/vlm-pdf12-r557-final.json', JSON.stringify({r: res.choices[0].message.content}, null, 2));
console.log(res.choices[0].message.content);
