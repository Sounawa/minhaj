// Z2-30 — scruterins v1 (objectif 3) + v2 (كلّ أمة/الأمم) à 1200 dpi
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-25/crops';
const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

const QS = [
  ['v1-p138', `C'est la ligne du 3e objectif (أهداف الدرس) de la leçon «الحياء». Les objectifs 1-2 étaient: «1. أَنْ أَتَعَرَّفَ مَعْنَى الْحَيَاءِ وَثَمَرَتَهُ. / 2. أَنْ أُمَيِّزَ مَظَاهِرَ الْمَحْمُودِ وَالْمَذْمُومِ مِنَ الْحَيَاءِ.».
TRANSCRIS la ligne du 3e objectif AU COMPLET mot à mot avec vocalisation (elle commence par «3.» et se termine par un point). Décompose ensuite lettre par lettre (forme + points + dents) le SEGMENT ENTRE «الْمَقَاصِدَ» et «الْحَيَاءِ» — je dois savoir exactement quels mots s'y trouvent (candidats vus ailleurs : الشَّرْعِيَّةَ / عِبْرَةً / عَبْرَ / نَشْرِ / التَّشْرِيعِ / مِنْ — mais transcris ce qui est réellement imprimé).`],
  ['v2-p138', `Fragment de la 2e ligne du تمهيد : «... ضَمَّنِ الْمَحَامِدِ فِي مَأْثُورِ كُلِّ ...». TRANSCRIS le fragment mot à mot. Décompose lettre par lettre (forme + points + dents) le DERNIER mot complet visible : أُمَّةٍ (singulier : hamza+mīm shadda+ة avec tanwīn kasr sous la lettre) ou الْأُمَمِ (pluriel : alif-lām + hamza ḍamma + mīm fatha + mīm kasra) ? Compte les lettres et les points.`],
];

for (const [k, q] of QS) {
  for (let run = 1; run <= 2; run++) {
    const out = `${DIR}/vlmv-${k}-r${run}.txt`;
    if (fs.existsSync(out)) { console.log(`skip ${k} r${run}`); continue; }
    const img = fs.readFileSync(`${DIR}/${k}.png`).toString('base64');
    let done = false;
    for (let attempt = 1; attempt <= 3 && !done; attempt++) {
      try {
        const r = await zai.createChatCompletionVision({
          messages: [{ role: 'user', content: [
              { type: 'text', text: `Recadrage natif 1200 dpi, manuel scolaire marocain d'hadith (5e primaire), lecture droite→gauche. Ne complète JAMAIS par mémoire.\n\n` + q },
              { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
          ] }],
          model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1600,
        });
        const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
        fs.writeFileSync(out, txt);
        console.log(`\n==== ${k} run${run} ====`);
        console.log(txt.length > 600 ? txt.slice(0, 450) + '\n[...]' : txt);
        done = true;
      } catch (e) { console.log(`échec ${k} r${run}: ${e.message}`); await sleep(8000*attempt); }
    }
    await sleep(2000);
  }
}
