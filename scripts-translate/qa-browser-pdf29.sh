#!/bin/bash
# QA navigateur pdf-29 en UNE invocation (le sandbox reape les daemons entre appels)
# Serveur dev:3000 déjà vivant (relancé en début de passe) — pas de redémarrage.
set -x
cd /home/z/my-project
TS=$(date +%s)

# serveur vivant ? sinon relance (node_modules parfois balayé entre invocations)
if [ ! -x node_modules/.bin/next ]; then timeout 400 bun install >/tmp/qa-install.log 2>&1; fi
C=$(curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:3000/" --max-time 15 || true)
if [ "$C" != "200" ]; then
  (setsid nohup node_modules/.bin/next dev -p 3000 > dev.log 2>&1 < /dev/null &)
  for i in 1 2 3 4 5 6; do sleep 8; C=$(curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:3000/" --max-time 20); [ "$C" = "200" ] && break; done
fi
echo "serveur: $C"

curl -s -o /dev/null -w "warm / -> %{http_code}\n" "http://127.0.0.1:3000/" --max-time 90
curl -s -o /dev/null -w "warm lesson -> %{http_code}\n" "http://127.0.0.1:3000/api/lessons/hadith-2es/pdf-29" --max-time 60

agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/hadith-2es/pdf-29" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2500
agent-browser set viewport 1280 900
agent-browser wait 1000
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,150), badge: !!document.body.innerText.includes('Traduction savante'), lecon: (document.body.innerText.match(/Leçon \d+ ?\/ ?31/)||[])[0], crochets: [862,864,887,865,863,866].map(n=>document.body.innerText.includes('n° '+n)), zarqani: !!document.body.innerText.includes('La meilleure des qualités du jeûneur'), bilingue: !!document.querySelector('[lang=\"ar\"]')})"

agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth})"
agent-browser console 2>&1 | tail -6
agent-browser errors 2>&1 | tail -3
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r573-pdf29-desktop.png" 2>&1 | tail -1

agent-browser set viewport 390 844
agent-browser wait 1200
agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth})"
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r573-pdf29-mobile.png" 2>&1 | tail -1

agent-browser close 2>&1 | tail -1
echo "QA DONE hadith-2es/pdf-29"
