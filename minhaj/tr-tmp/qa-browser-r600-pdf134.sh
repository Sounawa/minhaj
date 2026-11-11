#!/bin/bash
# R600 — QA navigateur pdf-mut23h2q-134 (dev server DÉJÀ ACTIF — ne pas relancer)
set -x
TS=$(date +%s)
cd /home/z/my-project

curl -s "http://127.0.0.1:3000/api/lessons/ulum-hadith-tanawi-1/pdf-mut23h2q-134" | head -c 220
echo

agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/ulum-hadith-tanawi-1/pdf-mut23h2q-134" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2500
agent-browser set viewport 1280 900
agent-browser wait 1200
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,120), badge: (document.body.innerText.match(/Leçon \d+ ?\/ ?\d+/)||[])[0], mudabbaj: document.body.innerText.includes('mudabbaǧ'), mudbaj: document.body.innerText.includes('mudbaǧ'), qaribayn: document.body.innerText.includes('aḥadu l-qarībayn'), wafra: document.body.innerText.includes('ka-l-wafra'), musalsalat: document.body.innerText.includes('al-Musalsalāt'), sulayman: document.body.innerText.includes('Sulaymān at-Taymī'), layth: document.body.innerText.includes('Yazīd ibn al-Hād'), muttafiq: document.body.innerText.includes('muttafiq'), innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth, maxRight: Math.max(...[...document.querySelectorAll('body *')].filter(e=>e.offsetParent).map(e=>Math.round(e.getBoundingClientRect().right)))})"
agent-browser console 2>&1 | tail -4
agent-browser errors 2>&1 | tail -3
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r600-uh1-134-desktop.png" 2>&1 | tail -1

agent-browser set viewport 390 844
agent-browser wait 1500
agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth, maxRight: Math.max(...[...document.querySelectorAll('body *')].filter(e=>e.offsetParent).map(e=>Math.round(e.getBoundingClientRect().right))), h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,80)})"
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r600-uh1-134-mobile.png" 2>&1 | tail -1

agent-browser close 2>&1 | tail -1
echo "QA DONE pdf-mut23h2q-134"
