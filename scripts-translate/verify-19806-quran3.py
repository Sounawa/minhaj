# -*- coding: utf-8 -*-
"""verify-19806-quran3.py — RAW des versets d'ancrage + résolution ibkār."""
import json, re, unicodedata

data = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json', encoding='utf-8'))

def bare(t):
    return ''.join(c for c in t if not unicodedata.category(c).startswith('M') and c != '\u0640').replace('\u0671', '\u0627')

corp = {}
for s in range(1, 115):
    corp[s] = [(i+1, bare(p[1]), p[1]) for i, p in enumerate(data.get(str(s), {}).get('ar', []))]

def hunt(sk, show=8):
    out = []
    for s, pairs in corp.items():
        for a, t, _ in pairs:
            if sk in t:
                out.append((s, a, t))
    print(f'[{sk}] = {len(out)}')
    for s, a, t in out[:show]:
        i = t.find(sk)
        print(f'   {s}:{a}  …{t[max(0,i-24):i+len(sk)+16]}…')
    return out

def show(s, a, hl=None):
    for s2, pairs in corp.items():
        for a2, t, raw in pairs:
            if s2 == s and a2 == a:
                frag = raw
                if hl and hl in raw:
                    i = raw.find(hl)
                    frag = '…' + raw[max(0, i-60):i+len(hl)+40] + '…'
                print(f'--- {s}:{a} ---')
                print('  RAW:', frag)

print('=== IBKAR : formes sans alif ===')
hunt('بكر', 10)

print('=== RAW ABKAR ===')
show(56, 36, 'أبكار')
show(66, 5, 'أبكار')

print('=== RAW des ancrages ===')
show(16, 92, 'أنكث')
show(37, 56, 'كدت')
show(79, 25, 'نكال')
show(2, 66, 'نكلا')
show(5, 38, 'نكلا')
show(18, 81, 'زكوة')
show(19, 13, 'زكوة')
show(30, 39, 'زكوة')
show(23, 4, 'زكوة')
show(2, 43, 'زكوة')
show(64, 2, 'كافر')
show(2, 41, 'كافر')

print('=== AKIFA / MIKIL ===')
hunt('عاكفا', 5)
hunt('ميكىل', 5)

print('=== 78:40 / 25:55 (singuliers kafir) ===')
show(78, 40, 'كافر')
show(25, 55, 'كافر')
