// IA-2 — vlm4-h6-19.mjs : scrutins VLM ronde 4 (finale) — glose + takar + بحقه
// + هي نيته + carte des guillemets istithmar (exécuté avant recyclage).
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const OUT = '/home/z/my-project/pdf-work/h6-15/vlm-l19';
const zai = await ZAI.create();
const jobs = [
  { key: 'p106-hamm3',   img: 'z6-p106-hamm3.png',    q: 'الهمُّ (ا-ل-ه-م-م, sans ة) — confirmé' },
  { key: 'p107-tarak3',  img: 'z7-p107-tarak3.png',   q: 'après تركها : [شاكراً لله] en bleu' },
  { key: 'p109-L3haq2',  img: 'z8-p109-L3haq2.png',   q: 'بحقه (bā\' point dessous confirmé)' },
  { key: 'p109-L9niyya', img: 'z8-p109-L9niyya.png',  q: 'هي نيته + «،»' },
  { key: 'p109-istfull', img: 'z6-p109-istfull.png',  q: 'carte des guillemets (l1 ouvre, l4/l8 ouvrent, l5/l9 ferment)' },
];
for (const j of jobs) {
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const img = fs.readFileSync(`${DIR}/${j.img}`).toString('base64');
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: j.q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1400,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(`${OUT}/${j.key}.txt`, txt);
      console.log(`\n########## ${j.key} ##########\n${txt}`);
      done = true;
    } catch (e) { console.log(`${j.key} tentative ${attempt} échec: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm4-h6-19');
