import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const ask = `Bande de page d'un manuel arabe de droit successoral mālikite. Transcris UNIQUEMENT les phrases arabes contenant le mot « الغراوين » (mot à mot, exactement, avec leur début). Si aucune phrase ne contient ce mot, réponds AUCUN. Ne transcris rien d'autre. Format :
PHRASE_1: <arabe>
PHRASE_2: <arabe>`;
async function main() {
  const zai = await ZAI.create();
  for (const p of ['/tmp/m325-p198-band0.png']) {
    const b64 = fs.readFileSync(p).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: ask },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
      ]}],
      model: 'glm-5v-turbo', max_tokens: 600,
    });
    console.log('=== ' + p + ' ===');
    console.log(res.choices[0].message.content);
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
