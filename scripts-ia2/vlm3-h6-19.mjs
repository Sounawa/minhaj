// IA-2 — vlm3-h6-19.mjs : scrutins VLM ronde 3 — 7 micro-crops + bloc istithmar
// (questions seules ; exécuté avant recyclage).
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const OUT = '/home/z/my-project/pdf-work/h6-15/vlm-l19';
const zai = await ZAI.create();
const jobs = [
  { key: 'p105-sayyi',  img: 'z5-p105-sayyi.png',  q: 'cas de سيئة/واحدة (réponse : سيئةً واحدةً. puis »)' },
  { key: 'p106-hamm2',  img: 'z5-p106-hamm2.png', q: 'mot du milieu de la glose همّ' },
  { key: 'p106-l3mid',  img: 'z5-p106-l3mid.png', q: '2e occurrence همّه/الهمّ/همّ العبد' },
  { key: 'p107-tarak',  img: 'z5-p107-tarak.png', q: 'séquence exacte تركها → ] (réponse : [شاكراً لله] en bleu)' },
  { key: 'p109-L3tail', img: 'z5-p109-L3tail.png',q: 'بحقه/حقه/بحقٍّ avant » (réponse : بحقه)' },
  { key: 'p109-L7tail', img: 'z5-p109-L7tail.png',q: 'حقه/بحقه/حقاً avant ؛ (réponse : حقه)' },
  { key: 'p109-L9mid',  img: 'z5-p109-L9mid.png', q: 'هي نيته + «،» + réf (réponse : هي نيته، فوزرهما)' },
  { key: 'p109-istfull',img: 'z6-p109-istfull.png',q: 'carte des guillemets du hadith Abū Kabsha' },
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1500,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(`${OUT}/${j.key}.txt`, txt);
      console.log(`\n########## ${j.key} ##########\n${txt}`);
      done = true;
    } catch (e) { console.log(`${j.key} tentative ${attempt} échec: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm3-h6-19');
