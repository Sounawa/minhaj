#!/bin/bash
# R622 takeover — recadrages manquants leçon 9 (pdf-mut23h2u-263, p.52-56)
# Reprise du WIP sous-agent interrompu (claim expiré 69 min) — méthode R621 :
# nombres miroir tranchés par image directe, jamais devinés.
cd /home/z/my-project || exit 1
# ADJ27 : p.54 y185-275 — exemple نكارة الإسناد (isnād + hadith + citation العلل 359/5)
bash tr-tmp/ocr263.sh 54 185 275 0 612 ADJ27-takeover-isnad 1200
# ADJ30 : p.54 y603-632 — zoom citation النكت 680/2
bash tr-tmp/ocr263.sh 54 603 632 60 500 ADJ30-takeover-nukat2-cite 1800
# ADJ31 : p.55 y206-236 — zoom citation مقدمة ابن الصلاح
bash tr-tmp/ocr263.sh 55 206 236 60 520 ADJ31-takeover-muqaddima-cite 1800
# ADJ32 : p.55 y455-522 — rubrique التقييم, items 1-2
bash tr-tmp/ocr263.sh 55 455 522 0 612 ADJ32-takeover-takyif 1200
# ADJ34 : p.53 y562-604 — titre de section الفرق/العلاقة بين المنكر والشاذ
bash tr-tmp/ocr263.sh 53 562 604 0 612 ADJ34-takeover-relation-title 1200
# ADJ35 : p.53 y183-215 — zoom ligne المفردات (lecture «لاؤثره»?)
bash tr-tmp/ocr263.sh 53 183 215 0 612 ADJ35-takeover-mufradat-line 1800
