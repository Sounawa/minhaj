import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const qs = [
  {
    img: '/home/z/my-project/scripts-translate/tr-tmp/m325-p196-196.png',
    ask: `Page de manuel arabe. Une phrase cite « مدونة الأسرة » (le Code de la famille marocain) et contient un numéro d'article (المادة ...). Transcris EXACTEMENT en arabe : (1) la phrase entière contenant مدونة الأسرة et le numéro de l'article ; (2) la phrase contenant « وإلى هذا يشير المصنف ». Réponds STRICTEMENT :
MUDAWANA: <phrase arabe exacte avec numéro>
MUSANNIF: <phrase arabe exacte>`
  },
  {
    img: '/home/z/my-project/scripts-translate/tr-tmp/m325-p198-198.png',
    ask: `Page de manuel arabe de droit successoral. Trois transcriptions exactes demandées (en arabe, mot à mot) :
(1) la phrase contenant le mot « الغراوين » qui commence environ par « لأنها إحدى الغراوين » et le contexte AVANT elle (l'énoncé « توفيت امرأة وتركت ... » ou « ساقت وترك » ...) ;
(2) la phrase complète commençant par « فعلى تقدير أن الأب حي حين موت المرأة، تكون المسألة ... » jusqu'à la fin de la phrase ;
(3) la phrase complète « على تقدير أن الأب ميت قبل موت المرأة، فكذلك تكون المسألة ... » jusqu'à « ... الثلث » ;
(4) la phrase commençant par « فالثمانية توافق الستة » (suite et fin exactes).
Réponds STRICTEMENT :
ENONCE_EXEMPLE: <arabe>
PHRASE_GHARAWAYN: <arabe>
HYPOTHESE_PERE_VIVANT: <arabe>
HYPOTHESE_PERE_MORT: <arabe>
PHRASE_WAFQ: <arabe>`
  },
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
      model: 'glm-5v-turbo', max_tokens: 900,
    });
    console.log('=== ' + q.img.split('/').pop() + ' ===');
    console.log(res.choices[0].message.content);
    console.log('');
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
