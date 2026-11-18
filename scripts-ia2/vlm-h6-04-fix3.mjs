// Z2-38 — Round 3b : micro-zooms finaux (diagramme p27 + derniers points disputés)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-04';

const COMMON = `Micro-recadrage (grossi) d'un manuel scolaire marocain d'hadith (6e primaire, arabe), leçon «التنافس في الخير». TRANSCRIS UNIQUEMENT ce qui est imprimé, mot à mot. Pour chaque candidat proposé, vérifie lettre par lettre (points, boucles, hampes) et conclus par CONCORDE ou NE CORRESPOND PAS. Ne complète jamais par mémoire d'un texte connu.`;

// (nom, [page,x0,y0,x1,y1,zoom] null si crop déjà fait, question)
const ZONES = [
  ['diag-centre', null,
   `Boîte jaune centrale en haut d'un organigramme. TRANSCRIS son texte complet mot à mot (c'est probablement une consigne d'activité, contenant peut-être le mot الصحابة). Donne chaque mot exactement.`],
  ['diag-bleu-d', null,
   `Boîte bleue de DROITE d'un organigramme (côté positif : أداء الفرائض). TRANSCRIS son texte complet mot à mot. Candidats: «أَدَاءُ الْفَرَائِضِ» / «أَدَاءُ الْفَرَائِضِ وَالنَّوَافِلِ» / «الْمُحَافِظُ» / autre. CONCORDE/NE CORRESPOND PAS pour chacun.`],
  ['diag-bleu-g', null,
   `Boîte bleue de GAUCHE d'un organigramme (côté négatif). TRANSCRIS son texte complet mot à mot. Candidats: «تَرْكُ الْفَرَائِضِ» / «الْإِهْمَالُ» / «الْمُفَرِّطُ» / autre. CONCORDE/NE CORRESPOND PAS pour chacun.`],
  ['diag-sous-d', null,
   `Zone sous la boîte bleue de droite d'un organigramme (entre la boîte et la première cellule «الإكثار من ذكر الله»). TRANSCRIS tout ce qui est imprimé (boîtes, texte, lignes). Candidat probable: une boîte avec «أَدَاءُ الْفَرَائِضِ وَالنَّوَافِلِ» ou similaire.`],
  ['diag-sous-g', null,
   `Zone sous la boîte bleue de gauche (entre la boîte et la première cellule «الغفلة عن ذكر الله»). TRANSCRIS tout ce qui est imprimé. Candidat probable: une boîte avec «تَرْكُ الْفَرَائِضِ» ou similaire.`],
  ['p24-tamhid-first', [24, 485, 346, 568, 384, 4],
   `Tout premier mot du paragraphe تمهيد (extrémité DROITE de la ligne). Candidats: (A) «فَيَظُنُّ» (fāʾ avec 1 point au-dessus + yāʾ + ẓāʾ avec 1 point + nūn avec shadda) ; (B) «قَدْ يَظُنُّ» (qāf 2 points + dāl, PUIS يَظُنُّ). Décris les TOUTES PREMIÈRES lettres à droite: combien de mots ? quelles lettres ? CONCORDE/NE CORRESPOND PAS pour (A) et (B).`],
  ['p24-aydha2', [24, 360, 560, 570, 610, 3],
   `Isnad du hadith: «عَنْ أَبِي ذَرٍّ رَضِيَ اللهُ عَنْهُ ... أَنَّ نَاسًا». Entre «عنه» et «أنّ», y a-t-il le mot «أَيْضًا» (alif-hamza + yāʾ 2 points dessous + ḍād 1 point au-dessus + alif + tanwīn fatha) ? CONCORDE/NE CORRESPOND PAS. Transcris la séquence exacte des mots entre عنه et ناسا.`],
  ['p25-dal-dhal', [25, 390, 410, 500, 444, 4],
   `Glose: «الدُّثُورُ: بِضَمِّ ...». Le mot après «بضم» est-il «الدَّالِ» (د sans point) ou «الذَّالِ» (ذ avec 1 point au-dessus) ? Décris la lettre entre le ال et le ا du mot. CONCORDE/NE CORRESPOND PAS.`],
  ['p26-tajannab', [26, 55, 654, 320, 696, 4],
   `Ligne de la section ثانياً (partie GAUCHE de la ligne): «... وَإِرْشَادُ النَّاسِ وَتَوْجِيهُهُمْ إِلَى الْخَيْرِ [?] صَدَقَةٌ مِنَ الصَّدَقَاتِ...». Le groupe entre «الخير» et «صدقة» est-il: (A) «وَتَجَنُّبُ الشَّرِّ» (wāw + tāʾ 2pts + jīm 1pt SOUS + nūn + bāʾ 1pt SOUS + shadda, puis shīn 3pts + rāʾ) ; (B) «وَتَحْذِيرُهُمْ» (wāw + tāʾ + ḥāʾ SANS point + dhāl 1pt + yāʾ + rāʾ + hāʾ-mīm) ; (C) autre chose — transcris-la. CONCORDE/NE CORRESPOND PAS pour (A) et (B).`],
  ['p26-dhalika2', [26, 370, 388, 568, 426, 4],
   `Ligne de la section أولاً: «... بِالْأَجْرِ كُلِّهِ؛ ذَلِكَ أَنَّ...». Après «أنّ», le mot est-il «هُ» (hāʾ bouclée avec damma, SANS mīm après) ou «هُمْ» (hāʾ + mīm boucle fermée) ? Décris précisément ce qui suit la hāʾ. CONCORDE/NE CORRESPOND PAS.`],
  ['p27-lastright2', [27, 330, 652, 550, 752, 3],
   `Cellule du bas de la colonne DROITE de l'organigramme (sous «التنافس في الخير», face à la cellule gauche «التمتع بالمباحات دون قصد التقرب إلى الله»). TRANSCRIS son texte complet (2 lignes). Candidats: (A) «التَّمَتُّعُ بِالْمُبَاحَاتِ بِقَصْدِ التَّقَرُّبِ إِلَى اللهِ» ; (B) «الِانْتِفَاعُ بِالْمُبَاحِ لِلتَّقَرُّبِ إِلَى اللهِ» ; (C) autre. CONCORDE/NE CORRESPOND PAS pour (A) et (B).`],
  ['p28-t3b', [28, 55, 210, 570, 268, 3],
   `Item 3 de la rubrique التقويم (troisième item numéroté 3-). TRANSCRIS-le mot à mot. Le premier verbe est-il «أَذْكُرُ» (alif-hamza + dhāl 1 point + kāf + rāʾ, SANS shadda sur kāf) ou «أُذَكِّرُ» (damma sur alif + shadda sur kāf) ? CONCORDE/NE CORRESPOND PAS.`],
  ['p28-t1-fin', [28, 50, 108, 270, 150, 4],
   `Fin de la ligne de l'item 1 de التقويم (partie GAUCHE): «... رَضِيَ اللهُ عَنْهُمْ ...». Transcris les derniers mots. La ligne se termine par «لِلَاقْتِدَاءِ» ou «لِلَاقْتِدَاءِ بِهِمْ.» (avec بِهِمْ: bāʾ 1 point sous + hāʾ + mīm) ? Décris la fin de ligne lettre par lettre. CONCORDE/NE CORRESPOND PAS.`],
  ['p28-cit-hadi', [28, 55, 396, 570, 438, 3],
   `Ligne de la citation d'Abû Ḏarr: «... رَفْعُكَ الْعَظْمَ عَنِ الطَّرِيقِ صَدَقَةٌ، وَ[?] الطَّرِيقَ صَدَقَةٌ، وَعَوْنُكَ ...». Le mot entre «وَ» et «الطريق» est-il: (A) «هُدَاكَ» (hāʾ + dāl + alif + kāf) ; (B) «هَادِي» (hāʾ + alif + dāl + yāʾ) ; (C) «هِدَايَتُكَ» (hāʾ + dāl + alif + yāʾ + tāʾ marbūṭa + kāf) ? Décris ses lettres une à une. CONCORDE/NE CORRESPOND PAS pour chacun. Transcris aussi la suite de la ligne («وعونك الضعيف بفضل قوتك صدقة»?).`],
  ['p28-cit-ref3', [28, 170, 438, 570, 470, 3],
   `Référence bibliographique en bleu entre crochets. TRANSCRIS-la mot à mot, en particulier: (1) le nom du livre («عَوْنُ الْمَعْبُودِ» ou autre) ; (2) la partie chiffrée avec l'ordre EXACT des chiffres (droite→gauche) ; (3) le dernier mot («بِتَصَرُّفٍ» avec tanwīn, ou «بِتَصَرُّفِ», ou autre).`],
];

const zai = await ZAI.create();
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

for (const [nom, spec, Q] of ZONES) {
  const out = `${DIR}/vlm-${nom}.txt`;
  if (fs.existsSync(out)) { console.log(`skip ${nom}`); continue; }
  let fp = `${DIR}/crops/vlm-${nom}.png`;
  if (spec) {
    const [pg, x0, y0, x1, y1, z] = spec;
    if (!fs.existsSync(fp)) {
      execSync(`python3 -c "
from PIL import Image
S=600/72.0
im=Image.open('${DIR}/r600/p${pg}.png')
c=im.crop((int(${x0}*S),int(${y0}*S),int(${x1}*S),int(${y1}*S)))
c=c.resize((c.width*${z},c.height*${z}),Image.LANCZOS)
c.save('${fp}')
"`);
    }
  }
  const img = fs.readFileSync(fp).toString('base64');
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
