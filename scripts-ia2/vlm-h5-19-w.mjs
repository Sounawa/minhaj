// Z2-21 — hadith-5ep leçon 19 — recadrages mot-niveau w-série
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-19';

const PRE = `Zoom extrême sur quelques mots d'un manuel marocain d'hadith (5e primaire), leçon 19. Les mots sont en gros. Décris chaque lettre une à une : sa FORME, son NOMBRE DE POINTS (et leur position au-dessus/dessous/dedans), et sa VOYELLE (fatha َ / damma ُ / kasra ِ / sukūn ْ / shadda ّ / tanwīn ًٌٍ). Ne devine AUCUN signe : si un point ou une voyelle est invisible ou ambigu, dis-le explicitement. Réponds en deux parties : LECTURE(s) puis ANALYSE. `;

const W = {
  w01: `MOTS : « ضَبْطُ ... رَعَايَاهُ/رَعَايَتُهُ/رَعِيَّتُهُ وَهُوَ مَسْئُولٌ عَنْهَا » (page 106, ligne 3).
ANALYSE DEMANDÉE : (1) Le mot entre « ضَبْطُ » et « رَ... » : est-ce « جَوَارِحِهِ » (jīm 1 point + wāw + alif + rāʾ) ? Puis « الَّتِي هِيَ » ou « الَّذِي هُوَ » ? Décris. (2) LE MOT CLÉ après : transcris-le. Entre le ʿayn (ع) et la fin : y a-t-il un ALIF puis UN yāʾ puis un hāʾ (رَعَايَـه) ? ou un yāʾ + shadda + yāʾ + tāʾ (رَعِيَّتُه) ? ou alif + yāʾ + tāʾ marbūṭa (رَعَايَتُهُ) ? Énumère les lettres DANS L'ORDRE avec leurs points. La lettre finale : hāʾ (ه) ou tāʾ marbūṭa (ة, 2 points) ? (3) « وَهُوَ مَسْئُولٌ عَنْهَا » — hamza de مَسْئُول sur siège de wāw ? tanwīn ḍamma sur lām ?`,
  w02: `MOTS : « عِنَايَةً خَاصَّةً تُمَكِّنُ/... تَمَاسُكَ الْمُجْتَمَعِ وَتُرَسِّخُ مَبْدَأَ التَّعَاوُنِ وَالتَّكَافُلِ وَالتَّعَايُشِ » (page 107, ligne 2 de la zone).
ANALYSE DEMANDÉE : (1) Les deux premiers mots : « عِنَايَةً » et « خَاصَّةً » (tanwīn fatha) — confirme. (2) LE VERBE qui suit : lettre à lettre. Si c'est « تُمَكِّنُ » : tāʾ (2 points, ḍamma) + mīm (ḍamma) + kāf (shadda + kasra) + nūn (ḍamma). Décris ce que tu vois RÉELLEMENT — le mot pourrait être تُحَقِّقُ / تُدَعِّمُ / تُمَكِّنُ / تَنْعَمُ / autre. (3) Le mot suivant : « تَمَاسُكَ » — tāʾ initiale présente ? voyelle du kāf final (fatha = objet, ou kasra) ? (4) « الْمُجْتَمَعِ » : voyelle du ʿayn final (kasra annexé ou fatha) ? (5) « وَتُرَسِّخُ » (tāʾ + ḍamma? + rāʾ + shadda + khāʾ 1 point + ḍamma) — décris la voyelle du tāʾ initial et la lettre finale (khāʾ avec point ou ḥāʾ sans point ?). (6) « مَبْدَأَ » — hamza finale ? (7) « وَالتَّعَايُشِ » — dernier mot de la zone ?`,
  w03: `MOTS : « بِمَا فَتَحَ اللهُ [لَهُ ?] مِنْ غَيْرِ كُلْفَةٍ » (page 109, ligne 4 de la citation d'Ibn Hubayra).
ANALYSE DEMANDÉE : (1) Après « اللهُ » (le mot الله en écriture noble), y a-t-il un mot « لَهُ » (lām + hāʾ avec ḍamma) AVANT « مِنْ » ? Compte les mots entre الله et من. (2) « بِمَا » — bāʾ avec kasra + mīm + alif. (3) « فَتَحَ » — fāʾ 1 point + tāʾ 2 points + ḥāʾ sans point + fatha. (4) « مِنْ غَيْرِ كُلْفَةٍ » — ġayn 1 point + yāʾ ; kāf + lām + fāʾ 1 point + tāʾ marbūṭa avec tanwīn kasra. Décris tout.`,
  w04: `MOTS : « حَثَّ/حَثُّ الْإِسْلَامَ/الْإِسْلَامِ/الْإِسْلَامُ عَلَى الْجُودِ » (page 109, item 3 de يُستفاد).
ANALYSE DEMANDÉE : (1) Le premier mot : ḥāʾ (sans point) + thāʾ (3 points) + shadda. QUELLE EST LA VOYELLE immédiatement APRÈS la shadda du thāʾ : FATHA (→ حَثَّ, verbe) ou ḌAMMA/ḌAMMATAYN (→ حَثُّ, nom) ? Regarde bien le signe au-dessus/en-dessous du thāʾ. (2) Le mot suivant : الْإِسْلَام — voyelle du mīm final : FATHA (الْإِسْلَامَ, objet) ou KASRA (الْإِسْلَامِ, annexé) ou ḌAMMA (الْإِسْلَامُ, sujet) ? (3) « عَلَى » — ʿayn + lām + alif maqṣūrā. (4) « الْجُودِ » — jīm avec point INTÉRIEUR + wāw + dāl, kasratayn ou kasra ?`,
  w05: `LIGNE : la question 2 du التقويم (page 109) : « 2. أَذْكُرُ/أَذْكُرْ/اذْكُرْ ... الْإِحْسَانِ إِلَى الْجِيرَانِ. »
ANALYSE DEMANDÉE : (1) Le verbe initial : y a-t-il une hamza-alif initiale (أَذْكُرُ/أَذْكُرْ) ou pas d'alif (اذْكُرْ) ? Voyelle du dhāl (ḍamma) ? Voyelle du rāʾ final : ḌAMMA (أَذْكُرُ, indicatif), SUKŪN (اذْكُرْ, impératif) ou KASRA ? (2) Le mot après : « نَوْعَيْنِ » (nūn + wāw + ʿayn + yāʾ + nūn + kasratayn) — confirme. (3) Y a-t-il un mot « أَسَاسِيَّيْنِ » (alif + sīn + alif + sīn + shadda + yāʾ + nūn) entre نَوْعَيْنِ et مِنْ ? Si oui décris-le ; si non, dis-le. (4) « مِنْ أَنْوَاعِ الْإِحْسَانِ » ou « مِنَ الْأَنْوَاعِ الْإِحْسَانِ » ? (5) Le dernier mot : « الْجِيرَانِ » — jīm + yāʾ (2 points dessous) + rāʾ + alif + nūn ? (6) Transcris la question complète.`,
  w06: `MOTS : « وَهَلْ يَكُبُّ/يُكَبُّ النَّاسَ فِي النَّارِ » (page 107, citation Tirmidhī).
ANALYSE DEMANDÉE : (1) Le verbe après « وَهَلْ » : trois lettres yāʾ + kāf + bāʾ avec shadda. Quelle est la voyelle SUR LE YĀʾ INITIAL : FATHA (يَكُبُّ, actif) ou ḌAMMA (يُكَبُّ, passif) ? Le signe au-dessus du yāʾ : trait oblique (fatha) ou petite boucle-wāw (ḍamma) ? (2) Voyelle du kāf : ḍamma ? (3) « النَّاسَ » — shadda sur le sīn, fatha finale. (4) « فِي النَّارِ » — fāʾ + kasra + yāʾ ; nūn + alif + rāʾ + kasra. Décris.`,
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
