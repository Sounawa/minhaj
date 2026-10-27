#!/usr/bin/env python3
"""Build 13478 — Sourate an-Naḥl, versets 24-29 (tafsir-tanawi-1, lessons[5], badge Leçon 7 / 32)."""
import pathlib, re

parts = []
for i in range(1, 8):
    p = pathlib.Path(f'/home/z/my-project/tr-tmp/13478.f{i}.html')
    parts.append(p.read_text(encoding='utf-8').strip())

html = '\n'.join(parts) + '\n'

out = pathlib.Path('/home/z/my-project/tr-tmp/13478.html')
out.write_text(html, encoding='utf-8')
print(f'OK {out} — {len(html)} car')

# --- Auto-vérifs pré-QA (protocole rodé) ---
arb = re.findall(r'[\u0600-\u06FF]', html)
print('arabe:', len(arb))
print('apostrophes droites:', html.count("'"))
print('cyrillique:', len(re.findall(r'[\u0400-\u04FF]', html)))
guo, guf = html.count('«'), html.count('»')
print(f'guillemets: {guo} ouvrants / {guf} fermants — {"OK" if guo == guf else "DÉSÉQUILIBRE"}')
ang = re.findall(r'\b(the|and|with|from|this|that|which)\b', html)
print('mots anglais suspects:', ang[:5] if ang else 'aucun')
tags = sorted(set(re.findall(r'</?([a-z0-9]+)[ >]', html)))
print('balises:', tags)
# citation Ghafir 73 restaurée ? + coquille Dukhān signalée ?
print('Ghāfir 73:', 'Ghāfir, 73' in html)
print('coquille Dukhān signalée:', 'ad-Dukhān : 46' in html)
print('span-crochets signalé:', 'crochets coraniques' in html)
