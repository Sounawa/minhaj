#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-40 — dernière vague de zooms (1200 dpi, 4x, psm 7/8/13) sur les derniers mots disputés.
import subprocess, os
from PIL import Image, ImageOps

DIR = '/home/z/my-project/scripts-ia2/tmp/h6-06'
TESS = '/home/z/my-project/scripts-translate/tessdata'
S = 1200 / 72.0
os.makedirs(f'{DIR}/zooms', exist_ok=True)

Z = [
    ('f1-cite-head', 38, 76, 106, 430, 565, 'premier(s) mot(s) citation (كالبر/قال/كما قال؟)'),
    ('f2-tail37', 37, 695, 735, 60, 420, 'fin p37: مرضي + هو في ت؟ية النفس'),
    ('f3-khuzayma', 37, 229, 251, 415, 470, 'خزيمة (ز ?)'),
    ('f4-islah1', 39, 448, 472, 355, 405, 'إصلاح 1er'),
    ('f5-sifat-ctl', 38, 407, 433, 130, 210, 'TEMOIN صفات (ص) même conditions'),
    ('f6-qabil-gap', 38, 706, 736, 433, 455, 'gap entre قابل et بينهما'),
    ('f7-lahu', 37, 255, 278, 400, 520, 'وله ? أحاديث'),
    ('f8-naam', 36, 630, 654, 360, 470, 'قلت نعم'),
    ('f9-ruwah', 36, 602, 624, 260, 470, '[رواه مسلم]'),
    ('f10-darami', 36, 697, 720, 135, 215, 'والدرامي (ordre lettres)'),
    ('f11-madud', 37, 141, 164, 428, 468, 'معدود'),
    ('f12-birr', 37, 663, 692, 330, 470, 'يبر به فاعله'),
    ('f13-muwalī', 40, 625, 655, 290, 420, 'الدرس الموالي (final ي/ى)'),
    ('f14-baka', 37, 258, 280, 105, 260, 'وكان قارئا... بكاء'),
]

for tag, pg, y0, y1, x0, x1, note in Z:
    im = Image.open(f'{DIR}/r1200/p{pg}.png').convert('L')
    c = im.crop((int(x0*S), int(y0*S), int(x1*S), int(y1*S)))
    c = ImageOps.autocontrast(c)
    print(f'===== {tag} — {note} =====')
    for vn, scale in (('x4', 4), ('x6', 6)):
        img = c.resize((c.width*scale, c.height*scale), Image.LANCZOS)
        fp = f'{DIR}/zooms/{tag}-{vn}.png'
        img.save(fp)
        for psm in (7, 8, 13):
            base = f'{DIR}/zooms/{tag}-{vn}'
            subprocess.run(['tesseract', fp, base, '-l', 'ara', '--tessdata-dir', TESS,
                            '--psm', str(psm)], capture_output=True)
            txt = open(base + '.txt', encoding='utf-8').read().strip()
            if txt and len(txt) > 1:
                print(f'  [{vn} psm{psm}] {txt[:130]}')
