# -*- coding: utf-8 -*-
"""Passe 2 : normalisation hamza + sondes IN + bruts des versets clés."""
import json, re

QC = '/home/z/my-project/scripts-translate/quran-cache.json'
cache = json.load(open(QC, encoding='utf-8'))

def bare(s):
    s = re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A\u0653\u0654\u0655]', '', s)
    s = s.replace('\u0671', '\u0627')
    for h in '\u0623\u0625\u0622\u0653':
        s = s.replace(h, '\u0627')
    return s

def words(b):
    return re.findall(r'[\u0621-\u064A]+', b)

CORPUS = []
for sura, v in cache.items():
    for idx, pair in enumerate(v['ar']):
        b = bare(pair[1])
        for w in words(b):
            CORPUS.append((int(sura), pair[0], pair[1], w))

def search(name, sk, exact=False, limit=15):
    res, seen = [], set()
    for sura, ayah, full, w in CORPUS:
        if (w == sk) if exact else (sk in w):
            k = (sura, ayah)
            if k not in seen:
                seen.add(k); res.append((sura, ayah, w))
    print(f'== {name} [{sk}] exact={exact} : {len(seen)} versets')
    for sura, ayah, w in res[:limit]:
        print(f'   {sura}:{ayah} {w}')
    return res

def brut(sura, ayah, fragment=None):
    t = cache[str(sura)]['ar'][ayah-1][1]
    b = bare(t)
    ctx = ''
    if fragment:
        i = b.find(fragment)
        if i >= 0:
            ctx = ' |ctx: ' + b[max(0,i-25):i+len(fragment)+25]
    print(f'BRUT {sura}:{ayah} bare{ctx}')
    print('   raw: ' + t[:220])

print('===== A. VEDettes restées a 0 (sondes IN) =====')
search('adh-dhakirat IN', 'ذاكرت')
search('muasir IN', 'معصر')
search('majhar/maghar IN', 'مغار')
search('majrat IN', 'مجرت')
search('zajir IN', 'زاجر')
search('muhajir IN', 'مهاجر')
search('marrat (bare-shadda) IN', 'مرت')
search('marrat exact', 'مرت', True)
search('hujur IN', 'حجر')
search('rashidun IN', 'رشدون')
search('rasikhun IN', 'رسخون')
search('rasikhun bare-IN', 'اسخون')
search('tantasir/tanasar IN', 'تناصر')
search('tantasr IN', 'تنتصر')
search('bahrayn IN', 'بحرين')
search('bahran IN', 'بحرن')
search('ibrahim IN', 'ابرهيم')
search('ibrahim alif IN', 'ابراهيم')
search('ulai IN', 'اولائك')
search('ulai IN2', 'اولئك')
search('malaik IN', 'ملائك')
search('muraghama exact', 'مرغما', True)
search('tarawad IN', 'راود')
search('tarawd IN', 'تراو')
search('arayt IN', 'ارايت')
search('arahayt IN', 'ارايتتم')
search('darahim IN', 'درهم')
search('daraahim IN', 'دراهيم')
print()
print('===== B. BRUTS DES VERSETS CLES =====')
brut(9, 57, 'مغرت')
brut(24, 58, 'مرت')
brut(2, 232, 'ترضوا')
brut(9, 96, 'ترضوا')
brut(21, 95, 'حر')
brut(25, 61, 'سرج')
brut(33, 46, 'سراج')
brut(71, 16, 'سراج')
brut(78, 13, 'سراج')
brut(12, 20, 'درهم')
brut(4, 100, 'مرغم')
brut(3, 7, 'اسخ')
brut(16, 76, 'رشد')
brut(18, 60, 'بحر')
brut(2, 31, 'هؤلاء')
brut(2, 21, 'يأيها')
brut(2, 34, 'ملائك')
brut(2, 27, 'اولئك')
brut(33, 35, 'ذاكر')
brut(55, 70, 'خيرت')
brut(12, 43, 'بقرت')
brut(13, 4, 'متجورت')
brut(3, 33, 'عمرن')
brut(37, 48, 'قصرت')
brut(52, 20, 'قصر')
brut(4, 19, 'راود')
brut(12, 26, 'راود')
brut(12, 51, 'راود')
