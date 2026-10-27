#!/usr/bin/env python3
# build-19377.py — 19377 « Jurisprudence : les moyens d'établir l'état du
# failli » (fiqh-tanawi-3, lessons[7], badge Leçon 9/33) — suite du bāb du
# taflīs, cinquième cours consécutif (3e → 4e → 5e). 2 axes (les moyens
# d'établir l'état : serment d'absence + serment réciproque + contradiction
# des preuves ; la durée de l'emprisonnement + dignité du débiteur).
# TROIS fentes de versets complétées (1re fois dans le fichier) : al-ʿĀdiyāt
# 6-8 / al-Baqara 280 / al-Isrāʾ 70 — vérifiées au quran-cache.
# Coquille التعبيم (b/l) 4e occurrence. 32e fente vide du fil.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19377_{i}.html').read())
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
for probe in ['les moyens d’établir l’état du failli', 'cinquième cours',
              'nāḍḍ', 'Sourate al-ʿĀdiyāt', 'al-Baqara', 'al-Isrāʾ',
              'istishhāb', 'transmettrice', 'maintenue', 'ḥamīl', 'taʿzīr',
              'Ibn Nāğī', 'ad-Dasūqī', 'al-Māzarī', 'Šarḥ at-talqīn',
              'donnant à l’inexistant la situation de l’existant',
              'La sauvegarde de l’honneur relève de la sauvegarde de la personne',
              'trente-deuxième fente vide', 'at-taʿbīm', 'Deuxièmement',
              'maqāṣid aš-šarīʿa', 'Leçon 9 / 33',
              'accordez un sursis jusqu’à ce qu’il soit dans l’aisance',
              'Nous avons honoré les fils d’Adam',
              'violent dans l’amour du bien']:
    if probe not in html:
        issues.append(f'sonde attendue absente: {probe}')
n_li = html.count('<li>')
print(f'caractères: {len(html)}')
print(f'entrées li: {n_li}')
print(f'em: {html.count("<em>")} | sup: {html.count("<sup>")}')
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

out = '/home/z/my-project/tr-tmp/19377.html'
open(out, 'w').write(html)
print('écrit:', out)
