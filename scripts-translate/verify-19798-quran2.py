# -*- coding: utf-8 -*-
"""Complément 19798 : norm() (hamza préservée) + textes complets des versets."""
import json, re

CACHE = '/home/z/my-project/scripts-translate/quran-cache.json'
data = json.load(open(CACHE))
DIAC = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]')

def bare(s):
    s = DIAC.sub('', s)
    s = s.replace('\u0671', '\u0627')
    s = s.replace('\u0624', '\u0648').replace('\u0626', '\u064A').replace('\u0621', '')
    return s

def norm(s):
    return DIAC.sub('', s)

verses = []
for sk, sv in data.items():
    if sk in ('info', 'meta'):
        continue
    for i, item in enumerate(sv.get('ar', [])):
        verses.append((int(sk), int(item[0]), item[1], bare(item[1]), norm(item[1])))

def txt(s, a):
    for (ss, aa, t, b, n) in verses:
        if ss == s and aa == a:
            return t
    return None

def find_n(tok, field=4):
    """Cherche token exact dans norm (field=4) ou bare (field=3)."""
    out = []
    for v in verses:
        toks = v[field].split()
        for t in toks:
            if t == tok:
                out.append((v[0], v[1], t))
                break
    return out

def find_cont_n(sub, field=4, suffix=None, prefix=None):
    out = []
    for v in verses:
        toks = v[field].split()
        for t in toks:
            if sub in t and (suffix is None or t.endswith(suffix)) and (prefix is None or t.startswith(prefix)):
                out.append((v[0], v[1], t))
                break
    return out

def show(tag, hits, limit=15, txts=False):
    print(f"### {tag} : {len(hits)} position(s)")
    for (s, a, t) in hits[:limit]:
        print(f"  {s}:{a}  token={t}")
    if len(hits) > limit:
        print(f"  ... (+{len(hits)-limit})")
    print()

# --- 1. sarabīl : le vrai squelette (avec ي) ---
show('F1 sarabil élidée (سربيل)', find_cont_n('سربيل'))
show('F2 sarabil thabūta (سرابيل)', find_cont_n('سرابيل'))

# --- 2. turab dans 13 / 27 / 78 spécifiquement ---
print("=== G. turab dans ar-Ra'd (13), an-Naml (27), an-Naba (78) ===")
for (s, a, t, b, n) in verses:
    if s in (13, 27, 78):
        for tk in b.split():
            if 'تراب' in tk or 'ترب' in tk:
                print(f"  {s}:{a} token={tk}")
print()
# affiche les versets suspects
for (s, a) in [(13, 4), (27, 61), (78, 33), (78, 27)]:
    print(f"--- {s}:{a} : {txt(s, a)}")
print()

# --- 3. turab ÉLIDÉE (naṣb) dans les 9 positions : quels versets ont تُرَابًا élidée ? ---
print("=== H. textes des positions turab ===")
for (s, a) in [(2, 264), (3, 59), (16, 59), (18, 37), (22, 5), (30, 20), (35, 11), (38, 52), (40, 67)]:
    print(f"--- {s}:{a} : {txt(s, a)}")
print()

# --- 4. tarāʾa / tarāʾat : sur norm (hamza préservée) ---
show('I1 tarāa élidée/forme (تراء)', find_cont_n('تراء'))
show('I2 tarāat (تراءت)', find_cont_n('تراءت'))
show('I3 raāt toute forme (راءت)', find_cont_n('راءت'))
show('I4 turā (توراء)', find_cont_n('توراء'))

# --- 5. duels finissant ران : liste complète filtrée ---
print("=== J. tous tokens finissant ران (bare) ===")
seen = {}
for (s, a, t, b, n) in verses:
    for tk in b.split():
        if tk.endswith('ران') and len(tk) >= 4:
            seen.setdefault(tk, []).append((s, a))
for tk, pos in sorted(seen.items(), key=lambda kv: -len(kv[1])):
    print(f"  token={tk} ×{len(pos)}  ex: {pos[:8]}")
print()

# --- 6. bushrā : textes complets ---
print("=== K. bushrā : textes ===")
for (s, a) in [(57, 12), (3, 126), (8, 10), (25, 22), (10, 64), (7, 57), (2, 97), (11, 69)]:
    print(f"--- {s}:{a} : {txt(s, a)}")
print()

# --- 7. jazāʾ sur norm ---
show('L1 jazāa avec hamza (جزاء)', find_cont_n('جزاء'))
show('L2 jazā sans hamza (جزا)', find_cont_n('جزا'))
show('L3 jazawa (جزؤا)', find_cont_n('جزؤا'))

# --- 8. muftarā / qurā / tatrā / mughirāt : textes complets ---
print("=== M. textes ===")
for (s, a) in [(28, 36), (34, 43), (59, 14), (34, 18), (23, 44), (100, 3), (2, 46), (2, 156), (21, 93), (23, 60)]:
    print(f"--- {s}:{a} : {txt(s, a)}")
print()

# --- 9. rāġibūna (رغبون) : le mot du bayt ---
show('N1 raghabūn (راغبون bare rghbwn)', find_n('رغبون', 3))
show('N2 avec و (ورغبون)', find_cont_n('رغبون', 3))
show('N3 raghba famille (يرغبون)', find_cont_n('رغب', 3))

# --- 10. furāḍā : textes des 4 positions فرض ---
print("=== O. farad : textes ===")
for (s, a) in [(2, 197), (28, 85), (33, 38), (66, 2)]:
    print(f"--- {s}:{a} : {txt(s, a)}")
print()

# --- 11. حدف/حذف frontières : وَاحْذِفْ / وَحَذَفُوا (rasm) ---
show('P1 ahzif (احذف)', find_cont_n('احذف', 3))
show('P2 wahazafū (وحذفوا)', find_cont_n('وحذفوا', 3))

# --- 12. sarābīl thabūta : chercher سرابي (partiel) ---
show('Q1 sarabil partiel (سربي/سرابي)', find_cont_n('سربي', 3))
show('Q2 sarabil (سرابي)', find_cont_n('سرابي', 3))
