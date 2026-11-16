// Z2-21 — hadith-5ep leçon 19 — derniers zooms w02b/w07/w08
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-19';

const PRE = `Zoom sur une ligne d'un manuel marocain d'hadith (5e primaire). Transcris STRICTEMENT lettre à lettre avec les diacritiques. Pour chaque mot contesté, décris les lettres (forme + nombre de points) et les voyelles. Si un signe est invisible, dis-le. Réponds : TRANSCRIPTION puis RÉPONSES. `;

const W = {
  w02b: `ZONE : la ligne complète qui commence par « عِنَايَةً خَاصَّةً ... » (page 107) et continue jusqu'à « وَالتَّعَايُشِ » ou la fin de ligne. La ligne précédente se termine par « ...بِالْجَارِ ».
QUESTIONS : (1) Transcris la ligne ENTIÈRE mot à mot. (2) Le 3e mot (le verbe après « خَاصَّةً ») : décris ses lettres une à une avec leurs points et voyelles — est-ce « تُمَكِّنُ » (tāʾ 2 pts + mīm + kāf + nūn) ou « تُحَقِّقُ » ou « تُدَعِّمُ » ou « تُقَوِّي » ou autre ? (3) Le mot suivant : « تَمَاسُكَ » ou « تَمَاسُكِ » — voyelle du kāf final ? Y a-t-il un tāʾ initial ? (4) « الْمُجْتَمَعِ » — kasra finale ? (5) Le verbe suivant : « وَتُرَسِّخُ » — voyelle du tāʾ ? (6) « مَبْدَأَ » ou « مَبْدَا » ? (7) La ligne se termine par quoi exactement (« وَالتَّعَايُشِ. » ? autre chose ?)`,
  w07: `ZONE : les deux mots « حَثَّ/حَثُّ » + « الْإِسْلَامَ/ِ/ُ » (page 109, item 3), très agrandis (x5).
QUESTIONS : (1) « حَثَّ » : le thāʾ porte une shadda. JUSTE APRÈS la shadda (au-dessus du thāʾ ou à côté), y a-t-il UN SEUL signe ou DEUX ? Décris la forme : trait oblique (fatha) ? boucle ronde (ḍamma) ? deux boucles (ḍammatayn) ? cercle (sukūn) ? La voyelle du ḥāʾ initial : fatha ? (2) « الْإِسْلَام... » : la voyelle finale sur le mīm : trait oblique au-dessus (fatha) ? boucle au-dessus (ḍamma) ? trait en dessous (kasra) ? Décris précisément. (3) Le mot qui suit : « عَلَى » — confirme. (4) « الْجُودِ » ou « الْجُودَ » — voyelle du dāl final ?`,
  w08: `ZONE : la question 2 du التقويم (page 109), ligne complète : « 2. ... الْإِحْسَانِ إِلَى الْجِيرَانِ. »
QUESTIONS : (1) Le verbe initial : « أَذْكُرُ » ou « أَذْكُرْ » ou « اذْكُرْ » ? Y a-t-il un alif initial ? Voyelle du rāʾ final : ḍamma (boucle) ou sukūn (cercle) ou kasra (trait dessous) ? (2) « نَوْعَيْنِ » ou « نُوعَيْنِ » — voyelle du nūn initial ? (3) Entre « نَوْعَيْنِ » et « مِنْ » : y a-t-il un mot « أَسَاسِيَّيْنِ » (avec shadda sur le sīn et yāʾ) ? Si OUI transcris-le ; si NON dis-le clairement. (4) « مِنْ أَنْوَاعِ » ou « مِنَ الْأَنْوَاعِ » ? (5) Le dernier mot : « الْجِيرَانِ » — jīm + yāʾ (2 points dessous) + rāʾ + alif + nūn — confirme. (6) Transcris la question complète.`,
};

async function main() {
  const zai = await ZAI.create();
  for (const tag of Object.keys(W)) {
    const img = `${DIR}/z-${tag}.png`;
    const out = `${DIR}/z-${tag}.txt`;
    if (fs.existsSync(out)) { console.log(`skip ${tag}`); continue; }
    const b64 = fs.readFileSync(img).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
          { type: 'text', text: PRE + W[tag] },
          { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 2500,
        temperature: 0.1,
      });
      const txt = res?.choices?.[0]?.message?.content ?? JSON.stringify(res);
      fs.writeFileSync(out, txt);
      console.log(`OK ${tag} (${txt.length} car)`);
    } catch (e) {
      console.error(`ÉCHEC ${tag}: ${e.message}`);
    }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
