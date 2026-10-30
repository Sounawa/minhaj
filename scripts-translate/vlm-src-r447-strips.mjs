// vlm-src-r447-strips.mjs — strips p.175 @400dpi : énoncé + table de l'application 2
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const shots = [
  ['strip-175-c-175.png', 'énoncé application 2 + haut de sa table'],
  ['strip-175-b-175.png', 'table de l\'application 2'],
  ['strip-175-a-175.png', 'suite/bas de la table de l\'application 2'],
  ['strip-175-d-175.png', 'bas de la page 175'],
];
const prompt = `Tu lis un manuel marocain de farāʾiḍ (arabe, 400 dpi). Transcris EXACTEMENT ce que tu vois, sans inventer : d'abord l'énoncé arabe complet (mots un par un), puis le tableau cellule par cellule — chaque ligne : nom d'héritier (أم/جد/بنت/ابن/زوج/أخ...) et ses nombres dans l'ordre (chiffres occidentaux), de droite à gauche. Si illisible : [illisibile]. Ne paraphrase pas : mot à mot.`;
async function main() {
  const zai = await ZAI.create();
  for (const [f, cue] of shots) {
    const b64 = fs.readFileSync('/home/z/my-project/scripts-translate/tr-tmp/' + f).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: prompt + '\nZONE : ' + cue },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
      ]}],
      model: 'glm-5v-turbo', max_tokens: 2000,
    });
    console.log('===== ' + f + ' =====');
    console.log(res.choices[0].message.content); console.log();
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
