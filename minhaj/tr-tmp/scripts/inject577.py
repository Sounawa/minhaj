#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Injection de la leçon 577 (pdf-only, 15e leçon tafsir-2es).

577 = سورة الحديد (الآيتان 27-28) = Ḥafṣ 28-29 (règle R84 : manual N = Ḥafṣ
N+1). Bloc = 2 versets Warš du cache (Ḥadīd Ḥafṣ 28-29 = cache ar[27]+ar[28]),
marqueurs muṣḥaf ۝٢٧-۝٢٨ (décompte marocain 28 versets, VLM×2 + glyphe-ASCII :
٢ = crochet-base ×2, ٨ = double anneau = glyphe comp11 du marqueur ۝٢٨).

Vérifications R90 (tesseract 300+600 dpi × multi-seuils + VLM sur chiffres) :
- LABEL imprimé [سورة الحديد: 28-29] = décompte Ḥafṣ (INCONSISTANCE du manuel
  vs ses propres marqueurs ۝٢٧-۝٢٨ !) — rendu tel qu'imprimé + NdT FR.
- [صحيح البخاري؛ كتاب الجهاد والسير؛ باب فضل من أسلم من أهل الكتابين] ✓
- [التحرير والتنوير للطاهر بن عاشور: 433/27] ✓ (VLM+tesseract concordants)
- [البحر المديد لابن عجيبة؛ 332/7] ✓ (VLM+tesseract)
- [الأنعام: 123 imprimé] = COQUILLE → 122 (le verset cité «وَجَعَلْنَا لَهُۥ
  نُورًۭا يَمْشِى بِهِۦ فِى ٱلنَّاسِ» = 6:122 Ḥafṣ ET Warš cache) — corrigé + NdT.
- [البقرة: 6 imprimé] = COQUILLE → 7 («خَتَمَ ٱللَّهُ عَلَىٰ قُلُوبِهِمْ» =
  2:7 Ḥafṣ ET Warš) — corrigé + NdT.
- Titre banner = الآيتان ٢٧-٢٨ (tesseract "27-", marqueurs cohérents, CMS).
- Règle d'or idad→glose 8e fois : كِفْلَيْنِ (نصيبين inline tafsīr) +
  اتقوا الله (glose 1) + وآمنوا برسوله (glose 2) ✓✓✓
- «ظَهَرَتِ التربية» (pointe du ẓāʾ visible au pixel, t200 concordant) ;
  «فإن حط رأسه» (t185+t200) ; «بالمغفرة» (VLM, contexte 3 promesses) ;
  «لماذا ضاعف» (VLM + grammaire, OCR lisait اذا) ; «في الآيتين» (dual,
  descendeurs ين visibles).
- Idad 578 (المجادلة 1-4) transcrits avec confiance variable : وَزُورًا (élevée),
  فِي زَوْجِهَا (moyenne-haute), قَوْلَ / مَنْكَرًا مِنَ الْقَوْلِ / يَتَمَاسَّا
  (moyenne — la glose de 578 tranchera, pattern R78).
"""
import json, re

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"
AR577 = "/home/z/my-project/tr-tmp/577-ar.html"
FR577 = "/home/z/my-project/tr-tmp/577-fr.html"
DOCID = "pdf-mut23h33-577"

NB = "\u202f"
def fix_fr(s: str) -> str:
    """Mêmes auto-fixes que scripts-translate/qa-lesson.py (nœuds texte uniquement)."""
    parts = re.split(r"(<[^>]+>)", s)
    for k, tok in enumerate(parts):
        if tok.startswith("<"):
            continue
        tok = tok.replace(" ;", NB + ";").replace(" :", NB + ":").replace(" !", NB + "!")
        tok = tok.replace(" ?", NB + "?").replace(" »", NB + "»").replace("« ", "«" + NB)
        tok = tok.replace("'", "\u2019")
        tok = re.sub(r"  +", " ", tok)
        parts[k] = tok
    return "".join(parts)

html577 = open(AR577, encoding="utf-8").read().strip()
fr577 = open(FR577, encoding="utf-8").read().strip()
assert html577.startswith("<h1>") and fr577.startswith("<h1>")
assert "{{" not in fr577 and "<img" not in fr577
assert "۞" not in html577

data = json.load(open(BOOK, encoding="utf-8"))
lessons = {les.get("docId"): les for les in data["lessons"]}

les = lessons[DOCID]
assert "27" in les["titleAr"], les["titleAr"]
les["html"] = html577
les["htmlFr"] = fix_fr(fr577)
les["pdfOnly"] = False

json.dump(data, open(BOOK, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("OK — 577 injectée :", len(html577), "car AR,", len(fix_fr(fr577)), "car FR")
print("titleAr:", les["titleAr"], "| titleFr:", les["titleFr"])
