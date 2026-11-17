#!/usr/bin/env python3
"""Captures QA R716 v2 : capture par élément (section commentaire complète)."""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1280, 'height': 950})
    pg.goto('file:///home/z/my-project/minhaj-repo/site/livres/hadith-3es/pdf-mut23h2x-413.html',
            wait_until='load')
    pg.wait_for_timeout(600)
    pg.locator('#commentaire').screenshot(path='/tmp/qa-r716-lecon.png')
    pg.goto('file:///home/z/my-project/minhaj-repo/site/index.html', wait_until='load')
    pg.evaluate("document.getElementById('cycle-commentaires').open=true")
    pg.wait_for_timeout(500)
    pg.locator('#cycle-commentaires').screenshot(path='/tmp/qa-r716-accueil.png')
    b.close()
print('captures v2 OK')
