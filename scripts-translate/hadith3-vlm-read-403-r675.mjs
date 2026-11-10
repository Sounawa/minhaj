// R675 — lectures VLM des crops de preuve leçon 403 hadith-3es (p.97-102).
// Usage: node scripts-translate/hadith3-vlm-read-403-r675.mjs
// Chaque renvoi Muwaṭṭaʾ / āya est tranché CHIFFRE PAR CHIFFRE à l'image.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/qa-crops-r675';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-403';
fs.mkdirSync(OUTDIR, { recursive: true });

const BASE = `Zone d'un manuel scolaire arabe (hadith, 3e année secondaire, madhab malikite) à très fort zoom. Transcris EXACTEMENT tout le texte visible, ligne par ligne, en arabe, en conservant diacritiques, crochets [] et guillemets « ». Pour tout renvoi entre crochets de la forme [الموطأ رقم: N] ou [سورة X الآية: N], transcris le nombre N CHIFFRE PAR CHIFFRE (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9) sous la forme NUM: <chiffres latins>. Ne devine rien : transcris ce qui est visible ; marque [?] les mots réellement illisibles.`;

const TASKS = [
  { tag: 'r675-t-p97-intro', ask: `${BASE}\nTranscris la définition de المزدلفة et les phrases qui suivent (أو…تقدّموا) visibles.` },
  { tag: 'r675-t-p97-hadith1', ask: `${BASE}\nTranscris le hadith complet (isnad + matn + fin «قال مالك: …») et le renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'r675-t-p98-hadith2', ask: `${BASE}\nTranscris le hadith complet (isnad + matn, y compris «الصلاة أمامك» et la fin …شيئاً) et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'r675-n-p98-hadith2', ask: `${BASE}\nTranscris uniquement la/les ligne(s) contenant le renvoi [الموطأ رقم: N] et le mot qui le précède — NUM: chiffre par chiffre.` },
  { tag: 'r675-n-p98-tarjama', ask: `${BASE}\nTranscris la notice biographique complète (أسامة بن زيد…) avec l'année de mort en NUM: chiffre par chiffre (توفي بالمدينة سنة Nه).` },
  { tag: 'r675-n-p99-athar', ask: `${BASE}\nTranscris le passage نافع/ابن عمر/محسّر + la glose وادي النار + le renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'r675-n-p100-mawqif', ask: `${BASE}\nTranscris le titre 2 الوقوف بمزدلفة, la phrase «كلها موقف…», son attribut (قال كذا) et le renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre. Transcris aussi le حديث جابر s'il est visible, avec son NUM.` },
  { tag: 'r675-n-p100-jamian', ask: `${BASE}\nTranscris le passage sur صلاة المغرب ليلة الأضحى (السنة…تأخير…) avec les DEUX renvois [الموطأ رقم: N] — NUM: chiffre par chiffre pour chacun, puis la phrase ابن القاسم/الجمهور.` },
  { tag: 'r675-t-p100-b', ask: `${BASE}\nTranscris le passage صفة الجمع وسببه (ثبت أن النبي لما جاء مزدلفة…) jusqu'à la fin de la page, avec tout renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'r675-t-p101-adhan', ask: `${BASE}\nTranscris les sections 3 الأذان والاقامة et 4 النزول بمزدلفة (y compris البخاري/ابن مسعود et la phrase «رأيت النبي…») exactement.` },
  { tag: 'r675-n-p101-rukh', ask: `${BASE}\nTranscris le passage ويُرخص للنساء… avec les narrations (ابن عمر, عطاء بن أبي رباح, أسماء بنت أبي بكر, طلحة بن عبيد الله) et TOUS les renvois [الموطأ رقم: N] — NUM: chiffre par chiffre pour chacun, dans leur ordre.` },
  { tag: 'r675-n-p102-talil', ask: `${BASE}\nTranscris le taʿlīl de مالك complet : les trois citations coraniques avec leurs renvois [سورة X الآية: N] — NUM: chiffre par chiffre pour chacun — puis le récit الحُمَس/قريش/العرب et le renvoi [الموطأ رقم: N] — NUM.` },
];

async function readOne(zai, t) {
  const out = `${OUTDIR}/${t.tag}.txt`;
  for (let k = 1; k <= 4; k++) {
    try {
      const b64 = fs.readFileSync(`${DIR}/${t.tag}.png`).toString('base64');
      const res = await zai.chat.completions.createVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: t.ask },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ] }],
        thinking: { type: 'disabled' },
      });
      const txt = res.choices[0]?.message?.content || '(vide)';
      fs.writeFileSync(out, txt, 'utf-8');
      return `${t.tag}: OK (${txt.length} car)`;
    } catch (e) {
      const msg = String(e?.message || e);
      if (k === 4) return `${t.tag}: ERREUR ${msg}`;
      const wait = msg.includes('429') ? 20000 * k : 5000;
      console.log(`  retry ${t.tag} (${k}) dans ${wait}ms`);
      await new Promise(r => setTimeout(r, wait));
    }
  }
}

async function main() {
  const zai = await ZAI.create();
  const todo = TASKS.filter(t => !fs.existsSync(`${OUTDIR}/${t.tag}.txt`));
  console.log(`tâches: ${todo.length}/${TASKS.length}`);
  const res = [];
  for (const t of todo) {
    res.push(await readOne(zai, t));
    await new Promise(r => setTimeout(r, 4000));
  }
  console.log(res.join('\n'));
  console.log('VLM-403 terminé');
}
main().catch(e => { console.error('VLM_ERR: ' + (e?.message || e)); process.exit(1); });
