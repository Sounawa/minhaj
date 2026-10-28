# -*- coding: utf-8 -*-
"""Vérification quran-cache pour 19798 (chapitre du rāʾ -3-).
Squelettes nus (hamza-normalisés) + frontières de mots (règle ca)."""
import json, re, unicodedata

CACHE = '/home/z/my-project/scripts-translate/quran-cache.json'
data = json.load(open(CACHE))

DIAC = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]')
ALIF_VARIANTS = '\u0627\u0622\u0623\u0625\u0671'

def bare(s):
    s = DIAC.sub('', s)
    s = s.replace('\u0671', '\u0627')  # alif wasla -> alif
    # hamza normalisée : ؤ -> و, ئ -> ي, ء -> ''
    s = s.replace('\u0624', '\u0648').replace('\u0626', '\u064A').replace('\u0621', '')
    return s

def norm(s):
    """Texte nu pour l'affichage (diacritiques enlevés, rasm conservé)."""
    return DIAC.sub('', s)

# précharge tokens par verset
verses = []  # (sura, ayah, text_bare, text_norm, tokens_bare)
for sk, sv in data.items():
    if sk in ('info', 'meta'):
        continue
    for i, item in enumerate(sv.get('ar', [])):
        num, txt = item[0], item[1]
        b = bare(txt)
        n = norm(txt)
        verses.append((int(sk), int(num), b, n, b.split()))

def find_word(sq):
    """Cherche le squelette nu comme TOKEN exact (frontières de mots)."""
    out = []
    for (s, a, b, n, toks) in verses:
        for t in toks:
            if t == sq:
                out.append((s, a, n, t))
                break
    return out

def find_contains(sq):
    out = []
    for (s, a, b, n, toks) in verses:
        for t in toks:
            if sq in t:
                out.append((s, a, n, t))
                break
    return out

def show(tag, hits, limit=12):
    print(f"### {tag} : {len(hits)} position(s)")
    for (s, a, n, t) in hits[:limit]:
        print(f"  {s}:{a}  token={t}")
    if len(hits) > limit:
        print(f"  ... (+{len(hits)-limit})")
    print()

# ============ FENTES ============
# 1. فالمغيرات (jamʿ muʾannaṯ sālim élidée) — squelettes possibles
show('A1 mughirat élidée (مغيرت)', find_word('مغيرت'))
show('A1b mughirat PLEINE (مغيرات)', find_word('مغيرات'))
show('A1c tout mot contenant مغير', find_contains('مغير'))

# 2. furāḍā élidée (فرض) vs pleine (فرضا)
show('A2 furadan élidée (فرض)', find_word('فرض'))
show('A2b furadan PLEINE (فرضا)', find_word('فرضا'))
show('A2c contenant فرض', find_contains('فرض'))

# 3. rājiʿūna élidée (رجعون) vs pleine (رجعونا)
show('A3 rajieun élidée (رجعون)', find_word('رجعون'))
show('A3b rajieun PLEINE (رجعونا)', find_word('رجعونا'))
show('A3c contenant رجعون', find_contains('رجعون'))

# 4. turāban élidée (تراب, à frontière) vs pleine (ترابا)
hits_trab = []
for (s, a, b, n, toks) in verses:
    for t in toks:
        # élidée : ت + راب ou وتراب ou بالتراب etc. -> token se terminant par تراب et ne contenant pas alif après ب
        if t.endswith('تراب') or t in ('تراب',):
            hits_trab.append((s, a, n, t))
            break
print(f"### A4 turaban élidée (finissant تراب) : {len(hits_trab)} position(s)")
for (s, a, n, t) in hits_trab[:15]:
    print(f"  {s}:{a}  token={t}")
print()
show('A4b turaban PLEINE (ترابا)', find_word('ترابا'))
show('A4c PLEINE avec suffixe (ترابا...)', find_contains('ترابا'))

# 5. sarabīla élidée (سربل) vs thabūta (سرابل)
show('A5 sarabil élidée (سربل)', find_word('سربل'))
show('A5b sarabil thabūta (سرابل)', find_word('سرابل'))
show('A5c contenant سربل', find_contains('سربل'))

# 6. tarāʾa élidée (ترء hamza -> ' donc تر) hmm : squelette hamza-normalisé de ترء = تر
#    → cherche tokens = ترء directement + forme با hamza
show('A6 tarāa avec hamza (ترء)', find_word('ترء'))
show('A6b tarāa thabūta (تراءت)', find_word('تراءت'))
show('A6c contenant تراء', find_contains('تراء'))
show('A6d token تر (ambigu)', find_word('تر'))

# 7. tatrā thabūta (تترا vs تترى)
show('B1 tatra (تترا)', find_word('تترا'))
show('B1b tatra au yāʾ (تترى)', find_word('تترى'))
show('B1c contenant تترا', find_contains('تترا'))

# 8. muṯannā thabūta : mots à rāʾ finale + nūn duel (token se terminant ران)
hits_dual = []
for (s, a, b, n, toks) in verses:
    for t in toks:
        if t.endswith('ران') and len(t) >= 4:
            hits_dual.append((s, a, n, t))
            break
print(f"### B2 mots à nūn duel + rāʾ finale (finissant ران) : {len(hits_dual)} position(s)")
for (s, a, n, t) in hits_dual[:20]:
    print(f"  {s}:{a}  token={t}")
print()

# 9. mots à rāʾ terminale dessinée au yāʾ (token finissant رى)
hits_ri = []
for (s, a, b, n, toks) in verses:
    for t in toks:
        if t.endswith('رى') and len(t) >= 3:
            hits_ri.append((s, a, n, t))
            break
print(f"### B3 mots à rāʾ finale + yāʾ (finissant رى) : {len(hits_ri)} position(s)")
seen = {}
for (s, a, n, t) in hits_ri:
    seen.setdefault(t, []).append((s, a))
for t, pos in sorted(seen.items(), key=lambda kv: -len(kv[1])):
    print(f"  token={t} ×{len(pos)}  ex: {pos[:6]}")
print()

# 10. muftarā (مفترى) et qurā (قرى)
show('B4 muftaran (مفترا/مفترى)', find_word('مفترا'))
show('B4b مفترى', find_word('مفترى'))
show('B4c contenant مفتر', find_contains('مفتر'))

# 11. bušrā (بشرا / بشرى) + bushrākum
show('C1 bushrā PLEINE (بشرا)', find_word('بشرا'))
show('C1b bushrā au yāʾ (بشرى)', find_word('بشرى'))
show('C1c bushrākum (بشراكم)', find_word('بشراكم'))
show('C1d bushrākum élidée (بشرىكم)', find_word('بشرىكم'))
show('C1e contenant بشر', find_contains('بشر'))

# 12. jazāʾ (جزاء vs جزا vs جزؤا)
show('D1 jazaā (جزاء)', find_word('جزاء'))
show('D1b jazā élidée (جزا)', find_word('جزا'))
show('D1c جزؤا', find_word('جزؤا'))
show('D1d contenant جزا', find_contains('جزا'))

# 13. ūlāika déjà vérifié R342 — vérification de complément : la madda sur l'alif mahdufa
show('E1 ulāika (اولئك rasm)', find_word('اولئك'))
show('E2 haʾulāʾi (هؤلاء rasm)', find_word('هؤلاء'))
