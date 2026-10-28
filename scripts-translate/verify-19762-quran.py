# -*- coding: utf-8 -*-
"""R335 — Vérification coranique étendue pour doc 19762 (chapitre du ǧīm).
Contrôle au muṣḥaf (quran-cache.json) :
  A. Inventaire systématique : ǧīm + alif SUSCRITE (جَٰ) vs ǧīm + alif PLEINE (جَا)
  B. Lexèmes de la leçon : ǧaʿala/ǧaʿilūna (+ iḥtirāz al-ayl), māddat al-ǧihād,
     māddat al-ǧidāl, ǧahlūna, al-ǧāhiliya, darāǧāt, al-ǧāriya, zawǧāni (duel),
     tiǧāra, yuǧzā, ǧaṯīm, mutabarriǧa, mutaǧāwira, wa-ǧawaznā, yuḫriǧakum
  C. najā (kalima du taḥlīl) + an-naǧāta dessinée à la wāw
  D. ISTITMĀR al-Ḫarrāz (bayts 391-394) : alif dessinée WĀW —
     ṣalawa, zakawa, ḥayawa, ribā, miškāwa, ġadāwa, manawa, naǧawa
     + la condition « mā lam tuḍifhuwa ilā ḍamīr » (annexé → alif)
Chaque sonde imprime : sūra:āya — rasm brut (contexte ± 25 car).
"""
import json, re, sys
from collections import Counter

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = []  # (sura, aya, texte)
for k in sorted(data, key=int):
    s = data[k]
    for a in s["ar"]:
        corpus.append((int(k), a[0], a[1]))

def find(pat, label, note="", maxprint=60):
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

def stat(pat, label):
    rx = re.compile(pat)
    full = sus = 0
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            seg = m.group(0)
            if "ٰ" in seg: sus += 1
            elif "ا" in seg: full += 1
    print(f"### {label}: pleine={full} suscrite={sus}")

print("■■■ R335 — VERIFICATIONS 19762 (chapitre du ǧīm) ■■■")

# ── A. INVENTAIRE SYSTÉMATIQUE ──────────────────────────────────────
print("\n────── A. INVENTAIRE ǧīm+alif ──────")
inv_sus = Counter(); inv_full = Counter()
for (sn, an, tx) in corpus:
    for m in re.finditer(r"جَٰ(\S{0,10})", tx):
        inv_sus[m.group(0)[:8]] += 1
    for m in re.finditer(r"جَا(\S{0,10})", tx):
        inv_full[m.group(0)[:8]] += 1
print("— ǧīm+SUSCRITE (جَٰ) — lexèmes distincts:", len(inv_sus))
for w, c in inv_sus.most_common(40):
    print(f"   {c:3d}× {w}")
print("— ǧīm+PLEINE (جَا) — lexèmes distincts:", len(inv_full))
for w, c in inv_full.most_common(40):
    print(f"   {c:3d}× {w}")

# ── B1. ǧaʿala / ǧaʿilūna ───────────────────────────────────────────
print("\n────── B1. ǧaʿala / ǧaʿilūna ──────")
find(r"جَٰعَل[^ ]{0,5}", "ǧaʿala SUSCRITE جَٰعَل")
find(r"جَاعَل[^ ]{0,5}", "ǧaʿala PLEINE جَاعَل")
find(r"جْعَل[^ ]{0,5}", "ǧaʿala SUKŪN جْعَل (skeleton sans alif)")
find(r"جَٰعِلُون[^ ]{0,3}", "ǧaʿilūna SUSCRITE جَٰعِلُون")
find(r"جَاعِلُون[^ ]{0,3}", "ǧaʿilūna PLEINE جَاعِلُون")
find(r"جَٰعِل[^ ]{0,3}", "ǧaʿil (toutes formes) SUSCRITE")
find(r"جَاعِل[^ ]{0,3}", "ǧaʿil (toutes formes) PLEINE")
# iḥtirāz al-ayl : ǧaʿala suivi de al-ayl
find(r"[جج][َٰ]?عَلَ [اأٱ]لَّيْل[^ ]{0,3}", "ǧaʿala + AL-AYL (toutes graphies)")
find(r"جَعَل[^ ]{0,4}", "ǧaʿala fatḥa simple جَعَل (échantillon)", maxprint=25)

# ── B2. māddat al-ǧihād (ǧ-ā-h-d) ───────────────────────────────────
print("\n────── B2. māddat al-ǧihād ──────")
find(r"وَجَٰهِد[^ ]{0,4}", "wa-ǧāhid SUSCRITE وَجَٰهِد")
find(r"وَجَاهِد[^ ]{0,4}", "wa-ǧāhid PLEINE وَجَاهِد")
find(r"وَجْهِد[^ ]{0,4}|وَجَهِد[^ ]{0,4}", "wa-ǧahid ELIDÉE وَجْهِد/وَجَهِد")
find(r"يُجَٰهِد[^ ]{0,4}", "yuǧāhid SUSCRITE")
find(r"يُجَاهِد[^ ]{0,4}", "yuǧāhid PLEINE")
find(r"يُجْهِد[^ ]{0,4}|يُجَهِد[^ ]{0,4}", "yuǧahid ELIDÉE")
find(r"جَٰهِدُون|جَٰهِدِين", "ǧāhidūna/ǧāhidīna SUSCRITE")
find(r"جَاهِدُون|جَاهِدِين", "ǧāhidūna/ǧāhidīna PLEINE")
find(r"جَٰهِد[^ ]{0,6}", "ǧihād mādda TOUTES suscrites (balayage)", maxprint=40)
find(r"جَاهِد[^ ]{0,6}", "ǧihād mādda TOUTES pleines (balayage)", maxprint=40)

# ── B3. māddat al-ǧidāl (ǧ-ā-d-l) ───────────────────────────────────
print("\n────── B3. māddat al-ǧidāl ──────")
find(r"وَجَادِل[^ ]{0,4}", "wa-ǧādil PLEINE وَجَادِل")
find(r"وَجَٰدِل[^ ]{0,4}", "wa-ǧādil SUSCRITE")
find(r"وَجْدِل[^ ]{0,4}|وَجَدِل[^ ]{0,4}", "wa-ǧadil ELIDÉE")
find(r"يُجَادِل[^ ]{0,4}|يُجَٰدِل[^ ]{0,4}|يُجْدِل[^ ]{0,4}", "yuǧādilu (toutes)")
find(r"جَادِل[^ ]{0,4}|جَٰدِل[^ ]{0,4}|جْدِل[^ ]{0,4}", "ǧidāl mādda TOUTES", maxprint=40)

# ── B4. lexèmes divers de la leçon ──────────────────────────────────
print("\n────── B4. lexèmes divers ──────")
find(r"جَٰهِلُون|جَٰهِلِين", "ǧāhilūna/ǧāhilīna SUSCRITE")
find(r"جَاهِلُون|جَاهِلِين", "ǧāhilūna/ǧāhilīna PLEINE")
find(r"جَٰهِلِيَّة|جَاهِلِيَّة", "al-ǧāhiliya (les deux)")
find(r"جَٰثِم[^ ]{0,4}|جَاثِم[^ ]{0,4}|جْثِم[^ ]{0,4}", "ǧaṯīm (toutes)")
find(r"دَرَجَٰت[^ ]{0,4}", "darāǧāt SUSCRITE دَرَجَٰت")
find(r"دَرَجَات[^ ]{0,4}", "darāǧāt PLEINE دَرَجَات")
find(r"[اأٱ]لْجَٰرِيَة[^ ]{0,3}|الْجَارِيَة[^ ]{0,3}|[اأٱ]لْجَارِيَة[^ ]{0,3}", "al-ǧāriya (les deux)")
find(r"زَوْجَٰنِ|زَوْجَانِ", "zawǧāni DUAL marfūʿ (suscrite/pleine)")
find(r"زَوْجَيْنِ", "zawǧayni DUAL oblique")
find(r"يُخْرِجَكُم", "yuḫriǧakum (documenté)")
find(r"وَجَوَزْنَا|جَوَزْنَا", "wa-ǧawaznā (le mot du bayt)")
find(r"تِجَٰرَة|تِجَارَة", "tiǧāra (les deux)")
find(r"مُتَبَرِّج", "mutabarriǧa (24:60 ?)")
find(r"مُتَجَوِر|مُتَجَاوِر", "mutaǧāwira")
find(r"يُجْزَى|يُجَٰزَى|يُجَزَى", "yuǧzā (toutes graphies)", maxprint=40)

# ── C. najā + an-naǧāta à la wāw ────────────────────────────────────
print("\n────── C. najā / an-naǧāta ──────")
find(r"(^|\s)نَجَا(\s|$|هَ?ٰ?[^م])", "najā (verbe simple)")
find(r"نَجَاة|نَجْوَة|نَجَوَة|النَّجَو", "naǧāta/naǧawa (les deux graphies)")

# ── D. ISTITMĀR al-Ḫarrāz : alif dessinée WĀW ───────────────────────
print("\n────── D. ISTITMĀR — wāw remplace l'alif ──────")
find(r"الصَّلَو[^ ]{0,4}|صَلَوَٰة[^ ]{0,4}|صَّلَٰوَٰة", "ṣalāt à la WĀW (ṣalawa)")
find(r"الصَّلَاة[^ ]{0,3}|صَلَاة[^ ]{0,3}", "ṣalāt à l'ALIF (ṣalāt)")
find(r"صَلَوَٰت[^ ]{0,4}|صَلَٰوَٰت[^ ]{0,4}", "ṣalawāt pluriel")
find(r"صَلَ[^ ]{0,3}[هك][مي]?[^ ]{0,2}", "ṣalāt + PRONOM (annexé)", maxprint=30)
find(r"الزَّكَو[^ ]{0,4}|زَكَوَٰة[^ ]{0,4}|زَّكَوَٰة", "zakāt à la WĀW (zakawa)")
find(r"الزَّكَاة[^ ]{0,3}|زَكَاة[^ ]{0,3}", "zakāt à l'ALIF")
find(r"زَكَ[^ ]{0,3}[هك][مي]?[^ ]{0,2}", "zakāt + PRONOM", maxprint=20)
find(r"الْحَيَو[^ ]{0,4}|حَيَوَٰة[^ ]{0,4}", "ḥayāt à la WĀW (ḥayawa)")
find(r"الْحَيَاة[^ ]{0,3}|حَيَاة[^ ]{0,3}", "ḥayāt à l'ALIF", maxprint=25)
find(r"حَيَ[^ ]{0,3}[هك][مي]?[^ ]{0,2}", "ḥayāt + PRONOM", maxprint=20)
find(r"الرِّبَو[^ ]{0,3}|الرِّبَٰو[^ ]{0,3}|رِبَو", "ribā à la WĀW (ribaw)")
find(r"الرِّبَا|رِبًا|رِبًى|رِّبًا", "ribā à l'ALIF/tanwīn")
find(r"مِشْكَو[^ ]{0,3}|مِشْكَوَٰة|مِشْكَٰوة", "miškāwa à la WĀW")
find(r"مِشْكَاة", "miškāt à l'ALIF")
find(r"الْغَدَو[^ ]{0,3}|غَدَوَٰة|الْغَدَوَة", "ġadāwa à la WĀW")
find(r"الْغَدَاة|غَدَاة", "ġadāt à l'ALIF")
find(r"مَنَوَة|مَنَاة", "manawa")
find(r"النَّجَو[^ ]{0,3}|نَجَوَة", "naǧawa à la WĀW")
print("\n■■■ FIN VERIFICATIONS 19762 ■■■")
