// Z2-39 — hadith-6ep leçon 4 «شكر الله على نعمة الجوارح» — ROND 3 : adjudications finales
// (protocole CONCORDE/NE CORRESPOND PAS + lignes pleine hauteur, citations p.34,
// soulignements de la citation الغزالي, sous-titre 2, chiffres).
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';
import { execSync } from 'child_process';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h6-05';

const COMMON = `Recadrage d'un manuel scolaire marocain d'hadith (6e année primaire traditionnel, en arabe), leçon «شكر الله على نعمة الجوارح». Sens de lecture droite→gauche. TRANSCRIS mot à mot ce qui est imprimé, sans jamais compléter par mémoire d'un texte connu. PROTOCOLE DE VÉRIFICATION : pour chaque mot disputé je te donne des CANDIDATS ; décris les lettres une par une (points au-dessus/dessous, boucles, hampes, signes de vocalisation) puis conclus : «CONCORDE avec le candidat X» ou «NE CORRESPOND PAS — je lis ...».`;

const ZONES = [
  ['p34-soulignements', 34, 600, 40, 505, 610, 728,
   `Citation de l'imam al-Ghazâlî (7 lignes) avec des mots SOULIGNÉS (traits horizontaux sous certains mots). TRANSCRIS la citation ENTIÈRE ligne par ligne, et pour CHAQUE ligne indique quels mots exactement portent le soulignement. Il y a environ 4 passages soulignés (fin de ligne 1, début de ligne 2, milieu de ligne 6, milieu de ligne 7). Transcris chaque passage souligné mot à mot avec ses voyelles.`],
  ['p31-sub2c', 31, 1200, 40, 522, 610, 568,
   `Sous-titre numéroté «2- ...» du deuxième وجيه de la section التحليل. CANDIDATS pour le titre complet: (A) «إعانة الناس ومساعدتهم» (B) «السعي في نفع العباد ومساعدتهم» (C) «إعانة الباس ومساعدتهم». Décris lettre par lettre le mot entre «2-» et «ومساعدتهم» (y a-t-il un seul mot ou plusieurs ? la 1re lettre du 2e mot: ن point AU-DESSUS ou ب point EN DESSOUS ?) et conclus.`],
  ['p31-yubayyin2', 31, 1200, 40, 560, 610, 600,
   `Première ligne du paragraphe du 2e وجيه (sous le sous-titre). Le PREMIER mot de la ligne. CANDIDATS: (A) «يُبَيِّنُ» (B) «يَرْشُدُ» (C) «كما أرشد» (D) «يبين». Décris: la 1re lettre (2 points dessous = yāʾ ?), la 2e lettre (1 point dessous = bāʾ ?), la 3e lettre (2 points dessous + shadda = yāʾ shadda ?). Puis transcris le reste de la ligne: «الرسول ﷺ في قوله: «وتعين الرجل في دابته فتحمله عليها، أو ترفع له عليها متاعه صدقة»...» jusqu'à la coupe. Le mot avant «الآخرين» (المبادرة بمساعدة الآخرين): décris «أن» ou «إن».`],
  ['p31-yuajjar2', 31, 1200, 40, 426, 610, 470,
   `Ligne du 1er وجيه: «فالإصلاح بين الناس من أعظم الصدقات التي ... عليها الإنسان؛». TRANSCRIS la ligne entière. Le VERBE: CANDIDATS (A) «تُؤَجَّرُ» (avec shadda sur le jīm) (B) «تُؤْجَرُ» (sans shadda) (C) «يُؤْجَرُ». Décris la 1re lettre (ت 2 points dessus ou ي 2 points dessous ?), le siège de la hamza, la présence/absence de shadda au-dessus du ج, et conclus.`],
  ['p32-yani2', 32, 1200, 40, 456, 610, 490,
   `Ligne: «باب فضل صلاة الجماعة] يعني: ...». Ce qui suit «يعني:». CANDIDATS: (A) «يُعْطَى حَسَنَةً، وَتُكَفَّرُ عَنْهُ سَيِّئَتُهُ» (B) «يُعْطَى بِحَسَنَةٍ، وَيُكَفَّرُ عَنْهُ سَيِّئَتُهُ» (C) «أُعْطِيَ حَسَنَةً، وَحُطَّ عَنْهُ خَطِيئَتُهُ». Décris: (1) le verbe après يعني (lettres + y a-t-il un ب devant حسنة ?) ; (2) le 2e verbe (ت ou ي initial ? shadda sur كاف ?) ; (3) le dernier mot (سيئته ? سيئة ? خطيئته ?) avec ses lettres. Conclus.`],
  ['p32-l6-imanan', 32, 1200, 40, 580, 610, 620,
   `Ligne contenant «...الأذى عن الطريق من فضائل الأعمال وشعب الإيمان...». Ce qui suit «وشعب الإيمان». CANDIDATS: (A) «؛» seul puis la ligne se termine (B) «كما جاء في الحديث الشريف؛» (C) «في الإسلام؛» (D) «كما حث عليها الإسلام؛». Décris mot à mot ce qui est imprimé après «الإيمان» jusqu'à la fin de ligne, puis le début de la ligne suivante si visible. Conclus.`],
  ['p32-bia', 32, 1200, 40, 548, 610, 586,
   `Ligne: «...بالمحيط وجمال ... والمبادرة إلى ... كل ما فيه أذى للإنسان أو غيره؛». Deux mots disputés: (1) après «وجمال»: CANDIDATS (A) «البيئة» (ب-ي-ئ-ة) (B) «الذات» (ذ-ا-ت). (2) après «إلى»: CANDIDATS (A) «إماطة» (إ-م-ا-ط-ة) (B) «إزالة» (إ-ز-ا-ل-ة). Décris les lettres de chaque mot et conclus. Transcris la ligne entière aussi.`],
  ['p33-faakhadh2', 33, 1200, 40, 104, 610, 142,
   `Deuxième ligne de la citation (haut de page 33): «يمشي بطريق وجد غصن شوك على الطريق ف...ه، فشكر الله له، فغفر له». Le VERBE après الطريق. CANDIDATS: (A) «فَأَخَرَهُ» (rāʾ SANS point) (B) «فَأَخَذَهُ» (dhāʾ 1 point AU-DESSUS). Décris la lettre entre le khāʾ et le hāʾ final. Transcris la ligne entière mot à mot avec la ponctuation exacte.`],
  ['p33-yujzi2', 33, 1200, 40, 268, 610, 336,
   `Fin du hadith du 6e وجيه + début de référence: «...وأمر بالمعروف صدقة، ونهي عن المنكر صدقة، ويجزي من ذلك ركعتان يركعهما من الضحى» [صحيح مسلم،...]. TRANSCRIS tout: (1) les voyelles de «ويجزي» (kasra ou fatha sous/ sur le yāʾ ?) ; (2) le verbe «يركعهما» (ses voyelles) ; (3) le début de la référence entre crochets (كتاب ...).`],
  ['p33-bab2', 33, 1200, 40, 335, 610, 368,
   `Ligne de référence + suite: la fin de [صحيح مسلم، كتاب صلاة المسافرين وقصرها، باب ...] — TRANSCRIS le chapitre complet (باب). Puis le début du commentaire «أي يكفي من هذه الصدقات...» si visible. Le verbe après «أي»: CANDIDATS (A) «يَكْفِي» (B) «تَكْفِي» (C) «يُغْنِي».`],
  ['p34-yantazim2', 34, 1200, 40, 540, 610, 574,
   `Deuxième ligne de la citation الغزالي: «السالكين وهو أيضا ... من علم وحال وعمل... فأما العلم فهو معرفة». Le mot après «وهو أيضا». CANDIDATS: (A) «يَنْتَظِمُ» (yāʾ initial avec 2 points dessous, puis nūn, puis tāʾ 2 points dessus, puis ẓāʾ 1 point, puis mīm) (B) «بِنْتَظِمُ» (bāʾ initial 1 point dessous) (C) «يَتَكَوَّنُ». Décris lettre par lettre et conclus. Transcris la ligne entière.`],
  ['p34-idmaruhu', 34, 1200, 40, 636, 610, 674,
   `Cinquième ligne de la citation الغزالي: «أما بالقلب فقصد الخير و... لكافة الخلق، وأما باللسان فإظهار الشكر لله تعالى بالتحميدات...». Le mot entre «الخير» et «لكافة». CANDIDATS: (A) «وإِضْمَارُهُ» (wāw + hamza-kasra + ḍād 1 point + mīm + alif + rāʾ + hāʾ) (B) «وَمَحَبَّتُهُ» (wāw + mīm + ḥāʾ SANS point + bāʾ shadda + tāʾ + hāʾ). Décris lettre par lettre et conclus. Transcris la ligne entière.`],
  ['p30-nasab', 30, 1200, 40, 120, 610, 168,
   `Deux premières lignes de la notice d'Abû Hurayra: «أبو هريرة رضي الله عنه. هو: ...». Le NASAB. CANDIDATS: (A) «عبد الرحمن بن صخر الدوسي» (صخر = ṣād + khāʾ 1 point + rāʾ) (B) «عبد الرحمن بن عمر بن عبد الدوسي». Décris les mots entre «هو:» et «كان» lettre par lettre et conclus. Transcris aussi la phrase suivante («كان أكثر الصحابة حفظا للحديث ورواية له. قدم المدينة ورسول الله ﷺ بخيبر سنة 7 هـ...») jusqu'à «ولزم».`],
  ['p30-fihi', 30, 1200, 40, 693, 610, 748,
   `Deux lignes de la section أولا (fin de page 30): «...وأمده بالصحة والعافية...، وأسبغ عليه نعما كثيرة ظاهرة وباطنة، في بدنه ويديه». Le mot après «والعافية». CANDIDATS: (A) «فيه،» (B) «،» seule (pas de فيه). Décris ce qui est imprimé entre «والعافية» et «وأسبغ» et conclus.`],
  ['p30-istaamala', 30, 1200, 40, 356, 610, 398,
   `Deuxième ligne de la glose السلامى: «والأصابع والأرجل، ثم ... في سائر عظام الجسد ومفاصله». Le verbe après «ثم». CANDIDATS: (A) «اسْتَعْمَلَ» (actif: sukūn sur le tāʾ, fatha sur le ʿayn) (B) «اسْتُعْمِلَ» (passif: ḍamma sur le tāʾ, kasra sous le ʿayn). Décris les voyelles imprimées sur le ت et le ع et conclus.`],
  ['p33-azum', 33, 1200, 40, 211, 610, 262,
   `Introduction du 6e وجيه + début du hadith. Le mot après «من». CANDIDATS: (A) «عِظَمِ» (kasra sous le ʿayn) (B) «عَظْمِ» (fatha sur ʿayn + sukūn sur ẓāʾ) (C) «عَظُمِ». Décris les voyelles et conclus. Puis le PREMIER mot du hadith après «ﷺ:»: CANDIDATS (A) «يَصْبَحُ» (fatha sur yāʾ, fatha sur bāʾ) (B) «يِصْبِحُ» (kasra sur yāʾ, kasra sous bāʾ). Décris et conclus. Transcris la ligne entière.`],
  ['p29-hadith-mid', 29, 1200, 40, 636, 610, 710,
   `Dernières lignes du hadith: «...متاعه صدقة، والكلمة الطيبة صدقة، وبكل خطوة تمشيها إلى الصلاة صدقة، وتميط الأذى عن الطريق صدقة». [رواه البخاري ومسلم]. VÉRIFIE mot à mot: (1) y a-t-il «صدقة» après «متاعه» ? (2) le segment «والكلمة الطيبة صدقة،» est-il imprimé ? (3) «وبكل خطوة» — puis le verbe: «تمشيها» (CANDIDATS A) ou «تخطوها» (B) ? (4) la référence finale: «رواه البخاري ومسلم» ou «متفق عليه» ? Décris et conclus pour chaque point.`],
  ['p35-jadwal-hdr2', 35, 1200, 40, 264, 610, 316,
   `En-têtes du tableau de l'activité 3 (3 colonnes). TRANSCRIS chaque en-tête. Le 3e en-tête (colonne de gauche): CANDIDATS (A) «الشكر بترك العباد» (B) «الشكر بترك العصيان» (C) «الشكر بترك المعصية» (D) «الشكر بترك المعاصي». Décris le dernier mot lettre par lettre et conclus. Donne aussi les 2 autres en-têtes exacts et l'étiquette de la 1re ligne de contenu (اللسان ?).`],
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
        model: 'glm-5v-turbo', temperature: 0.1, max_tokens: 1700,
      });
      const txt = r?.choices?.[0]?.message?.content ?? JSON.stringify(r);
      fs.writeFileSync(out, txt);
      console.log(txt.slice(0, 400));
      done = true;
    } catch (e) { console.log(`tentative ${attempt} ${nom} échec: ${e.message}`); await sleep(5000*attempt); }
  }
  if (!done) console.log(`ECHEC ${nom} — quota ?`);
  await sleep(2000);
}
