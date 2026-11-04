#!/bin/bash
# QA navigateur hadith-2es/pdf-26 (leçon 25, les règles du jeûne (3), R571)
set -x
cd /home/z/my-project
TS=$(date +%s)

if ! curl -s -o /dev/null --max-time 5 "http://127.0.0.1:3000/"; then
  for i in 1 2 3; do bun install >/dev/null 2>&1; ls node_modules/.bin/next >/dev/null 2>&1 && break; done
  (setsid nohup ./node_modules/.bin/next dev -p 3000 > dev.log 2>&1 < /dev/null &)
fi
for i in $(seq 1 30); do
  C=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "http://127.0.0.1:3000/")
  [ "$C" = "200" ] && break
  sleep 6
done
echo "PORTAIL $C"

curl -s -o /dev/null -w "warm / -> %{http_code}\n" "http://127.0.0.1:3000/" --max-time 60
curl -s -o /dev/null -w "warm api/lesson -> %{http_code}\n" "http://127.0.0.1:3000/api/lessons/hadith-2es/pdf-26" --max-time 60

# 1. desktop 1280
agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/hadith-2es/pdf-26" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2500
agent-browser set viewport 1280 900
agent-browser wait 1200
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,120), badge: !!document.body.innerText.includes('Traduction savante'), lecon: (document.body.innerText.match(/Leçon \d+\/31/)||[])[0], h2count: document.querySelectorAll('h2').length, renvois: ['818','819','821','822','824','825','826'].map(n=>document.body.innerText.includes(n)), muaw: !!document.body.innerText.includes('où sont vos savants'), aicha: !!document.body.innerText.includes('Qui veut le jeûne'), tamr: !!document.body.innerText.includes('hotte'), overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth})" 2>&1 | tail -3
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r571-pdf26-desktop.png" 2>&1 | tail -1

# 2. mobile 390
agent-browser set viewport 390 844
agent-browser wait 1200
agent-browser eval "JSON.stringify({overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth, h1ok: !!document.querySelector('h1'), err: (window.__nextErr||null)})" 2>&1 | tail -2
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r571-pdf26-mobile.png" 2>&1 | tail -1
echo "QA DONE"
