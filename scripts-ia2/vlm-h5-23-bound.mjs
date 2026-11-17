// Z2-27 — hadith-5ep leçon 23 — bornage : p127-p131 (fin attendue ~p.129 ; prochaine leçon = درس 25 du livre)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-23';
const COMMON = `Page entière (150 dpi) d'un manuel scolaire marocain d'hadith (5e année primaire traditionnel), sens de lecture droite→gauche.
TRANSCRIS TOUT ce qui est imprimé sur la page, rubrique par rubrique, mot à mot, avec la vocalisation. Balise les titres de rubrique comme [TITRE] ... [/TITRE], les encadrés comme [CADRE] ... [/CADRE]. Les bandeaux décoratifs illisibles : [؟]. Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé.`;

const Q = {
  127: `Page 127 : suite de la leçon «التقوى وحسن الخلق» (hadith d'Abû Dharr et Muʿâdh). Transcris tout : at-taḥlīl, istinbāṭ, wa-mimmā yustafād, at-taqwīm...`,
  128: `Page 128 : suite ou FIN de la leçon «التقوى وحسن الخلق» ? Cherche at-taqwīm (التقويم) et al-iʿdād al-qabliyy (الإعداد القبلي). Y a-t-il en bas de page le bandeau de la leçon SUIVANTE (الدَّرْسُ 25) ? Transcris tout.`,
  129: `Page 129 : cette page contient-elle la FIN de la leçon «التقوى وحسن الخلق» (تقويم + إعداد قبلي) ou le DÉBUT de la leçon suivante (الدَّرْسُ 25 et son titre) ? Transcris tout, y compris le bandeau de titre s'il est présent.`,
  130: `Page 130 : contenu de cette page — suite de quelle leçon ? Transcris tout, y compris tout bandeau de titre de leçon (الدَّرْسُ + numéro) et les أهداف.`,
  131: `Page 131 : contenu de cette page — transcris tout, y compris tout bandeau de titre de leçon (الدَّرْسُ + numéro) et les rubriques visibles.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const p of Object.keys(Q)) {
  const out = `${DIR}/vlm23-bound-p-${p}.txt`;
  if (fs.existsSync(out)) { console.log(`skip p${p}`); continue; }
  const img = fs.readFileSync(`${DIR}/r150/p${p}.png`).toString('base64');
  console.log(`\n======== p${p} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 3 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q[p] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
          ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 2048,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 700 ? txt.slice(0, 350) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} p${p} échec: ${e.message}`); await sleep(10000*attempt); }
  }
  await sleep(3000);
}
