#!/bin/bash
# QA navigateur hadith-2es/pdf-21 (leçon 16, R565) en UNE invocation
# (le sandbox reaped les daemons entre appels — schéma qa-browser-pdf17.sh)
set -x
cd /home/z/my-project
TS=$(date +%s)

# 0. Serveur vivant (relance en session si besoin)
if ! curl -s -o /dev/null --max-time 5 "http://127.0.0.1:3000/"; then
  for i in 1 2 3; do bun install >/dev/null 2>&1; ls node_modules/.bin/next >/dev/null 2>&1 && break; done
  (setsid nohup ./node_modules/.bin/next dev -p 3000 > tr-tmp/dev.log 2>&1 < /dev/null &)
fi
for i in $(seq 1 30); do
  C=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "http://127.0.0.1:3000/")
  [ "$C" = "200" ] && break
  sleep 6
done
echo "PORTAIL $C"

curl -s -o /dev/null -w "warm / -> %{http_code}\n" "http://127.0.0.1:3000/" --max-time 60
curl -s -o /dev/null -w "warm api/books -> %{http_code}\n" "http://127.0.0.1:3000/api/books" --max-time 60
curl -s -o /dev/null -w "warm lesson -> %{http_code}\n" "http://127.0.0.1:3000/api/lessons/hadith-2es/pdf-21" --max-time 60

# 1. Browser QA — desktop 1280 d'abord
agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/hadith-2es/pdf-21" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2500
agent-browser set viewport 1280 900
agent-browser wait 1200
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,140), badge: !!document.body.innerText.includes('Traduction savante'), lecon: (document.body.innerText.match(/Leçon \d+\/31/)||[])[0], h2count: document.querySelectorAll('h2').length, renvois: ['728','745','747','727','733','734','735','746','736','739','737','729','743'].map(n=>document.body.innerText.includes(n)), verse: !!document.body.innerText.includes('treillagés et non treillagés'), overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth, console: (window.__nextErr||null)})" 2>&1 | tail -3
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r565-pdf21-desktop.png" 2>&1 | tail -1

# 2. Browser QA — mobile 390
agent-browser set viewport 390 844
agent-browser wait 1200
agent-browser eval "JSON.stringify({overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth, h1ok: !!document.querySelector('h1')})" 2>&1 | tail -2
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r565-pdf21-mobile.png" 2>&1 | tail -1
echo "QA DONE"
