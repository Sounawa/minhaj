import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';

// R524 — relecture VLM des zones corrompues de la leçon 23 (Kahf p.171-178, slot 761)
// + badge p.179 (leçon 24) pour trancher la continuité des plages.
const qs = [
  { img: '/home/z/my-project/tr-tmp/probe-l23-p171-badge.png',
    ask: `En-tête de page d'un manuel arabe (très zoomé). Transcris EXACTEMENT, mot à mot, chiffres arabes-orientaux exacts : (1) la ligne du badge de sourate (سورة الكهف et la plage de versets entre parenthèses) ; (2) la ligne أهداف الدرس ; (3) les trois objectifs numérotés. Format :
BADGE: <texte exact>
OBJ1: <texte>
OBJ2: <texte>
OBJ3: <texte>` },
  { img: '/home/z/my-project/tr-tmp/probe-l23-p179-badge.png',
    ask: `En-tête de page d'un manuel arabe (très zoomé). Transcris EXACTEMENT la ligne du badge de sourate : سورة الكهف et la plage de versets entre parenthèses (chiffres arabes-orientaux exacts), puis la première ligne qui suit. Format :
BADGE: <texte exact>` },
  { img: '/home/z/my-project/tr-tmp/probe-l23-p171.png',
    ask: `Page de manuel arabe (tafsīr, Dhū al-Qarnayn). Après le tamhīd se trouve un TABLEAU DE GLOSSAIRE (المفردات) dont la couche OCR est corrompue. Transcris le tableau ENTIER : chaque ligne = le mot (colonne droite) puis sa définition (colonne gauche). Inclus aussi les questions qui suivent le tableau si présentes. Format par ligne :
GLOSE: <mot> : <définition>` },
  { img: '/home/z/my-project/tr-tmp/probe-l23-p172.png',
    ask: `Page de manuel arabe. Transcris : (1) les lignes du HAUT de page (fin du glossaire : mots + définitions, avant استخلاص مضامين الآيات) ; (2) la section استخلاص مضامين الآيات (les trois questions numérotées) ; (3) les premières lignes de التفسير (اشتملت آيات الدرس على ما يأتي / أولا). Format :
GLOSE_FIN: <mot> : <définition>
QUESTION1: <texte>
QUESTION2: <texte>
QUESTION3: <texte>
TAFSIR_DEBUT: <texte>` },
  { img: '/home/z/my-project/tr-tmp/probe-l23-p173.png',
    ask: `Page de manuel arabe (tafsīr). Transcris EXACTEMENT mot à mot : (1) le passage de قال أبو حيان (commençant par وأنى...) ; (2) les deux versets comparatifs cités avec leurs références [الواقعة: ...] et [يوسف: ...] (chiffres exacts) ; (3) le passage de قال الطبري رحمه الله avec sa référence [جامع البيان: .../...] ; (4) la phrase commençant par وقوله «...» suivie de نأمره بما يسهل عليه من التكاليف ; (5) la citation d'Abū Ḥayyān [البحر المحيط: ...] avec le verset comparatif فلنينا/لينو ; (6) le début de la section ثانيا : بلوغ ذي القرنين مطلع الشمس avec le verset cité. Format :
ABU_HAYYAN1: <texte>
CIT_WAQIA: <texte + ref>
CIT_YUSUF: <texte + ref>
TABARI: <texte + ref>
WANAAMURU: <texte>
ABU_HAYYAN2: <texte + ref>
THANIYA_VERSET: <texte>` },
  { img: '/home/z/my-project/tr-tmp/probe-l23-p174.png',
    ask: `Page de manuel arabe (tafsīr, Dhū al-Qarnayn). Transcris EXACTEMENT mot à mot : (1) le verset cité contenant وجد الشمس تطلع/تشرق على قوم لم نجعل لهم من دونها سترا (après وقوله) ; (2) le verset comparatif avec sa référence [الأنعام: ...] (chiffre exact) et la note grammaticale انتصاب كلمة... ; (3) le passage de قتادة avec sa référence [الجامع لأحكام القرآن: .../...] ; (4) le passage المعنى: كما وجد أولئك... (toutes les opinions وقال) ; (5) le début de la section ثالثا avec le verset (ثم أتبع سببا) et la note grammaticale. Format :
VERSET_SETTER: <texte>
ANAM_VERSET: <texte + ref + note>
QATADA: <texte + ref>
MANAA: <texte>
THALITHA: <texte>` },
  { img: '/home/z/my-project/tr-tmp/probe-l23-p175.png',
    ask: `Page de manuel arabe (tafsīr, Dhū al-Qarnayn entre les deux barrières). Transcris EXACTEMENT mot à mot : (1) le verset cité contenant حتى إذا بلغ بين السدين وجد من دونهما قوما لا يكادون يفقهون قولا (la citation corrompue après وقوله وهو) ; (2) le verset comparatif cité après وهو كقوله تعالى ; (3) les lectures de يفقهون (حمزة والكسائي...) et le verset comparatif avec sa référence [هود: ...] ; (4) le passage sur les lectures de يأجوج ومأجوج (جمهور القراء... محمد ويعقوب...). Format :
VERSET_SADAYN: <texte>
VERSET_COMPARATIF: <texte>
LECTURES_YAFQAHUN: <texte + ref>
LECTURES_YAJUJ: <texte>` },
  { img: '/home/z/my-project/tr-tmp/probe-l23-p176.png',
    ask: `Page de manuel arabe (tafsīr, la plainte des peuples à Dhū al-Qarnayn). Transcris EXACTEMENT mot à mot : (1) le verset de la plainte : قالوا يا ذا القرنين إن يأجوج ومأجوج مفسدون في الأرض فهل نجعل لك خرجا على أن تجعل بيننا وبينهم سدا (les fragments corrompus) ; (2) le verset قال ما مكني فيه ربي خير فأعينوني بقوة أجعل بينكم وبينهم ردما ; (3) les lectures قرأ نافع وابن كثير وأبو عمرو وعاصم (خرجا/هرجا?) et قرأ حمزة والكسائي (خراجا) ; (4) la définition du ردم (والردم وضع الشيء على الشيء...). Format :
VERSET_PLAINTE: <texte>
VERSET_MAKKANI: <texte>
LECTURES_KHARAJ: <texte>
DEF_RADM: <texte>` },
  { img: '/home/z/my-project/tr-tmp/probe-l23-p177.png',
    ask: `Page de manuel arabe (tafsīr, subtilités de la leçon de Dhū al-Qarnayn). Transcris EXACTEMENT mot à mot : (1) le verset cité dans la subtilité (قوله تعالى...) ; (2) la première question d'évaluation (ما القراءات الواردة في قوله تعالى...) avec le fragment de verset cité ; (3) la troisième question d'évaluation (أستخلص قيمتين من قوله تعالى «أعينوني بقوة»...) ; (4) le début du passage de l'Imam ابن العربي avec le verset/fragment cité (وكان ملكا...). Format :
SUBTILITE_VERSET: <texte>
EVAL1: <texte>
EVAL3: <texte>
IBN_ARABI_DEBUT: <texte>` },
  { img: '/home/z/my-project/tr-tmp/probe-l23-p178.png',
    ask: `Page de manuel arabe (fin de leçon). Transcris EXACTEMENT mot à mot : (1) la fin du passage d'Ibn العربي (فأطلعت الحوادث... حتى [أحكام القرآن: .../...]) ; (2) les trois consignes après أقرأ النص بإمعان ; (3) la préparation préalable : أراجع تفسير الآيات de QUELLE PLAGE de versets (chiffres exacts) ; (4) la seconde question : المراد بالكلمات الآتية + la LISTE des mots. Format :
IBN_ARABI_FIN: <texte>
CONSIGNES: <texte>
I3DAD: <texte exact avec plage>
MOTS: <liste exacte>` },
];

async function main() {
  const zai = await ZAI.create();
  for (const q of qs) {
    const b64 = fs.readFileSync(q.img).toString('base64');
    const res = await zai.createChatCompletionVision({
      messages: [{ role: 'user', content: [
        { type: 'text', text: q.ask },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${b64}` } },
      ]}],
      model: 'glm-5v-turbo', max_tokens: 1400,
    });
    console.log('=== ' + q.img.split('/').pop() + ' ===');
    console.log(res.choices[0].message.content);
    console.log('');
  }
}
main().catch(e => { console.error('VLM_FAIL', e.message); process.exit(1); });
