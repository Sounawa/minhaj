#!/bin/bash
# R591 — QA navigateur pdf-mut23h2q-125 (dev server DÉJÀ ACTIF — ne pas relancer)
set -x
TS=$(date +%s)
cd /home/z/my-project

agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/ulum-hadith-tanawi-1/pdf-mut23h2q-125" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2500
agent-browser set viewport 1280 900
agent-browser wait 1200
agent-browser eval "JSON.stringify({h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,120), badge: (document.body.innerText.match(/Leçon \d+ ?\/ ?\d+/)||[])[0], savante: document.body.innerText.includes('Traduction savante'), mursal: document.body.innerText.includes('mursal'), maryam84: document.body.innerText.includes('84'), suyuti: document.body.innerText.includes('Suyūṭī'), muwatta: document.body.innerText.includes('Muwaṭṭaʾ'), innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth, maxRight: Math.max(...[...document.querySelectorAll('body *')].filter(e=>e.offsetParent).map(e=>Math.round(e.getBoundingClientRect().right)))})"
agent-browser console 2>&1 | tail -4
agent-browser errors 2>&1 | tail -3
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r591-uh1-125-desktop.png" 2>&1 | tail -1

agent-browser set viewport 390 844
agent-browser wait 1500
agent-browser eval "JSON.stringify({innerW: window.innerWidth, scrollW: document.body.scrollWidth, overflow: document.body.scrollWidth > window.innerWidth, maxRight: Math.max(...[...document.querySelectorAll('body *')].filter(e=>e.offsetParent).map(e=>Math.round(e.getBoundingClientRect().right))), h1: document.querySelector('h1')?.textContent?.trim()?.slice(0,80)})"
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-r591-uh1-125-mobile.png" 2>&1 | tail -1

agent-browser close 2>&1 | tail -1
echo "QA DONE pdf-mut23h2q-125"
