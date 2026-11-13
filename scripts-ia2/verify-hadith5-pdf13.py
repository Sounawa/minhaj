#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-15 — vérification de la livraison hadith-5ep / pdf-13 (La facilité de la religion islamique)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-13.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-13']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-13 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon 6 pages)', 10000 <= len(src) <= 16000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 10, f'(h2={src.count("<h2>")})')
check('sous-sections h3', src.count('<h3>') == 6, f'(h3={src.count("<h3>")})')
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
check('0 point-virgule vertical (U+FE14)', '\ufe14' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?', src))
# — matière adjudiquée du manuel (Z2-15, planches p74-79 + composites 600 dpi A→E) —
for kw in ['<h1>La facilité de la religion islamique</h1>',
           'al-yusr', '(يُسْرُ الْإِسْلَامِ)',
           'Treizième leçon (13) du manuel', 'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'tamhīd', 'tarǧamat ar-rāwī',
           'al-fahm', 'istikhlāṣ al-maḍāmīn', 'at-taḥlīl', 'at-taqwīm',
           'al-istiṯmār', 'al-a’dād al-qabliyya',
           'du neuvième hadīth des Quarante',
           '‘Abd ar-Raḥmān ibn Ṣaḫr',
           'la facilité de l’islam et certaines de ses manifestations',
           'les effets de la facilité dans l’islam',
           'le principe de facilité et la levée de la gêne',
           'les principes majeurs sur lesquels repose l’islam',
           'la relation de l’homme avec son Seigneur',
           'Éloignez-vous de ce que je vous ai interdit',
           'accomplissez de ce que je vous ai ordonné ce que vous pouvez',
           'les questions excessives et les divergences envers leurs prophètes',
           'Ṣaḥīḥ de al-Buḫārī et Muslim',
           '‘Abd ar-Raḥmān ibn Ṣaḫr ad-Dawsī',
           'celle dont le Messager d’Allah',
           'l’année de <em>Ḫaybar</em>',
           'fréquentation assidue',
           'par désir du savoir',
           'mémorisa le mieux le hadīth prophétique',
           'son empressement vers le savoir et le hadīth',
           'gouverneur d’<em>al-Baḥrayn</em>',
           'le gouvernement de Médine la Illuminée',
           'en l’an cinquante-sept ou cinquante-huit de l’Hégire',
           'à l’âge de soixante-dix-huit ans',
           'enterré au <em>al-Baqī’</em>',
           'fajtanibūhu', 'écartez-vous de cela',
           'ce dont vous avez la capacité et le pouvoir',
           'leur opposition et leur désobéissance à leurs prophètes',
           'indique la facilité de l’islam',
           'ce que le Prophète — prière et salut d’Allah sur lui — a ordonné',
           'maẓāhiru al-yusr fi al-’islām', '(أَوَّلًا: مَظَاهِرُ الْيُسْرِ فِي الْإِسْلَامِ)',
           'des ordres et des interdits qu’il faut observer',
           'laissé les interdits en leur généralité',
           'conditionné les commandements par la capacité',
           'l’interdit est une demande d’abandon',
           'à la portée de chacun',
           'quant au commandement, il est tantôt réalisable et tantôt irréalisable',
           'certains piliers de la prière ou certaines de ses conditions',
           'il prie selon ce qu’il peut en accomplir',
           'laver certains membres des ablutions',
           'il lave ce qui lui est possible',
           'la suppression des répréhensibles',
           '’āṯāru yusri al-’islām', '(ثَانِيًا: آثَارُ يُسْرِ الْإِسْلَامِ)',
           'la levée de la gêne qui pèse sur l’assujetti',
           'son élan vers l’obéissance',
           'obtempérer en toute circonstance',
           'Allah n’impose à une âme que ce qu’elle peut porter',
           '(Sourate al-Baqara — verset 286)',
           'Craignez Allah autant que vous le pouvez',
           '(Sourate at-Taġābun — verset 16)',
           'Il ne vous a imposé aucune gêne dans la religion',
           '(Sourate al-Ḥaǧǧ — verset 76)',
           'la souplesse de la religion et de sa facilité',
           'la permission de l’interdit par nécessité',
           'la consommation de charogne pour préserver la vie',
           'Les nécessités autorisent les interdits',
           'respecter les principes de la facilité',
           'par ménagement de l’assujetti',
           'en rendant l’obéissance aisée',
           'pour donner à aimer la pratique religieuse',
           'en évitant de rendre les choses difficiles tout comme la divergence',
           'à la gêne, à l’adversité et à la scission',
           'an-nahyu ‘ani l-iḫtilāf', '(النَّهْيُ عَنِ الِاخْتِلَافِ)',
           'une menace de perdition',
           'cause de division et de faiblesse',
           'Attachez-vous tous ensemble au câble d’Allah',
           '(Sourate Āl ’Imrān — verset 103)',
           'wa-ḫtilāfuhum', '<span dir="rtl" lang="ar">(وَاخْتِلَافُهُمْ)</span>',
           'avec ḍamma sur le hā’',
           'coordonné à «\u202f&nbsp;kathra&nbsp;\u202f»',
           'le plus expressif',
           'la perdition naquit de la divergence elle-même',
           'an-nahyu ‘an kathrati s-su’āl', '(النَّهْيُ عَنْ كَثْرَةِ السُّؤَالِ)',
           'réparti la question en deux catégories',
           'ce qui relève de la pratique',
           'ce dont on a besoin dans les affaires de la religion',
           'Interrogez donc les gens du rappel',
           '(Sourate al-Anbiyā’ — verset 7)',
           'les butins, la succession calale et les novas',
           'Fatḥ al-Bārī d’Ibn Ḥaǧar',
           'la contestation, de l’affectation et de l’indiscrétion',
           'la multiplication des questions peut engendrer la multiplication des réponses',
           'gêne et peine',
           'Le pèlerinage vous a été prescrit',
           'Chaque année, ô Messager d’Allah',
           'Il garda le silence jusqu’à ce que l’homme eut répété trois fois',
           'ce serait obligatoire, et vous ne le pourriez pas',
           'Laissez-moi ce que je vous ai laissé',
           'quand je vous interdis une chose, délaissez-la',
           'al-’Aqra’ ibn Ḥābis at-Tamīmī',
           'religion de facilité et d’unité',
           'religion de gêne et de scission',
           'La guidance du Prophète',
           'dans les affaires de la religion et du monde',
           'certaines manifestations de la facilité dans l’islam',
           'Pourquoi le commandement a-t-il été conditionné par la capacité',
           'mis en garde contre la divergence et la multiplication des questions',
           '‘Imrān ibn Ḥuṣayn',
           'je souffrais d’hémorroïdes', 'bawāsīr',
           'Prie debout', 'assis', 'sur le flanc',
           'les manifestations de l’obligation mesurée à la capacité',
           'd’autres manifestations que je peux convoquer',
           'Je lis les textes de la leçon qui vient',
           'les acquis de mon savoir dans les leçons précédentes',
           'répondre aux questions liées au texte']:
    check(f'matière: {kw[:52]}', kw in fr)

# — pose == source, garde-doublon, titleFr —
check('pose == source', fr == src, f'({len(fr)} vs {len(src)} car)')
check('titleFr correct', l.get('titleFr') == 'La facilité de la religion islamique',
      f'({l.get("titleFr")!r})')
# — cohérence série —
reg = json.load(open('/home/z/my-project/scripts-ia2/savant-registry-ia2.json', encoding='utf-8'))
check('registre IA-2 → 13', 'hadith-5ep/pdf-13' in reg['hand'] and len(reg['hand']) == 13,
      f'({len(reg["hand"])} entrées)')

print(f"VÉRIF pdf-13 : {len(ok)} contrôles PASS / {len(fail)} échec(s)")
for f in fail:
    print('  ÉCHEC:', f)
sys.exit(1 if fail else 0)
