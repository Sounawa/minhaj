#!/bin/bash
# R606 — QA navigateur pdf-mut23h2r-137 (dev server DÉJÀ ACTIF)
set -x
TS=$(date +%s)
cd /home/z/my-project
agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/ulum-hadith-tanawi-1/pdf-mut23h2r-137" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2500
agent-browser set viewport 1280 900
agent-browser wait 1200
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,120), badge: (document.body.innerText.match(/Leçon \d+ ?\/ ?\d+/)||[])[0], munkar: document.body.innerText.includes('munkar'), bayt: document.body.innerText.includes('taʿdīluhu lā yaḥmilu t-tafarrudā'), abuzakir: document.body.innerText.includes('Abū Zakīr'), gbayzar: document.body.innerText.includes('al-Ġayzār b. Ḥurayth'), sabii: document.body.innerText.includes('as-Sabīʿī'), muslim: document.body.innerText.includes('Fuʾād ʿAbd al-Bāqī'), mahfuz: document.body.innerText.includes('maḥfūẓ'), maruf: document.body.innerText.includes('maʿrūf'), innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth, maxRight: Math.max(...[...document.querySelectorAll('body *')].filter(e=>e.offsetParent).map(e=>Math.round(e.getBoundingClientRect().right)))})"
agent-browser console 2>&1 | tail -4
agent-browser errors 2>&1 | tail -3
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r606-uh1-137-desktop.png" 2>&1 | tail -1
agent-browser set viewport 390 844
agent-browser wait 1500
agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth, maxRight: Math.max(...[...document.querySelectorAll('body *')].filter(e=>e.offsetParent).map(e=>Math.round(e.getBoundingClientRect().right))), h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,80)})"
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r606-uh1-137-mobile.png" 2>&1 | tail -1
agent-browser close 2>&1 | tail -1
echo "QA DONE pdf-mut23h2r-137"
