# -*- coding: utf-8 -*-
"""verify-19805-quran.py — sondes coraniques pour 19805 (le kāf, R346)."""
import json, re, unicodedata

data = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json', encoding='utf-8'))

def bare(t):
    return ''.join(c for c in t if not unicodedata.category(c).startswith('M') and c != '\u0640').replace('\u0671', '\u0627')

# cache bare en mémoire
corp = {}
for s in range(1, 115):
    corp[s] = [(i+1, bare(p[1])) for i, p in enumerate(data.get(str(s), {}).get('ar', []))]

def hunt(sk, show=8):
    out = []
    for s, pairs in corp.items():
        for a, t in pairs:
            if sk in t:
                out.append((s, a, t))
    print(f'[{sk}] = {len(out)}')
    for s, a, t in out[:show]:
        i = t.find(sk)
        print(f'   {s}:{a}  …{t[max(0,i-22):i+len(sk)+18]}…')
    return out

print('=== 1. SAKRĀ ===')
for sk in ('سكرى', 'سكارى', 'سكارا', 'سكرا'): hunt(sk)

print('=== 2. KĀŠIFĀT ===')
for sk in ('كشفت', 'كاشفت', 'كاشفات', 'كاشفة', 'كاشفه'): hunt(sk, 6)

print('=== 3. MUŠRIKĀT / MUMSIKĀT / MUTAFIKKĀT ===')
for sk in ('مشركات', 'المشركت', 'مشررت', 'ممسكت', 'ممسكت', 'موتفكت', 'تفكت', 'مفكت', 'المتفكات'): hunt(sk, 8)

print('=== 4. BARAKĀT ===')
for sk in ('بركت', 'بركات'): hunt(sk, 6)

print('=== 5. KĀLIḤŪN ===')
for sk in ('كلحون', 'كاليحون', 'كلحن'): hunt(sk, 5)

print('=== 6. KĀFIR (rasm) ===')
for sk in ('كفرون', 'كافرون', 'الكفرون', 'الكافرون', 'كفرين', 'كافرين', 'الكفرين', 'الكافرين'): hunt(sk, 10)

print('=== 7. ĀKILŪN ===')
for sk in ('اكلون', 'أكلون', 'اكالون', 'أكالون', 'اكالين', 'أكالين'): hunt(sk, 6)

print('=== 8. AKBAR ===')
for sk in ('أكبر', 'اكبر', 'اكبروا', 'أكبروا'): hunt(sk, 10)

print('=== 9. KĀẒIMĪN ===')
for sk in ('كزمين', 'كاظمين', 'الكزمين', 'الكاظمين'): hunt(sk, 6)

print('=== 10. KĀRIHŪN ===')
for sk in ('كرهون', 'كارهون'): hunt(sk, 5)

print('=== 11. KĀTIBĪN + KĀTIBŌ + KĀTIB ===')
for sk in ('كتبين', 'كاتبين', 'كاتبوا', 'كاتبون', 'كاتيبين', 'كاتب'): hunt(sk, 8)

print('=== 12. KAḎIB ===')
for sk in ('كذب', 'كذبون', 'كاذبون', 'الكذبون', 'كذبن'): hunt(sk, 8)

print('=== 13. SŪRA 13 (ar-Raʿd) — kāfir élidé ===')
for a, t in corp[13]:
    for sk in ('كفر', 'كافر', 'كفار', 'يكفر', 'وكفر'):
        if sk in t:
            print(f'   13:{a} [{sk}] …{t}…')
            break

print('=== 14. AUZĀN ISTITIMĀR (constantes) ===')
for sk in ('طغيان', 'بنيان', 'خوان', 'ختار', 'صنوان', 'قنوان', 'بونا'): hunt(sk, 6)

print('=== 15. ŠURAKĀʾ (rappel déjà ancré) ===')
for sk in ('شركا', 'شركاء', 'شركؤا'): hunt(sk, 13)

print('=== 16. MUŠRIKŪN / KĀFIRŪN nu (contrôle rasm) ===')
for sk in ('مشررون', 'مشركون', 'المشركون', 'كفروا'): hunt(sk, 4)
