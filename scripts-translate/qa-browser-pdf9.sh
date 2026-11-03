#!/bin/bash
# QA navigateur hadith-2es/pdf-9 (leçon 7, R541) en UNE invocation
set -x
cd /home/z/my-project
TS=$(date +%s)

# 0. Serveur vivant + préchauffe des routes
curl -s -o /dev/null -w "warm / -> %{http_code}\n" "http://127.0.0.1:3000/" --max-time 90
curl -s -o /dev/null -w "warm api/books -> %{http_code}\n" "http://127.0.0.1:3000/api/books" --max-time 60
curl -s -o /dev/null -w "warm lesson -> %{http_code}\n" "http://127.0.0.1:3000/api/lessons/hadith-2es/pdf-9" --max-time 60

# 1. Browser QA — desktop 1280
agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/hadith-2es/pdf-9" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2500
agent-browser set viewport 1280 900
agent-browser wait 1000
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,140), badge: !!document.body.innerText.includes('Traduction savante'), lecon: (document.body.innerText.match(/Leçon \d+\/31/)||[])[0], bilingue: !!document.querySelector('[lang=\"ar\"]'), h2s: Array.from(document.querySelectorAll('h2')).map(h=>h.textContent.trim()).slice(0,12), overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth, err: (window.__nextErr||null)})" 2>&1 | tail -3
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r544-hadith2-pdf9-desktop.png" 2>&1 | tail -1

# 2. Browser QA — mobile 390
agent-browser set viewport 390 844
agent-browser wait 1500
agent-browser eval "JSON.stringify({overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth, bodyW: document.documentElement.clientWidth, scrollW: document.documentElement.scrollWidth})" 2>&1 | tail -2
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r544-hadith2-pdf9-mobile.png" 2>&1 | tail -1
