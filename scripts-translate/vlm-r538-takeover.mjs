// vlm-r538-takeover.mjs — relecture image des zones clés de la leçon 4 hadith-2 (p.34/35/38)
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const shots = [
  ['r538-p34-ov.png', 'Page entière d\'un manuel scolaire arabe. Transcris VERBATIM la section « الأحاديث » (le hadith complet avec son isnād et son matn, du début « مالك عن » jusqu\'à la fin de la page). N\'invente rien : ce que tu ne lis pas, écris [?].'],
  ['r538-p35-ov.png', 'Page d\'un manuel scolaire arabe. Transcris VERBATIM, dans l\'ordre : (1) la fin du hadith avec ses paroles du Prophète ﷺ entre « » et le renvoi [الموطأ رقم: ...] ; (2) la section « ترجمة الراوي » complète ; (3) la section « الفهم » : chaque mot arabe et sa définition après le deux-points. N\'invente rien : [?] si illisible.'],
  ['r538-p38-istishhad1.png', 'Bloc de citation arabe (citation coranique + parole de ʿAlī + hadith du Prophète + renvois [السنن الكبرى للبيهقي...]). Transcris VERBATIM chaque ligne, chiffres compris. N\'invente rien : [?] si illisible.'],
  ['r538-p38-istishhad2.png', 'Bloc de citation arabe. Transcris VERBATIM chaque ligne, chiffres compris. N\'invente rien : [?] si illisible.'],
];
async function main() {
  const zai = await ZAI.create();
  for (const [f, cue] of shots) {
    const b64 = fs.readFileSync('/home/z/my-project/tr-tmp/' + f).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: 'Tu es transcripteur d\'arabe imprimé (naskh maghrébin). Aucune invention : ce que tu ne lis pas, écris [?].\nZONE : ' + cue },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
      ]}],
      model: 'glm-5v-turbo', max_tokens: 2000,
    });
    console.log('===== ' + f + ' =====');
    console.log(res.choices[0].message.content); console.log();
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
