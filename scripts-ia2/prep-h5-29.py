#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-34 — prépa leçon 29 hadith-5ep «لائحة المصادر والمراجع» (pp.159-166 présumées,
# bornage À CONFIRMER : p.167 = page de couverture finale, 167 pages au total).
# DERNIÈRE leçon du livre : bibliographie en rubriques, texte NON vocalisé,
# dates hijrī/milādī en chiffres arabo-orientaux — profil de transcription différent
# (tesseract non-vocalisé plus fiable, VLM moins nécessaire).
# L28 s'arrête p.158 (dernières sous-puces تطبيق) → bornage L29 = pp.159-166 attendu.
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-29'
os.makedirs(f'{OUT}/r150', exist_ok=True)
os.makedirs(f'{OUT}/r600', exist_ok=True)
os.makedirs(f'{OUT}/r1200', exist_ok=True)

PAGES = list(range(159, 167))

for res in (150, 600, 1200):
    d = f'{OUT}/r{res}'
    for p in PAGES:
        png = f'{d}/p{p}.png'
        if os.path.exists(png):
            continue
        subprocess.run(['pdftoppm', '-png', '-r', str(res), '-f', str(p), '-l', str(p),
                        SRC, f'{d}/q{p}'], check=True)
        got = [f for f in os.listdir(d) if f.startswith(f'q{p}-')]
        os.rename(f'{d}/{got[0]}', png)
        print(f'{res}dpi p{p} OK')

# textlayer élargi pour vérifier le bornage des DEUX côtés (fin L28 p.158 / début L29 p.159 / p.167 = couverture)
subprocess.run(['pdftotext', '-f', '156', '-l', '167', SRC, f'{OUT}/textlayer-156-167.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '159', '-l', '166', SRC, f'{OUT}/bbox-159-166.html'], check=True)
print('couche texte OK')
