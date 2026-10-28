# -*- coding: utf-8 -*-
"""R336 — Vérifications 19768, passe 2 : sondes d'ordre diacritique + codepoints.
P1. maḥārīb (shadda sur le mīm — ordre ح*رِيب)
P2. sāʾiḥūn / sābiḥāt / ṣāliḥāt fem-pl (ordres shadda+U+0670)
P3. subḥāna 17:93 — codepoints exacts + āya complète
P4. ḍuḥā — codepoints des quatre positions (93:1 + ḍuḥāhā ×3)
P5. ḥāffī (حَآفِّي) — localisation
P6. خَٰفَتُو — localisation (la suscrite inattendue du ḫāf)
P7. les verbes ḥāǧa — dump codepoints 2:139 / 3:65 / 3:66 / 6:80 / 40:47
P8. صَٰلِحَٰت — le décompte du pluriel féminin (les DEUX alifs)
P9. contrôle final du lexème ḥifẓ (total 19 = 15 sus + 1 pleine + 3 yuḥāfiẓūn)
"""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = []
for k in sorted(data, key=int):
    for a in data[k]["ar"]:
        corpus.append((int(k), a[0], a[1]))

def dump(sn, an, n=0, note=""):
    for (s, a, tx) in corpus:
        if s == sn and a == an:
            print(f"  [{sn}:{an}] {note} RAW: {tx[:140]}{'...' if len(tx)>140 else ''}")
            # codepoints autour de la zone cherchée
            return tx

def find(pat, label, maxprint=12, dumpcp=False):
    rx = re.compile(pat)
    hits = []
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            st = max(0, m.start()-30); en = min(len(tx), m.end()+30)
            hits.append((sn, an, tx[st:en], m.group(0)))
    print(f"\n=== {label} — {len(hits)} occ.")
    for (sn, an, ctx, g) in hits[:maxprint]:
        cps = " ".join(f"U+{ord(c):04X}" for c in g[:14])
        print(f"  {sn}:{an} | {ctx}")
        if dumpcp:
            print(f"        → {g}  [{cps}]")
    return hits

print("■■■ R336 — VERIFICATIONS 19768, PASSE 2 ■■■")

print("\n────── P1. MAḤĀRĪB (ordre diacritique) ──────")
find(r"ح\S{0,2}رِيب", "P1a. maḥārīb (tolérant)", dumpcp=True)

print("\n────── P2. sāʾiḥūn / sābiḥāt / ṣāliḥāt ──────")
find(r"س\S{0,3}ئ\S{0,2}ح", "P2a. sāʾiḥ (tolérant)", dumpcp=True)
find(r"س\S{0,3}ب\S{0,2}ح", "P2b. sābiḥ (tolérant)", maxprint=10, dumpcp=True)
find(r"ص\S{0,3}ل\S{0,2}ح\S{0,3}ت", "P2c. ṣāliḥāt — formes en -t", maxprint=40, dumpcp=False)

print("\n────── P3. SUBḤĀNA 17:93 ──────")
find(r"س\S{0,3}ح\S{0,3}ن", "P3a. subḥān — TOUS les dessins (madda/suscrite/pleine)", maxprint=50, dumpcp=False)
t93 = dump(17, 93, note="āya complète")

print("\n────── P4. ḌUḤĀ — codepoints ──────")
for (s, a) in [(93, 1), (79, 29), (79, 46), (91, 1)]:
    dump(s, a, note="ḍuḥā")
find(r"ض\S{0,2}ح\S{0,3}", "P4b. ḍuḥā — tous dessins tolérants", maxprint=10, dumpcp=True)

print("\n────── P5. ḤĀFFĪ ──────")
find(r"ح\S{0,3}ف\S{0,2}ي|ح\S{0,3}ف\S{0,3}و", "P5a. ḥāffī / ḥāffūn (tolérant)", maxprint=10, dumpcp=True)

print("\n────── P6. خَٰفَتُو ──────")
find(r"خ\S{0,3}ف\S{0,3}ت", "P6a. ḫāfatū (tolérant)", maxprint=10, dumpcp=True)

print("\n────── P7. VERBES ḤĀǦA — codepoints ──────")
for (s, a) in [(2, 139), (3, 65), (3, 66), (6, 80), (40, 47), (4, 60), (58, 1), (89, 18)]:
    dump(s, a, note="verbe ḥāǧa / voisin")

print("\n────── P8. ṢĀLIḤĀT — les deux alifs ──────")
find(r"ص\S{0,2}ل\S{0,2}ح\S{0,2}ت", "P8a. ṣāliḥāt exact (les deux suscrites)", maxprint=30, dumpcp=False)

print("\n────── P9. RÉCAPITULATIF LEXÈME ḤIFẒ ──────")
tot_sus = tot_full = tot_mad = 0
det_sus = []
for (sn, an, tx) in corpus:
    for m in re.finditer(r"ح\S{0,2}ف\S{0,2}ظ", tx):
        seg = m.group(0)
        if "فِظ" in seg or "فظ" in seg:  # ḥifẓ squelette sans alif
            continue
        if "\u0653" in seg: tot_mad += 1
        elif "\u0670" in seg: tot_sus += 1; det_sus.append((sn, an, seg))
        elif "ا" in seg: tot_full += 1
print(f"### LEXÈME ḤIFẒ (tolérant, hors squelette): suscrite={tot_sus} pleine={tot_full} madda={tot_mad}")
for (sn, an, g) in det_sus:
    print(f"   suscrite: {sn}:{an} | {g}")

print("\n■■■ FIN PASSE 2 ────────────────────────────────")
