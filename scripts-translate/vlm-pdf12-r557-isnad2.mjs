import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const b64 = fs.readFileSync('/home/z/my-project/tr-tmp/qa-crops-r557/p80-isnad2.png').toString('base64');
const zai = await ZAI.create();
const res = await zai.createChatCompletionVision({
  messages: [{ role: 'user', content: [
    { type: 'text', text: "Bande supérieure d'une page d'un manuel de hadith. Transcris ligne par ligne, mot à mot, le texte visible. Objectif principal : la CHAÎNE de transmission (isnād) du hadith qui commence par « مَالِكٌ... » et mène à « ...أبي هريرة، أن رسول الله ﷺ قال: يَنْزِلُ... ». Nomme CHAQUE rapporteur dans l'ordre. Si un nom est illisible, écris [illisible] à sa place. Ne complète jamais de mémoire." },
    { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
  ]}],
});
fs.writeFileSync('/home/z/my-project/tr-tmp/vlm-pdf12-r557-isnad2.json', JSON.stringify({r: res.choices[0].message.content}, null, 2));
console.log(res.choices[0].message.content);
