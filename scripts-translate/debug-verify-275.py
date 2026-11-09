# -*- coding: utf-8 -*-
import re
v = open('scripts-translate/verify-ulumhadith2-pdf275.py', encoding='utf-8').read()
h = open('tr-tmp/lesson-uh2-pdf-mut23h2u-275-fr.html', encoding='utf-8').read()
hn = re.sub(r' +', ' ', h.replace('&nbsp;', ' ').replace('\u202f', ' ').replace('\u2009', ' '))

# extraire la chaîne exacte du verify entre "interpolé par ... et in hn
i = v.find('interpol\u00e9 par Ibn Ab\u012b Maryam')
j = v.find('" in hn', i)
pat = v[i:j]
print('pattern extrait:', repr(pat))
print('pattern in hn:', pat in hn)
if pat not in hn:
    i2 = h.find('interpol\u00e9 par Ibn Ab\u012b Maryam')
    seg = h[i2:i2+len(pat)+20]
    seg = re.sub(r' +', ' ', seg.replace('&nbsp;', ' ').replace('\u202f', ' ').replace('\u2009', ' '))
    n = 0
    for a, b in zip(pat, seg):
        if a != b:
            break
        n += 1
    print('préfixe commun:', n, '/', len(pat))
    print('pat  @', repr(pat[max(0, n-10):n+10]))
    print('html @', repr(seg[max(0, n-10):n+10]))
    print('codes pat :', [hex(ord(c)) for c in pat[max(0, n-2):n+4]])
    print('codes html:', [hex(ord(c)) for c in seg[max(0, n-2):n+4]])
