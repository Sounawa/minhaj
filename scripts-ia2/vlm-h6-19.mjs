// IA-2 — vlm-h6-19.mjs : scrutins VLM L19 ronde 1 — 17 points douteux (pp.105-109).
// Exécuté avant le recyclage du bac ; adjudications consignées au worklog Z2-55.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const OUT = '/home/z/my-project/pdf-work/h6-15/vlm-l19';
fs.mkdirSync(OUT, { recursive: true });
const zai = await ZAI.create();

const jobs = [
  { key: 'p105-cart',    img: 'z1-p105-cart-vlm.png',    q: 'Cartouche : numéro (18/١٨ ?) + titre exact.' },
  { key: 'p105-matn12',  img: 'z3-p105-matn12-vlm.png',  q: 'يروي/يرويه ? عن/عنه ? guillemet après قال: ? shadda sur إنّ ?' },
  { key: 'p105-matn6',   img: 'z3-p105-matn6-vlm.png',   q: 'سيئةً/سيئةٌ ? عنده entre كتبها الله et سيئة ? réf mot à mot ?' },
  { key: 'p106-hamm',    img: 'z3-p106-hamm-vlm.png',    q: 'glose همّ : mot du milieu الهمّة/الهمّ/ألَه ?' },
  { key: 'p106-tahlil',  img: 'z3-p106-tahlil-vlm.png',  q: 'أن جعل همّ العبد ou همّه ? et la 2e occurrence ? عشراً/عشر ?' },
  { key: 'p107-lataf',   img: 'z3-p107-lataf-vlm.png',   q: 'كتبها الله عنده/عنه حسنة ?' },
  { key: 'p107-item1a',  img: 'z3-p107-item1a-vlm.png',  q: 'point après بالقلب. exact ?' },
  { key: 'p107-item1c',  img: 'z3-p107-item1c-vlm.png',  q: 'après تركها : لله / شاكراً ? où se ferme ] ?' },
  { key: 'p107-item2',   img: 'z3-p107-item2-vlm.png',   q: 'وإيقاعها ou ووقوعها ?' },
  { key: 'p108-item3',   img: 'z3-p108-item3-vlm.png',   q: 'أزكى/أرقى ? verbe استُصلحت/استُخصبت/استُحصدت lettre à lettre ?' },
  { key: 'p108-item4',   img: 'z3-p108-item4-vlm.png',   q: 'citation coranique mot à mot + réf [النحل: ٩٧?] chiffres exacts ?' },
  { key: 'p108-item4b',  img: 'z3-p108-item4b-vlm.png',  q: 'يحيط به / يحصره / يعده ?' },
  { key: 'p108-item5',   img: 'z3-p108-item5-vlm.png',   q: 'mot avant ألفاً : وللأول/وللثالث ? logique 10→100→1000 ?' },
  { key: 'p108-yust',    img: 'z3-p108-yust-vlm.png',    q: 'item 3 : تبشير/تنعيم + الفائزين/الفوز ? item 4 : الإيمان/اليقين ?' },
  { key: 'p109-ist1',    img: 'z3-p109-ist1-vlm.png',    q: 'ligne L2/L3 : ويعمل/ويعلم + بحقه/حقه ?' },
  { key: 'p109-ist2',    img: 'z3-p109-ist2-vlm.png',    q: 'L7 : ويعمل/ويعلم + بحقه/حقه/بحقٍّ ?' },
  { key: 'p109-ist4',    img: 'z3-p109-ist4-vlm.png',    q: 'L9 : فهو بنيته/هي نيته ? réf chiffres 29/562 ?' },
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1600,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(`${OUT}/${j.key}.txt`, txt);
      console.log(`\n########## ${j.key} ##########\n${txt}`);
      done = true;
    } catch (e) { console.log(`${j.key} tentative ${attempt} échec: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm-h6-19');
