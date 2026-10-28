// vlm-qa-19798.mjs — relecture VLM des captures QA R343 (19798)
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const shots = [
  '/home/z/my-project/tr-tmp/qa-19798-desktop.png',
  '/home/z/my-project/tr-tmp/qa-19798-mobile.png',
];

const prompt = `Tu es contrôleur qualité d'un site de lecture académique bilingue (français/arabe). Voici une capture d'écran pleine page d'une leçon. Réponds en français, brièvement, avec ce format strict :
VERDICT: OK ou PROBLEME
OBSERVATIONS: 3-5 points (typographie, colonnes, débordements, chevauchements, lisibilité, badge/élements d'en-tête, rendu général).`;

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
    });
    console.log('=== ' + p.split('/').pop() + ' ===');
    console.log(res.choices[0].message.content);
  }
}
main().catch(e => { console.error('ERREUR VLM:', e.message); process.exit(1); });
