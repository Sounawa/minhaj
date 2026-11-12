import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/tr-tmp/qa-crops-r689c';
const OUTDIR = '/home/z/my-project/tr-tmp/vlm-411';
const TASKS = [
  { tag: 'a411-1263-anaq', ask: `Zoom 900 dpi d'un manuel arabe (hadith n° 1263). Dans la phrase « فتكون كفارة ذلك ... رقبة على كل إنسان منهم », le mot avant رقبة est-il « عَنْقُ » (ع ن ق : point SUR le ق, sens = cou d'un esclave) ou « عَتْقُ » (ع ت ق : point SUR le ت, sens = affranchissement) ? Et le mot avant : « كفارة ذلك » exactement ? Transcris la phrase entière lettre par lettre. Ne devine pas : décris les points.` },
  { tag: 'b411-1252-lalaka', ask: `Zoom 900 dpi (hadith n° 1252, Ka'b b. 'Ajra). Le Prophète ﷺ dit à Ka'b une première phrase : « ... أذاك هوامك ». 1) Avant أذاك : est-ce « لَعَلَكَ » (ل ع ل ك) ou « أَأَذَاكَ » (hamza + alif) ou autre ? 2) Le mot أذاك porte-t-il un madda sur l'alif (آذاك) ? 3) Le mot هوامك : هوامّك ou هوامك ? Transcris la phrase entière + la réponse de Ka'b (« نعم يا رسول الله ») lettre par lettre. Ne devine pas.` },
  { tag: 'c411-gloses-istihlas', ask: `Zoom 900 dpi d'un manuel arabe. DEUX questions : 1) La glose « أنسك بشاة: ... إلى الله تعالى » — transcris-la EXACTEMENT : après « اذبح شاة » le mot est « تقرَّبا » ou « تقرَّب بها » ou autre ? 2) La glose suivante commence par « ق...ة: بفتح القاف، والضم لغة، أي حفنة » — le mot de tête est-il « قَبْضَة » (qabḍa, fatha sur ق, sans kasra) ou « قِبْضَة » (kasra sous ق) ? Regarde le signe de vocalisation sous/alors le ق initial. 3) Ensuite les deux items de « استخلاص المضامين » : commencent-ils par « أستخرج / أستخلص » (avec hamza initiale) ou « استخرج / استخلص » (sans hamza) ? Transcris les deux items entiers. Ne devine pas.` },
  { tag: 'd411-1255-fin', ask: `Zoom 900 dpi (fin du hadith n° 1255). La fin de la phrase : « فعليه فدية ... ». Suite exacte : « كما مُرَّ الله به » ou « كما أمره الله تعالى » ou « كما مَرَّ الله به » ou autre ? Décris lettre par lettre après الفدية : ي-ة puis ك-م-ا puis م/أ-ر-... Transcris la fin complète. Ne devine pas.` },
  { tag: 'e411-madin-nazalat', ask: `Zoom 900 dpi d'un manuel arabe (fiqh, hadith n° 1251). QUATRE transcriptions lettre par lettre : 1) La phrase « والتكرير في (مدين مدين) لإفادة عموم ... » — le mot après عموم est-il « النية » ou « المدِّ » ou autre ? Décris les points. 2) La phrase suivante « أي مد لكل مسكين » ou « أي مدين لكل مسكين » ? 3) Le hadith des deux authentiques : « نزلت الآية ... » — le premier mot : « نُزِّلَتِ » (shadda) ? Et le mot suivant : « خاضَة » (avec ض) ou « خَاصَّة » (avec ص + shadda) ? 4) La phrase « وفي هذا دلالة لأصح/لأصحاب قول/قولي مالك » — transcris-la exactement : avant قول y a-t-il « لأصح » ou « لأصحاب » ? et après مالك ? Ne devine pas.` },
  { tag: 'f411-dhimm', ask: `Zoom 900 dpi (bas de p.149). Dans « ... عامدا من غير ضرورة فعليه ... », le mot final est-il « ذِمٌ » (ذ + م, 2 mots) ou « ذِمَامٌ » (ذ م ا م) ou « ذِمَّة » ? Décris les lettres et points. Transcris la fin de la phrase entière. Ne devine pas.` },
  { tag: 'g411-1256-tafl', ask: `Zoom 900 dpi (hadith n° 1256). Transcris TOUT le hadith lettre par lettre : 1) Le premier mot : « مَنْ تَفَلَّ » (ف ل ف) ou « مَنْ نَقَفَ » ou « مَنْ تَنَفَّ » ? 2) « شعرا من أنفه أو من إبطه » ✓ ? 3) Le verbe après أو : « اطَّلَى جَسَدَهُ بِنُورَةٍ » ✓ ? et la parenthèse glosse « (بضم النون: أخلاط تضاف إليه من زرنيخ وغيره، يستعمل لإزالة الشعر) » exactement ? 4) La suite : « أو يحلق عن شجرة رأسه لضرورة، أو يحلق قفاه لموضع الصائم » — « قفاه » ou « قافه » ? et « لموضع الصائم » exact ? 5) « وهو محرم ناسيا أو جاهلا إن فعل شيئا من ذلك فعليه الفدية في ذلك كله ولا ينبغي له أن يحلق موضع الصائم » exactement. Ne devine pas.` },
  { tag: 'h411-maida', ask: `Zoom 900 dpi (p.151, dialogue d'Omar). Transcris TOUT le paragraphe lettre par lettre : 1) « وقد استغرب السائل من فعل عمر هذا؛ فقال: ... » — la suite exacte (« قال الرجل وهو يقول: هذا أمير المؤمنين لا يستطيع أن يحكم في ... حتى دعا رجلا يحكم معه ») ? Le mot après في : « ظبي » ou « طلِّي » ? 2) « وفي رواية الحاكم، قال: ... » exact ? 3) Le verset : « مستدلا بقوله تعالى: {يَحْكُمُ بِهِ ...} [سورة المائدة الآية: N] » — transcris le VERSE ENTIER entre accolades lettre par lettre (يحكم به ذوا عدل منكم هديا بلغ الكعبة ?) et le NUMÉRO N imprimé (95 ou 97 ou 79 ?). 4) Le dialogue « وفي الموطأ: فسمع عمر قول الرجل فدعاه فسأله: هل تقرأ/تحفظ سورة المائدة؟ قال: لا... » transcris-le ENTIER. Ne devine pas.` },
];
async function readOne(zai, t) {
  const out = `${OUTDIR}/r689c-${t.tag}.txt`;
  if (fs.existsSync(out) && fs.statSync(out).size > 150) return `${t.tag}: cache`;
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
      await new Promise(r => setTimeout(r, msg.includes('429') ? 20000 * k : 5000));
    }
  }
}
async function main() { const zai = await ZAI.create(); for (const t of TASKS) console.log(await readOne(zai, t)); }
main().catch(e => { console.error('FATAL', e); process.exit(1); });
