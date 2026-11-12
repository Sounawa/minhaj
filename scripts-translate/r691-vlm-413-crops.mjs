// R691 — lectures VLM des microcrops d'adjudication leçon 413 hadith-3es (la uḍḥiya).
// Usage: node scripts-translate/r691-vlm-413-crops.mjs
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/m413-r691';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-413';
fs.mkdirSync(OUTDIR, { recursive: true });

const BASE = `Zone d'un manuel scolaire arabe (hadith, 3e année secondaire, Muwaṭṭaʾ de l'imam Mālik) à très fort zoom. Transcris EXACTEMENT tout le texte visible, ligne par ligne, en arabe, en conservant diacritiques, crochets [] et guillemets « ». Pour tout renvoi [الموطأ رقم: N] ou [سورة X الآية: N], transcris le nombre N CHIFFRE PAR CHIFFRE (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9 et chiffres latins) sous la forme NUM: <chiffres latins>. Ne devine rien : transcris ce qui est visible, marque [?] l'illisible.`;

const TASKS = [
  { tag: 'p159-a', ask: `${BASE}\nTranscris le médaillon (numéro du درس et titre) exactement lettre à lettre, puis la rubrique أهداف الدرس et les objectifs numérotés visibles lettre à lettre — précise combien d'objectifs apparaissent.` },
  { tag: 'p159-b', ask: `${BASE}\nTranscris TOUT (objectifs restants avec leurs numéros, rubrique تمهيد, paragraphe du tamhīd, citation coranique calligraphique entre ﴿ ﴾ lettre à lettre, renvoi [سورة الكوثر الآية: N] — NUM: chiffre par chiffre).` },
  { tag: 'p159-c', ask: `${BASE}\nTranscris TOUT (fin du tamhīd, la question d'ouverture فما مفهوم..., rubrique des textes, le hadith n° 1367 : isnad + citation entre « » + renvoi NUM: chiffre par chiffre).` },
  { tag: 'p160-a', ask: `${BASE}\nTranscris TOUT (le hadith n° 1364 : isnad + citation entre « » + renvoi [الموطأ رقم: N] — NUM chiffre par chiffre — et le début du hadith n° 1354). Transcris chaque mot lettre à lettre.` },
  { tag: 'p160-b', ask: `${BASE}\nTranscris TOUT (le hadith n° 1354 complet : isnad + récit + citations entre « » + renvoi NUM chiffre par chiffre ; rubrique ترجمة الراوي ; début de la notice). Transcris les verbes أنبأه/ضحى/جدعًا lettre à lettre.` },
  { tag: 'p160-c', ask: `${BASE}\nTranscris TOUT (fin de notice avec année de mort NUM chiffre par chiffre ; rubrique الشرح et les deux gloses exactement — chaque glose lettre à lettre ; rubrique استخلاص المضامين et ses items numérotés).` },
  { tag: 'p160-d', ask: `${BASE}\nTranscris TOUT (le titre أولا: مفهوم الأضحية وحكمها ; la glose de عياض lettre à lettre ; le titre ٢- حكم الأضحية ; la citation de مالك entre « » ; la citation de صحيح مسلم entre « » avec le mot فليصق/فليمسك lettre à lettre ; l'attribution الطبراني et sa citation « الأضحى عليّ... » lettre à lettre).` },
  { tag: 'p161-a', ask: `${BASE}\nTranscris TOUT lettre à lettre (ce que la zone contient : suite de حكم الأضحية ou دبت الثانيا: وقت الأضحية, etc.).` },
  { tag: 'p161-b', ask: `${BASE}\nTranscris TOUT lettre à lettre (rubrique rouge ثانيا: وقت الأضحية si visible, titre ١- أيام الأضحية, la phrase ذهب مالك وأبو حنيفة وأحمد وأكثر العلماء..., la citation entre « » et l'āya ﴿...﴾ avec renvoi [سورة الحج الآية: N] — NUM chiffre par chiffre).` },
  { tag: 'p161-c', ask: `${BASE}\nTranscris TOUT lettre à lettre (suite de l'analyse des jours, la citation قال: «والأيام المعلومات...», l'āya suivante ﴿...﴾ avec renvoi [سورة البقرة الآية: N] — NUM chiffre par chiffre, l'attribution كتاب/شرح + auteur + cote chiffrée).` },
  { tag: 'p162-a', ask: `${BASE}\nTranscris TOUT lettre à lettre (rubrique rouge ٢- حكم ذبح الأضحية قبل الصلاة si visible, le paragraphe لا خلاف بين العلماء..., la citation وَفي... letter à letter).` },
  { tag: 'p162-b', ask: `${BASE}\nTranscris TOUT lettre à lettre (la رواية du hadith : خطبنا رسول الله ﷺ يوم النحر... chaque mot lettre à lettre, surtout فَذَبَّحْهُ/فَاذْبَحْهُ et شَاة/شَاه et نَحَر).` },
  { tag: 'p162-c', ask: `${BASE}\nTranscris TOUT lettre à lettre (rubrique ٣- حكم ذبح الأضحية بعد الصلاة وقبل ذبح الإمام si visible ; le hadith de جابر entre « » — le mot après يعيد lettre à lettre (بشاة/بغير) ; وقال الحسن ; l'āya calligraphique ﴿...﴾ avec renvoi [سورة الحجرات الآية: N] — NUM).` },
  { tag: 'p163-a', ask: `${BASE}\nTranscris TOUT lettre à lettre (rubrique verte si visible + les items numérotés — précise le nombre d'items et leurs numéros).` },
  { tag: 'p163-b', ask: `${BASE}\nTranscris TOUT lettre à lettre (le texte n° 1356 d'عبد الله بن عمر : isnad + récit complet + citations entre « » + renvoi [الموطأ رقم: N] — NUM chiffre par chiffre). Transcris le mot après كبشًا lettre à lettre (فحلّا/أفرن/...) et la fin du texte.` },
  { tag: 'p163-c', ask: `${BASE}\nTranscris TOUT lettre à lettre (rubrique الاستثمار si visible, la consigne أقرأ الأثر..., rubrique الإعداد القبلي, la consigne أحفظ أحاديث..., l'exercice avec ses éléments — chaque mot lettre à lettre).` },
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
