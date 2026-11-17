#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-23 — vérification de la livraison hadith-5ep / pdf-20 (Consolidation et application)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-20.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-20']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-20 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon de consolidation)', 4500 <= len(src) <= 8000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 6, f'(h2={src.count("<h2>")})')
check('pas de h3 (leçon sans sous-sections)', src.count('<h3>') == 0, f'(h3={src.count("<h3>")})')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Le texte', 'La compréhension', 'L’analyse',
       'L’application', 'La préparation de la leçon suivante']))
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 demi-anneau (U+02BF/02BE)', '\u02bf' not in src and '\u02be' not in src)
check('0 point-virgule vertical (U+FE14)', '\ufe14' not in src)
check('0 double tiret résiduel', '——' not in src)
check('0 double entité &nbsp;', '&nbsp;&nbsp;' not in src)
check('0 U+00A0 littéral', '\u00a0' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?', src))
# — matière adjudiquée du manuel (Z2-23, pp.111-113 + composites 600 dpi A-C +
#   bandes r ×1.6-×3 + recadrages w + série N étroite ×2.5-×5 lettre-analyzed +
#   couche bbox + canonique Ṣaḥīḥ al-Buḫārī ḥadīth 3) —
for kw in ['<h1>Consolidation et application</h1>',
           'da’m wa-taṭbīq', '(دَعْمٌ وَتَطْبِيقٌ)',
           'vingtième leçon (20) du manuel',
           'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'an-naṣṣ', 'al-fahm', 'at-taḥlīl', 'at-taṭbīq',
           'al-’i’dād al-qabliyy',
           # objectifs (r01 : أقوم مكتسباتي / أقف على قدراتي / أطبق ما اكتسبته)
           'Que je fasse le bilan de mes acquis des leçons précédentes',
           'Que je mesure mes capacités dans l’apprentissage',
           'Que je mette en pratique ce que j’ai acquis dans des situations nouvelles',
           # النص §1 (w04 أَبْعَدَ مِنْ ذَلِكَ + n05 إِخْوَةً letter-analyzed)
           'sociable par nature', '(اجْتِمَاعِيٌّ بِطَبْعِهِ)',
           'l’islam a organisé ces relations en tous leurs genres',
           'l’exhortation au beau traitement d’autrui, la bienfaisance envers le voisin et l’honneur fait à l’hôte',
           'L’islam est même allé plus loin encore',
           'comme des frères', '(إِخْوَةً)',
           'nulle différence entre l’arabe et le non-arabe sinon par la piété',
           'Ô hommes', 'pour que vous vous connaissiez',
           'Le plus noble d’entre vous, auprès de Dieu, est le plus pieux d’entre vous',
           '[al-Ḥuǧurāt\u202f: 13]',
           # النص §2 (n02 الدَّالَّةِ letter-analyzed + w06 وَلَنَا + w07 الْمَثَلُ الْأَعْلَى + w08 مَدَّحَهُ)
           'au nombre des signes de la foi qui attestent sa perfection',
           'un beau modèle', '(أُسْوَةٌ حَسَنَةٌ)',
           'le modèle suprême dans la bienfaisance envers autrui',
           'l’a loué pour cela',
           'Et certes, tu es d’une moralité immense', '[al-Qalam\u202f: 4]',
           # النص §3 خديجة (n23 تَخَفَّفَ + n17 قَبْلَ + n13 وَتُكْسِبُ + r07 يُخْزِيكَ canonique)
           'la Mère des croyants Khadīǧa',
           'voulut apaiser le Prophète',
           'l’effroi que lui causa la survenue de la révélation',
           'dont il s’était rendu célèbre avant la prophétie',
           'que Dieu ne l’exposerait jamais au déshonneur',
           'Certes non, par Dieu', 'Dieu ne t’exposera jamais au déshonneur',
           'tu maintiens les liens du sang', 'tu prends en charge le faible',
           'tu procures au démuni', 'tu honores l’hôte',
           'tu portes secours aux épreuves du droit',
           '[Ṣaḥīḥ d’al-Buḫārī]',
           # الفهم (w14 مُنَاسِبًا + n15 glossaire : تُكْسِبُ ḍamma + تُقْرَى fatha — imprimés)
           'Je propose un titre convenable au texte',
           'J’explique',
           '(لِتَصِلَ الرَّحِمَ)', '(تَحْمِلُ الْكَلَّ)',
           '(تُكْسِبُ الْمَعْدُومَ)', '(تُقْرَى الضَّيْفَ)', '(نَوَائِبُ الْحَقِّ)',
           # التحليل (w16 نَظَّمَ + n20 ثَلَاثًا letter-analyzed + r10 أستدل + w11 الَّتِي)
           'que l’islam a organisé toutes les relations de l’homme',
           'je cite trois sortes de ces relations, avec des exemples',
           'par des textes scripturaires', '(بِنُصُوصٍ شَرْعِيَّةٍ)',
           'la bienfaisance envers le voisin — l’honneur fait à l’hôte — l’amour du bien pour les gens',
           'J’extrais de la parole de la Mère des croyants Khadīǧa',
           'les nobles caractères dont se parait le Messager d’Allah',
           'avant la descente de la révélation',
           # التطبيق (n06 حَدَّثَ imprimé + n08 أُقْنِعُ الْمُحْسِنَ + n09 يَقْطَعَ + couche لِيَ)
           'L’islam a appelé à l’excellence du caractère', '(حُسْنِ الْخُلُقِ)',
           'comment convaincre celui qui fait du bien envers tels gens',
           'de ne pas répondre à leur offense par une autre offense',
           'ni même d’interrompre pour autant sa bienfaisance à leur égard',
           'maîtriser les membres', '(ضَبْطُ الْجَوَارِحِ)',
           'en m’appuyant sur les preuves qui m’ont été facilitées',
           # الإعداد القبلي (w22 singulier + w23 التَّوْجِيهَاتِ + w24 الْغَضَبِ)
           'Je mémorise le hadīth de la leçon à venir',
           'orientations religieuses', '(التَّوْجِيهَاتِ الشَّرْعِيَّةِ)',
           'pour traiter la colère', '(الْغَضَبِ)',
           ]:
    check(f'kw « {kw[:48]} »' if len(kw) > 48 else f'kw « {kw} »', kw in src)
# — matière sur le JSON MONTÉ —
check('htmlFr monté non vide', len(fr) > 4000, f'({len(fr)} car)')
check('htmlFr monté = fichier source', fr.strip() == src.strip(), f'({len(fr)} vs {len(src)} car)')
check('titleFr conservé', l.get('titleFr') == 'Consolidation et application', f"({l.get('titleFr')})")
check('titleAr conservé', l.get('titleAr') == 'دعم وتطبيق', f"({l.get('titleAr')})")
check('pdfOnly conservé', str(l.get('pdfOnly')) == 'True')
check('leçons voisines intactes', all(any(li['docId'] == d and len(li.get('htmlFr') or '') > 5000
      for li in book['lessons']) for d in ('pdf-18', 'pdf-19')))

print(f"{len(ok)} contrôles OK / {len(fail)} échec(s)")
for f_ in fail:
    print('ÉCHEC :', f_)
sys.exit(1 if fail else 0)
