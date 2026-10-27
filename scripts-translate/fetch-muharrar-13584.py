#!/usr/bin/env python3
# fetch-muharrar-13584.py — Muḥarrar al-wajīz (quran-tafsir.net/atia) — Naḥl 81-85
# + extraction des versets du quran-cache (Naḥl 81-85 ; Nūr 53 ; Mursalāt 35-36 ; Zalzala 8-9 ; Kahf 52 ; Furqān 13-14 ; Anbiyā 107)
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
    open(f'/home/z/my-project/tr-tmp/13584-muharrar-{a}.txt', 'w').write(txt)
    print(f'=== MUHARRAR AYA {a} : {len(txt)} car ===')

for a in (81, 82, 83, 84, 85):
    try:
        fetch(a)
    except Exception as e:
        print(f'!!! Echec aya {a}: {e}')

print('=' * 60)
c = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))
def show(sura, aya1, aya2=None, label=''):
    s = c[str(sura)]
    keys = [k for k in s.keys() if k not in ('number', 'englishName', 'nAyahs')]
    rng = range(aya1, (aya2 or aya1) + 1)
    print(f'### {label or sura} {aya1}' + (f'-{aya2}' if aya2 else ''))
    for k in keys:
        arr = s[k]
        for n, txt in arr:
            if n in rng:
                print(f'[{sura}:{k}:{n}] {txt[:400]}')
    print('-' * 40)

show(16, 81, 85, 'AN-NAHL')
show(24, 53, None, 'AN-NUR')
show(77, 35, 36, 'AL-MURSALAT')
show(99, 8, 9, 'AZ-ZALZALA')
show(18, 52, None, 'AL-KAHF')
show(25, 13, 14, 'AL-FURQAN')
show(21, 107, None, 'AL-ANBIYA (cité au sein de ar-Rāzī)')
