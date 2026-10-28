# -*- coding: utf-8 -*-
"""R345 — Script 1 : inventaire corpus pour 19800 (فصلا الطاء والظاء).
Ṭāʾ : طائ/طئ/حطم/شيطان/سطع/طاغوت/ناشط/طاغين/طاغون/خطيا/خطيئ/خطا/سلطان/طاع/استطاع
Ẓāʾ : حافظ/ظالمين/ظالمي construct/ظالمون/ظاهر/عظام/عظام
Ṭarf : mots finissant طا/ظا/ضا (alif ṭarf après ṭ/ẓ)
Istitimār ad-Dānī : صالحات/حافظات/صافات/تائب/سائح
Iʿdād (sonde) : شركاء
"""
import json, re
from collections import Counter

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

def bare(t):
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t).replace('\u0671', '\u0627')

bc = [(s, a, bare(tx)) for (s, a, tx) in corpus]

def find_all(skel, limit=40):
    out = []
    for (sn, an, b) in bc:
        start = 0
        while True:
            i = b.find(skel, start)
            if i < 0:
                break
            lo = max(0, i-42); hi = min(len(b), i+len(skel)+42)
            out.append((sn, an, b[lo:hi]))
            start = i + 1
            if len(out) >= limit:
                return out
    return out

def word_final(suffixes):
    """Mots uniques finissant par l'un des suffixes (après bare, sans clitics ـه/ـك ?) : garde tout, trie par fréquence."""
    cnt = Counter()
    ex = {}
    for (sn, an, b) in bc:
        for w in b.split():
            core = w
            # retire pronoms suffixés courants pour classifier ? on garde les 2 : mot brut + mot réduit
            for suf in suffixes:
                if w.endswith(suf) and len(w) >= len(suf)+2:
                    cnt[w] += 1
                    if w not in ex:
                        i = b.find(w)
                        lo = max(0, i-30); hi = min(len(b), i+len(w)+30)
                        ex[w] = (sn, an, b[lo:hi])
    return cnt, ex

print("=========== ṬĀʾ : SQUELETTES ===========")
for skel in ["طائ", "طئ", "حطم", "سطع", "طاغوت", "ناشط", "طاغين", "طاغون",
             "خطيا", "خطيئ", "استطاع", "طوع", "اطع", "طوي", "مطا", "وطا"]:
    r = find_all(skel, 25)
    print(f"\n[{skel}] : {len(r)} pos (plafonné à 25)")
    for (sn, an, ctx) in r:
        print(f"   {sn}:{an}  {ctx}")

print("\n[خطا] avec frontière de mot :")
n = 0
for (sn, an, b) in bc:
    start = 0
    while True:
        i = b.find("خطا", start)
        if i < 0: break
        okb = (i == 0 or b[i-1] == ' ') and (i+3 == len(b) or b[i+3] == ' ')
        if okb:
            n += 1
            if n <= 12:
                lo = max(0, i-40); hi = min(len(b), i+44)
                print(f"   {sn}:{an}  {b[lo:hi]}")
        start = i + 1
print("   total:", n)

print("\n[شيطان] décompte global :", len(find_all("شيطان", 10**6)))
print("[شياطين] décompte global :", len(find_all("شياطين", 10**6)))
print("[سلطان] décompte global :", len(find_all("سلطان", 10**6)))
print("[اطيع] décompte :", len(find_all("اطيع", 10**6)))
print("[اطاع] décompte :", len(find_all("اطاع", 10**6)))

print("\n=========== ẒĀʾ : SQUELETTES ===========")
for skel in ["حافظ", "ظالمين", "ظالمون", "ظالموا", "ظاهر", "يظهر", "اظهر", "عظام", "ظهرا", "اظلم"]:
    r = find_all(skel, 20)
    print(f"\n[{skel}] : {len(r)} pos (plafonné à 20)")
    for (sn, an, ctx) in r:
        print(f"   {sn}:{an}  {ctx}")

print("\n[ظالمي] construct (non suivi de ن) :")
n = 0
for (sn, an, b) in bc:
    start = 0
    while True:
        i = b.find("ظالمي", start)
        if i < 0: break
        j = i + len("ظالمي")
        if j < len(b) and b[j] != 'ن' and (j == len(b) or b[j] in ' ا'):
            n += 1
            if n <= 12:
                lo = max(0, i-40); hi = min(len(b), j+42)
                print(f"   {sn}:{an}  {b[lo:hi]}")
        start = i + 1
print("   total:", n)

print("\n=========== ṬARF : mots finissant طا / ظا / ضا ===========")
for suf in ["طا", "ظا", "ضا", "طى", "ظى", "ضى"]:
    cnt, ex = word_final([suf])
    print(f"\n--- suffixe [{suf}] : {len(cnt)} mots uniques ---")
    for w, c in cnt.most_common(20):
        sn, an, ctx = ex[w]
        print(f"   {w} ×{c}   → {sn}:{an}  {ctx}")

print("\n=========== ISTIMĀR AD-DĀNĪ : les cinq vedettes ===========")
for skel in ["صالحات", "حافظت", "حافظات", "صافات", "تائب", "تائبت", "سائح", "توب", "صلحت"]:
    r = find_all(skel, 15)
    print(f"\n[{skel}] : {len(r)} pos")
    for (sn, an, ctx) in r:
        print(f"   {sn}:{an}  {ctx}")

print("\n=========== IʿDĀD (sonde) : شركاء ===========")
r = find_all("شركاء", 12)
print(f"[شركاء] : {len(r)} pos")
for (sn, an, ctx) in r:
    print(f"   {sn}:{an}  {ctx}")
r2 = find_all("شركا", 20)
print(f"[شركا large] : {len(r2)} pos")
