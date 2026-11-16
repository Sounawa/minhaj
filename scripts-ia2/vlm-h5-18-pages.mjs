// Z2-20 — hadith-5ep leçon pdf-18 (محبة الخير للناس) — lectures VLM pages 98-103
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-18';
const pages = ['098', '099', '100', '101', '102', '103'];

const ask = (p) => `Page ${p} d'un manuel scolaire marocain d'hadith (arabe, sens de lecture droite→gauche), 5ᵉ année primaire. Il s'agit de la leçon « مَحَبَّةُ الْخَيْرِ لِلنَّاس » (aimer le bien pour les gens), treizième hadīth des Quarante nawawiyya « لَا يُؤْمِنُ أَحَدُكُمْ حَتَّى يُحِبَّ لِأَخِيهِ مَا يُحِبُّ لِنَفْسِهِ ».

Transcris la page ENTIÈRE en arabe, fidèlement, mot à mot :
- Respecte la structure : titres de rubriques (أهداف الدرس، التمهيد، الحديث، ترجمة الراوي، الفهم، شرح المفردات، استخلاص المضامين، التحليل، أولاً/ثانياً/ثالثاً، التقويم، الاستثمار، يُستفاد، الإعداد القبلي …), paragraphes, listes numérotées, encadrés.
- Marque chaque titre de rubrique avec [TITRE] … [/TITRE].
- Marque chaque encadré/décoration avec [CADRE] … [/CADRE].
- Ne saute AUCUNE phrase. Un mot illisible : écris [؟]. Ne devine pas au-delà de ce qui est imprimé.
- Garde la vocalisation diacritique telle qu'imprimée.
- Les références entre crochets [صحيح مسلم]، [البخاري ومسلم]، [فتح الباري لابن رجب]… doivent être transcrites telles quelles.
- La page 98 contient les objectifs, le تمهيد et le texte du hadith encadré (bandeau «13») ; la page 99 la biographie du rapporteur (أنس بن مالك ?) ; les pages 100-101 l'analyse en trois axes ; la page 102 le texte d'استثمار et le تقويم ; la page 103 l'إعداد القبلي.

Réponds UNIQUEMENT avec la transcription structurée, sans commentaire.`;

async function main() {
  const zai = await ZAI.create();
  for (const pg of pages) {
    const img = `${DIR}/p-${pg}.png`;
    const out = `${DIR}/vlm18-p-${pg}.txt`;
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
