#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R339 — Passe 2 : sondes de POSITION EXACTE pour 19771 (faṣl ad-dāl).
Passe 1 (instance parallèle) = patterns littéraux → faux négatifs (règle R338 :
SONDE LARGE PUIS POSITION EXACTE). Ici : patterns tolérants aux diacritiques
+ cps par position. Cibles : participes d-kh-l/d-kh-r, pluriels fém salim
(šāhidat/ʿābidat/walidat/maʿdūdāt), duels à dāl (taḏūdāni, ataʿidāni,
yurīdāni, yadāhu, wildān), ǧidāl(ānā), addaraʾtum, tadaraka/bali addaraka/
iddārakū, ʿadwa, yudfaʿ/dāfiʿ, ladā/ladā l-ḥanāǧir, hudāyā, ġadawa (2 pos.),
hudan/sudan, dāl mušaddada + alif, Dānī : ribāwā/naǧawa/manawa/miškawa,
ṣalawā/zakawā/ḥayawā (recompte large)."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE, encoding="utf-8"))
corpus = []
for k in sorted(data, key=int):
    for a in data[k]["ar"]:
        corpus.append((int(k), a[0], a[1]))
IDX = {(sn, an): tx for (sn, an, tx) in corpus}

DIAC = "\u064B-\u0655\u0670\u06D6-\u06ED\u0640\u06DF\u06E0"

def cps_at(sn, an, needle, ctx=30):
    tx = IDX.get((sn, an), "")
    i = tx.find(needle)
    if i < 0:
        print(f"  {sn}:{an} — '{needle}' ABSENT"); return
    seg = tx[i:i + len(needle) + 1]
    print(f"  {sn}:{an} [{needle}]")
    print(f"    text: …{tx[max(0,i-ctx):i+len(needle)+ctx]}…")
    print(f"    cps : " + " ".join(f"{ord(c):04X}({c})" for c in seg))

def sweep(label, pattern, ctx=16, maxs=14):
    print(f"\n=== {label} ===")
    rx = re.compile(pattern)
    hits = []
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            st = max(0, m.start() - ctx); en = min(len(tx), m.end() + ctx)
            hits.append((sn, an, m.group(0), tx[st:en]))
    print(f"  {len(hits)} occ.")
    for (sn, an, g, c) in hits[:maxs]:
        print(f"  {sn}:{an} [{g}] | …{c}…")
    if len(hits) > maxs:
        print(f"  … +{len(hits)-maxs} autres")
    return hits

print("########## 1. PARTICIPE D-KH-L (dākhil, chapitre du dāl) ##########")
sweep("dākhil: د+ا?+خ+ل (toutes formes)", f"د[{DIAC}]*ا?[{DIAC}]*خ[{DIAC}]*ل[{DIAC}]*و?[{DIAC}]*ن?")
sweep("PARTICIPE pluriel dākhilūna/dākhilīna", f"د[{DIAC}]*ا[{DIAC}]*خ[{DIAC}]*ل[{DIAC}]*[وي][{DIAC}]*ن[{DIAC}]*")
print("--- rasm SANS alif : دَخِلُون/دَخِلين ---")
sweep("daḫilūna sans alif (د+خ+ل+و/ي+ن)", f"د[{DIAC}]*خ[{DIAC}]*ل[{DIAC}]*[وي][{DIAC}]*ن[{DIAC}]*")

print("\n########## 2. PARTICIPE D-KH-R (dākhir — l'exception Ghāfir) ##########")
sweep("dākhir toutes formes د+خ+ر", f"د[{DIAC}]*ا?[{DIAC}]*خ[{DIAC}]*ر[{DIAC}]*")
cps_at(40, 60, "دَاخِرِينَ")

print("\n########## 3. PLURIELS FÉMININS SALIM (a. du taḥlīl) ##########")
sweep("šāhidat: ش+ا?+ه+د+ت", f"ش[{DIAC}]*ا?[{DIAC}]*ه[{DIAC}]*د[{DIAC}]*ت[{DIAC}]*")
sweep("ʿābidat: ع+ا?+ب+د+ت", f"ع[{DIAC}]*ا?[{DIAC}]*ب[{DIAC}]*د[{DIAC}]*ت[{DIAC}]*")
sweep("walidat: و+ا?+ل+د+ت (abs/alif)", f"و[{DIAC}]*ا?[{DIAC}]*ل[{DIAC}]*د[{DIAC}]*ت[{DIAC}]*")
sweep("maʿdūdāt: م+ع+د+و+د+ا?+ت", f"م[{DIAC}]*ع[{DIAC}]*د[{DIAC}]*و[{DIAC}]*د[{DIAC}]*ا?[{DIAC}]*ت[{DIAC}]*")
print("--- cps clés ---")
sweep("شهدات/شهدت exactes (rasm)", f"ش[{DIAC}]*ه[{DIAC}]*د[{DIAC}]*ت[{DIAC}]*")
for (sn, an) in [(2,184),(2,203)]:
    tx = IDX.get((sn,an),"")
    i = tx.find("مَّعْدُود")
    if i < 0: i = tx.find("مَعْدُود")
    if i >= 0:
        seg = tx[i:i+10]
        print(f"  {sn}:{an} cps مَعْدُود: " + " ".join(f"{ord(c):04X}({c})" for c in seg))
        print(f"  {sn}:{an} texte: …{tx[max(0,i-25):i+30]}…")

print("\n########## 4. DUELS À DĀL (t. muṯannā mutawassiṭ) ##########")
sweep("duel د+ا+ن (dāni/dayni)", f"د[{DIAC}]*ا[{DIAC}]*ن[{DIAC}]*")
print("--- cps clés des duels ---")
cps_at(28, 23, "تَذُودَانِ")
cps_at(46, 17, "أَتَعِدَانِنِي")
sweep("yurīdāni: ي+ر+ي+د+ا+ن", f"ي[{DIAC}]*ر[{DIAC}]*ي[{DIAC}]*د[{DIAC}]*ا[{DIAC}]*ن[{DIAC}]*")
sweep("yasjudāni: ي+س+ج+د+ا+ن", f"ي[{DIAC}]*س[{DIAC}]*ج[{DIAC}]*د[{DIAC}]*ا[{DIAC}]*ن[{DIAC}]*")
sweep("yadāhu/yadāhā/yadān: ي+د+ا+ه/ن", f"ي[{DIAC}]*د[{DIAC}]*ا[{DIAC}]*[هن][{DIAC}]*")
sweep("wildān: و+ل+د+ا+ن", f"و[{DIAC}]*ل[{DIAC}]*د[{DIAC}]*ا[{DIAC}]*ن[{DIAC}]*")

print("\n########## 5. Ǧ-D-L (ǧidalanā maṣdar vs ǧidāl thābit) ##########")
sweep("ǧidāl/ǧadala/ǧādala: ج+د+ل", f"ج[{DIAC}]*ا?[{DIAC}]*د[{DIAC}]*ل[{DIAC}]*")
cps_at(2, 197, "جِدَالَ")

print("\n########## 6. D-R-ʾ / D-R-K ##########")
sweep("addaraʾa: د+ر+أ/ء", f"د[{DIAC}]*ا?[{DIAC}]*ر[{DIAC}]*[أء]")
sweep("tadaraka/iddārakū/adrak: د+ر+ك", f"د[{DIAC}]*ا?[{DIAC}]*ر[{DIAC}]*ك[{DIAC}]*")

print("\n########## 7. ʿ-D-W (ʿadwa) ##########")
sweep("ʿadwa: ع+د+و", f"ع[{DIAC}]*د[{DIAC}]*و[{DIAC}]*")

print("\n########## 8. D-F-ʿ (yudfaʿ/dāfiʿ) ##########")
sweep("dāfaʿa/yudāfiʿ/dāfiʿun: د+ا+ف+ع", f"د[{DIAC}]*ا[{DIAC}]*ف[{DIAC}]*ع[{DIAC}]*")
sweep("yudfaʿ/yadfaʿ: ي+د+ف+ع", f"ي[{DIAC}]*د[{DIAC}]*ف[{DIAC}]*ع[{DIAC}]*")

print("\n########## 9. L-D-Y (ladā/ladī/ladayna) ##########")
sweep("l+د+ى/ا/ي : ladā family", f"ل[{DIAC}]*د[{DIAC}]*[اىي][{DIAC}]*")
sweep("ḥanāǧir: ح+ن+ا+ج+ر", f"ح[{DIAC}]*ن[{DIAC}]*ا[{DIAC}]*ج[{DIAC}]*ر[{DIAC}]*")

print("\n########## 10. H-D-Y (hudāyā/hudā) ##########")
sweep("hudāy: ه+د+ا+ي", f"ه[{DIAC}]*د[{DIAC}]*ا[{DIAC}]*ي[{DIAC}]*")

print("\n########## 11. Ġ-D-W (al-ġadawa — les 2 positions du Dānī) ##########")
sweep("ġadawa: غ+د+و", f"غ[{DIAC}]*د[{DIAC}]*و[{DIAC}]*")
cps_at(6, 52, "بِٱلْغَدَوٰةِ")
cps_at(18, 28, "بِٱلْغَدَوٰةِ")

print("\n########## 12. DĀL MUŠADDADA + ALIF (iḥtirāz) ##########")
sweep("mots finissant دّ+ا (dāl šadda + alif)", f"[ابتثجحخسشصضطظعغفقكلمنهي][{DIAC}]*دّ[{DIAC}]*ا[{DIAC}]*")
sweep("مثال بديل : دّ au milieu + ا", f"دّ[{DIAC}]*ا[{DIAC}]*")

print("\n########## 13. DĀNĪ — LES 4 UṢŪL (rasm wāw) ##########")
sweep("ribā: ر+ب+و (rasm wāw)", f"ر[{DIAC}]*ب[{DIAC}]*و[{DIAC}]*")
cps_at(2, 275, "ٱلرِّبَوٰا")
sweep("ṣalawā rasm wāw: ص+ل+و+ة", f"ص[{DIAC}]*ل[{DIAC}]*و[{DIAC}]*ه[{DIAC}]*")
sweep("zakawā rasm wāw: ز+ك+و+ة", f"ز[{DIAC}]*ك[{DIAC}]*و[{DIAC}]*ه[{DIAC}]*")
sweep("ḥayawā rasm wāw: ح+ي+و+ة", f"ح[{DIAC}]*ي[{DIAC}]*و[{DIAC}]*ه[{DIAC}]*")
print("--- cps ṣalawā 2:3, zakawā 2:43, ḥayawā 2:85 ---")
for (sn, an, w) in [(2,3,"ٱلصَّلَوٰةَ"),(2,43,"وَٱلزَّكَوٰةَ"),(2,85,"ٱلْحَيَوٰةَ")]:
    tx = IDX.get((sn,an),"")
    i = tx.find(w)
    if i >= 0:
        seg = tx[i:i+len(w)+1]
        print(f"  {sn}:{an} [{w}] cps: " + " ".join(f"{ord(c):04X}" for c in seg))
    else:
        print(f"  {sn}:{an} — '{w}' ABSENT (chercher variante)")

print("\n########## 14. DĀNĪ — LES 4 AḤRUF ##########")
sweep("naǧawa: ن+ج+و", f"ن[{DIAC}]*ج[{DIAC}]*و[{DIAC}]*")
cps_at(53, 20, "وَمَنَوٰةَ")
cps_at(24, 35, "كَمِشْكَوٰةٍ")

print("\n########## 15. ÉTAT INITIAL : ÉLISION DE L'ALIF DE DUEL — RECENSEMENT ##########")
sweep("tous دا+ن dans le corpus (position de l'alif)", f"د[{DIAC}]*ا[{DIAC}]*ن[{DIAC}]*[‌ٮ]")
