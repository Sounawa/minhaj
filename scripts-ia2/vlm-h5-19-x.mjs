import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-19';
const Q = {
  x01: `Micro-zoom sur l'en-tête de section (page 104, avant le paragraphe qui commence par « للإيمان بالله... »). Quel est EXACTEMENT cet en-tête : « تَمْهِيد » ou « تَهْيِئَة » ou autre ? Décris les lettres : combien de syllabes, y a-t-il un hāʾ médial (تـهـ) ou un mīm (تـمـ) ? Transcris aussi la première ligne du paragraphe qui suit.`,
  x02: `Micro-zoom sur l'en-tête de l'encadré du hadith (page 104). Quel est EXACTEMENT cet en-tête : « الْحَدِيثُ » ou autre ? Transcris aussi l'isnād visible : « عَنْ أَبِي هُرَيْرَةَ رَضِيَ اللهُ عَنْهُ أَنَّ رَسُولَ اللهِ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ قَالَ » et le début du matn.`,
};
const zai = await ZAI.create();
for (const tag of Object.keys(Q)) {
  const out = `${DIR}/z-${tag}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${tag}`); continue; }
  const b64 = fs.readFileSync(`${DIR}/z-${tag}.png`).toString('base64');
  const res = await zai.createChatCompletionVision({
    messages: [{ role: 'user', content: [
      { type: 'text', text: Q[tag] },
      { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
    ] }],
    model: 'glm-5v-turbo', max_tokens: 1200, temperature: 0.1,
  });
  fs.writeFileSync(out, res?.choices?.[0]?.message?.content ?? JSON.stringify(res));
  console.log(`OK ${tag}`);
}
