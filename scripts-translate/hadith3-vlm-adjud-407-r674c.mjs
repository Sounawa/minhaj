// R674-C — lectures VLM d'ADJUDICATION leçon 407 (crops a-*, ronde de conflits + p.129).
// Chaque zone est tranchée sur preuve image ; ne jamais deviner.
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/qa-crops-r674c';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-407';
fs.mkdirSync(OUTDIR, { recursive: true });

const PROMPTS = {
  'a-p124-aya': `Ligne d'un manuel arabe avec une citation coranique ﴿...﴾ suivie d'un renvoi bleu [سورة الحج الآية: N]. IMPORTANT : transcris la citation MOT POUR MOT depuis l'image, même si elle ne correspond à aucun verset que tu connais. N'importe PAS de texte coranique de mémoire. Donne NUM: pour N chiffre par chiffre (٠=0…٩=9). Transcris aussi le fragment qui précède et qui suit la citation.`,
  'a-p125-h1135': `Hadith du Muwaṭṭaʾ complet très zoomé (récit d'Hibbār/Habbar fils d'al-Aswad devant ʿUmar le jour du nahr). Transcris TOUT exactement ligne par ligne, marque [?] l'illisible, ne complète PAS de mémoire. Donne NUM: pour le renvoi [الموطأ رقم: N] chiffre par chiffre.`,
  'a-p126-rule': `Paragraphe فقهي d'un manuel arabe : « إذا عطب الهدي قبل بلوغ محله... ». Transcris TOUT exactement ligne par ligne. Attention spéciale : (1) après «؛» le mot introducteur de la preuve est-il «لقوله تعالى» ou «لقوله عليه الصلاة والسلام» ? transcris le mot exact visible ; (2) la clause entre « ولا يأكل منه » et «؛» — transcris-la mot pour mot ; (3) la citation entre « » — mot pour mot. Marque [?] l'illisible.`,
  'a-p126-q1125': `Bloc d'un manuel arabe : «2- ضياع الهدي» puis règle puis citation d'ابن عمر رضي الله عنهما entre « » puis renvoi [الموطأ رقم: N]. Transcris tout exactement, diacritiques comprises. Dans la citation, précise si tu lis «إن نذرها» ou «إن أنث» ou autre — transcris les lettres visibles. NUM: chiffre par chiffre.`,
  'a-p126-thania': `Titres de section d'un manuel arabe très zoomés : «ثانيا: أحكام من فاته الحج» puis «1 - فوات الحج ... مباشرة الزوجة». Dans le sous-titre, la particule avant «مباشرة» est-elle «بغير» ou «بسبب» ? Regarde les lettres GLYPHE PAR GLYPHE : ب-غ-ير vs ب-س-ب. Transcris le titre exactement. Transcris aussi la ligne suivante (من فاته الحج...) en entier.`,
  'a-p127-h1134': `Hadith du Muwaṭṭaʾ n° 1134 très zoomé. Transcris TOUT exactement ligne par ligne, marque [?] l'illisible, ne complète PAS de mémoire. Points à trancher : le nom du rapporteur (أن أبا ... الخ), le nom de lieu (بالنازية ou autre), les paroles dʿUmar «فقال عمر: ...» mot pour mot, et «ما استطعت من الهدي» vs «ما استيسر من الهدي» — transcris ce qui est visible. NUM: chiffre par chiffre.`,
  'a-p127-q1136': `Citation de مالك entre « » dans un manuel arabe très zoomé (cas du qārin dont le ḥaǧǧ a manqué) + renvoi [الموطأ رقم: N]. Transcris la citation MOT POUR MOT, diacritiques comprises, même si elle semble inhabituelle. NUM: chiffre par chiffre.`,
  'a-p127-h1128': `Récit complet rapporté par يحيى بن سعيد de سعيد بن المسيب (question sur un muḥrim ayant touché sa femme). Transcris TOUT exactement ligne par ligne, marque [?] l'illisible. Ne complète PAS de mémoire. NUM: chiffre par chiffre pour le renvoi final.`,
  'a-p127-after2': `Passage فقهي «وإن باشر الحاج زوجته بعد رمي جمرة العقبة وقبل طواف الإفاضة...». Transcris tout exactement. Attention : après «صحيح؛ لوقوعه بعد التحلل» le texte suivant est-il «غير أنه وقع» ou «غايته أنه وقع» ? glyphe par glyphe. Transcris la dernière ligne aussi.`,
  'a-p128-malik1129': `Passage très zoomé : suite de paroles de مالك «ففي رجل وقع بامراته في الحج...» avec citation entre « » et renvoi [الموطأ رقم: N]. Transcris TOUT exactement ligne par ligne, diacritiques comprises, ne complète PAS de mémoire. NUM: chiffre par chiffre.`,
  'a-p128-h1138': `Lignes d'un manuel arabe très zoomées : isnad «فعن ... بن زيد الديلي عن عكرمة مولى ابن عباس» puis citation entre « » puis renvoi [الموطأ رقم: N]. Le premier nom de l'isnad : transcris-le GLYPHE PAR GLYPHE lettre par lettre (c'est peut-être نُزَيْل, نَوَّار, قَثْن ou autre — lis ce qui est imprimé). Transcris la citation mot pour mot. NUM: chiffre par chiffre.`,
  'a-p128-h1139': `Ligne très zoomée : «قول ربيعة بن عبد الرحمن قال مالك: «...»» + renvoi [الموطأ رقم: N]. Dans la citation, précise si tu lis «ما سمعت الْيَوْمَ» ou «ما سمعتُ إليَّ» — glyphe par glyphe. Transcris la ligne entière exactement. NUM: chiffre par chiffre.`,
  'a-p128-h1140': `Athar final très zoomé : «سُئل مالك عن رجل نسى الطواف الإفاضة...» avec citation entre « » + renvoi [الموطأ رقم: N]. Transcris TOUT exactement, diacritiques comprises, ne complète PAS de mémoire. NUM: chiffre par chiffre.`,
  'a-p129-full': `Page entière d'un manuel arabe (couleur). Transcris TOUT le texte visible exactement, ligne par ligne, en haut et en bas de page, y compris les titres encadrés ou colorés (أتأمل النص / أحفظ أحاديث الدرس المقبل وأجيب عن), la citation avec بشرح الزرقاني, et les questions numérotées 1- 2- 3-. Marque [?] l'illisible. Ne complète PAS de mémoire. NUM: pour tout renvoi visible.`,
  'a-p129-announce': `Bas de page d'un manuel arabe : bannière «أحفظ أحاديث الدرس المقبل وأجيب عن الآتي:» puis trois questions numérotées 1- 2- 3-. Transcris la bannière et les trois questions EXACTEMENT, glyphe par glyphe, diacritiques comprises. Ne complète PAS de mémoire.`,
  'a-p130-top': `Haut de page d'un manuel arabe : médaillon circulaire coloré avec un numéro de cours, une bannière calligraphiée (titre de cours), puis des objectifs numérotés 1- 2- 3- et le début de l'introduction. Décris le numéro du médaillon CHIFFRE PAR CHIFFRE, transcris la bannière calligraphiée, puis les objectifs et les lignes suivantes exactement. NUM: pour tout renvoi coranique visible (سورة ... آية N).`,
};

async function main() {
  const zai = await ZAI.create();
  const tags = Object.keys(PROMPTS).filter(t => fs.existsSync(`${DIR}/${t}.png`) && !fs.existsSync(`${OUTDIR}/${t}.txt`));
  console.log(`tâches adjudication: ${tags.length}`);
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
        const wait = msg.includes('429') ? 20000 * k : 5000;
        await new Promise(r => setTimeout(r, wait));
      }
    }
    await new Promise(r => setTimeout(r, 3500));
  }
  console.log('VLM adjudication terminé');
}
main().catch(e => { console.error('VLM_ERR: ' + (e?.message || e)); process.exit(1); });
