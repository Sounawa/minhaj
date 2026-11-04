#!/bin/bash
# QA finale pdf-29 sur le VRAI site :3000 — TOUT en une invocation (sandbox fauche les daemons)
cd /home/z/my-project
TS=$(date +%s)
if ! pgrep -f "next dev" >/dev/null; then
  (setsid nohup node_modules/.bin/next dev -p 3000 > dev.log 2>&1 < /dev/null &)
  for i in $(seq 1 12); do sleep 5; C=$(curl -s -o /dev/null -w "%{http_code}" --max-time 15 http://127.0.0.1:3000/); [ "$C" = "200" ] && break; done
fi
C=$(curl -s -o /dev/null -w "%{http_code}" --max-time 20 http://127.0.0.1:3000/)
echo "serveur: $C"
curl -s -o /dev/null --max-time 90 "http://127.0.0.1:3000/?nc=$TS"
curl -s -o /dev/null --max-time 60 "http://127.0.0.1:3000/api/lessons/hadith-2es/pdf-29"

agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/hadith-2es/pdf-29" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2500
agent-browser set viewport 1280 900
agent-browser wait 1200
echo "=== DESKTOP CHECKS ==="
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,120), badge: !!document.body.innerText.includes('Traduction savante'), lecon: (document.body.innerText.match(/Le\u00e7on \d+ ?\/ ?31/)||[])[0], crochets: [862,864,887,865,863,866].map(n=>document.body.innerText.includes('n\u00b0 '+n)), zarqani: !!document.body.innerText.includes('meilleure des qualit\u00e9s du je\u00fbneur'), overflow: document.body.scrollWidth > window.innerWidth})"
agent-browser eval "JSON.stringify({errors: (window.__nextErrors||[]).length})"
agent-browser console 2>&1 | tail -4
agent-browser errors 2>&1 | tail -3
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r573-pdf29-desktop.png" 2>&1 | tail -1
agent-browser set viewport 390 844
agent-browser wait 1500
echo "=== MOBILE CHECKS ==="
agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth})"
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r573-pdf29-mobile.png" 2>&1 | tail -1
agent-browser close 2>&1 | tail -1
echo "=== SERVEUR TOUJOURS VIVANT ? ==="
curl -s -o /dev/null -w "final: %{http_code}\n" --max-time 15 http://127.0.0.1:3000/
pgrep -f "next dev" | head -1
echo "QA DONE pdf-29 sur :3000"
