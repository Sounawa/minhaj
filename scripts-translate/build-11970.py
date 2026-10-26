#!/usr/bin/env python3
"""Build 11970 — Les règles de la récolte et de la prise en charge après le retour du vendu."""
import pathlib

parts = []
for i in range(1, 10):
    p = pathlib.Path(f'/home/z/my-project/tr-tmp/11970.f{i}.html')
    parts.append(p.read_text(encoding='utf-8').strip())

html = '\n'.join(parts) + '\n'

out = pathlib.Path('/home/z/my-project/tr-tmp/11970.html')
out.write_text(html, encoding='utf-8')
print(f'OK {out} — {len(html)} car')
