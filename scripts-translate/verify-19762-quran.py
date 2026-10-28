#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Vérifications coraniques du doc 19762 (rasm-wa-dabt-4ep, chapitre du jīm).

Le doc enseigne :
  (1) élidées après le jīm : وجعِلُ اليْلِ (jaʿala + iḥtirāz al-layl), جَعِلُونَ,
      جَهِلُونَ, جَثِمِينَ, māḏat al-ǧihād (māḍin/muḍāriʿ/ism fāʿil), māḏat
      al-ǧidāl (māḍin/muḍāriʿ/amr), دَرَجَتٍ (pl. fém. salim), الجَرِيَتِ,
      زَوْجَنِ + يُخْرِجَكُمْ (duel médian), الجَهِلِيَّةِ, وَجَوَزْنَا,
      تِجَرَةٌ, يُجَزَى
  (2) thubūt à l'extrémité : نجَا (mot) + l'aṣl du duel + le reste du mutarraf
      au yāʾ ; CLÔTURE : النَّجَاة rasmée au wāw
  (3) ISTITIMĀR d'al-Ḫarrāz (Mawrid aẓ-ẓamʾān p. 32, abiyāt 391-394) :
      les wāw-graphies — الغدوة, مشكوة, الصلوة, الزكوة, الربوا, الحيوة,
      المنوة, النجوة — restreintes par « ما لم تضفهن إلى ضمير ».
Tous les motifs arabes sont écrits en échappements \u pour éviter toute faute de saisie.
"""
import json
import re

C = json.load(open("/home/z/my-project/scripts-translate/quran-cache.json"))
HARAKAT = re.compile(r"[\u064B-\u0652\u0653-\u0655\u0670\u06D6-\u06ED\u08F0-\u08F3]")
ALIF_S = "\u0670"  # alif suscrite (dagger alif)

def strip(s):
    return HARAKAT.sub("", s).replace("\u0640", "")

def plain_search(pat, label, limit=14, ctx=34, wb=False):
    """recherche sur texte sans harakat ; wb=True : motif entier (frontières de mots)."""
    hits = []
    for s, obj in C.items():
        for n, t in obj["ar"]:
            st = strip(t)
            if wb:
                if re.search(r"(?<![\u0621-\u064A])" + pat + r"(?![\u0621-\u064A])", st):
                    hits.append((s, n, t, st))
            else:
                if pat in st:
                    hits.append((s, n, t, st))
    print(f"[{label}] {len(hits)} hit(s) :")
    for s, n, t, st in hits[:limit]:
        idx = st.find(pat)
        print(f"   [{s}:{n}] {t[:110]}")
    return hits

def raw_refs(refs, label):
    print(f"[{label}] formes harakatées :")
    for s, n in refs:
        try:
            for nn, t in C[s]["ar"]:
                if nn == n:
                    print(f"   [{s}:{n}] {t[:130]}")
        except KeyError:
            print(f"   [{s}:{n}] introuvable")

print("=" * 72)
print("A. LA FAMILLE DE JAʿALA — وجعِلُ اليْلِ et l'iḥtirāz")
print("=" * 72)
h = plain_search("\u0648\u062C\u0639\u0644", "وجعل (wāw+jaʿl, tout)")
plain_search("\u062C\u0639\u0644 \u0627\u0644\u064A\u0644", "جعل اليل (jaʿala l-layla)")
plain_search("\u062C\u0639\u0644\u0627", "جعلا (duel jaʿalāni ?)")
print()
print("=" * 72)
print("B. LES ÉLIDÉES DU JĪM — jamʿ mudakkar sālim")
print("=" * 72)
a = plain_search("\u062C\u0639\u0644\u0648\u0646", "جعلون (ÉLIDÉ ǧaʿilūn)")
plain_search("\u062C\u0627\u0639\u0644\u0648\u0646", "جاعلون (PLEINE ǧāʿilūn — iḥtirāz)")
b = plain_search("\u062C\u0647\u0644\u0648\u0646", "جهلون (ÉLIDÉ ǧāhilūn)")
plain_search("\u062C\u0627\u0647\u0644\u0648\u0646", "جاهلون (PLEINE)")
c = plain_search("\u062C\u062B\u0645\u064A\u0646", "جثمين (ÉLIDÉ ǧāthimīn)")
plain_search("\u062C\u0627\u062B\u0645\u064A\u0646", "جاثمين (PLEINE)")
print()
print("=" * 72)
print("C. MĀḎAT AL-ǦIHĀD — élision MUtlaqa ? (māḍin / muḍāriʿ / ism fāʿil)")
print("=" * 72)
d = plain_search("\u062C\u0647\u062F", "جهد (SANS alif : élidé ou forme I)")
e = plain_search("\u062C\u0627\u0647\u062F", "جاهد (AVEC alif : ǧāhad — dague ?)")
print()
print("=" * 72)
print("D. MĀḎAT AL-ǦIDĀL — élision mUtlaqa ? (māḍin / muḍāriʿ / amr)")
print("=" * 72)
f = plain_search("\u062C\u062F\u0644", "جذل ? NON — ج‌د‌ل (SANS alif : جَدِلْ élidé)")
g = plain_search("\u062C\u0627\u062F\u0644", "جادل (AVEC alif — dague ?)")
print()
print("=" * 72)
print("E. LES PLURIELS FÉMININS SALIM ET DIVERS")
print("=" * 72)
plain_search("\u062F\u0631\u062C\u062A", "درجت (ÉLIDÉ darajāt)")
plain_search("\u062F\u0631\u062C\u0627\u062A", "درجات (PLEINE)")
plain_search("\u0627\u0644\u062C\u0631\u064A\u062A", "الجريت (ÉLIDÉ al-ǧāriyāt)")
plain_search("\u0627\u0644\u062C\u0627\u0631\u064A\u0627\u062A", "الجاريات (PLEINE)")
plain_search("\u062C\u0627\u0631\u064A\u0627\u062A", "جاريات (sans ال)")
plain_search("\u0627\u0644\u062C\u0647\u0644\u064A\u062A", "الجهليت (ÉLIDÉ)")
plain_search("\u0627\u0644\u062C\u0627\u0647\u0644\u064A\u062A", "الجاهليت (PLEINE)")
plain_search("\u0627\u0644\u062C\u0627\u0647\u0644\u064A\u0629", "الجاهلية (avec tāʾ marbūṭa)")
plain_search("\u062A\u062C\u0631\u062A", "تجرت (ÉLIDÉ tiǧāra)")
plain_search("\u062A\u062C\u0627\u0631\u062A", "تجارت (PLEINE)")
plain_search("\u062A\u062C\u0627\u0631\u0629", "تجارة (PLEINE tāʾ marbūṭa)")
plain_search("\u064A\u062C\u0632\u0649", "يجزى (yāʾ maqṣūra — yuǧzā)")
plain_search("\u064A\u062C\u0632\u0627", "يجزا (ALIF PLEINE — divergence ?)")
print()
print("=" * 72)
print("F. LE DUEL MÉDIAN : زَوْجَنِ — et يُخْرِجَكُمْ")
print("=" * 72)
plain_search("\u0632\u0648\u062C\u0646", "زوجن (ÉLIDÉ zawǧāni)")
plain_search("\u0632\u0648\u062C\u064A\u0646", "زوجين (au yāʾ)")
plain_search("\u0632\u0648\u062C\u0627\u0646", "زوجان (alif pleine)")
plain_search("\u064A\u062E\u0631\u062C\u0643\u0645", "يخرجكم (rasm — 71:18 ?)")
plain_search("\u0645\u062A\u0628\u0631\u062C", "متبرج (étiquette ?)")
plain_search("\u0645\u062A\u062C\u0648\u0631", "متجور (étiquette ?)")
plain_search("\u0645\u062A\u062C\u0627\u0648\u0631", "متجاور (étiquette ?)")
print()
print("=" * 72)
print("G. THUBŪT À L'EXTRÉMITÉ : نجَا + l'aṣl du duel + النجوة au wāw")
print("=" * 72)
plain_search("\u0646\u062C\u0627", "نجا (mot entier — alif du thubūt)", wb=True)
plain_search("\u0646\u062C\u0649", "نجى (au yāʾ)", wb=True)
plain_search("\u0646\u062C\u0627\u0629", "نجاة (an-naǧāh — alif)")
plain_search("\u0646\u062C\u0648\u0629", "نجوة (WĀW — an-naǧawa !)")
plain_search("\u0627\u0644\u0646\u062C\u0648\u0629", "النجوة (WĀW — la clôture)")
h = plain_search("\u062C\u0627(?![\u0621-\u064A])", "…جا (mots finissant جا)", wb=False)
plain_search("\u062C\u0627\u0646(?![\u0621-\u064A])", "…جان (mots finissant جان)")
plain_search("\u064A\u062C\u0631\u0649", "يجرى (yāʾ — le mutarraf)")
plain_search("\u064A\u062C\u0631\u0627", "يجرا (alif — divergence ?)")
print()
print("=" * 72)
print("H. ISTITIMĀR D'AL-ḪARRĀZ — les WĀW-GRAPHIES")
print("=" * 72)
plain_search("\u0635\u0644\u0648\u0629", "صلوة (wāw — ṣalāh)", limit=8)
p1 = plain_search("\u0635\u0644\u0648\u062A", "صلوت (wāw+tāʾ)", limit=4)
p2 = plain_search("\u0635\u0644\u0627\u062A", "صلات (alif : صلاه + suffixes)", limit=10)
plain_search("\u0635\u0644\u0648\u062A\u0647", "صلوته (wāw+pronom — attendu 0)")
plain_search("\u0635\u0644\u0648\u0627\u062A", "صلوات (pluriel, wāw+alif)", limit=6)
plain_search("\u0632\u0643\u0648\u0629", "زكوة (wāw — zakāh)")
plain_search("\u0632\u0643\u0648\u062A", "زكوت (wāw+tāʾ)")
plain_search("\u0632\u0643\u0627\u062A", "زكات (alif + suffixes)", limit=8)
plain_search("\u0632\u0643\u0648\u062A\u0647", "زكوته (wāw+pronom — attendu 0)")
plain_search("\u062D\u064A\u0648\u0629", "حيوة (wāw — ḥayāh)", limit=8)
plain_search("\u062D\u064A\u0648\u062A", "حيوت (wāw+tāʾ)")
plain_search("\u062D\u064A\u0627\u062A", "حيات (alif + suffixes)", limit=10)
plain_search("\u062D\u064A\u0648\u062A\u0647", "حيوته (wāw+pronom — attendu 0)")
plain_search("\u0631\u0628\u0648\u0627", "ربوا (wāw — ar-ribā)")
plain_search("\u0631\u0628\u0627", "ربا (alif — r-ribā/r-riban)", limit=8)
plain_search("\u0645\u0646\u0648\u0629", "منوة (wāw — maniyah)", limit=4)
plain_search("\u0645\u0646\u0648\u062A", "منوت (wāw+tāʾ)")
plain_search("\u0645\u0646\u064A\u0629", "منية (yāʾ — maniyah classique)", limit=6)
plain_search("\u0645\u0646\u064A", "مني (racine — maniyy)", limit=6)
plain_search("\u0627\u0644\u063A\u062F\u0648\u0629", "الغدوة (wāw — al-ḡadāh)", limit=4)
plain_search("\u0627\u0644\u063A\u062F\u0648\u062A", "الغدوت (wāw+tāʾ)")
plain_search("\u0627\u0644\u063A\u062F\u0627\u0629", "الغداة (alif)")
plain_search("\u063A\u062F\u0627\u0629", "غداة (sans ال)", limit=6)
plain_search("\u0645\u0634\u0643\u0648\u0629", "مشكوة (wāw — miškāh 24:35)")
plain_search("\u0645\u0634\u0643\u0627\u0629", "مشكاة (alif)")
plain_search("\u0643\u064A\u0641\u0645\u0627", "كيفما (étiquette du bayt ?)")
print()
print("=" * 72)
print("I. FORMES BRUTES CLÉS (dagues \u0670, maddas)")
print("=" * 72)
raw_refs([(2, 3), (2, 43), (2, 277)], "صلوة — échantillons")
raw_refs([(24, 35)], "مشكوة 24:35")
raw_refs([(40, 41)], "40:41 النجاة/النجوة ?")
raw_refs([(2, 275), (2, 276), (3, 130)], "ربوا")
raw_refs([(71, 18)], "يخرجكم 71:18")
for s, n, t, st in e[:14]:
    print(f"   [جاهد-brut {s}:{n}] {t[:120]}")
for s, n, t, st in d[:14]:
    print(f"   [جهد-brut {s}:{n}] {t[:120]}")
for s, n, t, st in g[:10]:
    print(f"   [جادل-brut {s}:{n}] {t[:120]}")
for s, n, t, st in f[:10]:
    print(f"   [جدل-brut {s}:{n}] {t[:120]}")
for s, n, t, st in h[:14]:
    print(f"   […جا-brut {s}:{n}] {t[:110]}")
print()
print("=== fin des vérifications 19762 ===")
