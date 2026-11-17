#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Générateur du site statique complet du Minhaj (المنهج النموذجي للتعليم العتيق).

Lit content/books/*.json (STRICTEMENT en lecture seule — la transcription
htmlFr n'est jamais modifiée) et content/manifest.json, puis produit dans
site/ un site entièrement pré-généré, sans aucun fetch à l'exécution :

  index.html                       accueil : grille des 64 livres + recherche globale
  livres/<slug>/index.html         sommaire du livre (leçons transcrites liées, autres grisées)
  livres/<slug>/introduction.html  présentation du manuel (si une intro existe)
  livres/<slug>/<docId>.html       page de leçon transcrite (htmlFr rendu tel quel)
  assets/style.css                 feuille de style unique — thème « automne »
  recherche.js                     moteur de recherche (JS pur, aucune dépendance)
  recherche/                       index de recherche découpé (titres + fragments par cycle)
  hors-ligne.html                  variante mono-fichier : tout embarqué, ouvrable en file://
  ancien-lecteur.html              copie de l'ancien lecteur SPA (chemins fetch corrigés)
  404.html, robots.txt, sitemap.xml

Publication (option --publier RACINE) : copie le contenu de site/ à la racine
RACINE du dépôt — la source GitHub Pages détectée est la branche main, chemin /.
À la racine, ancien-lecteur.html garde ses fetch « content/books/… » ; dans
site/, la copie utilise « ../../content/books/… ».

Chemins RELATIFS partout (site servi depuis /minhaj/), UTF-8, Python stdlib.
"""

import argparse
import base64
import html as html_mod
import json
import re
import shutil
import sys
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape as xescape

# ---------------------------------------------------------------------------
# Constantes de mise en page
# ---------------------------------------------------------------------------

CSS = r"""/* ============================================================
   Minhaj — المنهاج النموذجي للتعليم العتيق
   Thème « manuscrit d’automne » : parchemin, olive profond,
   terre brûlée, or vieilli. CSS pur, aucune dépendance locale.
   ============================================================ */
:root{
  --fond:#f3ebd8;
  --fond-2:#eaddc1;
  --carte:#fffdf6;
  --carte-2:#f9f3e2;
  --encre:#2c2314;
  --encre-2:#5f5140;
  --gris:#75664e;
  --terracotta:#a8511b;
  --terracotta-f:#8c4212;
  --or:#b98a2e;
  --or-f:#8f6a1e;
  --or-p:#ecd9a8;
  --olive:#5b6a2c;
  --olive-f:#3c4818;
  --olive-nuit:#333e14;
  --ligne:#e0d2b2;
  --ligne-2:#c9b98f;
  --naskh:"Noto Naskh Arabic","Amiri","Scheherazade New","Geeza Pro","Traditional Arabic",serif;
  --amiri:"Amiri","Noto Naskh Arabic","Scheherazade New","Traditional Arabic",serif;
  --serif:Georgia,"Iowan Old Style","Palatino Linotype","Times New Roman",serif;
}
/* Couleur d’accent par matière (automne : olives, terres, bronzes) */
[data-sujet="tawhid"]{--sujet:#4c5d1f}
[data-sujet="fiqh"]{--sujet:#7a5418}
[data-sujet="sira"]{--sujet:#9c4a12}
[data-sujet="tajwid"]{--sujet:#8a6a14}
[data-sujet="tafsir"]{--sujet:#57641d}
[data-sujet="hadith"]{--sujet:#8c4a2a}
[data-sujet="faraid"]{--sujet:#9c5c14}
[data-sujet="usul-fiqh"]{--sujet:#5c5218}
[data-sujet="mantiq"]{--sujet:#41564f}
[data-sujet="ulum-hadith"]{--sujet:#7c3f16}
[data-sujet="ulum-quran"]{--sujet:#4e6118}
[data-sujet="qiraat"]{--sujet:#8f5c18}
[data-sujet="rasm-wa-dabt"]{--sujet:#3f5b47}
[data-sujet="taqtit"]{--sujet:#6e5c20}
[data-sujet="fikr-islami"]{--sujet:#833c12}
[data-sujet="usul-qiyam"]{--sujet:#55642b}
[data-sujet="nahu"]{--sujet:#6b3a20}
[data-sujet="balagha"]{--sujet:#714a12}
[data-sujet="adab"]{--sujet:#54491a}
[data-sujet=""]{--sujet:#5c5218}

*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--fond);color:var(--encre);font:17px/1.75 var(--serif)}
::selection{background:var(--or-p);color:var(--encre)}
a{color:var(--terracotta-f);text-decoration:none}
a:hover{text-decoration:underline;color:var(--terracotta)}
:focus-visible{outline:3px solid var(--or);outline-offset:2px;border-radius:3px}
.hors-ecran{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}

/* ---------- en-tête ---------- */
.en-tete{background:linear-gradient(180deg,#46541f,#333e14 82%);color:#f2ecd9;border-bottom:1px solid #222b0c}
.en-tete::after{content:"";display:block;height:5px;
  background:repeating-linear-gradient(90deg,#b98a2e 0 16px,#7d6118 16px 19px,#55672a 19px 34px,#7d6118 34px 37px)}
.en-tete .interieur{max-width:1120px;margin:0 auto;padding:12px 22px;display:flex;flex-wrap:wrap;gap:2px 22px;align-items:center}
.en-tete .marque a{display:inline-flex;flex-direction:column;gap:1px}
.en-tete .marque .arabe{font-family:var(--amiri);font-size:1.5rem;line-height:1.5;color:#f3e6c3}
.en-tete .marque .sous-marque{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:#c9bd97}
.en-tete .liens{margin-inline-start:auto;display:flex;gap:18px;font-size:.85rem;letter-spacing:.02em}
.en-tete .liens a{color:#e6d9ae}
.en-tete .liens a:hover{color:#fff3d0}

/* ---------- corps ---------- */
main{max-width:1120px;margin:0 auto;padding:26px 22px 40px}
main.lecture{max-width:940px}
.fil{font-size:.8rem;letter-spacing:.05em;text-transform:uppercase;color:var(--gris);margin:2px 0 20px}
.fil a{color:var(--olive-f)}
.fil .sep{margin:0 9px;color:var(--or)}

/* ---------- héros (pleine page, accueil) ---------- */
.heros.pleine{background:
  radial-gradient(1100px 420px at 50% -60px,rgba(185,138,46,.16),transparent 62%),
  linear-gradient(180deg,#f7f0dd,var(--fond));
  text-align:center;padding:44px 22px 36px;border-bottom:1px solid var(--ligne-2)}
.heros.pleine .surline{color:var(--terracotta-f);letter-spacing:.13em;text-transform:uppercase;font-size:.74rem;font-weight:600;margin:0}
.heros h1{margin:.35em 0 .1em}
.heros h1 .arabe{font-family:var(--amiri);font-weight:700;font-size:clamp(2.4rem,6vw,3.5rem);line-height:1.75;color:var(--olive-f);display:block}
.heros .sous{color:var(--encre-2);max-width:720px;margin:.4em auto .2em;font-size:1.03rem}
/* variante en panneau (hors-ligne, 404) */
main .heros{max-width:840px;margin:6px auto 26px;text-align:center;background:var(--carte);border:1px solid var(--ligne);border-radius:16px;padding:32px 26px 28px}
main .heros .surline{color:var(--terracotta-f);letter-spacing:.13em;text-transform:uppercase;font-size:.74rem;font-weight:600;margin:0}
main .heros h1 .arabe{font-family:var(--amiri);font-weight:700;font-size:2.2rem;line-height:1.8;color:var(--olive-f);display:block}
main .heros .sous{color:var(--encre-2);max-width:680px;margin:.4em auto .2em}

/* ornement : filets + trois losanges */
.ornement{display:flex;align-items:center;gap:9px;max-width:400px;margin:16px auto 6px}
.ornement span{flex:1;height:1px;background:linear-gradient(90deg,transparent,var(--or))}
.ornement span:last-child{background:linear-gradient(90deg,var(--or),transparent)}
.ornement i{width:5px;height:5px;background:var(--or);transform:rotate(45deg);flex:none}
.ornement i:first-of-type{width:7px;height:7px}

/* statistiques */
.stats{display:flex;max-width:640px;margin:24px auto 4px;border:1px solid var(--ligne-2);border-radius:14px;background:rgba(255,253,246,.8);box-shadow:0 2px 12px -6px rgba(90,70,30,.25)}
.stat{flex:1;padding:13px 8px 11px;border-inline-end:1px solid var(--ligne)}
.stat:last-child{border-inline-end:0}
.stat b{display:block;font-size:1.55rem;line-height:1.2;color:var(--olive-f);font-variant-numeric:tabular-nums}
.stat span{font-size:.72rem;letter-spacing:.09em;text-transform:uppercase;color:var(--gris)}

/* progression */
.prog{max-width:520px;margin:18px auto 0}
.barre{height:9px;background:var(--fond-2);border:1px solid var(--ligne-2);border-radius:99px;overflow:hidden}
.barre span{display:block;height:100%;background:linear-gradient(90deg,var(--olive-f),#7d8c3e);border-radius:99px}
.compte{font-size:.92rem;color:var(--encre-2);margin:9px 0 0}
.compte strong{color:var(--encre);font-size:1.06rem}

/* ---------- recherche ---------- */
.recherche{position:relative;max-width:660px;margin:26px auto 8px}
.recherche input{width:100%;font:inherit;padding:13px 20px 13px 46px;border:1px solid var(--ligne-2);border-radius:14px;background:var(--carte);color:var(--encre);box-shadow:0 3px 14px -8px rgba(90,70,30,.35)}
.recherche input::placeholder{color:var(--gris);font-style:italic}
.recherche input:focus{border-color:var(--or);outline:2px solid var(--or-p)}
.recherche input{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Ccircle cx='8.5' cy='8.5' r='5.5' fill='none' stroke='%23b98a2e' stroke-width='2'/%3E%3Cline x1='13' y1='13' x2='18' y2='18' stroke='%23b98a2e' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:15px 50%;background-size:19px}
.statut{color:var(--gris);font-size:.85rem;margin:8px 4px}
.resultats{margin-top:12px}
.resultats ol{list-style:none;margin:8px 0 0;padding:0}
.resultats li{background:var(--carte);border:1px solid var(--ligne);border-radius:12px;padding:12px 16px;margin-bottom:9px;box-shadow:0 2px 8px -6px rgba(90,70,30,.3)}
.resultats li.r-livre{border-inline-start:4px solid var(--olive)}
.resultats li.r-lecon{border-inline-start:4px solid var(--or)}
.resultats .r-titre{font-weight:700}
.resultats .r-titre a{display:inline}
.resultats .r-livre-n{color:var(--gris);font-size:.8rem;margin-inline-start:9px;letter-spacing:.04em}
.resultats .r-extrait{margin:7px 0 0;font-size:.93rem;color:var(--encre-2);line-height:2}
.resultats .r-extrait mark{background:var(--or-p);color:var(--encre);padding:0 3px;border-radius:3px}
.resultats .r-compte{color:var(--gris);font-size:.85rem;margin:10px 4px}

/* ---------- bibliothèque : sections par matière ---------- */
.sujet-titre{display:flex;align-items:center;gap:13px;margin:36px 2px 16px;font-size:1rem;font-weight:400}
.sujet-titre::before{content:"";width:10px;height:10px;background:var(--or);transform:rotate(45deg);flex:none}
.sujet-titre .sujet-ar{font-family:var(--amiri);font-size:1.65rem;line-height:1.4;color:var(--olive-f)}
.sujet-titre .sujet-fr{letter-spacing:.11em;text-transform:uppercase;font-size:.8rem;font-weight:700;color:var(--encre-2)}
.sujet-titre::after{content:"";flex:1;height:1px;background:linear-gradient(90deg,var(--ligne-2),transparent)}
.sujet-titre .sujet-n{color:var(--gris);font-size:.8rem;white-space:nowrap;letter-spacing:.03em}

/* grille et cartes des livres */
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(258px,1fr));gap:16px}
.carte-cadre{display:contents}
.carte{--sujet:#5c5218;position:relative;display:flex;flex-direction:column;background:var(--carte);border:1px solid var(--ligne);border-radius:13px;padding:17px 17px 14px;color:inherit;overflow:hidden;transition:transform .16s ease,box-shadow .16s ease,border-color .16s ease}
.carte::before{content:"";position:absolute;inset:0 0 auto 0;height:3px;background:var(--sujet)}
.carte::after{content:"";position:absolute;top:9px;inset-inline-end:9px;width:20px;height:20px;border-top:1px solid var(--or-p);border-inline-end:1px solid var(--or-p);border-start-end-radius:7px}
.carte:hover{text-decoration:none;transform:translateY(-3px);box-shadow:0 12px 26px -14px rgba(70,50,15,.45);border-color:var(--ligne-2);color:inherit}
.puces{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 10px}
.chip{font-size:.67rem;letter-spacing:.07em;text-transform:uppercase;font-weight:700;color:var(--encre-2);border:1px solid var(--ligne-2);border-radius:99px;padding:2.5px 10px;background:var(--carte-2);white-space:nowrap}
.chip-sujet{color:var(--sujet,#5c5218);border-color:var(--sujet,#c9b98f);background:transparent}
.chip-lien{cursor:pointer}
a.chip-lien:hover{text-decoration:none;border-color:var(--or);color:var(--or-f)}
.carte .t-ar{font-family:var(--naskh);font-size:1.4rem;line-height:2.05;text-align:center;display:block;margin:1px 0 7px;color:var(--olive-f)}
.carte .t-fr{display:block;text-align:center;font-size:.92rem;line-height:1.55;color:var(--encre-2);flex:1}
.carte-pied{margin-top:12px;padding-top:10px;border-top:1px dashed var(--ligne-2);display:flex;flex-direction:column;gap:8px}
.carte .compte{font-size:.82rem;color:var(--gris);margin:0}
.mini-barre{height:5px;border-radius:99px;background:var(--fond-2);overflow:hidden;display:block}
.mini-barre span{display:block;height:100%;background:linear-gradient(90deg,var(--olive-f),#7d8c3e);border-radius:99px}
.carte.a-faire .t-ar{color:var(--gris)}
.carte.a-faire::before{opacity:.45}

/* ---------- sommaire d’un livre ---------- */
.livre-tete{max-width:780px;margin:4px auto 26px;text-align:center;background:var(--carte);border:1px solid var(--ligne-2);border-radius:16px;padding:30px 28px 24px;position:relative;box-shadow:0 3px 16px -10px rgba(90,70,30,.3)}
.livre-tete::before{content:"";position:absolute;inset:7px;border:1px solid var(--or-p);border-radius:11px;pointer-events:none}
.livre-tete .puces{justify-content:center;margin:0 0 12px}
.livre-tete h1{margin:.05em 0 .05em}
.livre-tete h1 .arabe{font-family:var(--amiri);font-weight:700;font-size:2.15rem;line-height:1.85;color:var(--olive-f);display:block}
.livre-tete .t-fr{color:var(--encre-2);margin:.1em 0 0;font-size:1rem}
.livre-tete .prog{margin-top:16px}

/* liste des leçons */
.lecons{list-style:none;margin:0 auto 34px;max-width:780px;padding:0;border:1px solid var(--ligne);border-radius:14px;background:var(--carte);overflow:hidden;box-shadow:0 3px 16px -12px rgba(90,70,30,.35)}
.lecons li{border-bottom:1px solid var(--ligne)}
.lecons li:last-child{border-bottom:0}
.lecons li a,.lecons .ligne-lecon{display:flex;gap:15px;align-items:flex-start;padding:13px 20px}
.lecons li a:hover{background:var(--carte-2);text-decoration:none}
.badge{flex:none;min-width:33px;height:33px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;background:var(--fond-2);border:1px solid var(--ligne-2);color:var(--encre-2);font-size:.82rem;font-variant-numeric:tabular-nums;font-weight:700;margin-top:3px}
.lecons .fait .badge{background:var(--olive-f);border-color:var(--olive-f);color:#f6f2df}
.lecons .intro-l .badge{background:var(--or);border-color:var(--or);color:#fffdf6;font-size:.85rem}
.libelles{display:flex;flex-direction:column;gap:1px;min-width:0;flex:1}
.lecons .t-ar{font-family:var(--naskh);font-size:1.2rem;line-height:2.05;color:var(--encre)}
.lecons .t-fr{color:var(--encre-2);font-size:.9rem;line-height:1.55}
.lecons li.a-faire{background:repeating-linear-gradient(45deg,transparent 0 13px,rgba(160,130,60,.055) 13px 26px)}
.lecons li.a-faire .t-ar,.lecons li.a-faire .t-fr{color:var(--gris)}
.lecons .pdf{flex:none;align-self:center;font-size:.74rem;letter-spacing:.04em;color:var(--or-f);border:1px solid var(--ligne-2);border-radius:99px;padding:3px 12px}
.lecons .pdf:hover{border-color:var(--or);text-decoration:none}

/* ---------- page de leçon ---------- */
.contenu{max-width:840px;margin:0 auto;background:var(--carte);border:1px solid var(--ligne-2);border-radius:6px;padding:44px 54px 40px;position:relative;box-shadow:0 16px 36px -24px rgba(70,50,15,.45)}
.contenu::before{content:"";position:absolute;inset:10px;border:1px solid var(--or-p);border-radius:3px;pointer-events:none}
.contenu::after{content:"";position:absolute;top:-9px;left:50%;transform:translateX(-50%) rotate(45deg);width:13px;height:13px;background:var(--or);border:2px solid var(--fond)}
.contenu h1{font-size:1.6rem;line-height:1.7;color:var(--olive-f);text-align:center;margin:.1em 0 .9em;padding-bottom:.6em;border-bottom:1px solid var(--ligne-2);position:relative}
.contenu h1::after{content:"";position:absolute;bottom:-4.5px;left:50%;transform:translateX(-50%) rotate(45deg);width:9px;height:9px;background:var(--or)}
.contenu h2{font-size:1.28rem;line-height:1.6;color:var(--olive-f);margin:2em 0 .7em;padding:0 0 .35em;padding-inline-start:26px;border-bottom:1px solid var(--ligne);position:relative}
.contenu h2::before{content:"";position:absolute;inset-inline-start:2px;top:.55em;width:9px;height:9px;background:var(--or);transform:rotate(45deg)}
.contenu h3{font-size:1.1rem;line-height:1.6;color:var(--terracotta-f);margin:1.6em 0 .45em}
.contenu h4,.contenu h5,.contenu h6{font-size:1rem;color:var(--encre-2);margin:1.3em 0 .4em}
.contenu p{margin:1em 0;line-height:1.85}
.contenu em{font-style:italic;color:#6d4318}
.contenu strong{color:var(--encre)}
.contenu ul{list-style:none;margin:.9em 0;padding:0}
.contenu ul li{margin:.45em 0;padding-inline-start:19px;position:relative}
.contenu ul li::before{content:"";position:absolute;inset-inline-start:3px;top:.75em;width:6px;height:6px;background:var(--or);transform:rotate(45deg);opacity:.8}
.contenu ol{margin:.9em 0;padding-inline-start:26px}
.contenu ol li{margin:.45em 0}
.contenu ol li::marker{color:var(--terracotta-f);font-weight:700}
.contenu dl{margin:.9em 0}
.contenu dt{font-weight:700;margin-top:.75em;color:var(--olive-f)}
.contenu dd{margin:.15em 0 .15em 1.4em}
.contenu blockquote{border-inline-start:3px solid var(--or);margin:1.1em 0;padding:.2em 0 .2em 1.15em;color:var(--encre-2);font-style:italic}
.contenu table{border-collapse:collapse;margin:1.2em 0;width:100%;font-size:.95em;line-height:1.7;background:var(--carte-2)}
.contenu th,.contenu td{border:1px solid var(--ligne-2);padding:8px 13px;vertical-align:top}
.contenu th{background:var(--or-p);color:var(--encre);font-weight:700}
.contenu sup{font-size:.72em}
.contenu code{font-size:.9em;background:var(--carte-2);border:1px solid var(--ligne);border-radius:4px;padding:0 5px}
.contenu [lang="ar"]{font-family:var(--naskh);font-size:1.42em;line-height:2.3;color:#24300e}
.contenu .intro-arabe{direction:rtl;text-align:right;border:1px solid var(--ligne);border-inline-start:4px solid var(--or);border-radius:10px;background:var(--carte-2);padding:20px 24px;margin:1.3em 0}
.contenu .intro-arabe [lang="ar"]{font-size:1.4em}

/* ---------- navigation précédent / suivant ---------- */
.pn{display:grid;grid-template-columns:1fr auto 1fr;gap:10px;align-items:stretch;max-width:840px;margin:24px auto 0}
.pn a,.pn .pn-vide{background:var(--carte);border:1px solid var(--ligne);border-radius:12px;padding:12px 16px;font-size:.93rem;line-height:1.6;color:var(--olive-f)}
.pn a:hover{text-decoration:none;border-color:var(--or);box-shadow:0 6px 16px -10px rgba(120,90,30,.5)}
.pn .pn-l{display:block;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gris);margin-bottom:3px}
.pn .pn-suiv{text-align:end}
.pn .pn-sommaire{background:var(--olive-f);border-color:var(--olive-f);color:#f2ecd9;text-align:center;padding:12px 20px;font-size:.9rem}
.pn .pn-sommaire:hover{background:#47551f}
.pn .pn-vide{color:var(--gris);border-style:dashed;background:transparent}

/* ---------- hors-ligne : accordéons ---------- */
details.lecon{background:var(--carte);border:1px solid var(--ligne);border-radius:12px;margin:10px 0;overflow:hidden}
details.lecon summary{cursor:pointer;padding:13px 20px;display:flex;gap:15px;align-items:flex-start;list-style:none}
details.lecon summary::-webkit-details-marker{display:none}
details.lecon summary::before{content:"";flex:none;width:9px;height:9px;background:var(--or);transform:rotate(45deg);margin-top:15px;transition:transform .15s ease}
details.lecon[open] summary::before{transform:rotate(225deg)}
details.lecon[open] summary{border-bottom:1px dashed var(--ligne-2);background:var(--carte-2)}
details.lecon summary:hover{background:var(--carte-2)}
details.lecon .contenu{background:none;border:none;border-radius:0;padding:18px 26px 22px;margin:0;max-width:none;box-shadow:none}
details.lecon .contenu::before,details.lecon .contenu::after{display:none}
.section-livre{margin:38px 0}
.section-livre>h2{font-size:1.2rem;font-weight:400;color:var(--olive-f);border-bottom:2px solid var(--ligne-2);padding-bottom:.35em;display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
.section-livre>h2 .arabe{font-family:var(--amiri);font-size:1.7rem}
.section-livre .meta-l{font-size:.83rem;color:var(--gris);margin:.25em 0 12px}

/* ---------- bandeau (404, ancien lecteur) ---------- */
.bandeau{background:linear-gradient(180deg,#46541f,#333e14);border-bottom:3px solid var(--or);color:#f2ecd9;text-align:center;font-size:.88rem;padding:10px 16px}
.bandeau a{color:#f3e0b0;font-weight:700;text-decoration:underline}

/* ---------- pied de page ---------- */
.pied{background:linear-gradient(180deg,#3a4517,#2c360f);color:#cfc6a6;margin-top:44px}
.pied::before{content:"";display:block;height:4px;
  background:repeating-linear-gradient(90deg,#8f6a1e 0 16px,#5b6a2c 16px 34px,#8f6a1e 34px 37px)}
.pied .interieur{max-width:1120px;margin:0 auto;padding:26px 22px 30px;text-align:center;font-size:.85rem;line-height:2}
.pied-orn{display:flex;align-items:center;justify-content:center;gap:8px;margin:0 0 12px}
.pied-orn i{width:5px;height:5px;background:var(--or);transform:rotate(45deg)}
.pied-orn i:first-child{width:7px;height:7px}
.pied-orn span{width:60px;height:1px;background:linear-gradient(90deg,transparent,#8f6a1e)}
.pied-orn span:last-child{background:linear-gradient(90deg,#8f6a1e,transparent)}
.pied a{color:#e6c98c}
.pied .pied-liens span{margin:0 8px;color:#7a7355}

/* ---------- impression ---------- */
@media print{
  .en-tete,.pied,.fil,.pn,.recherche,.bandeau,.stats{display:none}
  .contenu{border:0;box-shadow:none;padding:0}
  .contenu::before,.contenu::after{display:none}
  body{background:#fff}
}

/* ---------- écrans étroits ---------- */
@media (max-width:720px){
  body{font-size:16px}
  .en-tete .interieur{padding:10px 16px;gap:2px 14px}
  .en-tete .marque .arabe{font-size:1.3rem}
  .en-tete .liens{margin-inline-start:0;gap:14px}
  main{padding:22px 14px 34px}
  .heros.pleine{padding:34px 16px 28px}
  .contenu{padding:26px 20px 24px}
  .lecons li a,.lecons .ligne-lecon{padding:12px 14px;gap:11px}
  .details-lecon-gap{display:none}
  .pn{grid-template-columns:1fr}
  .pn .pn-sommaire{order:-1}
  .stats{flex-direction:column}
  .stat{border-inline-end:0;border-bottom:1px solid var(--ligne);padding:10px 8px 8px}
  .stat:last-child{border-bottom:0}
  .sujet-titre{gap:9px;margin:30px 2px 12px}
  .sujet-titre .sujet-ar{font-size:1.45rem}
  .sujet-titre .sujet-fr{font-size:.72rem;letter-spacing:.08em}
}
"""

# Feuille de style externe (scripts/site-style.css) si présente :
# permet de faire évoluer le design sans toucher à la constante embarquée.
_CSS_EXTERNE = Path(__file__).resolve().parent / 'site-style.css'
if _CSS_EXTERNE.exists():
    CSS = _CSS_EXTERNE.read_text(encoding='utf-8')

RECHERCHE_JS = r"""/* Moteur de recherche du Minhaj — JS pur, aucune dépendance.
 * Recherche par titre et par texte des leçons transcrites, en français
 * comme en arabe : la requête et l'index sont normalisés de la même façon
 * (voyelles courtes arabes retirées, hamzas unifiées, accents français retirés).
 * L'extrait affiché est recadré dans le texte d'origine (arabe vocalisé conservé).
 */
(function (globale) {
'use strict';

/* Normalisation rapide (utilisée sur tout l'index à la première recherche). */
function normaliser(s) {
  return String(s).toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed\u0640]/g, '')
    .replace(/[\u0623\u0625\u0622\u0671]/g, '\u0627')
    .replace(/\u0649/g, '\u064a')
    .replace(/\u0153/g, 'oe').replace(/\u00e6/g, 'ae')
    .replace(/\s+/g, ' ').trim();
}

/* Normalisation avec carte vers les positions d'origine (pour les extraits).
 * Règles identiques à normaliser() : les positions restent donc alignées. */
function normaliserCarte(s) {
  var t = '', m = [], esp = true;
  for (var i = 0; i < s.length; i++) {
    var d = s.charAt(i).toLowerCase().normalize('NFD');
    for (var j = 0; j < d.length; j++) {
      var c = d.charAt(j), k = d.charCodeAt(j);
      if ((k >= 0x0300 && k <= 0x036f) || (k >= 0x0610 && k <= 0x061a) ||
          (k >= 0x064b && k <= 0x065f) || k === 0x0670 || k === 0x0640 ||
          (k >= 0x06d6 && k <= 0x06ed)) continue;
      var reps;
      if (k === 0x0623 || k === 0x0625 || k === 0x0622 || k === 0x0671) reps = ['\u0627'];
      else if (k === 0x0649) reps = ['\u064a'];
      else if (k === 0x0153) reps = ['o', 'e'];
      else if (k === 0x00e6) reps = ['a', 'e'];
      else reps = [c];
      for (var q = 0; q < reps.length; q++) {
        var rc = reps[q];
        if (/\s/.test(rc)) { if (!esp) { t += ' '; m.push(i); esp = true; } }
        else { t += rc; m.push(i); esp = false; }
      }
    }
  }
  while (t.length && t.charAt(t.length - 1) === ' ') { t = t.slice(0, -1); m.pop(); }
  return { t: t, m: m };
}

function ech(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

var etat = { pret: false, donnees: null };

function preparer(donnees) {
  var livres = (donnees.books || []).map(function (b) {
    return { titre: b.t || '', nt: normaliser((b.t || '') + ' ' + (b.ta || '')), url: b.u || '#' };
  });
  var lecons = (donnees.lecons || []).map(function (l) {
    return {
      b: l.b, docId: l.d, titre: l.t || '', url: l.u || '#', x: l.x || '',
      nt: normaliser((l.t || '') + ' ' + (l.ta || '')), nx: null
    };
  });
  return { books: livres, lecons: lecons };
}

/* Extrait recadré dans le texte d'origine, avec surlignage du terme. */
function extrait(l, termes) {
  if (!l.x) return '';
  var carte = normaliserCarte(l.x);
  var nt = carte.t, m = carte.m, pos = -1, lg = 0;
  for (var k = 0; k < termes.length; k++) {
    var p = nt.indexOf(termes[k]);
    if (p !== -1 && (pos === -1 || p < pos)) { pos = p; lg = termes[k].length; }
  }
  var brut = l.x, d, f;
  if (pos === -1) { d = 0; f = Math.min(180, brut.length); }
  else {
    var rd = m[pos] || 0;
    var rf = (m[Math.min(pos + lg - 1, m.length - 1)] || rd) + 1;
    d = Math.max(0, rd - 80); f = Math.min(brut.length, rf + 110);
  }
  var morceau = brut.slice(d, f).replace(/\s+/g, ' ').trim();
  var cm = normaliserCarte(morceau), im = -1, it = 0;
  for (var k2 = 0; k2 < termes.length; k2++) {
    var p2 = cm.t.indexOf(termes[k2]);
    if (p2 !== -1) { im = p2; it = termes[k2].length; break; }
  }
  if (im !== -1) {
    var jd = cm.m[im] || 0;
    var jf = (cm.m[Math.min(im + it - 1, cm.m.length - 1)] || jd) + 1;
    return ech(morceau.slice(0, jd)) + '<mark>' + ech(morceau.slice(jd, jf)) + '</mark>' + ech(morceau.slice(jf));
  }
  return ech(morceau);
}

function chercher(requete) {
  if (!etat.pret) throw new Error('index non chargé');
  var qn = normaliser(requete).trim();
  var termes = qn ? qn.split(' ') : [];
  if (!termes.length) return { total: 0, resultats: [] };
  var res = [];
  etat.donnees.books.forEach(function (b, i) {
    var ok = termes.every(function (t) { return b.nt.indexOf(t) !== -1; });
    if (ok) res.push({ type: 'livre', score: 60 + (b.nt.indexOf(qn) === 0 ? 25 : 0), i: i });
  });
  etat.donnees.lecons.forEach(function (l, i) {
    if (l.nx === null) l.nx = normaliser(l.x);
    var dt = 0, dx = 0;
    for (var k = 0; k < termes.length; k++) {
      if (l.nt.indexOf(termes[k]) !== -1) dt++;
      if (l.nx.indexOf(termes[k]) !== -1) dx++;
    }
    if (dt + dx < termes.length) return;
    var s = 40 * dt + 26 * dx + ((l.nt.indexOf(qn) !== -1 || l.nx.indexOf(qn) !== -1) ? 30 : 0);
    res.push({ type: 'lecon', score: s, i: i });
  });
  res.sort(function (a, b) { return b.score - a.score; });
  var total = res.length;
  var resultats = res.slice(0, 50).map(function (x) {
    if (x.type === 'livre') {
      var b = etat.donnees.books[x.i];
      return { type: 'livre', titre: ech(b.titre), url: b.url };
    }
    var l = etat.donnees.lecons[x.i];
    var b2 = etat.donnees.books[l.b] || { titre: '' };
    return { type: 'lecon', titre: ech(l.titre), sousTitre: ech(b2.titre), url: l.url, extrait: extrait(l, termes) };
  });
  return { total: total, resultats: resultats };
}

/* Carte « b:d » -> entrée de leçon, pour l'ajout progressif des textes
 * complets arrivant par fragments (voir ajouterTexte). */
var indexLecons = {};

function definirDonnees(d) {
  etat.donnees = preparer(d);
  indexLecons = {};
  etat.donnees.lecons.forEach(function (l) { indexLecons[l.b + ':' + l.docId] = l; });
  etat.pret = true;
}

/* Ajout de fragments de texte complet chargés en arrière-plan : la recherche
 * suivante couvre aussi le contenu des leçons. Accepte soit une liste de
 * fragments {cycle, paires} (window.MINHAJ_TEXTE), soit une liste directe
 * de paires {b, d, x}. Retourne le nombre de documents enrichis. */
function ajouterTexte(fragments) {
  if (!etat.pret) return 0;
  var n = 0;
  (fragments || []).forEach(function (fr) {
    var paires = fr && fr.paires ? fr.paires : [fr];
    paires.forEach(function (p) {
      var l = indexLecons[p.b + ':' + p.d];
      if (l && p.x) { l.x = p.x; l.nx = null; n++; }
    });
  });
  return n;
}

function installerUI(opts) {
  var input = opts.input, cont = opts.conteneur, statut = opts.statut || null;
  var charge = false, enCours = false, minuteur = null;
  function rendre(r) {
    var h = '<p class="r-compte">' + r.total + ' résultat' + (r.total > 1 ? 's' : '') +
      (r.total > 50 ? ' — les 50 premiers sont affichés' : '') + '</p>';
    if (!r.total) h += '<p class="r-compte">Aucun résultat. Essayer un autre mot — français ou arabe (les voyelles courtes arabes sont ignorées).</p>';
    h += '<ol>';
    r.resultats.forEach(function (x) {
      if (x.type === 'livre') {
        h += '<li class="r-livre"><span class="r-titre"><a href="' + x.url + '">' + x.titre + '</a></span>' +
             '<span class="r-livre-n">livre</span></li>';
      } else {
        h += '<li class="r-lecon"><span class="r-titre"><a href="' + x.url + '">' + x.titre + '</a></span>' +
             '<span class="r-livre-n">' + x.sousTitre + '</span>' +
             (x.extrait ? '<p class="r-extrait" dir="auto">' + x.extrait + '</p>' : '') + '</li>';
      }
    });
    h += '</ol>';
    cont.innerHTML = h;
  }
  function lancer() {
    var q = input.value || '';
    if (q.trim().length < 2) { cont.innerHTML = ''; if (statut) statut.hidden = true; return; }
    if (!charge) { charger(); return; }
    var r;
    try { r = chercher(q); } catch (e) { charger(); return; }
    rendre(r);
  }
  function charger() {
    if (charge || enCours) return;
    enCours = true;
    if (statut) { statut.hidden = false; statut.textContent = 'Chargement de l\u2019index de recherche\u2026'; }
    opts.chargerIndex(function () {
      enCours = false; charge = true;
      if (statut) statut.hidden = true;
      lancer();
    }, function (msg) {
      enCours = false;
      if (statut) { statut.hidden = false; statut.textContent = 'Impossible de charger l\u2019index de recherche.' + (msg ? ' ' + msg : ''); }
    });
  }
  input.addEventListener('focus', charger);
  input.addEventListener('input', function () {
    if (minuteur) clearTimeout(minuteur);
    minuteur = setTimeout(lancer, 150);
  });
  return { lancer: lancer };
}

globale.MinhajRecherche = {
  normaliser: normaliser,
  definirDonnees: definirDonnees,
  ajouterTexte: ajouterTexte,
  pret: function () { return etat.pret; },
  chercher: chercher,
  installerUI: installerUI
};
})(window);
"""

BANDEAU_CSS = ('<style>.bandeau{background:#f1d9a0;border-bottom:2px solid #a67c00;color:#33291a;'
               'text-align:center;font-size:.85rem;padding:7px 14px;font-family:Georgia,serif}'
               '.bandeau a{color:#8a5616;font-weight:bold}</style>')

# ---------------------------------------------------------------------------
# Extraction de texte
# ---------------------------------------------------------------------------

class ExtracteurTexte(HTMLParser):
    """htmlFr -> texte brut : balises retirées, entités décodées, espaces compactés."""

    BLOCS = ('p', 'br', 'h1', 'h2', 'h3', 'h4', 'h5', 'li', 'div', 'tr', 'dt', 'dd')

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.morceaux = []
        self.ignorer = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.ignorer += 1
        elif tag in self.BLOCS:
            self.morceaux.append(' ')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            if self.ignorer:
                self.ignorer -= 1
        elif tag in self.BLOCS:
            self.morceaux.append(' ')

    def handle_data(self, data):
        if not self.ignorer:
            self.morceaux.append(data)


def texte_plain(fragment):
    if not fragment:
        return ''
    ex = ExtracteurTexte()
    try:
        ex.feed(fragment)
        ex.close()
    except Exception:
        pass
    return re.sub(r'\s+', ' ', ''.join(ex.morceaux)).strip()


def esc(s):
    return html_mod.escape(str(s), quote=True)


def url_lecon(doc_id):
    """docId -> nom de fichier / segment d'URL (encodage % si nécessaire)."""
    return quote(doc_id, safe='')


# ---------------------------------------------------------------------------
# Chargement des données
# ---------------------------------------------------------------------------

def charger_livres(rep_books, manifest, avertissements):
    sujets = {s.get('id'): s for s in (manifest or {}).get('subjects', [])}
    niveaux = {n.get('id'): n for n in (manifest or {}).get('levels', [])}
    books_manifest = (manifest or {}).get('books', [])
    rang_manifest = {b.get('id'): i for i, b in enumerate(books_manifest)}

    livres = []
    for chemin in sorted(Path(rep_books).glob('*.json')):
        slug = chemin.stem
        try:
            data = json.loads(chemin.read_text(encoding='utf-8'))
        except Exception as e:
            avertissements.append(f'{chemin.name} illisible : {e}')
            continue
        lessons = data.get('lessons', []) if isinstance(data, dict) else data
        intro = (data.get('intro') or {}) if isinstance(data, dict) else {}

        sujet = sujets.get(data.get('subject') or '', {})
        niveau = niveaux.get(data.get('level') or '', {})
        sujet_fr = sujet.get('titleFr') or data.get('subjectAr') or data.get('subject') or ''
        sujet_ar = sujet.get('labelAr') or data.get('subjectAr') or ''
        sujet_id = data.get('subject') or ''
        niveau_fr = niveau.get('shortFr') or niveau.get('labelFr') or data.get('levelAr') or ''
        niveau_id = data.get('level') or ''
        niveau_ar = niveau.get('labelAr') or data.get('levelAr') or ''
        cycle = niveau.get('cycle') or 'autre'
        annee = niveau.get('year') or 0

        # introduction
        intro_fr = (intro.get('htmlFr') or '').strip()
        intro_ar = (intro.get('html') or '').strip()
        entree_intro = None
        if intro_fr or intro_ar:
            entree_intro = {
                'titreFr': (intro.get('titleFr') or '').strip() or 'Présentation du manuel',
                'titreAr': (intro.get('titleAr') or '').strip(),
                'htmlFr': intro_fr,
                'htmlAr': intro_ar,
                'texte': texte_plain(intro_fr or intro_ar),
                'docId': (intro.get('docId') or '').strip(),
            }

        # leçons
        lecons = []
        vus = set()
        for i, l in enumerate(lessons):
            did = str(l.get('docId') or '').strip()
            if not did:
                avertissements.append(f'{slug} : leçon {i + 1} sans docId — ignorée')
                continue
            if did in vus:
                avertissements.append(f'{slug} : docId en double {did} — seconde occurrence ignorée')
                continue
            vus.add(did)
            fr = l.get('htmlFr') or ''
            ok = bool(fr.strip())
            lecons.append({
                'docId': did,
                'num': i + 1,
                'titleFr': (l.get('titleFr') or '').strip(),
                'titleAr': (l.get('titleAr') or '').strip(),
                'pdfUrl': (l.get('pdfUrl') or '').strip(),
                'ok': ok,
                'htmlFr': fr if ok else '',
                'texte': texte_plain(fr) if ok else '',
            })

        livres.append({
            'slug': slug,
            'ordre': rang_manifest.get(slug, 10_000),
            'titleFr': (data.get('titleFr') or '').strip() or slug,
            'titleAr': (data.get('titleAr') or '').strip(),
            'sujetFr': sujet_fr,
            'sujetAr': sujet_ar,
            'sujetId': sujet_id,
            'niveauFr': niveau_fr,
            'niveauId': niveau_id,
            'niveauAr': niveau_ar,
            'cycle': cycle,
            'annee': annee,
            'pdfUrl': (data.get('pdfUrl') or '').strip(),
            'non_publie': bool(data.get('unpublished')),
            'intro': entree_intro,
            'lecons': lecons,
        })

    #Collision « introduction » avec un docId de leçon ?
    for b in livres:
        if any(l['docId'] == 'introduction' for l in b['lecons']):
            avertissements.append(f"{b['slug']} : une leçon occupe déjà le nom « introduction »")
    livres.sort(key=lambda b: (b['ordre'], b['slug']))
    return livres


# Cycles scolaires (ordre de lecture de la bibliothèque) :
# id, libellé court FR, libellé complet FR, libellé AR, couleur, nuance profonde
CYCLES = [
    ('ep', 'Primaire', 'Enseignement primaire', 'السلك الابتدائي العتيق', '#4f611d', '#37430f'),
    ('es', 'Collège', 'Enseignement secondaire collégial', 'السلك الإعدادي العتيق', '#9c4a12', '#5e2c0a'),
    ('tanawi', 'Lycée', 'Enseignement secondaire qualifiant', 'السلك التأهيلي العتيق', '#7a5418', '#4a3210'),
]


def groupes_niveaux(livres):
    """Regroupe les livres par cycle scolaire puis par année.

    Retourne une liste de dictionnaires :
      {id, court, long, ar, couleur, nuit, total, niveaux: [(id, fr, ar, badge, [livres])]}
    Les livres hors des cycles connus (improbable) tombent dans un groupe « Autres ».
    """
    par_cycle = {}
    for b in livres:
        par_cycle.setdefault(b['cycle'], {}).setdefault(b['niveauId'] or 'autre', []).append(b)

    sections = []
    for cid, court, long_fr, ar, coul, nuit in CYCLES:
        nivs = par_cycle.pop(cid, {})
        if not nivs:
            continue
        paires = []
        for nid in sorted(nivs, key=lambda x: (min((b['annee'] for b in nivs[x]), default=0), x)):
            bs = sorted(nivs[nid], key=lambda b: b['ordre'])
            badge = (bs[0]['niveauFr'].split(' ')[0] if bs[0]['niveauFr'] else '') or nid
            paires.append((nid, bs[0]['niveauFr'], bs[0]['niveauAr'], badge, bs))
        sections.append({
            'id': cid, 'court': court, 'long': long_fr, 'ar': ar,
            'couleur': coul, 'nuit': nuit, 'total': sum(len(p[4]) for p in paires),
            'niveaux': paires,
        })
    if par_cycle:  # niveaux ou cycles inattendus — filet de sécurité
        reste = [b for nivs in par_cycle.values() for bs in nivs.values() for b in bs]
        sections.append({
            'id': 'autre', 'court': 'Autres', 'long': 'Autres manuels',
            'ar': 'مصنفات أخرى', 'couleur': '#5c5218', 'nuit': '#3a3210',
            'total': len(reste),
            'niveaux': [('autre', 'Autres', '', '•', sorted(reste, key=lambda b: b['ordre']))],
        })
    return sections


def html_niveau_tete(nfr, nar, badge, compte):
    """En-tête d'un sous-onglet niveau — rendu comme <summary>
    (premier enfant d'un <details class="niveau">)."""
    ar_html = (f'<span class="niveau-ar" dir="rtl" lang="ar">{esc(nar)}</span>'
               if nar else '')
    return (f'<summary class="niveau-tete" title="Déplier / replier ce niveau">'
            f'<span class="niveau-badge" aria-hidden="true">{esc(badge)}</span>'
            f'<span class="niveau-lib"><span class="niveau-fr">{esc(nfr)}</span>{ar_html}</span>'
            f'<span class="niveau-filet" aria-hidden="true"></span>'
            f'<span class="niveau-n">{esc(compte)}</span>'
            f'<span class="niveau-chev" aria-hidden="true">'
            f'<svg viewBox="0 0 24 24" width="15" height="15" fill="none" '
            f'stroke="currentColor" stroke-width="2.6" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
            f'</span>'
            f'<span class="hors-ecran">— appuyer pour déplier ou replier ce niveau</span>'
            f'</summary>')


def html_niveau_accordeon(nid, nfr, nar, badge, bs, rel):
    """Sous-onglet rétractable d'un niveau scolaire : <details class="niveau">
    imbriqué dans le <details class="cycle"> de sa série. Refermé par défaut,
    il reste très compact ; les cartes restent dans le DOM (accessibilité,
    recherche navigateur, impression via JS)."""
    compte = f'{len(bs)} manuel{"s" if len(bs) > 1 else ""}'
    return (f'<details class="niveau" id="niveau-{esc(nid)}" data-niveau="{esc(nid)}">\n'
            + html_niveau_tete(nfr, nar, badge, compte) + '\n'
            + '<div class="niveau-corps">\n' + html_cartes(bs, rel) + '\n</div>\n'
            + '</details>')


def style_cycle(sec):
    """Variables CSS de la palette du cycle — posées sur <details class="cycle">
    pour que les sous-onglets niveaux (badges) héritent de la couleur."""
    return f'--cycle:{sec["couleur"]};--cycle-nuit:{sec["nuit"]}'


def html_cycle_bande(sec, indice=None):
    """Bandeau d'un cycle — rendu comme <summary> (onglet rétractable,
    premier enfant d'un <details class="cycle">). Les couleurs viennent des
    variables posées par style_cycle() sur le <details> parent."""
    niveaux_l = ' · '.join(esc(p[1]) for p in sec['niveaux'])
    med = (f'<span class="cycle-medaille" aria-hidden="true">{indice}</span>' if indice
           else '')
    chev = (f'<span class="cycle-chev" aria-hidden="true">'
            f'<svg viewBox="0 0 24 24" width="19" height="19" fill="none" '
            f'stroke="currentColor" stroke-width="2.6" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
            f'</span>')
    return (f'<summary class="cycle-tete" title="Déplier / replier cette série">{med}'
            f'<span class="cycle-titres"><h2>{esc(sec["long"])}</h2>'
            f'<p class="cycle-meta">{niveaux_l}</p></span>'
            f'<span class="cycle-ar" dir="rtl" lang="ar">{esc(sec["ar"])}</span>'
            f'<span class="cycle-compte">{sec["total"]} manuel{"s" if sec["total"] > 1 else ""}</span>'
            f'{chev}'
            f'<span class="hors-ecran">— appuyer pour déplier ou replier cette série</span>'
            f'</summary>')


def chaine_navigation(livre):
    """Liste ordonnée des pages navigables : introduction puis leçons transcrites."""
    elements = []
    if livre['intro']:
        elements.append({'type': 'intro', 'url': 'introduction.html', 'label': 'Présentation'})
    for l in livre['lecons']:
        if l['ok']:
            elements.append({'type': 'lecon', 'url': url_lecon(l['docId']) + '.html',
                             'label': f"Leçon {l['num']}", 'lecon': l})
    return elements


# ---------------------------------------------------------------------------
# Gabarits de pages
# ---------------------------------------------------------------------------

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='7' fill='%23333e14'/%3E"
           "%3Crect x='10' y='10' width='12' height='12' fill='%23e8cf9a'/%3E"
           "%3Crect x='10' y='10' width='12' height='12' fill='%23e8cf9a' transform='rotate(45 16 16)'/%3E"
           "%3Ccircle cx='16' cy='16' r='2.6' fill='%23333e14'/%3E%3C/svg%3E")


def entete(rel, programme_ar):
    return f"""<header class="en-tete"><div class="interieur">
<span class="marque"><a href="{rel}index.html"><span class="arabe" dir="rtl" lang="ar">{programme_ar}</span><span class="sous-marque">Manuels de l’enseignement traditionnel — Maroc</span></a></span>
<span class="liens"><a href="{rel}hors-ligne.html">Hors connexion</a><a href="https://github.com/Sounawa/minhaj" target="_blank" rel="noopener">Dépôt GitHub</a></span>
</div></header>"""


def pied(rel, date_fr):
    return f"""<footer class="pied"><div class="interieur">
<p class="pied-orn" aria-hidden="true"><span></span><i></i><i></i><i></i><span></span></p>
<p>Transcription mot à mot et traduction française du curriculum de l’enseignement traditionnel marocain<br>Ministère des Habous et des Affaires islamiques — Royaume du Maroc</p>
<p class="pied-liens"><a href="{rel}ancien-lecteur.html">Ancien lecteur</a><span aria-hidden="true">·</span><a href="https://github.com/Sounawa/minhaj" target="_blank" rel="noopener">Dépôt GitHub</a><span aria-hidden="true">·</span>site statique généré le {date_fr}</p>
</div></footer>"""


def bootstrap_recherche_racine(fragments):
    """Chargeur progressif de la recherche (accueil) : l'index léger des
    titres est chargé à la première frappe — résultats immédiats — puis les
    fragments de texte complet (par cycle) arrivent en arrière-plan et
    enrichissent les résultats sans nouvelle action de l'utilisateur."""
    liste = json.dumps(fragments, ensure_ascii=False)
    return """<script src="recherche.js"></script>
<script>
(function(){
var frags=""" + liste + r""";
var restants=frags.length;
var input=document.getElementById('champ');
function majStatut(txt){
var s=document.getElementById('statut');
if(!s)return;
s.hidden=!txt;s.textContent=txt||'';
}
window.__minhajRechercheUI=MinhajRecherche.installerUI({
input:input,
conteneur:document.getElementById('resultats'),
statut:document.getElementById('statut'),
chargerIndex:function(suivant,echec){
var t=document.createElement('script');
t.src='recherche/index-titres.js';
t.onload=function(){
if(!window.MINHAJ_INDEX){if(echec)echec('Index illisible.');return;}
MinhajRecherche.definirDonnees(window.MINHAJ_INDEX);window.MINHAJ_INDEX=null;suivant();
/* texte complet en arrière-plan : chaque fragment enrichit les résultats */
frags.forEach(function(src){
var s=document.createElement('script');
s.src=src;
s.onload=function(){
var pile=window.MINHAJ_TEXTE;window.MINHAJ_TEXTE=null;
if(pile)MinhajRecherche.ajouterTexte(pile);
restants--;
if(restants&&input.value.trim().length>=2)
majStatut('Résultats des titres affichés — texte complet en cours ('+(frags.length-restants)+'/'+frags.length+')…');
else majStatut('');
var ui=window.__minhajRechercheUI;ui&&ui.lancer();
};
s.onerror=function(){restants--;majStatut('');};
document.head.appendChild(s);
});
};
t.onerror=function(){if(echec)echec();};
document.head.appendChild(t);
}
});
})();
</script>"""


def coquille(titre, description, rel, programme_ar, date_fr, corps, scripts_html=''):
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#2a340c">
<meta name="generator" content="minhaj-build {date_fr}">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Noto+Naskh+Arabic:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}assets/style.css">
</head>
<body>
{entete(rel, programme_ar)}
{corps}
{pied(rel, date_fr)}
{scripts_html}
</body>
</html>
"""


def carte_livre(b, href):
    n_total = len(b['lecons'])
    n_ok = sum(1 for l in b['lecons'] if l['ok'])
    pct = round(100 * n_ok / n_total) if n_total else 0
    classe = 'fait' if n_ok else 'a-faire'
    return f"""<span class="carte-cadre" data-sujet="{esc(b.get('sujetId') or '')}"><a class="carte {classe}" href="{href}">
<span class="puces"><span class="chip chip-sujet">{esc(b['sujetFr'])}</span></span>
<span class="t-ar" dir="rtl" lang="ar">{esc(b['titleAr'])}</span>
<span class="t-fr">{esc(b['titleFr'])}</span>
<span class="carte-pied"><span class="compte">{n_ok} / {n_total} leçons transcrites</span>
<span class="mini-barre" aria-hidden="true"><span style="width:{pct}%"></span></span></span>
</a></span>"""


def grille_cartes(livres, hrefs):
    return '<section class="grille">\n' + '\n'.join(
        carte_livre(b, h) for b, h in zip(livres, hrefs)) + '\n</section>'


def html_cartes(livres, rel):
    hrefs = [f'{rel}livres/{b["slug"]}/' for b in livres]
    return grille_cartes(livres, hrefs)


def html_recherche():
    return """<section class="recherche" id="recherche">
<label class="hors-ecran" for="champ">Rechercher dans les leçons transcrites</label>
<input id="champ" type="search" autocomplete="off"
       placeholder="Rechercher dans les leçons transcrites — français ou arabe…">
<p id="statut" class="statut" hidden></p>
<div id="resultats" class="resultats" aria-live="polite"></div>
</section>"""


def nav_cycle_html(sections):
    """Barre d'onglets collante : un onglet par cycle (avec effectif) +
    bouton « tout déplier / replier ». Clic = ouvre la série demandée et
    referme les autres (comportement accordéon, géré par BOOTSTRAP_ACCUEIL)."""
    liens = []
    for sec in sections:
        liens.append(
            f'<a href="#cycle-{esc(sec["id"])}" data-cible="cycle-{esc(sec["id"])}" '
            f'style="--nav-coul:{sec["couleur"]};--nav-coul-f:{sec["nuit"]}">'
            f'<i aria-hidden="true"></i>{esc(sec["court"])}'
            f'<b class="nav-n">{sec["total"]}</b></a>')
    return ('<nav class="cycle-nav" aria-label="Niveaux scolaires"><div class="interieur">'
            '<span class="nav-titre">Choisir une série :</span>'
            + ''.join(liens) +
            '<button type="button" id="bascule-tout" class="nav-tout" '
            'aria-pressed="false">Tout déplier</button>'
            '</div></nav>')


BOOTSTRAP_ACCUEIL = r"""<script>
(function(){
'use strict';
var nav=document.querySelector('.cycle-nav');
var cycles=[].slice.call(document.querySelectorAll('details.cycle'));
var niveaux=[].slice.call(document.querySelectorAll('details.niveau'));
var repliables=cycles.concat(niveaux);
var bouton=document.getElementById('bascule-tout');
var memo=false;
try{memo=!!window.sessionStorage;}catch(e){memo=false;}
function maj(){
  cycles.forEach(function(c){
    var t=nav?nav.querySelector('a[data-cible="'+c.id+'"]'):null;
    if(t){if(c.open){t.setAttribute('data-ouvert','');}else{t.removeAttribute('data-ouvert');}}
  });
  if(bouton){
    var tous=repliables.length>0&&repliables.every(function(d){return d.open;});
    bouton.textContent=tous?'Tout replier':'Tout déplier';
    bouton.setAttribute('aria-pressed',tous?'true':'false');
  }
  if(memo){try{
    sessionStorage.setItem('minhaj-cycles',
      cycles.filter(function(c){return c.open;}).map(function(c){return c.id;}).join(','));
    sessionStorage.setItem('minhaj-niveaux',
      niveaux.filter(function(n){return n.open;}).map(function(n){return n.id;}).join(','));
  }catch(e){}}
}
function ouvrirSeul(cible){
  cycles.forEach(function(c){c.open=(c===cible);});
  maj();
}
repliables.forEach(function(d){d.addEventListener('toggle',maj);});
if(nav){
  nav.addEventListener('click',function(ev){
    var a=ev.target&&ev.target.closest?ev.target.closest('a[data-cible]'):null;
    if(!a)return;
    var cible=document.getElementById(a.getAttribute('data-cible'));
    if(!cible)return;
    ev.preventDefault();
    var ouverts=cycles.filter(function(c){return c.open;});
    if(cible.open&&ouverts.length===1){cible.scrollIntoView({behavior:'smooth',block:'start'});return;}
    ouvrirSeul(cible);
    if(history.replaceState)history.replaceState(null,'','#'+cible.id);
    cible.scrollIntoView({behavior:'smooth',block:'start'});
  });
}
if(bouton){
  bouton.addEventListener('click',function(){
    var tous=repliables.length>0&&repliables.every(function(d){return d.open;});
    repliables.forEach(function(d){d.open=!tous;});
    maj();
    if(nav){
      if(tous){nav.scrollIntoView({behavior:'smooth',block:'start'});}
      else{window.scrollTo({top:0,behavior:'smooth'});}
    }
  });
}
function ouvrirAncetres(el){
  var d=el;
  while(d){
    if(d.tagName==='DETAILS'&&!d.open)d.open=true;
    d=d.parentElement&&d.parentElement.closest?d.parentElement.closest('details'):null;
  }
}
function traiterAncre(){
  var id;
  try{id=decodeURIComponent((location.hash||'').slice(1));}catch(e){id=(location.hash||'').slice(1);}
  if(!id)return;
  var el=document.getElementById(id);
  if(!el)return;
  ouvrirAncetres(el);
  maj();
  setTimeout(function(){el.scrollIntoView({behavior:'smooth',block:'start'});},80);
}
window.addEventListener('hashchange',traiterAncre);
window.addEventListener('beforeprint',function(){repliables.forEach(function(d){d.open=true;});maj();});
if(memo&&!location.hash){
  try{
    ['minhaj-cycles','minhaj-niveaux'].forEach(function(cle){
      var memoStr=sessionStorage.getItem(cle)||'';
      if(memoStr){memoStr.split(',').forEach(function(id){
        var d=document.getElementById(id);if(d)d.open=true;});}
    });
  }catch(e){}
}
maj();
traiterAncre();
})();
</script>"""


def page_accueil(livres, programme, date_fr, fragments_recherche):
    n_total = sum(len(b['lecons']) for b in livres)
    n_ok = sum(1 for b in livres for l in b['lecons'] if l['ok'])
    pct = round(100 * n_ok / n_total) if n_total else 0
    nom_ar = programme.get('nameAr', 'المنهج النموذجي للتعليم العتيق')
    nom_fr = programme.get('nameFr') or 'Programme modèle de l’enseignement traditionnel'
    editeur_fr = programme.get('publisherFr') or 'Ministère des Habous et des Affaires islamiques — Royaume du Maroc'

    # ---- bibliothèque rangée par cycle scolaire puis par année
    #      chaque cycle est un onglet rétractable (details/summary) et chaque
    #      niveau un sous-onglet imbriqué (details.niveau) : trois clics
    #      maximum pour atteindre les cartes, l'accueil reste compact.
    sections = groupes_niveaux(livres)
    sections_html = []
    for i, sec in enumerate(sections, start=1):
        niveaux_html = []
        for nid, nfr, nar, badge, bs in sec['niveaux']:
            niveaux_html.append(html_niveau_accordeon(nid, nfr, nar, badge, bs, ''))
        sections_html.append(
            f'<details class="cycle" id="cycle-{esc(sec["id"])}" data-cycle="{esc(sec["id"])}" style="{style_cycle(sec)}">\n'
            + html_cycle_bande(sec, indice=i) + '\n'
            + '<div class="cycle-corps">\n' + '\n'.join(niveaux_html) + '\n</div>\n</details>')

    corps = f"""<section class="heros pleine" id="accueil">
<div class="heros-interieur">
<p class="surline">{esc(nom_fr)} — {esc(editeur_fr)}</p>
<h1><span class="arabe" dir="rtl" lang="ar">{esc(nom_ar)}</span></h1>
<p class="sous">Collection de {len(livres)} manuels scolaires marocains d’enseignement traditionnel, transcrits mot à mot en arabe et traduits ou commentés en français, leçon par leçon — rangés ici du primaire au lycée.</p>
<div class="ornement" aria-hidden="true"><span></span><i></i><i></i><i></i><span></span></div>
<div class="stats">
<div class="stat"><b>{len(livres)}</b><span>manuels</span></div>
<div class="stat"><b>{n_ok}</b><span>leçons transcrites</span></div>
<div class="stat"><b>{pct} %</b><span>du corpus</span></div>
</div>
<div class="prog"><div class="barre"><span style="width:{pct}%"></span></div>
<p class="compte"><strong>{n_ok} / {n_total}</strong> leçons transcrites · mise à jour : {date_fr}</p></div>
{html_recherche()}
</div>
</section>
{nav_cycle_html(sections)}
<main>
{''.join(sections_html)}
</main>"""
    return coquille(
        'Minhaj — manuels de l’enseignement traditionnel (Maroc)',
        'Sommaire des 64 manuels du المنهج النموذجي للتعليم العتيق, rangés par niveau scolaire (primaire, collège, lycée) : leçons transcrites mot à mot en arabe, traduites et commentées en français. Recherche globale en français et en arabe.',
        '', nom_ar, date_fr, corps,
        bootstrap_recherche_racine(fragments_recherche) + '\n' + BOOTSTRAP_ACCUEIL), n_ok, n_total


def html_liste_lecons(livre):
    items = []
    if livre['intro']:
        it = livre['intro']
        ar = f'<span class="t-ar" dir="rtl" lang="ar">{esc(it["titreAr"])}</span>' if it['titreAr'] else ''
        lib = f'<span class="libelles">{ar}<span class="t-fr">{esc(it["titreFr"])}</span></span>'
        items.append(f'<li class="intro-l fait"><a href="introduction.html"><span class="badge" aria-hidden="true">✦</span>{lib}</a></li>')
    for l in livre['lecons']:
        badge = f'<span class="badge" aria-hidden="true">{l["num"]}</span>'
        ar = f'<span class="t-ar" dir="rtl" lang="ar">{esc(l["titleAr"])}</span>' if l['titleAr'] else ''
        fr = f'<span class="t-fr">{esc(l["titleFr"])}</span>' if l['titleFr'] else ''
        lib = f'<span class="libelles">{ar}{fr}</span>'
        pdf = f'<a class="pdf" href="{esc(l["pdfUrl"])}" target="_blank" rel="noopener">PDF officiel</a>' if l['pdfUrl'] else ''
        if l['ok']:
            items.append(f'<li class="fait"><a href="{url_lecon(l["docId"])}.html">{badge}{lib}</a></li>')
        else:
            items.append(f'<li class="a-faire"><span class="ligne-lecon">{badge}{lib}{pdf}</span></li>')
    return '<ol class="lecons">\n' + '\n'.join(items) + '\n</ol>' 


def page_sommaire_livre(livre, programme_ar, date_fr):
    n_total = len(livre['lecons'])
    n_ok = sum(1 for l in livre['lecons'] if l['ok'])
    pct = round(100 * n_ok / n_total) if n_total else 0
    pdf_chip = (f'<a class="chip chip-lien" href="{esc(livre["pdfUrl"])}" target="_blank" rel="noopener">PDF du manuel</a>'
                if livre['pdfUrl'] else '')
    fil = (f'<nav class="fil"><a href="../../index.html">Accueil</a><span class="sep">›</span>'
           f'<a href="../../index.html#cycle-{esc(livre["cycle"])}">{esc({c[1]: c[1] for c in CYCLES}.get(livre["cycle"], "Bibliothèque"))}</a><span class="sep">›</span>'
           f'<a href="../../index.html#niveau-{esc(livre["niveauId"])}">{esc(livre["niveauFr"])}</a><span class="sep">›</span>'
           f'<span>{esc(livre["titleFr"])}</span></nav>') if livre['cycle'] in {c[0] for c in CYCLES} else (
           f'<nav class="fil"><a href="../../index.html">Accueil</a><span class="sep">›</span>'
           f'<span>{esc(livre["titleFr"])}</span></nav>')
    corps = f"""<main>
{fil}
<header class="livre-tete" data-sujet="{esc(livre['sujetId'] or '')}">
<p class="puces"><span class="chip chip-sujet">{esc(livre['sujetFr'])}</span><span class="chip">{esc(livre['niveauFr'])}</span>{pdf_chip}</p>
<h1><span class="arabe" dir="rtl" lang="ar">{esc(livre['titleAr'])}</span></h1>
<p class="t-fr">{esc(livre['titleFr'])}</p>
<div class="ornement" aria-hidden="true"><span></span><i></i><i></i><i></i><span></span></div>
<div class="prog"><div class="barre"><span style="width:{pct}%"></span></div>
<p class="compte"><strong>{n_ok} / {n_total}</strong> leçons transcrites</p></div>
</header>
{html_liste_lecons(livre)}
</main>"""
    description = (f"{livre['titleFr']} ({livre['sujetFr']}, {livre['niveauFr']}) : "
                   f"{n_ok} leçons transcrites sur {n_total}, transcription mot à mot en arabe et traduction française.")
    return coquille(
        f"{livre['titleFr']} — sommaire | Minhaj",
        esc(description), '../../', programme_ar, date_fr, corps)


def html_pn(prec, suiv, url_sommaire):
    def bloc(el, cote):
        if el:
            rel_attr = ' rel="prev"' if cote == 'prec' else ' rel="next"'
            fleche = '←' if cote == 'prec' else '→'
            return (f'<a class="pn-{cote}" href="{el["url"]}"{rel_attr}>'
                    f'<span class="pn-l">{"Précédent" if cote == "prec" else "Suivant"}</span>'
                    f'<span class="pn-t">{fleche} {esc(el["label"])}</span></a>')
        texte = 'Début du livre' if cote == 'prec' else 'Fin des pages transcrites'
        return f'<span class="pn-vide"><span class="pn-l">{"Précédent" if cote == "prec" else "Suivant"}</span><span class="pn-t">{texte}</span></span>'

    return (f'<nav class="pn" aria-label="Navigation entre les leçons">{bloc(prec, "prec")}'
            f'<a class="pn-sommaire" href="{url_sommaire}">Sommaire du livre</a>'
            f'{bloc(suiv, "suiv")}</nav>')


def page_lecon(livre, lecon, prec, suiv, programme_ar, date_fr):
    titre_page = f"Leçon {lecon['num']} — {livre['titleFr']} | Minhaj"
    description = texte_plain(lecon['htmlFr'])[:160].strip()
    fil_niveau = (f'<a href="../../index.html#niveau-{esc(livre["niveauId"])}">{esc(livre["niveauFr"])}</a><span class="sep">›</span>'
                  if livre['niveauId'] else '')
    fil = (f'<nav class="fil"><a href="../../index.html">Accueil</a><span class="sep">›</span>'
           f'{fil_niveau}'
           f'<a href="index.html">{esc(livre["titleFr"])}</a><span class="sep">›</span>'
           f'<span>Leçon {lecon["num"]}</span></nav>')
    corps = f"""<main class="lecture">
{fil}
<article class="contenu">
{lecon['htmlFr']}
</article>
{html_pn(prec, suiv, 'index.html')}
</main>"""
    return coquille(esc(titre_page), esc(description), '../../', programme_ar, date_fr, corps)


def page_introduction(livre, suiv, programme_ar, date_fr):
    it = livre['intro']
    if it['htmlFr']:
        contenu = it['htmlFr']
    else:
        contenu = f'<div class="intro-arabe" dir="rtl" lang="ar">\n{it["htmlAr"]}\n</div>'
    # Titre h1 garanti sur chaque page d'introduction (accessibilité / hiérarchie)
    # — seulement si le contenu n'en apporte pas déjà un.
    if '<h1' not in contenu.lower():
        titre_h1 = esc(it['titreFr'] or 'Présentation du manuel')
        contenu = f'<h1>{titre_h1}</h1>\n{contenu}'
    fil_niveau = (f'<a href="../../index.html#niveau-{esc(livre["niveauId"])}">{esc(livre["niveauFr"])}</a><span class="sep">›</span>'
                  if livre['niveauId'] else '')
    fil = (f'<nav class="fil"><a href="../../index.html">Accueil</a><span class="sep">›</span>'
           f'{fil_niveau}'
           f'<a href="index.html">{esc(livre["titleFr"])}</a><span class="sep">›</span>'
           f'<span>{esc(it["titreFr"])}</span></nav>')
    corps = f"""<main class="lecture">
{fil}
<article class="contenu">
{contenu}
</article>
{html_pn(None, suiv, 'index.html')}
</main>"""
    description = f"Présentation du manuel « {livre['titleFr']} » ({livre['sujetFr']}, {livre['niveauFr']})."
    return coquille(f"{esc(it['titreFr'])} — {esc(livre['titleFr'])} | Minhaj",
                    esc(description), '../../', programme_ar, date_fr, corps)


# ---------------------------------------------------------------------------
# Hors-ligne (mono-fichier)
# ---------------------------------------------------------------------------

def polices_inline(depot):
    """Bloc <style> des polices embarquées (base64) pour le hors-ligne, ou None.
    Source : content/fonts/google-fonts.css + fichiers woff2 voisins, récupérés
    une fois par scripts/fetch-polices.py — le build reste hors-ligne."""
    rep = depot / 'content' / 'fonts'
    css = rep / 'google-fonts.css'
    if not css.exists():
        return None
    try:
        texte = css.read_text(encoding='utf-8')
    except Exception:
        return None
    manquants = []

    def remplacer(m):
        nom = m.group(1).rsplit('/', 1)[-1].split('?')[0]
        f = rep / nom
        if not f.exists():
            manquants.append(nom)
            return m.group(0)
        b64 = base64.b64encode(f.read_bytes()).decode('ascii')
        return "src: url(data:font/woff2;base64," + b64 + ") format('woff2');"

    bloc = re.sub(r"src:\s*url\((https://fonts\.gstatic\.com/[^)]+)\)\s*format\('woff2'\)",
                  remplacer, texte)
    if manquants or 'data:font/woff2' not in bloc:
        return None
    return bloc


def page_hors_ligne(livres, programme, css_texte, recherche_js, date_fr, polices=None):
    n_total = sum(len(b['lecons']) for b in livres)
    n_ok = sum(1 for b in livres for l in b['lecons'] if l['ok'])
    pct = round(100 * n_ok / n_total) if n_total else 0
    nom_ar = programme.get('nameAr', 'المنهج النموذجي للتعليم العتيق')
    if polices:
        liens_polices = ('<style id="polices-embarquees">\n' + polices + '\n</style>')
    else:
        liens_polices = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
                         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
                         '<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700'
                         '&family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600'
                         '&family=Noto+Naskh+Arabic:wght@400;500;700&display=swap" rel="stylesheet">')

    # ---- partie 1 : bibliothèque rangée par cycle puis niveau (cartes -> ancres)
    #      cycles en onglets rétractables, niveaux en sous-onglets imbriqués,
    #      comme l'accueil en ligne
    bibli_html = []
    # ---- partie 2 : sections complètes (leçons transcrites), même rangement
    sections = []
    for i, sec in enumerate(groupes_niveaux(livres), start=1):
        # cartes de la bibliothèque
        niveaux_cartes = []
        blocs_cycle = []
        for nid, nfr, nar, badge, bs in sec['niveaux']:
            cartes_n = [carte_livre(b, f'#livre-{b["slug"]}') for b in bs]
            compte_c = f'{len(bs)} manuel{"s" if len(bs) > 1 else ""}'
            niveaux_cartes.append(
                f'<details class="niveau" id="niveau-{esc(nid)}">\n'
                + html_niveau_tete(nfr, nar, badge, compte_c) + '\n'
                + '<div class="niveau-corps">\n'
                + '<section class="grille">\n' + '\n'.join(cartes_n) + '\n</section>\n'
                + '</div>\n</details>')

            # sections complètes de ce niveau
            n_ok_lv = sum(1 for b in bs for l in b['lecons'] if l['ok'])
            compte_l = (f'{len(bs)} livre{"s" if len(bs) > 1 else ""}'
                        f' · {n_ok_lv} leçons transcrites')
            blocs_cycle.append(
                f'<details class="niveau" id="contenu-niveau-{esc(nid)}">\n'
                + html_niveau_tete(nfr, nar, badge, compte_l) + '\n'
                + '<div class="niveau-corps">\n'
                + '\n'.join(section_livre_hl(b) for b in bs) + '\n</div>\n'
                + '</details>')

        bibli_html.append(
            f'<details class="cycle" id="cycle-{esc(sec["id"])}" data-cycle="{esc(sec["id"])}" style="{style_cycle(sec)}">\n'
            + html_cycle_bande(sec, indice=i) + '\n'
            + '<div class="cycle-corps">\n' + '\n'.join(niveaux_cartes) + '\n</div>\n</details>')

        sections.append(
            f'<details class="cycle" id="contenu-cycle-{esc(sec["id"])}" data-cycle="{esc(sec["id"])}" style="{style_cycle(sec)}">\n'
            + html_cycle_bande(sec) + '\n'
            + '<div class="cycle-corps">\n' + '\n'.join(blocs_cycle) + '\n</div>\n</details>')

    bootstrap = r"""(function(){
function indexDepuisDOM(){
var livres=[],lecons=[];
var secs=document.querySelectorAll('section.livre-hl');
for(var i=0;i<secs.length;i++){
var sec=secs[i];
livres.push({s:sec.getAttribute('data-slug'),t:sec.getAttribute('data-titre'),u:'#'+sec.id});
var arts=sec.querySelectorAll('details.lecon');
for(var j=0;j<arts.length;j++){
var art=arts[j];
lecons.push({b:i,d:art.getAttribute('data-docid'),t:art.getAttribute('data-titre'),
u:'#'+art.id,x:(art.textContent||'').replace(/\s+/g,' ').trim()});
}
}
return {books:livres,lecons:lecons};
}
MinhajRecherche.installerUI({
input:document.getElementById('champ'),
conteneur:document.getElementById('resultats'),
statut:document.getElementById('statut'),
chargerIndex:function(suivant,echec){
try{MinhajRecherche.definirDonnees(indexDepuisDOM());suivant();}
catch(e){if(echec)echec(String(e&&e.message||e));}
}
});
function ouvrirAncetres(el){
var d=el;
while(d){
if(d.tagName==='DETAILS')d.open=true;
d=d.parentElement&&d.parentElement.closest?d.parentElement.closest('details'):null;
}
}
function ouvrirAncre(){
var id=decodeURIComponent((location.hash||'').slice(1));
if(!id)return;
var el=document.getElementById(id);
if(!el)return;
ouvrirAncetres(el);
setTimeout(function(){el.scrollIntoView({behavior:'smooth',block:'start'});},80);
}
window.addEventListener('hashchange',ouvrirAncre);
document.addEventListener('click',function(ev){
var a=ev.target.closest?ev.target.closest('a[href^="#"]'):null;
if(!a)return;
var el=document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
if(el){ouvrirAncetres(el);setTimeout(function(){el.scrollIntoView({behavior:'smooth',block:'start'});},80);}
});
window.addEventListener('beforeprint',function(){
var ds=document.querySelectorAll('details');for(var k=0;k<ds.length;k++)ds[k].open=true;
});
ouvrirAncre();
})();"""

    corps = f"""<main>
<section class="heros" id="accueil">
<p class="surline">Consultation hors connexion — fichier unique</p>
<h1><span class="arabe" dir="rtl" lang="ar">{esc(nom_ar)}</span></h1>
<p class="sous">Toute la collection est embarquée dans ce fichier : sommaires rangés par niveau scolaire, leçons transcrites, recherche. Enregistrez-le et ouvrez-le sans connexion.</p>
<div class="prog"><div class="barre"><span style="width:{pct}%"></span></div>
<p class="compte"><strong>{n_ok} / {n_total}</strong> leçons transcrites · {len(livres)} livres · mise à jour : {date_fr}</p></div>
</section>
{html_recherche()}
<h2 class="hors-ligne-partie">Bibliothèque par niveau scolaire</h2>
{''.join(bibli_html)}
<h2 class="hors-ligne-partie">Leçons transcrites</h2>
{''.join(sections)}
</main>"""

    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Minhaj — consultation hors connexion | {esc(nom_ar)}</title>
<meta name="description" content="Variante mono-fichier du site Minhaj : tous les livres et leçons transcrites embarqués, consultable hors connexion (file://).">
<meta name="theme-color" content="#2a340c">
<meta name="generator" content="minhaj-build {date_fr}">
<link rel="icon" href="{FAVICON}">
{liens_polices}
<style>
{css_texte}
</style>
</head>
<body>
{entete('', nom_ar).replace('href="hors-ligne.html"', 'href="#recherche"').replace('href="index.html"', 'href="#accueil"')}
{corps}
{pied('', date_fr)}
<script>
{recherche_js}
</script>
<script>
{bootstrap}
</script>
</body>
</html>
"""


def section_livre_hl(b):
    """Bloc complet d'un livre pour la version hors-ligne (leçons en accordéons)."""
    blocs = []
    if b['intro']:
        it = b['intro']
        contenu = it['htmlFr'] or f'<div class="intro-arabe" dir="rtl" lang="ar">\n{it["htmlAr"]}\n</div>'
        blocs.append(f"""<details class="lecon intro-l" id="lec-{b['slug']}-introduction">
<summary><span class="badge">✦</span><span class="t-ar" dir="rtl" lang="ar">{esc(it['titreAr'])}</span><span class="t-fr">{esc(it['titreFr'])}</span></summary>
<div class="contenu">
{contenu}
</div>
</details>""")
    for l in b['lecons']:
        if not l['ok']:
            continue
        blocs.append(f"""<details class="lecon" id="lec-{b['slug']}-{l['docId']}" data-docid="{esc(l['docId'])}" data-titre="{esc(l['titleFr'] or l['titleAr'])}">
<summary><span class="badge">{l['num']}</span><span class="t-ar" dir="rtl" lang="ar">{esc(l['titleAr'])}</span><span class="t-fr">{esc(l['titleFr'])}</span></summary>
<div class="contenu">
{l['htmlFr']}
</div>
</details>""")
    return f"""<section class="section-livre livre-hl" id="livre-{b['slug']}" data-slug="{b['slug']}" data-titre="{esc(b['titleFr'])}">
<h2><span class="arabe" dir="rtl" lang="ar">{esc(b['titleAr'])}</span> — {esc(b['titleFr'])}</h2>
<p class="meta-l">{esc(b['sujetFr'])} · {esc(b['niveauFr'])} · {sum(1 for l in b['lecons'] if l['ok'])} / {len(b['lecons'])} leçons transcrites · les leçons non transcrites n’apparaissent pas ici (voir le site en ligne).</p>
{''.join(blocs)}
</section>"""


# ---------------------------------------------------------------------------
# Ancien lecteur
# ---------------------------------------------------------------------------

def preparer_ancien_lecteur(texte_spa, prefixe_fetch, lien_retour):
    """Copie de l'ancien lecteur : chemins fetch corrigés + bandeau d'archivage."""
    texte = texte_spa.replace("fetch('content/books/", "fetch('" + prefixe_fetch)
    bandeau = (f'<div class="bandeau">Ancien lecteur (archivé) — le '
               f'<a href="{lien_retour}">site statique complet</a> remplace cette page : '
               f'sommaires par livre, leçons transcrites, recherche globale, version hors connexion.</div>')
    texte = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + bandeau, texte, count=1)
    texte = texte.replace('</head>', BANDEAU_CSS + '\n</head>', 1)
    return texte


# ---------------------------------------------------------------------------
# 404 / robots / sitemap
# ---------------------------------------------------------------------------

def page_404(css_texte, nom_ar, date_fr, base_url):
    script = r"""(function(){
var dossier=location.pathname.slice(0,location.pathname.lastIndexOf('/')+1);
var sous=dossier.split('/').filter(function(x){return x.length;});
var i=sous.indexOf('minhaj');
var profondeur=(i===-1)?0:(sous.length-i-1);
var pref=profondeur>0?new Array(profondeur+1).join('../'):'./';
var c=document.getElementById('retour');
if(c)c.href=pref+'index.html';
})();"""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page introuvable — Minhaj</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#2a340c">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Noto+Naskh+Arabic:wght@400;500;700&display=swap" rel="stylesheet">
<style>
{css_texte}
</style>
</head>
<body>
<div class="bandeau">Erreur 404 — cette adresse n’existe pas sur le site.</div>
<main>
<section class="heros">
<p class="surline">Erreur 404</p>
<h1><span class="arabe" dir="rtl" lang="ar">{esc(nom_ar)}</span></h1>
<div class="ornement" aria-hidden="true"><span></span><i></i><i></i><i></i><span></span></div>
<p class="sous">La page demandée est introuvable. Revenir à l’accueil pour retrouver les 64 livres et leurs leçons transcrites.</p>
<p style="margin-top:20px"><a class="chip chip-lien" id="retour" href="{base_url}" style="font-size:.85rem;padding:8px 20px">← Accueil du Minhaj</a></p>
</section>
</main>
<script>{script}</script>
</body>
</html>
"""


def robots_txt(base):
    return f"""User-agent: *
Allow: /

Sitemap: {base}sitemap.xml
"""


def sitemap_xml(livres, base, date_str):
    lignes = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
              f'<url><loc>{xescape(base)}</loc><lastmod>{date_str}</lastmod></url>']
    for b in livres:
        prefixe = f"{xescape(base)}livres/{b['slug']}/"
        lignes.append(f'<url><loc>{prefixe}</loc><lastmod>{date_str}</lastmod></url>')
        if b['intro']:
            lignes.append(f'<url><loc>{prefixe}introduction.html</loc><lastmod>{date_str}</lastmod></url>')
        for l in b['lecons']:
            if l['ok']:
                lignes.append(f'<url><loc>{prefixe}{url_lecon(l["docId"])}.html</loc><lastmod>{date_str}</lastmod></url>')
    lignes.append('</urlset>')
    return '\n'.join(lignes) + '\n'


# ---------------------------------------------------------------------------
# Programme principal
# ---------------------------------------------------------------------------

def mo_octets(n):
    return f'{n / (1024 * 1024):.1f} Mo'


def main():
    parseur = argparse.ArgumentParser(
        description='Génère le site statique complet du Minhaj dans site/ (Python stdlib).')
    parseur.add_argument('--content', default=None, help='répertoire content/books (défaut : déduit du script)')
    parseur.add_argument('--sortie', default=None, help='répertoire de sortie site/ (défaut : déduit)')
    parseur.add_argument('--base-url', default='https://sounawa.github.io/minhaj/',
                         help='URL publique du site (sitemap, robots)')
    parseur.add_argument('--publier', metavar='RACINE', default=None,
                         help='copie aussi le contenu de site/ à la racine RACINE (publication Pages)')
    parseur.add_argument('--sans-nettoyage', action='store_true',
                         help='ne supprime pas site/ avant génération (débogage)')
    opts = parseur.parse_args()

    repertoire_script = Path(__file__).resolve().parent
    depot = repertoire_script.parent
    rep_books = Path(opts.content) if opts.content else depot / 'content' / 'books'
    sortie = Path(opts.sortie) if opts.sortie else depot / 'site'
    base = opts.base_url if opts.base_url.endswith('/') else opts.base_url + '/'

    # date française
    try:
        from zoneinfo import ZoneInfo
        maintenant = datetime.now(ZoneInfo('Europe/Paris'))
    except Exception:
        maintenant = datetime.now()
    date_fr = maintenant.strftime('%d/%m/%Y').lstrip('0').replace('/0', '/')
    date_str = maintenant.strftime('%Y-%m-%d')
    mois_fr = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet',
               'août', 'septembre', 'octobre', 'novembre', 'décembre']
    date_fr = f"{maintenant.day} {mois_fr[maintenant.month - 1]} {maintenant.year}"

    manifest_path = depot / 'content' / 'manifest.json'
    manifest = {}
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        except Exception as e:
            print(f'! manifest.json illisible ({e}) — ordre alphabétique de secours')

    avertissements = []
    livres = charger_livres(rep_books, manifest, avertissements)
    if not livres:
        print('!! aucun livre trouvé dans', rep_books)
        return 1
    # cycles ayant au moins un document transcrit -> fragments de l'index
    cycles_frag = sorted({(b['cycle'] or 'autre') for b in livres
                          if b['intro'] or any(l['ok'] for l in b['lecons'])})
    fragments_recherche = [f'recherche/index-{c}.js' for c in cycles_frag]
    programme = manifest.get('program', {})
    nom_ar = programme.get('nameAr', 'المنهج النموذجي للتعليم العتيق')

    # ---- préparation du répertoire
    if sortie.exists() and not opts.sans_nettoyage:
        shutil.rmtree(sortie)
    (sortie / 'assets').mkdir(parents=True, exist_ok=True)

    n_pages = 0
    total_lecons = 0
    total_ok = 0
    total_intro = 0

    # ---- accueil
    page, total_ok, total_lecons = page_accueil(livres, programme, date_fr, fragments_recherche)
    (sortie / 'index.html').write_text(page, encoding='utf-8')
    n_pages += 1
    total_intro = sum(1 for b in livres if b['intro'])

    # ---- CSS + moteur de recherche
    (sortie / 'assets' / 'style.css').write_text(CSS, encoding='utf-8')
    (sortie / 'recherche.js').write_text(RECHERCHE_JS, encoding='utf-8')

    # ---- index de recherche pré-généré (découpé : titres puis fragments par cycle)
    entrees_books = []
    entrees_lecons = []
    textes_par_cycle = {}
    for ib, b in enumerate(livres):
        entrees_books.append({'s': b['slug'], 't': b['titleFr'], 'ta': b['titleAr'],
                              'u': f"livres/{b['slug']}/"})
        cyc = b['cycle'] or 'autre'
        if b['intro']:
            it = b['intro']
            entrees_lecons.append({
                'b': ib, 'd': 'introduction',
                't': it['titreFr'], 'ta': it['titreAr'],
                'u': f"livres/{b['slug']}/introduction.html",
                'x': it['texte'],
            })
            textes_par_cycle.setdefault(cyc, []).append(
                {'b': ib, 'd': 'introduction', 'x': it['texte']})
        for l in b['lecons']:
            if not l['ok']:
                continue
            entrees_lecons.append({
                'b': ib, 'd': l['docId'],
                't': l['titleFr'] or l['titleAr'] or f"Leçon {l['num']}",
                'ta': l['titleAr'],
                'u': f"livres/{b['slug']}/{url_lecon(l['docId'])}.html",
                'x': l['texte'],
            })
            textes_par_cycle.setdefault(cyc, []).append(
                {'b': ib, 'd': l['docId'], 'x': l['texte']})
    if sorted(textes_par_cycle) != cycles_frag:
        avertissements.append('cycles sans fragment de texte — incohérence de découpage')
    (sortie / 'recherche').mkdir(exist_ok=True)
    titres_seuls = [{k: v for k, v in e.items() if k != 'x'} for e in entrees_lecons]
    titres_js = ('/* Index léger des titres — pré-généré par scripts/build-site.py — '
                 f'{len(entrees_books)} livres, {len(titres_seuls)} documents (sans texte ; '
                 'les textes arrivent par fragments de cycle). */\n'
                 'window.MINHAJ_INDEX=' +
                 json.dumps({'books': entrees_books, 'lecons': titres_seuls},
                            ensure_ascii=False, separators=(',', ':')) + ';\n')
    (sortie / 'recherche' / 'index-titres.js').write_text(titres_js, encoding='utf-8')
    n_frags = 0
    for cyc in sorted(textes_par_cycle):
        paires = textes_par_cycle[cyc]
        frag_js = (f"/* Fragment de texte complet — cycle {cyc} — {len(paires)} documents — "
                   "pré-généré par scripts/build-site.py. */\n"
                   '(window.MINHAJ_TEXTE=window.MINHAJ_TEXTE||[]).push(' +
                   json.dumps({'cycle': cyc, 'paires': paires},
                              ensure_ascii=False, separators=(',', ':')) + ");\n")
        (sortie / 'recherche' / f'index-{cyc}.js').write_text(frag_js, encoding='utf-8')
        n_frags += 1

    # ---- pages livres / introductions / leçons
    for b in livres:
        rep_livre = sortie / 'livres' / b['slug']
        rep_livre.mkdir(parents=True, exist_ok=True)
        (rep_livre / 'index.html').write_text(page_sommaire_livre(b, nom_ar, date_fr), encoding='utf-8')
        n_pages += 1
        chaine = chaine_navigation(b)
        if b['intro']:
            suiv = chaine[1] if len(chaine) > 1 else None
            (rep_livre / 'introduction.html').write_text(
                page_introduction(b, suiv, nom_ar, date_fr), encoding='utf-8')
            n_pages += 1
        for idx, el in enumerate(chaine):
            if el['type'] != 'lecon':
                continue
            lecon = el['lecon']
            prec = chaine[idx - 1] if idx > 0 else None
            suiv = chaine[idx + 1] if idx + 1 < len(chaine) else None
            (rep_livre / (url_lecon(lecon['docId']) + '.html')).write_text(
                page_lecon(b, lecon, prec, suiv, nom_ar, date_fr), encoding='utf-8')
            n_pages += 1

    # ---- hors-ligne
    bloc_polices = polices_inline(depot)
    page_hl = page_hors_ligne(livres, programme, CSS, RECHERCHE_JS, date_fr, polices=bloc_polices)
    (sortie / 'hors-ligne.html').write_text(page_hl, encoding='utf-8')

    # ---- 404 / robots / sitemap
    (sortie / '404.html').write_text(page_404(CSS, nom_ar, date_fr, base), encoding='utf-8')
    (sortie / 'robots.txt').write_text(robots_txt(base), encoding='utf-8')
    (sortie / 'sitemap.xml').write_text(sitemap_xml(livres, base, date_str), encoding='utf-8')
    (sortie / '.nojekyll').touch(exist_ok=True)

    # ---- ancien lecteur (copie de la SPA d'origine, fetch corrigés)
    # Source : scripts/ancien-lecteur.source.html (copie vierge, pour des
    # reconstructions idempotentes même après publication à la racine) ;
    # à défaut, l'index.html courant s'il est encore l'ancien lecteur.
    spa = depot / 'scripts' / 'ancien-lecteur.source.html'
    texte_spa = None
    if spa.exists():
        texte_spa = spa.read_text(encoding='utf-8')
    else:
        idx_racine = depot / 'index.html'
        if idx_racine.exists() and "fetch('content/books/" in idx_racine.read_text(encoding='utf-8'):
            texte_spa = idx_racine.read_text(encoding='utf-8')
            spa.write_text(texte_spa, encoding='utf-8')
    if texte_spa:
        # depuis site/, content/ est à un niveau : ../content/books/
        (sortie / 'ancien-lecteur.html').write_text(
            preparer_ancien_lecteur(texte_spa, '../content/books/', '../'), encoding='utf-8')
    else:
        avertissements.append('ancien lecteur introuvable — site/ancien-lecteur.html absent')

    # ---- publication à la racine du dépôt (source Pages : main, chemin /)
    n_copies = 0
    if opts.publier:
        racine = Path(opts.publier).resolve()
        if not (racine / 'content').is_dir():
            print(f'!! --publier {racine} : pas de content/ ici, publication annulée')
            return 1
        for chemin in sorted(sortie.rglob('*')):
            cible = racine / chemin.relative_to(sortie)
            if chemin.is_dir():
                cible.mkdir(exist_ok=True)
                continue
            cible.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(chemin, cible)
            n_copies += 1
        if texte_spa:
            # à la racine, les fetch d'origine (content/books/…) sont déjà corrects
            (racine / 'ancien-lecteur.html').write_text(
                preparer_ancien_lecteur(texte_spa, 'content/books/', './'), encoding='utf-8')
        (racine / '.nojekyll').touch(exist_ok=True)
        ancien_index = racine / 'recherche-index.js'
        if ancien_index.exists():
            ancien_index.unlink()

    # ---- rapport
    fichiers_recherche = sorted((sortie / 'recherche').glob('*.js'))
    octets_recherche = sum(p.stat().st_size for p in fichiers_recherche)
    octets_titres = (sortie / 'recherche' / 'index-titres.js').stat().st_size
    taille_hl = (sortie / 'hors-ligne.html').stat().st_size
    print('=== Génération terminée ===')
    print(f'livres : {len(livres)} | leçons : {total_lecons} ({total_ok} transcrites) | introductions : {total_intro}')
    print(f'pages HTML : {n_pages} | fichiers copiés à la racine : {n_copies}')
    print(f'index de recherche : {len(entrees_lecons)} documents en {len(fichiers_recherche)} fichiers '
          f'({mo_octets(octets_recherche)} — titres {mo_octets(octets_titres)} + {n_frags} fragments de texte) '
          f'| hors-ligne : {mo_octets(taille_hl)} | '
          f'polices hors-ligne : {"embarquées" if bloc_polices else "Google Fonts (repli)"}')
    if avertissements:
        print(f'avertissements ({len(avertissements)}) :')
        for a in avertissements[:20]:
            print('  -', a)
    return 0


if __name__ == '__main__':
    sys.exit(main())
