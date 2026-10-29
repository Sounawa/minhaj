# -*- coding: utf-8 -*-
"""verify-19806-quran.py — sondes coraniques pour 19806 (le kāf II, R347)."""
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
        print(f'   {s}:{a}  …{t[max(0,i-22):i+len(sk)+18]}…')
    return out

def hunt_diac(mask, show=6):
    """cherche le motif diacritique exact dans le texte tashkilé"""
    out = []
    for s, pairs in corp.items():
        for a, _, raw in pairs:
            if mask in raw:
                out.append((s, a, mask))
    print(f'[DIAC {mask}] = {len(out)}')
    for s, a, m in out[:show]:
        print(f'   {s}:{a}')
    return out

print('=== 1. KADAT (V1) + ihtiraz KADA/KADU ===')
hunt('كدت', 10)
hunt_diac('كَدَتْ', 6)
hunt_diac('كَدْتُ', 6)
for sk in ('كاد', 'وآد'): hunt(sk, 8)

print('=== 2. MIKAL (V2) ===')
hunt('ميكال', 5)
hunt('ميكائيل', 5)

print('=== 3. ANKATH (V3) ===')
hunt('انكث', 5)

print('=== 4. MIŠKAWA (V4) ===')
hunt('مشكوة', 5)
hunt('مشكاة', 5)

print('=== 5. ZAKAWA (V5-V6) ===')
hunt('زكوة', 8)
hunt('الزكوة', 5)
hunt('زكاة', 5)

print('=== 6. NAKAL (V7-V10) ===')
hunt('نكلا', 5)
hunt('نكالا', 5)
hunt('نكل', 5)
hunt('انكالا', 5)
hunt('انكال', 5)

print('=== 7. IBKAR (V11-V13) ===')
hunt('ابكار', 8)
hunt('ابكارا', 5)

print('=== 8. KAFIRIN x55 + singulier (V14) ===')
hunt('كفرين', 3)
hunt('الكفرين', 3)
o = hunt('الكافرين', 3)
o = hunt('كافر', 0)
# comptes précis
for sk in ('كفرين', 'كافرين', 'كافر', 'كفرون', 'كافرون'):
    n = sum(1 for s, pairs in corp.items() for a, t, _ in pairs if sk in t)
    print(f'   count[{sk}] = {n}')

print('=== 9. ALIF FINALE APRES KAF (V15) : mots finissant kaf+alif/yaw ===')
pat = re.compile(r'(\S*كف[اىيو]\S*)')
seen = {}
for s, pairs in corp.items():
    for a, t, _ in pairs:
        for w in pat.findall(t):
            seen.setdefault(w, []).append((s, a))
for w, locs in sorted(seen.items(), key=lambda x: -len(x[1]))[:20]:
    print(f'   {w} ×{len(locs)}  ex: {locs[0][0]}:{locs[0][1]}')

print('=== 10. THABITNA / contexte du bayt ===')
hunt('ثبتن', 3)
