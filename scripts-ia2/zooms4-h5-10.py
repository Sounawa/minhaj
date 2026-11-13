#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-11 — micro-fenêtres 600 dpi natif (1568px = pas de downscale API) — leçon 10
import subprocess, os
from PIL import Image

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'
OUT = '/home/z/my-project/scripts-ia2/tmp/h5-10/zooms4'
os.makedirs(OUT, exist_ok=True)
_cache = {}

def page600(pg):
    if pg not in _cache:
        png = f'{OUT}/p600-{pg}.png'
        if not os.path.exists(png):
            subprocess.run(['pdftoppm', '-png', '-r', '600', '-f', str(pg), '-l', str(pg),
                            SRC, f'{OUT}/tmp600-{pg}'], check=True)
            os.replace(f'{OUT}/tmp600-{pg}-{pg:03d}.png', png)
        _cache[pg] = Image.open(png)
    return _cache[pg]

def crop(pg, y0, y1, x0, x1):
    im = page600(pg); w, h = im.size
    c = im.crop((int(x0*w), int(y0*h), int(x1*w), int(y1*h)))
    if c.size[0] > 1560:
        c = c.resize((1560, int(c.size[1]*1560/c.size[0])), Image.LANCZOS)
    return c

def composite(name, crops):
    W = max(c.size[0] for c in crops)
    H = sum(c.size[1] for c in crops) + 8 * (len(crops) - 1)
    canvas = Image.new('RGB', (W, H), (200, 60, 60))
    y = 0
    for c in crops:
        canvas.paste(c, (0, y)); y += c.size[1] + 8
    canvas.save(f'{OUT}/{name}.png'); print(name, canvas.size)

# G1 — tamhīd (أذن + أشبه) + rāwī (استشهدت + معالية/مغرية + date)
composite('g1', [
    crop(60, 0.405, 0.452, 0.40, 0.74),   # L1 : فإن أذن/أنّ له فعله
    crop(60, 0.445, 0.490, 0.28, 0.62),   # L2 : وأشبه/واشتبه حكمه
    crop(61, 0.292, 0.338, 0.00, 0.34),   # L3 fin : استشهدت
    crop(61, 0.330, 0.378, 0.66, 1.00),   # L4 début : مغرية/معالية رضي الله عنه
    crop(61, 0.370, 0.415, 0.38, 0.74),   # L5 : توفي سنة خمس وس...
])

# G2 — p62 : āyas item 2 + prose وَكَتَحْرِيمِ + entame item 3
composite('g2', [
    crop(62, 0.545, 0.592, 0.32, 0.68),   # حُرِّمَتْ عَلَيْكُمْ أُمَّهَاتُكُمْ
    crop(62, 0.545, 0.592, 0.03, 0.37),   # ...وبناتكُم + [النساء:23]
    crop(62, 0.586, 0.632, 0.32, 0.68),   # قُلْ إِنَّمَا حَرَّمَ رَبِّيَ...
    crop(62, 0.586, 0.632, 0.03, 0.37),   # ...الْفَوَاحِشَ + [ref]
    crop(62, 0.626, 0.672, 0.03, 0.37),   # وَكَتَحْرِيمِ الْفَوَاحِشِ...
    crop(62, 0.692, 0.738, 0.30, 0.70),   # item3 L1 : وجه الْحَاقَة/الْحَقّ
])

# G3 — p62 item 3 (إجماع + athar النمور) + p63 (تنتقف + نقض + إنّ يحمل)
composite('g3', [
    crop(62, 0.728, 0.778, 0.28, 0.66),   # من الكتاب والسنة وإجماع الْمَعَانِي
    crop(62, 0.770, 0.820, 0.08, 0.46),   # لحُمُور/لنُمُور الساقطة جين
    crop(63, 0.294, 0.342, 0.32, 0.68),   # أن تَنْتَقِفَّ/تَنْتَفِكَّ عنها
    crop(63, 0.434, 0.482, 0.28, 0.66),   # وقد نَقُضُ/يَقُودُ بها إلى المحرمات
    crop(63, 0.466, 0.514, 0.02, 0.40),   # إنّ/إنّه يحمل التساهل
])

# G4 — p63 milieu (المرعى المنعو + غالبا + āya + الاقتراب) + التزينة + p64 (ممنون + واتبـع)
composite('g4', [
    crop(63, 0.570, 0.618, 0.12, 0.50),   # وهو الْمَرْعَى الْمَنْعُو مِنْهُ
    crop(63, 0.640, 0.688, 0.32, 0.70),   # خَالَطَهُ غَالِبًا
    crop(63, 0.676, 0.724, 0.32, 0.70),   # وَلَا تُرْكُوا/تَرْكَنُوا إِلَى...
    crop(63, 0.676, 0.724, 0.02, 0.40),   # ...الَّذِينَ ظَلَمُوا + [البقرة:186]
    crop(63, 0.920, 0.968, 0.30, 0.70),   # الدَّعْوَةُ إِلَى التَّزَيُّنِ/التَّزَيِّةِ
    crop(64, 0.464, 0.512, 0.28, 0.68),   # وهو مَمْنُونٌ/مَانِعٌ لا يعلمها
    crop(64, 0.500, 0.552, 0.02, 0.42),   # وَاتَّبَعَ مَا دَلَّ/دَلَّهُ...
])

print('OK zooms4')
