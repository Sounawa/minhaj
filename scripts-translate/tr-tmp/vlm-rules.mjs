import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const shots = ['/tmp/q207-rule2.png','/tmp/q207-rule2-x2.png','/tmp/q207-rules89.png','/tmp/q207-rules89-x2.png'];
const prompt = `Transcris EXACTEMENT le texte arabe imprimé dans cette image, ligne par ligne (une ligne de l'image = une ligne de sortie), sans traduire, sans ponctuation ajoutée, en conservant l'ordre des mots. Si un mot est illisible, écris [؟]. Réponds uniquement par la transcription.`;
async function main() {
  const zai = await ZAI.create();
  for (const p of shots) {
    const b64 = fs.readFileSync(p).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: prompt },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
      ]}],
      model: 'glm-5v-turbo', max_tokens: 500,
    });
    console.log('=== ' + p + ' ===');
    console.log(res.choices[0].message.content.trim());
    console.log();
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
