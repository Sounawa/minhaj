#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-40 — tesseract pleine page 600 dpi (psm 4 + 6) pp.36-40,
# leçon 5 du tirage hadith-6ep «الْبِرُّ حُسْنُ الْخُلُقِ» (hadith an-Nawwās b. Samʿān,
# Muslim : «البر حسن الخلق، والإثم ما حاك في نفسك وكرهت أن يطلع عليه الناس»)
import subprocess, os

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-06'
TESS = '/home/z/my-project/scripts-translate/tessdata'
for p in range(36, 41):
    for psm in (4, 6):
        out = f'{DIR}/t-p{p}-psm{psm}.txt'
        if os.path.exists(out):
            continue
        subprocess.run(['tesseract', f'{DIR}/r600/p{p}.png', out[:-4], '-l', 'ara',
                        '--tessdata-dir', TESS, '--psm', str(psm)],
                       check=True, capture_output=True)
        print(f'p{p} psm{psm} OK')
print('done')
