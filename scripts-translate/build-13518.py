#!/usr/bin/env python3
"""Build 13518 — Sourate an-Naḥl, versets 51-56 (tafsir-tanawi-1, lessons[8], badge Leçon 10 / 32)."""
import pathlib, re

parts = []
for i in range(1, 8):
    p = pathlib.Path(f'/home/z/my-project/tr-tmp/13518.f{i}.html')
    parts.append(p.read_text(encoding='utf-8').strip())

html = '\n'.join(parts) + '\n'

# Post-traitement : apostrophes droites du FR du cache -> courbes (convention chantier)
html = html.replace("'", "’")

out = pathlib.Path('/home/z/my-project/tr-tmp/13518.html')
out.write_text(html, encoding='utf-8')
print(f'OK {out} — {len(html)} car')

# --- Auto-vérifs pré-QA (protocole rodé) ---
arb = re.findall(r'[\u0600-\u06FF\uFD3E\uFD3F]', html)
print('arabe (incl. crochets ornés):', len(arb))
if arb:
    for m in re.finditer(r'.{40}[\u0600-\u06FF\uFD3E\uFD3F]+.{40}', html):
        print('  ctx:', m.group(0)[:100])
        break
print('apostrophes droites:', html.count("'"))
print('cyrillique:', len(re.findall(r'[\u0400-\u04FF]', html)))
guo, guf = html.count('«'), html.count('»')
print(f'guillemets: {guo} ouvrants / {guf} fermants — {"OK" if guo == guf else "DÉSÉQUILIBRE"}')
ang = re.findall(r'\b(the|and|with|from|this|that|which)\b', html)
print('mots anglais suspects:', ang[:5] if ang else 'aucun')
tags = sorted(set(re.findall(r'</?([a-z0-9]+)[ >]', html)))
print('balises:', tags)
print('Isrā 67:', 'al-Isrāʾ, 67' in html, '| Anʿām 137:', 'al-Anʿām, 137' in html, '| Anbiyā 21-24:', 'al-Anbiyāʾ, 21-24' in html, '| Zumar 8:', 'az-Zumar, 8' in html)
print('blocs restaurés (notes inline):', html.count('restaurée d’après le corpus canonique'))
print('candidats signalés:', html.count('ressort du traducteur'))
