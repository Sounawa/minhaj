#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R576 — sondage de bornes des 3 nouvelles sources acquises au miroir
(tafsir-1-iadadi, tafsir-2-iadadi, ulum-hadith-1-thanawi).
Méthode éprouvée hadith2-map.py / kahf-map.py : chercher les en-têtes
« أهداف الدرس » page par page, JAMAIS deviner. Sorte : tr-logs/map-r576.txt
+ json des occurrences (page, contexte court) pour arbitrage au prochain tour.
"""
import json
import os
import re

from pypdf import PdfReader

HOME = "/home/z/my-project"
SRC = os.path.join(HOME, "content", "textbooks-src")
OUT_TXT = os.path.join(HOME, "tr-logs", "map-r576.txt")
OUT_JSON = os.path.join(HOME, "tr-logs", "map-r576.json")

BOOKS = ["tafsir-1-iadadi", "tafsir-2-iadadi", "ulum-hadith-1-thanawi"]

# marqueurs d'en-tête de leçon (idem sondages R511+ : jamais devinés)
MARKERS = [
    "أهداف الدرس",
    "أهداف الدروس",
    "اهداف الدرس",
]
NUM_RE = re.compile(r"الدرس\s*[:٫.،]?\s*(\d{1,3})|\((\d{1,3})\)")


def ar_digits_to_int(s: str):
    """Chiffres OCR latins/arabes → int (prudence : peuvent être inversés)."""
    table = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
    s = s.translate(table)
    m = re.search(r"\d{1,3}", s)
    return int(m.group()) if m else None


def probe(book: str):
    path = os.path.join(SRC, book + ".pdf")
    reader = PdfReader(path)
    hits = []
    for i, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception:  # noqa: BLE001
            text = ""
        flat = re.sub(r"\s+", " ", text)
        for mk in MARKERS:
            if mk in flat:
                pos = flat.find(mk)
                ctx = flat[max(0, pos - 60):pos + 60]
                # numéro de leçon éventuel à proximité
                seg = flat[max(0, pos - 80):pos + 80]
                nm = NUM_RE.search(seg)
                num = ar_digits_to_int(nm.group(0)) if nm else None
                hits.append({"page": i, "marker": mk, "num": num,
                             "ctx": ctx[:120], "chars": len(flat)})
                break
        # pages quasi vides → indicateur de fin de livre / séparateurs
        if len(flat) < 40:
            hits.append({"page": i, "marker": "__QUASI_VIDE__",
                         "num": None, "ctx": flat[:40], "chars": len(flat)})
    return len(reader.pages), hits


def main() -> int:
    report = {}
    lines = ["# map-r576 — sondage bornes 3 nouvelles sources (ÉTAPE 6)",
             "# occurrences LUES dans la couche texte, aucune borne devinée",
             "# chiffres OCR possiblement inversés — arbitrage à l'image requis",
             ""]
    for book in BOOKS:
        pages, hits = probe(book)
        report[book] = {"pages": pages, "hits": hits}
        lines.append(f"## {book} — {pages} pages, {len(hits)} repères")
        for h in hits:
            if h["marker"] == "__QUASI_VIDE__":
                lines.append(f"  p.{h['page']:>3}  [quasi vide, {h['chars']} car]")
            else:
                lines.append(
                    f"  p.{h['page']:>3}  {h['marker']}  num={h['num']}"
                    f"  …{h['ctx']}…")
        lines.append("")
    with open(OUT_TXT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=1)
    print("\n".join(lines[:4]))
    print(f"→ {OUT_TXT} / {OUT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
