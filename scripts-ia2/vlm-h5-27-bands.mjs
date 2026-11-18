// Z2-32 — VLM bandes 1200 dpi natives, leçon 27 — questions neutres
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-27/bands';
const COMMON = `Bande pleine largeur à 1200 dpi NATIF d'un manuel scolaire marocain d'hadith (5e primaire), leçon 27, lecture droite→gauche.
TRANSCRIS TOUT ce qui est imprimé sur la bande, ligne par ligne, mot à mot, avec la vocalisation. Pour les mots signalés : décompose lettre par lettre (forme, nombre de points et place, dents) et décris les voyelles. Ne complète JAMAIS par mémoire d'un texte connu.`;

const Q = {
  'b01-p150': `L'ENCADRÉ DU HADITH (fond ornementé) : l'en-tête, le sanad complet (transcris le nom du rāwī mot à mot — la structure autour de «جَابِر», y a-t-il «قَالَ:» avant «أَنَّ رَجُلًا» ?), le matn complet (les 4 propositions de l'homme dans l'ordre exact — note [?] sur le mot de la question finale : combien de hamza avant «دْخُلُ» ? un seul أَدْخُلُ ou deux أَأَدْخُلُ ?), la réponse du Prophète et la référence.`,
  'b02-p151': `La rubrique الفهم/الشرح avec sa glose de «أَرَأَيْتَ». Transcris tout. SCRUTIN : les DEUX DERNIERS mots de la glose (après «بِمَعْنَى:») — décompose-les lettre par lettre.`,
  'b03-p151': `La ligne «وَلِبَيَانِ مَوْضُوعِ الدَّرْسِ ... عَلَى مَا يَأْتِي:». SCRUTIN : le verbe après «الدَّرْسِ» — première lettre (ن ou ت ?), voyelles ; puis le mot suivant (مَحَاوِرُهُ ou مَحَاوِرَهُ ?) — voyelle finale.`,
  'b04-p152': `Les 2 lignes de la glose de النووي : «فَسَّرَ النَّوَوِيُّ رَحِمَهُ اللهُ...». Transcris-les. SCRUTIN 1 : le mot entre «بِـ» et les guillemets «اجْتَنَبْتُهُ» — 4 lettres ? décompose-le (ا-ج-ت-ن-ب ?). SCRUTIN 2 : la ponctuation (deux-points ?) autour de «حَرَّمْتُ الْحَرَامَ» et «أَحْلَلْتُ الْحَلَالَ». SCRUTIN 3 : le dernier mot «حِلَّهُ» ou «حَلَالَهُ».`,
  'b05-p153': `La ligne «وَأَ... صَاحِبُ الْمَفْهُومِ أَنَّهُ لَمْ...». SCRUTIN : le 2e mot du verbe initial — décompose-le lettre par lettre (أَفَادَ = hamza-fāʾ-alif-dāl, ou أَقَادَ = hamza-qāf-alif-dāl ? compte les points de la 2e lettre : 0 ou 2 ?).`,
  'b06-p153': `Les lignes «وَلِذَلِكَ كَانَ الصَّحَابَةُ... يُ... عَلَى فِعْلِ السُّنَنِ... مُ... عَلَى الْفَرَائِضِ، وَلَمْ يَكُونُوا يُفَرِّقُونَ بَيْنَهُمَا فِي اغْتِنَامِ... وَتَنْمِ... الْفَرَائِضِ بِهَا...». SCRUTIN 1 : le verbe après «وَمَنْ بَعْدَهُمْ» (يُثَابِرُونَ/يُجَابِرُونَ/يَثِرُونَ ?). SCRUTIN 2 : le mot après «مُ...» (مُثَابَرَتِهِمْ/مُتَابَرَتِهِمْ ?). SCRUTIN 3 : le mot entre «فِي» et «ثَوَابِهَا» (اغْتِنَامِ/اعْتِمَادِ ?). SCRUTIN 4 : le mot entre «وَتَنْـ...» et «الْفَرَائِضِ» (تَنْمِيَةِ/تَنْمِيمِ/تَثْمِيرِ ?).`,
  'b07-p153': `Les lignes du الحاصل : «...فَلَاحٌ أَيْ فَلَاحٌ، وَضَمُّ التَّطَوُّعَاتِ إِلَيْهَا زِيَادَةٌ فِي الْفَلَاحِ يُتَقَرَّبُ بِهَا ... مَحَبَّةِ/مَحَبَّتِهِ ... وَجَبْرٌ/جَزَاءٌ لِمَا يَقَعُ...». SCRUTIN 1 : ce qui suit «بِهَا» jusqu'à «سُبْحَانَهُ» (préposition + mot + voyelles). SCRUTIN 2 : le mot après «وَ» avant «لِمَا يَقَعُ». Transcris les 2 lignes entières.`,
  'b08-p154': `La ligne de l'item 2 du يُسْتَفَاد : «الِاسْتِزَادَةُ مِنَ التَّطَوُّعَاتِ ... لِلْفَرَائِضِ وَزِيَادَةٌ فِي الدَّرَجَاتِ...». SCRUTIN : le mot entre «التَّطَوُّعَاتِ» et «لِلْفَرَائِضِ» — décompose-le lettre par lettre (تَنْمِيَةٌ/تَنْمِيمٌ/تَثْمِيمٌ/تَثْمِيرٌ ?).`,
  'b09-p154': `La ligne de la question 2 du تقويم : «أُوَضِّحُ مَا يَتَرَتَّبُ مِنَ الْ... عَلَى الْجَمْعِ...». SCRUTIN : le mot entre «مِنَ الْ» et «عَلَى الْجَمْعِ» — décompose-le lettre par lettre (فَوَائِدِ = ف-و-ا-ئ-د, ou قَوَاعِدِ = ق-و-ا-ع-د ? compte les points de la 1re et de la 4e lettre).`,
  'b10-p154': `Les lignes de l'encadré du استثمار (début) : «قَالَ الشِّبْرَخِيتِيُّ رَحِمَهُ اللهُ: وَظَاهِرُ الْحَدِيثِ يَقْتَضِي...». SCRUTIN : le dernier mot de la ligne «لِأَنَّ تَعْلِيقَ الْحُكْمِ عَلَى الْوَصْفِ يُشْعِرُ بِالْ...» — décompose-le (بِالْعِلَّةِ = ع-ل-ة, ou بِالْعِلِّيَّةِ = ع-لّ-ي-ة ?).`,
  'b11-p155': `La fin de l'encadré du استثمار : «...وَأَمَّا اخْتِلَافُ مَرَاتِبِهَا فَبِحَسَبِ الْعَمَلِ، لَكِنْ لَا بُدَّ ...» + le crochet [الفتوحات الوهبية...]. SCRUTIN : la fin de la phrase après «لَا بُدَّ» — transcris le mot ou les mots qui suivent, lettre par lettre. Puis transcris le contenu ENTIER du crochet.`,
  'b12-p155': `La rubrique du bas de page : l'en-tête et son/ses item(s). SCRUTIN : combien d'items numérotés ? Transcris-les tous mot à mot (notamment le verbe de l'item 1 : أَقْرَأُ/أُفْرِأُ et sa voyelle, et ce qui suit «نَصَّ»).`,
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
      console.log(txt.length > 600 ? txt.slice(0, 450) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${k} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(2500);
}
