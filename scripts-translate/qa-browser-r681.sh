#!/bin/bash
# QA navigateur hadith-3es/pdf-mut23h2x-407 (leçon 18, R681) — desktop 1280 + mobile 390
# Portail : serveur standalone zone stable (R676), lecture directe de content/
set -x
cd /home/z/my-project
TS=$(date +%s)
mkdir -p tr-tmp/qa-crops-r681

for i in $(seq 1 10); do
  C=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "http://127.0.0.1:3000/")
  [ "$C" = "200" ] && break
  sleep 3
done
echo "PORTAIL $C"

curl -s -o /dev/null -w "warm api lesson -> %{http_code}\n" "http://127.0.0.1:3000/api/lessons/hadith-3es/pdf-mut23h2x-407" --max-time 60
sleep 2

# 1. Desktop 1280
agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/hadith-3es/pdf-mut23h2x-407" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 3000
agent-browser set viewport 1280 900
agent-browser wait 1500
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,120), badge: !!document.body.innerText.includes('Traduction savante'), lecon: (document.body.innerText.match(/Leçon\s*18\s*\/\s*29/)||document.body.innerText.match(/18\s*\/\s*29/)||[])[0], h2s: Array.from(document.querySelectorAll('h2')).length, nums: ['1121','1135','1122','1124','1125','1134','1136','1128','1129','1138','1139','1140'].filter(n=>document.body.innerText.includes(n)).length, verse: !!document.body.innerText.includes('mangez de ces bêtes'), tafath: !!document.body.innerText.includes('ilqāʾ at-tafath'), overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth})" 2>&1 | tail -2
agent-browser screenshot tr-tmp/qa-crops-r681/qa-r681-407-desktop.png 2>&1 | tail -1

# 2. Mobile 390
agent-browser set viewport 390 844
agent-browser wait 1500
agent-browser eval "JSON.stringify({overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth, scrollW: document.documentElement.scrollWidth, h1: !!document.querySelector('h1')})" 2>&1 | tail -2
agent-browser screenshot tr-tmp/qa-crops-r681/qa-r681-407-mobile.png 2>&1 | tail -1
agent-browser close 2>&1 | tail -1
