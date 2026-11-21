// Z2-48 — sonde VLM : 1 seule bande (p71-b2) pour vérifier la disponibilité du service.
import ZAI from '/tmp/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-13/bands';
const BASE = `Image : bande horizontale d'une page d'un manuel scolaire marocain de hadith (6e année, trad. du livre des Arba'īn nawawiyya avec commentaire d'Ibn Daqīq al-'Īd). Transcris TOUT le texte arabe visible, dans l'ordre de lecture (droite → gauche, haut → bas), mot à mot, AVEC la voyellisation imprimée. Ne devine JAMAIS : un mot illisible → [؟]. Réponds UNIQUEMENT par la transcription.`;

async function main() {
  const zai = await ZAI.create();
  const b64 = fs.readFileSync(`${DIR}/p71-b2.png`).toString('base64');
  const res = await zai.chat.completions.createVision({
    messages: [{ role: 'user', content: [
        { type: 'text', text: BASE },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
      ] }],
    thinking: { type: 'disabled' },
  });
  console.log(res.choices[0]?.message?.content || '(vide)');
}
main().catch(e => { console.error('FATAL', String(e?.message || e).slice(0, 300)); process.exit(1); });
