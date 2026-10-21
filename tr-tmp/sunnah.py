#!/usr/bin/env python3
"""Minhāj — fetch + parse sunnah.com hadith page (Arabic full text)."""
import re, sys, subprocess, html as H
def fetch(url):
    r = subprocess.run(['curl','-s','-A','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36','--max-time','25',url], capture_output=True, text=True)
    return r.stdout
def parse(raw):
    m = re.search(r'<title>(.*?)</title>', raw, re.S)
    title = H.unescape(m.group(1)).strip() if m else '?'
    texts = []
    for mm in re.finditer(r'<div[^>]*>(.*?)</div>', raw, re.S):
        t = re.sub(r'<[^>]+>', ' ', mm.group(1)); t = H.unescape(t)
        if re.search(r'[\u0600-\u06FF]{10,}', t):
            t = re.sub(r'\s+', ' ', t).strip()
            if len(t) > 80: texts.append(t)
    full = max(texts, key=len) if texts else ''
    bab = next((t for t in texts if 'باب' in t[:12]), '')
    return title, bab, full
if __name__ == '__main__':
    for url in sys.argv[1:]:
        raw = fetch(url)
        title, bab, full = parse(raw)
        print(f'== {url}')
        print('TITLE:', title[:110])
        if bab: print('BAB:', bab[:130])
        print('TEXT:', full[:900])
        print('---')
