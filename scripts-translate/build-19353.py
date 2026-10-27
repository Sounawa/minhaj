#!/usr/bin/env python3
# build-19353.py — 19353 « Glossaire des termes du Mukhtaṣar de Khalīl »
# (fiqh-tanawi-3, lessons[3], badge Leçon 5/33) — DOCUMENT TRÈS COURT
# (148 car AR, GT 158). CORPS ENTIÈREMENT VIDE : fente liminaire VIDE
# (28e du fil — retour au vide après les deux datées), p d'espace insécable,
# 2 p vides, div vide — glossaire promis par le h1 et non imprimé.
# Enregistrement SANS INVENTION (convention tajwīd 17882) ; ≥ 12k par la
# lecture savante de la promesse du titre. ZÉRO āyāt, ZÉRO hadith — 5e
# application du protocole adapté (aucun cache coranique, aucun Muḥarrar).
import re

parts = []
for i in range(1, 5):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19353_{i}.html').read())
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
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'li', 'em', 'span']:
    o, c = html.count(f'<{tag}'), html.count(f'</{tag}>')
    if o != c:
        issues.append(f'balises {tag} non appariées: {o} / {c}')
n_li = html.count('<li>')
print(f'caractères: {len(html)}')
print(f'entrées li: {n_li}')
print(f'em: {html.count("<em>")}')
print(f'guillemets: {html.count("«")}/{html.count("»")}')
if issues:
    print('PROBLÈMES:')
    for i in issues:
        print(' -', i)
    raise SystemExit(1)
if len(html) < 12000:
    print('TROP COURT (< 12 000 car) — rédaction insuffisante')
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19353.html'
open(out, 'w').write(html)
print('écrit:', out)
