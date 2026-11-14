#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-19 — vérification de la livraison hadith-5ep / pdf-17 (Délaisser ce qui ne nous regarde pas)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-17.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-17']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-17 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon pleine)', 8000 <= len(src) <= 14000, f'({len(src)} car)')
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
# — matière adjudiquée du manuel (Z2-19, planches pp.93-97 + composites + zooms ×3-×8
#   + portail officiel + sources canoniques web : Iḥyāʾ/Ghazali, Ṣaḥīḥ Ibn Ḥibbān,
#   Muwaṭṭaʾ/Luqmān, Fayḍ al-Qadīr/Mālik ibn Dīnār) —
for kw in ['<h1>Délaisser ce qui ne nous regarde pas</h1>',
           'tarku mā lā ya’nīhi', '(تَرْكُ مَا لَا يَعْنِي)',
           'douzième hadīth des Quarante', 'Dix-septième leçon (17) du manuel',
           'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'tamhīd', 'an-naṣṣ', 'tarǧamat ar-rāwī',
           'al-fahm', 'šarḥ', 'istikhlāṣ al-maḍāmīn', 'at-taḥlīl',
           'wamimmā yustafādu mina l-ḥadīṯ', 'at-taqwīm', 'al-istiṯmār',
           'al-a’dād al-qabliyya',
           # objectifs
           'Que je connaisse le sens de l’occupation par ce qui ne regarde pas',
           'les effets néfastes de l’occupation par ce qui ne regarde pas',
           'la différence entre elle et ce qui regarde',
           'Que je m’occupe de ce qui me regarde, et que je délaisse ce qui ne me regarde pas',
           # exorde
           'outrepassent les convenances dans leurs propos ou leur conduite envers autrui',
           'des nobles caractères et des beautés de la nature',
           "s'immisce dans ce qui ne le regarde pas".replace("'", '’'),
           'à dessein ou sans dessein',
           'qui tombe — ou fait tomber — dans l’embarras',
           'Qu’est-ce donc au fond que l’occupation par ce qui ne regarde pas',
           'les conséquences qui en découlent',
           # hadith
           'Il est de la beauté de l’islam d’un homme qu’il délaisse ce qui ne le regarde pas',
           '[Sunan de at-Tirmiḏī]',
           # notice
           'sa notice biographique a été donnée précédemment',
           # glossaire
           'le beau est le contraire du laid',
           'la personne',
           'ce qui ne l’importe pas, parmi les affaires de la religion et de la vie d’ici-bas',
           'l’intensité de l’attention portée à une chose',
           'il l’a pris à cœur',
           # extraction
           'J’expose, à partir du hadīth, le statut de l’islam à l’égard de ce qui ne regarde pas',
           # analyse intro
           'oriente vers l’abandon de l’occupation par ce qui ne regarde pas',
           'ce dont l’homme n’a pas besoin et auquel nulle nécessité ne le lie',
           'ni utilité ni intérêt qui le requière',
           # premièrement
           'un bienfait (<em>iḥsān</em>) qui compte pour un degré élevé dans l’islam',
           'voilà le bienfaiteur véritable',
           'réalisé son islam en son extérieur comme en son intérieur',
           # deuxièmement
           'dommages graves et des suites funestes',
           'la dilapidation du temps précieux, impossible à compenser',
           'une grâce immense et une faveur très grande',
           'des laideurs des états de l’homme que de s’occuper de ce qui ne le regarde pas',
           'dont le perdu ne peut être compensé en ce pour quoi l’homme n’a pas été créé',
           '[Šarḥ az-Zarqānī sur le <em>Muwaṭṭa’</em>]',
           'la négligence dans l’accomplissement des obligations',
           'le moyen de délaisser ce qui regarde',
           'pour issue le regret',
           'entendre ce qui lui déplaît',
           'ce dont la suite n’est pas louée',
           'la dureté du cœur, à l’affaiblissement du corps et au resserrement de la subsistance',
           'Mālik ibn Dīnār',
           'une dureté dans ton cœur, une faiblesse dans ton corps et une privation dans ta subsistance',
           'tu as parlé de ce qui ne te regarde pas',
           '[Fayḍ al-Qadīr d’al-Munāwī]',
           # salaf
           'Les vertueux des premières générations',
           'de nombreux récits ont été transmis d’eux',
           'la parole d’Abū Ḏarr',
           'compte sa parole au nombre de ses actes',
           'sa parole se fait rare, sinon en ce qui le regarde',
           '[Ṣaḥīḥ d’Ibn Ḥibbān]',
           'il fut dit à Luqmān',
           'Qu’est-ce qui t’a valu ce que nous voyons',
           'on voulait parler de son mérite',
           'La véracité du propos, l’acquittement du dépôt, et le délaissement de ce qui ne me regarde pas',
           '[al-Muwaṭṭa’]',
           'al-Ḥasan al-Baṣrī',
           'qu’Allah le Très-Haut détourne Son attention du serviteur',
           # troisièmement
           'de s’occuper de ce qui le regarde parmi les affaires',
           'l’œuvre droite',
           'satiété et désaltèrement',
           'couverture de la nudité, chasteté du sexe',
           'de quoi la nécessité est satisfaite, sans superflu d’aisance',
           'préservé de l’ensemble des maux',
           'pour sa religion et pour son au-delà',
           'en ayant présent à l’esprit Sa proximité de son Seigneur',
           'a réalisé la beauté de son islam',
           # retraits
           'le bien, la rectitude et le profit pour l’homme',
           'afin qu’il ne gaspille pas sa vie dans les futilités',
           # évaluation
           'certaines des conséquences qui découlent de l’occupation par ce qui ne regarde pas',
           'Que retire-t-on de l’exhortation de l’islam à l’occupation par ce qui regarde',
           'des exemples de ce qui regarde l’homme et de ce qui ne le regarde pas',
           # valorisation (Ġazālī)
           'La définition de ce qui, dans la parole, ne te regarde pas',
           'si tu t’en taisais, tu n’encourrais ni faute ni dommage',
           'ni à l’immédiat ni à terme',
           'tu dilapides ton temps et tu auras à rendre compte de l’activité de ta langue',
           'tu échanges ce qui est moindre contre ce qui est meilleur',
           'l’évocation d’Allah et à l’invocation',
           'des effusions d’Allah, ce dont le profit est immense',
           'un trésor des trésors du Paradis',
           'prend à sa place une bourse (<em>badra</em>) est perdant',
           '[Dalīl al-fāliḥīn li-ṭuruqi Riyāḍ aṣ-ṣāliḥīn, qui l’attribue à al-Ġazālī]',
           'le critère de l’occupation par ce qui ne regarde pas',
           # iʿdād qablī
           'Je mémorise le hadīth de la leçon qui vient',
           'et j’accomplis ce qui suit',
           'le mérite de l’amour du bien pour les gens',
           'certaines des manifestations de l’amour du bien pour les gens']:
    check(f'matière: {kw[:52]}', kw in fr)

# — pose == source, garde-doublon, titleFr —
check('pose == source', fr == src, f'({len(fr)} vs {len(src)} car)')
check('titleFr intact', l.get('titleFr') == 'Délaisser ce qui ne nous regarde pas',
      f'({l.get("titleFr")!r})')
check('titleAr intact', l.get('titleAr') == 'ترك ما لا يعني', f'({l.get("titleAr")!r})')
check('pdfOnly toujours vrai', l.get('pdfOnly') is True)
# — cohérence série —
reg = json.load(open('/home/z/my-project/scripts-ia2/savant-registry-ia2.json', encoding='utf-8'))
check('registre IA-2 → 17', 'hadith-5ep/pdf-17' in reg['hand'] and len(reg['hand']) == 17,
      f'({len(reg["hand"])} entrées)')
done = [x for x in reg['hand'] if x.startswith('hadith-5ep/')]
check('série hadith-5ep : 17/29 dans le registre', len(done) == 17, f'({len(done)})')

print(f"VÉRIF pdf-17 : {len(ok)} contrôles PASS / {len(fail)} échec(s)")
for f in fail:
    print('  ÉCHEC:', f)
sys.exit(1 if fail else 0)
