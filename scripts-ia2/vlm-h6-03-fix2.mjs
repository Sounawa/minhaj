// Z2-37 — lot de rattrapage : finesse de lecture (zones délimitées à la ligne près)
// + confirmations tableau p22 + bandeau p23 + p20/p21 jointure de citation.
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-03';

const COMMON = `Recadrage précis d'un manuel scolaire marocain d'hadith (6e primaire), leçon «تحريم الظلم» (hadith qudsi d'Abû Ḏarr). Texte naskh vocalisé, lecture droite→gauche. TRANSCRIS mot à mot avec les voyelles ce qui est imprimé, sans compléter par mémoire.`;

// (nom, page, dpi, x0,y0,x1,y1, question)
const ZONES = [
  ['fx-p20-joint', 20, 1200, 40, 726, 610, 772,
   `Bas de page (2 lignes). TRANSCRIS-les entièrement mot à mot. La 1re ligne contient probablement la fin d'une phrase sur l'adoration («...فعبادة الله... بها تترقى؟...») et la 2e ligne commence peut-être par «وفي قوله: «يا عبادي لو أن أولكم وآخركم وإنسكم وجنكم كانوا على...»» (citation qui continue en page suivante). Donne chaque mot exactement.`],
  ['fx-p21-top', 21, 1200, 40, 78, 610, 200,
   `Bloc de 4 lignes en haut de page. TRANSCRIS tout mot à mot. Contenu attendu (à VÉRIFIER sur les pixels, ne pas compléter): une fin de phrase sur les âmes/cœurs («...نفوسهم... قلوبهم...»), puis «وفي قوله: «يا عبادي لو أن أولكم وآخركم وإنسكم وجنكم كانوا على أتقى...»», puis «...قلب/قلوب رجل/رجُل واحد منكم ما زاد ذلك في ملكي شيئا» تأكيد لما تقدم، puis «وفيه أن تقوى المتقين مصلحة... وأنها لا تزيد في ملكه تعالى شيئا». CONFIRME: (a) le mot avant «قلب/قلوب» est-il أتقى (une ou deux fois?) ; (b) «قلب رجل واحد» ou «قلوب رجل» ? ; (c) «مصلحة لهم» ou «مصلحة عمومهم» ?`],
  ['fx-p17-questions', 17, 1200, 40, 473, 610, 532,
   `Les deux questions conclusives du تمهيد (2-3 lignes). TRANSCRIS-les mot à mot avec la ponctuation (؟). Attendu: «فما معنى تحريم الله الظلم على نفسه؟ وما مظاهر افتقار...؟ وما ثمرتها في حياتي؟» — donne la formulation EXACTE (افتقار الخلق؟ افتقارنا؟ إليه؟).`],
  ['fx-p22-table', 22, 600, 30, 540, 610, 795,
   `Tableau du التقويم (3 colonnes × 6 lignes). CONFIRME mot à mot: (1) l'en-tête de droite (أسماء الله الحسنى وصفاته? أسماء الله تعالى وصفاته? autre?) ; (2) l'en-tête du centre (مظاهرها في الحديث القدسي?) ; (3) l'en-tête de gauche (أثرها في حياتي? تفسيرها في حياتي? autre?) ; (4) les 5 mots de la colonne de droite, ligne par ligne (العدل؟ الغني؟ الهادي؟ الغفور؟ الرزاق؟ — vocalisation exacte de chacun). Les colonnes centre/gauche sont-elles vides?`],
  ['fx-p23-ban', 23, 600, 40, 470, 610, 510,
   `Bandeau décoratif de rubrique (calligraphie claire sur fond coloré). TRANSCRIS-le lettre par lettre: «الإعداد القبلي» ou «الإعداد التربوي» ou autre ?`],
  ['fx-p20-lidhalik', 20, 1200, 380, 422, 610, 446,
   `UNE ligne (moitié droite). Elle contient «...أُمِرُوا بطلبِ الهداية والطعام والكسوة والمغفرة من الله عز وجل وحده، وعدمِ الاستغناء عنه». Quel est le PREMIER mot de la ligne (à droite): «لأنهم» (ل-أ-ن-ه-م) ou «لذلك» (ل-ذ-ل-ك) ou «فذلك» ou autre ? Décris les lettres du premier mot une par une.`],
  ['fx-p21-tanbih2', 21, 1200, 40, 333, 610, 382,
   `Trois lignes du commentaire ثالثاً. TRANSCRIS-les mot à mot: «...ويوسعوا الطلب، وأن لا يحقر سائلا ولا يخجل طالب؛ فإن ... لا ...، وخزائنه لا تنفد؛ فلا يظن ظان أن ما عند الله يغيضه الإنفاق، وقد قال...». Donne EXACTEMENT: (a) le mot entre «فإن» et «لا» ; (b) le verbe après ce «لا» (ينفد؟ ينقص؟) ; (c) le mot après «وخزائنه».`],
  ['fx-p20-thani2', 20, 1200, 40, 158, 610, 188,
   `UNE ligne. Attendu: «لأن الظلم بعيد عن رحمة الله ...، ولأن للظلم آثارا سيئة على الفرد والمجتمع». TRANSCRIS-la mot à mot; quel est le mot après «رحمة الله» (عز وجل ? تعالى ?) et la ponctuation autour.`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

fs.mkdirSync(`${DIR}/crops`, { recursive: true });
for (const [nom, pg, dpi, x0, y0, x1, y1] of ZONES) {
  const fp = `${DIR}/crops/vlm-${nom}.png`;
  if (!fs.existsSync(fp)) {
    const S = dpi / 72.0;
    execSync(`python3 -c "
from PIL import Image
S=${S}
im=Image.open('${DIR}/r${dpi}/p${pg}.png')
im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S))).save('${fp}')
"`);
  }
}

for (const [nom, pg, , , , , , Q] of ZONES) {
  const out = `${DIR}/vlm-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  const img = fs.readFileSync(`${DIR}/crops/vlm-${nom}.png`).toString('base64');
  console.log(`\n======== ${nom} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 3 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1300,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${nom} échec: ${e.message}`); await sleep(5000*attempt); }
  }
  if (!done) console.log(`ECHEC ${nom} — quota ?`);
  await sleep(2000);
}
