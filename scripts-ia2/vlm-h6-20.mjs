// IA-2 — vlm-h6-20.mjs : scrutins VLM L20 (11 points, pp.110-114).
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

const DIR = '/home/z/my-project/pdf-work/h6-15/zoom';
const OUT = '/home/z/my-project/pdf-work/h6-15/vlm-l20';
fs.mkdirSync(OUT, { recursive: true });
const zai = await ZAI.create();

const jobs = [
  {
    key: 'p110-cart',
    img: 'z1-p110-cart-vlm.png',
    q: `Cartouche de leçon d'un manuel scolaire marocain (1200 dpi couleur). SCRUTIN 1 : le NUMÉRO de la leçon dans le médaillon (chiffres attendus : 19 ou ١٩). SCRUTIN 2 : transcris le TITRE complet mot à mot (attendu : «العبادة وسيلة القرب والمحبة» ou proche). Décris la ponctuation.`,
  },
  {
    key: 'p110-tam1',
    img: 'z3-p110-tam1-vlm.png',
    q: `Première ligne du تمهيد d'un manuel (3600 dpi) : «___ غَايَةٌ يَرْجُو الْعَبْدُ الْوُصُولَ إِلَيْهَا هِيَ الْقُرْبُ مِنَ اللهِ تَعَالَى...». SCRUTIN : le PREMIER mot : «الْوِلَايَةُ» (alif-lām-wāw-lām-yā'-tā' marbūṭa) ou «الْمَحَبَّةُ» ou «الْقُرْبُ» ou autre ? Décris ses consonnes une par une. Transcris la ligne entière.`,
  },
  {
    key: 'p110-tam3',
    img: 'z3-p110-tam3-vlm.png',
    q: `Lignes d'un manuel scolaire (3600 dpi) : «فما هي العبادة التي ___ القرب من الله وولايته؟ ومن هم أولياء الله؟ وما جزاء من عاداهم؟». SCRUTIN : le verbe après «التي» : «تُنِيلُهُ» (nūn-yā'-lām + hā' : lui procure) ou «تُوصِلُهُ إِلَى» ou autre ? Décris les consonnes. Transcris les deux lignes.`,
  },
  {
    key: 'p110-matn2',
    img: 'z3-p110-matn2-vlm.png',
    q: `Deux-trois lignes d'un hadith vocalisé (3600 dpi) : «...وما تقرب إليّ عبدي بشيء أحب إليّ مما افترضته عليه، ___ يزال عبدي يتقرب إليّ بالنوافل حتى أحبه ...» [رواه البخاري]. SCRUTIN 1 : «ولا يزال» (lām-alif après le waw) ou «وما يزال» (mīm-alif) ? SCRUTIN 2 : «افترضته» (avec hā' final) ou «افترضت» (sans hā') ? SCRUTIN 3 : après «حتى أحبه» : y a-t-il des points de suspension «...» ? Où se trouve exactement le guillemet fermant » par rapport à l'ellipse et à [رواه البخاري] ? Transcris mot à mot.`,
  },
  {
    key: 'p111-aya',
    img: 'z3-p111-aya-vlm.png',
    q: `Encadré coranique coloré d'un manuel (3600 dpi) contenant un verset ou plusieurs de sourate يونس : «ألا إن أولياء الله لا خوف عليهم ولا هم يحزنون...». SCRUTIN 1 : transcris le texte coranique MOT À MOT exactement quoté (jusqu'à «وفي الآخرة» ?). SCRUTIN 2 : la RÉFÉRENCE entre crochets : [يونس: ٦٢] ou [يونس: ٦٢-٦٤] ou autre — quels chiffres exacts ? Transcris aussi la ligne qui suit («وفي هذا الحديث من الفقه...») si visible.`,
  },
  {
    key: 'p112-umaref',
    img: 'z3-p112-umaref-vlm.png',
    q: `Fin d'un hadith (3600 dpi) : «...ثم تلا رسول الله ﷺ: "ألا إن أولياء الله لا خوف عليهم ولا هم يحزنون" [يونس: ...]». [سنن أبي داود...]. SCRUTIN 1 : le verbe : «ثم تلا» ou «ثم قرأ» ? SCRUTIN 2 : la référence du verset : [يونس: ٦٢] ? SCRUTIN 3 : la référence finale : transcris-la MOT À MOT : [سنن أبي داود باب في الرهن] ou [سنن أبي داود، كتاب الإجارة، باب في الرهن] ou autre ? Transcris les deux dernières lignes.`,
  },
  {
    key: 'p112-thalitha',
    img: 'z3-p112-thalitha-vlm.png',
    q: `Passage d'un manuel (3600 dpi) : «دل قوله "حتى أحبه" على أن أولياء الله الأخيار الأتقياء مقاماً عند الله، هو مقام المحبة، ومحبة الله لأوليائه ___ عن قربه منهم ونصرته وتأييده ومعيته لهم بالحفظ والنصر واللطف والتمكين». SCRUTIN : le mot : «كِنايةٌ» (kāf-nūn-alif-yā'-tā' marbūṭa = métaphore) ou «كِفايةٌ» (kāf-fā'-...) ou autre ? Décris ses consonnes. Transcris le passage.`,
  },
  {
    key: 'p112-wasail',
    img: 'z3-p112-wasail-vlm.png',
    q: `Ligne d'un manuel (3600 dpi) : «فالفرائض لتحقيق القدر الواجب ___ التزكية والاستقامة». SCRUTIN : y a-t-il «مِنْ» entre الواجب et التزكية ? La séquence exacte : «القدر الواجب التزكية والاستقامة» ou «القدر الواجب من التزكية والاستقامة» ou «القدر الواجب للتزكية والاستقامة» ? Transcris la ligne.`,
  },
  {
    key: 'p113-maida',
    img: 'z3-p113-maida-vlm.png',
    q: `Encadré coranique coloré (3600 dpi) avec un ou deux versets de sourate المائدة : «إنما وليكم الله ورسوله والذين آمنوا...» + éventuellement «ومن يتول الله ورسوله والذين آمنوا فإن حزب الله هم الغالبون». SCRUTIN 1 : transcris le(s) verset(s) MOT À MOT. SCRUTIN 2 : les RÉFÉRENCES : [المائدة: ٥٥] seul, ou [المائدة: ٥٥-٥٦], ou une réf après chaque verset ? SCRUTIN 3 : la ligne après l'encadré : «فمن أحبهم فقد أحب الله ومن أحب الله أحبه الله» — transcris-la exactement.`,
  },
  {
    key: 'p113-yust3',
    img: 'z3-p113-yust3-vlm.png',
    q: `Items d'une liste d'un manuel (3600 dpi) : «- محبة الله لأوليائه توجب محبتهم ___ وعدم معاداتهم.» et «- دعوة الله تعالى عباده إلى السعي لنيل ولايته والارتقاء في درجاتها.». SCRUTIN : le mot manquant de l'item 3 : «ودوام مودتهم» ou «ودفع أذاهم» ou «ودوام برهم» ou autre ? Décris ses consonnes. Transcris les items complets.`,
  },
  {
    key: 'p114-aya1',
    img: 'z3-p114-aya1-vlm.png',
    q: `Citation coranique d'un manuel (3600 dpi) : «قال الله تعالى: (إن الله يحب ___)... [البقرة: ...]». SCRUTIN 1 : transcris le verset MOT À MOT — «إن الله يحب التوابين ويحب المتطهرين» ? SCRUTIN 2 : la RÉFÉRENCE : [البقرة: ٢٢٢] ou autre — quels chiffres ? Transcris aussi la citation suivante «وقال الله تعالى: (قل إن كنتم تحبون الله...)» et sa référence si visible.`,
  },
];

for (const j of jobs) {
  let done = false;
  for (let attempt = 1; attempt <= 4 && !done; attempt++) {
    try {
      const img = fs.readFileSync(`${DIR}/${j.img}`).toString('base64');
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: j.q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1500,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(`${OUT}/${j.key}.txt`, txt);
      console.log(`\n########## ${j.key} ##########\n${txt}`);
      done = true;
    } catch (e) { console.log(`${j.key} tentative ${attempt} échec: ${e.message}`); await new Promise(r => setTimeout(r, 8000 * attempt)); }
  }
}
console.log('OK vlm-h6-20');
