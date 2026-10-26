#!/usr/bin/env python3
"""Build 11923 — L'effet du vice dans le change (fiqh-tanawi-1, leçon 8)."""
import pathlib

parts = []
for i in range(1, 8):
    p = pathlib.Path(f'/home/z/my-project/tr-tmp/11923.f{i}.html')
    parts.append(p.read_text(encoding='utf-8').strip())

html = '\n'.join(parts) + '\n'

# Retouches de cohérence (correctifs de formulation appliqués aux fragments)
fixes = [
    # « s’en prévaut de son droit » -> « s’en prévaut » (économie de style constante)
    ('s’en prévaut de son droit — [à l’instar de]', 's’en prévaut — [à l’instar de]'),
    ('si le découvreur du vice s’en prévaut de son droit, en demandant', 'si le découvreur du vice s’en prévaut, en demandant'),
    ('l’échange est résilié si le découvreur du vice s’en prévaut de son droit, en demandant l’échange de la sous-pesante', 'l’échange est résilié si le découvreur du vice s’en prévaut, en demandant l’échange de la sous-pesante'),
    # harmonisation « tirer(s)-en »
    ('Lis le texte et tire(s)-en les règles', 'Lis le texte et tire(s)-en les règles'),
]
for old, new in fixes:
    html = html.replace(old, new)

out = pathlib.Path('/home/z/my-project/tr-tmp/11923.html')
out.write_text(html, encoding='utf-8')
print(f'OK {out} — {len(html)} car')
