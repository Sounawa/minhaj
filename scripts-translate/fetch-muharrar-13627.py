#!/usr/bin/env python3
# fetch-muharrar-13627.py — consultation du Muḥarrar original en ligne (règle x)
# Muḥarrar = quran-tafsir.net/atia — sourate 16, āyāt 92 (دخل 1re occurrence) et 94..97
import urllib.request, re

BASE = 'https://quran-tafsir.net/atia/sura16-aya{}.html'
OUT = '/home/z/my-project/tr-tmp/muharrar-13627-aya{}.html'

for aya in (92, 94, 95, 96, 97):
    url = BASE.format(aya)
    dst = OUT.format(aya)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'replace')
        open(dst, 'w', encoding='utf-8').write(html)
        txt = re.sub(r'<script.*?</script>', ' ', html, flags=re.S)
        txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
        txt = re.sub(r'<[^>]+>', ' ', txt)
        txt = re.sub(r'\s+', ' ', txt)
        print(f'=== aya {aya} — fetch OK ({len(html)} bytes) — {len(txt)} car texte ===')
        print(txt[:3200])
        print()
    except Exception as e:
        print(f'=== aya {aya} — FETCH ERR: {e} ===')
print('--- fetch-muharrar-13627 terminé ---')
