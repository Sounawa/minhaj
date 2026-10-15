#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Injection de la leçon 576 (pdf-only, 14e leçon tafsir-2es).

576 = سورة الحديد (الآيات 24-26) = Ḥafṣ 25-27 (règle R84 : manual N = Ḥafṣ N+1
pour N≥15). Bloc = 3 versets Warš du cache (Ḥadīd Ḥafṣ 25-27), numérotation
madrasa ٢٤-٢٦ (label pixel-vérifié [سورة الحديد: ٢٤-٢٦], fin de bloc فاسقون ۝٢٦).

Vérifications R86 (tesseract multi-résolutions 300/600 dpi × multi-seuils + VLM
sur les chiffres de refs) :
- [البحر المحيط لأبي حيان: 114/10] — 4 confirmé (pas 8), volume 10 ✓
- [التحرير والتنوير... بتصرف: 418/27] — le 8 est un 8 (pas 410) ✓
- [مفاتيح الغيب...: 470/29] — le 0 est un 0 (pas 478) ✓
- Rāzī : «مدار التكليف» (600 dpi, pas الكون) ; «وهو العارف» (3 lectures,
  flag variante vs edition «العلم») ; «والزائد» (5 lectures) ; «وكان أشرف
  الأقسام» (و sans point ×3, flag variante vs edition «فكان») ;
  «رعاية الصلاح الروحانية / رعاية المصالح الجسمانية» (paire confirmée).
- Bullet 2 maqāṣid complet : «...التي تحرر الإنسان وتقوم على قيم العدل
  والإنصاف والفضيلة» (2 lignes pixel-vérifiées 600 dpi).
- إعداد expression 1 = «كِفْلَيْنِ» (mot rare Ḥadīd 28 = leçon 577).
"""
import json, re

BOOK = "/home/z/my-project/content/books/tafsir-2es.json"
AR576 = "/home/z/my-project/tr-tmp/576-ar.html"
FR576 = "/home/z/my-project/tr-tmp/576-fr.html"
DOCID = "pdf-mut23h33-576"

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

html576 = open(AR576, encoding="utf-8").read().strip()
fr576 = open(FR576, encoding="utf-8").read().strip()
assert html576.startswith("<h1>") and fr576.startswith("<h1>")
assert "{{" not in fr576 and "<img" not in fr576
assert "۞" not in html576

data = json.load(open(BOOK, encoding="utf-8"))
lessons = {les.get("docId"): les for les in data["lessons"]}

les = lessons[DOCID]
assert "24" in les["titleAr"], les["titleAr"]
les["html"] = html576
les["htmlFr"] = fix_fr(fr576)
les["pdfOnly"] = False

json.dump(data, open(BOOK, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("OK — 576 injectée :", len(html576), "car AR,", len(fix_fr(fr576)), "car FR")
print("titleAr:", les["titleAr"], "| titleFr:", les["titleFr"])
