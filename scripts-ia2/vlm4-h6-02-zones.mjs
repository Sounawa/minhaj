// Z2-36 — VLM round 4b : versets muminun/baqara ligne par ligne, zooms sur les
// chiffres de références [sourate: verset], cellule sulukat L1, cartouche أحاديث.
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-02';
const S = 600 / 72.0;

const COMMON = `Recadrage d'un manuel scolaire marocain d'hadith (arabe), leçon sur le hadith «الطهور شطر الإيمان». Le texte coranique cité est imprimé dans une police de moucharabieh calligraphiée avec ornements ۞ et ﴿﴾. TRANSCRIS mot à mot UNIQUEMENT ce qui est imprimé (ne complète jamais par mémoire d'un texte connu). Les chiffres peuvent être occidentaux (0-9) ou arabo-orientaux (٠-٩) : donne leur valeur.`;

// (nom, page, x0,y0,x1,y1 en pt @600dpi, question)
const ZONES = [
  ['muminun-2l', 13, 60, 578, 637, 630,
   `Deux lignes. La ligne 1 finit par «...قال الله تعالى:» suivi du DÉBUT d'un verset (ornement ﴿ puis 2-6 mots). La ligne 2 (courte, alignée à droite) contient la FIN du verset puis la référence entre crochets [المؤمنون: ...]. TRANSCRIS : (a) la fin de la ligne 1 après «قال الله تعالى:» mot à mot ; (b) la ligne 2 ENTIÈRE mot à mot ; (c) la valeur EXACTE des chiffres de la référence. Le verset parle des balances (موازين) au Jour du Jugement.`],
  ['muminun-ref', 13, 400, 606, 470, 632,
   `Zoom sur la fin de la citation coranique : derniers mots du verset + référence entre crochets [المؤمنون: ...]. TRANSCRIS lettre par lettre et donne la valeur EXACTE des chiffres (103 ? 102 ? autre ?).`],
  ['baqara-2l', 13, 60, 228, 637, 284,
   `Deux lignes. La ligne 1 finit par «وقيل: المراد بالإيمان هنا: الصلاة، قال الله تعالى: ﴿وَمَا...» (début d'un verset). La ligne 2 contient la FIN du verset ﴾ puis la référence [البقرة: ...] puis «أي صلاتكم، فالطهارة شرط في صحة الصلاة...». TRANSCRIS : (a) le verset ENTIÈRement mot à mot (il commence par ﴿وما) ; (b) la référence exacte : la valeur des chiffres (142 ? 143 ?) ; (c) les premiers mots après le crochet fermant.`],
  ['baqara-ref', 13, 60, 252, 170, 286,
   `Zoom sur le début gauche de la ligne 2 : fin du verset ﴾, référence entre crochets [البقرة: ...], puis le mot suivant. TRANSCRIS lettre par lettre et donne la valeur EXACTE des chiffres (142 ? 143 ? autre ?).`],
  ['tawba-ref', 15, 110, 406, 280, 434,
   `Zoom sur la fin de la citation coranique «...بأن لهم الجنة﴾» : la référence entre crochets [التوبة: ...] et le début de «ومنهم من يبيعها للشيطان...». TRANSCRIS lettre par lettre et donne la valeur EXACTE des chiffres (111 ? 112 ? 113 ?).`],
  ['sulukat-r1', 16, 330, 492, 637, 532,
   `Première ligne du tableau des comportements (colonne de droite «السلوكات»). TRANSCRIS le comportement de cette première ligne mot à mot : est-ce «محبة الناس والنصح لهم» ou «محبة الناس والصدق عليهم» ou autre ? Décris les lettres du 2e mot après «وال» : ن ص ح (ṣād pointillé + ḥā') ou ص د ق ? Donne la préposition exacte (لهم ? عليهم ?).`],
  ['ahadith-cart', 11, 120, 136, 520, 178,
   `Sous le bandeau-titre «المسارعة في الخيرات» il y a un second cartouche décoratif bleu calligraphié. TRANSCRIS son texte lettre par lettre (il commence peut-être par «أحاديث...»).`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

for (const [nom, pg, x0, y0, x1, y1] of ZONES) {
  const fp = `${DIR}/crops/vlm4-${nom}.png`;
  if (!fs.existsSync(fp)) {
    execSync(`python3 -c "
from PIL import Image
S=${S}
im=Image.open('${DIR}/r600/p${pg}.png')
im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S))).save('${fp}')
"`);
  }
}

for (const [nom, , , , , , Q] of ZONES) {
  const out = `${DIR}/vlm4-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  const img = fs.readFileSync(`${DIR}/crops/vlm4-${nom}.png`).toString('base64');
  console.log(`\n======== ${nom} ========`);
  let done = false;
  for (let attempt = 1; attempt <= 2 && !done; attempt++) {
    try {
      const r = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: COMMON + '\n\n' + Q },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${img}` } },
        ] }],
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1200,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt);
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${nom} échec: ${e.message}`); await sleep(5000*attempt); }
  }
  await sleep(2000);
}
