#!/bin/bash
# R592 — serveur éphémère + QA navigateur, boucle jusqu'à verte (reaper hostile)
for i in 1 2 3 4 5; do
  echo "=== QA-ESSAI $i $(date -u +%H:%M:%SZ) ==="
  pkill -f "uh1-stand-r592/server.js" 2>/dev/null
  sleep 1
  cd /home/z/uh1-stand-r592
  DATABASE_URL="file:/home/z/my-project/db/custom.db" NODE_ENV=production setsid nohup bun server.js > server.log 2>&1 &
  ok=""
  for k in $(seq 1 15); do
    sleep 1
    code=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3000/ 2>/dev/null)
    [ "$code" = "200" ] && { ok=1; break; }
  done
  [ -z "$ok" ] && { echo "server KO essai $i"; continue; }
  echo "server UP"
  bash /home/z/my-project/tr-tmp/qa-browser-r592-pdf126.sh > /home/z/qa-r592-out.log 2>&1
  if grep -q "Le hadith insolite" /home/z/qa-r592-out.log; then
    echo "QA_VERTE_ESSAI_$i"
    grep -E '"\{' /home/z/qa-r592-out.log
    exit 0
  fi
  echo "QA rate essai $i:"
  grep -E '"\{' /home/z/qa-r592-out.log | head -2
done
echo "ECHEC_QA_5_ESSAIS"
exit 1
