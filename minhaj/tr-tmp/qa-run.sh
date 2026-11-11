#!/bin/bash
# QA pdf-29 — remonte le serveur SI nécessaire puis QA, tout en une invocation
cd /home/z/my-project
TS=$(date +%s)
pgrep -f dev-watchdog.sh >/dev/null || (setsid nohup bash scripts-translate/dev-watchdog.sh > tr-tmp/watchdog-start.log 2>&1 < /dev/null &)
C=$(curl -s -o /dev/null -w "%{http_code}" --max-time 8 http://127.0.0.1:3000/)
if [ "$C" != "200" ]; then
  (setsid nohup node_modules/.bin/next dev -p 3000 > dev.log 2>&1 < /dev/null &)
fi
for i in $(seq 1 24); do sleep 5; C=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 http://127.0.0.1:3000/); [ "$C" = "200" ] && break; done
echo "serveur: $C"
A=$(curl -s -o /dev/null -w "%{http_code}" --max-time 120 "http://127.0.0.1:3000/api/lessons/hadith-2es/pdf-29")
echo "api: $A"
agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/hadith-2es/pdf-29" 2>&1 | tail -1
agent-browser set viewport 1280 900
agent-browser wait --load networkidle 2>&1 | tail -1
for t in $(seq 1 20); do
  H=$(agent-browser eval "document.querySelector('h1') ? document.querySelector('h1').textContent.length : 0" 2>/dev/null | tr -d '" ')
  [ "${H:-0}" -gt 30 ] 2>/dev/null && break
  sleep 5
done
echo "h1 après ~$((t*5))s (len=${H:-0})"
agent-browser wait 1500
echo "=== DESKTOP 1280 ==="
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,110), badge: !!document.body.innerText.includes('Traduction savante'), lecon: (document.body.innerText.match(/Le\u00e7on \d+ ?\/ ?31/)||[])[0], crochets: [862,864,887,865,863,866].map(n=>document.body.innerText.includes('n\u00b0 '+n)), zarqani: !!document.body.innerText.includes('meilleure des qualit\u00e9s du je\u00fbneur'), overflow: document.body.scrollWidth > window.innerWidth})"
agent-browser errors 2>&1 | tail -3
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r573-pdf29-desktop.png" 2>&1 | tail -1
agent-browser set viewport 390 844
agent-browser wait 1500
echo "=== MOBILE 390 ==="
agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth, h1len: document.querySelector('h1')?.textContent?.length})"
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r573-pdf29-mobile.png" 2>&1 | tail -1
agent-browser close 2>&1 | tail -1
echo "final: $(curl -s -o /dev/null -w "%{http_code}" --max-time 8 http://127.0.0.1:3000/)"
echo "QA DONE"
