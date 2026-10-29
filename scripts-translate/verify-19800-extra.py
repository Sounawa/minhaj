# -*- coding: utf-8 -*-
"""Sondes complémentaires 19800 (R345) : šurakāʾ (iʿdād), ṣāliḥāt/ṣāffāt (istitimār E1/E2),
et vérification des versets vedettes cités dans la rédaction."""
import json, re, unicodedata

CACHE = '/home/z/my-project/scripts-translate/quran-cache.json'
data = json.load(open(CACHE, encoding='utf-8'))

def bare(t):
    t = ''.join(c for c in t if not unicodedata.category(c).startswith('M'))
    t = t.replace('\u0671', '\u0627')  # alif wasla -> alif
    return t

def ay(s, a):
    try:
        return bare(data[str(s)]['ar'][a-1][1])
    except Exception:
        return None

def hunt(sk, limit=0, word=True):
    """Cherche le squelette dans tout le corpus, retourne [(s:a, ctx)]"""
    out = []
    pat = re.compile(r'(?<![\u0600-\u06FF])' + sk if word else sk)
    for s in range(1, 115):
        ars = data.get(str(s), {}).get('ar', [])
        for i, pair in enumerate(ars):
            t = bare(pair[1])
            if (word and re.search(r'(?<![\u0621-\u064A])' + re.escape(sk) + r'(?![\u0621-\u064A])', t)) or \
               (not word and sk in t):
                out.append((s, i+1, t))
    return out

print('=== 1. ŠURAKĀʾ (iʿdād kāf, pour 19805) ===')
for sk, lab in [('شركا','élidé nu شركا'), ('شركاء','constant شركاء'), ('شركؤا','exotique شركؤا'), ('شركؤ','شركؤ'), ('شركوا','شركوا'), ('شركاوا','شركاوا')]:
    r = hunt(sk, word=True)
    print(f'[{lab}] word-boundary = {len(r)}')
    for s, a, t in r[:14]:
        print(f'   {s}:{a}  …{t[max(0,t.find(sk)-25):t.find(sk)+len(sk)+20]}…')

print()
print('=== 2. ṢĀLIḤĀT / ṢĀFFĀT (istitimār ad-Dānī E1/E2) ===')
for sk, lab in [('صلحت','élidé صلحت'), ('صالحت','constant صالحت'), ('صففت','élidé صففت'), ('صاففت','constant صاففت'), ('قنتت','élidé قنتت'), ('تئبت','تئبت'), ('سئحت','سئحت'), ('عبدت','عبدت'), ('ثيبت','ثيبت')]:
    r = hunt(sk, word=True)
    print(f'[{lab}] = {len(r)}')
    for s, a, t in r[:10]:
        print(f'   {s}:{a}  …{t[max(0,t.find(sk)-22):t.find(sk)+len(sk)+18]}…')

print()
print('=== 3. VEDETTES CITÉES (vérification verbatim) ===')
checks = [
    (37,30,'سلطن'), (37,30,'طغين'),
    (66,5,'تئبت'), (66,5,'سئحت'), (66,5,'عبدت'), (66,5,'ثيبت'), (66,5,'قنتت'), (66,5,'مسلمت'), (66,5,'مؤمنت'),
    (79,11,'عظما'), (36,78,'العظم'), (2,259,'العظام'), (75,3,'عظامه'),
    (4,97,'ظالمى'), (16,28,'ظالمى'), (21,14,'ظلمين'), (29,14,'ظلمون'), (2,124,'الظلمي'),
    (70,15,'لظى'), (92,14,'تلظى'), (3,159,'فظا'), (4,80,'حفيظا'),
    (2,238,'قنتين'), (6,153,'صرطى'), (4,68,'صرطا'),
    (79,2,'النشطت'), (79,2,'نشطا'), (37,1,'الصفت'), (37,1,'صفا'),
    (4,34,'صلحت'), (4,34,'قنتت'), (4,34,'حفظت'), (33,35,'الحفظت'), (33,35,'الصئمت'),
    (2,15,'طغين'), (68,31,'طغين'), (78,22,'للطغين'), (37,30,'طغين'),
    (51,53,'طاغون'), (52,32,'طاغون'),
    (15,17,'شيطن'), (22,3,'شيطن'), (37,7,'شيطن'), (81,25,'شيطن'), (4,60,'الشيطن'),
    (16,99,'سلطن'), (17,65,'سلطن'), (37,30,'سلطن'), (3,151,'سلطنا'),
    (56,65,'حطما'), (39,21,'حطما'), (57,20,'حطما'), (104,4,'الحطمة'),
    (6,38,'طئر'), (17,13,'طئره'), (27,47,'طئركم'), (36,19,'طئركم'), (7,131,'طئرهم'),
    (7,201,'طئف'),
    (2,256,'الطغوت'), (4,51,'الطغوت'),
    (26,51,'خطينا'), (20,73,'خطينا'), (12,91,'لخطين'), (2,58,'خطيكم'), (2,81,'خطيته'),
    (31,20,'ظهرة'), (34,18,'ظهرة'), (6,120,'ظهر'), (9,48,'ظهر'), (6,151,'ظهر'), (9,8,'يظهروا'),
    (2,143,'وسطا'), (71,19,'بساطا'), (18,14,'شططا'), (73,6,'وطا'), (4,92,'خطا'),
    (20,50,'أعطى'), (92,5,'أعطى'), (54,29,'تعاطى'), (75,33,'يتمطى'), (11,92,'أرهطى'), (53,34,'وأكدى'),
    (21,104,'كطى'),
    (12,64,'حفظا'), (21,32,'محفوظا'), (41,12,'حفظا'), (4,21,'غليظا'),
    (2,285,'أطعنا'), (4,80,'يطع'), (3,32,'أطيعوا'), (4,80,'أطاع'), (23,34,'أطعتم'),
    (9,53,'طوعا'),
]
bad = 0
for s, a, sk in checks:
    t = ay(s, a)
    ok = t is not None and sk in t
    if not ok:
        bad += 1
        print(f'  !! {s}:{a} — "{sk}" ABSENT : {t[:110] if t else None}')
print(f'vedettes vérifiées : {len(checks)-bad}/{len(checks)} OK, {bad} écart(s)')

print()
print('=== 4. رasm l-ẓā D2 (16 constantes) rapide ===')
for sk, lab in [('لظى','لظى'), ('تلظى','تلظى')]:
    r = hunt(sk, word=True)
    print(f'[{lab}] = {len(r)} :', [(s,a) for s,a,_ in r][:8])
