// Z2-22 — hadith-5ep leçon pdf-20 (دعم وتطبيق, consolidation leçons 15-19) — lectures VLM pages 111-113
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-20';
const pages = [111, 112, 113];

const ask = (p) => `Page ${p} d'un manuel scolaire marocain d'hadith (arabe, sens de lecture droite→gauche), 5ᵉ année primaire. Il s'agit de la leçon « دَعْمٌ وَتَطْبِيقٌ » (consolidation et application), leçon de synthèse après les leçons 15-19 (الدعاء، الورع، ترك ما لا يعني، محبة الخير للناس، خصال الإيمان). Le texte compose un paragraphe sur l'homme sociable par nature (الإنسان اجتماعي بطبعه), la āya des Hujurāt 13, l'amour du bien pour les frères, puis des exercices (الفهم، التحليل، التطبيق، الإعداد القبلي).

Transcris la page ENTIÈRE en arabe, fidèlement, mot à mot :
- Respecte la structure : titres de rubriques (أهداف الدرس، النص، الفهم، التحليل، التطبيق، الإعداد القبلي …), paragraphes, listes numérotées (1. 2. 3. أ ب ج), encadrés, pupitres d'exercices.
- Marque chaque titre de rubrique avec [TITRE] … [/TITRE].
- Marque chaque encadré/décoration avec [CADRE] … [/CADRE].
- Ne saute AUCUNE phrase. Un mot illisible : écris [؟]. Ne devine pas au-delà de ce qui est imprimé.
- Garde la vocalisation diacritique telle qu'imprimée.
- Les références entre crochets [الحجرات: 13]، [القلم: 4]، [صحيح البخاري]… doivent être transcrites telles quelles.
- La page 111 contient les objectifs et le texte composé (nass) ; la page 112 les exercices de compréhension/analyse (dont la mention d'أم المؤمنين خديجة) ; la page 113 la fin de l'analyse, le التطبيق et l'إعداد القبلي (leçon suivante : النهي عن الغضب).

Réponds UNIQUEMENT avec la transcription structurée, sans commentaire.`;

async function main() {
  const zai = await ZAI.create();
  for (const pg of pages) {
    const img = `${DIR}/r150/p${pg}.png`;
    const out = `${DIR}/vlm20-p-${pg}.txt`;
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
      console.log(`OK p${pg} (${txt.length} car)`);
    } catch (e) {
      console.error(`ÉCHEC p${pg}: ${e.message}`);
    }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
