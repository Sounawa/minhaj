#!/usr/bin/env python3
# fetch-muharrar-13537.py — Muḥarrar al-wajīz (quran-tafsir.net/atia) — Naḥl 45-50
# + extraction des versets du quran-cache (Naḥl 45-50)
import json, re, html, urllib.request

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
    m = re.search(r'المحرر الوجيز في تفسير الكتاب العزيز لابن عطية - ابن عطية\n', txt)
    if m:
        txt = txt[m.end():]
    open(f'/home/z/my-project/tr-tmp/13537-muharrar-{a}.txt', 'w').write(txt)
    print(f'=== MUHARRAR AYA {a} : {len(txt)} car ===')
    print(txt[:6000])
    print('...\n')

for a in (45, 46, 47, 48, 49, 50):
    try:
        fetch(a)
    except Exception as e:
        print(f'!!! Echec aya {a}: {e}')

print('=' * 60)
c = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))
def show(sura, aya1, aya2=None):
    s = c[str(sura)]
    keys = [k for k in s.keys() if k not in ('number', 'englishName', 'nAyahs')]
    rng = range(aya1, (aya2 or aya1) + 1)
    for k in keys:
        arr = s[k]
        for n, txt in arr:
            if n in rng:
                print(f'[{sura}:{k}:{n}] {txt}')
    print('-' * 40)

print('### AN-NAHL 45-50')
show(16, 45, 50)
