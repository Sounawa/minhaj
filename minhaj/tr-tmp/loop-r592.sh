#!/bin/bash
# R592 — boucle de reconstruction atomique (piège recyclage en tempête)
# installe + build + start + vérif HTTP 200 ; sauvegarde externe du standalone.
cd /home/z/my-project
LOG=tr-logs/loop-r592.log
: > "$LOG"
for i in 1 2 3 4 5 6; do
  echo "=== TENTATIVE $i $(date -u +%H:%M:%SZ) ===" >> "$LOG"
  bun install >> "$LOG" 2>&1 || { sleep 15; continue; }
  node_modules/.bin/next build >> "$LOG" 2>&1 || { sleep 15; continue; }
  cp -r .next/static .next/standalone/.next/ >> "$LOG" 2>&1
  cp -r public .next/standalone/ >> "$LOG" 2>&1
  pkill -f "standalone/server.js" 2>/dev/null; sleep 1
  NODE_ENV=production bun .next/standalone/server.js > server.log 2>&1 &
  for k in $(seq 1 30); do
    sleep 2
    code=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000/ 2>/dev/null)
    if [ "$code" = "200" ]; then
      echo "HTTP200_TENTATIVE_$i $(date -u +%H:%M:%SZ)" >> "$LOG"
      cp -a .next/standalone /home/z/uh1-stand-r592 2>/dev/null
      echo "STANDALONE_SAUVE /home/z/uh1-stand-r592" >> "$LOG"
      exit 0
    fi
  done
  sleep 10
done
echo "ECHEC_BOUCLE $(date -u +%H:%M:%SZ)" >> "$LOG"
exit 1
