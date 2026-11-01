#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R108 — Écriture du cache OCR officiel pdf-mut23h36-621 (فهرس الأعلام).

Assemble, depuis le cru tesseract (300 dpi, psm 6, tessdata_best) produit par
probe-r108.py, le JSON du cache : { docId, bookId, pages, ocrAt, pdfUrl, html }
avec une section par page (p167-169), sur le modèle des caches 619/620.
"""
import json
import time

HOME = "/home/z/my-project"
DOC_ID = "pdf-mut23h36-621"
BOOK_ID = "tafsir-3es"
PDF_URL = ("https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/"
           "التفسير-الثالثة-إعدادي/فهرس_الأعلام.pdf")
PAGES = [167, 168, 169]

sections = []
for p in PAGES:
    with open(f"{HOME}/tr-tmp/probe-r108/ocr-p{p}.txt", "r", encoding="utf-8") as fh:
        lines = [ln.strip() for ln in fh.read().splitlines() if ln.strip()]
    body = "\n".join(f"<p>{ln}</p>" for ln in lines)
    sections.append(f'<section class="ocr-page"><h3>صفحة {p}</h3>\n{body}</section>')

payload = {
    "docId": DOC_ID,
    "bookId": BOOK_ID,
    "pages": len(sections),
    "ocrAt": time.strftime("%Y-%m-%dT%H:%M:%S"),
    "pdfUrl": PDF_URL,
    "html": "\n".join(sections),
}
out = f"{HOME}/content/ocr-cache/{DOC_ID}.json"
tmp = out + ".tmp"
with open(tmp, "w", encoding="utf-8") as fh:
    json.dump(payload, fh, ensure_ascii=False)
    fh.write("\n")
import os
os.replace(tmp, out)
print(f"cache écrit : {out} ({len(sections)} pages, html {len(payload['html'])} car)")
