// vlm-qa-19798-crops.mjs — VLM ciblé sur crops mobile R343 (19798) — règle (cb)
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const shots = [
  ['/home/z/my-project/tr-tmp/qa-19798-matn-mobile.png', 'capture de la table du matn (4 bayts translittérés en latin, 2 colonnes) en viewport mobile 390px'],
  ['/home/z/my-project/tr-tmp/qa-19798-arabic-mobile.png', 'capture de la section arabe اَلْمَتْنُ (texte arabe de la leçon) en viewport mobile 390px'],
];

const prompt = `Tu es contrôleur qualité d'un site de lecture académique bilingue (français/arabe) rendu sur mobile 390px. Voici une capture CIBLÉE d'une section. Réponds en français, brièvement :
VERDICT: OK ou PROBLEME
OBSERVATIONS: 2-3 points — y a-t-il du texte qui DÉBORDE de la largeur de l'écran ? des chevauchements ? la table/texte est-elle lisible ?`;

async function main() {
  const zai = await ZAI.create();
  for (const [p, desc] of shots) {
    const b64 = fs.readFileSync(p).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{
        role: 'user',
        content: [
          { type: 'text', text: prompt + '\nContexte : ' + desc },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ],
      }],
    });
    console.log('=== ' + p.split('/').pop() + ' ===');
    console.log(res.choices[0].message.content);
  }
}
main().catch(e => { console.error('ERREUR VLM:', e.message); process.exit(1); });
