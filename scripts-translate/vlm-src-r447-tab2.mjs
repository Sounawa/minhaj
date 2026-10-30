import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const b64 = fs.readFileSync('/home/z/my-project/scripts-translate/tr-tmp/table-175-app2-full-175.png').toString('base64');
async function ask(zai, prompt) {
  const res = await zai.createChatCompletionVision({
    messages: [{ role: 'user', content: [
      { type: 'text', text: prompt },
      { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
    ]}],
    model: 'glm-5v-turbo', max_tokens: 1200,
  });
  return res.choices[0].message.content;
}
async function main() {
  const zai = await ZAI.create();
  console.log('--- lecture 1 (structure) ---');
  console.log(await ask(zai, 'Tableau de farāʾiḍ (dubl) marocain, 600 dpi. Réponds UNIQUEMENT par : (1) nombre de colonnes et leur contenu d\'en-tête (nombres de tête, ex. 3, 6, 60...) ; (2) liste des lignes : nom d\'héritier + suite de ses nombres de droite à gauche ; (3) la dernière colonne = parts finales. Aucune invention : [?] si illisible.'));
  console.log('--- lecture 2 (mots) ---');
  console.log(await ask(zai, 'Même tableau. Transcris cette fois les ÉTIQUETTES de lignes exactement (أم؟ جد؟ بنت؟ ابن؟ زوج؟ أخ؟) et pour chaque étiquette la suite EXACTE de nombres. Indique le sens de lecture des colonnes.'));
  console.log('--- lecture 3 (nombres seuls) ---');
  console.log(await ask(zai, 'Même tableau. Ignore l\'arabe : liste UNIQUEMENT tous les nombres imprimés, ligne par ligne, de droite à gauche, avec leur position (1re ligne, 2e ligne, etc.).'));
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
