// vlm-qa-r342.mjs — relecture VLM des captures QA R342 (19785)
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const shots = [
  '/home/z/my-project/tr-tmp/qa-19785-top-desktop.png',
  '/home/z/my-project/tr-tmp/qa-19785-matn-mobile.png',
  '/home/z/my-project/tr-tmp/qa-19785-footer-mobile.png',
];

const prompt = `Tu es contrôleur qualité d'un site de lecture académique bilingue (français/arabe). Voici une capture d'écran d'une leçon (desktop ou mobile 390px). Réponds en français, brièvement, avec ce format strict :
VERDICT: OK ou PROBLEME
OBSERVATIONS: 2-4 points (typographie, colonnes, débordements horizontaux, chevauchements, lisibilité, badge/éléments d'en-tête, pied de page).`;

async function main() {
  const zai = await ZAI.create();
  for (const p of shots) {
    const b64 = fs.readFileSync(p).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{
        role: 'user',
        content: [
          { type: 'text', text: prompt },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ],
      }],
      model: 'glm-5v-turbo',
      max_tokens: 400,
    });
    console.log('=== ' + p.split('/').pop() + ' ===');
    console.log(res.choices[0].message.content);
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
