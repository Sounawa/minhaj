// R690 — lectures VLM des microcrops d'adjudication leçon 412 hadith-3es (la 'umra).
// Usage: node scripts-translate/r690-vlm-412-crops.mjs
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/m412';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-412';
fs.mkdirSync(OUTDIR, { recursive: true });

const BASE = `Zone d'un manuel scolaire arabe (hadith, 3e année secondaire, Muwaṭṭaʾ de l'imam Mālik) à très fort zoom. Transcris EXACTEMENT tout le texte visible, ligne par ligne, en arabe, en conservant diacritiques, crochets [] et guillemets « ». Pour tout renvoi [الموطأ رقم: N] ou [سورة X الآية: N], transcris le nombre N CHIFFRE PAR CHIFFRE (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9 et chiffres latins) sous la forme NUM: <chiffres latins>. Ne devine rien : transcris ce qui est visible, marque [?] l'illisible.`;

const TASKS = [
  { tag: 'p152-idad', ask: `${BASE}\nTranscris les deux questions numérotées de la préparation (أعرّف... / أبين...). Transcris le mot clé de chaque question lettre à lettre (العمرة ou autre).` },
  { tag: 'p153-medail', ask: `${BASE}\nTranscris le médaillon (numéro du درس et titre) exactement.` },
  { tag: 'p153-objectifs', ask: `${BASE}\nTranscris les trois objectifs numérotés (أن أتعرف... / أن أدرك...) lettre à lettre.` },
  { tag: 'p153-aya', ask: `${BASE}\nTranscris la citation coranique calligraphique ENTRE ﴿ ﴾ lettre à lettre (c'est de la calligraphie : sois très prudent), puis le renvoi [سورة الحج الآية: N] — NUM: chiffre par chiffre.` },
  { tag: 'p153-umar', ask: `${BASE}\nTranscris le hadith d'عمر بن الخطاب complet (isnad + citation entre « » + renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre). Transcris le premier mot de la citation lettre à lettre.` },
  { tag: 'p154-icha-quote', ask: `${BASE}\nTranscris le hadith de la femme (isnad + question + citation du Prophète entre « » + renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre). Transcris le verbe de la citation du Prophète lettre à lettre (اعتمري ou autre).` },
  { tag: 'p154-malik-miq', ask: `${BASE}\nTranscris le texte de مالك (question sur المواقيت + citation entre « » + renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre). Le verbe avant التلبية : transcris-le lettre à lettre (يقضي ou يقطع ou autre).` },
  { tag: 'p154-hicham', ask: `${BASE}\nTranscris le hadith d'هشام بن عروة (isnad + citation entre « » + renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre).` },
  { tag: 'p154-notice', ask: `${BASE}\nTranscris la notice biographique (أبو بكر بن عبد الرحمن...) avec les années de mort CHIFFRE PAR CHIFFRE en NUM:. Note aussi كل qualification (فقهاء السبعة؟ راهب قريش؟ مكفوف؟).` },
  { tag: 'p154-charh', ask: `${BASE}\nTranscris la rubrique الشرح et toutes ses gloses (terme: explication) exactement — chaque glose lettre à lettre.` },
  { tag: 'p155-istikhlas', ask: `${BASE}\nTranscris le titre استخلاص المضامين et TOUS les items numérotés — précise combien d'items sont numérotés (1-، 2-، 3- ou sans numéro).` },
  { tag: 'p155-malik-sunna', ask: `${BASE}\nTranscris la citation de مالك entre « » et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre. Transcris le mot qui décrit la العمرة lettre à lettre (سنة مؤكدة، ضضض...).` },
  { tag: 'p155-kaffara', ask: `${BASE}\nTranscris le hadith d'أبي هريرة entre « » et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'p156-ramadan', ask: `${BASE}\nTranscris le paragraphe فضل العمرة في رمضان (la citation du Prophète entre « » lettre à lettre).` },
  { tag: 'p156-repetition', ask: `${BASE}\nTranscris la citation de مالك sur le تكرار entre « » (le mot final avant le renvoi : مرارا أو أكثر ou autre — lettre à lettre) et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'p156-miqat', ask: `${BASE}\nTranscris le paragraphe ميقات العمرة et la citation de مالك entre « » avec son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre. Les noms des miqāts (التنعيم، الجعرانة، الحديبية) lettre à lettre.` },
  { tag: 'p157-3umras', ask: `${BASE}\nTranscris le titre ثانيا: عمر النبي et le passage sur les trois عمرات (les trois noms d'années exactement + renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre).` },
  { tag: 'p157-hicham2', ask: `${BASE}\nTranscris le passage ويؤيد القول الأول ما رواه هشام... avec la citation entre « » et son renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre.` },
  { tag: 'p157-said', ask: `${BASE}\nTranscris le passage sur سعيد بن المسيب (question + citation entre « » + renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre). Le premier mot de la citation de سعيد : lettre à lettre.` },
  { tag: 'p158-umar-salama', ask: `${BASE}\nTranscris le hadith d'عمر بن أبي سلامة (isnad + citation entre « » + renvoi [الموطأ رقم: N] — NUM: chiffre par chiffre).` },
  { tag: 'p158-idad', ask: `${BASE}\nTranscris les deux questions numérotées de الإعداد القبلي lettre à lettre.` },
];

async function readOne(zai, t) {
  const out = `${OUTDIR}/c-${t.tag}.txt`;
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
  const todo = TASKS.filter(t => !fs.existsSync(`${OUTDIR}/c-${t.tag}.txt`));
  console.log(`tâches: ${todo.length}/${TASKS.length}`);
  for (const t of todo) {
    const r = await readOne(zai, t);
    console.log(r);
    await new Promise(r => setTimeout(r, 3500));
  }
}
main().catch(e => { console.error('FATAL', e); process.exit(1); });
