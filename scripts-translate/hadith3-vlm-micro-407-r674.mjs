// R674 — micro-lot final de lecture (7 crops hyper-serrés).
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/qa-crops-r674';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-407';

const PROMPTS = {
  'm-1134-name': `Très fort zoom sur une ligne arabe calligraphiée : début d'un récit rapporté, commençant par أنّ suivi du NOM d'un homme (ex. حنّى/كِتّان/أبو أوب... الأنصاريّ خرج حاجا). Transcris la ligne EXACTEMENT lettre par lettre sans deviner le nom ; si une lettre est illisible, marque [?].`,
  'm-1135-mid': `Très fort zoom sur le cœur d'un hadith : ʿUmar répond « فقال عمر: اذْهَبْ... » à Hibbār. Transcris EXACTEMENT les lignes visibles lettre par lettre (verbes, impératifs), marque [?] l'illisible.`,
  'm-p124-aya': `Très fort zoom sur une citation coranique entre ﴿ ﴾ ou « » au milieu d'une ligne. Transcris UNIQUEMENT le texte coranique visible, lettre par lettre, sans extrapoler ; marque [?] l'illisible. Donne aussi NUM: si un numéro bleu apparaît.`,
  'm-1128-malik': `Très fort zoom sur une ligne arabe : verdict de مالك (فقال مالك:...) suivi d'un renvoi bleu [الموطأ رقم: N]. Transcris la ligne exactement et donne NUM: chiffre par chiffre (٠=0…٩=9).`,
  'm-1138-isnad': `Très fort zoom sur un isnad : فعن [نام] بن [نام] ال[نسبة] عن عكرمة مولى ابن عباس... Transcris la ligne EXACTEMENT ; le premier nom (avant بن زيد) et la نسبة (قبل عن عكرمة) doivent être transcrits lettre par lettre, marque [?] l'illisible.`,
  'm-1136-frame': `Très fort zoom sur deux lignes arabe : introduction (ومنه المفرد في ذلك القارن...) puis citation de مالك «ومن قرن الحج والعُمرة...». Transcris EXACTEMENT les deux lignes lettre par lettre, marque [?] l'illisible.`,
  'm-1139-quote': `Très fort zoom sur une ligne arabe : قول ربيعة بن عبد الرحمن puis citation de مالك entre « » + renvoi bleu [الموطأ رقم: N]. Transcris EXACTEMENT (attention au mot entre وذلك et ما سمعت) et donne NUM: chiffre par chiffre.`,
};

async function main() {
  const zai = await ZAI.create();
  const tags = Object.keys(PROMPTS).filter(t => fs.existsSync(`${DIR}/${t}.png`) && !fs.existsSync(`${OUTDIR}/${t}.txt`));
  console.log(`micro-tâches: ${tags.length}`);
  for (const tag of tags) {
    for (let k = 1; k <= 4; k++) {
      try {
        const b64 = fs.readFileSync(`${DIR}/${tag}.png`).toString('base64');
        const res = await zai.chat.completions.createVision({
          messages: [{ role: 'user', content: [
            { type: 'text', text: PROMPTS[tag] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
          ] }],
          thinking: { type: 'disabled' },
        });
        const txt = res.choices[0]?.message?.content || '(vide)';
        fs.writeFileSync(`${OUTDIR}/${tag}.txt`, txt, 'utf-8');
        console.log(`${tag}: OK (${txt.length} car)`);
        break;
      } catch (e) {
        const msg = String(e?.message || e);
        if (k === 4) { console.log(`${tag}: ERREUR ${msg}`); break; }
        await new Promise(r => setTimeout(r, msg.includes('429') ? 20000 * k : 5000));
      }
    }
    await new Promise(r => setTimeout(r, 4000));
  }
  console.log('micro-lot terminé');
}
main().catch(e => { console.error('VLM_ERR: ' + (e?.message || e)); process.exit(1); });
