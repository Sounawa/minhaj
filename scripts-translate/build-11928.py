#!/usr/bin/env python3
"""Build 11928 — Les règles de l'acquittement de la dette (qadāʾ al-dayn)."""
import pathlib

parts = []
for i in range(1, 8):
    p = pathlib.Path(f'/home/z/my-project/tr-tmp/11928.f{i}.html')
    parts.append(p.read_text(encoding='utf-8').strip())

html = '\n'.join(parts) + '\n'

# Retouches de cohérence (accords, précisions)
fixes = [
    # unicité de l'annonce des axes (l'imprimé dit « trois axes » — cohérent ici)
    ('<p>Cette leçon comporte trois axes :</p>', '<p>Cette leçon comporte trois axes :</p>'),
]
for old, new in fixes:
    html = html.replace(old, new)

out = pathlib.Path('/home/z/my-project/tr-tmp/11928.html')
out.write_text(html, encoding='utf-8')
print(f'OK {out} — {len(html)} car')
