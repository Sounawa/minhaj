#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-41 — tesseract pleine page 600 dpi (psm 4 + 6) pp.41-46,
# leçon 6 du tirage hadith-6ep «لُزُومُ السُّنَّةِ» (hadith al-'Irbāḍ b. Sāriya,
# Abu Dāwūd + Tirmiḏī ḥasan ṣaḥīḥ : «أوصيكم بتقوى الله والسمع والطاعة... عليكم بسنتي»)
import subprocess, os

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-07'
TESS = '/home/z/my-project/scripts-translate/tessdata'
for p in range(41, 47):
    for psm in (4, 6):
        out = f'{DIR}/t-p{p}-psm{psm}.txt'
        if os.path.exists(out):
            continue
        subprocess.run(['tesseract', f'{DIR}/r600/p{p}.png', out[:-4], '-l', 'ara',
                        '--tessdata-dir', TESS, '--psm', str(psm)],
                       check=True, capture_output=True)
        print(f'p{p} psm{psm} OK')
print('done')
