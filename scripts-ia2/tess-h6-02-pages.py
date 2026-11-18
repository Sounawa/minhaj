#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-36 — tesseract pleine page 600 dpi (psm 4 + 6) pp.11-16,
# leçon 1 du tirage hadith-6ep «المسارعة في الخيرات» (texte vocalisé)
import subprocess, os

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-02'
TESS = '/home/z/my-project/scripts-translate/tessdata'
for p in range(11, 17):
    for psm in (4, 6):
        out = f'{DIR}/t-p{p}-psm{psm}.txt'
        if os.path.exists(out):
            continue
        subprocess.run(['tesseract', f'{DIR}/r600/p{p}.png', out[:-4], '-l', 'ara',
                        '--tessdata-dir', TESS, '--psm', str(psm)],
                       check=True, capture_output=True)
        print(f'p{p} psm{psm} OK')
print('done')
