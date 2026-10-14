#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — OCR à la demande d'une leçon pdfOnly (scans du ministère des Habous).

Usage : python3 scripts-translate/ocr-one.py <bookId> <docId>

- Lit pdfUrl dans content/books/<bookId>.json pour le docId donné.
- Télécharge le PDF (TLS non vérifié : le certificat de habous.gov.ma n'est pas
  reconnu dans le bac à sable) avec mise en cache /tmp.
- Rend chaque page en PNG 300 dpi (PyMuPDF) puis OCR tesseract (ara,
  tessdata_best — modèle de précision, voir tessdata/ara.traineddata).
- Assemble un HTML directionnel RTL (une section par page) et l'écrit dans
  content/ocr-cache/<docId>.json : { docId, bookId, pages, ocrAt, html }.
- Idempotent : si le cache existe et est valide, il est retourné tel quel.
- Sortie : JSON sur stdout { ok, cached, pages, htmlPath } ou { ok: false, error }.
"""

import json
import os
import ssl
import subprocess
import sys
import time
import urllib.request

HOME = "/home/z/my-project"
CACHE_DIR = f"{HOME}/content/ocr-cache"
TESSDATA = f"{HOME}/scripts-translate/tessdata"

def fail(msg: str) -> None:
    print(json.dumps({"ok": False, "error": msg}, ensure_ascii=False))
    raise SystemExit(1)

def main() -> None:
    if len(sys.argv) != 3:
        fail("usage: ocr-one.py <bookId> <docId>")
    book_id, doc_id = sys.argv[1], sys.argv[2]
    if not book_id.replace("-", "").isalnum() or not doc_id.replace("-", "").replace("_", "").isalnum():
        fail("identifiants invalides")

    book_path = f"{HOME}/content/books/{book_id}.json"
    if not os.path.isfile(book_path):
        fail("livre inconnu")
    with open(book_path, "r", encoding="utf-8") as fh:
        book = json.load(fh)

    lessons = []
    intro = book.get("intro") or {}
    if str(intro.get("docId")) == doc_id:
        lessons.append(intro)
    lessons.extend(book.get("lessons", []))
    doc = next((d for d in lessons if str(d.get("docId")) == doc_id), None)
    if doc is None or not doc.get("pdfOnly") or not doc.get("pdfUrl"):
        fail("document introuvable ou non pdfOnly")

    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_path = f"{CACHE_DIR}/{doc_id}.json"
    if os.path.isfile(cache_path):
        try:
            with open(cache_path, "r", encoding="utf-8") as fh:
                cached = json.load(fh)
            if cached.get("html") and cached.get("pages", 0) > 0:
                print(json.dumps({
                    "ok": True, "cached": True,
                    "pages": cached["pages"], "htmlPath": cache_path,
                }, ensure_ascii=False))
                return
        except Exception:
            pass  # cache corrompu : on recalcule

    pdf_url = doc["pdfUrl"]
    # URL du ministère contient des caractères arabes : encodage pour cent
    # (seule la partie non-ASCII est échappée — « / » et « : » sont préservés).
    from urllib.parse import quote, urlsplit, urlunsplit
    parts = urlsplit(pdf_url)
    pdf_url = urlunsplit(parts._replace(path=quote(parts.path, safe="/%")))
    pdf_path = f"/tmp/ocr-{doc_id}.pdf"
    if not (os.path.isfile(pdf_path) and os.path.getsize(pdf_path) > 1024):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(pdf_url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"})
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp, open(pdf_path, "wb") as out:
            out.write(resp.read())
    if os.path.getsize(pdf_path) < 1024:
        fail("téléchargement vide")

    try:
        import fitz  # PyMuPDF
    except ImportError:
        fail("PyMuPDF indisponible")

    docpdf = fitz.open(pdf_path)
    sections = []
    for i, page in enumerate(docpdf):
        pix = page.get_pixmap(dpi=300)
        png_path = f"/tmp/ocr-{doc_id}-p{i+1}.png"
        pix.save(png_path)
        env = dict(os.environ)
        env["TESSDATA_PREFIX"] = TESSDATA
        try:
            proc = subprocess.run(
                ["tesseract", png_path, "stdout", "-l", "ara", "--psm", "6"],
                capture_output=True, text=True, timeout=180, env=env,
            )
        except subprocess.TimeoutExpired:
            proc = None
        os.remove(png_path)
        if proc is None or proc.returncode != 0:
            sections.append(f'<section class="ocr-page"><p><em>[page {i+1} : OCR indisponible]</em></p></section>')
            continue
        lines = [ln.strip() for ln in proc.stdout.splitlines() if ln.strip()]
        if not lines:
            sections.append(f'<section class="ocr-page"><p><em>[page {i+1} : sans texte détecté]</em></p></section>')
            continue
        body = "\n".join(f"<p>{ln}</p>" for ln in lines)
        sections.append(f'<section class="ocr-page"><h3>صفحة {i+1}</h3>\n{body}</section>')
    docpdf.close()

    html = "\n".join(sections)
    payload = {
        "docId": doc_id, "bookId": book_id,
        "pages": len(sections), "ocrAt": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "pdfUrl": pdf_url, "html": html,
    }
    tmp = cache_path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False)
    os.replace(tmp, cache_path)
    print(json.dumps({"ok": True, "cached": False, "pages": len(sections), "htmlPath": cache_path}, ensure_ascii=False))

if __name__ == "__main__":
    main()
