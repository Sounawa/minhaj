#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-18 — vérification de la livraison hadith-5ep / pdf-16 (La circonspection envers le douteux)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-16.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-16']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-16 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon pleine)', 9000 <= len(src) <= 15000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 10, f'(h2={src.count("<h2>")})')
check('sous-sections h3', src.count('<h3>') == 5, f'(h3={src.count("<h3>")})')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Exorde', 'Le texte', 'Notice biographique du transmetteur',
       'La compréhension', 'Glossaire', 'Extraction des contenus', 'L’analyse',
       'Ce qu’il faut retirer du hadīth', 'L’évaluation', 'La valorisation',
       'La préparation de la leçon suivante']))
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
# — matière adjudiquée du manuel (Z2-18, planches pp.88-92 + composites/microcrops/zooms ×4-×6
#   + portail officiel « بوابة ابن العربي عتيق » (arbitre humain) + sources canoniques web) —
for kw in ['<h1>La circonspection envers le douteux (wara’)</h1>',
           'at-tawarru’ ’an-iš-šubuhāt', '(التَّوَرُّعُ عَنِ الشُّبُهَاتِ)',
           'onzième hadīth des Quarante', 'Seizième leçon (16) du manuel',
           'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'tamhīd', 'an-naṣṣ', 'tarǧamat ar-rāwī',
           'al-fahm', 'šarḥ', 'istikhlāṣ al-maḍāmīn', 'at-taḥlīl',
           'wamimmā yustafādu mina l-ḥadīṯ', 'at-taqwīm', 'al-istiṯmār',
           'al-a’dād al-qabliyya',
           # objectifs
           'Que je connaisse le sens des choses ambiguës',
           'Que je discerne le statut que la Loi religieuse assigne aux divers types de choses ambiguës',
           'Que je m’écarte des choses ambiguës dans mes actes d’adoration et mes transactions',
           # exorde
           'La voie de l’islam est une route blanche et éclatante',
           'Je vous ai laissés sur la voie blanche',
           'sa nuit en est comme le jour',
           'ne s’en détourne après moi que celui qui est perdu',
           '[Sunan d’Ibn Māǧa]',
           'des matières équivoques où le statut légal se brouille pour le responsable',
           'il ne distingue plus son droit de celui d’autrui, ni le licite de l’illicite',
           'tel est ce que l’on appelle les choses ambiguës',
           'Qu’entend-on donc par choses ambiguës',
           # hadith
           'Abū Muḥammad al-Ḥasan ibn ’Alī ibn Abī Ṭālib, petit-fils du Messager d’Allah',
           'J’ai retenu du Messager d’Allah',
           'Laisse ce qui te met en doute pour ce qui ne t’y met pas',
           '[Rapporté par at-Tirmiḏī et an-Nasā’ī]',
           # notice du rapporteur
           'le Qurayšite, le Hāšimite, le Médinois',
           'fils de la fille du Messager d’Allah',
           'Fāṭima az-Zahrā’',
           'le maître de la jeunesse des gens du Paradis',
           'au milieu de Ramaḍān de l’an trois de l’Hégire',
           'mourut en l’an quarante-quatre',
           'il fut enterré au',
           'le <em>sibt</em> est le fils de la fille, et le petit-fils (<em>ḥafīd</em>) le fils du fils',
           # glossaire
           '(<em>da’</em> <span dir="rtl" lang="ar">(دَعْ)</span>)',
           '(<em>yurībuka</em> <span dir="rtl" lang="ar">(يُرِيبُكَ)</span>)',
           'de <em>rāba</em> et de <em>arāba</em>',
           'dérive du doute (<em>ar-rayb</em>), qui est le soupçon',
           # extraction
           'Je détermine ce que le hadīth indique du statut de la Loi religieuse à l’égard des choses ambiguës',
           # analyse I
           'le pluriel de <em>šubha</em>',
           'toute chose qui ressemble au licite à un égard et à l’illicite à un autre',
           'le licite certain est ce dont il est su avec certitude que la propriété revient à soi',
           'l’illicite manifeste (<em>al-ḥarām al-bayyin</em>)',
           'la circonspection (<em>wara’</em>) consiste à l’éviter',
           '[’Umdat al-qārī d’al-’Aynī, adapté]',
           # analyse II
           'délaisser les choses ambiguës en raison de leur équivocité et de leur obscurité',
           'les statuts légaux se répartissent en deux classes',
           'limpide et manifeste, qui n’échappe pas à la généralité de la communauté',
           'dont il est parlé dans le hadīth des choses ambiguës précédent',
           'ce au sujet de quoi l’on n’a pas tranché d’interdiction ni de permission',
           'faute de clarté de sa preuve et par suite du désaccord des savants',
           'par prévention de l’ambiguïté',
           'abandonne ce dont tu doutes de l’interdiction parmi les propos et les actes',
           'et tourne-toi vers ce dont tu ne doutes pas parmi eux',
           '[Fatḥ al-bārī d’Ibn Raǧab, adapté]',
           'Le serviteur n’atteint pas d’être au nombre des pieux',
           'par crainte de ce qui en comporte',
           '[Sunan de at-Tirmiḏī]',
           'un degré de circonspection plus élevé que le précédent',
           # analyse III
           'Ce dont on n’est pas excusé parmi les choses ambiguës',
           'des degrés gradués selon leur proximité ou leur éloignement de l’illicite',
           'l’existence des causes de licéité et d’interdiction',
           'est-il sa propriété ou non',
           'mélange du licite et de l’illicite dans les aliments, les boissons et le reste',
           'quelque chose est-il survenu qui la rende licite',
           "qu'il est interdit à l'homme de manger avant son égorgement rituel".replace("'", '’'),
           'il ne sort de l’interdiction qu’avec la certitude de l’égorgement',
           '[Šarḥ Ṣaḥīḥ al-Buḫārī d’Ibn Baṭṭāl, adapté]',
           'Ce dont on est excusé parmi les choses ambiguës',
           'comportent le sens de l’ambiguïté sans que celle-ci s’y réalise',
           'demeure dans la permission jusqu’à ce que son interdiction soit sue avec certitude',
           'la certitude ne fait pas place au doute',
           'suggestion obsédante (<em>waswās</em>)',
           'il bâtit sur la certitude et ne prête pas attention au doute',
           'comme celui que domine le doute au sujet de la rupture de l’ablution après la purification',
           'l’homme trouve quelque chose pendant la prière',
           'doit-il interrompre la prière',
           'Non, jusqu’à ce qu’il sente une odeur ou qu’il entende un son',
           'cela s’entend de celui que le doute assaille fréquemment',
           # retraits
           'Le licite pur n’engendre pour le croyant, dans son cœur, ni soupçon ni gêne',
           'l’âme s’y apaise et le cœur s’en tranquillise',
           'les choses ambiguës, elles, engendrent le soupçon et la gêne',
           'entraîne, à plus forte raison, la circonspection à l’égard des interdictions',
           # évaluation
           'Je définis les choses ambiguës, et je donne un exemple pour chacun de leurs types',
           'Je mentionne le statut du délaissement des choses ambiguës, en l’appuyant d’une preuve',
           # valorisation (Ġazālī par Ibn Raǧab)
           'La circonspection (<em>wara’</em>) a ses divisions',
           'la circonspection des véridiques (<em>aṣ-ṣiddīqūn</em>)',
           'délaisser ce dont on ne fait pas usage sans l’intention d’en tirer force pour l’adoration',
           'la circonspection des pieux (<em>al-muttaqūn</em>)',
           'délaisser ce qui ne comporte aucune ambiguïté, mais dont on craint qu’il n’entraîne vers l’illicite',
           'la circonspection des vertueux (<em>aṣ-ṣāliḥūn</em>)',
           'la possibilité de l’interdiction — à condition que cette possibilité ait quelque poids',
           'la circonspection des obsédés',
           '[Fatḥ al-bārī, qui l’attribue à al-Ġazālī]',
           'J’extrais les types de circonspection mentionnés dans le texte',
           'lesquels comptent comme délaissement des choses ambiguës et lesquels n’y comptent pas',
           # iʿdād qablī
           'Je mémorise le hadīth de la leçon qui vient',
           'et j’accomplis ce qui suit',
           'le sens de l’occupation par ce qui ne regarde pas',
           'les méfaits de l’occupation par ce qui ne regarde pas']:
    check(f'matière: {kw[:52]}', kw in fr)

# — pose == source, garde-doublon, titleFr —
check('pose == source', fr == src, f'({len(fr)} vs {len(src)} car)')
check('titleFr correct', l.get('titleFr') == 'La circonspection envers le douteux (wara’)',
      f'({l.get("titleFr")!r})')
check('titleAr intact', l.get('titleAr') == 'التورع عن الشبهات', f'({l.get("titleAr")!r})')
check('pdfOnly toujours vrai', l.get('pdfOnly') is True)
# — cohérence série —
reg = json.load(open('/home/z/my-project/scripts-ia2/savant-registry-ia2.json', encoding='utf-8'))
check('registre IA-2 → 16', 'hadith-5ep/pdf-16' in reg['hand'] and len(reg['hand']) == 16,
      f'({len(reg["hand"])} entrées)')
# leçons 1-16 livrées, 17-29 restantes
done = [x for x in reg['hand'] if x.startswith('hadith-5ep/')]
check('série hadith-5ep : 16/29 dans le registre', len(done) == 16, f'({len(done)})')

print(f"VÉRIF pdf-16 : {len(ok)} contrôles PASS / {len(fail)} échec(s)")
for f in fail:
    print('  ÉCHEC:', f)
sys.exit(1 if fail else 0)
