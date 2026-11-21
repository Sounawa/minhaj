// IA-2 — vlm2-h6-14 : 2e salve VLM, recadrages serrés avec questions ciblées.
import ZAI from '/tmp/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/pdf-work/h6-14/vlm';
const BASE = `Image : extrait d'une page d'un manuel scolaire marocain de hadith (6e année, tirage des Arba'īn nawawiyya avec commentaire d'Ibn Daqīq al-'Īd). Transcris TOUT le texte arabe visible, mot à mot, AVEC la voyellisation imprimée, dans l'ordre de lecture (droite → gauche). Ne devine JAMAIS : un mot illisible → [؟]. Réponds UNIQUEMENT par la transcription.`;
const FOCUS = {
  'u1-glosse1-p77': `${BASE}\nC'est une ligne de glose (terme : définition) du commentaire, sur fond coloré.`,
  'u2-glosse2-p77': `${BASE}\nC'est une ligne de glose (terme : définition) du commentaire, sur fond coloré.`,
  'u3-fahim-p77': `${BASE}\nLigne isolée (texte bleu sur fond clair ?) entre la traduction du rapporteur et le titre «الشرح».`,
  'u4-lead-p79': `${BASE}\nLigne d'appel éventuelle entre le bandeau «الاستثمار» et le hadith. S'il n'y a AUCUN texte, réponds exactement : (aucun texte).`,
  'u5-objectif3-p76': `${BASE}\nTroisième objectif de la leçon (ligne isolée).`,
  'u6-ouv-p78': `${BASE}\nCe sont les premiers mots (à droite) d'un paragraphe qui continue par «أنه لولا البينة لادّعى أناس…». Transcris mot à mot les 3-4 premiers mots.`,
  'u7-taqum-p78': `${BASE}\nTranscris ; indique le verbe exact entre «ما لم» et «عليه بيّنة» (تَقُمْ ou تَكُنْ ?).`,
  'u8-lahiqqi-p78': `${BASE}\nTranscris ; indique le mot exact entre «استحقاقه» et «الذي يدّعيه» (لِحَقِّهِ ou لِحَظِّهِ ?).`,
};

async function main() {
  const zai = await ZAI.create();
  for (const label of Object.keys(FOCUS)) {
    const file = `${DIR}/${label}.png`;
    if (!fs.existsSync(file)) { console.log(`\n== ${label} : ABSENT`); continue; }
    try {
      const b64 = fs.readFileSync(file).toString('base64');
      const res = await zai.chat.completions.createVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: FOCUS[label] },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ] }],
        thinking: { type: 'disabled' },
      });
      console.log(`\n== ${label} ==\n` + (res.choices[0]?.message?.content || '(vide)'));
    } catch (e) {
      console.log(`\n== ${label} : ERREUR ${String(e?.message || e).slice(0, 200)}`);
    }
  }
}
main().catch(e => { console.error('FATAL', String(e?.message || e).slice(0, 300)); process.exit(1); });
