// Z2-26 — dernière vague : T3c (ref Bukhârî), T4c (يُتْقِنَ), T8b (ligne إعداد)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-22';

const COMMON = `Zoom d'une bande de ligne d'un manuel scolaire marocain d'hadith (5e année primaire), leçon 22, sens de lecture droite→gauche.
TRANSCRIS mot à mot avec la vocalisation. Pour les mots signalés, analyse LES LETTRES UNE À UNE (lettre de base, points 0/1/2/3, diacritique). Ne complète JAMAIS par mémoire : seulement ce qui est imprimé. Illisible : [؟]. Réponds : TRANSCRIPTION puis RÉPONSES.`;

const R = {
  T3c: `ZONE : fin de ligne (p.122) — une référence entre crochets [ ... ] après ».
QUESTIONS : (1) Transcris la référence complète. (2) Le premier mot : « صحيح » ou « صحيحا » (alif ou tanwīn après le ḥāʾ) ? Décris la fin du mot lettre par lettre. (3) Suite : « البخاري ومسلم » ou autre ? (4) S'il y a un point final ou autre signe, décris-le.`,
  T4c: `ZONE : fragment d'une ligne dense (p.123) — elle contient « ... ذلك ... التعذيب ... ».
QUESTIONS : (1) Transcris TOUT ce qui est visible de droite à gauche. (2) Si un verbe est visible entre « بِأَنْ » (ou un mot similaire) et « الذَّابِحُ » : LETTRE PAR LETTRE — « يُتْقِنَ » (yāʾ+tāʾ 2 points DESSUS avec sukūn+qāf 2 points DESSUS+nūn) ou « يُنْقَنَ » ou « يُقْنَ » ? Décris la 2e lettre : ses points (combien, au-dessus ou en dessous ?). (3) Transcris les mots autour du verbe.`,
  T8b: `ZONE : ligne d'instruction sous la rubrique الإعداد القبلي (p.124).
QUESTIONS : (1) Transcris la ligne complète. (2) Entre « الدَّرْسِ » et le verbe « ...جِيبُ » : y a-t-il « الْآتِيَ » ou rien ? Décris l'enchaînement exact. (3) Le verbe : « أُجِيبُ » (ḍamma sur hamza) ou « أَجِيبُ » (fatha) ? (4) Confirme « أَحْفَظُ » et « عَنِ الْآتِي: ».`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of Object.keys(R)) {
  const out = `${DIR}/z22-${k}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${k}`); continue; }
  const img = fs.readFileSync(`${DIR}/z22-${k}.png`).toString('base64');
  console.log(`\n======== ${k} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + R[k] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo',
        temperature: 0.1,
        max_tokens: 1200,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt);
      done = true;
    } catch (e) {
      console.log(`tentative ${attempt} ${k} échec: ${e.message}`);
      await sleep(8000 * attempt);
    }
  }
  if (!done) console.log(`ABANDON ${k}`);
  await sleep(3000);
}
console.log('\nFIN DE VAGUE');
