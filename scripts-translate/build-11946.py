#!/usr/bin/env python3
"""Build 11946 — Les effets de la vente vicieuse et ses « passatoires » (mufawwitāt)."""
import pathlib

parts = []
for i in range(1, 9):
    p = pathlib.Path(f'/home/z/my-project/tr-tmp/11946.f{i}.html')
    parts.append(p.read_text(encoding='utf-8').strip())

html = '\n'.join(parts) + '\n'

out = pathlib.Path('/home/z/my-project/tr-tmp/11946.html')
out.write_text(html, encoding='utf-8')
print(f'OK {out} — {len(html)} car')
