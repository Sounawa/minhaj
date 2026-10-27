#!/usr/bin/env python3
# build-16212.py — 16212 « Comment utiliser mon livre » (fiqh-tanawi-3,
# lessons[2], badge Leçon 4/33) — DOCUMENT TRÈS COURT (374 car AR, GT 494).
# DÉCOUVERTE MAJEURE : le h1 porte « Comment utiliser mon livre » (1re entrée
# du sommaire de la présentation, notée R293 « sans doc propre ») — le titleAr
# du registre (« compétences ») est une étiquette erronée ; le CORPS est VIDE
# (fente DATÉE 2e du fil — même date que 16211 —, fil d'Ariane répétant le
# titre, p vide, p d'une espace, fermetures vides). Enregistrement SANS
# INVENTION (convention tajwīd 17882) ; ≥ 12k par la lecture savante de la
# promesse du titre. ZÉRO āyāt, ZÉRO hadith — 4e application du protocole
# adapté (aucun cache coranique, aucun Muḥarrar).
import re

parts = []
for i in range(1, 5):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr16212_{i}.html').read())
html = ''.join(parts).strip()
html = html.replace("'", chr(0x2019))

issues = []
AR = re.compile('[' + ''.join(chr(a) + '-' + chr(b) for a, b in [
    (0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF),
    (0xFB50, 0xFDF9), (0xFDFB, 0xFDFF), (0xFE70, 0xFEFF)]) + ']')
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

out = '/home/z/my-project/tr-tmp/16212.html'
open(out, 'w').write(html)
print('écrit:', out)
