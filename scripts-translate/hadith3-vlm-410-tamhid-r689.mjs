import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const zai = await ZAI.create();
const b64 = fs.readFileSync('/home/z/my-project/tr-tmp/qa-crops-r688/z410-9-p141-tamhid.png').toString('base64');
const ask = `Zoom haute résolution du paragraphe تمهيد (page 141) d'un manuel arabe. Le paragraphe commence par « حرم الشرع على المحرم بحج أو عمرة فعل كثير من الأمور ».

TRANSCRIS le paragraphe ENTIER lettre par lettre. QUESTION CRUCIALE : au milieu, après « ومن ذلك », le verbe est-il :
- « فَتَّلَ الحيوانات بألوانها » (fat-tala avec ت+shadda, et بألوانها = بأ-ل-و-ا-ن-ها) 
- ou « قَتَلَ الحيوانات بمختلف أنواعها » (qatala, et بمختلف أنواعها) ?
Décris : 1) la 1re lettre du verbe (ف avec 1 point dessus, ou ق avec 2 points dessus), 2) le mot qui suit الحيوانات : بألوانها (أ-ل-و-ا-ن) ou بمختلف (م-خ-ت-ل-ف avec خ à 1 point dessus)? Ne devine pas.`;
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
    fs.writeFileSync('/home/z/my-project/tr-tmp/vlm-410/r689-z410-9-tamhid.txt', txt, 'utf-8');
    console.log(`OK (${txt.length} car)`);
    process.exit(0);
  } catch (e) {
    const msg = String(e?.message || e);
    if (k === 4) { console.error('ERREUR', msg); process.exit(1); }
    await new Promise(r => setTimeout(r, msg.includes('429') ? 20000 * k : 5000));
  }
}
