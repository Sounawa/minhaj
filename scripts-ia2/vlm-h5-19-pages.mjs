// Z2-21 — hadith-5ep leçon 19 (من خصال الإيمان) — lectures VLM pages 104-110
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-19';
const pages = ['104', '105', '106', '107', '108', '109', '110'];

const ask = (p) => `Page ${p} d'un manuel scolaire marocain d'hadith (arabe, sens de lecture droite→gauche), 5ᵉ année primaire. Leçon « مِنْ خِصَالِ الْإِيمَانِ » (des qualités de la foi), quatorzième hadīth des Quarante nawawiyya, Abū Hurayra : « مَنْ كَانَ يُؤْمِنُ بِاللهِ وَالْيَوْمِ الْآخِرِ فَلْيَقُلْ خَيْرًا أَوْ لِيَصْمُتْ، وَمَنْ كَانَ يُؤْمِنُ بِاللهِ وَالْيَوْمِ الْآخِرِ فَلْيُكْرِمْ جَارَهُ، وَمَنْ كَانَ يُؤْمِنُ بِاللهِ وَالْيَوْمِ الْآخِرِ فَلْيُكْرِمْ ضَيْفَهُ » [صحيح البخاري ومسلم].

Transcris la page ENTIÈRE en arabe, fidèlement, mot à mot :
- Respecte la structure : titres de rubriques (أهداف الدرس، التمهيد، الحديث، ترجمة الراوي، الفهم، شرح المفردات، استخلاص المضامين، التحليل، أولاً/ثانياً، يُستفاد، التقويم، الاستثمار، الإعداد القبلي …), paragraphes, listes numérotées, tirets, encadrés.
- Marque chaque titre de rubrique avec [TITRE] … [/TITLE] non — [TITRE] … [/TITRE].
- Marque chaque encadré/décoration avec [CADRE] … [/CADRE].
- Ne saute AUCUNE phrase. Un mot illisible : écris [؟]. Ne devine pas au-delà de ce qui est imprimé.
- Garde la vocalisation diacritique telle qu'imprimée.
- Les références entre crochets [صحيح البخاري ومسلم]، [سنن الترمذي]، [فتح الباري، ونسبه للطبراني]، [الجامع الصغير للسيوطي]، [المعجم الكبير للطبراني]، [الإسراء: 36]، [ق: 18]، [النساء: 36]، [الذاريات: …] doivent être transcrites telles quelles, avec le numéro de verset EXACT tel qu'imprimé.
- La page 104 contient les objectifs (3), le تمهيد et le hadith encadré (bandeau «14») ; la page 105 : ترجمة الراوي (أبو هريرة «سبقت ترجمته»), الفهم وشرح المفردات (الآخِر، يَصْمُت، الصَّمْت), استخلاص المضامين et le début du التحليل ; la page 106 : l'analyse أولاً حفظ اللسان (hadith Muʿādh ibn Jabal, verset ق, حصائد الألسنة) ; la page 107 : fin du hadith de la قسوة, ثانياً إكرام الجار والضيف, آية النساء, début إكرام الجار ; la page 108 : hadith ʿĀʾisha/Jibrīl, آية, hadith «بات شبعان», 2. إكرام الضيف, citation Ibn Hubayra ; la page 109 : آية الذاريات (ضيافة إبراهيم), يُستفاد, التقويم (3 questions) ; la page 110 : الاستثمار (hadith Ibn ʿUmar زكاة, المعجم الكبير) et الإعداد القبلي.

Réponds UNIQUEMENT avec la transcription structurée, sans commentaire.`;

async function main() {
  const zai = await ZAI.create();
  for (const pg of pages) {
    const img = `${DIR}/r150/p${pg}.png`;
    const out = `${DIR}/vlm19-p-${pg}.txt`;
    if (fs.existsSync(out)) { console.log(`skip ${pg} (déjà lu)`); continue; }
    const b64 = fs.readFileSync(img).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: ask(pg) },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 4096,
        temperature: 0.1,
      });
      const txt = res?.choices?.[0]?.message?.content ?? JSON.stringify(res);
      fs.writeFileSync(out, txt);
      console.log(`OK p-${pg} (${txt.length} car)`);
    } catch (e) {
      console.error(`ÉCHEC p-${pg}: ${e.message}`);
    }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
