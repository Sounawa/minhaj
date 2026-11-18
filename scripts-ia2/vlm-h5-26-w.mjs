// Z2-31 — VLM derniers scrutins (w1-w9, leçon 26) — questions neutres
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-26/crops3';
const COMMON = `Recadrage ultra-net (1200 dpi ×2) d'un manuel scolaire marocain d'hadith (5e primaire), leçon 26 «الاستقامة», lecture droite→gauche.
TRANSCRIS d'abord les mots imprimés, puis réponds au scrutin : pour le mot visé, donne CHAQUE lettre (forme, nombre de points, place des points, dents) et CHAQUE voyelle imprimée (fatḥa/kasra/ḍamma/sukūn/shadda/tanwīn), en t'arrêtant sur ce qui est réellement imprimé. Ne complète JAMAIS par mémoire.`;

const Q = {
  'w1-p144': `Le 3e objectif commence par «أَنْ أَ...». SCRUTIN : le verbe après «أَنْ». Donne sa 1re lettre et sa voyelle, sa 2e lettre, la voyelle de la 3e lettre (petit wāw au-dessus OU petit trait oblique en dessous ?), et la voyelle de la 4e lettre.`,
  'w2-p144': `Deux lignes du تمهيد. SCRUTIN 1 (ligne 1) : le mot entre «فِي الدِّينِ» et «لِمَقَاصِدِهِ» — décris sa 1re lettre, sa 2e lettre (avec ou sans shadda ?), la shadda est-elle sur la 2e ou la 3e lettre ? SCRUTIN 2 (ligne 2) : le signe de ponctuation imprimé juste après le mot «نَافِعَةٌ» (avant «أَجَابَ») : point, virgule, ou point-virgule ?`,
  'w3-p146': `Une ligne de commentaire : «... غَيْرِكَ، أَعْمَلُ عَلَيْهِ وَ... بِهِ. فَأَجَابَهُ...». SCRUTIN : le verbe entre «عَلَيْهِ وَ» et «بِهِ» — décompose-le ENTIEREMENT : chaque lettre, ses points (nombre + place), shadda éventuelle, voyelles.`,
  'w4-p146': `Fin de la citation de ʿUmar : «... وَلَمْ يَ... رَوْغَانَ ال...». SCRUTIN 1 : le verbe entre «وَلَمْ» et «رَوْغَانَ» — sa 4e lettre : combien de points et où (0, 1 au-dessus) ? SCRUTIN 2 : le dernier mot de la citation — sa 3e lettre : combien de points au-dessus (2 ou 3) ? SCRUTIN 3 : la voyelle finale de ce dernier mot.`,
  'w5-p147': `Une ligne contenant une citation entre guillemets : «...: «... بِاللهِ ثُمَّ اسْتَقِمْ»، وَلِقَوْلِهِ...». SCRUTIN : le premier mot à l'intérieur des guillemets — quelles lettres le composent AVANT «آمَنْتُ» ? Y a-t-il un qāf (2 points au-dessus) ? un fāʾ (1 point en dessous) ? un wāw ? Décris la séquence complète avec les voyelles.`,
  'w6-p147': `Une ligne de citation d'al-Wāsiṭī : «... وَبِفَقْدِهَا ... الْمَحَاسِنُ...». SCRUTIN : le verbe entre «وَبِفَقْدِهَا» et «الْمَحَاسِنُ» — décompose-le : 1re lettre (points ?), 2e lettre (points ? place ?), 3e lettre, 4e lettre, et toutes les voyelles.`,
  'w7-p147': `Fin de l'en-tête «وَمِنْ فَضَائِلِ الِاسْتِقَامَةِ وَ...:». SCRUTIN : le dernier mot avant les deux-points — décompose-le lettre par lettre : nombre de lettres, y a-t-il un alif entre le rāʾ et le tāʾ final ? Voyelles.`,
  'w8-p149': `Fin du hadith d'Anas dans l'encadré : «... وَلَا يَدْخُلُ الْجَنَّةَ حَتَّى يَأْمَنَ ...». SCRUTIN 1 : le mot après «يَأْمَنَ» — décompose-le : voyelle du rāʾ (petit wāw au-dessus ou petit trait oblique au-dessus ?), et le pronom. SCRUTIN 2 : le DERNIER mot du hadith — décompose-le lettre par lettre (lettres, points, alif médian ?).`,
  'w9-p147': `Une ligne : «فِي الْحَدِيثِ بِـ«ثُمَّ» الَّ... ... التَّرْتِيبَ». SCRUTIN 1 : le mot relatif après «بِـ«ثُمَّ»» — points de sa 3e lettre (après le lām). SCRUTIN 2 : le verbe qui suit ce mot relatif — décompose-le ENTIEREMENT : lettres, points, voyelles (notamment la 2e lettre : 0 point/1 point/3 dents sans point ?).`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const k of Object.keys(Q)) {
  const out = `${DIR}/vlm-${k}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${k}`); continue; }
  const img = fs.readFileSync(`${DIR}/${k}.png`).toString('base64');
  console.log(`\n======== ${k} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q[k] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 2000,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 600 ? txt.slice(0, 500) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(2500);
}
