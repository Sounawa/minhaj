#!/usr/bin/env python3
# fetch-muharrar-13527.py — Muḥarrar al-wajīz (quran-tafsir.net/atia) — Naḥl 41-44
# + extraction des versets du quran-cache (Naḥl 41-44, Yūnus 2, Muʾminūn 33-34)
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
    open(f'/home/z/my-project/tr-tmp/13527-muharrar-{a}.txt', 'w').write(txt)
    print(f'=== MUHARRAR AYA {a} : {len(txt)} car ===')
    print(txt[:5500])
    print('...\n')

for a in (41, 42, 43, 44):
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

print('### AN-NAHL 41-44')
show(16, 41, 44)
print('### YUNUS 2')
show(10, 2)
print('### AL-MUMINUN 33-34')
show(23, 33, 34)
