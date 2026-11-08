# -*- coding: utf-8 -*-
# R653 — QA navigateur via le portail :3000 remonté (acquittement rétroéventuel R651
# + QA de la leçon livrée R653 uh2-272), captures 1280 + 390, stats DOM, non-vidéité.
from playwright.sync_api import sync_playwright
from PIL import Image

OUT = "/home/z/my-project/tr-tmp"

with sync_playwright() as p:
    b = p.chromium.launch()
    for tag, path in [
        ("r651-398", "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-398-fr.html"),
        ("r653-272", "/home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-272-fr.html"),
    ]:
        url = f"file://{path}"
        for name, w, h in [("desktop", 1280, 900), ("mobile", 390, 844)]:
            pg = b.new_page(viewport={"width": w, "height": h})
            pg.goto(url, wait_until="load")
            stats = pg.evaluate("""() => ({
                h1: document.querySelector('h1') ? document.querySelector('h1').textContent.trim().slice(0, 70) : '',
                h2: document.querySelectorAll('h2').length,
                h3: document.querySelectorAll('h3').length,
                p: document.querySelectorAll('p').length,
                li: document.querySelectorAll('li').length,
                strong: document.querySelectorAll('strong').length,
                chars: document.body.innerText.length,
                overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth
            })""")
            pg.screenshot(path=f"{OUT}/qa-r653-{tag}-{name}.png", full_page=(name == "desktop"))
            pg.close()
            img = Image.open(f"{OUT}/qa-r653-{tag}-{name}.png").convert("L")
            nonwhite = sum(1 for px in img.getdata() if px < 245) / (img.width * img.height)
            print(tag, name, stats, f"non-blanc {nonwhite:.1%}")
    b.close()
