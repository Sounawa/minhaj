// vlm-src-r447-320.mjs — passe image 300 dpi : transcription certifiante des p.173-176 faraid-2 (leçon 320)
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const pages = [173, 174, 175, 176].map(n => `/home/z/my-project/scripts-translate/tr-tmp/faraid2-p-${n}.png`);

const prompt = `Tu es transcripteur expert d'un manuel marocain de farāʾiḍ (science des parts) en arabe, éducation traditionnelle secondaire. Voici une page numérisée à 300 dpi. Transcris fidèlement et intégralement, en arabe, avec les voyelles telles qu'imprimées quand elles sont visibles :
1) Le corps du texte (paragraphes complets).
2) TOUT tableau (dubl) de répartition : donne-le ligne par ligne en structure claire — chaque ligne = nom de l'héritier (أم، أخ، أخت، بنت، ابن، جد، زوج...) suivi de SES nombres exactement dans l'ordre des colonnes (فريضة الإنكار / فريضة الإقرار / النصيب النهائي etc. — indique l'en-tête des colonnes si visible, sinon liste les valeurs).
3) Toute citation du matn (entre guillemets ﴿...﴾ ou «...») : transcris-la lettre par lettre avec les voyelles.
4) Les numéros d'exercices/activités et leurs énoncés complets.
Si une zone est illisible, écris [illisibile] plutôt que d'inventer. Réponds uniquement par la transcription structurée.`;

async function main() {
  const zai = await ZAI.create();
  for (const p of pages) {
    const b64 = fs.readFileSync(p).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{
        role: 'user',
        content: [
          { type: 'text', text: prompt },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ],
      }],
      model: 'glm-5v-turbo',
      max_tokens: 3000,
    });
    console.log('===== PAGE ' + p.split('-').pop().replace('.png','') + ' =====');
    console.log(res.choices[0].message.content);
    console.log();
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
