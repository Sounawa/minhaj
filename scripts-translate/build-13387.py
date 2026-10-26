#!/usr/bin/env python3
"""Build 13387 — Sourate an-Naḥl, versets 5-9 (tafsir-tanawi-1, lessons[2], badge Leçon 4 / 32)."""
import pathlib

parts = []
for i in range(1, 7):
    p = pathlib.Path(f'/home/z/my-project/tr-tmp/13387.f{i}.html')
    parts.append(p.read_text(encoding='utf-8').strip())

html = '\n'.join(parts) + '\n'

out = pathlib.Path('/home/z/my-project/tr-tmp/13387.html')
out.write_text(html, encoding='utf-8')
print(f'OK {out} — {len(html)} car')
