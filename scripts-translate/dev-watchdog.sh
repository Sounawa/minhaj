#!/bin/bash
# Garde-fou dev :3000 v4 — R571 : le `rm -rf node_modules` de la v3 a détruit
# deux installations en cours (course de processus, balayages n°71-78 pendant
# les passes npm) ; l'effacement est INTERDIT : bun install est idempotent.
cd /home/z/my-project
LOG=tr-tmp/dev-watchdog.log
SWEEPS=0
HEALTHY() { [ -f node_modules/next/package.json ] && [ -f node_modules/@next/env/package.json ]; }
while true; do
  if ! curl -s -o /dev/null --max-time 6 http://localhost:3000/; then
    pkill -f "next dev -p 3000" 2>/dev/null; pkill -f "next-server" 2>/dev/null; sleep 2
    for t in 1 2 3; do
      if ! HEALTHY; then
        SWEEPS=$((SWEEPS+1)); echo "$(date -u +%H:%M:%SZ) balayage n°$SWEEPS — réinstallation (v4 sans effacement)" >> $LOG
        mkdir -p tr-tmp
        if mkdir tr-tmp/watchdog.lock 2>/dev/null; then
          bun install --frozen-lockfile >/dev/null 2>&1
          rmdir tr-tmp/watchdog.lock 2>/dev/null
        fi
      fi
      if HEALTHY; then
        setsid nohup ./node_modules/.bin/next dev -p 3000 > dev.log 2>&1 < /dev/null &
        for w in 1 2 3 4 5 6 7 8; do sleep 5; curl -s -o /dev/null --max-time 5 http://localhost:3000/ && break; done
        curl -s -o /dev/null --max-time 5 http://localhost:3000/ && break
      fi
    done
  fi
  sleep 5
done
