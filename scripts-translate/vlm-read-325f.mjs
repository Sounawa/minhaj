import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
async function main() {
  const zai = await ZAI.create();
  for (const p of ['/tmp/m325-exo1.png','/tmp/m325-exo2.png']) {
    for (let attempt = 1; attempt <= 2; attempt++) {
      const b64 = fs.readFileSync(p).toString('base64');
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: `Lis cette ligne d'énoncé d'exercice arabe et transcris-la mot à mot. Attention aux mots du domaine successoral (زوج، زوجة، أم، أب، ابن، بنت، أخ، أخت، جد، عم، خمسة، إخوة، بنون، أولاد، مفقود). Format : ENONCE: <arabe>` },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ]}],
        model: 'glm-5v-turbo', max_tokens: 300,
      });
      console.log(`=== ${p} duel${attempt} ===`);
      console.log(res.choices[0].message.content);
    }
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
