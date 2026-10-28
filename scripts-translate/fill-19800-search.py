# -*- coding: utf-8 -*-
"""R345 — Fente-filling 19800 (les chapitres du ṭāʾ et du ẓāʾ).
Squelettes nus, comparaisons élidé/constant systématiques, finales (maqṣūra/alif),
boundary lexicale pour les squelettes à collisions (ظلم, عظم, صفت...).
Familles : I.a ṭāʾ élidées (ṭāġūn/ṭ-w-ʿ/ḥuṭāma/šayṭān/ṭāʾir/ḫaṭayā/sulṭān/ṭāġūt/ṭāʾif),
I.b našīṭāt ; I.t ṭāġīn ; II finales ṭāʾ ; III ẓāʾ élidées (ḥāfiẓāt/ẓālimīn/ẓālimī/ẓālim/
ẓāhir/ʿiẓām) ; IV finales ẓāʾ (laẓā) ; Istitmār ad-Dānī (ṣāliḥāt/ṣāffāt/tāʾibat/sāʾiḥat) ;
Iʿdād šurakāʾ."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

def bare(t):
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t).replace('\u0671', '\u0627')

def find_all(skel, limit=60, bnd=False):
    """bnd=True : occurrence délimitée par espaces/debord (mot entier)."""
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

def finale(skel, limit=60):
    """Occurrences en FIN de mot (suffixe)."""
    out = []
    for (sn, an, tx) in corpus:
        b = bare(tx)
        start = 0
        while True:
            i = b.find(skel, start)
            if i < 0:
                break
            j = i + len(skel)
            if j == len(b) or b[j] == ' ':
                lo = max(0, i-45); hi = min(len(b), j+45)
                out.append((sn, an, b[lo:hi]))
                if len(out) >= limit:
                    return out
            start = i + 1
    return out

def compare(label, eli, con, bnd=False):
    r1 = find_all(eli, 60, bnd)
    r2 = find_all(con, 60, bnd)
    print(f"\n=== {label} : ÉLIDÉ [{eli}] = {len(r1)} | CONSTANT [{con}] = {len(r2)} ===")
    for (sn, an, ctx) in r1[:25]:
        print(f"  E {sn}:{an}  {ctx}")
    for (sn, an, ctx) in r2[:10]:
        print(f"  C {sn}:{an}  {ctx}")
    return r1, r2

print("############ A. FAMILLES DU ṬĀʾ ############")

# 1) pluriels masc sains du ṭāʾ : ṭāġūn/ṭāġīn
compare("A1 ṭāġūn (pluriel masc sain, wāw)", "طغون", "طاغون")
compare("A1b ṭāġīn (pluriel masc sain, yāʾ)", "طغين", "طاغين")

# 2) racine Ṭ-W-ʿ (l'obéissance)
print("\n=== A2 RACINE Ṭ-W-ʿ ===")
for skel in ["أطع", "أطاع", "أطوع", "أطيعوا", "أطيعن", "مطيع", "أطعوا", "أطعت", "أطعتم", "أطاعوا", "أطاعن", "أطاع"]:
    r = find_all(skel, 15)
    print(f"  [{skel}] : {len(r)}")
    for (sn, an, ctx) in r[:6]:
        print(f"     {sn}:{an}  {ctx}")

# 3) ḥuṭāma
compare("A3 ḥuṭāma (ḥuṭāman élidé)", "حطمى", "حطامى")
for skel in ["حطم", "حطام", "حطمت", "حطمنا"]:
    r = find_all(skel, 12)
    print(f"  [{skel}] : {len(r)}")
    for (sn, an, ctx) in r[:8]:
        print(f"     {sn}:{an}  {ctx}")

# 4) šayṭān
compare("A4 šayṭān (élidé)", "شيطن", "شيطان", bnd=True)

# 5) ṭāʾir
compare("A5 ṭāʾir (élidé)", "طئر", "طاير")
r = find_all("طا", 60, bnd=True)
print(f"\n  [طا] mot entier : {len(r)}")
for (sn, an, ctx) in r[:20]:
    print(f"     {sn}:{an}  {ctx}")

# 6) ḫaṭayā
print("\n=== A6 ḫaṭayā ===")
for skel in ["خطيا", "خطايا", "خطي", "خطايا"]:
    r = find_all(skel, 12)
    print(f"  [{skel}] : {len(r)}")
    for (sn, an, ctx) in r[:8]:
        print(f"     {sn}:{an}  {ctx}")

# 7) sulṭān
compare("A7 sulṭān", "سلطن", "سلطان", bnd=True)

# 8) ṭāġūt
compare("A8 ṭāġūt", "طغوت", "طاغوت")

# 9) ṭāʾif
compare("A9 ṭāʾif (élidé)", "طئف", "طايف")

# 10) našīṭāt
print("\n=== A10 našīṭāt ===")
for skel in ["نشطت", "نشط", "النشطت"]:
    r = find_all(skel, 12)
    print(f"  [{skel}] : {len(r)}")
    for (sn, an, ctx) in r[:8]:
        print(f"     {sn}:{an}  {ctx}")

print("\n############ B. FINALES DU ṬĀʾ ############")
r = finale("طى")
print(f"\n=== B1 finale طى (maqṣūra) : {len(r)} ===")
for (sn, an, ctx) in r:
    print(f"     {sn}:{an}  {ctx}")
r = finale("طا")
print(f"\n=== B2 finale طا (alif constante) : {len(r)} ===")
for (sn, an, ctx) in r:
    print(f"     {sn}:{an}  {ctx}")

print("\n############ C. FAMILLES DU ẒĀʾ ############")

# 11) ḥāfiẓāt
print("\n=== C1 ḥāfiẓāt ===")
for skel in ["حفظت", "حافظت", "حفظ"]:
    r = find_all(skel, 12)
    print(f"  [{skel}] : {len(r)}")
    for (sn, an, ctx) in r[:8]:
        print(f"     {sn}:{an}  {ctx}")

# 12) pluriels de ẓālim
compare("C2 ẓālimīn (yāʾ)", "ظلمين", "ظالمين", bnd=True)
compare("C2b ẓālimūn (wāw)", "ظلمون", "ظالمون", bnd=True)
compare("C3 ẓālimī (iḍāfa sans nūn)", "ظلمي", "ظالمي")
compare("C4 ẓālim (mufrad)", "ظلمى", "ظالمى")
r = find_all("ظلمى", 30)
print(f"\n  [ظلمى] nu : {len(r)}")
for (sn, an, ctx) in r[:12]:
    print(f"     {sn}:{an}  {ctx}")

# 13) ẓāhir
print("\n=== C5 ẓāhir ===")
for skel, bnd in [("ظهر", False), ("ظهرة", False), ("ظاهر", True), ("ظاهرة", False), ("الظهر", True)]:
    r = find_all(skel, 30, bnd)
    print(f"  [{skel}] bnd={bnd} : {len(r)}")
    for (sn, an, ctx) in r[:10]:
        print(f"     {sn}:{an}  {ctx}")

# 14) ʿiẓām
compare("C6 ʿiẓām (pluriel takṯīr)", "عظمى", "عظام")
r = find_all("عظام", 20)
print(f"\n  [عظام] : {len(r)}")
for (sn, an, ctx) in r:
    print(f"     {sn}:{an}  {ctx}")
r = find_all("عظم", 60, bnd=True)
print(f"\n  [عظم] bnd : {len(r)}")
for (sn, an, ctx) in r[:20]:
    print(f"     {sn}:{an}  {ctx}")

print("\n############ D. FINALES DU ẒĀʾ ############")
r = finale("ظى")
print(f"\n=== D1 finale ظى : {len(r)} ===")
for (sn, an, ctx) in r:
    print(f"     {sn}:{an}  {ctx}")
r = finale("ظا")
print(f"\n=== D2 finale ظا : {len(r)} ===")
for (sn, an, ctx) in r:
    print(f"     {sn}:{an}  {ctx}")

print("\n############ E. L'ISTITIMĀR D'AD-DĀNĪ ############")
compare("E1 ṣāliḥāt", "صلحت", "صالحات", bnd=True)
compare("E2 ṣāffāt", "صففت", "صاففات")
r = find_all("صففت", 15)
print(f"\n  [صففت] : {len(r)}")
for (sn, an, ctx) in r[:10]:
    print(f"     {sn}:{an}  {ctx}")
compare("E3 tāʾibat", "تئبت", "تائبت")
r = find_all("تائبت", 15)
print(f"\n  [تائبت] : {len(r)}")
for (sn, an, ctx) in r[:10]:
    print(f"     {sn}:{an}  {ctx}")
compare("E4 sāʾiḥat", "سئحت", "سائحت")
r = find_all("سائحت", 15)
print(f"\n  [سائحت] : {len(r)}")
for (sn, an, ctx) in r[:10]:
    print(f"     {sn}:{an}  {ctx}")

print("\n############ F. L'I'DĀD (šurakāʾ, pour 19805) ############")
compare("F1 šurakāʾ", "شركؤ", "شركاء", bnd=True)

print("\n############ G. TEXTES COMPLETS DES CIBLES ############")
for (sn, an) in [(36,19),(36,18),(79,39),(70,15),(36,78),(79,11),(17,5),(20,24),(79,17),(2,256),
                 (4,51),(4,60),(5,60),(16,36),(39,17),(4,76),(9,53),(4,152),(37,1)]:
    t = "?"
    for (s, a, tx) in corpus:
        if s == sn and a == an:
            t = bare(tx); break
    print(f"--- {sn}:{an} ---")
    print(t)
