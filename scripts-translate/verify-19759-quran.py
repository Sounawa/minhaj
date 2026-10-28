# -*- coding: utf-8 -*-
"""R334 — Vérification coranique étendue pour doc 19759 (fiche du thāʾ).
Contrôle au muṣḥaf (quran-cache.json) :
  mīthāq, awthān, aṯara(t), formes d'aṯar (+hum/-him), naffāṯāt,
  ḫabīṯ (sing./pluriel), yastaġīṯ (toutes formes), ṯulūth,
  amṯal (de Maryam au sceau vs avant Maryam), aṯaba, aṯāth,
  anṯā (duel/sing.), duel de thāʾ à l'alif fixe (le mot unique).
Chaque sonde imprime : sūra:āya — rasm brut (contexte ± 25 car).
"""
import json, re, sys

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = []  # (sura, aya, texte)
for k in sorted(data, key=int):
    s = data[k]
    for a in s["ar"]:
        corpus.append((int(k), a[0], a[1]))

def find(pat, label, note=""):
    rx = re.compile(pat)
    hits = []
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            st = max(0, m.start()-25); en = min(len(tx), m.end()+25)
            hits.append((sn, an, tx[st:en]))
    print(f"\n=== {label} — {len(hits)} occ. {note}")
    for (sn, an, ctx) in hits:
        print(f"  {sn}:{an} | {ctx}")
    return hits

def stat_alif(pat, label):
    """Répartition alif pleine / suscrite / yāʾ dans le rasm du lexème trouvé."""
    rx = re.compile(pat)
    full = sus = ya = none = 0
    for (sn, an, tx) in corpus:
        for m in rx.finditer(tx):
            seg = m.group(0)
            if "ٰ" in seg: sus += 1
            elif "ا" in seg: full += 1
            elif "ى" in seg or "ي" in seg: ya += 1
            else: none += 1
    print(f"\n### {label}: pleine={full} suscrite={sus} yāʾ={ya} sans trace={none}")

print("■■■ R334 — VERIFICATIONS 19759 (chapitre du thāʾ) ■■■")

# 1. MĪTHĀQ — alif élidée après ṯāʾ en milieu de mot ?
h = find(r"مِيث[^ ]{0,6}", "MĪTHĀQ مِيثَاق")
stat_alif(r"مِيث[^ ]{0,6}", "mīthāq")

# 2. AWTHĀN
h = find(r"[اأ]وْثَان[^ ]{0,4}", "AWTHĀN أَوْثَان")
stat_alif(r"[اأ]وْثَان[^ ]{0,4}", "awthān")

# 3. AṮARA(t) — أَثَرَة (mot du poème)
h = find(r"[اأ]ثَرَة[^ ]{0,4}", "AṮARA(t) أَثَرَة")

# 4. Formes d'AṮAR (le verbe/nom) — toutes graphies أ/ا + ث + ر
h = find(r"[اأ]ث[َٰ]?ر[^ ]{0,8}", "formes d'AṮAR أَثَر (toutes)")

# 5. NAFFĀṮĀT
h = find(r"نَفَّاث[^ ]{0,5}", "NAFFĀṮĀT نَفَّاثَات")
stat_alif(r"نَفَّاث[^ ]{0,5}", "naffāṯāt")

# 6. ḪABĪṮ — singulier + pluriel
h = find(r"[اأ]ل?ْ?خَبِيث[^ ]{0,5}", "ḪABĪṮ خَبِيث (sing. + pluriel)")
stat_alif(r"خَبِيث[^ ]{0,5}", "ḫabīṯ")

# 7. YASTAĠĪṮ — toutes formes (sing., pluriel, duel ?)
h = find(r"سْتَغِيث[^ ]{0,5}", "YASTAĠĪṮ سْتَغِيث (toutes formes)")
stat_alif(r"سْتَغِيث[^ ]{0,5}", "yastaġīṯ")

# 8. ṮULŪTH
h = find(r"ثُلُث[^ ]{0,5}", "ṮULŪTH ثُلُث")
stat_alif(r"ثُلُث[^ ]{0,5}", "ṯulūth")

# 9. AMṮAL (le mot) vs AMṮĀL (pluriel de maṯal — autre mot)
h = find(r"[اأ]مْثَل[^ ا]{0,4}", "AMṮAL أَمْثَل (le mot)")
h2 = find(r"[اأ]مْثَال[^ ]{0,4}", "AMṮĀL أَمْثَال (pluriel de maṯal, autre mot)")

# 10. AṮABA
h = find(r"[اأ]ثَ?ب[^ ]{0,6}", "AṮABA أَثَب (toutes formes d'أ-ث-ب)")

# 11. AṮĀṮ
h = find(r"[اأ]ثَا?ث[^ ]{0,5}", "AṮĀṮ أَثَاث")
stat_alif(r"[اأ]ثَا?ث[^ ]{0,5}", "aṯāth")

# 12. ANṮĀ — singulier + duel
h = find(r"[اأ]نْث[^ ]{0,5}", "ANṮĀ أُنْثَى (toutes formes)")
stat_alif(r"[اأ]نْث[^ ]{0,5}", "anṯā")

# 13. LE DUEL DE THĀʾ À L'ALIF FIXE — noms au duel finissant -ṯāni/-ṯayni
h = find(r"ثَانِ|ثَانَا|ثَانَ |ثَانَ$|ثَيْنِ", "DUEL DE THĀʾ (ثَانِ/ثَانَا/ثَيْنِ)")
h = find(r"[^ا]ثَانِ|[ا-ي]ثَانِ", "…ṯāni en fin/flux (2ᵉ passe)")
