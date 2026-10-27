#!/usr/bin/env python3
# fetch-muharrar-13587.py — Muḥarrar al-wajīz (quran-tafsir.net/atia) — Naḥl 68-70
import re, html, urllib.request

def fetch(a):
    url = f'https://quran-tafsir.net/atia/sura16-aya{a}.html'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    t = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'replace')
    t = re.sub(r'<script.*?</script>', '', t, flags=re.S)
    t = re.sub(r'<style.*?</style>', '', t, flags=re.S)
    t = re.sub(r'<[^>]+>', '\n', t)
    t = html.unescape(t)
    t = re.sub(r'[ \t]+', ' ', t)
    lines = [l.strip() for l in t.split('\n') if l.strip()]
    txt = '\n'.join(lines)
    open(f'/home/z/my-project/tr-tmp/13587-muharrar-{a}.txt', 'w', encoding='utf-8').write(txt)
    print(f'=== MUHARRAR AYA {a} : {len(txt)} car ===')

ok = 0
for a in (68, 69, 70):
    try:
        fetch(a)
        ok += 1
    except Exception as e:
        print(f'!!! Echec aya {a}: {e}')
print(f'FETCH {ok}/3 OK')
