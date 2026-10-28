#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérifications coraniques du doc 19759 (rasm-wa-dabt-4ep, chapitre du thāʾ).

Le doc enseigne :
  (1) élidées MÉDIANES après le thāʾ : أَثَرَة (aṯara), مِيثَاق (mīṯāq),
      أَوْثَان (awṯān), أَثَرَ + هُم (ḍamma — le verbe « suivre derrière »)
  (2) le pluriel féminin salim élidé : نَفَّاثَاتٍ (113:4), الْخَبِيثَاتُ (8:37 ?)
  (3) les DUELS élidées : يَسْتَغِيثَانِ, ثُلُثَانِ (4:176 ?)
  (4) أَثَبْ (mot du vers deux — exemple en image)
  (5) أَمْثَل — élidé DEPUIS MARYAM jusqu'à la fin du Coran ; AVANT Maryam :
      alif maintenue sur le qiyās (règle positionnelle !)
  (6) أَثَاثًا (aṯāṯan)
  (7) l'alif après thāʾ à l'EXTRÉMITÉ → yāʾ, SAUF le duel (alif maintenue) —
      ثَاءٌ مُثَنَّى مُتَطَرِّفَةٌ بِالْأَلِفِ en UNE SEULE position (image)
  (8) l'élidée MUMĀLA : أَثَرِ + هِمْ (kasra — إِثْرِهِمْ) ḥaḏf SANS yāʾ ;
      iḥtirāz contre l'ajouté au DUEL (qiyās)
  (9) ISTITIMĀR d'Abū Wakīl : l'alif ḥamrāʾ (maqṣūra) — yāʾ, sukūn, نَرَى اللهَ, ذِكْرَى الدَّارِ
"""
import json
import re

C = json.load(open("/home/z/my-project/scripts-translate/quran-cache.json"))
HARAKAT = re.compile(r"[\u064B-\u0652\u0653-\u0655\u0670\u06D6-\u06ED\u08F0-\u08F3]")

def strip(s):
    return HARAKAT.sub("", s).replace("\u0640", "")

def plain_search(pat_plain, label, limit=12, ctx=32):
    hits = []
    for s, obj in C.items():
        for n, t in obj["ar"]:
            st = strip(t)
            if pat_plain in st:
                hits.append((s, n, t, st, st.find(pat_plain)))
    print(f"   [{label}] {len(hits)} hit(s) :")
    for s, n, t, st, idx in hits[:limit]:
        print(f"     [{s}:{n}] …{st[max(0,idx-ctx):idx+len(pat_plain)+ctx]}…")
    return hits

def raw_show(refs, label):
    print(f"   [{label}] formes harakatées :")
    for s, n in refs:
        try:
            for nn, t in C[s]["ar"]:
                if nn == n:
                    print(f"     [{s}:{n}] {t[:200]}")
        except KeyError:
            print(f"     [{s}:{n}] — introuvable")

def raw_search(pat_harak, label, limit=10, ctx=30):
    hits = []
    for s, obj in C.items():
        for n, t in obj["ar"]:
            if pat_harak in t:
                idx = t.find(pat_harak)
                hits.append((s, n, t, idx))
    print(f"   [{label}] {len(hits)} hit(s) — formes harakatées :")
    for s, n, t, idx in hits[:limit]:
        print(f"     [{s}:{n}] …{t[max(0,idx-ctx):idx+ctx+len(pat_harak)]}…")
    return hits

print("=" * 70)
print("A. أَثَرَة — aṯara (la dot). Élidée médiane ?")
hits = plain_search("ثرة", "…ثرة (stripped)")
for s, n, t, st, idx in hits:
    print(f"      RAW [{s}:{n}] : …{t[max(0,t.find('ثرة')-40):t.find('ثرة')+40] if 'ثرة' in t else t[:120]}…")
raw_search("أَثَٰرَة", "أَثَٰرَة (susCRITE)")
raw_search("أَثَرَة", "أَثَرَة (PLEINE ?)")

print("=" * 70)
print("B. مِيثَاق — mīṯāq. « لفظه كله محذوف » = TOUTES occurrences élidées ?")
plain_search("ميثاق", "مِيثَاق (stripped)")
raw_search("مِيثَٰق", "مِيثَٰق (susCRITE)")
raw_search("مِيثَاق", "مِيثَاق (PLEINE)")

print("=" * 70)
print("C. أَوْثَان — awṯān (les idoles).")
plain_search("وثان", "…وثان (stripped)")
raw_search("أَوْثَٰن", "أَوْثَٰن (susCRITE)")
raw_search("أَوْثَان", "أَوْثَان (PLEINE)")

print("=" * 70)
print("D. أَثَرَ / إِثْر + هُم — le verbe et le nom avec le suffixe.")
plain_search("ثرهم", "…ثرهم (stripped)")
plain_search("ثرهما", "…ثرهما (stripped)")
raw_search("أَثَرَهُمْ", "أَثَرَهُمْ (dhamma)")
raw_search("إِثْرِهِمْ", "إِثْرِهِمْ (kasra)")
raw_search("إِثْرِهِمَا", "إِثْرِهِمَا (kasra + DUEL)")
plain_search("اثر", "…اثر (stripped, large)")

print("=" * 70)
print("E. نَفَّاثَاتٍ — 113:4. Élidée au corpus ?")
raw_search("نَفَّاثَ", "نَفَّاثَ (raw)")
plain_search("نفاث", "نَفَّاثَ (stripped)")

print("=" * 70)
print("F. الْخَبِيثَاتُ — pluriel féminin salim élidé.")
plain_search("خبيث", "…خبيث (stripped)")
raw_search("خَبِيثَٰت", "خَبِيثَٰت (susCRITE)")
raw_search("خَبِيثَات", "خَبِيثَات (PLEINE)")

print("=" * 70)
print("G. يَسْتَغِيثَانِ — le duel.")
plain_search("ستغيث", "…ستغيث (stripped)")
raw_search("يَسْتَغِيثَٰن", "يَسْتَغِيثَٰن (susCRITE)")
raw_search("يَسْتَغِيثَان", "يَسْتَغِيثَان (PLEINE)")

print("=" * 70)
print("H. ثُلُثَا / ثُلُثَانِ / الثُّلُثِ — tous les ثلث du corpus (raw).")
plain_search("ثلث", "…ثلث (stripped)")
raw_search("ثُلُثَٰ", "ثُلُثَٰ (susCRITE)")
raw_search("ثُلُثَا", "ثُلُثَا (PLEINE)")

print("=" * 70)
print("I. أَثَبْ — le mot du vers deux.")
plain_search("اثب", "…اثب (stripped)")

print("=" * 70)
print("J. أَمْثَل — la règle positionnelle (avant/après Maryam).")
plain_search("امثل", "…امثل (stripped, large — à classer)")

print("=" * 70)
print("K. أَثَاثًا — aṯāṯan.")
plain_search("اثاث", "…اثاث (stripped)")
raw_search("أَثَٰث", "أَثَٰث (susCRITE)")
raw_search("أَثَاث", "أَثَاث (PLEINE)")

print("=" * 70)
print("L. ISTITIMĀR Abū Wakīl — نَحْوَ الْهُدَى / نَرَى اللهَ / ذِكْرَى")
plain_search("نحو الهد", "نَحْوَ الْهُدَى")
plain_search("رى الله", "نَرَى اللهَ")
plain_search("ذكرى", "ذِكْرَى")
raw_search("ذِكْرَى", "ذِكْرَى (raw)")

print("=" * 70)
print("M. iʿdād — الصَّلَوْة (l'alif dessinée WĀW) + أَثْل (34:16 ?)")
plain_search("صلوة", "…صلوة (stripped)")
raw_search("صَلَو", "…صَلَو (raw)")
plain_search("اثل", "…اثل (stripped)")
