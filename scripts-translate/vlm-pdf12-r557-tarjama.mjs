import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const b64 = fs.readFileSync('/home/z/my-project/tr-tmp/qa-crops-r557/p80-tarjama.png').toString('base64');
const zai = await ZAI.create();
const res = await zai.createChatCompletionVision({
  messages: [{ role: 'user', content: [
    { type: 'text', text: "Bloc « ترجمة الراوي » d'un manuel de hadith (bas de page). Transcris TOUT le bloc mot à mot : nom du rapporteur, sa description, et CHAQUE chiffre de la biographie DIGIT PAR DIGIT (ex. « neuf-trois » pour 93). Si un mot est illisible, écris [illisible]. Ne complète jamais de mémoire." },
    { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
  ]}],
});
fs.writeFileSync('/home/z/my-project/tr-tmp/vlm-pdf12-r557-tarjama.json', JSON.stringify({r: res.choices[0].message.content}, null, 2));
console.log(res.choices[0].message.content);
