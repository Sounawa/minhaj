#!/bin/bash
cd /home/z/my-project
URL="http://localhost:3000/?nc=R350qa#/livre/rasm-wa-dabt-4ep/20054"
agent-browser open "$URL" 2>/dev/null | tail -1
agent-browser set viewport 1280 900 2>/dev/null | tail -1
sleep 2
agent-browser eval "JSON.stringify({sw:screen.width,cw:document.documentElement.clientWidth,maxR:Math.round(Math.max(...document.querySelectorAll('body *').filter(e=>e.getBoundingClientRect().right>1281).map(e=>Math.round(e.getBoundingClientRect().right)).slice(0,20)),sc:document.body.scrollHeight,h1:document.querySelector('h1')?.textContent.trim(),badge:document.querySelector('.lesson-badge')?.textContent.trim(),err:window.__errors||0})" 2>/dev/null | tail -2
agent-browser eval "window.addEventListener('error',e=>{window.__ec=(window.__ec||0)+1})" 2>/dev/null | tail -1
sleep 1
agent-browser eval "JSON.stringify({ec:window.__ec||0})" 2>/dev/null | tail -1
agent-browser screenshot tr-tmp/qa-20054-desktop.png 2>/dev/null | tail -1
agent-browser set viewport 390 844 2>/dev/null | tail -1
sleep 2
agent-browser eval "JSON.stringify({sw:screen.width,cw:document.documentElement.clientWidth,maxR:Math.round(Math.max(...document.querySelectorAll('body *').filter(e=>e.getBoundingClientRect().right>391).map(e=>Math.round(e.getBoundingClientRect().right)).slice(0,20)),nOver:document.querySelectorAll('body *').filter(e=>e.getBoundingClientRect().right>391).length})" 2>/dev/null | tail -2
agent-browser screenshot tr-tmp/qa-20054-mobile.png 2>/dev/null | tail -1
