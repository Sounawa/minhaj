// Z2-27 — VLM sur zooms W ×3 : derniers points litigieux (bandeaux/cadres blancs sur fond)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-23';
const COMMON = `Recadrage ×3 (600 dpi source) d'un manuel scolaire marocain d'hadith (5e primaire), droite→gauche. Certains textes sont en BLANC sur fond décoré.
TRANSCRIS mot à mot, avec vocalisation, uniquement ce qui est imprimé. Ne complète JAMAIS par mémoire.`;

const Q = {
  W13: `Bandeau de titre. Lis : le mot الدَّرْسُ, puis le NUMÉRO en chiffres arabes orientaux imprimé dans le médaillon (٢٣ ? ٢٤ ? autre ?), puis le TITRE. Réponds STRICTEMENT au format : الدرس | numéro | titre`,
  W01: `Ligne d'objectif n°3 de أهداف الدرس, commençant par «3. أَنْ أَتَمَثَّلَ...». Transcris-la mot à mot jusqu'au point final — surtout la fin : وَالْمُحَافَظَةَ عَلَى ... ? (عَلَى الْحَسَنَة ? عَلَى أَخْلَاقِيَ ? autre ?)`,
  W02: `Glose n°2 du شرح : le mot تَمْحُهَا suivi de DEUX verbes à l'accompli. Transcris : تَمْحُهَا : تُ... آثَارَهَا وَ... — quel est le 1er verbe (تُزِيلُ ? تُذْهِبُ ? autre) et le 2e (وَتُلْغِيهَا ? وَتَمْحُوهَا ? وَإِبْطَالُهَا ? autre) ?`,
  W03: `Encadré de verset en blanc sur fond décoré. Transcris le texte vocalisé COMPLET et la référence [هود : ...]. Je crois qu'il contient وَأَقِمِ الصَّلَاةَ ... et éventuellement إِنَّ الْحَسَنَاتِ يُذْهِبْنَ السَّيِّئَاتِ — mais ne te fie pas à ma mémoire : lis l'image.`,
  W05: `Item n°2 (tiret) de وَمِمَّا يُسْتَفَادُ مِنَ الْحَدِيثِ : il commence par أَنَّهُ يُحَقِّقُ ... النَّاسَ بَعْضِهِمْ لِبَعْضٍ... Le mot après يُحَقِّقُ : تَفَاعُلَ ? تَعَاضُدَ ? تَعَاوُنَ ? autre ? Transcris l'item entier.`,
  W07: `Activité n°1 de l'استثمار : أَسْتَخْرِجُ مَا تَضَمَّنَتْهُ الْآيَاتُ مِنَ الْأَخْلَاقِ الَّتِي تُعْتَبَرُ مِنْ أَوْصَافِ ... ? Le dernier mot : الْمُتَّقِينَ ? الْمُنَافِقِينَ ? الْمُحْسِنِينَ ? Transcris l'item entier mot à mot.`,
  W09: `Item 1 de l'إعداد قبلي : «1. أَحْفَظُ حَدِيثَ الدَّرْسِ الْآتِيَ وَأَقُومُ بِمَا يَلِي:» suivi d'un EXTRAIT du hadith à mémoriser (il contient des mots comme ...تُجَاهَكَ ou ...الصُّحُفُ ou أَخْطَأَكَ...). Transcris CET EXTRAIT de hadith mot à mot, avec ses éventuelles sous-lettres a./b.`,
  W11: `Début du verset coranique de l'encadré [آل عمران] : le tout premier mot après ﴿ : سَابِقُوا ? سَارِعُوا ? Transcris la première ligne complète du verset 133.`,
  W12: `Fin du passage coranique [آل عمرan] : le verset 135 contient وَمَنْ يَغْفِرُ الذُّنُوبَ إِلَّا اللهُ ou وَمَا لِيَغْفِرَ... ? et la fin (136) : وَنِعْمَ أَجْرُ الْعَامِلِينَ ? Transcris les derniers mots imprimés + la référence [آل عمران : ...] avec les numéros EXACTS.`,
};

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
for (const t of Object.keys(Q)) {
  const out = `${DIR}/vlm23-${t}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${t}`); continue; }
  const img = fs.readFileSync(`${DIR}/z23-${t}.png`).toString('base64');
  console.log(`\n======== ${t} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q[t] },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1024,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.length > 420 ? txt.slice(0, 210) + '\n[...]' : txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${t} échec: ${e.message}`); await sleep(8000*attempt); }
  }
  await sleep(2500);
}
