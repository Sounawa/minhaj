#!/usr/bin/env python3
"""Build 13508 — Sourate an-Naḥl, versets 36-40 (tafsir-tanawi-1, lessons[7], badge Leçon 9 / 32)."""
import pathlib, re

parts = []
for i in range(1, 8):
    p = pathlib.Path(f'/home/z/my-project/tr-tmp/13508.f{i}.html')
    parts.append(p.read_text(encoding='utf-8').strip())

html = '\n'.join(parts) + '\n'

out = pathlib.Path('/home/z/my-project/tr-tmp/13508.html')
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
print('Tawba 106:', 'at-Tawba, 106' in html, '| Āl 164:', 'Āl ʿImrān, 164' in html, '| Naḥl 64:', 'an-Naḥl, 64' in html)
print('blocs restaurés (notes inline):', html.count('restaurée d’après le corpus canonique'))
