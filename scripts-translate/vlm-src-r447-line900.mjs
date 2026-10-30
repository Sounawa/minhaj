import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const b64 = fs.readFileSync('/home/z/my-project/scripts-translate/tr-tmp/line-900-175.png').toString('base64');
const prompts = [
  'Transcris cette ligne d\'arabe imprimé (naskh maghrébin vocalisé, 900 dpi) MOT PAR MOT. Ne devine pas : chaque mot que tu ne lis pas clairement, remplace-le par [?]. Ce sont des mots de fiqh (فرائض) : verbes أقرّ/أنكر, noms d\'héritiers (أم، جد، بنت، ابن، زوج، أخ), tanwīn -ًا.',
  'Même ligne, deuxième lecture indépendante. Liste les mots un par un dans l\'ordre droite→gauche. Indique pour chaque mot ton niveau de certitude (sûr/?).',
];
async function main() {
  const zai = await ZAI.create();
  for (const p of prompts) {
    const res = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: p },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
      ]}],
      model: 'glm-5v-turbo', max_tokens: 800,
    });
    console.log('----- lecture -----');
    console.log(res.choices[0].message.content); console.log();
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
