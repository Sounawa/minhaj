import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
const zai = await ZAI.create();
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const OUT = '/home/z/my-project/pdf-work/h6-15/vlm-l20';
// Job 1 : boîte المائدة complète @2400 couleur — référence
const img1 = fs.readFileSync(`${DIR}/z7-p113-maidabox.png`).toString('base64');
const r1 = await zai.createChatCompletionVision({
  messages: [{ role: 'user', content: [
      { type: 'text', text: `Encadré coranique coloré d'un manuel marocain (2400 dpi) citant deux versets consécutifs de sourate المائدة : «إنما وليكم الله ورسوله والذين آمنوا الذين يقيمون الصلاة ويؤتون الزكاة وهم راكعون» puis «ومن يتول الله ورسوله والذين آمنوا فإن حزب الله هم الغالبون». QUESTION UNIQUE : la référence entre crochets [المائدة: ...] — décris les CHIFFRES imprimés chiffre par chiffre (sont-ce ٥٥-٥٦ ou ٥٧-٥٨ ou autre ?) et dis où elle se trouve (fin de 2e ligne ? en dessous ?).` },
      { type: 'image_url', image_url: { url: `data:image/png;base64,${img1}` } },
  ] }],
  model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 700,
});
console.log('########## maidabox-ref ##########\n' + (r1?.choices?.[0]?.message?.content ?? 'ERREUR'));
fs.writeFileSync(`${OUT}/p113-maidabox-ref.txt`, r1?.choices?.[0]?.message?.content ?? 'ERREUR');
// Job 2 : mot entre الواجب et التزكية
const img2 = fs.readFileSync(`${DIR}/z7-p112-qadarw.png`).toString('base64');
const r2 = await zai.createChatCompletionVision({
  messages: [{ role: 'user', content: [
      { type: 'text', text: `Fragment d'une ligne d'un manuel (4800 dpi) : «الواجب ___ التزكية والاستقامة؛ والنوافل لتحصيل...». QUESTION UNIQUE : entre «الواجب» (visible en partie à droite) et «التزكية» : y a-t-il un mot (مِنْ / فِيهِ / لِ) ou une JONCTION DIRECTE ? Décris ce qui se trouve entre ces deux mots, lettre par lettre.` },
      { type: 'image_url', image_url: { url: `data:image/png;base64,${img2}` } },
  ] }],
  model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 700,
});
console.log('\n########## qadar-gap ##########\n' + (r2?.choices?.[0]?.message?.content ?? 'ERREUR'));
fs.writeFileSync(`${OUT}/p112-qadar-gap.txt`, r2?.choices?.[0]?.message?.content ?? 'ERREUR');
