// vlm-qa-r451-tables.mjs — vérification binaire par zoom (doctrine R450/R62) des tableaux corrigés du print
// Usage: bun scripts-translate/vlm-qa-r451-tables.mjs <crop> "<question>"
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const [,, imgPath, question] = process.argv;
if (!imgPath || !question) { console.error('usage: bun vlm-qa-r451-tables.mjs <image> "<question>"'); process.exit(2); }
const b64 = fs.readFileSync(imgPath).toString('base64');

async function main() {
  const zai = await ZAI.create();
  const res = await zai.createChatCompletionVision({
    messages: [{ role: 'user', content: [
      { type: 'text', text: `Tableau de correction de problèmes successoraux (manuel marocain, chiffres occidentaux 0-9, texte arabe). ${question} Réponds de façon factuelle et concise. Si le chiffre est partiellement coupé ou ambigu, dis-le explicitement.` },
      { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
    ]}],
    model: 'glm-5v-turbo', max_tokens: 400,
  });
  console.log(res.choices[0].message.content);
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
