#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-12 — vérification de la livraison hadith-5ep / pdf-11 (la correction du cœur)
import json, re, sys

PATH = '/home/z/my-project/minhaj/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/minhaj/scripts-ia2/livraisons/hadith-5ep/pdf-11.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-11']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-11 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon 4 pages)', 9000 <= len(src) <= 16000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 10, f'(h2={src.count("<h2>")})')
check('sous-sections h3', src.count('<h3>') == 4, f'(h3={src.count("<h3>")})')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Exorde', 'Le texte', 'Notice biographique du transmetteur',
       'La compréhension', 'Glossaire', 'Extraction des contenus', 'L’analyse',
       'Premièrement', 'Deuxièmement',
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
# — matière adjudiquée du manuel (Z2-12, planches p65-68 + zooms 600 dpi) —
for kw in ['<h1>La correction du cœur</h1>',
           'iṣlāḥ al-qalb', '(إِصْلَاحُ الْقَلْبِ)',
           'Onzième leçon (11) du manuel', 'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'tamhīd', 'an-naṣṣ', 'tarǧamat ar-rāwī',
           'al-fahm', 'istikhlāṣ al-maḍāmīn', 'at-taḥlīl', 'at-taqwīm',
           'al-istiṯmār', 'al-a’dād al-qabliyya',
           'la clôture du sixième hadīth des Quarante',
           'Abū ’Abd Allāh an-Nu’mān ibn Bašīr',
           'la position du cœur parmi les organes',
           'la forteresse de la foi', 'maḥkamu al-īmān',
           'le lieu du regard du Miséricordieux', 'manāṭu at-taklīf',
           'mawḍi’u at-tašrīf',
           'questions épineuses',
           'Quelle est donc la position du cœur parmi les organes',
           'Le licite est évident et l’illicite est évident',
           'un morceau de chair', 'c’est le cœur',
           'Ṣaḥīḥ de al-Buḫārī et Muslim',
           'sa notice biographique a déjà été donnée',
           'nom verbal', 'maṣdar', 'qalaba', 'ḫawāṭir',
           'J’en extrais ce qui indique l’importance du cœur',
           'ahammīyatu al-qalb bayna a’ḍā’i al-ǧasad',
           '(أَوَّلًا: أَهَمِّيَّةُ الْقَلْبِ بَيْنَ أَعْضَاءِ الْجَسَد)',
           'l’émir des organes',
           'ils s’amendent par son amendement',
           'Dès lors que tu connais son immense valeur',
           'Ǧāmi’ al-’ulūm wa-l-ḥikam — adapté',
           'l’espèce animale', 'les intérêts visés',
           'en sus du cœur, la raison', 'al-’aql',
           'N’ont-ils donc pas parcouru la terre',
           'des cœurs pour comprendre, ou des oreilles pour entendre',
           'Ce ne sont pas les yeux qui s’aveuglent',
           '(Sourate al-Ḥaǧǧ — verset 44)',
           'Il a soumis les organes, obéissants envers lui',
           'Telle est la portée de Sa parole',
           'la droiture du cœur est la plus grande des sources de bien',
           'aṯaru al-qalb fī ṣalāḥi al-’amal wa-fasādih',
           '(ثَانِيًا: أَثَرُ الْقَلْبِ فِي صَلَاحِ الْعَمَلِ وَفَسَادِه)',
           'Les savants ont ainsi explicité ce qui amende le cœur',
           'la récitation du noble Coran avec méditation',
           'l’approfondissement de la religion',
           'Sa belle surveillance', 'la veille nocturne',
           'aux dernières heures de la nuit', 'la piété filiale',
           'la fréquentation des justes', 'l’assistance aux funérailles',
           'la visite des tombes',
           'l’acquisition de tout gain licite',
           'l’abstention des choses douteuses',
           'le délaissement du noble Coran',
           'la négligence de l’évocation d’Allah le Très-Haut',
           'l’abandon de la prière', 'l’ignorance de la religion',
           'la volubilité du propos et du regard',
           'l’excès de sommeil, de nourriture et d’étourderie',
           'l’oubli de l’évocation de l’au-delà',
           'At-Tirmiḏī a en effet rapporté', 'Abū Hurayra',
           'une tache noire est inscrite sur son cœur',
           's’il se détourne, implore le pardon et se repent',
           'suqqa', 'forme dialectale',
           'ar-rān',
           'la rouille de leurs acquisitions',
           '(Sourate al-Muṭaffifīn — verset 14)',
           'Sunan at-Tirmiḏī',
           'L’immense effet du cœur sur les organes',
           'La recherche du gain licite est une cause de droiture',
           'la plus grande des droitures',
           'Pourquoi le cœur est-il celui qui commande aux organes',
           'la droiture de la conduite ou sa corruption',
           'après le licite et l’illicite',
           '(Sourate al-Ḥadīd — verset 15)',
           'Le temps n’est-il pas venu pour ceux qui ont cru',
           'leurs cœurs se sont endurcis',
           'qasat qulūbuhum', '(فَقَسَتْ قُلُوبُهُمْ)',
           'Je déduis de l’āya l’effet de la droiture du cœur',
           'Tamīm ad-Dārī', 'an-naṣīḥa',
           'l’importance du cœur parmi les membres du corps']:
    check(f'matière: {kw[:52]}', kw in fr)

# — pose == source, garde-doublon, titleFr —
check('pose == source', fr == src, f'({len(fr)} vs {len(src)} car)')
check('titleFr correct', l.get('titleFr') == 'La correction du cœur',
      f'({l.get("titleFr")!r})')
# — cohérence série —
reg = json.load(open('/home/z/my-project/minhaj/scripts-ia2/savant-registry-ia2.json', encoding='utf-8'))
check('registre IA-2 → 11', 'hadith-5ep/pdf-11' in reg['hand'] and len(reg['hand']) == 11,
      f'({len(reg["hand"])} entrées)')

print(f"VÉRIF pdf-11 : {len(ok)} contrôles PASS / {len(fail)} échec(s)")
for f in fail:
    print('  ÉCHEC:', f)
sys.exit(1 if fail else 0)
