#!/bin/bash
# QA navigateur en UNE invocation (le sandbox reape les daemons entre appels)
# Usage: qa-browser-one.sh <bookId> <docId> <tag>
set -x
BOOK="$1"; DOC="$2"; TAG="$3"
cd /home/z/my-project
TS=$(date +%s)

NODE_OPTIONS="--max-old-space-size=614" setsid nohup npx next dev -p 3000 > dev-server.log 2>&1 < /dev/null &
sleep 9
curl -s -o /dev/null -w "warm / -> %{http_code}\n" "http://127.0.0.1:3000/" --max-time 90
sleep 2
curl -s -o /dev/null -w "warm api/books -> %{http_code}\n" "http://127.0.0.1:3000/api/books" --max-time 60
sleep 2
curl -s -o /dev/null -w "warm lesson -> %{http_code}\n" "http://127.0.0.1:3000/api/lessons/$BOOK/$DOC" --max-time 60
free -m | head -2 | tail -1

agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/$BOOK/$DOC" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2500
agent-browser set viewport 1280 900
agent-browser wait 1000
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,150), badge: !!document.body.innerText.includes('Traduction savante'), lecon: (document.body.innerText.match(/Leçon \d+ ?\/ ?31/)||[])[0], lecture: (document.body.innerText.match(/\d+ min(?:utes)? de lecture/)||[])[0], prog: (document.body.innerText.match(/\d+ ?%/)||[])[0], bilingue: !!document.querySelector('[lang=\"ar\"]')})"

agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth})"
agent-browser console 2>&1 | tail -6
agent-browser errors 2>&1 | tail -3
agent-browser screenshot "/home/z/my-project/qa-$TAG-$DOC-desktop.png" 2>&1 | tail -1

agent-browser set viewport 390 844
agent-browser wait 1200
agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth})"
agent-browser screenshot "/home/z/my-project/qa-$TAG-$DOC-mobile.png" 2>&1 | tail -1

agent-browser close 2>&1 | tail -1
echo "QA DONE $BOOK/$DOC"
