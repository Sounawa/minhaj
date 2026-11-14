#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-17 — vérification de la livraison hadith-5ep / pdf-15 (Le licite et l'exaucement de l'invocation)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-15.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-15']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-15 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon pleine)', 9000 <= len(src) <= 15000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 10, f'(h2={src.count("<h2>")})')
check('sous-sections h3', src.count('<h3>') == 4, f'(h3={src.count("<h3>")})')
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
# — matière adjudiquée du manuel (Z2-17, planches pp.83-87 + composites/microcrops v1-v4) —
for kw in ['<h1>Le licite et l’exaucement de l’invocation</h1>',
           'al-ḥalāl wa-ijābatu d-du’ā’', '(الْحَلَالُ وَإِجَابَةُ الدُّعَاءِ)',
           'dixième hadīth des Quarante', 'Quinzième leçon (15) du manuel',
           'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'tamhīd', 'an-naṣṣ', 'tarǧamat ar-rāwī',
           'al-fahm', 'šarḥ', 'istikhlāṣ al-maḍāmīn', 'at-taḥlīl',
           'wamimmā yustafādu mina l-ḥadīṯ', 'at-taqwīm', 'al-istiṯmār',
           'al-a’dād al-qabliyya',
           # objectifs
           'Que je connaisse les causes de l’exaucement de l’invocation',
           'Que je discerne le lien du gain licite avec l’exaucement de l’invocation',
           'Que j’évite les empêchements de l’exaucement de l’invocation',
           'jusqu’à être un homme dont l’invocation est exaucée',
           # exorde
           'a ordonné à Ses serviteurs l’invocation',
           'Et votre Seigneur a dit&nbsp; : Implorez-Moi, Je vous répondrai',
           'ceux qui, par orgueil, dédaignent de M’adorer entreront bientôt dans la Géhenne, humiliés',
           '(Sourate Ġāfir — verset 60)',
           'certaines personnes insistent dans l’invocation sans voir l’effet de l’exaucement',
           'Quelles sont donc les causes de l’exaucement de l’invocation',
           # hadith central (Muslim 1015)
           'Certes Allah, le Très-Haut, est bon et n’accepte que ce qui est bon',
           'et certes Allah a ordonné aux croyants ce qu’Il a ordonné aux Messagers',
           'Ô Messagers, mangez des choses excellentes et œuvrez avec droiture',
           '(Sourate al-Mu’minūn — verset 52)',
           'Ô vous qui croyez, mangez des excellentes choses que Nous vous avons attribuées',
           '(Sourate al-Baqara — verset 171)',
           'Puis il mentionna l’homme qui prolonge le voyage, ébouriffé, couvert de poussière',
           'tendant ses deux mains vers le ciel — Seigneur',
           'sa nourriture est illicite, sa boisson illicite, son vêtement illicite',
           'et qu’il a été nourri d’illicite&nbsp; : comment donc serait-il exaucé',
           '[Ṣaḥīḥ de Muslim]',
           # notice
           'sa notice biographique a été donnée précédemment',
           # glossaire
           'le bon est le contraire du vil',
           'transcendant au-dessus des imperfections et des défauts',
           'ce qui est exempt d’illicite',
           'ce qui est exempt de ce qui corrompt',
           'dont le teint est altéré par l’effet de la poussière',
           'les élève, par l’invocation, vers Allah',
           'son corps s’est nourri d’illicite',
           'de quelle manière serait-il exaucé, lui',
           'il n’est pas digne d’être exaucé',
           'ṭayyib', 'ṭayyiban', 'aġbar', 'yamuddu yadayhi', 'ġuḏiya',
           'fa-annā yustajābu li-ḏālika',
           '(إِنَّ اللهَ طَيِّبٌ)', '(طَيِّبًا)', '(أَغْبَرَ)', '(يَمُدُّ يَدَيْهِ)',
           '(غُذِيَ)', '(فَأَنَّى يُسْتَجَابُ لِذَلِكَ)',
           # maḍāmīn
           'J’extrais du hadīth les causes de l’exaucement de l’invocation',
           'J’expose, à partir du hadīth, les empêchements de l’exaucement',
           # analyse — premièrement
           'dont certaines sont obligatoires et d’autres recommandées',
           'les réunir au moment de l’invocation est ce qu’il y a de plus excellent et de plus indiqué',
           'Au nombre des causes obligatoires figure ce à quoi a exhorté le Prophète',
           'Le hadīth exhorte au gain tiré du licite excellent et à la dépense qui en provient',
           'proscrit le gain tiré de l’illicite vil',
           'doit être tout entier licite, pur, sans aucun soupçon',
           'dépensez des choses excellentes que vous avez gagnées',
           'de ce que Nous avons fait sortir pour vous de la terre',
           '(Sourate al-Baqara — verset 266)',
           'Et ne visez pas le vil pour en faire dépense',
           'Il est rapporté dans le hadīth',
           'le Prophète — prière et salut d’Allah sur lui — a ainsi montré',
           'de manger du licite, de même qu’Il l’a ordonné aux Messagers',
           # analyse — deuxièmement
           'Au nombre des causes recommandées figure',
           'élever les deux mains vers le ciel au moment de l’invocation',
           'il tend ses deux mains vers le ciel',
           'élevait les mains dans la prière de demande de pluie',
           'le blanc de ses aisselles',
           'Ṣaḥīḥ de al-Buḫārī',
           'l’insistance auprès d’Allah le Très-Haut par la louange qui Lui est adressée',
           'l’évocation de la faveur de Sa générosité et de Ses bienfaits',
           # analyse — mawāniʿ
           'Au nombre des empêchements qui font obstacle à l’exaucement',
           'consommer de l’illicite par la nourriture, la boisson ou l’habillement',
           'C’est là tenir l’exaucement de son invocation pour improbable',
           'par pure faveur, par ménagement et par générosité',
           'istidrāǧ',
           'l’amenée insidieuse du châtiment',
           'l’insouciance d’Allah le Très-Haut',
           'Ǧāmi’', 'at-Tirmiḏī',
           'Implorez Allah en ayant la certitude de l’exaucement',
           'n’exauce pas l’invocation proférée par un cœur insoucieux et distrait',
           '[Sunan de at-Tirmiḏī]',
           # yustafād
           'la nécessité de réunir les causes de l’exaucement',
           'au premier chef desquelles la consommation du licite',
           'Le recours à Allah, l’humilité suppliante et l’insistance dans l’invocation',
           'Le gain licite relève de la conduite des Messagers et des serviteurs vertueux d’Allah',
           # taqwīm
           'Quel est le lien du gain licite avec l’exaucement de l’invocation',
           'Je mentionne certaines des règles de bienséance de l’invocation',
           # istiṯmār (Ṭabarānī, Ibn ʿAbbās)
           'D’après Ibn ’Abbās — qu’Allah soit satisfait de lui et de son père',
           'ce verset fut récité devant le Messager d’Allah',
           'Ô gens, mangez de ce qui est licite et excellent sur terre',
           '(Sourate al-Baqara — verset 167)',
           'Sa’d ibn Abī Waqqāṣ se leva alors et dit',
           'implore Allah qu’Il me fasse l’un de ceux dont l’invocation est exaucée',
           'Ô Sa’d, purifie ce que tu manges&nbsp; : ton invocation sera exaucée',
           'Par Celui qui détient l’âme de Muḥammad en Sa main',
           'une bouchée d’illicite, nulle action n’est acceptée de lui pendant quarante jours',
           'dont la chair s’est développée d’un bien illicitement acquis',
           'le Feu a plus de droit sur lui',
           '[al-Mu’ǧam al-awsaṭ de aṭ-Ṭabarānī]',
           'J’extrais du texte ce qui met en évidence l’importance de la consommation du licite',
           # iʿdād qablī
           'Je mémorise le hadīth de la leçon qui vient',
           'la notice biographique de al-Ḥasan ibn ’Alī',
           'le sens des choses ambiguës',
           'šubuhāt']:
    check(f'matière: {kw[:52]}', kw in fr)

# — pose == source, garde-doublon, titleFr —
check('pose == source', fr == src, f'({len(fr)} vs {len(src)} car)')
check('titleFr correct', l.get('titleFr') == 'Le licite et l’exaucement de l’invocation',
      f'({l.get("titleFr")!r})')
check('titleAr intact', l.get('titleAr') == 'الحلال وإجابة الدعاء', f'({l.get("titleAr")!r})')
check('pdfOnly toujours vrai', l.get('pdfOnly') is True)
# — cohérence série —
reg = json.load(open('/home/z/my-project/scripts-ia2/savant-registry-ia2.json', encoding='utf-8'))
check('registre IA-2 → 15', 'hadith-5ep/pdf-15' in reg['hand'] and len(reg['hand']) == 15,
      f'({len(reg["hand"])} entrées)')
# leçons 1-15 livrées, 16-29 restantes
done = [x for x in reg['hand'] if x.startswith('hadith-5ep/')]
check('série hadith-5ep : 15/29 dans le registre', len(done) == 15, f'({len(done)})')

print(f"VÉRIF pdf-15 : {len(ok)} contrôles PASS / {len(fail)} échec(s)")
for f in fail:
    print('  ÉCHEC:', f)
sys.exit(1 if fail else 0)
