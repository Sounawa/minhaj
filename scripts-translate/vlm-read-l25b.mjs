import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

// R571 — passe 2 : bandeau الدرس 25 + dernière ligne p.173 + zones box (824) — retry après 429.
const qs = [
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/mc-r571-bandeau-171-200.png',
    ask: `Bandeau d'ouverture d'une leçon d'un manuel arabe (crop très zoomé, fond décoré). Il y a un mot الدرس suivi d'un numéro dans un médaillon/cartouche. Transcris le numéro chiffre par chiffre (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9). Format :\nBADGE: الدرس <numéro exact en chiffres>`,
  },
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/tail-173.png',
    ask: `Dernières lignes d'une page d'un manuel arabe (crop très zoomé). La ligne finale commence par : والكفارة خاصة بالعمد في مشهور قول الإمام مالك… Transcris EXACTEMENT la fin de cette phrase après الإمام مالك (mot à mot, y compris toute formule entre مالك et la fin). Si un mot est illisible, écris-le tel que tu le vois graphiquement. Format :\nFIN: <suite exacte après الإمام مالك>`,
  },
  { img: '/home/z/my-project/tr-tmp/qa-crops-r571/n824b-1200.png',
    ask: `Fin d'un paragraphe encadré d'un manuel arabe (crop très zoomé). À gauche : un crochet [الموطأ رقم: NNN]. Transcris le nombre NNN chiffre par chiffre (٠=0 … ٩=9). Format :\nNUM: <chiffres>`,
  },
];

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

async function main() {
  const zai = await ZAI.create();
  for (const q of qs) {
    const b64 = fs.readFileSync(q.img).toString('base64');
    let res = null, attempt = 0;
    while (res === null && attempt < 4) {
      attempt++;
      try {
        res = await zai.createChatCompletionVision({
          messages: [{ role: 'user', content: [
            { type: 'text', text: q.ask },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
          ]}],
          model: 'glm-5v-turbo', max_tokens: 900,
        });
      } catch (e) {
        console.error(`retry ${attempt} ${q.img.split('/').pop()} : ${e.message}`);
        await sleep(30000);
      }
    }
    console.log('=== ' + q.img.split('/').pop() + ' ===');
    console.log(res ? res.choices[0].message.content : 'ECHEC');
    console.log('');
    await sleep(3000);
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
