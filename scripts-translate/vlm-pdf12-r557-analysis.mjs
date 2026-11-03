// vlm-pdf12-r557-analysis.mjs — R557 : lectures composites p81/p82/p84 (matns de l'analyse).
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const OUT = '/home/z/my-project/tr-tmp/vlm-pdf12-r557-analysis.json';
const BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭa' Mālik / " +
  "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, " +
  "par transcription EXACTE du texte imprimé visible, ligne par ligne. Si tu n'es pas sûr d'un mot ou d'un chiffre, " +
  "écris [illisible]. N'invente AUCUN texte, ne complète jamais de mémoire.");

const shots = [
  ['/home/z/my-project/tr-tmp/qa-crops-r555/composite-p81.png',
   "Transcris TOUT le texte visible, ligne par ligne, y compris les renvois entre crochets [الموطأ رقم: N] chiffre par chiffre."],
  ['/home/z/my-project/tr-tmp/qa-crops-r555/composite-p82.png',
   "Transcris TOUT le texte visible, ligne par ligne, y compris les renvois entre crochets chiffre par chiffre et la glose (الشرح) si visible."],
  ['/home/z/my-project/tr-tmp/qa-crops-r555/composite-p84.png',
   "Transcris TOUT le texte visible, ligne par ligne, y compris les invocations citées et les renvois entre crochets chiffre par chiffre."],
];

async function main() {
  const zai = await ZAI.create();
  const results = {};
  for (const [name, q] of shots) {
    const b64 = fs.readFileSync(name).toString('base64');
    let done = false;
    for (let attempt = 1; attempt <= 3 && !done; attempt++) {
      try {
        const res = await zai.createChatCompletionVision({
          messages: [{
            role: 'user',
            content: [
              { type: 'text', text: BASE + '\n\n' + q },
              { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
            ],
          }],
        });
        results[name.split('/').pop()] = res.choices[0].message.content;
        done = true;
        console.log(`OK ${name}`);
      } catch (e) {
        console.error(`ERR ${name} t${attempt}: ${e.message}`);
        if (attempt < 3) await new Promise(r => setTimeout(r, 45000 * attempt));
        else results[name.split('/').pop()] = 'ERREUR: ' + e.message;
      }
    }
  }
  fs.writeFileSync(OUT, JSON.stringify(results, null, 2));
  console.log('Écrit:', OUT);
}
main().catch(e => { console.error(e); process.exit(1); });
