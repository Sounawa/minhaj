#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-34 — tesseract pleine page 600 + 1200 dpi (psm 4 + 6) pp.159-166,
# leçon 29 «لائحة المصادر والمراجع» (bibliographie, texte NON vocalisé)
import subprocess, os

DIR = '/home/z/my-project/scripts-ia2/tmp/h5-29'
TESS = '/home/z/my-project/scripts-translate/tessdata'
for p in range(159, 167):
    for psm in (4, 6):
        out = f'{DIR}/t-p{p}-psm{psm}.txt'
        if os.path.exists(out):
            continue
        subprocess.run(['tesseract', f'{DIR}/r600/p{p}.png', out[:-4], '-l', 'ara',
                        '--tessdata-dir', TESS, '--psm', str(psm)],
                       check=True, capture_output=True)
        print(f'p{p} psm{psm} OK')

for p in range(159, 167):
    for psm in (4, 6):
        out = f'{DIR}/t1200-p{p}-psm{psm}.txt'
        if os.path.exists(out):
            continue
        subprocess.run(['tesseract', f'{DIR}/r1200/p{p}.png', out[:-4], '-l', 'ara',
                        '--tessdata-dir', TESS, '--psm', str(psm)],
                       check=True, capture_output=True)
        print(f'1200 p{p} psm{psm} OK')
print('done')
