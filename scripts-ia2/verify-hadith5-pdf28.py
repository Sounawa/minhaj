#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-33 — vérification de la livraison hadith-5ep / pdf-28 (Consolidation et application)
# Leçon de SYNTHÈSE pp.156-158, SANS encadré de hadith et SANS إعداد قبلي (L29 = bibliographie).
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-28.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-28']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-28 unique', len(les) == 1, f'{len(les)} occurrences')
l = les[0]
fr = l.get('htmlFr') or ''
# — matière sur le FICHIER SOURCE —
check('volume cohérent (leçon de synthèse pp.156-158, 3 pages', 5000 <= len(src) <= 9000, f'{len(src)} car')
check('titre h1 présent', src.startswith('<h1>Consolidation et application</h1>'))
check('sections h2 = 5 (leçon de synthèse)', src.count('<h2>') == 5, f'h2={src.count("<h2>")}')
check('rubriques présentes', all(k in src for k in
      ['Objectifs', 'Le texte', 'La compréhension', 'L’analyse', 'L’application']))
check('PAS d’i’dād qabli (leçon 28 = dernière avant bibliographie — conforme au tirage)',
      'préparation de la leçon suivante' not in src and 'الْإِعْدَاد' not in src)
check('arabe uniquement en spans RTL', not re.search(
    r'[\u0600-\u06FF]', re.sub(r'<span dir="rtl" lang="ar">[^<]*</span>', '', src)))
check('guillemets appariés', src.count('«') == src.count('»'),
      f"({src.count('«')}/{src.count('»')})")
check('0 apostrophe droite', "'" not in src)
check('0 parenthèse ornementale', '﴿' not in src and '﴾' not in src)
check('0 demi-anneau (U+02BF/02BE/02BC/02BB', not any(c in src for c in '\u02bf\u02be\u02bc\u02bb'))
check('0 point-virgule vertical (U+FE14', '\ufe14' not in src)
check('0 double tiret résiduel', '——' not in src)
check('0 double entité &nbsp;', '&nbsp;&nbsp;' not in src)
check('0 U+00A0 littéral', '\u00a0' not in src)
check('0 ligature ﷺ (honorifique porté par le français, convention série', '\ufdfa' not in src)
check('0 placeholder', not re.search(r'XXX|TODO|【|\?\?\?|⟦', src))
check('U+202F en vigueur (espaces fines devant ; : ! ? et dans « »)', src.count('\u202f') >= 25,
      f"{src.count('\u202f')} occurrences")
# — matière adjudiquée du manuel (Z2-33, pp.156-158 : textlayer 154-161 + bbox word-level
#   + tesseract ara 600/1200 dpi psm 4/6 + recadrages ciblés 1200 + analyse d’encre numpy
#   (VLM 429 épuisé en début de tour — relire bandeau p158 + glose Z2-32 si quota revient) —
KW = [
    '<h1>Consolidation et application</h1>',
    # أهداف (3 objectifs, p.156 — T600+T1200+bbox)
    'أَنْ أُقَوِّمَ مُكْتَسَبَاتِي الْمَعْرِفِيَّةَ فِي الدُّرُوسِ السَّابِقَةِ',
    'أَنْ أَذْكُرَ قُدُرَاتِي فِي الِاسْتِيعَابِ وَالْفَهْمِ وَالتَّحْلِيلِ',
    'أَنْ أَعْمَلَ عَلَى تَطْبِيقِ ذَلِكَ مِنْ خِلَالِ وَضْعِيَّاتٍ جَدِيدَةٍ',
    # النص (p.156 — T600+T1200+crop A)
    'إِنَّمَا بُعِثْتُ لِأُتَمِّمَ مَكَارِمَ الْأَخْلَاقِ',
    'أَثْمَرَ ذَلِكَ اسْتِقَامَةَ أَخْلَاقِهِ',
    'الْحَيَاءِ الْمَشْرُوعِ',
    'فِي مَسَالِكِ الْمُحْسِنِينَ',
    # hadith de clôture (p.156 — SANS المحجة dans le tirage : T600×2+T1200×2+bbox+crops K/K2
    #   + analyse d’encre ; «على» fin de ligne au cadre x=78, «البيضاء» début de ligne suivante)
    'قَدْ تَرَكْتُكُمْ عَلَى الْبَيْضَاءِ، لَيْلُهَا كَنَهَارِهَا، لَا يَزِيغُ عَنْهَا بَعْدِي إِلَّا هَالِكٌ',
    # الفهم (p.157 — bbox+T600 ; المذموم tranché ذ par analyse d’encre blob au-dessus du د)
    'الْمَحَجَّةُ الْبَيْضَاءُ',
    'الْغَضَبُ الْمَذْمُومُ',
    'سُلُوكٌ مُنْحَرِفٌ',
    # التحليل (p.157 — bbox+T600 ; «في المجتمع» ligne séparée confirmée bbox y=595)
    'لِأُتَمِّمَ',
    'بِنُصُوصٍ شَرْعِيَّةٍ',
    # التطبيق (p.158 — T600+T1200+bbox ; bandeau illisible à tesseract, attribution par
    #   parallèle L7/L14/L20 + formule أوظف sous bandeau تطبيق p.113 — consignée worklog)
    'أُوَظِّفُ مُكْتَسَبَاتِي لِلْإِجَابَةِ عَمَّا يَأْتِي',
    'أَصُوغُ تَوْجِيهَاتٍ لِحِمَايَةِ حُقُوقِ الْأَطْفَالِ',
    'أُقَدِّمُ ثَلَاثَ نَصَائِحَ لِلتَّخَلُّقِ بِخُلُقِ الْإِحْسَانِ فِيْمَا يَأْتِي',
    'فِي مُعَامَلَةِ الْأَوْلَادِ لِآبَائِهِمْ وَأُمَّهَاتِهِمْ',
    'فِي عَلَاقَةِ الْفَرْدِ بِمُجْتَمَعِهِ',
]
for kw in KW:
    check(f'motif présent : {kw[:42]}…', kw in src)
# références du tirage
check('réf hadith 1 [Sunan d’al-Bayhaqī]', '[Sunan d’al-Bayhaqī]' in src)
check('réf hadith 2 [al-Mustadrak d’al-Ḥākim]', '[al-Mustadrak d’al-Ḥākim]' in src)
check('réf verset TIRAGE [al-’Anbiyā’ : 106] (canonique 107 — décalage ±1 du tirage, conservé)',
      '[al-’Anbiyā’\u202f: 106]' in src)
# DATUM du tirage : المحجة ABSENT du hadith imprimé (vocab فهم 1 l’emploie comme glose canonique)
check('hadith du tirage SANS المحجة (datum p.156, prouvé par l’encre)',
      'عَلَى الْمَحَجَّةِ' not in src and 'الْمَحَجَّةِ الْبَيْضَاءِ' not in src.split('الْمَحَجَّةُ الْبَيْضَاءُ')[0])
check('la voie blanche rend le datum lisible en français', 'la voie blanche' in src)
check('verset rendu (miséricorde pour les mondes)', 'miséricorde pour les mondes' in src)
# — correspondance FICHIER ↔ JSON —
check('htmlFr posé identique au fichier', fr == src, f'{len(fr)} vs {len(src)} car')
check('titleFr conservé', l.get('titleFr') == 'Consolidation et application', f"({l.get('titleFr')})")
check('titleAr conservé', l.get('titleAr') == 'دعم وتطبيق', f"({l.get('titleAr')})")
check('pdfOnly conservé', l.get('pdfOnly') is True)

print(f'{len(ok)} OK / {len(fail)} échec(s)')
for f in fail:
    print('  ÉCHEC :', f)
sys.exit(1 if fail else 0)
