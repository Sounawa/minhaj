#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-35 — re-génère les supports des DEUX relectures VLM en attente (perdues au reset du bac) :
#  (1) bandeau calligraphique p.158 de hadith-5ep (attribution «التَّطْبِيقُ» par parallèle
#      structurel en Z2-33 — bandeau illisible pour tesseract, relecture VLM reportée)
#  (2) glose أَرَأْيْتَ de L27 (pp.150-155, reconstruction «بِمَعْنَى التَّرَوِّي وَالتَّقْدِيرِ»
#      consignée en Z2-32 — les deux derniers mots restent obscurs, réserve w10 perdue)
# Sortie : scripts-ia2/tmp/h5-rereads/
import subprocess, os

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-rereads'
for sub in ('r150', 'r600', 'r1200', 'crops'):
    os.makedirs(f'{OUT}/{sub}', exist_ok=True)

# pp.150-155 = L27 (glose أَرَأْيْتَ), p.156-158 = L28 fin (bandeau p.158)
P150 = list(range(150, 156))   # L27
P158 = [156, 157, 158]         # L28 (bandeau sur 158)

for res in (150, 600, 1200):
    d = f'{OUT}/r{res}'
    todo = P150 if res == 150 else (P150 + P158 if res == 600 else P158)
    for p in todo:
        png = f'{d}/p{p}.png'
        if os.path.exists(png):
            continue
        subprocess.run(['pdftoppm', '-png', '-r', str(res), '-f', str(p), '-l', str(p),
                        SRC, f'{d}/q{p}'], check=True)
        got = [f for f in os.listdir(d) if f.startswith(f'q{p}-')]
        os.rename(f'{d}/{got[0]}', png)
        print(f'{res}dpi p{p} OK')

# couches texte + bbox pour localiser la glose et le bandeau
subprocess.run(['pdftotext', '-f', '150', '-l', '158', SRC, f'{OUT}/textlayer-150-158.txt'], check=True)
subprocess.run(['pdftotext', '-bbox', '-f', '150', '-l', '158', SRC, f'{OUT}/bbox-150-158.html'], check=True)
print('couche texte OK')
