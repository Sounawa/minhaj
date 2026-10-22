#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download verse images from a habous page."""
import re
import sys
import urllib.parse
import urllib.request
import ssl
import os

HOME = "/home/z/my-project"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

page = sys.argv[1]  # habous html file
doc_id = sys.argv[2]  # docId for output naming

html = open(page, encoding="utf-8", errors="replace").read()
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
verse_imgs = [i for i in imgs if "AhabousAR" in urllib.parse.unquote(i)]
os.makedirs(f"{HOME}/tr-tmp", exist_ok=True)

for i in verse_imgs:
    if i.startswith("http"):
        url = i
    else:
        url = "https://www.habous.gov.ma" + urllib.parse.quote(i, safe="/%")
    name = urllib.parse.unquote(i).split("/")[-1]
    # normalize weird chars in filename for local fs
    local = f"{HOME}/tr-tmp/{doc_id}-img-{name}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=40, context=ctx).read()
        with open(local, "wb") as fh:
            fh.write(data)
        print(f"OK  {len(data):>7} bytes  {name}")
    except Exception as e:
        print(f"ERR {name}: {e}")
