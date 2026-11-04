#!/bin/bash
# Garde-fou dev :3000 v4 — R571 : le `rm -rf node_modules` de la v3 a détruit
# deux installations en cours (course de processus, balayages n°71-78 pendant
# les passes npm) ; l'effacement est INTERDIT : bun install est idempotent.
cd /home/z/my-project
LOG=tr-tmp/dev-watchdog.log
SWEEPS=0
HEALTHY() { [ -f node_modules/next/package.json ] && [ -f node_modules/@next/env/package.json ]; }
while true; do
  # v4.1 : timeout 25s + double échec avant pkill (les compilations Turbopack a froid
  # depassent 6s — l'ancien timeout tuait le serveur en pleine charge, cf. dev.log)
  if ! curl -s -o /dev/null --max-time 25 http://localhost:3000/; then
    sleep 5
    if ! curl -s -o /dev/null --max-time 25 http://localhost:3000/; then
    pkill -f "next dev -p 3000" 2>/dev/null; pkill -f "next-server" 2>/dev/null; sleep 2
    fi
  fi
  if false; then
    for t in 1 2 3; do
      if ! HEALTHY; then
        SWEEPS=$((SWEEPS+1)); echo "$(date -u +%H:%M:%SZ) balayage n°$SWEEPS — réinstallation (v4 sans effacement)" >> $LOG
        mkdir -p tr-tmp
        # v4.2 : purge des verrous orphelins (> 10 min = run tue en plein install)
        if [ -d tr-tmp/watchdog.lock ]; then
          AGE=$(( $(date +%s) - $(stat -c %Y tr-tmp/watchdog.lock 2>/dev/null || date +%s) ))
          [ "$AGE" -gt 600 ] && rmdir tr-tmp/watchdog.lock 2>/dev/null && echo "$(date -u +%H:%M:%SZ) verrou orphelin purgé (${AGE}s)" >> $LOG
        fi
        if mkdir tr-tmp/watchdog.lock 2>/dev/null; then
          bun install --frozen-lockfile >> $LOG 2>&1
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
