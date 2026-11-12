// R691-b — lectures VLM des microcrops fins d'adjudication leçon 413.
// Usage: node scripts-translate/r691-vlm-413-micro.mjs
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/m413-r691b';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-413';
fs.mkdirSync(OUTDIR, { recursive: true });

const BASE = `Microcrop à très fort zoom (900 dpi) d'un manuel scolaire arabe (hadith, 3e année, Muwaṭṭaʾ de l'imam Mālik). Transcris EXACTEMENT tout le texte visible ligne par ligne en arabe, EN CONSERVANT les diacritiques visibles (فتحة ضمة كسرة شدة) et les guillemets « ». Pour tout renvoi [الموطأ رقم: N] ou [سورة X الآية: N], transcris le nombre CHIFFRE PAR CHIFFRE sous la forme NUM: <chiffres>. Distingue avec soin les lettres proches : ذ vs ن vs ر vs د ; ش vs س ; ة vs ه. Ne devine RIEN : transcris ce qui est visible, marque [?] l'illisible. Si la zone est décorative (titre encadré), transcris-la aussi.`;

const TASKS = [
  { tag: 'm159-obj', ask: `${BASE}\nTranscris le médaillon (الدرس + numéro + titre) et la rubrique أهداف الدرس avec TOUS les objectifs numérotés visibles lettre à lettre. Mot clé : le premier objectif finit-il par وحكمها ou وأحكامها ?` },
  { tag: 'm159-tamh', ask: `${BASE}\nTranscris TOUT : rubrique تمهيد, le paragraphe (le premier verbe après الأضحية شعيرة من الشعائر الدينية est يذبحها ou ينبغها ou autre ? lettre à lettre ; le verbe avant النبي ﷺ : وحثّ/وحدّ/أمر/autre lettre à lettre ; le dernier mot : مشروعيتها ou مشروعتها), la citation calligraphique ﴿...﴾ lettre à lettre, le renvoi NUM chiffre par chiffre, la question finale فما مفهوم... exactement.` },
  { tag: 'm159-t1367', ask: `${BASE}\nTranscris le hadith complet (isnad + matn entre « » + renvoi NUM). Lettre à lettre : أحب/أُحِبّ ? لأحد من قوي ou لأحد قوي ? le mot après على : تمنها ou شعرها ou نفسها ? le mot final : يتركها. Chaque harakat visible.` },
  { tag: 'm159-t1364', ask: `${BASE}\nTranscris le hadith complet (isnad + matn entre « » + renvoi NUM). Lettre à lettre : le premier mot du matn est الأضحية ou الأضحى ? puis يومان بعد يوم الأضحى ? Les harakats.` },
  { tag: 'm160-t1354', ask: `${BASE}\nTranscris le hadith complet (isnad + matn + renvoi NUM). Lettre à lettre : ضحى ضحيته ? قبل أن يذبح/يُذبح رسول الله ﷺ يوم الأضحى ? فأنبأه/فرعع ? أن يعود بضحية أخرى ? لا أجد إلا جدعًا يا رسول الله ? قال له : وإن لم تجد إلا جدعًا فاذبح/فذبحه lettre à lettre.` },
  { tag: 'm160-notice', ask: `${BASE}\nTranscris TOUT : rubrique ترجمة الراوي + la notice complète. Lettre à lettre : le nom أبو بردة رضي الله عنه : هانئ بن نيار؟ البلوي؟ الأنصاري ? شهد بدرا والمشاهد كلها ? روى عنه ابن أخته البراء بن عازب وجابر بن عبد الله وجماعة مات سنة N — NUM chiffre par chiffre.` },
  { tag: 'm160-gloss', ask: `${BASE}\nTranscris la rubrique الشرح et TOUTES les gloses (terme : explication) — chaque glose lettre à lettre avec les harakats (بفتح الدال والجيم ? بفتح الجيم والدال ?).` },
  { tag: 'm161-hukm', ask: `${BASE}\nTranscris TOUT : la glose de عياض lettre à lettre (سُمّيت بذلك ; لأنها تُفعل/تَفَعَّل في الضحى ; ارتفاع النهار ; فسميت بزمن فعلها), la phrase هذا هو الأصل ثم غلب استعماله..., le titre rouge ٢- حكم الأضحية, et la première phrase الأضحية سنة مؤكدة... lettre à lettre.` },
  { tag: 'm161-muslim', ask: `${BASE}\nTranscris TOUT lettre à lettre : la phrase والذين بمنى..., والجملة avec الموطأ: «الضحية سنة وليست بواجبة» (harakats), وقوله: «وليست بواجبة» زيادة في البيان..., لدفع توهم..., فبين المراد بالسنة والحجة..., et la citation de صحيح مسلم عن أم سلمة : «إذا رأيتم هلال ذي الحجة وأراد أحدكم أن يضحي فليمسك/فليصق/فليضح عن شعره وأظفاره» — le verbe après يضحي lettre à lettre.` },
  { tag: 'm161-tabarani', ask: `${BASE}\nTranscris TOUT lettre à lettre : ففي قوله «أراد» دليل..., la phrase وصرح/وثبت بالنكية/بالسنة في حديث الطبراني عن ابن عباس مرفوعا, la citation «الأضحى عليّ فريضة وعليكم سنة» lettre à lettre, et le titre rouge ثانيا: وقت الأضحية.` },
  { tag: 'm161-ayam', ask: `${BASE}\nTranscris TOUT lettre à lettre : le titre ١- أيام الأضحية, la phrase ذهب مالك وأبو حنيفة وأحمد وأكثر العلماء..., يوم النحر ويومان بعده ولا أضحية في يوم الرابع؟ (lettre à lettre), لما رواه مالك في الموطأ عن نافع أن عبد الله بن عمر قال: «...» lettre à lettre.` },
  { tag: 'm161-ibnumar', ask: `${BASE}\nTranscris TOUT lettre à lettre : ومثله مروي عن علي بن أبي طالب..., la phrase فهذا وإن كان موقوفا على الصحابة... — le verbe final avant حكم الرفع : فيبطل/فيسقط/فينتفض lettre à lettre — et وإن/وأو.` },
  { tag: 'm161-qassar', ask: `${BASE}\nTranscris TOUT lettre à lettre : وقد استدل ابن القصار/القاسم؟ في ذلك بقوله تعالى, la citation ﴿...﴾ lettre à lettre, le renvoi [سورة الحج الآية: N] — NUM chiffre par chiffre (٢٦ ou ٢٨ ?).` },
  { tag: 'm162-analyse', ask: `${BASE}\nTranscris TOUT lettre à lettre : قال: «والأيام المعلومات: يوم النحر ويومان بعده»..., والأيام المعدودات ثلاثة بعد يوم النحر..., فيوم النحر معلوم غير معدود..., la citation ﴿...﴾ lettre à lettre et le renvoi [سورة البقرة الآية: N] — NUM chiffre par chiffre (٢٠١ ou ٢٠٣ ?).` },
  { tag: 'm162-msalik', ask: `${BASE}\nTranscris TOUT lettre à lettre : l'attribution entre parenthèses ou crochets (المسالك في شرح موطأ مالك لابن العربي؟ لابن عرفة؟ + cote 5/196 — NUM chiffre par chiffre), et le titre rouge ٢- حكم ذبح الأضحية قبل الصلاة.` },
  { tag: 'm162-barra', ask: `${BASE}\nTranscris TOUT lettre à lettre : لا خلاف بين العلماء..., كما جاء في حديث الدرس, وفي الصحيحين؟ عن البراء..., خَطَبَنَا رَسُولَ اللهِ ﷺ يَوْمَ النَّحْرِ, (وفي رواية: يوم الأضحى بعد الصلاة), فَقَالَ: مَنْ صَلَّى صَلَاتِنَا وَنَسَكَ نُسُكِنَا فَقَدْ أَصَابَ النُّسُكَ, وَمَنْ ذَبَحَ قَبْلَ الصَّلَاةِ فَلَكَ شَاةِ لَحْمٍ (شاة/شاه lettre à lettre), فَقَامَ أَبُو بُرْدَةَ بْنَ نِيَارٍ..., نَسَكْتُ شَاتِي..., وَعَرَفْتَ أَنَّ الْيَوْمَ يَوْمَ كُلٍّ وَشَرْبٍ (كل/كيل lettre à lettre), فَتَعَجَّلْتُ وَأَكَلْتُ وَأَطْعَمْتُ أَهْلِي وَجِيرَانِي, فَقَالَ رَسُولُ اللهِ ﷺ: تِلْكَ شَاةُ لَحْمٍ/شَاةُ لَحْمٍ lettre à lettre.` },
  { tag: 'm162-jabir', ask: `${BASE}\nTranscris TOUT lettre à lettre : ذهب مالك والشافعي والأوزاعي..., للحديث الذي أخرجه مسلم عن جابر..., «أَنَّ النَّبِيَّ ﷺ صَلَّى يَوْمَ النَّحْرِ بِالْمَدِينَةِ فَسَبَقَهُ رِجَالٌ فَنَحَرُوا وَظَنُّوا أَنَّهُ قَدْ نَحَرَ فَأَمَرَ رَسُولَ اللهِ ﷺ مَنْ كَانَ نَحَرَ قَبْلَهُ أَنْ يُعِيدَ بـ...» — le mot après يعيد ب : نحرٍ/غيرٍ/شاةٍ lettre à lettre — وَلَا يَنْحَرُوا حَتَّى يَنْحَرَ, وَقَالَ الْحَسَنُ فِي قَوْلِهِ تَعَالَى, la citation calligraphique ﴿...﴾ lettre à lettre, le renvoi [سورة الحجرات الآية: N] NUM, نزلت في قوم ذبحوا قبل أن يضحي النبي ﷺ فأمرهم أن يعيدوا lettre à lettre.` },
  { tag: 'm163-taqwim', ask: `${BASE}\nTranscris la rubrique verte et les items numérotés lettre à lettre — combien d'items ? Le titre de la rubrique : التقويم ? précisément.` },
  { tag: 'm163-t1356', ask: `${BASE}\nTranscris la rubrique verte puis le texte n° 1356 ENTIER lettre à lettre : ضحى بمرة/مرة بالمدينة, فأمرني أن أشتري له كبشًا فحيلًا/فحلًا + le mot suivant (أقرن/أفرن/عظم/autre lettre à lettre), ثم ذبحه يوم الأضحى في مصلى الناس, ففعلت, ثم حمل إلى عبد الله بن عمر فحلق رأسه حين ذبح الكبش, وكان مريضًا لم يشهد العيد مع الناس, وكان عبد الله بن عمر يقول: ليس/... (la fin du texte lettre à lettre + قد فعله عبد الله بن عمر), renvoi NUM.` },
  { tag: 'm163-idad', ask: `${BASE}\nTranscris TOUT : la rubrique verte (الاستثمار ?), la consigne أقرأ الأثر..., la rubrique الإعداد القبلي/الإعداد التربوي (lettre à lettre), la consigne أحفظ أحاديث الدرس المقبل..., et l'exercice avec ses éléments — chaque mot lettre à lettre (أشرح؟ ظلعها؟ العوراء؟ العجفاء؟ لا تنقي؟).` },
];

async function readOne(zai, t) {
  const out = `${OUTDIR}/m-${t.tag}.txt`;
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
  const todo = TASKS.filter(t => !fs.existsSync(`${OUTDIR}/m-${t.tag}.txt`));
  console.log(`tâches: ${todo.length}/${TASKS.length}`);
  for (const t of todo) {
    const r = await readOne(zai, t);
    console.log(r);
    await new Promise(r => setTimeout(r, 3500));
  }
}
main().catch(e => { console.error('FATAL', e); process.exit(1); });
