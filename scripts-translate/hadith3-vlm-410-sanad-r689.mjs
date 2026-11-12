import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const zai = await ZAI.create();
const b64 = fs.readFileSync('/home/z/my-project/tr-tmp/qa-crops-r688/z410-8-p145-sanad.png').toString('base64');
const ask = `Zoom haute résolution du haut de la page 145 d'un manuel arabe. Le paragraphe contient « ففي الموطأ: عن عبد ... بن ... عن محمد بن سيرين أن رجلا جاء إلى عمر بن الخطاب ... نستبق إلى نقرة ... فأصبنا ظبيا ونحن محرمان ... فحكما عليه بعنز» [الموطأ رقم: 1241].

TRANSCRIPTION DEMANDÉE : transcris le hadith ENTIER (de « عن عبد » jusqu'à « بعنز » + le numéro entre crochets) lettre par lettre en arabe. SPÉCIALEMENT :
1) Le 1er nom du sanad : « عبد الله » ou « عبد الملك » ? (الله = ل ل ه avec shadda ; الملك = م ل ك)
2) Le nom après بن : « قيس » ou « قريز » ou « قيس » ? (قيس = ق ر ي س hmm non : ق + ي + س ; قريز = ق + ر + ي + ز avec ز final à 1 point)
3) Les mots de la course : « أجريت أنا وصاحب لي فرسين نستبق إلى نقرة ثنية » ? Décris chaque mot ambigu.
4) Le verdict final : « فحكما عليه بعنز » ou autre ?
Ne devine pas : décris les points et les boucles de chaque lettre contestée.`;
for (let k = 1; k <= 4; k++) {
  try {
    const res = await zai.chat.completions.createVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: ask },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
      ] }],
      thinking: { type: 'disabled' },
    });
    const txt = res.choices[0]?.message?.content || '(vide)';
    fs.writeFileSync('/home/z/my-project/tr-tmp/vlm-410/r689-z410-8-sanad1241.txt', txt, 'utf-8');
    console.log(`OK (${txt.length} car)`);
    break;
  } catch (e) {
    const msg = String(e?.message || e);
    if (k === 4) { console.error('ERREUR', msg); process.exit(1); }
    await new Promise(r => setTimeout(r, msg.includes('429') ? 20000 * k : 5000));
  }
}
