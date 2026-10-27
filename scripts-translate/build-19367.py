#!/usr/bin/env python3
# build-19367.py — 19367 « Jurisprudence : les règles de la vente du bien du
# failli et l'acquittement de ses dettes » (fiqh-tanawi-3, lessons[5], badge
# Leçon 7/33) — leçon de fiqh COMPLÈTE : matn du taflīs (vente hâtée/patientée,
# partage au prorata, évaluation de la dette contraire au numéraire, muḥāṣṣa
# de l'épouse, dette survenante) + 3 axes (2 h4 chacun) + contrôle (2 situations
# chiffrées) + exploitation (Ibn al-Ḥājib, Jāmiʿ al-Ummahāt 166) + préparation
# (annonce du doc suivant) + sens de la leçon (3 p) + 11 N.d.T.
# ZÉRO āya, ZÉRO hadith — aucun slot coranique ; références de commentaire :
# Sharḥ al-Zarqānī 5/483, Mawāhib al-Jalīl 5/42, Jāmiʿ al-Ummahāt 166.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19367_{i}.html').read())
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
for tag in ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'em', 'span']:
    o, c = html.count(f'<{tag}>'), html.count(f'</{tag}>')
    if o != c:
        issues.append(f'balises {tag} non appariées: {o} / {c}')
# sondes de contenu attendues (leçons de structure + matn + axes + maximes)
for probe in ['deux mois', 'juzʾ as-sahm', 'Mawāhib al-Jalīl', 'Jāmiʿ al-Ummahāt',
              'al-ġunm bil-ġurm', 'Aṣbagh', 'Ibn al-Ḥājib', 'Le sens de cette leçon',
              'Notes du traducteur', 'part de solde', 'Leçon 7 / 33',
              'Sharḥ al-Zarqānī', 'pension de l’enfant', 'ne tombent point par la prescription']:
    if probe not in html:
        issues.append(f'sonde absente: {probe}')
# typo résiduelle
for bad in ['faibi', 'préalale']:
    if bad in html:
        issues.append(f'typo résiduelle: {bad}')
n_li = html.count('<li>')
print(f'caractères: {len(html)}')
print(f'entrées li: {n_li}')
print(f'em: {html.count("<em>")}')
print(f'guillemets: {html.count("«")}/{html.count("»")}')
print(f'ul: {html.count("<ul>")} | ol: {html.count("<ol>")}')
if issues:
    print('PROBLÈMES:')
    for i in issues:
        print(' -', i)
    raise SystemExit(1)
if len(html) < 12000:
    print('TROP COURT (< 12 000 car) — rédaction insuffisante')
    raise SystemExit(1)

out = '/home/z/my-project/tr-tmp/19367.html'
open(out, 'w').write(html)
print('écrit:', out)
