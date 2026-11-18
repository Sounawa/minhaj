// Z2-30 — scruterins FINAUX sur les 2 occurrences du mot (crops corrigés 1200 dpi)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-25/crops';
const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

const QS = [
  ['x1-p140', `Fin de la phrase ثانيهما : «... مَنْ لَمْ يَكُنْ عِنْدَهُ حَيَاءٌ فَعَلَ كُلَّ مَا ...». Le fragment montre la fin de ligne avec le DERNIER mot (الْمُشَبَّه: يُسْتَ...).
TRANSCRIS le mot mot à mot puis décompose-le lettre par lettre avec pour CHAQUE lettre : sa forme, son NOMBRE EXACT DE POINTS (0/1/2/3, au-dessus ou en-dessous), son nombre de dents.
SCRUTIN SPÉCIFIQUE de la 3e lettre du mot (après يُـسْـتَـ) : s'agit-il de ت (2 points au-dessus), ذ (1 point au-dessus), ن (1 point au-dessus, bol médian), ق (2 points au-dessus, tête ronde) ou د (0 point) ? Compte les points visibles.`],
  ['x2b-p139', `Fin de la glose du الشرح : «... مَنْ لَمْ يَكُنْ عِنْدَهُ حَيَاءٌ فَعَلَ كُلَّ مَا ...» + la ligne suivante. Le fragment montre la fin de la glose avec le DERNIER mot (الْمُشَبَّه: يُسْتَ...).
TRANSCRIS le mot mot à mot puis décompose-le lettre par lettre (forme + points + dents). MÊME SCRUTIN : 3e lettre du mot = ت / ذ / ن / ق / د ? Compte les points.`],
];

for (const [k, q] of QS) {
  for (let run = 1; run <= 2; run++) {
    const out = `${DIR}/vlmx-${k}-r${run}.txt`;
    if (fs.existsSync(out)) { console.log(`skip ${k} r${run}`); continue; }
    const img = fs.readFileSync(`${DIR}/${k}.png`).toString('base64');
    let done = false;
    for (let attempt = 1; attempt <= 3 && !done; attempt++) {
      try {
        const r = await zai.createChatCompletionVision({
          messages: [{ role: 'user', content: [
              { type: 'text', text: `Recadrage natif 1200 dpi, manuel scolaire marocain d'hadith, lecture droite→gauche. Ne complète JAMAIS par mémoire d'un texte connu.\n\n` + q },
              { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
          ] }],
          model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1600,
        });
        const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
        fs.writeFileSync(out, txt);
        console.log(`\n==== ${k} run${run} ====`);
        console.log(txt.length > 500 ? txt.slice(0, 400) + '\n[...]' : txt);
        done = true;
      } catch (e) { console.log(`échec ${k} r${run}: ${e.message}`); await sleep(8000*attempt); }
    }
    await sleep(2000);
  }
}
