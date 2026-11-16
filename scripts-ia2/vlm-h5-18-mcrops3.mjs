// Z2-20 — microcrops v3 VLM — transcription STRICTE sans interprétation
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-18';

const ASKS = {
  'mc-m23-q1-l1-p102.jpg': `Photographie d'UNE ligne d'imprimé arabe scolaire, zoom ×3. Transcris UNIQUEMENT les caractères visibles, de droite à gauche, sous forme de mots arabes. N'UTILISE PAS ta mémoire : ne recopie que ce que tu vois. Si un mot est illisible, écris [؟]. Donne ensuite le décompte des mots.`,
  'mc-m24-q1-l2-p102.jpg': `Photographie d'UNE ligne d'imprimé arabe scolaire, zoom ×3. Transcris UNIQUEMENT les caractères visibles, de droite à gauche, sous forme de mots arabes. N'UTILISE PAS ta mémoire : ne recopie que ce que tu vois. Si un mot est illisible, écris [؟]. Donne ensuite le décompte des mots.`,
  'mc-m25-y3-l1-p102.jpg': `Photographie d'UNE ligne d'imprimé arabe scolaire, zoom ×3. Transcris UNIQUEMENT les caractères visibles, de droite à gauche, sous forme de mots arabes. N'UTILISE PAS ta mémoire : ne recopie que ce que tu vois. Si un mot est illisible, écris [؟]. Donne ensuite le décompte des mots.`,
  'mc-m26-y3-l2-p102.jpg': `Photographie d'UNE ligne d'imprimé arabe scolaire, zoom ×3. Transcris UNIQUEMENT les caractères visibles, de droite à gauche, sous forme de mots arabes. N'UTILISE PAS ta mémoire : ne recopie que ce que tu vois. Si un mot est illisible, écris [؟]. Donne ensuite le décompte des mots.`,
};

async function main() {
  const zai = await ZAI.create();
  for (const [img, ask] of Object.entries(ASKS)) {
    const out = `${DIR}/z-${img.replace('.jpg', '.txt')}`;
    if (fs.existsSync(out)) { console.log(`skip ${img}`); continue; }
    const b64 = fs.readFileSync(`${DIR}/${img}`).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: ask },
          { type: 'image_url', image_url: { url: `data:image/jpeg;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 1200,
        temperature: 0.0,
      });
      const txt = res?.choices?.[0]?.message?.content ?? JSON.stringify(res);
      fs.writeFileSync(out, txt);
      console.log(`OK ${img} (${txt.length} car)`);
    } catch (e) {
      console.error(`ÉCHEC ${img}: ${e.message}`);
    }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
