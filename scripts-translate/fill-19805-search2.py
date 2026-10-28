# -*- coding: utf-8 -*-
"""R345 — Fente-filling 19805, PASSE 2 : hamzas inclus + brut diacritique
pour vérifier les alifs réelles du rasm hafsi."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

def bare(t):
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t).replace('\u0671', '\u0627')

def find_all(skel, limit=40, bnd=False):
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

def report(out, label, skels, bnd=False, n=10):
    out.append(f"\n### {label} ###")
    for skel in skels:
        r = find_all(skel, 40, bnd)
        out.append(f"  [{skel}] : {len(r)}")
        for (sn, an, ctx) in r[:n]:
            out.append(f"     {sn}:{an}  {ctx}")

# BRUT diacritique des versets clés (alifs réelles)
out = ["############ D. BRUT DIACRITIQUE (alifs réelles) ############"]
for (sn, an) in [(4,43),(22,2),(82,11),(40,18),(2,221),(39,38),(7,96),(7,134),
                 (42,21),(6,94),(2,282),(9,48),(18,35),(35,32),(6,99),(13,4),
                 (22,38),(31,32),(6,59),(6,22)]:
    for (s2, a2, tx) in corpus:
        if s2 == sn and a2 == an:
            out.append(f"\n--- {sn}:{an} ---\n{tx}")
            break

out.append("\n############ E. PASSE 2 (hamzas inclus) ############")

# E1 akbar/akabir avec hamza
report(out, "E1 akbar (hamza)", ["أكبر", "أكابر", "الاكبر", "الاكابر", "اكبر", "كبر"], bnd=True)

# E2 mutafikat
report(out, "E2 mutafikāt", ["تفك", "وتفك", "موتفك", "وركا", "ورقت"])

# E3 akkalūn
report(out, "E3 akkālūn", ["أكل", "كلون", "أكال", "اكلون", "أكلون", "كلت"], bnd=True)

# E4 kālihūn
report(out, "E4 kāliḥūn", ["كليح", "كالح", "كلح", "كال", "لكل"], bnd=True)

# E5 kāḏib complet
report(out, "E5 kāḏib bnd complet", ["كذب", "كذاب", "كذبوا", "كذبن", "كذبى", "كذبين"], bnd=True)

# E6 raʿd
report(out, "E6 raʿd", ["رعد", "الرعد", "ثور", "صاعق"], bnd=False)

# E7 kafr (toutes formes bnd)
report(out, "E7 kafr bnd", ["كفر", "كفرو", "كفرا", "كفرت", "الكفر"], bnd=True)

# E8 šurakā libre (avec suffixes)
report(out, "E8 šurakā libre", ["شركا", "شركؤ"])

# E9 kātibū/kātib large
report(out, "E9 kātib large", ["كات", "كاتبوا", "كتبوا"], bnd=False)

# E10 binyān/ṭuġyān
report(out, "E10 awzān", ["بنيان", "طغيان", "طغى", "عنوان", "صران"], bnd=True)

with open("/home/z/my-project/tr-tmp/fill-19805-out2.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")
print("\n".join(out))
