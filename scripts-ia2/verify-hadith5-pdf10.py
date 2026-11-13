#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-11 — vérification de la livraison hadith-5ep / pdf-10 (le licite, l'illicite et les choses ambiguës)
import json, re, sys

PATH = '/home/z/my-project/minhaj/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/minhaj/scripts-ia2/livraisons/hadith-5ep/pdf-10.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-10']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-10 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon 5 pages)', 9500 <= len(src) <= 17000, f'({len(src)} car)')
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
# — matière adjudiquée du manuel (Z2-11, planches p60-64 + zooms 600 dpi) —
for kw in ['<h1>Le licite, l’illicite et les choses ambiguës</h1>',
           'al-ḥalāl wa-l-ḥarām wa-l-muštabahāt',
           '(الْحَلَالُ وَالْحَرَامُ وَالْمُشْتَبِهَاتُ)',
           'Dixième leçon (10) du manuel', 'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'tamhīd', 'an-naṣṣ', 'tarǧamat ar-rāwī',
           'al-fahm', 'istikhlāṣ al-maḍāmīn', 'at-taḥlīl', 'at-taqwīm',
           'al-istiṯmār', 'al-a’dād al-qabliyya',
           'le sixième hadīth des Quarante', 'Abū ’Abd Allāh an-Nu’mān ibn Bašīr',
           'qu’Allah soit satisfait d’eux deux',
           'Le licite est évident et l’illicite est évident',
           'des choses ambiguës que beaucoup de gens ne connaissent pas',
           'préserve ainsi la pureté de sa religion et de son honneur',
           'comme le berger qui fait paître autour d’une réserve',
           'tout roi possède une réserve',
           'la réserve d’Allah, ce sont Ses interdictions',
           'un morceau de chair', 'c’est le cœur',
           'Ṣaḥīḥ de al-Buḫārī et Muslim',
           'ibn Sa’d ibn Ṯa’laba al-Anṣārī al-Ḫazraǧī',
           'kunya Abū ’Abd Allāh', 'an 90 de l’Hégire',
           'premier enfant né dans l’islam parmi les Anṣār',
           'gouverneur de la Kūfa', 'Ǧumaṣ (Ḥimṣ)', 'Qaṣā’ de Damas',
           'orateur éloquent', 'an 65 de l’Hégire',
           'ce dont aucune interdiction n’est connue',
           'ce que la Loi est venue interdire',
           'ce qui hésite entre le licite et l’illicite',
           'il a pris garde et s’est abstenu',
           'la pureté et la sauvegarde à l’égard du péché',
           'le lieu de la louange et du blâme',
           'interdit à quiconque n’en est pas le propriétaire',
           'son bétail en mange et y broute',
           'Quel est le sens du licite et de l’illicite',
           'Quel est le jugement des choses ambiguës',
           'aqsām al-ištibāh bi-ḥukm aš-šar’',
           'al-ḥalāl aṭ-ṭayyib',
           'Il rend licites pour eux les bonnes choses',
           '(Sourate al-Mā’ida — verset 6)',
           'Et Il vous a rendu licites ce qui est au-delà de cela',
           '(Sourate an-Nisā’ — verset 24)',
           'Sont illicites pour vous vos mères, vos filles',
           '(Sourate an-Nisā’ — verset 23)',
           'le gibier de la terre tant que vous êtes en état de sacralisation',
           '(Sourate al-Mā’ida — verset 96)',
           'turpitudes, apparentes ou cachées',
           'an-namra as-sāqiṭa', 'Sunan al-Bayhaqī al-kubrā',
           'Si je n’avais pas craint qu’elle fût de l’aumône, je l’aurais mangée',
           'Écarte ce qui te met dans le doute pour ce qui ne t’en met pas',
           'Sunan an-Nasā’',
           'ḥukm al-’umūr al-muštabahāt',
           'On a dit&nbsp;\u202f: elles sont illicites',
           'On a dit aussi&nbsp;\u202f: elles sont licites',
           'elles ne sont ni illicites ni licites',
           'anwā’ an-nās fī t-ta’āmuli ma’a l-muštabahāt',
           'sont de deux types',
           'sa religion et son honneur sont alors sauves',
           'la complaisance à leur égard incite à l’audace',
           'un pâturage dont l’accès est interdit',
           's’y trouve généralement mêlé',
           'Telles sont les limites d’Allah — ne vous en approchez pas',
           '(Sourate al-Baqara — verset 186)',
           'par crainte de tomber dans l’illicite',
           'La mise en garde contre tout ce qui mène à l’illicite',
           'continence', 'al-qanā’a',
           'Cite un exemple de licite et d’illicite',
           'Ibn Raǧab — qu’Allah lui fasse miséricorde',
           'divise les gens, face aux choses ambiguës, en deux catégories',
           'celui sur qui elles sont devenues ambiguës',
           'troisième catégorie, qui est la meilleure des trois',
           'Ǧāmi’ al-’ulūm wa-l-ḥikam',
           'telles que le texte les met en lumière',
           'l’importance du cœur parmi les membres du corps',
           'la droiture de l’œuvre ou sur sa corruption']:
    check(f'matière: {kw[:52]}', kw in fr)

# — pose == source, garde-doublon, titleFr —
check('pose == source', fr == src, f'({len(fr)} vs {len(src)} car)')
check('titleFr correct', l.get('titleFr') == 'Le licite, l’illicite et les choses ambiguës',
      f'({l.get("titleFr")!r})')
# — cohérence série —
reg = json.load(open('/home/z/my-project/minhaj/scripts-ia2/savant-registry-ia2.json', encoding='utf-8'))
check('registre IA-2 → 10', f'hadith-5ep/pdf-10' in reg['hand'] and len(reg['hand']) == 10,
      f'({len(reg["hand"])} entrées)')

print(f"VÉRIF pdf-10 : {len(ok)} contrôles PASS / {len(fail)} échec(s)")
for f in fail:
    print('  ÉCHEC:', f)
sys.exit(1 if fail else 0)
