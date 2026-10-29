# -*- coding: utf-8 -*-
"""verify-20048-quran3.py — sondes 3 : recensement sīmāhum (2 rasm) + textes d'ancres."""
import json, re, unicodedata

data = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json', encoding='utf-8'))

def bare2(t):
    out = []
    for c in t:
        if unicodedata.category(c).startswith('M') or c == '\u0640':
            continue
        if c == '\u0622': c = '\u0627'
        if c == '\u0649': c = '\u064a'
        out.append(c)
    return ''.join(out).replace('\u0671', '\u0627')

W = lambda s: re.split(r'[\s\u00a0]+', s.strip())

def sous(chaine, label):
    print(f'\n## {label} — sous-chaîne «{chaine}»')
    n = 0
    for s in range(1, 115):
        for i, p in enumerate(data.get(str(s), {}).get('ar', [])):
            for w in W(p[1]):
                if chaine in bare2(w):
                    n += 1
                    print(f'   {s}:{i+1} «{w}»')
    print(f'   TOTAL = {n}')

# Recensement des DEUX rasm de sīmāhum
sous('سيمه', 'A1. sīmāhum — rasm yāʾ/alif-suscrite (سيمهم...)')
sous('سيماه', 'A2. sīmāhum — rasm alif pleine (سيماهم)')
sous('سليمن', 'B. Sulaymān — rasm sans alif (سليمن)')
sous('سليمان', 'B2. Sulaymān — variante alif pleine (si elle existe)')

# Textes exacts des ancres
ANCRES = [
    ('2:273', 'Baqara sīmāhum'), ('7:46', 'Aʿrāf 1'), ('7:47', 'Aʿrāf 2 ?'),
    ('47:30', 'Muḥammad'), ('55:41', 'Raḥmān'), ('48:29', 'Fatḥ ثبت'),
    ('5:107', 'yaqūmāni'), ('5:41', 'samāʿūn'), ('5:42', 'samāʿūn 2'),
    ('6:143', 'thamāniya 1'), ('6:144', 'thamāniya 2'), ('24:4', 'thamānīna'),
    ('28:27', 'thamāniyya nue'), ('69:17', 'thamāniya sing.'),
    ('2:17', 'ẓulumāt 1'), ('2:19', 'ẓulumāt 2'), ('22:28', 'maʿlūmāt 2'),
    ('27:30', 'Sulaymān'), ('27:88', 'tamurru'), ('77:33', 'jimālat'),
    ('76:18', 'tusammā'), ('28:28', 'ayyimā'), ('7:132', 'mahmā'),
    ('15:7', 'law mā'), ('15:2', 'rabamā'), ('18:110', 'innamā+annamā'),
    ('22:19', 'khaṣmāni'), ('3:106', 'fa-ammā'), ('3:107', 'fa-ammā 2'),
    ('7:20', 'duals 1'), ('7:21', 'duals 2'), ('7:22', 'duals 3'),
    ('30:9', 'ʿamarūhā'), ('93:3', 'mā waddaʿaka'),
]
print('\n## TEXTES DES ANCRES')
for ref, label in ANCRES:
    s, v = ref.split(':')
    pages = data.get(s, {}).get('ar', [])
    if int(v) <= len(pages):
        print(f'   [{ref}] {label} :: {pages[int(v)-1][1][:150]}')
    else:
        print(f'   [{ref}] {label} :: INEXISTANT ({len(pages)} pages en {s})')

print('\n== FIN DES SONDES 3 ==')
