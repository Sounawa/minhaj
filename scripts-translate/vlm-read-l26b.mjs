import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

// R527 — relecture VLM fine de la boîte des āyāt p.195 (bandes 600 dpi)
// + référence تقويم Q1 p.201. Objectif : médaillons exacts + premier mot
// de chaque verset (tranchage décalage imprimé→cache).
const qs = [
  { img: '/home/z/my-project/tr-tmp/probe-l26-box-band1.png',
    ask: `Bande horizontale d'un extrait coranique arabe (muṣḥaf crop, très zoomé). Si un numéro entre parenthèses ou médaillon est visible, transcris-le (chiffres exacts). Transcris le texte arabe visible ENTIER mot à mot, sans rien inventer. Si illisible, écris ILLISIBLE. Format :
NUM: <numéro exact ou aucun>
TEXTE: <texte exact>` },
  { img: '/home/z/my-project/tr-tmp/probe-l26-box-band2.png',
    ask: `Bande horizontale d'un extrait coranique arabe (muṣḥaf crop, très zoomé). Si un numéro entre parenthèses ou médaillon est visible, transcris-le (chiffres exacts). Transcris le texte arabe visible ENTIER mot à mot, sans rien inventer. Si illisible, écris ILLISIBLE. Format :
NUM: <numéro exact ou aucun>
TEXTE: <texte exact>` },
  { img: '/home/z/my-project/tr-tmp/probe-l26-box-band3.png',
    ask: `Bande horizontale d'un extrait coranique arabe (muṣḥaf crop, très zoomé). Si un numéro entre parenthèses ou médaillon est visible, transcris-le (chiffres exacts). Transcris le texte arabe visible ENTIER mot à mot, sans rien inventer. Si illisible, écris ILLISIBLE. Format :
NUM: <numéro exact ou aucun>
TEXTE: <texte exact>` },
  { img: '/home/z/my-project/tr-tmp/probe-l26-box-band4.png',
    ask: `Bande horizontale d'un extrait coranique arabe (muṣḥaf crop, très zoomé). Si un numéro entre parenthèses ou médaillon est visible, transcris-le (chiffres exacts). Transcris le texte arabe visible ENTIER mot à mot, sans rien inventer. Si illisible, écris ILLISIBLE. Format :
NUM: <numéro exact ou aucun>
TEXTE: <texte exact>` },
  { img: '/home/z/my-project/tr-tmp/probe-l26-box-band5.png',
    ask: `Bande horizontale d'un extrait coranique arabe (muṣḥaf crop, très zoomé). Si un numéro entre parenthèses ou médaillon est visible, transcris-le (chiffres exacts). Transcris le texte arabe visible ENTIER mot à mot, sans rien inventer. Si illisible, écris ILLISIBLE. Format :
NUM: <numéro exact ou aucun>
TEXTE: <texte exact>` },
  { img: '/home/z/my-project/tr-tmp/probe-l26-p201-q1.png',
    ask: `Ligne très zoomée d'un manuel arabe : une question d'évaluation numérotée 1. Transcris EXACTEMENT la ligne entière, y compris le fragment de verset entre guillemets (lettres et chiffres exacts). Format :
Q1: <texte exact>` },
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
