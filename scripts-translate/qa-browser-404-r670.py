# -*- coding: utf-8 -*-
"""Minhāj — QA navigateur leçon 404 (R670) : 1280/390, DOM, overflow, captures."""
from playwright.sync_api import sync_playwright

SRC = "file:///home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-404-fr.html"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r670"

with sync_playwright() as p:
    b = p.chromium.launch()
    for w, h, tag in ((1280, 800, "desktop"), (390, 700, "mobile")):
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.goto(SRC)
        pg.wait_for_timeout(400)
        m = pg.evaluate("""() => {
            const d=document;
            const h1=d.querySelector('h1'), h2s=d.querySelectorAll('h2'), lis=d.querySelectorAll('li');
            const b=d.body;
            const ol=(b.scrollWidth||0), il=(b.clientWidth||0);
            const meta=d.querySelector('.lesson-meta');
            return {
                dom: (d.documentElement.outerHTML||'').length,
                text: (b.innerText||'').length,
                h1: h1 ? h1.innerText.slice(0,60) : '',
                h2: h2s.length, li: lis.length,
                metaDts: meta ? meta.querySelectorAll('dt').length : 0,
                overflowX: ol > il + 2, scrollW: ol, clientW: il,
                hasArabic: /[\u0600-\u06FF]/.test(b.innerText.replace(/\uFDFA/g,''))
            };
        }""")
        print(f"[{tag}] {m}")
        pg.screenshot(path=f"{OUT}/qa-r670-404-{tag}.png", full_page=(tag == "desktop"))
        pg.close()
    b.close()
print("QA navigateur OK — captures", OUT)
