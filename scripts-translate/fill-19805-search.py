# -*- coding: utf-8 -*-
"""R345 — Fente-filling 19805 (le chapitre du kāf, 1ʳᵉ livraison).
Squelettes nus + boundary, comparaisons élidé/constant systématiques.
Familles : I.a élidées muṭlaqan (sukary/kašifāt/mušrikāt/mumsikāt/mutafikāt/barakāt/
kāliḥūn/kafirūn/akkalūn/kārihūn/kātibīn/kāẓimīn/akābir/kāḏib) ; I.b mixtes
(šurakāʾ, kātibū/kātib, kafr+kraʿd) ; II istiṯmār ad-Dānī (awzān).
Sortie : tr-tmp/fill-19805-out.txt"""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

def bare(t):
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t).replace('\u0671', '\u0627')

def find_all(skel, limit=60, bnd=False):
    out = []
    for (sn, an, tx) in corpus:
        b = bare(tx)
        start = 0
        while True:
            i = b.find(skel, start)
            if i < 0:
                break
            ok = True
            if bnd:
                ok = (i == 0 or b[i-1] == ' ') and (i+len(skel) == len(b) or b[i+len(skel)] == ' ')
            if ok:
                lo = max(0, i-45); hi = min(len(b), i+len(skel)+45)
                out.append((sn, an, b[lo:hi]))
                if len(out) >= limit:
                    return out
            start = i + 1
    return out

def compare(out, label, eli, con, bnd=False):
    r1 = find_all(eli, 60, bnd)
    r2 = find_all(con, 60, bnd)
    out.append(f"\n=== {label} : ÉLIDÉ [{eli}] = {len(r1)} | CONSTANT [{con}] = {len(r2)} ===")
    for (sn, an, ctx) in r1[:25]:
        out.append(f"  E {sn}:{an}  {ctx}")
    for (sn, an, ctx) in r2[:10]:
        out.append(f"  C {sn}:{an}  {ctx}")
    return r1, r2

def report(out, label, skels, bnd=False, n=12):
    out.append(f"\n### {label} ###")
    for skel in skels:
        r = find_all(skel, 40, bnd)
        out.append(f"  [{skel}] : {len(r)}")
        for (sn, an, ctx) in r[:n]:
            out.append(f"     {sn}:{an}  {ctx}")

out = ["############ A. FAMILLES ÉLIDÉES MUṬLAQAN ############"]

# A0 : sukary (22:2, deux occurrences)
compare(out, "A0 sukary", "سكرى", "سكارى", bnd=True)
report(out, "A0b سكر بndx", ["سكار", "سكرا"], bnd=True)

# A1 kašifat
report(out, "A1 kašifat", ["كشفى", "كشفات", "كشفت", "المشكفت"], bnd=True)
compare(out, "A1b kašifat", "كشفى", "كشفات", bnd=False)

# A2 mušrikat
compare(out, "A2 mušrikāt", "المشركت", "المشركات", bnd=True)
report(out, "A2b", ["مشركت", "مشركات"], bnd=True)

# A3 mumsikat
report(out, "A3 mumsikāt", ["ممسكات", "ممسكت", "مستمسكات", "المسكت"], bnd=True)

# A4 mutafikat
report(out, "A4 mutafikāt", ["المتفكت", "المتفكات", "متفكات", "ورق"], bnd=True)
r = find_all("ورق", 20)
out.append(f"  [ورق libre] : {len(r)}")
for (sn, an, ctx) in r[:10]:
    out.append(f"     {sn}:{an}  {ctx}")

# A5 barakat
report(out, "A5 barakāt", ["بركت", "بركات", "باركت"], bnd=True)

# A6 kālihūn
compare(out, "A6 kāliḥūn", "كليحون", "كالحون", bnd=True)
report(out, "A6b", ["كليح", "كالح"], bnd=True)

# A7 kafirūn (élidé = كفرو ?)
report(out, "A7 kāfirūn", ["كفرو", "كفرون", "كافرون", "الكفرو", "الكفرون", "الكافرون"], bnd=True)

# A8 akkalūn
compare(out, "A8 akkālūn", "اكلون", "اكالون", bnd=True)
report(out, "A8b", ["اكل", "اكال"], bnd=True)

# A9 kārihūn
compare(out, "A9 kārihūn", "كرهون", "كارهون", bnd=True)
report(out, "A9b", ["كره", "كار"], bnd=True)

# A10 kātibīn
compare(out, "A10 kātibīn", "كتبين", "كاتبين", bnd=True)
report(out, "A10b", ["كتبى", "كاتبى"], bnd=True)

# A11 kāẓimīn
compare(out, "A11 kāẓimīn", "كظمين", "كاظمين", bnd=True)
report(out, "A11b", ["كظم", "كاظم"], bnd=True)

# A12 akābir (élidé = أكبر) vs akbar comparatif
report(out, "A12 akābir/akbar", ["اكبر", "اكابر"], bnd=True)

# A13 kāḏib (élidé) — le naẓīm : وَكَيْفَ كَذِبٌ
report(out, "A13 kāḏib", ["كذب", "كاذب", "كذبون", "كاذبون"], bnd=True)

out.append("\n############ B. FAMILLES MIXTES (élision/ṯubūt) ############")

# B1 šurakāʾ
report(out, "B1 šurakāʾ", ["شركوا", "شركاء", "شركؤا", "شركء", "شراء"], bnd=True)

# B2 kātibū (impératif) / kātib (nom)
report(out, "B2 kātibū/kātib", ["كاتبوا", "كاتب", "كتب"], bnd=True)

# B3 kafr + raʿd (le verset du كفر élidé « بالرعد »)
report(out, "B3 raʿd", ["رعد"], bnd=True)

out.append("\n############ C. ISTITIMĀR AD-DĀNĪ (awzān, alif constante) ############")
report(out, "C1 awzān", ["ظالم", "طغيان", "صنوان", "قنوان", "خوان", "ختار"], bnd=True)

with open("/home/z/my-project/tr-tmp/fill-19805-out.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")
print("\n".join(out))
