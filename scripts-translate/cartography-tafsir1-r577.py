#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R577 — cartographie OCR de tafsir-1-iadadi.pdf (150 p), méthode hadith2/l23
validée : fitz 300/200 dpi + tesseract ara (tessdata du dépôt) — zéro API vision.
PASS 1 : OCR 200 dpi intégral (rapide) → candidats « أهداف الدرس ».
PASS 2 : re-OCR 300 dpi des pages candidates ±1 → adjudication numéros.
Anti-doublon pré-production : claim O_EXCL tr-tmp/claims/preprod-tafsir1-iadadi
 (expiration 50 min, idem claim-lesson.py).
Sorties : tr-tmp/r577-t1/ocr-200/p<N>.txt, tr-logs/map-tafsir1-iadadi.txt/.json
Usage : python3 scripts-translate/cartography-tafsir1-r577.py [first last]
"""
import glob
import json
import os
import re
import subprocess
import sys

import fitz

HOME = "/home/z/my-project"
PDF = f"{HOME}/content/textbooks-src/tafsir-1-iadadi.pdf"
WORK = f"{HOME}/tr-tmp/r577-t1"
CLAIM = f"{HOME}/tr-tmp/claims/preprod-tafsir1-iadadi.claim.json"
TESSDATA = f"{HOME}/scripts-translate/tessdata"
OUT_TXT = f"{HOME}/tr-logs/map-tafsir1-iadadi.txt"
OUT_JSON = f"{HOME}/tr-logs/map-tafsir1-iadadi.json"

MARKERS = ["أهداف الدرس", "أهداف الدروس", "اهداف الدرس", "أهداف الدرس"]
NUM_RE = re.compile(r"الدَّرْس\s*(\S{0,12})|الدرس\s*(\S{0,12})|الدروس\s*(\S{0,12})")
AR_DIG = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")


def ocr_page(doc, n: int, dpi: int, outdir: str) -> str:
    """Rendu + OCR d'une page (1-based), cache texte par dpi."""
    os.makedirs(outdir, exist_ok=True)
    tp = f"{outdir}/p{n}.txt"
    if os.path.exists(tp) and os.path.getsize(tp) > 0:
        return open(tp, encoding="utf-8").read()
    png = f"{outdir}/p{n}.png"
    if not os.path.exists(png):
        doc[n - 1].get_pixmap(dpi=dpi).save(png)
    env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
    r = subprocess.run(["tesseract", png, tp[:-4], "-l", "ara", "--psm", "4"],
                       env=env, capture_output=True, text=True)
    if r.returncode != 0:
        return ""
    txt = open(tp, encoding="utf-8").read() if os.path.exists(tp) else ""
    os.remove(png)  # économie disque — re-rendu possible si re-OCR
    return txt


def preprod_claim():
    """O_EXCL — si déjà pris, on signale et on sort (jamais de chevauchement)."""
    os.makedirs(os.path.dirname(CLAIM), exist_ok=True)
    try:
        fd = os.open(CLAIM, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        stamp = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"],
                               capture_output=True, text=True).stdout.strip()
        os.write(fd, json.dumps({
            "utc": stamp,
            "trace_id": "1a19c7c0ffb4f845-cron-agent-loop-202611050522",
            "objet": "cartographie OCR tafsir-1-iadadi (R577)",
        }).encode())
        os.close(fd)
        return True
    except FileExistsError:
        age = (os.path.getmtime(CLAIM) and __import__("time").time()
               - os.path.getmtime(CLAIM)) / 60
        if age > 50:
            os.remove(CLAIM)
            return preprod_claim()  # takeover, périmé
        return False


def main() -> int:
    if not preprod_claim():
        print("CLAIM PRIS par un autre ouvrier → j'abandonne la cartographie "
              "(anti-doublon)")
        return 2
    doc = fitz.open(PDF)
    total = doc.page_count
    first = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    last = int(sys.argv[2]) if len(sys.argv) > 2 else total
    print(f"PASS 1 — OCR 200 dpi pages {first}-{last} / {total}")
    hits = []
    for n in range(first, last + 1):
        txt = ocr_page(doc, n, 200, f"{WORK}/ocr-200")
        flat = re.sub(r"\s+", " ", txt)
        for mk in MARKERS:
            if mk in flat:
                pos = flat.find(mk)
                seg = flat[max(0, pos - 60):pos + 90]
                nm = NUM_RE.search(seg)
                hits.append({"page": n, "ctx": seg[:140],
                             "num_raw": (nm.group(0) if nm else None)})
                print(f"  CANDIDAT p.{n}: …{seg[:110]}…")
                break
    print(f"PASS 1 fini : {len(hits)} candidats — pages déjà OCRisées en cache")
    json.dump({"total_pages": total, "pass1": hits},
              open(f"{WORK}/pass1.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    # PASS 2 — adjudication 300 dpi des candidates ±1
    print("PASS 2 — adjudication 300 dpi")
    adjs = []
    done = set()
    for h in hits:
        for n in (h["page"] - 1, h["page"], h["page"] + 1):
            if n < 1 or n > total or n in done:
                continue
            done.add(n)
            txt = ocr_page(doc, n, 300, f"{WORK}/ocr-300")
            flat = re.sub(r"\s+", " ", txt)
            mks = [mk for mk in MARKERS if mk in flat]
            num = None
            if mks:
                seg = flat[max(0, flat.find(mks[0]) - 80):flat.find(mks[0]) + 100]
                nm = NUM_RE.search(seg)
                num = nm.group(0) if nm else None
                adjs.append({"page": n, "num_raw": num, "ctx": seg[:150]})
                print(f"  ADJ p.{n}: num_raw={num} …{seg[:100]}…")
    json.dump({"total_pages": total, "pass1": hits, "pass2": adjs},
              open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    lines = [f"# map-tafsir1-iadadi — cartographie OCR (R577) {total} pages",
             "# occurrences LUES, chiffres OCR possiblement inversés — jamais devinés", ""]
    for a in adjs:
        lines.append(f"  p.{a['page']:>3}  أهداف الدرس  num_raw={a['num_raw']}  …{a['ctx'][:120]}…")
    open(OUT_TXT, "w", encoding="utf-8").write("\n".join(lines))
    print(f"→ {OUT_TXT} / {OUT_JSON} — {len(adjs)} en-têtes adjudiqués")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
