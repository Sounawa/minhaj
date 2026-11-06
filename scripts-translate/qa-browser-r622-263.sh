#!/bin/bash
# R622 — QA navigateur leçon uh2 pdf-mut23h2u-263 sur le portail (déjà en :3000, API 200 vérifiée)
# Méthode R621 : 1280/390, badge, h2/h3, overflow, console, captures pleine page + ratio non-blanc
set -u
cd /home/z/my-project
TS=$(date +%s)
TAG="r622-263"
OUT=/home/z/my-project/tr-tmp

agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/ulum-hadith-tanawi-2/pdf-mut23h2u-263" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2500
agent-browser set viewport 1280 900
agent-browser wait 1200
echo "--- DESKTOP 1280 ---"
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,120), badge: document.body.innerText.includes('Traduction savante'), h2: document.querySelectorAll('h2').length, h3: document.querySelectorAll('h3').length, innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth})"
agent-browser console 2>&1 | tail -4
agent-browser errors 2>&1 | tail -3
agent-browser screenshot --full "$OUT/qa-$TAG-1280-full.png" 2>&1 | tail -1

echo "--- MOBILE 390 ---"
agent-browser set viewport 390 844
agent-browser wait 1500
agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth})"
agent-browser screenshot --full "$OUT/qa-$TAG-390-full.png" 2>&1 | tail -1
agent-browser close 2>&1 | tail -1

python3 - <<'PY'
from PIL import Image
import os
for tag, path in [("1280", "/home/z/my-project/tr-tmp/qa-r622-263-1280-full.png"),
                  ("390", "/home/z/my-project/tr-tmp/qa-r622-263-390-full.png")]:
    if not os.path.exists(path):
        print(tag, "CAPTURE ABSENTE"); continue
    im = Image.open(path).convert("L")
    px = list(im.getdata())
    nonwhite = sum(1 for v in px if v < 245) / len(px)
    print(f"{tag}: {im.width}x{im.height} — non-blanc {nonwhite*100:.1f} %")
PY
echo "QA DONE $TAG"
