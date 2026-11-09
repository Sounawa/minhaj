#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R93 — OCR d'une leçon depuis un PDF manuel LOCAL (archive.org).

Usage : python3 scripts-translate/ocr-local-r93.py <bookId> <docId> <pdfPath> <première> <dernière>

- Rend les pages [première..dernière] (1-based) en PNG 300 dpi (PyMuPDF)
  puis OCR tesseract (ara, tessdata_best).
- Assemble le même format que ocr-one.py et écrit content/ocr-cache/<docId>.json
  ({ docId, bookId, pages, ocrAt, pdfUrl, html }) — pdfUrl repris du CMS
  pour la provenance.
- Idempotent : cache existant valide → retourné tel quel.
"""
import json
import os
import subprocess
import sys
import time

HOME = "/home/z/my-project"
CACHE_DIR = f"{HOME}/content/ocr-cache"
TESSDATA = f"{HOME}/scripts-translate/tessdata"


def fail(msg: str) -> None:
    print(json.dumps({"ok": False, "error": msg}, ensure_ascii=False))
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 6:
        fail("usage: ocr-local-r93.py <bookId> <docId> <pdfPath> <première> <dernière>")
    book_id, doc_id, pdf_path, p1, p2 = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
    if p2 < p1:
        fail("plage invalide")
    book_path = f"{HOME}/content/books/{book_id}.json"
    book = json.load(open(book_path, encoding="utf-8"))
    doc = next((d for d in book.get("lessons", []) if str(d.get("docId")) == doc_id), None)
    if doc is None:
        fail("docId inconnu dans le book")
    cms_url = doc.get("pdfUrl") or ""

    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_path = f"{CACHE_DIR}/{doc_id}.json"
    if os.path.isfile(cache_path):
        try:
            cached = json.load(open(cache_path, encoding="utf-8"))
            if cached.get("html") and cached.get("pages", 0) > 0:
                print(json.dumps({"ok": True, "cached": True, "pages": cached["pages"]}, ensure_ascii=False))
                return
        except Exception:
            pass

    try:
        import fitz
    except ImportError:
        fail("PyMuPDF indisponible")

    pdf = fitz.open(pdf_path)
    if p2 > len(pdf):
        fail(f"le PDF n'a que {len(pdf)} pages")
    sections = []
    for i in range(p1 - 1, p2):
        pix = pdf[i].get_pixmap(dpi=300)
        png = f"/tmp/ocrL-{doc_id}-p{i+1}.png"
        pix.save(png)
        env = dict(os.environ)
        env["TESSDATA_PREFIX"] = TESSDATA
        try:
            proc = subprocess.run(["tesseract", png, "stdout", "-l", "ara", "--psm", "6"],
                                  capture_output=True, text=True, timeout=240, env=env)
        except subprocess.TimeoutExpired:
            proc = None
        os.remove(png)
        if proc is None or proc.returncode != 0:
            sections.append(f'<section class="ocr-page"><h3>صفحة {i+1}</h3>\n<p><em>[page {i+1} : OCR indisponible]</em></p></section>')
            continue
        lines = [ln.strip() for ln in proc.stdout.splitlines() if ln.strip()]
        body = "\n".join(f"<p>{ln}</p>" for ln in lines) or "<p><em>[sans texte détecté]</em></p>"
        sections.append(f'<section class="ocr-page"><h3>صفحة {i+1}</h3>\n{body}</section>')
    pdf.close()

    payload = {
        "docId": doc_id, "bookId": book_id,
        "pages": len(sections), "ocrAt": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "pdfUrl": cms_url,
        "html": "\n".join(sections),
    }
    tmp = cache_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False)
    os.replace(tmp, cache_path)
    print(json.dumps({"ok": True, "cached": False, "pages": len(sections)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
