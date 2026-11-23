// IA-2 — vlm4-h6-18.mjs : ronde VLM 4 — segments précis (dernier kilomètre).
import ZAI from '/home/z/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const zai = await ZAI.create();

const PRE = `Tu lis un crop très haute résolution (3600 dpi) du manuel marocain officiel de hadith (document public, projet de transcription académique). Transcris l'arabe EXACTEMENT tel qu'imprimé (vocalisation + ponctuation). ÉPELLE les mots douteux lettre par lettre avec leurs points. Ne récite jamais de mémoire : uniquement ce qui est imprimé. Réponds en arabe.`;

const QS = [
  ["z8-item4-seg", `Segment central d'une ligne (le début de la ligne complète est : «4- عَوْنُ الْمُسْلِمِ لِأَخِيهِ؛ وَذَلِكَ بِأَنْ...» et la suite : «...مِنَ الْمُسَاعَدَةِ إِذَا احْتَاجَ إِلَيْهِ»). Transcris CE segment mot par mot avec vocalisation. ÉPELLE le mot ou les mots entre «بأن» et «بما» (s'ils sont dans ce segment).`],
  ["z8-item4-start", `Début (droite) de la ligne : «4- عَوْنُ الْمُسْلِمِ لِأَخِيهِ؛ وَذَلِكَ بِأَنْ...». Transcris ce début tel qu'imprimé, mot par mot.`],
  ["z8-manas-seg", `Début (droite) d'une ligne qui poursuit la phrase : «...أَنَّ مَنْ أَخَّرَ عَمَلَهُ [?] أَوْ تَفْرِيطًا وَتَقْصِيرًا لَا يَتَقَدَّمَ بِهِ نَسَبُهُ...». Transcris les 3-5 premiers mots de ce segment. ÉPELLE le premier mot complet lettre par lettre avec ses points et sa vocalisation (التَّسْوِيفِ ? تَسْوِيفًا ? autre ?).`],
  ["z8-aya1-right", `Moitié DROITE (début) d'un verset coranique imprimé dans un encadré orné. Transcris-la mot par mot TELLE QU'IMPRIMÉE (ne corrige pas depuis ta mémoire du Coran).`],
  ["z8-aya1-left", `Moitié GAUCHE (fin) du même verset coranique. Transcris-la mot par mot telle qu'imprimée.`],
  ["z8-aya2-right", `Moitié DROITE (début) de la 2e ligne du verset coranique de l'encadré. Transcris-la mot par mot telle qu'imprimée.`],
  ["z8-aya2-left", `Moitié GAUCHE (fin) de la 2e ligne du verset + la référence [الـ...: N] si visible. Transcris tout, épele le nom de sourate et le chiffre.`],
  ["z8-jabir-yusr-end", `Fin (gauche) d'une ligne : «...فَقَدْ دَعَا عَلَيْهِ السَّلَامُ بِالرَّحْمَةِ لِمَنْ يُعَامِلُ النَّاسَ بِالْيُسْرِ وَالسُّهُولَةِ وَال...». Transcris le DERNIER mot exactement avec sa vocalisation (وَالسَّمَاحَةِ ? وَالسَّمَاحِ ? autre ?) et la ponctuation qui suit.`],
  ["z8-p101-glose23", `Deux ou trois gloses lexicographiques du manuel (terme en rouge : définition en noir). Transcris-les TOUTES exactement (TERME : DÉFINITION).`],
  ["z8-p101-ragabba4", `UNE ligne complète : «رَغَّبَ النبيُّ ﷺ في ... الناس وبذل النفع إليهم والإحسان إليهم، ومن مظاهر ذلك:» (ou similaire). Transcris la ligne ENTIÈRE. ÉPELLE ce qui se trouve entre «في» et «الناس» : الإكثار من الإحسان إلى ? autre ?`],
  ["z8-p104-table3", `TABLEAU complet d'un exercice («أستثمر تعلماتي وأملأ الجدول في دفتري بما يناسب:»). QUESTIONS : (1) Y a-t-il une rangée d'EN-TÊTES ? Transcris chaque en-tête exactement (ils peuvent être en couleur). (2) Combien de colonnes et de rangées de contenu ? (3) Transcris le contenu de CHAQUE case remplie (celles de droite), rangée par rangée. (4) Les colonnes de gauche sont-elles vides ?`],
  ["z8-p104-aya-box", `ENCADRÉ complet : un verset coranique ornementé sur deux lignes, puis sa référence [الـ...: N], puis «كيف أوافق بين مدلول هذه الآية ومدلول قوله ﷺ...». (1) IDENTIFIE le verset : de quelle sourate et quel numéro s'agit-il selon les mots que tu lis ? (2) Transcris le verset tel qu'imprimé. (3) Transcris la référence (nom + chiffre épelés). (4) Transcris la question complète.`],
];

for (const [name, q] of QS) {
  const png = `${DIR}/${name}.png`;
  const out = `${DIR}/vlm4-h6-18-${name}.txt`;
  if (!fs.existsSync(png)) { console.log(`MANQUANT: ${png}`); continue; }
  if (fs.existsSync(out)) { console.log(`déjà fait: ${out}`); continue; }
  const img = fs.readFileSync(png).toString('base64');
  let done = false;
  for (let attempt = 1; attempt <= 5 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: PRE + '\n\n' + q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1500,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(`=== ${name} ===\n` + txt.slice(0, 800) + '\n');
      done = true;
    } catch (e) { console.log(`${name} tentative ${attempt} échouée: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm4-h6-18');
