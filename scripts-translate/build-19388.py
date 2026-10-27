#!/usr/bin/env python3
# build-19388.py — 19388 « Jurisprudence : les jugements des dispositions du
# créancier sur ce qui est à lui chez le failli » (fiqh-tanawi-3, lessons[9],
# badge Leçon 11/33) — suite du bāb du taflīs, septième cours consécutif
# (4e → 5e → 6e → 7e). 3 régimes (dispositions du créancier : rupture du gage,
# rupture du partage, retour 5 situations ; ce dont le failli est le plus
# digne : fruit cueilli, produit survenu, exception des palmiers pollinisés ;
# défaillance du locataire : choix du loueur, préséances fonds → arroseur →
# gagiste). 2e citation prophétique du fichier (Muwaṭṭaʾ, palmiers pollinisés)
# ; Dhakhīra 5/474 ; fente tableau VIDE (2e fois) ; coquille التعبيم 6e
# occurrence ; 0 āya ; réseau de maximes al-ġunm bil-ġurm / al-ḫarāğ bi-ḍ-ḍamān.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19388_{i}.html').read())
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
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'em', 'span', 'br']:
    if tag in ('br',):
        continue
    o, c = html.count(f'<{tag}>'), html.count(f'</{tag}>')
    if o != c:
        issues.append(f'balises {tag} non appariées: {o} / {c}')
# sondes attendues dans l'article
for probe in ['les jugements des dispositions du créancier sur ce qui est à lui chez le failli',
              'septième leçon', 'septième cours', 'fakk ar-rahin', 'rupture du gage',
              'gagiste', 'arš', 'pollinisé', 'al-ġunm bil-ġurm', 'al-ḫarāğ bi-ḍ-ḍamān',
              'aḍ-ḍamān tabaʿ li-l-intifāʿ', 'al-manāfiʿ tatabbaʿ an-nafaqa',
              'Muwaṭṭaʾ', 'Quiconque vend des palmiers', 'Dhakhīra</em> 5/474',
              'al-Qarāfī', 'Ibn Yūnus', 'la place de sa main', 'Leçon 11 / 33',
              'trente-quatrième fente', 'at-taʿbīm', 'Deuxièmement', 'Troisièmement',
              'al-miṯliyyāt', 'wağība', 'tağdīd milk', 'samāwī', 'bi-t-tabʿ',
              'l’arroseur', 'Livre des ventes']:
    if probe not in html:
        issues.append(f'sonde attendue absente: {probe}')
n_li = html.count('<li>')
print(f'caractères: {len(html)}')
print(f'entrées li: {n_li}')
print(f'em: {html.count("<em>")} | span: {html.count("<span>")}')
print(f'guillemets: {html.count("«")}/{html.count("»")}')
print(f'ul: {html.count("<ul>")} | ol: {html.count("<ol>")}')
print(f'ﷺ: {html.count(chr(0xFDFA))}')
if issues:
    print('PROBLÈMES:')
    for i in issues:
        print(' -', i)
    raise SystemExit(1)
if len(html) < 12000:
    print('TROP COURT (< 12 000 car) — rédaction insuffisante')
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19388.html'
open(out, 'w').write(html)
print('écrit:', out)
