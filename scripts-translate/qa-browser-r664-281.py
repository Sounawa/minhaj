# -*- coding: utf-8 -*-
# R664 — QA navigateur leçon uh2-281 (tarāǧim al-aʿlām, p.132-134) : rendu
# file:// via Chromium headless (playwright), captures 1280 + 390, stats DOM,
# 0 overflow exigé, captures non vides (patron qa-browser-r662).
from playwright.sync_api import sync_playwright
from PIL import Image
import os

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-281-fr.html"
OUT = "/home/z/my-project/tr-tmp/qa-crops-r664"
os.makedirs(OUT, exist_ok=True)
url = f"file://{HTML}"

with sync_playwright() as p:
    b = p.chromium.launch()
    for name, w, h in [("desktop", 1280, 900), ("mobile", 390, 844)]:
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.goto(url, wait_until="load")
        stats = pg.evaluate("""() => ({
            h1: document.querySelector('h1') ? document.querySelector('h1').textContent.trim().slice(0, 70) : '',
            h2: document.querySelectorAll('h2').length,
            p: document.querySelectorAll('p').length,
            li: document.querySelectorAll('li').length,
            strong: document.querySelectorAll('strong').length,
            chars: document.body.innerText.length,
            overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth
        })""")
        pg.screenshot(path=f"{OUT}/qa-r664-281-{name}.png", full_page=(name == "desktop"))
        pg.close()
        print(name, stats)
    b.close()

for name in ["desktop", "mobile"]:
    im = Image.open(f"{OUT}/qa-r664-281-{name}.png")
    px = im.convert("L")
    hist = px.histogram()
    nonwhite = sum(hist[:240]) / (im.size[0] * im.size[1])
    print(f"{name}: {im.size} non-blanc {nonwhite:.1%} — {'NON VIDE OK' if im.size[0] > 0 and nonwhite > 0.02 else 'SUSPECT'}")
