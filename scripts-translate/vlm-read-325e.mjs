import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const qs = [
  { img: '/tmp/m325-rows.png',
    ask: `Image agrandie d'un tableau arabe. Transcris UNIQUEMENT : (1) la ligne d'héritier située entre « بنت ابن » et « أب مفقود » (nom + nombres) ; (2) la ligne « أب مفقود » entière ; (3) la ligne « الحظ الموقوف » entière. Chiffres exacts. Format :
LIGNE_MYSTERE: <nom> | <nombres droite→gauche>
LIGNE_PERE: <nombres>
LIGNE_MOQUOUF: <nombres>` },
  { img: '/tmp/m325-exos2.png',
    ask: `Image agrandie : énoncés de trois exercices arabes numérotés. Transcris CHAQUE ligne d'énoncé mot à mot (les chiffres et les mots comme « هلك هالك وترك »). Format :
LIGNE1: <arabe>
LIGNE2: <arabe>
LIGNE3: <arabe>
LIGNE4: <arabe>
LIGNE5: <arabe>
LIGNE6: <arabe>` },
];
async function main() {
  const zai = await ZAI.create();
  for (const q of qs) {
    const b64 = fs.readFileSync(q.img).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: q.ask },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
      ]}],
      model: 'glm-5v-turbo', max_tokens: 800,
    });
    console.log('=== ' + q.img + ' ===');
    console.log(res.choices[0].message.content);
    console.log('');
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
