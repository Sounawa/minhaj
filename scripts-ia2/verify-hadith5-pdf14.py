#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-16 — vérification de la livraison hadith-5ep / pdf-14 (Consolidation et application)
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-14.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-14']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-14 unique', len(les) == 1, f'({len(les)} occurrences)')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon consolidation)', 4000 <= len(src) <= 8000, f'({len(src)} car)')
check('titre h1 présent', src.startswith('<h1>'))
check('sections h2', src.count('<h2>') == 6, f'(h2={src.count("<h2>")})')
check('0 sous-section h3 (format consolidation)', src.count('<h3>') == 0, f'(h3={src.count("<h3>")})')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Le texte', 'La compréhension', 'L’analyse', 'L’application',
       'La préparation de la leçon suivante']))
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 demi-anneau (U+02BF/02BE)', '\u02bf' not in src and '\u02be' not in src)
check('0 point-virgule vertical (U+FE14)', '\ufe14' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?', src))
# — matière adjudiquée du manuel (Z2-16, planches p80-82 + composites Z14/W14/V14) —
for kw in ['<h1>Consolidation et application</h1>',
           'da’m wa-t-taṭbīq', '(دَعْمٌ وَتَطْبِيقٌ)',
           'Quatorzième leçon (14) du manuel', 'Arba’ūn', 'ta’līm ’atīq',
           'ahdāf ad-dars', 'an-naṣṣ', 'al-fahm', 'at-taḥlīl', 'at-taṭbīq',
           'al-a’dād al-qabliyya',
           'Que j’évalue mes acquis dans les leçons précédentes',
           'Que je repère mes capacités dans l’analyse',
           'Que je mette mes acquis à profit dans des situations nouvelles',
           'L’homme est une créature honorée auprès d’Allah le Très-Haut',
           'Il l’a créé — glorifié soit-Il — de terre',
           'une extraction d’eau vile',
           'création après création, dans trois ténèbres',
           'béni soit Allah, le meilleur des créateurs',
           'Il est de Ses signes qu’Il vous a créés de terre',
           'vous êtes des hommes qui se répandent sur la terre',
           '(Sourate ar-Rūm — verset 19)',
           'l’âge de la responsabilité religieuse',
           'Il lui commande la foi en Lui et l’obéissance',
           'le guide vers le soin du cœur',
           'la source de son bonheur et de son malheur',
           'un jour où ni les biens ni les enfants ne seront d’aucune utilité',
           'un cœur sain',
           '(Sourate ash-Shu’arā’ — versets 88-89)',
           'Il lui a permis certaines choses et lui en a interdit d’autres',
           'Il a interdit l’usure',
           'la piété de prudence et à l’écart des choses douteuses',
           'les innovations et les répréhensibles',
           'le conseil sincère en vertu de la fraternité de foi',
           'l’attachement à la Sunna',
           'Attachez-vous à ma Sunna et à la Sunna des califes bien guidés',
           'mordez-y avec les dents molaires',
           'Ǧāmi’ bayān al-’ilm wa-faḍlihi d’Ibn ‘Abd al-Barr',
           'Il a placé son devenir entre Ses mains',
           'Il connaît vos mouvements et vos lieux de repos',
           '(Sourate Muḥammad — verset 20)',
           'si seulement j’avais fait telle et telle chose',
           'Allah l’a décrété, et ce qu’Il a voulu, Il l’a fait',
           'ouvre l’œuvre de Satan',
           'Ṣaḥīḥ de Muslim',
           'J’explique',
           'les choses douteuses — les répréhensibles',
           'tantashirūn',
           'Je cite les contraires des mots suivants',
           'al-’īmān', 'al-wara’', 'al-mahdiyyūn',
           'j’appuie cela d’un texte religieux',
           'la source du bonheur de l’homme et de son malheur',
           'la piété de prudence face aux choses douteuses',
           'que l’issue finale appartient à Allah le Très-Haut',
           'l’importance du cœur',
           'l’attachement à la Sunna',
           'les étapes du développement de l’embryon dans le ventre de sa mère',
           'parmi les plus impérieuses des obligations',
           'des orientations pour le soin du cœur et sa correction',
           'des conseils à un camarade',
           'éviter de tomber dans les innovations et les répréhensibles',
           'l’éducation de l’âme',
           'ses enseignements de tolérance',
           'Je mémorise le hadīth de la leçon qui vient',
           'l’importance de l’invocation', 'ad-du’ā’',
           'le rapport entre la consommation du licite et l’invocation']:
    check(f'matière: {kw[:52]}', kw in fr)

# — pose == source, garde-doublon, titleFr —
check('pose == source', fr == src, f'({len(fr)} vs {len(src)} car)')
check('titleFr correct', l.get('titleFr') == 'Consolidation et application',
      f'({l.get("titleFr")!r})')
# — cohérence série —
reg = json.load(open('/home/z/my-project/scripts-ia2/savant-registry-ia2.json', encoding='utf-8'))
check('registre IA-2 → 14', 'hadith-5ep/pdf-14' in reg['hand'] and len(reg['hand']) == 14,
      f'({len(reg["hand"])} entrées)')

print(f"VÉRIF pdf-14 : {len(ok)} contrôles PASS / {len(fail)} échec(s)")
for f in fail:
    print('  ÉCHEC:', f)
sys.exit(1 if fail else 0)
