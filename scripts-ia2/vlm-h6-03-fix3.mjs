// Z2-37 — fix3 : adjudication finale citations p.23 + derniers points disputés.
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-03';

const COMMON = `Manuel scolaire marocain d'hadith (6e primaire), leçon «تحريم الظلم». Lecture droite→gauche. RÈGLE ABSOLUE: transcris UNIQUEMENT les pixels visibles, mot à mot. Si un mot ne correspond pas au candidat proposé dans la question, écris ce que tu vois, pas le candidat. Un mot illisible → [illisible].`;

const ZONES = [
  // ===== ADJUDICATION CITATIONS p.23 =====
  ['a23-v1', 23, 1200, 40, 122, 610, 178,
   `Activité 1 de الاستثمار: le VERSAT 1 complet (2 lignes dans un cadre moucharabieh) + sa référence. Structure: «1- قال الله تعالى: ﴿[ligne1] [ligne2]﴾ ۝[médaillon] [sourate: numéro].». CANDIDAT à VÉRIFIER pixel par pixel (peut être FAUX): «وإذا أردنا أن نهلك قرية أمرنا مترفيها ففسقوا فيها فحق عليها القول فدمرناها تدميرا» avec référence [الإسراء: 16]. TRANSCRIS: (1) la ligne 1 mot à mot ; (2) la ligne 2 mot à mot ; (3) le numéro du médaillon (valeur) ; (4) la référence: nom de sourate LETTRE PAR LETTRE + valeur des chiffres (décris-les) ; (5) VERDICT: le candidat correspond-il aux pixels ? Cite les différences.`],
  ['a23-v2', 23, 1200, 40, 150, 610, 226,
   `Suite de l'activité 1: le VERSET 2 complet (3 lignes: début après la référence du verset 1, suite, fin) + sa référence. Structure: «وقال الله تعالى: ﴿[lignes]﴾ ۝[médaillon] [طه: numéro].». CANDIDAT à VÉRIFIER pixel par pixel (peut être FAUX): «ولا تمدن عينيك إلى ما متعنا به أزواجا منهم زهرة الحياة الدنيا لنفتنهم فيه ورزق ربك خير وأبقى» avec référence [طه: 131]. TRANSCRIS: (1) chaque ligne mot à mot ; (2) le numéro du médaillon ; (3) la référence [طه: chiffres] avec la valeur exacte (décris chaque chiffre) ; (4) VERDICT: le candidat correspond-il ? Différences ?`],
  // ===== BANDEAU RUBRIQUE p.19 =====
  ['a19-ban', 19, 1200, 120, 100, 500, 155,
   `Bandeau décoratif de rubrique (calligraphie claire sur fond coloré, en haut de page, au-dessus des gloses «ضال: مائل عن...»). TRANSCRIS-le lettre par lettre. Candidats (VÉRIFIE): «الفهم» ou «الشرح» ou autre. Décris chaque lettre: nombre de points, forme.`],
  // ===== MOT INITIAL التحليل p.19 =====
  ['a19-intro', 19, 1200, 380, 506, 610, 540,
   `Début de la phrase d'intro du التحليل. TRANSCRIS la ligne mot à mot. Le PREMIER mot (à droite) est-il «يُبيِّنُ» (ي-ب-ي-ن, racine بيّن) ou «يتضمن» (ي-ت-ض-م-ن, racine ضمّ)? Décris les lettres du premier mot une par une (points, boucles).`],
  // ===== GLOSE 1 p.19 =====
  ['a19-glose1', 19, 1200, 40, 143, 610, 170,
   `UNE ligne de glose: «ضالٌّ: ...». TRANSCRIS-la mot à mot. Le mot après «عن» est-il «الصراط» (ص-ر-ا-ط) ou «الطريق» (ط-ر-ي-ق)? Décris les lettres de ce mot une par une.`],
  // ===== OBJECTIF 1 p.17 =====
  ['a17-obj1', 17, 1200, 40, 182, 610, 210,
   `UNE ligne: le premier objectif de la leçon. TRANSCRIS-la mot à mot avec la voyellation. Le verbe après «أن» est-il «أعرفَ» (ع-ر-ف, 3 lettres) ou «أتعرفَ» (ت-ع-ر-ف, 4 lettres)? Et le dernier mot est-il «للظلم» (ل-ل-ظ-ل-م, DEUX lâm avant ظ) ou «الظلم» (un seul lâm)? Décris lettre par lettre.`],
  // ===== QUESTION MILIEU p.17 =====
  ['a17-quest', 17, 1200, 40, 476, 610, 518,
   `La deuxième question du تمهيد (2 lignes). TRANSCRIS mot à mot: «وما مظاهر افتقار...؟». Le mot après «مظاهر» est-il «افتقارنا» (suffixe ـنا) ou «افتقار الخلق» (mot الخلق)? Y a-t-il «إلى» avant «الله عز وجل»? Donne la formulation exacte complète de la ligne.`],
  // ===== JOINTURE p.20 =====
  ['a20-joint2', 20, 1200, 40, 693, 610, 764,
   `Les DEUX dernières lignes de texte de la page (au-dessus du bandeau de pagination). TRANSCRIS-les mot à mot. Attendu (VÉRIFIE): ligne A: «...ولا ضره بطاعته أو معصيته، فعبادة الله ما هي إلا لمصلحة العباد، بها تترقى...» ligne B: la suite de la phrase. CONFIRME: (a) «ما هي إلا» ou «ما هي» ou «إنما هي»? (b) «لمصلحة العباد» ou «لمصلحة العبد»? (c) la ligne B commence-t-elle par «نفوسهم»? Donne tout ce qui est visible ligne par ligne.`],
  // ===== p.21 LIGNE 1 =====
  ['a21-l1', 21, 1200, 40, 80, 610, 112,
   `UNE ligne (première ligne de la page): «نُفُوسُهُمْ، و...». TRANSCRIS-la mot à mot avec voyellation. Le mot entre «نفوسهم،» et le mot final: est-il «وتطمئن قلوبهم» ou «وتطهر قلوبهم» ou «وتنظف قلوبهم» ou autre? Le dernier mot: «وتسعد حياتهم» ou autre? Décris les lettres.`],
  // ===== p.21 لا ينفد/ينقص =====
  ['a21-nafd', 21, 1200, 340, 358, 610, 384,
   `UNE ligne (partie droite): «فإن ما عند الله لا ...، وخزائنه لا تنفد؛...». TRANSCRIS-la mot à mot. Le verbe après le premier «لا» est-il «ينفدُ» (ن-ف-د) ou «ينقصُ» (ن-ق-ص)? Décris la 3e lettre: boucle fermée avec point au-dessus (د) ou boucle ouverte avec 2 points (ص)?`],
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
  for (let attempt = 1; attempt <= 2 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1400,
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
