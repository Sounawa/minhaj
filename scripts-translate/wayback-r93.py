#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R93 — sondes Wayback Machine : les PDF habous.gov.ma ont-ils des snapshots ?"""

import json
import ssl
import urllib.request
import urllib.parse

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
HDRS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}


def wayback(url):
    api = "http://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    req = urllib.request.Request(api, headers=HDRS)
    try:
        with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
            d = json.loads(r.read().decode())
        snap = (d.get("archived_snapshots") or {}).get("closest") or {}
        if snap.get("available"):
            return f"SNAPSHOT {snap.get('timestamp')} -> {snap.get('url')}"
        return "aucun snapshot"
    except Exception as e:
        return f"ERR:{type(e).__name__}:{str(e)[:60]}"


def cdx(url):
    """CDX complète (plus fiable que l'API available)."""
    api = "http://web.archive.org/cdx/search/cdx?url=" + urllib.parse.quote(url, safe="") + "&output=json&limit=5"
    req = urllib.request.Request(api, headers=HDRS)
    try:
        with urllib.request.urlopen(req, timeout=40, context=CTX) as r:
            rows = json.loads(r.read().decode())
        if len(rows) <= 1:
            return "CDX: vide"
        out = []
        for row in rows[1:]:
            out.append(f"{row[1]} {row[4]} {row[3]}")
        return "CDX: " + " | ".join(out)
    except Exception as e:
        return f"CDX ERR:{type(e).__name__}:{str(e)[:50]}"


URLS = [
    ("faraid 311", "https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/الفرائض-الثالثة-ثانوي/2B0631.PDF"),
    ("faraid 312", "https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/الفرائض-الثالثة-ثانوي/371171.PDF"),
    ("faraid 313", "https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/الفرائض-الثالثة-ثانوي/4F0571.PDF"),
    ("tafsir2es 563", "https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/التفسير-الثانية-إعدادي/827-21.PDF"),
    ("rasm5ep 623", "https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/الرسم-و-الضبط-الخامس-ابتدائي/156741.PDF"),
    ("fiqh3es pdf-1", "https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/الفقه-الثالث-إعدادي/1._البيع_والربا_في_الطعام.pdf"),
    ("répertoire faraid", "https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/الفرائض-الثالثة-ثانوي/"),
    ("répertoire drus", "https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/"),
]

for label, url in URLS:
    print(f"--- {label} ---")
    print("  ", wayback(url))
    print("  ", cdx(url))
