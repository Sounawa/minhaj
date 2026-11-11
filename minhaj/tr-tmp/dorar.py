#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch dorar.net hadith search results and print cleaned entries."""
import re, html, sys, urllib.parse, urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

def fetch(q):
    url = "https://dorar.net/hadith/search?q=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")

def clean(seg):
    seg = html.unescape(seg)
    txt = re.sub(r"<[^>]+>", " ", seg)
    txt = re.sub(r"[\t\r\n]+", " ", txt)
    txt = re.sub(r" {2,}", " ", txt)
    return txt.strip()

def results(raw, n=3):
    out = []
    for m in re.finditer(r"الراوي", raw):
        seg = raw[m.start():m.start()+2600]
        if "التخريج" not in seg:
            continue
        line = clean(seg)
        # hadith text = what precedes 'الراوي' -> backtrack
        pre = raw[max(0, m.start()-3200):m.start()]
        htxt = clean(pre)
        for marker in ("خلاصة حكم المحدث", "أصول الحديث", "الحديث كاملاً"):
            cut = htxt.rfind(marker)
            if cut > 0:
                htxt = htxt[:cut]
        htxt = htxt.strip(" |")
        def field(name, maxlen=200):
            mm = re.search(name + r"\s*:\s*([^|]{1,%d})" % maxlen, line)
            return mm.group(1).strip() if mm else "?"
        out.append({
            "narrator": field("الراوي", 60),
            "verdict": field("خلاصة حكم المحدث", 120),
            "muhaddith": field("المحدث", 60),
            "source": field("المصدر", 80),
            "takhrij": field("التخريج", 260),
            "text": htxt[-750:],
        })
    # dedupe by takhrij+text head
    seen, ded = set(), []
    for o in out:
        k = o["takhrij"][:60] + o["text"][-80:]
        if k not in seen:
            seen.add(k)
            ded.append(o)
    return ded[:n]

if __name__ == "__main__":
    q = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    raw = fetch(q)
    for i, o in enumerate(results(raw, n), 1):
        print(f"=== RESULT {i} ===")
        print("الراوي:", o["narrator"], "| حكم:", o["verdict"], "| المحدث:", o["muhaddith"])
        print("المصدر:", o["source"])
        print("التخريج:", o["takhrij"])
        print("نص (fin):", o["text"][-500:])
        print()
