#!/usr/bin/env python3
# fetch-muharrar-13547.py — Muḥarrar al-wajīz (quran-tafsir.net/atia) — Naḥl 75-77
# + extraction des versets du quran-cache (Naḥl 75-77 ; Baqara 2 & 252 ; Qamar 50 ; Luqman 27 ; Isra 70)
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
    open(f'/home/z/my-project/tr-tmp/13547-muharrar-{a}.txt', 'w').write(txt)
    print(f'=== MUHARRAR AYA {a} : {len(txt)} car ===')
    print(txt[:7000])
    print('...\n')

for a in (75, 76, 77):
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

print('### AN-NAHL 75-77')
show(16, 75, 77)
print('### AL-BAQARA 2')
show(2, 2)
print('### AL-BAQARA 252')
show(2, 252)
print('### AL-QAMAR 50')
show(54, 50)
print('### LUQMAN 27')
show(31, 27)
print('### AL-ISRA 70')
show(17, 70)
