# -*- coding: utf-8 -*-
"""Passe 3 : micro-sondes finales 19785."""
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

def search(name, sk, exact=False, limit=12):
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

def brut(sura, ayah, frag=None, tail=False):
    t = cache[str(sura)]['ar'][ayah-1][1]
    b = bare(t)
    ctx = ''
    if frag:
        i = b.find(frag)
        if i >= 0:
            ctx = ' | ' + b[max(0,i-30):i+len(frag)+30]
    if tail:
        print(f'BRUT {sura}:{ayah} TAIL: ...{t[-160:]}')
    else:
        print(f'BRUT {sura}:{ayah}{ctx}')
        if not frag:
            print('   ' + t[:250])

print('--- le rasm reel de malaika ---')
search('malaik rasm IN', 'ملئك')
brut(2, 34)
print('--- arayt : variants ---')
search('arit IN', 'اريت')
search('aray IN', 'ارا')
search('arai IN', 'اراي')
brut(2, 67)
brut(6, 40)
print('--- racine r-w-d (murawada) ---')
search('raw IN', 'راو')
search('rwd IN', 'راود')
search('traw IN', 'تراو')
search('straw IN', 'استرا')
brut(4, 19)
brut(12, 26)
brut(12, 51)
print('--- z-j-r (fa-z-zajirati) ---')
search('zjr IN', 'زجر')
search('zajr IN', 'زاجر')
print('--- tantasiran : brut 55:35 + char exact ---')
brut(55, 35)
t = cache['55']['ar'][34][1]
i = t.find('نتصر')
print('   chars autour de نتصر:', repr(t[max(0,i-10):i+15]))
print('--- sahran 20:63 (pattern duel elide, contre-point) ---')
search('sahrn exact', 'سحرن', True)
search('sihran 28:48', 'سحران', True)
print('--- 33:35 : adh-dhakirati (rasm dhkrt) ---')
search('dhkrt exact', 'ذكرت', True)
t = cache['33']['ar'][34][1]
i = t.find('ذكر')
print('   chars ذاكر:', repr(t[max(0,i-5):i+20]))
print('--- turab : les 17 loci complets ---')
r = search('turab complet', 'تراب', limit=20)
print('--- muasirat brut 78:14 + hajarat brut 49:4 ---')
brut(78, 14, 'معصرت')
brut(49, 4, 'حجرت')
print('--- 9:96 char exact taradaw ---')
t = cache['9']['ar'][95][1]
i = t.find('ترض')
print('   chars:', repr(t[max(0,i-8):i+15]))
print('--- 2:232 char exact ---')
t = cache['2']['ar'][231][1]
i = t.find('ترض')
print('   chars:', repr(t[max(0,i-8):i+15]))
print('--- rashidun brut 49:7 / 16:76 fin ---')
brut(49, 7, 'رشدون')
brut(16, 76, tail=True)
print('--- rasikhun brut 3:7 / 4:162 ---')
brut(3, 7, 'رسخون')
brut(4, 162, 'رسخون')
print('--- marra 24:58 dagger + marratayn 9:101 ---')
t = cache['24']['ar'][57][1]
i = t.find('مرت')
print('   24:58 chars:', repr(t[max(0,i-12):i+12]))
brut(9, 101, 'مرتين')
brut(9, 126, 'مرتين')
print('--- ulaihahum 2:27 char exact (madda/dagger) ---')
t = cache['2']['ar'][26][1]
i = t.find('ئ')
print('   2:27 chars:', repr(t[max(0,i-18):i+8]))
