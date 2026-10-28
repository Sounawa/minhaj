# -*- coding: utf-8 -*-
"""R339 — Vérification coranique 19771 (fascule du dāl, rasm-wa-dabt-4ep).
Restitution des fentes vides de l'appareil : chaque mot revendiqué par le
šarḥ est cherché au corpus (rasm officiel) avec position exacte.
Clés de recherche : squelettes sans diacritiques, alif élidée incluse.
"""
import json, re, unicodedata

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = []
for k in sorted(data, key=int):
    s = data[k]
    for a in s["ar"]:
        corpus.append((int(k), a[0], a[1]))
IDX = {(sn, an): tx for (sn, an, tx) in corpus}

DIAC = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A\u0670]')
def bare(t):
    t = DIAC.sub('', t)
    t = t.replace('\u0671', '\u0627')  # alif wasla -> alif
    return t

def find(skel, limit=8):
    """skel : squelette (alifs élidées ou stables incluses, sans diacritiques)."""
    out = []
    for (sn, an, tx) in corpus:
        b = bare(tx)
        if skel in b:
            # contexte
            i = b.index(skel)
            ctx = b[max(0, i-25):i+len(skel)+25]
            out.append((sn, an, ctx))
    return out[:limit]

QUERIES = [
    # --- Section 1, type أ : jamʿ muʾannath sālim
    ("F-a1  شاهدات (šāhidāt)", "شاهدات"),
    ("F-a2  عابدات (ʿābidāt)", "عابدات"),
    ("F-a3  والولدت/والدات (al-wālidātu)", "والدات"),
    ("F-a4  معدودات (maʿdūdāt)", "معدودات"),
    # --- type ب : jamʿ muḏakkar sālim
    ("F-b1  داخرون (dāḫirūn)", "داخرون"),
    ("F-b2  داخرين (dāḫirīn)", "داخرين"),
    ("F-b3  داخلون (dāḫilūn)", "داخلون"),
    ("F-b4  داخلين (dāḫilīn)", "داخلين"),
    # --- type ت : muṯannā mutawassiṭ al-alif
    ("F-t1  يدك (yadaka)", "يدك"),
    ("F-t2  يده (yadahu)", "يده"),
    ("F-t3  يسجدن/يسجدان (yasǧudāni)", "يسجدان"),
    ("F-t4  جهدك/جاهدك (ǧahadaka)", "جاهدك"),
    ("F-t5  الوالدن/الوالدان (al-wālidāni)", "الوالدان"),
    ("F-t6  يريدن/يريدان (yurīdāni)", "يريدان"),
    ("F-t7  تذودن (taḏūdāni)", "تذودان"),
    ("F-t8  اتعدنني/اتعدني (aʿtidanī)", "اتعد"),
    # --- type ث : hors règles
    ("F-th1 عدوة/عادوة (ʿadawa)", "عدوة"),
    ("F-th2 العدوة (al-ʿadawa)", "العدوة"),
    ("F-th3 جدلنا/جدالنا (ǧidālanā)", "جدالنا"),
    ("F-th4 جدال (ǧidāl)", "جدال"),
    ("F-th5 ادرأتم (iddaraʾtum)", "ادرأتم"),
    ("F-th6 ادرا/ادرأ (iddaraʾ racine)", "ادرأ"),
    ("F-th7 تدراك (tadaraka)", "تدراك"),
    ("F-th8 بل ادرك (bal iddaraka)", "ادرك"),
    ("F-th9 اداركوا (iddārakū)", "ادارك"),
    ("F-th10 ولدان/الولدن (wildān)", "ولدان"),
    ("F-th11 يدفع (yudfaʿ)", "يدفع"),
    ("F-th12 دافع (dāfiʿ)", "دافع"),
    # --- Section 2 : mutaṭarrifa
    ("F-m1  لدا/لدى (ladā)", "لدا"),
    ("F-m1b لدى (ladā yāʾ)", "لدى"),
    ("F-m2  بدا (badā)", "بدا"),
    ("F-m3  لدى الحناجر", "لدى الحناجر"),
    ("F-m4  هداي (hudāya)", "هداي"),
    ("F-m5  الغدوة (al-ġadwa)", "غدوة"),
    ("F-m6  هدى/هدي (hudiyy)", "سدى"),
    ("F-m6b هدى نكرة", "هدى"),
    # --- Istitimār : Dānī
    ("D1  الصلوة (aṣ-ṣalawā)", "الصلوة"),
    ("D2  الزكوة (az-zakāwa)", "الزكوة"),
    ("D3  الحيوة (al-ḥayāwa)", "الحيوة"),
    ("D4  الربوا/ربوا (ar-ribāwa)", "ربوا"),
    ("D5  كمشكوة (kamiškāwa)", "مشكوة"),
    ("D6  النجوة (an-naǧāwa)", "النجوة"),
    ("D7  ومنوة (wa-manāwa)", "منوة"),
]

for label, skel in QUERIES:
    res = find(skel)
    print(f"== {label} : {len(res)} occurrence(s)")
    for (sn, an, ctx) in res[:8]:
        print(f"   {sn}:{an}  …{ctx}…")
