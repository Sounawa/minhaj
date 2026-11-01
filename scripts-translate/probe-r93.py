#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R93 — sondes habous.gov.ma : le site restructuré sert-il encore les PDF
du manuel الفرائض الثالثة ثانوي (et voisins) sous un autre chemin ?"""

import ssl
import urllib.request
import urllib.error
import urllib.parse

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE
HDRS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}


def enc(url):
    """Encode le chemin (caractères non-ASCII) en pourcentage, préserve le schéma/hôte."""
    parts = urllib.parse.urlsplit(url)
    path = urllib.parse.quote(parts.path)
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.frag if hasattr(parts, "frag") else parts.fragment))


def probe(url, method="GET"):
    req = urllib.request.Request(url, headers=HDRS, method=method)
    try:
        with urllib.request.urlopen(req, timeout=25, context=CTX) as r:
            body = r.read(400)
            return r.status, r.headers.get("Content-Type", "?"), len(body), body[:120]
    except urllib.error.HTTPError as e:
        return e.code, "-", 0, b""
    except Exception as e:
        return f"ERR:{type(e).__name__}", str(e)[:60], 0, b""


TESTS = [
    ("base site", "https://www.habous.gov.ma/"),
    ("page drus 2024", "https://www.habous.gov.ma/images/2024/"),
    ("old faraid 311", "https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/الفرائض-الثالثة-ثانوي/2B0631.PDF"),
    ("faraid 311 .pdf min", "https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/الفرائض-الثالثة-ثانوي/2B0631.pdf"),
    ("faraid sans doublon seg", "https://www.habous.gov.ma/images/2024/التعليم-العتيق/الفرائض-الثالثة-ثانوي/2B0631.PDF"),
    ("faraid 2025", "https://www.habous.gov.ma/images/2025/التعليم-العتيق/دروس-التعليم-العتيق/الفرائض-الثالثة-ثانوي/2B0631.PDF"),
    ("faraid 311 via fr", "https://www.habous.gov.ma/images/2024/الفرائض-الثالثة-ثانوي/2B0631.PDF"),
    ("fiqh-3es pdf-1", "https://www.habous.gov.ma/images/2024/التعليم-العتيق/دروس-التعليم-العتيق/الفقه-الثالث-إعدادي/1._البيع_والربا_في_الطعام.pdf"),
]

for label, url in TESTS:
    st, ct, ln, head = probe(enc(url))
    print(f"{label:26s} -> {st} {ct} ({ln} o) {head[:80]!r}")
