// IA-2 — vlm2-h6-19.mjs : scrutins VLM ronde 2 — micro-crops 4800/3600
// (لن ي garder que les questions ; réponses exécutées avant recyclage).
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const OUT = '/home/z/my-project/pdf-work/h6-15/vlm-l19';
fs.mkdirSync(OUT, { recursive: true });
const zai = await ZAI.create();

const jobs = [
  { key: 'p105-l5start', img: 'z4-p105-l5start.png', q: 'guillemet fermant après كثيرة ? (réponse : NON)' },
  { key: 'p105-l6',      img: 'z4-p105-l6.png',      q: 'vocalisation سيئة/واحدة + position de » (réponse : سيئةً واحدةً. puis »)' },
  { key: 'p106-hamm',    img: 'z4-p106-hamm.png',    q: 'الهمّة/الهمّ ?' },
  { key: 'p106-tafaddul',img: 'z4-p106-tafaddul.png',q: 'تفضُّل/فضل/تفضيل ? (réponse : تفضُّل avec tā\' + shadda)' },
  { key: 'p106-l3',      img: 'z4-p106-l3.png',      q: 'وجعل همّه/الهمّ/همّ العبد بالسيئة ?' },
  { key: 'p107-tarak',   img: 'z4-p107-tarak.png',   q: 'après تركها : شاكراً لله + crochets ?' },
  { key: 'p108-azka',    img: 'z4-p108-azka.png',    q: 'أزكى×2 + استُصلحت lettre à lettre ?' },
  { key: 'p108-yust3',   img: 'z4-p108-yust3.png',   q: 'تبشير/تنعيم + الفائزين/الفوز ?' },
  { key: 'p109-istL3',   img: 'z4-p109-istL3.png',   q: 'ويعمل/ويعلم + بحقه/حقه/بحقٍّ ?' },
  { key: 'p109-istL5',   img: 'z4-p109-istL5.png',   q: 'clause فهو بنيته entre فلان» et قال: فأجرهما ? (réponse : OUI)' },
  { key: 'p109-istL7',   img: 'z4-p109-istL7.png',   q: 'يعمل/يعلم + حقه/بحقه/حقاً ?' },
  { key: 'p109-istL9',   img: 'z4-p109-istL9.png',   q: 'هي نيته + réf 29/562 ?' },
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
console.log('OK vlm2-h6-19');
