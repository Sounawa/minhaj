#!/bin/bash
# QA navigateur 13124 en UNE invocation (le sandbox reaped les daemons entre appels)
set -x
cd /home/z/my-project
TS=$(date +%s)

# 1. Serveur (dans l'appel, reaped à la fin)
NODE_OPTIONS="--max-old-space-size=614" setsid nohup npx next dev -p 3000 > dev-server.log 2>&1 < /dev/null &
sleep 9

# 2. Préchauffe des routes
curl -s -o /dev/null -w "warm / -> %{http_code}\n" "http://127.0.0.1:3000/" --max-time 90
sleep 2
curl -s -o /dev/null -w "warm api/books -> %{http_code}\n" "http://127.0.0.1:3000/api/books" --max-time 60
sleep 2
curl -s -o /dev/null -w "warm lesson -> %{http_code}\n" "http://127.0.0.1:3000/api/lessons/hadith-tanawi-1/13124" --max-time 60
free -m | head -2 | tail -1

# 3. Browser QA — desktop
agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/hadith-tanawi-1/13124" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2500
agent-browser set viewport 1280 900
agent-browser wait 1000
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,150), badge: !!document.body.innerText.includes('Traduction savante'), lecon: (document.body.innerText.match(/Leçon \d+\/31/)||[])[0], lecture: (document.body.innerText.match(/\d+ min(?:utes)? de lecture/)||[])[0], prog: (document.body.innerText.match(/\d+ ?%/)||[])[0], bilingue: !!document.body.innerText.match(/عدة المتوفى/) || !!document.querySelector('[lang=\"ar\"]'), h2s: Array.from(document.querySelectorAll('h2')).map(h=>h.textContent.trim()).slice(0,12)})"

# overflow desktop
agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth})"

# console + erreurs
agent-browser console 2>&1 | tail -8
agent-browser errors 2>&1 | tail -4

# capture desktop
agent-browser screenshot "/home/z/my-project/qa-r236-13124-desktop.png" 2>&1 | tail -1

# 4. Browser QA — mobile
agent-browser set viewport 390 844
agent-browser wait 1200
agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth})"
agent-browser screenshot "/home/z/my-project/qa-r236-13124-mobile.png" 2>&1 | tail -1

agent-browser close 2>&1 | tail -1
free -m | head -2 | tail -1
echo "QA SCRIPT DONE"
