import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const OUT = '/home/z/my-project/pdf-work/h6-15/vlm-l20';
fs.mkdirSync(OUT, { recursive: true });
const zai = await ZAI.create();
const jobs = [
  { key: 'p113-maidaref-digits', img: 'z6-p113-maidaref.png',
    q: `Fin d'une ligne d'un encadré coranique (4800 dpi) : «...فإن حزب الله هم الغالبون [المائدة: ___]». UNIQUE QUESTION : quels sont les CHIFFRES exacts de la référence après «المائدة:» ? Décris chaque chiffre un par un (٥٥-٥٦ ? ٥٧-٥٨ ? autre ?). Y a-t-il un tiret entre les deux nombres ?` },
  { key: 'p112-qadar', img: 'z6-p112-qadar.png',
    q: `Ligne d'un manuel scolaire (3600 dpi) : «فالفرائض لتحقيق القدر الواجب ___ التزكية والاستقامة؛». SCRUTIN : entre «الواجب» et «التزكية» : y a-t-il «مِنْ» (mīm-nūn), «فِي» (fā'-yā'), «لِ» (lām), ou RIEN (jonction directe) ? Transcris la ligne entière mot à mot.` },
  { key: 'p113-yust3c', img: 'z6-p113-yust3c.png',
    q: `Item d'une liste d'un manuel (4800 dpi) : «- محبة الله لأوليائه توجب ___ ودوام مودتهم وعدم معاداتهم.». SCRUTIN : le mot après «توجب» : «مَحَبَّتَهُمْ» (mīm-ḥā'-bā'-tā'-hā'-mīm) seul, ou «وُجُودَ مَحَبَّتِهِمْ» (wāw-ǧīm-wāw-dāl = existence + محبتهم), ou autre ? Décris les consonnes. Transcris l'item complet.` },
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 900,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(`${OUT}/${j.key}.txt`, txt);
      console.log(`\n########## ${j.key} ##########\n${txt}`);
      done = true;
    } catch (e) { console.log(`${j.key} tentative ${attempt} échec: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm2-h6-20');
