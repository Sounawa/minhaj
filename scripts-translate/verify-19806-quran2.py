# -*- coding: utf-8 -*-
"""verify-19806-quran2.py — sondes complémentaires (hamza, positions détaillées)."""
import json, re, unicodedata

data = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json', encoding='utf-8'))

def bare(t):
    return ''.join(c for c in t if not unicodedata.category(c).startswith('M') and c != '\u0640').replace('\u0671', '\u0627')

corp = {}
for s in range(1, 115):
    corp[s] = [(i+1, bare(p[1]), p[1]) for i, p in enumerate(data.get(str(s), {}).get('ar', []))]

def hunt(sk, show=10):
    out = []
    for s, pairs in corp.items():
        for a, t, _ in pairs:
            if sk in t:
                out.append((s, a, t))
    print(f'[{sk}] = {len(out)}')
    for s, a, t in out[:show]:
        i = t.find(sk)
        print(f'   {s}:{a}  …{t[max(0,i-20):i+len(sk)+20]}…')
    return out

def show(s, a):
    for s2, pairs in corp.items():
        for a2, t, raw in pairs:
            if s2 == s and a2 == a:
                print(f'--- {s}:{a} ---')
                print('  RAW:', raw)
                print('  BARE:', t)

print('=== MIKAIL 2:98 ===')
show(2, 98)

print('=== ANKATH : toutes formes ===')
hunt('نكث', 10)
hunt('انكث', 5)

print('=== IBKAR (hamza) ===')
hunt('بكار', 10)
hunt('إبكار', 5)
hunt('أبكار', 5)

print('=== NAKAL (V9/V10) ===')
hunt('نكال', 10)

print('=== ZAKAWA sans AL (indéfinies) ===')
for s, pairs in corp.items():
    for a, t, _ in pairs:
        if 'زكوة' in t:
            # occurrences hors ال
            for m in re.finditer(r'(?<!ال)زكوة', t):
                i = m.start()
                print(f'   {s}:{a}  …{t[max(0,i-28):i+12]}…')

print('=== KAFIR singulier (6) ===')
hunt('كافر', 8)

print('=== KAFIRIN sans AL (36 positions) ===')
cnt = 0
for s, pairs in corp.items():
    for a, t, _ in pairs:
        if 'كفرين' in t and 'الكفرين' not in t:
            cnt += 1
            if cnt <= 12:
                i = t.find('كفرين')
                print(f'   {s}:{a}  …{t[max(0,i-24):i+14]}…')
print(f'   total versets كفرين sans ال = {cnt}')

print('=== KAFIRIN avec AL mais pas مألوفة (les autres de 91) ===')
n2 = sum(1 for s, pairs in corp.items() for a, t, _ in pairs if 'الكفرين' in t)
print(f'   الكفرين = {n2}')

print('=== KAFI vs alif finale ===')
pat = re.compile(r'\S*كفا$')
seen = {}
for s, pairs in corp.items():
    for a, t, _ in pairs:
        for w in t.split():
            if pat.match(w):
                seen.setdefault(w, []).append((s, a))
print('   mots finissant كف+ا pleine:', {w: len(v) for w, v in seen.items()})

print('=== RAW 24:35 (miškawa) ===')
show(24, 35)
print('=== RAW 73:12 (ankala) ===')
show(73, 12)
print('=== RAW 17:74 (kadat + thabbatnak) ===')
show(17, 74)
