# -*- coding: utf-8 -*-
"""R335 — Vérification coranique 19762 (2e passage) — alif wasla ٱ, débogages."""
import json, re
from collections import Counter

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = []
for k in sorted(data, key=int):
    s = data[k]
    for a in s["ar"]:
        corpus.append((int(k), a[0], a[1]))

def find(pat, label, note="", maxprint=45):
    rx = re.compile(pat)
    hits = []
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            st = max(0, m.start()-25); en = min(len(tx), m.end()+25)
            hits.append((sn, an, tx[st:en]))
    print(f"\n=== {label} — {len(hits)} occ. {note}")
    for (sn, an, ctx) in hits[:maxprint]:
        print(f"  {sn}:{an} | {ctx}")
    if len(hits) > maxprint:
        print(f"  ... +{len(hits)-maxprint} autres")
    return hits

print("■■■ R335 — VERIFICATIONS 19762 (2) ■■■")

# F1. ṣalāt avec article (ٱ U+0671 corrigé)
find(r"[اأٱ]لصَّلَو[^ ]{0,5}", "aṣ-ṣalāt article+WĀW")
find(r"[اأٱ]لصَّلَاة[^ ]{0,4}", "aṣ-ṣalāt article+ALIF")

# F2. zakāt toutes graphies
find(r"زَّكَو[^ ]{0,4}|زَكَو[^ ]{0,4}", "zakāt WĀW (loose)")
find(r"زَّكَاة[^ ]{0,3}|زَكَاة[^ ]{0,3}|زَّكَا[^ ]{0,4}", "zakāt ALIF (loose)")

# F3. ḥayāt toutes graphies
find(r"حَيَو[^ ]{0,4}", "ḥayāt WĀW (loose)")
find(r"حَيَاة[^ ]{0,3}|حَيَا[^ ]{0,4}", "ḥayāt ALIF (loose)", maxprint=25)

# F4. ribā
find(r"رِّبَو[^ ]{0,3}|رِبَو[^ ]{0,3}", "ribā WĀW (loose)")
find(r"رِّبَا[^ ]{0,3}|رِبًا|رِبًى", "ribā ALIF (loose)")

# F5. ġadāt / manawa
find(r"غَدَو[^ ]{0,3}|غَدَا[^ ]{0,3}", "ġadāwa/ġadāt (loose)")

# F6. al-ǧāhiliya suscrite
find(r"جَٰهِلِيَّة", "al-ǧāhiliya (rasm)")

# F7. wa-ǧāwaznā positions
find(r"جَٰوَزْن[^ ]{0,3}", "wa-ǧāwaznā (positions)")

# F8. ǧāriya les deux graphies
find(r"جَٰرِيَ[^ ]{0,3}", "ǧāriya SUSCRITE")
find(r"جَارِيَ[^ ]{0,3}", "ǧāriya PLEINE")

# F9. al-ayl — debug brut + contexte large
for (sn, an, tx) in corpus:
    if sn == 6 and an == 96:
        i = tx.find("سَكَن")
        print(f"\nRAW 6:96 (extrait): {repr(tx[max(0,i-30):i+15])}")
    if sn == 25 and an == 47:
        i = tx.find("لِبَاس")
        print(f"RAW 25:47 (extrait): {repr(tx[max(0,i-30):i+15])}")
print("\n— Contextes لَّيْل précédés de جَعَل/جْعَل (recherche inversée) —")
n = 0
for (sn, an, tx) in corpus:
    for m in re.finditer(r"لَّيْل", tx):
        seg = tx[max(0, m.start()-16):m.end()+6]
        if "عَل" in seg or "جْع" in seg:
            n += 1
            print(f"  {sn}:{an} | {seg}")
print(f"— total {n}")

# F10. mutabarriǧa debug — texte brut 24:60
for (sn, an, tx) in corpus:
    if sn == 24 and an == 60:
        i = tx.find("جَةٍ")
        print(f"\nRAW 24:60 (extrait): {repr(tx[max(0,i-40):i+12])}")
        i2 = tx.find("ثِيَاب")
        print(f"RAW 24:60 (extrait 2): {repr(tx[max(0,i2-8):i2+40])}")

# F11. naǧwā
find(r"نَجْوَ[^ ]{0,4}", "naǧwā (toutes graphies)")

# F12. māddat al-ḥifẓ (iʿdād → chapitre du ḥāʾ)
find(r"حَٰفِظ[^ ]{0,4}|حَافِظ[^ ]{0,4}", "ḥāfiẓ (suscrite vs pleine — iʿdād)", maxprint=30)

print("\n■■■ FIN VERIFICATIONS 19762 (2) ■■■")
