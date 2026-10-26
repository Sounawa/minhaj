#!/usr/bin/env python3
"""Build 11934 — Les ventes vicieuses (al-bayʿāt al-fāsida)."""
import pathlib

parts = []
for i in range(1, 8):
    p = pathlib.Path(f'/home/z/my-project/tr-tmp/11934.f{i}.html')
    parts.append(p.read_text(encoding='utf-8').strip())

html = '\n'.join(parts) + '\n'

out = pathlib.Path('/home/z/my-project/tr-tmp/11934.html')
out.write_text(html, encoding='utf-8')
print(f'OK {out} — {len(html)} car')
