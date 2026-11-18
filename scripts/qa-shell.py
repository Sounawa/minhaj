#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R501-503 — QA navigateur de repli : coquille statique fidèle au rendu leçon.
Le dev server (Turbopack: panic worker PostCSS ; webpack: mort au premier hit)
est inopérant après les rebuilds sandbox — obstacle d'environnement documenté.
Usage : python3 scripts/qa-shell.py <745|746|747>"""
import sys

n = sys.argv[1]
doc = {"745": ("pdf-mut23h3c-745", "leçon 7", "pages 50-57"),
       "746": ("pdf-mut23h3c-746", "leçon 8", "pages 58-64"),
       "747": ("pdf-mut23h3c-747", "leçon 9", "pages 65-72")}[n]

html = open(f"scripts-translate/tr-tmp/{doc[0]}.html", encoding="utf-8").read()

CSS = """
:root { --ink:#1d1c19; --paper:#faf7f0; --accent:#8a6d3b; --rule:#d8cfc0; }
* { box-sizing: border-box; }
body { margin:0; background:var(--paper); color:var(--ink);
  font-family: Georgia, 'Noto Serif', serif; font-size:17px; line-height:1.72; }
.page { max-width:768px; margin:0 auto; padding:28px 22px 60px; }
h1 { font-size:1.5rem; line-height:1.35; margin:.2em 0 1em; color:#2b2114; }
h2 { font-size:1.22rem; margin:1.6em 0 .5em; color:var(--accent);
  border-bottom:1px solid var(--rule); padding-bottom:.25em; }
h3 { font-size:1.05rem; margin:1.3em 0 .4em; color:#5a4632; }
p { margin:.55em 0; text-align:justify; hyphens:auto; }
ol { margin:.5em 0 .9em 1.4em; padding:0; }
li { margin:.32em 0; }
dl.lesson-meta { border:1px solid var(--rule); border-radius:10px;
  background:#f3ecdd; padding:12px 16px; margin:0 0 1.4em; }
dl.lesson-meta dt { font-variant:small-caps; letter-spacing:.06em;
  color:var(--accent); font-weight:700; }
dl.lesson-meta dd { margin:.4em 0 0; font-size:.94rem; line-height:1.6; text-align:justify; }
footer { margin-top:2.4em; padding-top:.9em; border-top:1px solid var(--rule);
  font-size:.85rem; color:#6b5b45; }
.badge { display:inline-block; background:var(--accent); color:#fff;
  border-radius:999px; padding:.15em .8em; font-size:.8rem; }
"""

page = f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>QA {n} — Sourate al-Kahf — {doc[1]}</title>
<style>{CSS}</style></head>
<body><div class="page" id="reader">
{html}
<footer><span class="badge">Traduction savante</span> — Minhāj · Tafsīr de troisième année secondaire · {doc[1]} ({doc[2]}) · production 24/7</footer>
</div></body></html>"""

open(f"tr-tmp/qa-{n}-preview.html", "w", encoding="utf-8").write(page)
print(f"preview {n} écrit:", len(page), "car")
