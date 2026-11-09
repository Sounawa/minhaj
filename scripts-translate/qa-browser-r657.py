# -*- coding: utf-8 -*-
# R657 — QA navigateur de la leçon livrée R657 uh2-276 (file:// 1280 + 390,
# stats DOM, non-vidéité) + acquittement du portail :3000 (best-effort).
from playwright.sync_api import sync_playwright
from PIL import Image

OUT = "/home/z/my-project/tr-tmp"

with sync_playwright() as p:
    b = p.chromium.launch()

    # 1) leçon 276 en file:// — desktop 1280 + mobile 390
    tag = "r657-276"
    url = "file:///home/z/my-project/tr-tmp/lesson-uh2-pdf-mut23h2u-276-fr.html"
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
        pg.screenshot(path=f"{OUT}/qa-{tag}-{name}.png", full_page=(name == "desktop"))
        pg.close()
        img = Image.open(f"{OUT}/qa-{tag}-{name}.png").convert("L")
        nonwhite = sum(1 for px in img.getdata() if px < 245) / (img.width * img.height)
        print(tag, name, stats, f"non-blanc {nonwhite:.1%}")

    # 2) acquittement portail :3000 — best-effort (peut être down, wipe node_modules)
    try:
        pg = b.new_page(viewport={"width": 1280, "height": 900})
        pg.goto("http://localhost:3000/", wait_until="networkidle", timeout=20000)
        ps = pg.evaluate("""() => ({
            title: document.title.slice(0, 80),
            chars: document.body.innerText.length,
            headings: document.querySelectorAll('h1,h2,h3').length
        })""")
        pg.screenshot(path=f"{OUT}/qa-r657-portail.png", full_page=False)
        pg.close()
        img = Image.open(f"{OUT}/qa-r657-portail.png").convert("L")
        nonwhite = sum(1 for px in img.getdata() if px < 245) / (img.width * img.height)
        print("portail-3000", ps, f"non-blanc {nonwhite:.1%}")
    except Exception as e:
        print("portail-3000 DOWN (documenté) :", type(e).__name__)
    b.close()
