#!/usr/bin/env python3
# Z2-3 — crops 300 dpi des zones contestées de la leçon 3 hadith-5ep (pp. 23-30)
# Convention Z2 : bandes depuis le rendu 150 dpi, upscale ×2 LANCZOS (effectif 300 dpi)
from PIL import Image
import os
SRC = '/home/z/my-project/repo-minhaj/scripts-ia2/tmp/h5-01'

# (page, nom, y0, y1) en coordonnées du rendu 150 dpi
BANDS = [
    ('023', 'A-rakibtayh',      1500, 1710),  # فأسند ركبتيه إلى/على ركبتيه
    ('024', 'B-falith',          620,  810),  # ثم انطلق فليث/فلبث مليحا
    ('024', 'C-gloses',          950, 1400),  # gloses : طلع علينا، رجل، أثر السفر، فعجبنا، الإيمان
    ('025', 'D-tahlil',          490,  950),  # كالأم/اللام للسنة + فالإسلام مدخل
    ('025', 'E-awla',            950, 1350),  # الدين السمح المعتدل، الموسوم بال...
    ('026', 'F-iman-def',        230,  440),  # التصديق الجازم بالأمور الستة
    ('026', 'G-iman-billah',     560,  950),  # حق واحد الوجود + أهمية هذا الركن
    ('026', 'H-versets',         930, 1220),  # les deux versets + citations
    ('027', 'I-hafaza',          140,  350),  # حفظة كل لحظة + من الكائنة
    ('027', 'J-kutub',           330,  740),  # ليبينوا لها الناس + بهديها ورسدها
    ('027', 'K-tafarruq',        980, 1240),  # لا تفرقوا بين أحد من رسله + [البقرة]
    ('028', 'L-akhir',           230,  500),  # الأعاذة + وآخر به النبي الأمين
    ('028', 'M-hadid',           910, 1080),  # citation الحديد
    ('028', 'N-silsul',         1130, 1300),  # سيصله + درءه
    ('029', 'O-baraheen',        190,  330),  # الممتني/المبني على البراهين
    ('029', 'P-sul',             670,  980),  # بلسان سؤول + إسناده الصحيح
    ('030', 'Q-badaa',           320,  500),  # بضع وسبعون باباً/شعبة
]

for pg, name, y0, y1 in BANDS:
    im = Image.open(f'{SRC}/p-{pg}.png')
    part = im.crop((0, y0, im.width, y1))
    up = part.resize((part.width * 2, part.height * 2), Image.LANCZOS)
    out = f'{SRC}/z3-{name}.png'
    up.save(out)
    print(name, pg, f'y{y0}-{y1}', up.size, os.path.getsize(out))
