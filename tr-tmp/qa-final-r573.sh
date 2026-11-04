#!/bin/bash
# QA finale pdf-29 — TOUT en une invocation : watchdog + serveur + préchauffe API longue + attente active du contenu
cd /home/z/my-project
TS=$(date +%s)

# 1) watchdog vivant ? sinon relance
pgrep -f dev-watchdog.sh >/dev/null || (setsid nohup bash scripts-translate/dev-watchdog.sh > tr-tmp/watchdog-start.log 2>&1 < /dev/null &)

# 2) serveur :3000 up ?
for i in $(seq 1 24); do
  C=$(curl -s -o /dev/null -w "%{http_code}" --max-time 8 http://127.0.0.1:3000/ 2>/dev/null)
  [ "$C" = "200" ] && break; sleep 5
done
echo "serveur /: $C (après $((i*5))s)"

# 3) préchauffe API leçon (compilation froide possible — 300 s)
A=$(curl -s -o /home/z/my-project/tr-tmp/api-pdf29-test.json -w "%{http_code}" --max-time 300 "http://127.0.0.1:3000/api/lessons/hadith-2es/pdf-29")
echo "api leçon: $A"
python3 -c "
import json
try:
    d = json.load(open('tr-tmp/api-pdf29-test.json'))
    print('  docId:', d.get('docId'), '| htmlFr len:', len(d.get('htmlFr','')), '| titleFr:', str(d.get('titleFr'))[:60])
except Exception as e:
    print('  parse FAIL:', e)"

# 4) QA navigateur — attente ACTIVE du h1
agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/hadith-2es/pdf-29" 2>&1 | tail -1
agent-browser set viewport 1280 900
for t in $(seq 1 24); do
  H=$(agent-browser eval "document.querySelector('h1') ? document.querySelector('h1').textContent.length : 0" 2>/dev/null | tr -d '" ')
  [ "${H:-0}" -gt 10 ] 2>/dev/null && break
  sleep 5
done
echo "h1 présent après ~$((t*5))s (len=${H:-0})"
agent-browser wait 1500
echo "=== DESKTOP ==="
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,110), badge: !!document.body.innerText.includes('Traduction savante'), lecon: (document.body.innerText.match(/Le\u00e7on \d+ ?\/ ?31/)||[])[0], crochets: [862,864,887,865,863,866].map(n=>document.body.innerText.includes('n\u00b0 '+n)), zarqani: !!document.body.innerText.includes('meilleure des qualit\u00e9s du je\u00fbneur'), overflow: document.body.scrollWidth > window.innerWidth})"
agent-browser errors 2>&1 | tail -3
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r573-pdf29-desktop.png" 2>&1 | tail -1
agent-browser set viewport 390 844
agent-browser wait 1500
echo "=== MOBILE ==="
agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth, h1: !!document.querySelector('h1')})"
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r573-pdf29-mobile.png" 2>&1 | tail -1
agent-browser close 2>&1 | tail -1
echo "final: $(curl -s -o /dev/null -w "%{http_code}" --max-time 8 http://127.0.0.1:3000/)"
echo "QA DONE"
