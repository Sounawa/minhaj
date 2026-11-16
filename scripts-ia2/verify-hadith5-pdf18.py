#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-20 — vérification de la livraison hadith-5ep / pdf-18 (Aimer le bien pour les gens)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-18.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-18']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-18 unique', len(les) == 1, f'({len(les)} occurrences)')
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
# — matière adjudiquée du manuel (Z2-20, pp.98-103 + composites 600 dpi A-F + microcrops
#   bbox ×2-×3 + sources canoniques web : Jāmiʿ al-ʿUlūm/Ibn Raǧab, Ṣaḥīḥ Ibn Ḥibbān,
#   Fatḥ al-Bārī d'Ibn Raǧab 1/45, Ṣaḥīḥ Muslim) —
for kw in ['<h1>Aimer le bien pour les gens</h1>',
           'maḥabbatu l-ḫayri li-n-nās', '(مَحَبَّةُ الْخَيْرِ لِلنَّاسِ)',
           'treizième hadīth des Quarante', 'Dix-huitième leçon (18) du manuel',
           'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'tamhīd', 'an-naṣṣ', 'tarǧamat ar-rāwī',
           'al-fahm', 'šarḥ', 'istikhlāṣ al-maḍāmīn', 'at-taḥlīl',
           'wamimmā yustafādu mina l-ḥadīṯ', 'at-taqwīm', 'al-istiṯmār',
           'al-a’dād al-qabliyya',
           # objectifs (A1 + m1 : أتعرف / أدرك letter-analyzed d-r-k / أحبّ)
           'Que je connaisse le sens de l’amour du bien pour les gens',
           'Que je saisisse les manifestations de l’amour du bien pour les gens',
           'Que j’aime pour les gens ce que j’aime pour moi-même',
           # exorde (m2/m15/m16/m17/m18)
           'la sagesse de Dieu — Puissant et Majestueux —',
           'différents quant à la couleur, la langue et l’origine',
           'égaux dans l’origine de la création, tous issus d’Adam',
           'des liens solides, dont l’islam a exhorté d’édifier l’ouvrage',
           'que tu aimes pour ton frère ce que tu aimes pour toi-même',
           'ses manifestations, celles qui le traduisent en actes',
           # hadith (A3 ×2 lectures concordantes)
           'Abū Ḥamza Anas ibn Mālik — que Dieu le Très-Haut soit satisfait de lui —, le serviteur du Messager d’Allah',
           '«\u202fNul d’entre vous n’a la foi tant qu’il n’aime pour son frère ce qu’il aime pour lui-même\u202f» [Ṣaḥīḥ d’al-Buḫārī et Muslim]',
           # notice (B1 + m4 + m19 : واغفر ذنبه letter-analyzed)
           'Anas ibn Mālik ibn an-Naḍr al-Anṣārī an-Naǧǧārī al-Ḫazraǧī',
           'surnommé (<em>kunyā</em>) Abū Ḥamza',
           'qu’il servit dix années',
           'celui qui eut le plus d’enfants',
           '«\u202fÔ Allah, bénis sa richesse et sa descendance, prolonge son existence et pardonne sa faute\u202f» [unanimement rapporté',
           'un verger dont la charge était portée deux fois l’an',
           'le dernier des Compagnons à mourir à Bassora',
           'quatre-vingt-dix, ou quatre-vingt-onze, ou quatre-vingt-douze, ou quatre-vingt-treize',
           'selon la divergence des transmetteurs',
           # glossaire (B2 + m5)
           'lā yu’minu', '(لَا يُؤْمِنُ)', 'sa foi n’est pas complète',
           'yuḥibbu', '(يُحِبُّ)',
           'l’inclinaison vers ce qui s’accorde à celui qui aime',
           'l’espoir du bien pour lui',
           # extraction (m6 + convention série أُحَدِّدُ/أُبَيِّنُ مِنَ)
           'Je détermine le sens de «\u202faimer pour son frère ce qu’il aime pour lui-même\u202f»',
           'J’expose, à partir du hadīth, l’aspect de l’exhortation à vouloir le bien des gens',
           # analyse — intro + axes
           'Le hadīth appelle à l’amour du bien pour les gens',
           'trois axes suivants',
           '’awwalan&nbsp;\u202f: ma’nā maḥabbati l-ḫayri li-n-nās',
           '(أَوَّلًا: مَعْنَى مَحَبَّةِ الْخَيْرِ لِلنَّاسِ)',
           'ṯāniyan&nbsp;\u202f: faḍlu maḥabbati l-ḫayri li-n-nās',
           '(ثَانِيًا: فَضْلُ مَحَبَّةِ الْخَيْرِ لِلنَّاسِ)',
           'ṯāliṯan&nbsp;\u202f: maẓāhiru maḥabbati l-ḫayri li-n-nās',
           '(ثَالِثًا: مَظَاهِرُ مَحَبَّةِ الْخَيْرِ لِلنَّاسِ)',
           # أولاً (C1/C2 + Fuḍayl canonique Jāmiʿ Ibn Raǧab)
           'une générosité de l’âme',
           'des impétuosités psychiques',
           'l’envie, l’égoïsme, l’accaparement (<em>isti’ṯār</em>)',
           'une formule plus profonde et plus frappante',
           'version d’an-Nasā’ī',
           '«\u202fNul d’entre vous n’a la foi tant qu’il n’aime pour son frère, du bien, ce qu’il aime pour lui-même\u202f»',
           'la foi de nul d’entre vous n’est complète tant qu’il n’aime pour son frère, en islam, le bien qu’il aime pour lui-même',
           'à son degré le plus bas, en aimant pour autrui l’obtention de pareil à ce que l’on a soi-même obtenu',
           'aimer pour les gens plus que ce que l’on est soi-même',
           'al-Fuḍayl ibn ’Iyāḍ dit à Sufyān ibn ’Uyayna',
           '«\u202fSi tu aimes que les gens soient ton pareil, tu n’as pas acquitté le conseil sincère envers ton Seigneur&nbsp;\u202f;',
           'comment, alors que tu aimes qu’ils soient au-dessous de toi&nbsp;\u202f?&nbsp;\u202f»',
           'se hâte de rendre justice à son frère contre lui-même',
           'dût-il en coûter quelque peine',
           # ثانياً (C4/D1/D2 + Ibn Ḥibbān web : يبلغ letter-analyzed m8)
           'une place considérable, qui se manifeste en ceci',
           'des caractères de la foi, et même de ses obligations',
           '«\u202fNul serviteur n’atteint la réalité de la foi tant qu’il n’aime pour les gens le bien qu’il aime pour lui-même\u202f» [Ṣaḥīḥ d’Ibn Ḥibbān]',
           'quant au fondement de la foi, il est acquis sans cette qualité',
           'préservé de l’envie, de la rancune (<em>ġill</em>), de la tromperie, du ressentiment (<em>ḥiqd</em>) et de l’égoïsme',
           '«\u202fVous n’entrerez pas au Paradis tant que vous n’aurez pas cru, et vous ne croirez pas tant que vous ne vous serez pas aimés…&nbsp;\u202f» [as-Sunan al-kubrā d’al-Bayhaqī]',
           'la pureté du cœur à l’égard du ressentiment, de l’envie et de leurs pareilles',
           'signe de la droiture du cœur et de la perfection de la foi',
           # ثالثاً (D3/D4 + m9/m10)
           'des manifestations et des signes qui attestent',
           'qu’il s’éjouit de sa joie&nbsp;\u202f: ce qui réjouit son frère le réjouit',
           'qu’il s’attriste de sa tristesse&nbsp;\u202f: ce qui afflige son frère l’afflige',
           'hadith d’an-Nu’mān ibn Bašīr',
           '«\u202fLes croyants, dans leur amour mutuel, leur tendresse et leur compassion, sont à la manière d’un seul corps',
           'par la fièvre et par la veille\u202f» [al-Buḫārī et Muslim]',
           'qu’il le traite comme il aime être traité lui-même',
           '«\u202f… quiconque aime être éloigné du Feu et introduit au Paradis, que sa mort le trouve croyant en Allah et au Jour dernier, et qu’il apporte aux gens ce qu’il aime qu’on lui apporte\u202f» [Ṣaḥīḥ de Muslim]',
           # يُستفاد (m11/m12/m13/m28)
           'comme une seule et même âme',
           'Les liens de l’amour et de la fraternité édifient une communauté soudée',
           'la sécurité et la paix',
           'la sérénité (<em>sakīna</em>) et la tranquillité de l’âme',
           'L’harmonie des cœurs des gens, le bon ordre de leurs états',
           'du principe de la coexistence',
           # تقويم (m24/E2)
           's’oppose-t-il à ce que l’homme aime pour lui-même comme bien',
           'l’effet de la volonté du bien des gens sur l’individu et sur la société',
           # استثمار (E3 + web Fatḥ al-Bārī 1/45)
           'L’imam aš-Šāfi’ī a dit',
           'apprennent cette science, sans qu’il m’en soit rien attribué',
           '[Fatḥ al-Bārī d’Ibn Raǧab]',
           'le type d’amour dont le texte fait état',
           'l’effet de ce type d’amour sur la société',
           # إعداد قبلي (F1 ×3 concordantes : والضيف)
           'Je mémorise le hadīth de la leçon qui vient',
           'la maîtrise des membres (<em>ḍabṭ al-ǧawāriḥ</em>) selon la Loi religieuse',
           'le rapport de la foi à l’honoration du voisin et de l’hôte',
           ]:
    check(f'motif « {kw[:58]}… »' if len(kw) > 58 else f'motif « {kw} »', kw in src)
# — registre —
check('pose == source', fr == src, f'({len(fr)} car registre vs {len(src)} car source)')
check('titleFr conservé', l.get('titleFr') == 'Aimer le bien pour les gens',
      f"({l.get('titleFr')!r})")
lessons_done = sum(1 for x in book['lessons'] if x.get('htmlFr'))
check('registre 18/29', lessons_done == 18, f'({lessons_done}/29)')

print(f"\n=== VÉRIFICATION pdf-18 : {len(ok)} OK / {len(fail)} ÉCHEC ===")
for f_ in fail:
    print('ÉCHEC :', f_)
sys.exit(1 if fail else 0)
