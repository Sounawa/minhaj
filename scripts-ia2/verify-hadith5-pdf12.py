#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-14 — vérification de la livraison hadith-5ep / pdf-12 (La religion, c'est le conseil sincère)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-12.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-12']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-12 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon 5 pages)', 9000 <= len(src) <= 16000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 10, f'(h2={src.count("<h2>")})')
check('sous-sections h3', src.count('<h3>') == 5, f'(h3={src.count("<h3>")})')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Exorde', 'Le texte', 'Notice biographique du transmetteur',
       'La compréhension', 'Glossaire', 'Extraction des contenus', 'L’analyse',
       'Premièrement', 'Deuxièmement', 'Troisièmement',
       'Ce qu’il faut retirer du hadīth', 'L’évaluation', 'La valorisation',
       'La préparation de la leçon suivante']))
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 demi-anneau ayn (U+02BF/02BE)', '\u02bf' not in src and '\u02be' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?', src))
# — matière adjudiquée du manuel (Z2-14, planches p69-73 + composites 600 dpi A→Y) —
for kw in ['<h1>La religion, c’est le conseil (naṣīḥa)</h1>',
           'an-naṣīḥa', '(الدِّينُ النَّصِيحَةُ)',
           'Douzième leçon (12) du manuel', 'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'tamhīd', 'an-naṣṣ', 'tarǧamat ar-rāwī',
           'al-fahm', 'istikhlāṣ al-maḍāmīn', 'at-taḥlīl', 'at-taqwīm',
           'al-istiṯmār', 'al-a’dād al-qabliyya',
           'du septième hadīth des Quarante',
           'Abū Ruqayya Tamīm ibn Aws ad-Dārī',
           'son statut juridique et son rang',
           'Que je m’applique à suivre la Sunna dans le conseil et la consultation',
           'la personne consultée donne à celle qui l’a consultée',
           'son sens est plus ample que cela',
           'englober la religion tout entière',
           'la fidélité aux promesses, le respect des contrats et la belle moralité',
           'le principe de la fraternité entre croyants exige le conseil mutuel',
           'La religion, c’est le conseil sincère',
           'Envers qui, ô Messager d’Allah',
           'Envers Allah, envers Son Livre, envers Son Messager',
           'les dirigeants des musulmans et leur ensemble',
           'Ṣaḥīḥ de Muslim',
           'Tamīm ibn Aws ibn Ḫāriǧa ad-Dārī al-Laḫmī',
           'Benū ad-Dār', 'Laḫm',
           'avec son frère <em>Nu’aym</em>', 'en l’an neuf de l’Hégire',
           'le premier à allumer les lampes dans la mosquée',
           'le premier à faire le récit édifiant', 'qaṣaṣ',
           'au temps de <em>’Umar</em>', 'dont il fut l’initiateur',
           'il fabriqua le minbar du Prophète',
           'l’ascète (<em>rāhib</em>) des gens de Palestine',
           'Il mourut en l’an quarante de l’Hégire',
           'al-Ḫalīl', 'que ce seul hadīth',
           'est le pluriel de',
           'les détenteurs de l’autorité de leurs affaires',
           'la communauté tout entière',
           'Je dégage du hadīth le sens général de la recommandation sincère',
           'ma’nā an-naṣīḥa', '(أَوَّلًا: مَعْنَى النَّصِيحَة)',
           'j’ai purifié le miel', 'quand on l’a débarrassé de sa cire',
           'comme le miel est purifié de sa cire',
           'l’acception coutumière',
           'la pureté de l’avis et sa purification de toute fraude envers celui qui consulte',
           'le privilège donné à son intérêt',
           'obtienne tout le bien et se préserve de tout le mal',
           'ahammīyyat an-naṣīḥa', '(ثَانِيًا: أَهَمِّيَّةُ النَّصِيحَة)',
           'un mot englobant (<em>ǧāmi’a</em>)',
           'assurer à celui que l’on conseille sa part de bien',
           'vouloir l’entièreté du bien pour lui',
           'noms les plus concis', 'formules les plus ramassées',
           'dans la langue des Arabes',
           'qui suffise à exprimer le sens de ce mot',
           'la religion se trouve contenue en elle',
           'La religion est tout entière conseil',
           'ce qui est entre le serviteur et son Seigneur',
           'les hommes tous ensemble',
           'li-man an-naṣīḥa wa-bi-mā takūn',
           '(ثَالِثًا: لِمَنْ النَّصِيحَةُ وَبِمَ تَكُونُ)',
           'an-naṣīḥa li-llāh ta’ālā', '(النَّصِيحَةُ لِلَّهِ تَعَالَى)',
           'à ne rien Lui associer',
           'les attributs de perfection et de majesté',
           'à aimer et à détester à cause de Lui',
           'à puiser dans Ses bienfaits et à Le remercier pour eux',
           'un conseil que le serviteur se donne à lui-même',
           'Allah peut se passer du conseil des conseillers',
           'an-naṣīḥa li-kitāb Allāh ta’ālā',
           '(النَّصِيحَةُ لِكِتَابِ اللهِ تَعَالَى)',
           'la parole d’Allah', 'que rien de la parole des hommes ne lui ressemble',
           'établir ses lettres dans la récitation',
           'le mémoriser et l’enseigner', 'aimer ceux qui le portent',
           's’arrêter à ses limites et à ses prescriptions',
           'méditer ses merveilles',
           'ses versets catégoriques', 'ses versets allégoriques',
           'le leur faire aimer',
           'an-naṣīḥa li-rasūl Allāh',
           'croire en sa véracité', 'lui obéir dans son ordre et son interdit',
           'lui porter secours vivant et mort',
           'se dresser contre quiconque se dresse contre lui',
           'magnifier son droit et le vénérer', 'vivifier sa Sunna',
           'approfondir la compréhension de ses sens',
           'observer la bienséance lors de sa récitation', 'la défendre',
           's’abstenir d’y plonger sans science',
           'se parer de ses morales', 'suivre son exemple dans sa conduite',
           'les membres de sa famille et ses Compagnons',
           'an-naṣīḥa li-’a’immat al-muslimīn',
           '(النَّصِيحَةُ لِأَئِمَّةِ الْمُسْلِمِينَ)',
           'en dehors de la désobéissance à Allah le Très-Haut',
           'leur prêter main-forte dans la vérité',
           'les avertir et leur rappeler avec douceur et ménagement',
           'les informer de ce qui leur a échappé',
           'leur transmettre les droits des musulmans',
           's’abstenir de se soulever contre eux',
           'invoquer Allah pour leur droiture',
           'an-naṣīḥa li-’āmmat al-muslimīn',
           '(النَّصِيحَةُ لِعَامَّةِ الْمُسْلِمِينَ)',
           'tous ceux autres que les détenteurs de l’autorité',
           'abaisser l’aile pour eux',
           'pour leur au-delà et pour leur vie présente',
           'voiler leurs défauts', 'indulgent envers leurs fautes',
           'les conseiller en privé, sans dénonciation publique ni déshonneur',
           'repousser ce qui leur nuit et à leur attirer ce qui leur profite',
           'leur commander le bien et leur interdire le mal',
           'honorer leurs aînés', 'miséricordieux envers leurs plus jeunes',
           'veiller sur eux par la bonne exhortation',
           'renoncer à les tromper et à les envier',
           'le bien que l’on souhaite pour soi-même',
           's’orner de belles qualités',
           'porte le nom de religion et d’islam',
           'une obligation pour tout musulman envers son frère musulman',
           'en toute situation, en tout temps et en tout lieu',
           'dans la mesure de sa capacité',
           'avec douceur, ménagement et sagesse',
           'Je définis la recommandation sincère et j’explicite son statut juridique',
           'Sous quelle forme la recommandation sincère s’adresse-t-elle',
           'il leur fit serment', 'je suis pour vous un sincère conseiller',
           '(Sourate al-A’rāf — verset 20)',
           'Il se détourna d’eux et dit',
           'je vous ai bien transmis le message de mon Seigneur',
           'je vous ai conseillé sincèrement',
           'vous n’aimez pas les sincères conseillers',
           '(Sourate al-A’rāf — verset 78)',
           'je suis pour toi un sincère conseiller',
           '(Sourate al-Qaṣaṣ — verset 19)',
           'qui est le conseiller sincère dans chacune d’elles',
           'le sens de la facilité (<em>al-yusr</em>) dans l’islam',
           'certains des effets qui découlent de la facilité de l’islam']:
    check(f'matière: {kw[:52]}', kw in fr)

# — pose == source, garde-doublon, titleFr —
check('pose == source', fr == src, f'({len(fr)} vs {len(src)} car)')
check('titleFr correct', l.get('titleFr') == 'La religion, c’est le conseil (naṣīḥa)',
      f'({l.get("titleFr")!r})')
# — cohérence série —
reg = json.load(open('/home/z/my-project/scripts-ia2/savant-registry-ia2.json', encoding='utf-8'))
check('registre IA-2 → 12', 'hadith-5ep/pdf-12' in reg['hand'] and len(reg['hand']) == 12,
      f'({len(reg["hand"])} entrées)')

print(f"VÉRIF pdf-12 : {len(ok)} contrôles PASS / {len(fail)} échec(s)")
for f in fail:
    print('  ÉCHEC:', f)
sys.exit(1 if fail else 0)
