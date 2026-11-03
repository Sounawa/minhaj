// vlm-pdf12-r557.mjs — R557 : passe VLM minimale leçon 11 (pdf-12) sur composites prêts (qa-crops-r555).
// 3 lectures max : numéros (×2 composites) + p85 (référence hadith + renvois āyāt).
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const OUT = '/home/z/my-project/tr-tmp/vlm-pdf12-r557.json';
const BASE = ("Tu lis une image d'un manuel scolaire marocain de hadith (Muwaṭṭa' Mālik / " +
  "Šarḥ az-Zarqānī, 2e année collégiale). Réponds UNIQUEMENT à la question posée, " +
  "par transcription EXACTE du texte imprimé visible. Si tu n'es pas sûr d'un mot ou d'un chiffre, " +
  "écris [illisible]. N'invente AUCUN texte, ne complète jamais de mémoire.");

const shots = [
  ['/home/z/my-project/tr-tmp/qa-crops-r555/composite-numbers.png',
   'Voici une page du manuel. Transcris TOUS les renvois de référence entre crochets visibles sous la forme [الموطأ رقم: N] ou [صحيح البخاري] etc., dans l\'ordre, avec les chiffres EXACTS imprimés (chiffres arabes orientaux ou occidentaux). Liste: référence → numéro exact.'],
  ['/home/z/my-project/tr-tmp/qa-crops-r555/composite-numbers-bis.png',
   'Voici une autre page du manuel. Transcris TOUS les renvois de référence entre crochets visibles [الموطأ رقم: N] [صحيح البخاري] [صحيح مسلم] etc., dans l\'ordre, chiffres EXACTS. Liste: référence → numéro exact.'],
  ['/home/z/my-project/tr-tmp/qa-crops-r555/composite-p85.png',
   'Transcris mot à mot le hadith de cette page avec son isnād et son matn, puis le renvoi entre crochets qui le suit (référence + numéro EXACT), puis les deux renvois coraniques [سورة البقرة الآية: N] avec leurs chiffres EXACTS, puis la question de l\'الإعداد القبلي si visible.'],
];

async function main() {
  const zai = await ZAI.create();
  const results = {};
  for (const [name, q] of shots) {
    if (!fs.existsSync(name)) { results[name] = 'FICHIER ABSENT'; continue; }
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
        results[name] = res.choices[0].message.content;
        done = true;
        console.log(`OK ${name}`);
      } catch (e) {
        console.error(`ERR ${name} tentative ${attempt}: ${e.message}`);
        if (attempt < 3) await new Promise(r => setTimeout(r, 45000 * attempt));
        else results[name] = 'ERREUR_429: ' + e.message;
      }
    }
  }
  fs.writeFileSync(OUT, JSON.stringify(results, null, 2));
  console.log('Écrit:', OUT);
}
main().catch(e => { console.error(e); process.exit(1); });
