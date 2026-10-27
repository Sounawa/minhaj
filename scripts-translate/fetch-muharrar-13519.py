#!/usr/bin/env python3
# Extraction intégrale du Muḥarrar al-wajīz (quran-tafsir.net/atia) — Naḥl 57-59
import re, html, urllib.request

def fetch(a):
    url = f'https://quran-tafsir.net/atia/sura16-aya{a}.html'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    t = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'replace')
    t = re.sub(r'<script.*?</script>', '', t, flags=re.S)
    t = re.sub(r'<style.*?</style>', '', t, flags=re.S)
    t = re.sub(r'<[^>]+>', '\n', t)
    t = html.unescape(t)
    t = re.sub(r'[ \t]+', ' ', t)
    lines = [l.strip() for l in t.split('\n') if l.strip()]
    txt = '\n'.join(lines)
    # le contenu du tafsir commence après le marqueur de l'auteur
    m = re.search(r'المحرر الوجيز في تفسير الكتاب العزيز لابن عطية - ابن عطية\n', txt)
    if m:
        txt = txt[m.end():]
    open(f'/home/z/my-project/tr-tmp/13519-muharrar-{a}.txt', 'w').write(txt)
    print(f'=== AYA {a} : {len(txt)} car ===')
    print(txt[:4000])
    print('...\n')

for a in (57, 58, 59):
    fetch(a)
