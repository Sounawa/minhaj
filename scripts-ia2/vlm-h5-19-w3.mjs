// Z2-21 — hadith-5ep leçon 19 — zooms finaux w09-w11
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-19';

const PRE = `Zoom extrême sur un ou deux mots d'un manuel marocain d'hadith. Décris chaque lettre : forme + nombre de points + voyelle. Ne devine aucun signe. Réponds : TRANSCRIPTION puis ANALYSE. `;

const W = {
  w09: `MOTS : le mot situé entre « خَاصَّةً » et « تَمَاسُكَ » (page 107). Contexte : « عِنَايَةً خَاصَّةً [CE MOT] تَمَاسُكَ الْمُجْتَمَعِ ».
ANALYSE : (1) Combien de lettres ? (2) Première lettre : tāʾ (2 points dessus) ou bāʾ (1 point dessous) ou autre ? Sa voyelle ? (3) Deuxième lettre : nūn (1 point dessus) ou thāʾ (3 points) ou autre ? (4) Troisième lettre : mīm ? kāf ? (5) Quatrième lettre : yāʾ (2 points dessous) ou rāʾ (0 point) ou autre ? (6) Y a-t-il une shadda quelque part ? (7) Le mot complet le plus probable : تُنَمِّي / تُثَمِّرُ / تُمَكِّنُ / تُرَسِّخُ / autre ?`,
  w10: `MOTS : le début de la question 2 du التقويم : « [VERBE] نَوْعَيْنِ ... » (page 109).
ANALYSE : (1) Le verbe : y a-t-il un alif (avec hamza) initial ? Lettres : dhāl (1 point dessus) + kāf + rāʾ. Voyelle du dhāl (ḍamma ?). Voyelle du rāʾ final : ḌAMMA (boucle ronde) / SUKŪN (petit cercle) / KASRA (trait dessous) ? Décris le signe précisément. (2) Le mot suivant : نَوْعَيْنِ — voyelle du nūn initial (fatha ou ḍamma) ? yāʾ avec 2 points dessous ? nūn final avec kasra ou kasratayn ? (3) Y a-t-il un wāw entre ʿayn et yāʾ (نَوْـعَـيْنِ) ?`,
  w11: `MOTS : le milieu de la question 2 du التقويم : « ... نَوْعَيْنِ [MOT] مِنْ أَنْوَاعِ الْإِحْسَانِ ... » (page 109). Le mot entre نوعين et مِنْ.
ANALYSE : (1) Ce mot existe-t-il ? Combien de lettres ? (2) Commence-t-il par alif-hamza (أَ) ou par l'article ال ? (3) Lettres : sīn ? (0 point, 3 dents) — combien de sīn ? shadda sur le premier sīn ? (4) Y a-t-il yāʾ + shadda + yāʾ (ـسِيَّـ) au milieu ? (5) La fin : yāʾ + nūn (ـيَّيْنِ) avec kasratayn ? (6) Le mot le plus probable : أَسَاسِيَّيْنِ (alif-hamza + sīn + alif + sīn + yāʾ shadda + yāʾ + nūn) ou السَّاسِيَّيْنِ (article + sīn shadda + alif + sīn...) ou autre ? (7) Le mot suivant : مِنْ puis أَنْوَاعِ — y a-t-il un article ال devant أَنْوَاعِ ?`,
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
        max_tokens: 2200,
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
