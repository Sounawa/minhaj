#!/bin/bash
# R344 — QA navigateur 19799 (dev server DÉJÀ ACTIF port 3000 — ne pas relancer)
set -x
TS=$(date +%s)
cd /home/z/my-project

agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/rasm-wa-dabt-4ep/19799" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2500
agent-browser set viewport 1280 900
agent-browser wait 1200
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,120), badge21: !!document.body.innerText.includes('Leçon 21'), titre: (document.body.innerText.match(/Leçon \d+ ?\/ ?30/)||[])[0], innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth, maxRight: Math.max(...[...document.querySelectorAll('body *')].filter(e=>e.offsetParent).map(e=>Math.round(e.getBoundingClientRect().right)))})"
agent-browser console 2>&1 | tail -5
agent-browser errors 2>&1 | tail -3
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-19799-desktop.png" 2>&1 | tail -1

agent-browser set viewport 390 844
agent-browser wait 1500
agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth, maxRight: Math.max(...[...document.querySelectorAll('body *')].filter(e=>e.offsetParent).map(e=>Math.round(e.getBoundingClientRect().right))), matnTable: (()=>{const t=document.querySelector('.matn-table'); if(!t) return null; const r=t.getBoundingClientRect(); return {w: Math.round(r.width), right: Math.round(r.right), cells: [...t.querySelectorAll('td')].length, maxCellRight: Math.max(...[...t.querySelectorAll('td')].map(c=>Math.round(c.getBoundingClientRect().right)))};})()})"
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-19799-mobile.png" 2>&1 | tail -1

agent-browser close 2>&1 | tail -1
echo "QA DONE 19799"
