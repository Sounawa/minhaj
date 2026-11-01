#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj R91 — Fetch de la page habous.gov.ma d'une leçon : captions + URLs d'images-versets."""
import json
import re
import ssl
import sys
import urllib.request
from urllib.parse import quote

TREE = "/home/z/my-project/content/source-tree.json"

def main() -> None:
    doc_id = sys.argv[1]
    tree = json.load(open(TREE, encoding="utf-8"))
    entry = next(e for e in tree["entries"] if str(e.get("docId")) == doc_id)
    url = "https://www.habous.gov.ma/" + quote(entry["pathAr"])
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"})
    try:
        with urllib.request.urlopen(req, timeout=45, context=ctx) as r:
            html = r.read().decode("utf-8", "replace")
    except Exception as e:
        print(json.dumps({"ok": False, "error": str(e), "url": url}, ensure_ascii=False))
        return
    # images du corps de la leçon
    imgs = re.findall(r'<img[^>]+src="([^"]+)"[^>]*>', html)
    imgs = [u for u in imgs if "logo" not in u.lower() and "icon" not in u.lower()]
    # captions
    caps = re.findall(r"سور[ةَُِّ ]+[\u0600-\u06FF\s]+الآية[\u0600-\u06FF\s]*\d+", html)
    # séquence textuelle approximative autour des captions
    print(json.dumps({
        "ok": True, "url": url, "len": len(html),
        "imgCount": len(imgs), "images": imgs[:14],
        "captions": caps[:12],
    }, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
