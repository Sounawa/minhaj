#!/bin/bash
# R344 — réfutation factuelle VLM mobile 19799 (règle cb)
set -x
TS=$(date +%s)
cd /home/z/my-project

agent-browser open "http://127.0.0.1:3000/?nc=$TS#/livre/rasm-wa-dabt-4ep/19799" 2>&1 | tail -1
agent-browser wait --load networkidle 2>&1 | tail -1
agent-browser wait 2200
agent-browser set viewport 390 844
agent-browser wait 1300

# 1) Chercher tout élément flottant/fixed (navigation) et mesurer le chevauchement réel avec le texte
agent-browser eval "JSON.stringify({fixed: [...document.querySelectorAll('body *')].filter(e=>{const s=getComputedStyle(e); return (s.position==='fixed'||s.position==='sticky')&&e.offsetParent!==undefined;}).slice(0,12).map(e=>{const r=e.getBoundingClientRect(); return {tag:e.tagName, cls:(e.className+'').slice(0,40), top:Math.round(r.top), bottom:Math.round(r.bottom), left:Math.round(r.left), right:Math.round(r.right)};})})"

# 2) Rect du premier paragraphe h1 + premier p
agent-browser eval "JSON.stringify({h1: (()=>{const e=document.querySelector('h1'); const r=e?.getBoundingClientRect(); return r?{top:Math.round(r.top),bottom:Math.round(r.bottom)}:null})(), firstP: (()=>{const e=document.querySelector('p'); const r=e?.getBoundingClientRect(); return r?{top:Math.round(r.top),bottom:Math.round(r.bottom)}:null})()})"

# 3) Scan TOUS les éléments : chevauchement réel d'un élément flottant sur du texte (zIndex)
agent-browser eval "(()=>{const fixed=[...document.querySelectorAll('body *')].filter(e=>{const s=getComputedStyle(e); return s.position==='fixed'&&e.offsetHeight>0;}); let overlaps=[]; for(const f of fixed){const fr=f.getBoundingClientRect(); if(fr.width===0) continue; for(const p of document.querySelectorAll('p,h1,h2,h3,li')){const pr=p.getBoundingClientRect(); if(pr.height===0) continue; const ix=Math.max(0,Math.min(fr.right,pr.right)-Math.max(fr.left,pr.left)); const iy=Math.max(0,Math.min(fr.bottom,pr.bottom)-Math.max(fr.top,pr.top)); if(ix>4&&iy>4){const fs=getComputedStyle(f); overlaps.push({f:(f.className+'').slice(0,30),p:p.tagName,sameStack: fs.zIndex}); break;}}} return JSON.stringify({nFixed:fixed.length, overlaps:overlaps});})()"

# 4) Crop ciblé du haut de page mobile (la zone alléguée)
agent-browser screenshot "/home/z/my-project/tr-tmp/qa-19799-top-mobile.png" 2>&1 | tail -1

agent-browser close 2>&1 | tail -1
echo "REFUTATION DONE"
