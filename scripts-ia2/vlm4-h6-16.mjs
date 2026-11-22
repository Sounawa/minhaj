// IA-2 — vlm4-h6-16.mjs : derniers arbitrages VLM — (1) heading ثانيا + ligne
// d'intro + item 1 p.92 ; (2) référence [الحجرات: …] ordre des chiffres p.94.
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

const QS = [
  ['z13-p92-thani', `Bande d'un manuel scolaire marocain (3600 dpi). Transcris, ligne par ligne de droite à gauche, TOUT ce qui est imprimé : il doit y avoir un SOUS-TITRE coloré ou gras (peut-être «ثانيا: ...»), puis une courte ligne d'introduction, puis le début «1- ...» d'un item. SCRUTIN 1 : le sous-titre complet, mot à mot avec vocalisation. SCRUTIN 2 : la ligne d'intro complète (elle commence peut-être par «مما ...»). SCRUTIN 3 : les quatre premiers mots de l'item 1 (après «1-») : «الالتزام» suivi de quoi exactement — «بما»، «كل ما»، autre ?`],
  ['z5-p94-ref-bw140', `Image binarisée (3600 dpi) : la fin de la dernière ligne d'un encadré de versets coraniques, avec la RÉFÉRENCE entre crochets «[الحجرات: ...]». SCRUTIN : les nombres dans la référence. Décris chaque groupe de chiffres, de DROITE à GAUCHE (l'ordre physique où ils apparaissent sur la ligne) : le groupe le plus à DROITE d'abord, puis le tiret, puis le groupe à GAUCHE. Pour chaque chiffre : est-ce ١ (trait vertical sans boucle) ou ٠ (boucle fermée ronde) ? Conclusion : la référence imprimée se lit-elle «١١ - ١٠» ou «١٠ - ١١» en allant de droite à gauche ?`],
];

for (const [k, q] of QS) {
  const out = `${DIR}/vlm-v4-${k}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${k}`); continue; }
  const img = fs.readFileSync(`${DIR}/${k}.png`).toString('base64');
  console.log(`\n======== ${k} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 2000,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 800 ? txt.slice(0, 650) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000 * attempt); }
  }
  await sleep(2500);
}
console.log('OK vlm4-h6-16');
