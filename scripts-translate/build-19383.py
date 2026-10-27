#!/usr/bin/env python3
# build-19383.py — 19383 « Jurisprudence : les options du créancier pour
# recouvrer son droit auprès du débiteur » (fiqh-tanawi-3, lessons[8], badge
# Leçon 10/33) — suite du bāb du taflīs, sixième cours consécutif (4e → 5e → 6e).
# 2 axes (quand le créancier l'emporte : 3 conditions ; quand il s'efface :
# 5 situations + divergence du prêt). PREMIÈRES citations prophétiques du
# fichier (Muwaṭṭaʾ buyūʿ + Sunan Abī Dāwūd) ; Mudawwana 3/239. Fente
# liminaire NON VIDE (date du cours, 1re fois) ; fente tableau VIDE au
# contrôle ; coquille التعبيم 5e occurrence ; 0 āya ; aswa al-ghuramāʾ =
# nouveau terme de famille.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19383_{i}.html').read())
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
for probe in ['les options du créancier pour recouvrer son droit auprès du débiteur',
              'sixième leçon', 'sixième cours', 'lundi 26 février 2024',
              'aswa al-ghuramāʾ', 'homologue des créanciers', 'al-muḥāz ʿan-hu',
              'mis à l’écart pour lui', 'Muwaṭṭaʾ', 'Abū Dāwūd', 'Abū Hurayra',
              'Mudawwana</em> 3/239', 'al-ḥiṣāṣ', 'buḍʿ', 'al-ʿiṣma', 'al-qiṣāṣ',
              'ḫulʿ', 'qabḍ ḥukmī', 'Leçon 10 / 33', 'trente-troisième fente',
              'at-taʿbīm', 'muskūk', 'ḥamīl', 'Deuxièmement', 'al-mudāyana',
              'tukkuri', 'salaf', 'faʿīl bi-maʿnā mafʿūl', 'al-maqāwīm']:
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

out = '/home/z/my-project/tr-tmp/19383.html'
open(out, 'w').write(html)
print('écrit:', out)
