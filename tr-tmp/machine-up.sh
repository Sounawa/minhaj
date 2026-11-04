#!/bin/bash
# Remontée machine complète en une invocation — disque assaini (4 Go libres), plus de balayages attendus
cd /home/z/my-project
echo "=== 1. bun install ==="
timeout 300 bun install --frozen-lockfile 2>&1 | tail -2
echo "=== 2. watchdog v4.2 ==="
pgrep -f dev-watchdog.sh >/dev/null || (setsid nohup bash scripts-translate/dev-watchdog.sh > tr-tmp/watchdog-start.log 2>&1 < /dev/null &)
sleep 1; pgrep -f dev-watchdog.sh | head -1
echo "=== 3. next dev ==="
if ! curl -s -o /dev/null --max-time 8 http://127.0.0.1:3000/; then
  (setsid nohup node_modules/.bin/next dev -p 3000 > dev.log 2>&1 < /dev/null &)
fi
for i in $(seq 1 20); do sleep 5; C=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 http://127.0.0.1:3000/); [ "$C" = "200" ] && break; done
echo "serveur: $C"
echo "=== 4. préchauffe API (compilation froide) ==="
A=$(curl -s -o tr-tmp/api-pdf29-test.json -w "%{http_code}" --max-time 300 "http://127.0.0.1:3000/api/lessons/hadith-2es/pdf-29")
echo "api leçon: $A"
python3 -c "
import json
d = json.load(open('tr-tmp/api-pdf29-test.json'))
print('  docId:', d.get('docId'), '| htmlFr len:', len(d.get('htmlFr','')), '| titleFr:', str(d.get('titleFr'))[:60])" 2>&1
echo "MACHINE UP"
