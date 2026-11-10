// R684 — lectures VLM ciblées des zones restées incertaines (leçon 408).
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/tr-tmp/qa-crops-r684';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-408';

const BASE = `Image d'un manuel scolaire arabe (hadith-3es, leçon 19 «ما يفعله الحاج يوم النحر», pages PDF 129-136). Transcris la zone EXACTEMENT, mot à mot, en arabe avec diacritiques. Ne devine JAMAIS : un mot illisible → [lettres lisibles?]. Transcris tout nombre CHIFFRE PAR CHIFFRE (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9) en NUM: <chiffres latins>.`;

const TASKS = [
  { tag: 't129-annonce', ask: `${BASE}
Transcris TOUT le contenu visible de cette zone de la page 129 (haut de page) : l'invite d'examen «أتأمل النص وأستعين بشرح الزرقاني...», la bannière «الإعداد القبلي» ou «الإعداد التمهيدي», la consigne «أحفظ أحاديث الدرس المقبل...» et les questions numérotées une à une (combien y en a-t-il ?). Puis dis S'IL EXISTE autre chose sur la zone : encadré de fatwā, renvoi [الموطأ رقم: N], renvoi coranique, numéro de folio. Transcris la première question lettre par lettre, surtout les deux entrées lexicales après «أشرح:».` },
  { tag: 't129-bas', ask: `${BASE}
Zone du BAS de la page 129. Transcris tout texte visible. S'il n'y a RIEN (page blanche), dis-le explicitement. Cherche spécifiquement : un encadré de fatwā ( bandeau titré فتوى ou استثمار ), un renvoi [الموطأ رقم: N], un folio.` },
  { tag: 't130-tamhid', ask: `${BASE}
Zone du tamhīd (تهيئة) de la leçon, page 130. Transcris TOUTES les lignes dans l'ordre : le texte d'introduction «من أيام الحج المشهودة...», le ou les versets coraniques entre ﴿ ﴾, le ou les renvois bleus [سورة ... الآية: N] (transcris le nom de la sourate et le chiffre CHIFFRE PAR CHIFFRE en NUM:), la ou les lignes après le renvoi. S'il y a PLUSIEURS versets ou PLUSIEURS renvois dans la zone, transcris-les TOUS dans l'ordre exact.` },
  { tag: 't130-aya-tight', ask: `${BASE}
Zoom serré sur le verset coranique du tamhīd et son renvoi, page 130. Transcris le verset ﴿...﴾ mot à mot puis le renvoi bleu [سورة ... الآية: N] — le nom de la sourate LETTRE PAR LETTRE et le chiffre CHIFFRE PAR CHIFFRE (٠=0 ١=1 ٢=2 ٣=3 ٤=4 ٥=5 ٦=6 ٧=7 ٨=8 ٩=9) en NUM:. S'il n'y a AUCUN chiffre après le nom de la sourate, dis-le explicitement.` },
  { tag: 't133-ali', ask: `${BASE}
Ligne(s) du hadith d'ʿAlī, page 133. Transcris EXACTEMENT : «فقد ثبت عن علي رضي الله عنه: أنّ رسول الله ﷺ نحر ...» — le complément du premier نحر (بعض هديه ? بيده ? بيضه ?) lettre par lettre, puis le second membre «ونحر ... بغيره» (بعضه ? غيره ? بضعه ?) lettre par lettre, puis le renvoi [الموطأ رقم: N] en NUM:, puis la ligne suivante (وفي هذا العصر...).` },
  { tag: 't134-tayb', ask: `${BASE}
Ligne de la page 134 contenant «وكذلك الطيب عند ابن عمر، وكرهه مالك ...». Transcris-la EXACTEMENT mot à mot — notamment ce qui suit «وكرهه مالك» (فقط ? ويحرم الصيد ? لقوله تعالى ?), et si un renvoi coranique [سورة المائدة الآية: N] suit, transcris le chiffre en NUM:.` },
  { tag: 't134-lubd', ask: `${BASE}
Titre de sous-section + première phrase, page 134 : «2- تحلّل من لبّد شعره أو عقصه أو ...». Transcris le TROISIÈME mot de la triade après «أو» LETTRE PAR LETTRE (ظفره ? ضفره ? وفّره ? — ظ = point unique au-dessus, ض = point unique au-dessus décalé, و = boucle) et la suite «وجب عليه الحلاق ولا يجوز له التقصير؛ فعن سعيد بن المسيب...».` },
  { tag: 't135-encadre', ask: `${BASE}
Encadré de la page 135. Transcris DANS L'ORDRE : (1) le bandeau-titre (mot bleu sur pastille verte — transcris-le LETTRE PAR LETTRE : الاستثمار ? الاستشهاد ? الاستفتاء ?), (2) tout l'athar «عن عبد الله بن عمر: أنه لقي رجلاً من أهله بـ...» mot à mot — notamment le LIEU après «من أهله بـ» (بالمدينة ? بمكة ?) et le mot après «ولم يقصر» (جهلاً ? جاهلاً ?), (3) le renvoi [الموطأ رقم: N] CHIFFRE PAR CHIFFRE en NUM:.` },
  { tag: 't135-athar-end', ask: `${BASE}
Zoom sur la DERNIÈRE ligne de l'athar de l'encadré, page 135. La ligne commence par «ثُمَّ» ou «يَرْجِعُ». Transcris-la EXACTEMENT lettre par lettre : يرجع إلى ... (البيت ? الذي قد أفاض ?) et le renvoi [الموطأ رقم: N] en NUM:. Ne devine pas : décris ce que tu vois.` },
  { tag: 't135-cloture', ask: `${BASE}
Zone de clôture de la page 135 : l'invite «أتأمل النص وأستعين بشرح الزرقاني لأبين...», la bannière «الإعداد القبلي», la consigne «أحفظ أحاديث الدرس المقبل وأجيب عن الآتي» et les questions numérotées. Transcris TOUT dans l'ordre. COMBIEN de questions numérotées y a-t-il (2 ? 3 ?) ? Transcris chacune mot à mot — notamment «نوعي التحلل ou التحليل» et «ميزاتهما ou مفاتيهما». Y a-t-il quoi que ce soit D'AUTRE sur la zone (exercice, renvoi, folio) ? Le bas de la page est-il blanc ?` },
  { tag: 't136-top', async: false, ask: `${BASE}
Haut de la page 136 : c'est l'ouverture de la leçon SUIVANTE (borne supérieure de la leçon 408). Transcris : le numéro dans le médaillon (الدرس ?), la bannière du titre (أحكام الحلق والتقصير ?), la rubrique أهداف الدرس et les objectifs visibles un à un. Rien d'autre.` },
];

async function readOne(zai, t) {
  const out = `${OUTDIR}/r684-${t.tag}.txt`;
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
      await new Promise(r => setTimeout(r, wait));
    }
  }
}

async function main() {
  const zai = await ZAI.create();
  for (const t of TASKS) console.log(await readOne(zai, t));
}
main().catch(e => { console.error('FATAL', e); process.exit(1); });
