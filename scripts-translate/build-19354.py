#!/usr/bin/env python3
# build-19354.py — 19354 « Jurisprudence : ce qu'il est interdit au failli… »
# (fiqh-tanawi-3, lessons[4], badge Leçon 6/33) — JUMELLE de 15355 (R294) :
# même matn verbatim, même exploitation ; édition-cours (titre court, sans
# en-tête تمهيد, sous-titres numérotés, listes rétablies, ligne de cours
# الدرس الأول). QUATRE emplacements coraniques VIDES (références tombées)
# résolus conformément au tranchage de la jumelle — verify-19354.py :
# (2:280) TREIZIÈME cas du fil, (2:282) QUATORZIÈME cas, (4:11) ×2 confirmées.
# Hadith du Muwaṭṭaʾ subsistant in extenso — suivi tel quel.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19354_{i}.html').read())
html = ''.join(parts).strip()
html = html.replace("'", chr(0x2019))

issues = []
AR = re.compile('[' + ''.join(chr(a) + '-' + chr(b) for a, b in [
    (0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF),
    (0xFB50, 0xFDF9), (0xFDFB, 0xFDFD), (0xFE70, 0xFEFF)]) + ']')
ar = AR.findall(html)
if ar:
    issues.append("caractères arabes résiduels: " + str(len(ar)) + " : " + ''.join(sorted(set(ar)))[:50])
if html.count("«") != html.count("»"):
    issues.append(f"guillemets non appariés: {html.count('«')} / {html.count('»')}")
if "'" in html:
    issues.append(f"apostrophes droites restantes: {html.count(chr(39))}")
for cp, name in [(0x0430, 'cyrillique'), (0xFD3E, 'crochet ornement gauche'), (0xFD3F, 'crochet ornement droit')]:
    if chr(cp) in html:
        issues.append(f'{name} présent')
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'li', 'em', 'span', 'br']:
    o, c = html.count(f'<{tag}'), html.count(f'</{tag}>')
    if tag in ('br',):
        continue
    if o != c:
        issues.append(f'balises {tag} non appariées: {o} / {c}')
# résolution des slots attendue
for ref in ['(2 :280)', '(2 :282)', '(4 :11)']:
    if ref not in html:
        issues.append(f'reférence coranique attendue absente: {ref}')
if html.count('(4 :11)') < 2:
    issues.append(f"(4 :11) doit apparaître au moins 2 fois — trouvé {html.count('(4 :11)')}")
n_li = html.count('<li>')
print(f'caractères: {len(html)}')
print(f'entrées li: {n_li}')
print(f'em: {html.count("<em>")}')
print(f'guillemets: {html.count("«")}/{html.count("»")}')
print(f'ul: {html.count("<ul>")}')
if issues:
    print('PROBLÈMES:')
    for i in issues:
        print(' -', i)
    raise SystemExit(1)
if len(html) < 12000:
    print('TROP COURT (< 12 000 car) — rédaction insuffisante')
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19354.html'
open(out, 'w').write(html)
print('écrit:', out)
