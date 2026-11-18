// Z2-31 — VLM scrutins RÉDO (bandes corrigées, leçon 26)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-26/crops2';
const COMMON = `Recadrage NATIF 1200 dpi d'une ou deux lignes d'un manuel scolaire marocain d'hadith (5e primaire), leçon 26 «الاستقامة», lecture droite→gauche. La ligne est ENTIÈRE.
TRANSCRIS la ligne entière mot à mot avec la vocalisation. Puis pour les mots signalés : décompose lettre par lettre (forme, NOMBRE DE POINTS et place, dents) et décris les VOYELLES imprimées. Ne complète JAMAIS par mémoire d'un texte connu : si un mot est ambigu, dis-le et décris ce qui est imprimé.`;

const Q = {
  'u02r-p144': `Ligne du تمهيد commençant par «كُلَّمَا...». Transcris-la. SCRUTIN : le mot entre «فِي الدِّينِ» et «لِمَقَاصِدِهِ» — décompose-le lettre par lettre : shadda présente ? sur quelle lettre ? quelles voyelles ?`,
  'u02b-p144': `Ligne du تمهيد «... أَوْ طُلِبَتْ مِنْهُ وَصِيَّةٌ ...». Transcris-la. SCRUTIN : la ponctuation imprimée après le mot «نَافِعَةٌ» (point . / virgule ، / point-virgule ؛ ?) et le mot suivant.`,
  'u04r-p144': `Le sanad de l'encadré du hadith (ligne sur fond ornementé : «عَنْ أَبِي عَمْرٍو...»). Transcris-le mot à mot. SCRUTIN : le mot entre «وَقِيلَ:» et «سُفْيَانُ» — décompose-le lettre par lettre avec les voyelles du bāʾ initial et du ʿayn. Y a-t-il un ethnique entre «عَبْدِ اللهِ» et «رَضِيَ» ?`,
  'u05r-p146': `La ligne «... أَعْمَلُ عَلَيْهِ وَ... بِهِ. فَأَجَابَهُ...». Transcris-la. SCRUTIN : le verbe entre «عَلَيْهِ وَ» et «بِهِ» — décompose-le lettre par lettre : forme, points (nombre + place), shadda, voyelles. Décris aussi la 3e lettre du mot «وَمَعْنَى» s'il est visible.`,
  'u06r-p146': `La ligne «وَهَذَا مِنْ جَوَامِعِ الْكَلِمِ ...». Transcris-la. SCRUTIN : le mot relatif entre «الْكَلِمِ» et le mot suivant — décompose-le lettre par lettre en comptant les points de la lettre après le lām (1 point = dhāl, 2 points = tāʾ, 3 points = thāʾ).`,
  'u08r-p146': `La citation de ʿUmar ibn al-Khaṭṭāb : «اسْتَقَامُوا وَاللهِ عَلَى طَاعَتِهِ وَلَمْ...». Transcris-la ENTIÈRE. SCRUTIN 1 : le verbe entre «وَلَمْ» et «رَوْغَانَ» — décompose-le lettre par lettre, compte les points de la 3e lettre. SCRUTIN 2 : le DERNIER mot — décompose-le lettre par lettre, compte les points de la 3e lettre (2 ou 3 ?).`,
  'u09r-p147': `La ligne «... لِقَوْلِهِ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ: «...»، وَلِقَوْلِهِ عَزَّ وَجَلَّ...». Transcris-la. SCRUTIN : le premier mot à l'intérieur des guillemets — y a-t-il un fāʾ ou un wāw avant lui ? Décompose la séquence entre guillemets et «آمَنْتُ» lettre par lettre.`,
  'u11r-p147': `La citation d'al-Wāsiṭī (fin) : «... وَبِفَقْدِهَا ... الْمَحَاسِنُ، وَاللهُ أَعْلَمُ». Transcris la ligne. SCRUTIN : le verbe entre «وَبِفَقْدِهَا» et «الْمَحَاسِنُ» — décompose-le lettre par lettre : nombre de lettres, points de la 3e lettre (0 = dāl, 1 dessous = bāʾ), voyelles.`,
  'u12r-p147': `La ligne d'en-tête «وَمِنْ فَضَائِلِ الِاسْتِقَامَةِ وَ...». Transcris-la. SCRUTIN : le DERNIER mot — décompose-le lettre par lettre : y a-t-il un alif entre le rāʾ et le tāʾ ? Combien de lettres ?`,
  'u13r-p147': `Le premier item en tiret des ثمرات («كَثْرَةُ...»). Transcris-le. SCRUTIN 1 : le mot entre «وَالْمَوْتِ» et «الْمُسْتَقِيمِينَ» — points de sa 2e lettre, shadda, voyelles. SCRUTIN 2 : ce qui suit «الْمُسْتَقِيمِينَ» — un mot ou deux ? décompose-le(s). SCRUTIN 3 : la voyelle du tāʾ du premier mot «كَثْرَةُ».`,
  'u15r-p148': `Le 3e item en tiret («الِاسْتِقَامَةُ تَكُونُ كَمَا أَمَرَنَا اللهُ تَعَالَى، لَا كَمَا...»). Transcris-le. SCRUTIN : le mot après «لَا كَمَا» — première lettre (points ? place ?), voyelles ; puis le mot suivant (حسب) — voyelle du sīn.`,
  'u16r-p149': `La fin du hadith d'Anas dans l'encadré («... حَتَّى يَسْتَقِيمَ لِسَانُهُ، وَلَا يَدْخُلُ الْجَنَّةَ...») et la référence. Transcris tout. SCRUTIN 1 : le mot «جَار...» — voyelle du rāʾ (ḍamma ou fatḥa). SCRUTIN 2 : le DERNIER mot avant les guillemets fermants — décomposition lettre par lettre (nombre de lettres, alif médian, points).`,
  'u17r-p149': `L'activité 3 avec sa citation entre guillemets. Transcris tout. SCRUTIN : dans la citation, le mot «جَار...» (voyelle du rāʾ) et le dernier mot (décomposition lettre par lettre).`,
  'u18r-p147': `La ligne «فِي الْحَدِيثِ بِـ«ثُمَّ» الَّتِي... التَّرْتِيبَ؛ فَالِاسْتِقَامَةُ...». Transcris-la. SCRUTIN : le mot relatif après les guillemets — points de sa 4e lettre ; puis le verbe suivant — décris sa 2e lettre (points) et sa 4e lettre (points), et les voyelles.`,
  'v0-p148': `La ligne d'introduction avant la citation coranique encadrée. Transcris-la mot à mot avec la vocalisation (notamment le dernier mot).`,
  'v1-p148': `Première ligne de la citation coranique encadrée (fond ornementé). Transcris TOUT mot à mot avec la vocalisation. Ne complète pas par mémoire : uniquement les mots imprimés.`,
  'v2-p148': `Deuxième ligne de la citation coranique encadrée. Transcris TOUT mot à mot avec la vocalisation et le numéro de verset dans son médaillon s'il est visible (décompose-le chiffre par chiffre).`,
  'v3-p148': `Troisième ligne de la citation coranique encadrée. Transcris TOUT mot à mot avec la vocalisation et le numéro de verset dans son médaillon s'il est visible.`,
  'v4-p148': `Quatrième ligne de la citation coranique encadrée. Transcris TOUT mot à mot avec la vocalisation et le numéro de verset dans son médaillon s'il est visible.`,
  'v5-p148': `Cinquième ligne de la citation coranique + la référence entre crochets. Transcris TOUT mot à mot avec la vocalisation, le numéro de verset, et la référence finale (sourate + numéros, chiffre par chiffre).`,
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 2200,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 500 ? txt.slice(0, 400) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(2500);
}
