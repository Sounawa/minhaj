import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const b64 = fs.readFileSync('/home/z/my-project/scripts-translate/tr-tmp/exo-176-176.png').toString('base64');
async function ask(zai, p) {
  const res = await zai.createChatCompletionVision({
    messages: [{ role: 'user', content: [
      { type: 'text', text: p },
      { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
    ]}],
    model: 'glm-5v-turbo', max_tokens: 900,
  });
  return res.choices[0].message.content;
}
async function main() {
  const zai = await ZAI.create();
  console.log('--- lecture A (mot à mot) ---');
  console.log(await ask(zai, 'Zone d\'un manuel de farāʾiḍ (600 dpi) : un titre de section, une consigne, deux énoncés d\'exercices, une ligne de consigne finale, trois objectifs. Transcris TOUT mot à mot en arabe avec les tanwīn, de droite à gauche. Aucune invention : [?] si illisible.'));
  console.log('--- lecture B (vue) ---');
  console.log(await ask(zai, 'Même zone. Décris la structure : combien de lignes, que porte la première ligne de consigne après les exercices (mémorisation ? préparation ?), et liste les héritiers nommés dans chaque exercice.'));
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
