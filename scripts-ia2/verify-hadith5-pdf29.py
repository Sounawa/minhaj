#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-34 — vérification de la livraison hadith-5ep / pdf-29 (Liste des sources et références)
# DERNIÈRE leçon du livre : bibliographie pp.159-166, 39 entrées numérotées + entrée Coran
# non numérotée, en 4 rubriques (القرآن / كتب الحديث / شروح الحديث / مراجع أخرى).
# Données adjudiquées Z2-34 : textlayer 156-167 + bbox word-level + tesseract ara 600/1200
# psm 4/6/13 + recadrages ciblés 1200 + analyse d'encre numpy + composantes connexes des
# chiffres (calibration sur dates connues) — VLM 429 épuisé tout le tour (relance tentée).
import json, re, sys

PATH = '/home/z/my-project/content/books/hadith-5ep.json'
HTML = '/home/z/my-project/scripts-ia2/livraisons/hadith-5ep/pdf-29.html'

src = open(HTML, encoding='utf-8').read()
book = json.load(open(PATH, encoding='utf-8'))
les = [l for l in book['lessons'] if l['docId'] == 'pdf-29']
ok, fail = [], []

def check(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

check('leçon pdf-29 unique', len(les) == 1, f'{len(les)} occurrences')
l = les[0]
fr = l.get('htmlFr') or ''
# — structure —
check('volume cohérent (bibliographie 8 pp., 39 entrées)', 13000 <= len(src) <= 21000, f'{len(src)} car')
check('titre h1 présent', src.startswith('<h1>Liste des sources et références</h1>'))
check('sections h2 = 4 rubriques', src.count('<h2>') == 4, f'h2={src.count("<h2>")}')
check('rubriques présentes', all(k in src for k in
      ['Le Coran', 'Les livres de hadith', 'Les commentaires de hadith', 'Autres références']))
check('39 entrées numérotées (19 + 17 + 3)', src.count('<li>') == 39, f'li={src.count("<li>")}')
check('ol start=20 et start=37 (numérotation continue du tirage)',
      '<ol start="20">' in src and '<ol start="37">' in src)
# — typographie série —
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
check('U+202F en vigueur (espaces fines devant ; : ! ? et dans « »)', src.count('\u202f') >= 90,
      f"{src.count('\u202f')} occurrences")
# — données adjudiquées du manuel (Z2-34, pp.159-166) —
KW = [
    '<h1>Liste des sources et références</h1>',
    'لائحة المصادر والمراجع',
    # entrée Coran (p.159 — ligne 2 cachée au cmap lue par psm13 ×8 : bandeau + texte)
    'القرآن الكريم؛ برواية ورش عن نافع من طريق الأزرق',
    'المصحف المحمدي',
    'مؤسسة محمد السادس لنشر المصحف الشريف',
    # les 39 titres (RTL spans, texte NON vocalisé du tirage)
    'صحيح البخاري', 'صحيح مسلم', 'الموطأ', 'سنن الترمذي', 'سنن ابن ماجة',
    'السنن الكبرى', 'سنن النسائي', 'صحيح ابن حبان', 'المستدرك على الصحيحين',
    'مسند الإمام أحمد بن حنبل', 'المعجم الكبير', 'المعجم الأوسط', 'المعجم الصغير',
    'شعب الإيمان', 'مسند أبي يعلى', 'الشمائل المحمدية والخصائل المصطفوية',
    'فضائل الصحابة', 'شرح الأربعين النووية في الأحاديث الصحيحة النبوية',
    'الفتح المبين بشرح الأربعين', 'الفتوحات الوهبية بشرح الأربعين النووية',
    'فتح الباري شرح صحيح البخاري', 'شرح ابن بطال لصحيح البخاري',
    'عمدة القاري شرح صحيح البخاري', 'شرح الزرقاني على موطأ الإمام مالك',
    'إكمال المعلم بفوائد مسلم', 'شرح النووي على مسلم؛ المسمى: المنهاج شرح صحيح مسلم بن الحجاج',
    'جامع العلوم والحكم شرح خمسين حديثا من جوامع الكلم', 'الجامع الصغير في أحاديث البشير النذير',
    'التيسير بشرح الجامع الصغير', 'دليل الفالحين لطرق رياض الصالحين', 'الآداب',
    'المفهم لما أشكل من تلخيص كتاب مسلم', 'إكمال إكمال المعلم شرح صحيح مسلم',
    'جامع بيان العلم وفضله', 'تفسير ابن أبي حاتم', 'فيض القدير شرح الجامع الصغير',
    # rubrique décorative lue psm13 ×4 + parallèle structurel (entrées 20-36 = commentaires)
    'شروح الحديث',
    # entrée 37 : header INVISIBLE au cmap ET à tesseract pleine page — lu par recadrage psm13 ×4
    'جامع بيان العلم وفضله', 'Abī ’Umar Yūsuf ibn ’Abd Allāh ibn Muḥammad',
    # dates adjudiquées (bbox ordre visuel + tesseract + CC-chiffres calibrés)
    'mort en 256 H', 'mort en 261 H', 'mort en 273 H', 'mort en 303 H',
    'mort en 354 H', 'mort en 360 H', 'mort en 405 H', 'mort en 458 H',
    'mort en 544 H', 'mort en 795 H', 'mort en 855 H', 'mort en 1031 H',
    'mort en 1057 H', 'mort en 307 H', 'mort en 241 H',
    'mort en 656 H', 'mort en 827 H', 'mort en l’an 449 H', 'mort en l’an 327 de l’hégire',
    '849 - 911 H', '1434 H / 2013', '1407 H / 1987', '1414 H / 1994',
    '1415 H / 1994', '1411 H / 1990', '1421 H / 2001', '1403 H / 1983',
    '1404 H / 1984', '1405 H / 1985', '1406 H / 1986', '1424 H / 2003',
    '1423 H / 2003', '1423 H / 2003', '1417 H / 1996', '1419 H / 1998',
    '1408 H', '1392 H', '1425 H / 2004', '1428 H', '1412 H',
    '1379 H', '1356',
]
for kw in KW:
    check(f'motif présent : {kw[:40]}…', kw in src)
# DATUM du tirage — entrée 7 (السنن الكبرى) SANS «الخسروجردي» (cmap + crop C2) :
# al-Ḫusrawǧardī n'apparaît que dans les entrées 16 (شعب الإيمان) et 34 (الآداب)
check('al-Ḫurāsānī présent (entrée 7, sans الخسروجردي)', 'al-Ḫurāsānī' in src)
check('al-Ḫusrawǧardī exactement 2 (entrées 16 et 34, PAS l’entrée 7)',
      src.count('al-Ḫusrawǧardī') == 2, f"{src.count('al-Ḫusrawǧardī')} occurrences")
# DATUM — entrée 4 (سنن أبي داود, دار الفكر) SANS date de mort (CC : une virgule seule
# après الأزدي ; l'entrée 9, autre édition, porte seule le (المتوفى: 275ه))
i4 = src.find('édition Dār al-Fikr')
seg4 = src[max(0, i4-320):i4]
check('entrée 4 SANS date de mort (datum du tirage, prouvé par composantes connexes)',
      'mort en' not in seg4)
check('entrée 9 AVEC 275 H (autre édition, datum du tirage)', 'mort en 275 H' in src)
# — correspondance FICHIER ↔ JSON —
check('htmlFr posé identique au fichier', fr == src, f'{len(fr)} vs {len(src)} car')
check('titleFr conservé', l.get('titleFr') == 'Liste des sources et références', f"({l.get('titleFr')})")
check('titleAr conservé', l.get('titleAr') == 'لائحة المصادر والمراجع', f"({l.get('titleAr')})")
check('pdfOnly conservé', l.get('pdfOnly') is True)

print(f'{len(ok)} OK / {len(fail)} échec(s)')
for f in fail:
    print('  ÉCHEC :', f)
sys.exit(1 if fail else 0)
