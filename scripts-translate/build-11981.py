#!/usr/bin/env python3
"""Build 11981 — Index des sources et références (fihrist al-maṣādir) du manuel fiqh-tanawi-1."""
import pathlib

parts = []
for i in range(1, 10):
    p = pathlib.Path(f'/home/z/my-project/tr-tmp/11981.f{i}.html')
    parts.append(p.read_text(encoding='utf-8').strip())

html = '\n'.join(parts) + '\n'

out = pathlib.Path('/home/z/my-project/tr-tmp/11981.html')
out.write_text(html, encoding='utf-8')
print(f'OK {out} — {len(html)} car')
