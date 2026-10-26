#!/usr/bin/env python3
"""Build 11927 — Les règles de la vente du plaqué (muḥallā), de l'échange et de la vente au poids (murāṭala)."""
import pathlib

parts = []
for i in range(1, 8):
    p = pathlib.Path(f'/home/z/my-project/tr-tmp/11927.f{i}.html')
    parts.append(p.read_text(encoding='utf-8').strip())

html = '\n'.join(parts) + '\n'

# Retouches de cohérence (accords, précisions)
fixes = [
    # accord grammatical : l'échange est masculin
    ('Et est permise l’échange par le compte', 'Et est permis l’échange par le compte'),
    ('« et est permise l’échange par le compte du peu compté', '« et est permis l’échange par le compte du peu compté'),
    # écho de l'exploitation : éviter la répétition « la vente de la vente au poids »
    ('les règles relatives à la vente de la vente au poids', 'les règles relatives à la vente au poids'),
    # harmonisation du préambule de l'analyse (l'imprimé dit « trois axes »)
    ('<p>Cette leçon comporte trois axes :</p>', '<p>Cette leçon comporte trois axes :</p>'),
]
for old, new in fixes:
    html = html.replace(old, new)

out = pathlib.Path('/home/z/my-project/tr-tmp/11927.html')
out.write_text(html, encoding='utf-8')
print(f'OK {out} — {len(html)} car')
