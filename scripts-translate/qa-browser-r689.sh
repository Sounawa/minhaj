#!/bin/bash
# QA navigateur hadith-3es/pdf-mut23h2x-410 (leçon 21, R689) — desktop 1280 + mobile 390
set -x
cd /home/z/my-project
TS=$(date +%s)
mkdir -p tr-tmp/qa-crops-r689

for i in $(seq 1 10); do
  C=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "http://127.0.0.1:3000/")
  [ "$C" = "200" ] && break
  sleep 3
done
echo "PORTAIL $C"

curl -s -o /dev/null -w "warm api lesson -> %{http_code}\n" "http://127.0.0.1:3000/api/lessons/hadith-3es/pdf-mut23h2x-410" --max-time 60
sleep 2

# 1. Desktop 1280
agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/hadith-3es/pdf-mut23h2x-410" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 3000
agent-browser set viewport 1280 900
agent-browser wait 1500
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,110), badge: !!document.body.innerText.includes('Traduction savante'), lecon: (document.body.innerText.match(/Leçon\s*21\s*\/\s*29/)||document.body.innerText.match(/21\s*\/\s*29/)||[])[0], h2s: Array.from(document.querySelectorAll('h2')).length, nums: ['1240','1242','1243','1244','1245','1248','1260','1261','1266','1241','1262','1255'].filter(n=>document.body.innerText.includes(n)).length, key1: !!document.body.innerText.includes('six pauvres'), key2: !!document.body.innerText.includes('une brebis par poussin'), key3: !!document.body.innerText.includes('poignée de nourriture'), overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth})" 2>&1 | tail -2
agent-browser screenshot tr-tmp/qa-crops-r689/qa-r689-410-desktop.png 2>&1 | tail -1

# 2. Mobile 390
agent-browser set viewport 390 844
agent-browser wait 1500
agent-browser eval "JSON.stringify({overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth, scrollW: document.documentElement.scrollWidth, h1: !!document.querySelector('h1')})" 2>&1 | tail -2
agent-browser screenshot tr-tmp/qa-crops-r689/qa-r689-410-mobile.png 2>&1 | tail -1
agent-browser close 2>&1 | tail -1
