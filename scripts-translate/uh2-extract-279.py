# -*- coding: utf-8 -*-
# R659 (ouvrier D tick 12:41, claim uh2-279) — extraction leçon 25 ulum-hadith-tanawi-2
# (pdf-mut23h2u-279, الدرس 25 : أنشطة تطبيقية)
# Passation R658 : leçon 25 commence p.129 (أهداف الأنشطة 4 items + أقرا + أطبق),
#   contenu p.130+ (الحديث المطلوب تخريجه ; chaîne أبو هشام الرفاعي … طلحة بن عبيد الله
#   «لكل نبي رفيق» سنن الترمذي أبواب المناقب ; étapes 1-6 de la recherche appliquée).
# Bornes par SONDAGE (jamais devinées) :
#   début = bannière leçon 25 أنشطة تطبيقية (p.129 attendu — à confirmer)
#   borne sup = en-têtes أهداف الدرس de la leçon 26 (الدرس 26 : ورشات عمل للدعم والتطبيق)
# Patron : scripts-translate/uh2-extract-278.py (fitz, couche BRUTE + couche FIX)
import os

import fitz

PDF = "/home/z/my-project/content/textbooks-src/ulum-hadith-2-thanawi_text.pdf"
OUT = "/home/z/my-project/tr-tmp/uh2-l279-raw.txt"
FIRST, LAST = 128, 150  # fenêtre large : fin leçon 24 + leçon 25 (129-?) + sondage borne sup


def fix_line(line: str) -> str:
    """Réinverse l'ordre des mots d'une ligne RTL fournie mot à mot par PyMuPDF."""
    words = line.split()
    return " ".join(reversed(words)) if len(words) > 1 else line


doc = fitz.open(PDF)
print(f"pages totales PDF : {doc.page_count}")
chunks = []
banner25_hits = []
banner26_hits = []
goals_hits = []
for p in range(FIRST, min(LAST, doc.page_count) + 1):
    txt = doc[p - 1].get_text("text")
    raw = f"===== PAGE {p} — BRUTE =====\n{txt}"
    fixed = "\n".join(fix_line(l) for l in txt.splitlines() if l.strip())
    chunks.append(raw + f"\n===== PAGE {p} — FIX (mots réinversés) =====\n{fixed}\n")
    # bannière leçon 25 : « أنشطة تطبيقية » — en brut inversé :
    #   أنشطة → ةطشنأ ; تطبيقية → ةيقبت
    if "ةطشنأ" in txt or "ةيقبت" in txt:
        banner25_hits.append(p)
    # bannière leçon 26 : « ورشات عمل » — ورشات → تاشرو ; عمل → لمع
    if "تاشرو" in txt or "لمع" in txt:
        banner26_hits.append(p)
    # en-têtes أهداف الدرس (candidat borne sup)
    if "درسلا فادهأ" in txt:
        goals_hits.append(p)
out = "\n".join(chunks)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write(out)
print(f"écrit {OUT} ({len(out)} car)")
print("bannière leçon 25 (ةطشنأ/ةيقبت) pages:", banner25_hits)
print("bannière leçon 26 (تاشرو/لمع) pages:", banner26_hits)
print("أهداف الدرس (درسلا فادهأ) pages:", goals_hits)
