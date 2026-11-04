#!/bin/bash
# R562 — QA navigateur pdf-18 (hadith-2es leçon 17) — dev:3000 DÉJÀ ACTIF
set -x
TS=$(date +%s)
cd /home/z/my-project

agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/hadith-2es/pdf-18" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2500
agent-browser set viewport 1280 900
agent-browser wait 1200
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,110), badge: !!document.body.innerText.includes('Leçon 18 / 31'), savante: !!document.body.innerText.includes('Traduction savante'), h2: document.querySelectorAll('h2').length, h4: document.querySelectorAll('h4').length, chars: document.body.innerText.length, renvois: ['685','687','688','689','690','691','693','694','695','696'].map(n=>!!document.body.innerText.includes('n° '+n)), risala: !!document.body.innerText.includes('page 67'), overflow: document.body.scrollWidth > window.innerWidth, maxRight: Math.max(...[...document.querySelectorAll('body *')].filter(e=>e.offsetParent).map(e=>Math.round(e.getBoundingClientRect().right)))})"
agent-browser console 2>&1 | tail -5
agent-browser errors 2>&1 | tail -3
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r562-pdf18-desktop.png" 2>&1 | tail -1

agent-browser set viewport 390 844
agent-browser wait 1500
agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth, maxRight: Math.max(...[...document.querySelectorAll('body *')].filter(e=>e.offsetParent).map(e=>Math.round(e.getBoundingClientRect().right)))})"
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r562-pdf18-mobile.png" 2>&1 | tail -1

agent-browser close 2>&1 | tail -1
echo "QA DONE pdf-18"
