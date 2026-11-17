// Z2-22 — hadith-5ep leçon 20 — adjudications VLM lettre-niveau (z20-r*/z20-w*)
import ZAI from '/home/z/my-project/node_modules/z-ai-web-dev-sdk/dist/index.js';
import fs from 'fs';

const DIR = '/home/z/my-project/scripts-ia2/tmp/h5-20';

const COMMON = `Extrait 600 dpi d'un manuel scolaire marocain d'hadith (5e année primaire), leçon 20 « دَعْمٌ وَتَطْبِيقٌ » (pp.111-113), sens de lecture droite→gauche.
TRANSCRIS EXACTEMENT ce qui est imprimé, mot à mot, avec la vocalisation. Analyse LES LETTRES UNE À UNE quand le mot est contesté : nomme chaque lettre de base (alif, bāʾ, tāʾ, thāʾ, ǧīm, ḥāʾ, khāʾ, dāl, dhāl, rāʾ, zāy, sīn, shīn, ṣād, ḍād, ṭāʾ, ẓāʾ, ʿayn, ġayn, fāʾ, qāf, kāf, lām, mīm, nūn, hāʾ, wāw, yāʾ) et les points (0/1/2/3) au-dessus/dessous, plus les diacritiques (fatha, kasra, ḍamma, sukūn, shadda, tanwīn). Ne complète JAMAIS par mémoire d'un texte connu : seulement ce qui est imprimé. Illisible : [؟]. Réponds par la transcription uniquement.`;

// question spécifique par recadrage
const Q = {
  r01: `Objectifs de la leçon. Transcris les 3 objectifs numérotés. Attention au 1er : le verbe après « أَنْ » — est-ce أَقُومَ بِتَقْوِيمِ (avec le mot بِتَقْوِيمِ) ou أُقَوِّمَ (un seul mot, shadda sur le wāw) ? Lettre-niveau sur ce verbe et sur مُكْتَسَبَاتِي.`,
  r02: `Début du texte (النص). Transcris les lignes : الإِنْسَانُ اجْتِمَاعِيٌّ بِطَبْعِهِ... jusqu'à ... بِكُلِّ أَنْوَاعِهَا. Attention : بِطَبْعِهِ ou بِطَبِيعَتِهِ ? تَرْبِطُهُ ou تَرْبِطُ ?`,
  r03: `Suite : la ligne qui commence par بَلْ (ou بِلْ) ذَهَبَ الْإِسْلَامُ... puis la citation et le début de l'āya des Ḥuǧurāt. Transcris tout. Attention : أَبْعَدَ مِنْ ذَلِكَ ou بَعْدَ ذَلِكَ ? حَيْثُ ou حَتَّى ?`,
  r04: `Deuxième paragraphe : وَجَعَلَ مِنْ عَلَامَاتِ الْإِيمَانِ... jusqu'à ﴿وَإِنَّكَ لَعَلَى خُلُقٍ عَظِيمٍ﴾ [القلم: 4]. Transcris tout, avec les refs entre crochets.`,
  r05: `Introduction خديجة (1re partie) : كَمَا أَنَّ أُمَّ الْمُؤْمِنِينَ خَدِيجَةَ... Transcris tout. Lettre-niveau sur le verbe après أَنْ تَـ : تُخَفِّفَ (khāʾ+fāʾ+shadda) ou autre chose ?`,
  r06: `Introduction خديجة (2e partie) : ...تَخْوُفَهُ مِنْ... نُزُولِ الْوَحْيِ... Transcris. Attention : حُدُوثِ (ḥāʾ+dāl+wāw+thāʾ) ou حَدَثِ ?`,
  r07: `Fin intro خديجة + citation complète : ... اتَّخَذَتْ/اِتَّخَذَتْ مِنْ حُسْنِ أَخْلَاقِهِ الَّتِي/الَّذِي... قَبْلَ النُّبُوَّةِ... فَقَالَتْ: كَلَّا وَاللهِ... Transcris tout, avec [صحيح البخاري] tel qu'imprimé.`,
  r08: `Rubrique الفهم et ses 2 questions : أَضَعُ عُنْوَانًا... / أَشْرَحُ ... Transcris tout, y compris le titre de rubrique.`,
  r09: `Titre de rubrique التحليل + question 1 : جَاءَ فِي النَّصِّ أَنَّ الْإِسْلَامَ... Transcris. Attention au verbe après الْإِسْلَامَ : نَظَّمَ (shadda sur ẓāʾ) ou autre ?`,
  r10: `Questions 2 et 3 de l'analyse : أَسْتَدِلُّ... / أَسْتَخْرِجُ مِنْ قَوْلِ أُمِّ الْمُؤْمِنِينَ خَدِيجَةَ... Transcris tout avec la liste des trois items.`,
  r11: `Question 4 : عَلَى أَيِّ شَيْءٍ يُسْتَدَلُّ... Transcris. Attention : اِتَّصَفَ (masculin) ou اِتَّصَفَتْ (tāʾ marbūṭa final) ?`,
  r12: `Rubrique التطبيق complète : question 1 (حث الإسلام... محسنه... أمثال هؤلاء...) et question 2 (بيّن كيف يمكن ضبط الجوارح...). Transcris tout mot à mot.`,
  r13: `Titre الإعداد القبلي + contenu : أَحْفَظُ حَدِيثَ الدَّرْسِ الْمُقْبِلِ... Transcris. Attention au titre : الإِعْدَادُ الْقَبْلِيُّ (singulier) ou الأَعْدَادُ الْقَبْلِيَّةُ (pluriel) ? Et le dernier mot après مَعَ : الْغَضَبِ ?`,
  w01: `Objectif 1. Analyse LETTRE PAR LETTRE ce qui est entre « أَنْ » et « فِي » : combien de mots ? Premier mot : أَقُومَ (qāf+wāw, sukūn?) — deuxième mot commence-t-il par bāʾ (بِتَقْوِيمِ) ou est-ce un seul mot أُقَوِّمَ (shadda sur wāw) ? Décris les points sur chaque lettre.`,
  w02: `Fin d'une ligne du texte : ... وَيَعِيشُ + le mot suivant (النَّاسُ ?). Transcris et décris lettre-niveau.`,
  w03: `Début de ligne : les 2-3 premiers mots après le début (droite). Y a-t-il فِي أَمْنٍ وَأَمَانٍ ou فِي أَمْنٍ وَإِيمَانٍ ou فِي سَلَامٍ ? Puis فَقَدْ نُظِّمَ/نَظَّمَ الْإِسْلَامُ ? Lettre-niveau sur le 2e mot du coordonné (mīm? yāʾ? hamza?) et sur le verbe (shadda?).`,
  w04: `Ligne : بَلْ/بِلْ ذَهَبَ الْإِسْلَامُ... Transcris tout le fragment. Lettre-niveau sur أَبْعَدَ/بَعْدَ (alif après bāʾ ?) et sur حَيْثُ/حَتَّى.`,
  w05: `Milieu de ligne : ...الْإِيمَانِ + le mot suivant. Est-ce الدَّالَّةِ (dāl+lām+tāʾ marbūṭa) ou اللَّهُ (lām+lām+hāʾ avec shadda) ? Décris chaque lettre et chaque point. Transcris ensuite عَلَى كَمَالِهِ.`,
  w06: `Fin de ligne : ... وَلَنَا فِي رَسُولِ اللهِ ou وَلَا فِي رَسُولِ اللهِ ? Lettre-niveau : après وَ y a-t-il لَ + نَا (nūn+alif) ou لَا (alif seul) ?`,
  w07: `Ligne : فَقَدْ كَانَ الْمَثَلُ الْأَعْلَى فِي الْإِحْسَانِ إِلَى... Lettre-niveau sur الْمَثَلُ (mīm+thāʾ+lām) et الْأَعْلَى, puis sur الْإِحْسَانِ (ḥāʾ+sīn) ou الْإِنْسَانِ (nūn)?`,
  w08: `Début de ligne (droite) : الْغَيْرُ؟ وَقَدْ مَدَحَهُ/مُدَّحَهُ اللهُ تَعَالَى بِذَلِكَ فَقَالَ. Lettre-niveau sur le verbe : mīm+fāʾ+ḥāʾ — y a-t-il une shadda (مُدَّحَ) ou pas (مَدَحَ) ?`,
  w09: `Ligne : كَمَا أَنَّ أُمَّ الْمُؤْمِنِينَ خَدِيجَةَ رَضِيَ اللهُ عَنْهَا لَمَّا أَرَادَتْ أَنْ... Transcris tout. Le verbe après أَنْ commence-t-il par تَ ?`,
  w10: `Suite : ...عَنِ النَّبِيِّ ﷺ/صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ + تَخْوُفَهُ مِنْ حُدُوثِ/حَدَثِ نُزُولِ الْوَحْيِ. Lettre-niveau sur le mot avant نُزُولِ : ḥāʾ+dāl+wāw+thāʾ (ḥudūth) ou ḥāʾ+dāl+thāʾ (ḥadath) ?`,
  w11: `Suite : ...الْوَحْيِ، + le verbe suivant : اِتَّخَذَتْ (alif+tāʾ+shadda+khāʾ+dhāl+tāʾ marbūṭa) ou اِنْتَخَذَتْ (nūn) ? + مِنْ حُسْنِ أَخْلَاقِهِ الَّتِي (tāʾ marbūṭa) ou الَّذِي (dhāl) ? Lettre-niveau.`,
  w12: `Suite : ...اِشْتَهَرَ بِهَا قَبْلَ/فِقُلْتُ النُّبُوَّةِ دَلِيلًا عَلَى أَنَّ اللهَ لَا يُخْزِيهِ. Lettre-niveau sur le mot avant النُّبُوَّةِ : qāf+bāʾ+lām (qabla) ou autre ?`,
  w13: `Citation خديجة : إِنَّكَ لَتَصِلُ الرَّحِمَ وَتَحْمِلُ الْكَلَّ وَ...كْسِبُ/تَكْسِبُ الْمَعْدُومَ وَ...قْرِي/تَقْرِي الضَّيْفَ وَتُعِينُ عَلَى نَوَائِبِ الْحَقِّ. Lettre-niveau sur les 2 verbes contestés : le premier commence par wāw+tāʾ+ ? (kasra sous le tāʾ ? ḍamma ?) — quels diacritiques ? Et la réf entre crochets à la fin.`,
  w14: `Question : أَضَعُ عُنْوَانًا ... لِلنَّصِّ. Le mot : مُنَاسِبًا (mīm+nūn) ou مُتَاسِبًا (mīm+tāʾ) ? Lettre-niveau : combien de points sur la 2e lettre, au-dessus ?`,
  w15: `Question : أَشْرَحُ : + la liste des items séparés par des tirets. Transcris chaque item exactement : لَتَصِلُ/لِتَصِلُ الرَّحِمَ — تَحْمِلُ الْكَلَّ — تَكْسِبُ/تُكْسِبُ الْمَعْدُومَ — تَقْرِي/تُقْرَى الضَّيْفَ — نَوَائِبُ الْحَقِّ. Note les diacritiques du premier mot (fatha ou kasra sous le lām ?).`,
  w16: `Question : جَاءَ فِي النَّصِّ أَنَّ الْإِسْلَامَ + verbe. Lettre-niveau : نَظَّمَ (nūn+ẓāʾ+shadda+mīm) ou عَنَى ou autre ? + جَمِيعَ عَلَاقَاتِ الْإِنْسَانِ + suite أَذْكُرْ ثَلَاثَةً مِنْ أَنْوَاعِ هَذِهِ الْعَلَاقَاتِ مَعَ التَّمْثِيلِ.`,
  w17: `Question 4 : ...الْأَخْلَاقِ الَّتِي + verbe : اِتَّصَفَ ou اِتَّصَفَتْ ? Lettre-niveau : après فāʾ, y a-t-il un tāʾ marbūṭa (ة) ou rien ? + بِهَا رَسُولُ اللهِ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ قَبْلَ نُزُولِ الْوَحْيِ؟`,
  w18: `Début (droite) de la question 1 du التطبيق : le premier mot après « 1. » : حَثَّ (ḥāʾ+thāʾ+shadda) ou حَدَّثَ (ḥāʾ+dāl+dāl) ou autre ? Lettre-niveau : combien de points sur la 2e lettre (thāʾ=3, dhāl/khāʾ=1) ? + الْإِسْلَامُ عَلَى حُسْنِ الْخُلُقِ لَكِنْ مَعَ الْأَسَفِ قَدْ يُسِيءُ بَعْضُ النَّاسِ.`,
  w19: `Début (droite) : ... إِلَى + le mot suivant : مُحْسِنِهِ (mīm+ḥāʾ+sīn+nūn+kasra+hāʾ) ou مُحْسِنٍ إِلَيْهِ ou مُحْسِنًا ? Lettre-niveau. Puis : كَيْفَ أُقْنِعُ.`,
  w20: `Milieu : الْمُحْسِنَ إِلَى أَمْثَالِ هَؤُلَاءِ/مِثْلِ هَؤُلَاءِ أَنْ لَا يُقَابِلَ إِسَاءَتَهُمْ. Lettre-niveau sur le mot après إِلَى : alif+mīm+thāʾ+alif+lām (amthāl) ou mīm+thāʾ+lām (mithl) ?`,
  w21: `Zone complète de la question 1 du التطبيق (3-4 lignes). Transcris TOUT ce qui est imprimé dans ce fragment, y compris toute numérotation, cadre ou élément décoratif. Y a-t-il d'autres mots/numéros imprimés entre les lignes ?`,
  w22: `Titre de rubrique : الإِعْدَادُ الْقَبْلِيُّ ou الأَعْدَادُ الْقَبْلِيَّةُ ? Lettre-niveau : après الْـ : hamza+suspension ? Le 2e mot : قَبْلِيُّ (yāʾ finale) ou قَبْلِيَّةُ (tāʾ marbūṭa) ?`,
  w23: `Début : أَحْفَظُ حَدِيثَ الدَّرْسِ + le mot suivant : الْمُقْبِلِ (qāf+bāʾ) ? Lettre-niveau. Puis وَأَبْحَثُ عَنِ التَّوْجِيهَاتِ الشَّرْعِيَّةِ.`,
  w24: `Fin de ligne (gauche) : ... لِلتَّعَامُلِ مَعَ + le ou les derniers mots : الْغَضَبِ (ġayn+ḍād+bāʾ) ? Lettre-niveau. Y a-t-il un point final ou autre chose après ?`,
};

const ORDER = ['r01','r02','r03','r04','r05','r06','r07','r08','r09','r10','r11','r12','r13',
  'w01','w02','w03','w04','w05','w06','w07','w08','w09','w10','w11','w12','w13','w14','w15','w16','w17','w18','w19','w20','w21','w22','w23','w24'];

async function main() {
  const zai = await ZAI.create();
  for (const tag of ORDER) {
    const img = `${DIR}/z20-${tag}.png`;
    const out = `${DIR}/z20-${tag}.txt`;
    if (fs.existsSync(out)) { console.log(`skip ${tag}`); continue; }
    const b64 = fs.readFileSync(img).toString('base64');
    try {
      const res = await zai.createChatCompletionVision({
        messages: [{ role: 'user', content: [
            { type: 'text', text: `${COMMON}\n\n${Q[tag]}` },
            { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
        ] }],
        model: 'glm-5v-turbo',
        max_tokens: 2048,
        temperature: 0.1,
      });
      const txt = res?.choices?.[0]?.message?.content ?? JSON.stringify(res);
      fs.writeFileSync(out, txt);
      console.log(`OK ${tag} (${txt.length} car)`);
    } catch (e) {
      console.error(`ÉCHEC ${tag}: ${e.message}`);
    }
  }
}
main().catch(e => { console.error(e); process.exit(1); });
