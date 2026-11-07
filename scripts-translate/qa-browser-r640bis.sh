#!/bin/bash
# QA navigateur 1280/390 — leçons 394 et 395 hadith-3es (passe R640-bis, tick 11:07)
# Captures : tr-tmp/qa-r640bis-<doc>-{desktop,mobile}.png
set -u
OUT=/home/z/my-project/tr-tmp
qa_one () {
  local DOC="$1"
  local URL="http://localhost:3000/#/livre/hadith-3es/pdf-mut23h2x-$DOC"
  echo "=== QA pdf-mut23h2x-$DOC ==="
  agent-browser set viewport 1280 900
  agent-browser open "$URL" || { echo "OPEN KO $DOC"; return 1; }
  agent-browser wait --load networkidle --timeout 20000 || true
  sleep 2
  echo "-- DOM desktop --"
  agent-browser eval "JSON.stringify({h1:document.querySelector('h1')?.textContent?.slice(0,90)||null, meta:!!document.querySelector('.lesson-meta, dl'), h2:document.querySelectorAll('h2').length, h3:document.querySelectorAll('h3').length, p:document.querySelectorAll('p').length, bodyChars:document.body.innerText.length})"
  echo "-- erreurs console --"
  agent-browser errors | tail -5
  agent-browser screenshot "$OUT/qa-r640bis-$DOC-desktop.png" || echo "capture desktop KO"
  echo "-- mobile 390 --"
  agent-browser set viewport 390 844
  agent-browser reload || true
  agent-browser wait --load networkidle --timeout 20000 || true
  sleep 2
  agent-browser eval "JSON.stringify({h1:document.querySelector('h1')?.textContent?.slice(0,90)||null, h2:document.querySelectorAll('h2').length, p:document.querySelectorAll('p').length, bodyChars:document.body.innerText.length, hOverflow:(document.documentElement.scrollWidth>window.innerWidth+2)})"
  agent-browser screenshot "$OUT/qa-r640bis-$DOC-mobile.png" || echo "capture mobile KO"
}
qa_one 394
qa_one 395
agent-browser close || true
echo "=== FIN QA ==="
