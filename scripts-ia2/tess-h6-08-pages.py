#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-42 — tesseract pleine page 600 dpi (psm 4 + 6) pp.45-50,
# leçon 7 du tirage hadith-6ep «دَعْمٌ وَتَطْبِيقٌ» (docId pdf-mut23h3b-687,
# leçon de consolidation : أنجز في دفتري + نصوص + أسئلة + أنشطة + مشروع العرض).
import subprocess, os

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-08'
TESS = '/home/z/my-project/scripts-translate/tessdata'
for p in range(45, 51):
    for psm in (4, 6):
        out = f'{DIR}/t-p{p}-psm{psm}.txt'
        if os.path.exists(out):
            continue
        subprocess.run(['tesseract', f'{DIR}/r600/p{p}.png', out[:-4], '-l', 'ara',
                        '--tessdata-dir', TESS, '--psm', str(psm)],
                       check=True, capture_output=True)
        print(f'p{p} psm{psm} OK')
print('done')
