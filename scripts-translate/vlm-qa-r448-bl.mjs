import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const b64 = fs.readFileSync('/home/z/my-project/scripts-translate/tr-tmp/qa-R448-321-mobile-bl.png').toString('base64');
async function main() {
  const zai = await ZAI.create();
  const res = await zai.createChatCompletionVision({
    messages: [{ role: 'user', content: [
      { type: 'text', text: 'Coin inférieur gauche d\'une capture mobile (390px). Décris précisément : (1) y a-t-il un bouton ou élément d\'interface flottant ? Lequel, quelle forme, quel(s) caractère(s) porte-t-il ? (2) ce bouton chevauche-t-il RÉELLEMENT le texte du corps (le texte passe-t-il dessous/derrière), ou bien le texte est-il en marge à côté ? Réponds factuellement.' },
      { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
    ]}],
    model: 'glm-5v-turbo', max_tokens: 500,
  });
  console.log(res.choices[0].message.content);
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
