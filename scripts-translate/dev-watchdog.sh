#!/bin/bash
# Garde-fou dev :3000 — détecte node_modules cassé (balayage partiel : next/ peut
# manquer alors que .bin/next existe), réinstalle PROPREMENT, relance le serveur.
cd /home/z/my-project
HEALTHY() { [ -f node_modules/next/package.json ] && [ -f node_modules/@next/env/package.json ]; }
while true; do
  if ! curl -s -o /dev/null --max-time 8 http://localhost:3000/; then
    if ! HEALTHY; then
      rm -rf node_modules 2>/dev/null
      bun install --frozen-lockfile >/dev/null 2>&1
    fi
    if HEALTHY; then
      setsid nohup ./node_modules/.bin/next dev -p 3000 > dev.log 2>&1 < /dev/null &
      sleep 25
    fi
  fi
  sleep 15
done
