// vlm-src-r447-tight.mjs — lecture serrée : énoncé + table de l'application 2 (600 dpi)
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const shots = [
  ['line-175-enonce-175.png', 'UNE SEULE LIGNE de texte arabe (énoncé d\'un exercice de farāʾiḍ). Transcris-la mot à mot, avec les tanwīn.'],
  ['table-175-app2-175.png', 'Le TABLEAU (dubl) de répartition d\'un exercice de farāʾiḍ. Structure : colonnes = فريضة الإنكار puis فريضة إقرار الأم puis فريضة إقرار الجد puis النصيب. Transcris chaque ligne : nom d\'héritier (أم، جد، بنت، ابن...) + ses nombres exacts (chiffres occidentaux), colonne par colonne de droite à gauche. Donne aussi les nombres de tête (المن، الفريضة) au-dessus des colonnes si visibles.'],
];
async function main() {
  const zai = await ZAI.create();
  for (const [f, cue] of shots) {
    const b64 = fs.readFileSync('/home/z/my-project/scripts-translate/tr-tmp/' + f).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: 'Tu es transcripteur d\'arabe imprimé (naskh maghrébin). Aucune invention : ce que tu ne lis pas, écris [?].\nZONE : ' + cue },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
      ]}],
      model: 'glm-5v-turbo', max_tokens: 1500,
    });
    console.log('===== ' + f + ' =====');
    console.log(res.choices[0].message.content); console.log();
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
