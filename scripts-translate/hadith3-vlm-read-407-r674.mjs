// R674 — lectures VLM des crops de preuve leçon 407 hadith-3es (p.124-128).
// Usage: node scripts-translate/hadith3-vlm-read-407-r674.mjs
// Chaque renvoi Muwaṭṭaʾ est tranché CHIFFRE PAR CHIFFRE à l'image.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/qa-crops-r674';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-407';
fs.mkdirSync(OUTDIR, { recursive: true });

const BASE = `Zone d'un manuel scolaire arabe (hadith, 3e année secondaire) à très fort zoom. Transcris EXACTEMENT tout le texte visible, ligne par ligne, en arabe, en conservant diacritiques, crochets [] et guillemets « ». Pour tout renvoi entre crochets de la forme [الموطأ رقم: N] (ou similaire), transcris le nombre N CHIFFRE PAR CHIFFRE (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9) sous la forme NUM: <chiffres latins>. Ne devine rien : transcris ce qui est visible.`;

const TASKS = [
  { tag: 'p124-qs-def', ask: `${BASE}\nTranscris les questions de révision et la définition (الهدي...) visibles.` },
  { tag: 'p124-aya', ask: `${BASE}\nTranscris la citation coranique complète ET le renvoi [سورة الحج N] : transcris le numéro de l'āya CHIFFRE PAR CHIFFRE en NUM:.` },
  { tag: 'p124-nuqsan', ask: `${BASE}\nTranscris le passage expliquant ce qui altère le pèlerinage (يشوب الحج...) jusqu'à la question centrale.` },
  { tag: 'p124-h1121', ask: `${BASE}\nTranscris le hadith complet (isnad + matn) et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'p125-h1135', ask: `${BASE}\nTranscris le hadith complet (isnad + matn + renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre). Zone partiellement dégradée : transcris ce qui est lisible, marque [?] les mots illisibles.` },
  { tag: 'p125-notice', ask: `${BASE}\nTranscris la notice biographique visible (mort en l'an N, qualité, ville) avec le numéro d'année CHIFFRE PAR CHIFFRE en NUM:.` },
  { tag: 'p125-istihlas', ask: `${BASE}\nTranscris le titre (استخلاص المضامين) et les deux items numérotés 1- et -.` },
  { tag: 'p126-atb1', ask: `${BASE}\nTranscris le passage فقهي sur le hady qui périt avant le miqāt, y compris la citation du Prophète entre « » et le renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'p126-atb2', ask: `${BASE}\nTranscris le passage فقهي (badane cyclope/تطوع, avis d'ابن شهاب...) avec ses deux renvois [الموطأ رقم: N] — NUM: chiffre par chiffre pour chacun.` },
  { tag: 'p126-daya', ask: `${BASE}\nTranscris le passage sur ضياع الهدي (hady perdu) avec la citation d'ابن عمر et le renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'p126-thania', ask: `${BASE}\nTranscris le titre ثانيا: et les lignes suivantes visibles.` },
  { tag: 'p127-h1134', ask: `${BASE}\nTranscris le passage sur celui qui a manqué le حج, la citation d'عمر entre « » et le renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre. Note aussi toute mention d'هبار.` },
  { tag: 'p127-h1136', ask: `${BASE}\nTranscris la citation de مالك entre « » et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'p127-fouat2', ask: `${BASE}\nTranscris le titre 2 - فوات الحج بمباشرة الزوجة et les lignes visibles.` },
  { tag: 'p127-said', ask: `${BASE}\nTranscris tout le récit de سعيد بن المسيب (rapport de يحيى بن سعيد) jusqu'à la citation de مالك et le renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre. Zone dégradée : transcris ce qui est lisible, marque [?] l'illisible.` },
  { tag: 'p127-after', ask: `${BASE}\nTranscris le passage وإن باشر الحاج زوجته بعد رمي جمرة العقبة... avec l'avis de مالك. Zone dégradée : transcris ce qui est lisible, marque [?] l'illisible.` },
  { tag: 'p128-h1129', ask: `${BASE}\nTranscris la citation entre « » et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'p128-h1138', ask: `${BASE}\nTranscris la ligne complète (rapport d'ابن عباس, citation entre « », renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre).` },
  { tag: 'p128-h1139', ask: `${BASE}\nTranscris la ligne complète (قول ربيعة بن عبد الرحمن, avis de مالك, renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre).` },
  { tag: 'p128-khatima', ask: `${BASE}\nTranscris le passage de conclusion (يستفاد مما سبق...) ET la citation coranique avec son renvoi [سورة X آية N] — NUM: chiffre par chiffre.` },
  { tag: 'p128-exos', ask: `${BASE}\nTranscris les deux exercices numérotés 1- et -. (المغاربة الحافلة...) exactement.` },
  { tag: 'p128-athar', ask: `${BASE}\nTranscris le athar final (سئل مالك...) avec sa citation entre « » et le renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre. Zone dégradée : transcris ce qui est lisible, marque [?] l'illisible.` },
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
  console.log('VLM-407 terminé');
}
main().catch(e => { console.error('VLM_ERR: ' + (e?.message || e)); process.exit(1); });
