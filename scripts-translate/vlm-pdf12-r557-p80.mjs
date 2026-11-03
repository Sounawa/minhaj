// vlm-pdf12-r557-p80.mjs — R557 : lecture page d'ouverture leçon 11 (composite-p79).
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const b64 = fs.readFileSync('/home/z/my-project/tr-tmp/qa-crops-r555/composite-p79.png').toString('base64');
const zai = await ZAI.create();
const res = await zai.createChatCompletionVision({
  messages: [{ role: 'user', content: [
    { type: 'text', text: "Tu lis une page d'un manuel scolaire marocain de hadith (Muwaṭṭa' Mālik, 2e année collégiale). Transcris EXACTEMENT, ligne par ligne : (1) les objectifs numérotés du haut de page (١- ٢- ٣- ...), (2) le paragraphe d'introduction avec la citation coranique et son renvoi entre crochets (chiffres exacts), (3) le hadith d'après Abū Mūsā avec son isnād complet mot à mot, son matn et son renvoi, (4) l'intitulé « أحاديث الدرس » et le début du premier hadith : l'isnād COMPLET du premier hadith (de « عن أبي بكر » jusqu'à « قال ») mot à mot — s'il y a un mot incertain, écris [illisible] plutôt que d'inventer." },
    { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
  ]}],
});
fs.writeFileSync('/home/z/my-project/tr-tmp/vlm-pdf12-r557-p79.json', JSON.stringify({r: res.choices[0].message.content}, null, 2));
console.log(res.choices[0].message.content);
