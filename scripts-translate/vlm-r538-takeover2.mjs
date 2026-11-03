// vlm-r538-takeover2.mjs — relecture haute résolution des zones clés (leçon 4 hadith-2)
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const shots = [
  ['r539-p34-hadith.png', 'Texte arabe imprimé : la section « الأحاديث » d\'un manuel (bas de page). Il commence par « مالك عن أبي حازم بن دينار عن سهل بن سعد الساعدي » et rapporte un hadith sur le Prophète ﷺ allant chez بني عمرو بن عوف, la prière dirigée par أبي بكر, les gens qui frappent des mains (التصفيق). Transcris VERBATIM tout le hadith visible ligne par ligne. N\'invente rien : [?] si illisible.'],
  ['r539-p35-top.png', 'Texte arabe : fin d\'un hadith (paroles du Prophète ﷺ : « يا أبا بكر ما منعك... » et « ما لي رأيتكم أكثرتم من التصفيق... ») puis renvoi [الموطأ رقم: ...] puis section « ترجمة الراوي ». Transcris VERBATIM ligne par ligne. N\'invente rien : [?] si illisible.'],
  ['r539-p35-bottom.png', 'Texte arabe : fin de « ترجمة الراوي » (bio de سهل بن سعد, dates 88/91) puis section « الفهم » : glossaire mot: définition (قالت الصلاة, خرق الصفوف, التصفيح, داه...). Transcris VERBATIM chaque entrée. N\'invente rien : [?] si illisible.'],
  ['r539-p38-bottom.png', 'Texte arabe : section « الاستشعار » — citations avec des guillemets « » : une parole de ʿAlī ibn Abī Ṭālib citant une āya coranique, puis un hadith du Prophète ﷺ, avec renvois [السنن الكبرى للبيهقي...]. Transcris VERBATIM ligne par ligne CHIFFRES COMPRIS. N\'invente rien : [?] si illisible.'],
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
      model: 'glm-5v-turbo', max_tokens: 2500,
    });
    console.log('===== ' + f + ' =====');
    console.log(res.choices[0].message.content); console.log();
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
