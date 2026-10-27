#!/usr/bin/env python3
# build-19373.py — 19373 « Jurisprudence : la garantie du droit du créancier
# et l'établissement de l'état du failli » (fiqh-tanawi-3, lessons[6], badge
# Leçon 8/33) — suite du bāb du taflīs, accomplissement des TROIS annonces de
# l'الإعداد القبلي de 19367 (règle ax). 4 axes (survenance après partage des
# héritiers / perte du lot du créancier absent / ce qui est laissé au failli /
# règles de la rétention, 3 états). ZÉRO āya / ZÉRO hadith ; refs d'OUVRAGES :
# Mudawwana 4/80, Dhakhīra 7/361. 4 objectifs (les cours précédents en
# portaient 3). Coquille التعبيmm (b/l) 3e occurrence. 31e fente vide du fil.
import re

parts = []
for i in range(1, 6):
    parts.append(open(f'/home/z/my-project/tr-tmp/fr19373_{i}.html').read())
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
    o, c = html.count(f'<{tag}>'), html.count(f'</{tag}>')
    if tag in ('br',):
        continue
    if o != c:
        issues.append(f'balises {tag} non appariées: {o} / {c}')
# sondes attendues dans l'article
for probe in ['la garantie du droit du créancier', 'l’établissement de l’état du failli',
              'quatrième cours', 'l’antériorité du créancier', 'Deux sens',
              'Mudawwana', 'Dhakhīra', 'Saḥnūn', 'Ibn Rushd', 'al-Lakhmī',
              'la sauvegarde de la personne est antérieure à la sauvegarde du bien',
              'garant de la personne', 'garant par le bien',
              'Troisièmement', 'Quatrièmement', 'dastan',
              'les droits ne s’éteignent point par prescription' ]:
    if probe == 'les droits ne s’éteignent point par prescription':
        continue  # sonde du doc 19367, non attendue ici
    if probe not in html:
        issues.append(f'sonde attendue absente: {probe}')
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

out = '/home/z/my-project/tr-tmp/19373.html'
open(out, 'w').write(html)
print('écrit:', out)
