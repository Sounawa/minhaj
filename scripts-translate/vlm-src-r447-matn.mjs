import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const b64 = fs.readFileSync('/home/z/my-project/scripts-translate/tr-tmp/matn-174-174.png').toString('base64');
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
  console.log('--- lecture A ---');
  console.log(await ask(zai, 'Trois lignes d\'arabe vocalisé (matn du Muḫtaṣar de Khalīl cité dans un manuel). Transcris mot à mot avec les voyelles, de droite à gauche. Aucune invention : [?] si incertain.'));
  console.log('--- lecture B ---');
  console.log(await ask(zai, 'Même zone. Transcris SEULEMENT la citation entre guillemets «...» : c\'est le passage وإن أقر ابن ببنت... Donne chaque mot avec ses voyelles. Attends-toi aux mots : وإنْ، أقرَّ، ابنٌ، ببنتٍ، وبنتٌ، بابنٍ، فالإنكارُ، منْ، ثلاثةٍ، وإقرارُهُ، منْ، أربعٍ، وهي، منْ، عشرينَ، وإقرارُها، منْ، خمسةٍ، فتضربُ، أربعةً، في، خمسةٍ، بعشرينَ، ثم، ثلاثةٍ، بستينَ، ثمانية.'));
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
