# -*- coding: utf-8 -*-
# R648 — QA navigateur fallback (serveur :3000 KO, méthode documentée R646/R640-bis) :
# rendu local du HTML livré via Chromium headless (playwright), captures 1280 + 390,
# stats DOM, vérification non-vidéité des captures.
from playwright.sync_api import sync_playwright
from PIL import Image
import os

HTML = "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-271-fr.html"
OUT = "/home/z/my-project/tr-tmp"
url = f"file://{HTML}"

with sync_playwright() as p:
    b = p.chromium.launch()
    for name, w, h in [("desktop", 1280, 900), ("mobile", 390, 844)]:
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.goto(url, wait_until="load")
        stats = pg.evaluate("""() => ({
            h1: document.querySelector('h1') ? document.querySelector('h1').textContent.trim().slice(0, 80) : '',
            h2: document.querySelectorAll('h2').length,
            h3: document.querySelectorAll('h3').length,
            p: document.querySelectorAll('p').length,
            li: document.querySelectorAll('li').length,
            strong: document.querySelectorAll('strong').length,
            chars: document.body.innerText.length,
            overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth
        })""")
        pg.screenshot(path=f"{OUT}/qa-r648-271-{name}.png", full_page=(name == "desktop"))
        pg.close()
        img = Image.open(f"{OUT}/qa-r648-271-{name}.png").convert("L")
        nonwhite = sum(1 for px in img.getdata() if px < 245) / (img.width * img.height)
        print(name, stats, f"non-blanc {nonwhite:.1%}")
    b.close()
