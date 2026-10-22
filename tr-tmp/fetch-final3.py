#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch habous pages for 11503-11505 and count verse images."""
import re
import urllib.parse
import subprocess

base = "https://www.habous.gov.ma/برنامج-التعليم-العتيق-الرئيسية/1546-المجلس-الأولى/الفقه/الإعدادي/"
docs = {
    "11503": "لائحة-الأعلام",
    "11504": "لائحة-المصادر-والمراجع-الفقه-من-متن-الرسالة-لابن-أبي-زيد-القيرواني-بشرح-كفاية-الطالب-الرباني",
    "11505": "كتاب-الفقه-من-متن-الرسالة-لابن-أبي-زيد-القيرواني-بشرح-كفاية-الطالب-الرباني-للسنة-الأولى-من-التعليم-الإعدادي-العتيق",
}
for doc, slug in docs.items():
    url = base + doc + "-" + slug + ".html"
    enc = urllib.parse.quote(url, safe="/:")
    r = subprocess.run(
        ["curl", "-sk", "-L", "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
         "--max-time", "30", enc],
        capture_output=True, text=True,
    )
    html = r.stdout
    with open(f"/home/z/my-project/tr-tmp/{doc}-habous.html", "w", encoding="utf-8") as fh:
        fh.write(html)
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    verses = [i for i in imgs if "AhabousAR" in urllib.parse.unquote(i)]
    names = [urllib.parse.unquote(v).split("/")[-1] for v in verses]
    print(f"{doc}: {len(html)} bytes, {len(verses)} verse images {names[:6]}")
