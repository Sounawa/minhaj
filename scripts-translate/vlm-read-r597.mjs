import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

// R597 — pdf-mut23h2q-131 (leçon 20, الحديث الفرد والمععل, p.99-103)
// Arbitrage VLM des zooms 1200 dpi : verset du fard (ق/ف après «ما»),
// verset du muʿallal, verset an-nasakh d'al-ʿIrāqī (p.103), mots critiques.
const C = '/home/z/my-project/tr-tmp/qa-crops-r597';
const qs = [
  { img: `${C}/compZ-99-r597.png`,
    ask: `Zoom 1200 dpi de la bannière-poème d'un manuel arabe (leçon 20, gros corps, vers du matn à mémoriser). Le premier vers concerne الحديث الفرد et commence par «والفردُ ما ...». Transcris mot à mot avec voyelles EXACTES, en séparant les deux hémistiches par ***. Attention critique : le mot après «ما» — indique s'il commence par ف (1 point) ou ق (2 points), et donne sa forme complète (ex: قُيِّدَ / قُيِّدَتْ / فُيِّدَتْهُ). Transcris aussi le deuxième vers (وما بعلة...). Ne traduis pas.` },
  { img: `${C}/compZ-100-r597.png`,
    ask: `Zooms 1200 dpi d'un manuel arabe : 1) le vers «والفردُ ما ... بثقة» en corps normal (شرح), 2) une glose «المعلل: مفعول من علّله بكذا إذا شغله به» (vérifie: بكذا ou بكذاء), 3) un hadith sur صفية (أولم على صفية بسويق وتمر). Transcris mot à mot chaque bande, séparées par ===. Pour le mot après «ما» dans le vers : ف (1 point) ou ق (2 points) ? Donne sa forme complète. Ne traduis pas.` },
  { img: `${C}/compZ-101-r597.png`,
    ask: `Zooms 1200 dpi d'un manuel arabe : 1) ligne avec أبو سعيد الخدري et le hadith «أمرنا رسول الله أن نقرأ بفاتحة الكتاب وما تيسر», 2) le vers «وما بعلة غموض أو خفا *** معلل عندهم قد عرفا» en corps normal. Transcris mot à mot avec voyelles, bandes séparées par ===. Ne traduis pas.` },
  { img: `${C}/compZ-103-r597.png`,
    ask: `Zooms 1200 dpi d'un manuel arabe (p.103, bloc الاستثمار) : 1) le vers d'al-ʿIrāqī «والنسخ سمّى الترمذي علّه *** فإن يرد في عمل فـ...» — transcris le verbe après «في عمل» lettre par lettre (points exacts : فَاجْتَنِ ? فَاجْتَحْ ? autre ?), 2) le début de son شرح «قال في شرح البيت: أي وسّمى الترمذي النسخ علة...». Transcris mot à mot, bandes séparées par ===. Ne traduis pas.` },
  { img: `${C}/compZ-nasakh-r597.png`,
    ask: `Zoom 1200 dpi : vers arabe du matn «والنسخ سمّى الترمذي علّه...». Transcris mot à mot avec toutes les voyettes et points diacritiques exacts. Le verbe final : donne chaque lettre. Ne traduis pas.` },
  { img: `${C}/compZ-nasakh2-r597.png`,
    ask: `Zoom 1200 dpi : suite ou شرح du vers sur النسخ/الترمذي. Transcris mot à mot avec voyettes exactes. Ne traduis pas.` },
  { img: `${C}/compZ-bayt-r597.png`,
    ask: `Zoom 1200 dpi d'un manuel arabe : le vers «قال الحافظ العراقي في ألفيته» complet. Transcris mot à mot avec voyelles et points exacts, hémistiches séparés par ***. Ne traduis pas.` },
  { img: `${C}/compZ-word-r597.png`,
    ask: `Zoom 1200 dpi très rapproché d'un mot ou groupe de mots arabes imprimés. Transcris mot à mot avec voyelles et points diacritiques exacts. Ne traduis pas.` },
  { img: `${C}/compZ-word2-r597.png`,
    ask: `Zoom 1200 dpi très rapproché d'un mot ou groupe de mots arabes imprimés. Transcris mot à mot avec voyelles et points diacritiques exacts. Ne traduis pas.` },
  { img: `${C}/compZ-heads-r597.png`,
    ask: `Zoom 1200 dpi : en-têtes/rubriques d'un manuel arabe (ex: أهداف الدرس, تمهيد, المتن, الشرح, التحليل, التقويم, الاستثمار, الإعداد القبلي). Transcris chaque ligne mot à mot, séparées par ===. Ne traduis pas.` },
  { img: `${C}/compZ-micro-r597.png`,
    ask: `Zoom 1200 dpi microscopique de lettres arabes. Transcris exactement ce que tu vois, lettre par lettre, avec les points diacritiques. Ne traduis pas.` },
  { img: `${C}/comp-100-r597.png`,
    ask: `Bandes 600 dpi d'un manuel arabe (p.100) : définitions الفرد/المعلل, analyse avec le vers du nāẓim et le hadith d'Ibn عيينة (أولم على صفية). Transcris mot à mot les bandes, séparées par ===. Ne traduis pas.` },
];

const sleep = (ms) => new Promise(r => setTimeout(r, ms));
async function main() {
  const zai = await ZAI.create();
  for (const q of qs) {
    if (!fs.existsSync(q.img)) { console.log('=== ABSENT ' + q.img.split('/').pop() + ' ==='); continue; }
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
          model: 'glm-5v-turbo', max_tokens: 1600,
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
main();
