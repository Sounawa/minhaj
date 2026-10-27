#!/usr/bin/env python3
"""Map 13518 — cartographie des emplacements coraniques vides (protocole R271-R274).

Cas 5e consécutif du livre : leçon de tafsir au matériau versical ravagé.
Repère les appels de citation (« قوله تعالى : », « فقال تعالى : », « وقوله : »)
dépourvus de texte coranique subsistant, les nbsp orphelins (slots visibles),
les gloses orphelines du الفهم, et les spans de référence subsistants.
"""
import re, pathlib

src = pathlib.Path('/home/z/my-project/tr-tmp/13518.src.html').read_text(encoding='utf-8')

# 1. Appels de citation (introductions imprimées « qāla taʿālā » etc.)
calls = re.findall(r'(فقال تعالى|وقوله تعالى|ومنه قوله تعالى|وقوله:|ومنه قوله|بقوله|قوله تعالى|قوله)', src)
print('appels de citation imprimés :', len(calls))

# 2. Slots visibles = nbsp orphelins (double nbsp = emplacement image perdu)
dbl = re.findall(r'[^\s]\u00a0\u00a0[^\s]', src)
sng = re.findall(r'[\u0600-\u06FF]\u00a0[\u0600-\u06FF\u00a0]', src)
print('double-nbsp (slots visibles) :', len(dbl))

# 3. Gloses orphelines du الفهم (lignes du bloc الشرح)
glosses = re.findall(r'<p>فاخش[^<]*</p>', src)
if glosses:
    lines = [l for l in glosses[0].replace('<p>', '').replace('</p>', '').split('<br>') if l.strip()]
    print('gloses orphelines الفهم :', len(lines))
    for l in lines:
        print('   -', l.strip()[:60])

# 4. Spans de référence subsistants (crochets coraniques vides ou références)
spans = re.findall(r'\[([^\]]*آيات[^\]]*|\S+: ?\d+[^\]]*)\]', src)
print('spans de référence subsistants :', spans)

# 5. Crochets ornementaux orphelins
for ch in ('\uFD3E', '\uFD3F'):
    n = src.count(ch)
    if n:
        print(f'crochet ornemental {hex(ord(ch))} : {n} occurrence(s)')

# 6. Fente dl/dt/dd vide
dd = re.search(r'<dl>\s*<dt></dt>\s*<dd>\s*</dd>\s*</dl>', src)
print('fente dl/dt/dd vide :', bool(dd), '(7e occurrence du chantier si oui)')

# 7. Paragraphe vides (liste de mots perdue)
empties = len(re.findall(r'<p></p>', src))
print('paragraphes vides (liste perdue + résidus) :', empties)

# 8. Vérifs de garde : appels sans slot identifiable
print()
print('=== DÉCOMpte attendu : 32 restaurations (R1-R39 plan de rédaction) ===')
print('bloc principal 51-56 + exploitation anbiyā 21-24 = 2 blocs')
print('الفهم = 7 tronçons ; Tafsir = 19+7+4 slots ; تقويم = 1')
