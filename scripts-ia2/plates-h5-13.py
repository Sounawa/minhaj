#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Z2-15 — planches d'adjudication leçon 13 : rendus 600 dpi + composites ciblés
from PIL import Image, ImageDraw
import subprocess, os

BASE = '/home/z/my-project/scripts-ia2/tmp/h5-13'
Z = f'{BASE}/zooms'
os.makedirs(Z, exist_ok=True)

SRC = '/home/z/my-project/content/textbooks-src/hadith-5-ibtidai_text.pdf'

# rendu 600 dpi des pages 74-79
for p in [74, 75, 76, 77, 78, 79]:
    subprocess.run(['pdftoppm', '-png', '-r', '600', '-f', str(p), '-l', str(p), SRC, f'{Z}/big-{p}'], check=True)

def zone(pg, y0, y1, x0, x1, label, scale=1.7):
    im = Image.open(f'{Z}/big-{pg}-0{pg}.png')
    W, H = im.size
    c = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
    tw = int(c.width * scale)
    if tw > 1700:
        tw = 1700
    c = c.resize((tw, int(c.height * tw / c.width)), Image.LANCZOS)
    return (label, c)

def build(crops, out):
    total_h = sum(c.height + 46 for _, c in crops)
    comp = Image.new('RGB', (1720, total_h), 'white')
    d = ImageDraw.Draw(comp)
    y = 0
    for label, c in crops:
        d.rectangle([0, y, 1719, y+40], fill=(230, 240, 230))
        d.text((14, y+10), label, fill=(20, 20, 20))
        y += 44
        comp.paste(c, ((1720-c.width)//2, y))
        y += c.height + 2
    comp.save(out)
    print('OK', out, comp.size, os.path.getsize(out)//1024, 'Ko')

# COMPOSITE A : pages 74-76
build([
    zone(74, 0.115, 0.335, 0.03, 0.99, 'A1. p74 AHDAF (an a-rif? u-dirik? atamaththala mabda-a l-yusri?)'),
    zone(74, 0.315, 0.525, 0.03, 0.99, 'A2. p74 TAMHID (bi-atharin baziratin? bi-nafsihi?)'),
    zone(75, 0.075, 0.36, 0.03, 0.99, 'A3. p75 BIO (aslama amma khaybara? mulazamat tammatan raghbatan fi l-ilmi? sanata ? wa-khamshina?)'),
    zone(75, 0.40, 0.80, 0.03, 0.99, 'A4. p75 SHARH + ISTIKHLAS items'),
    zone(76, 0.28, 0.62, 0.03, 0.99, 'A5. p76 AVVALAN debut (awamiran wa-nawahiya? ma-qdurun li-kulli ahad?)'),
    zone(76, 0.55, 0.95, 0.03, 0.99, 'A6. p76 AMTHILA (arkana s-salati? a-daa l-wudui? yughassilu l-mumkina? al-munkarat?)'),
], f'{Z}/comp-A13.png')

# COMPOSITE B : pages 77-79
build([
    zone(77, 0.045, 0.235, 0.03, 0.99, 'B1. p77 ATHAR + 3 AYAS refs (Baqara? Taghabun 16? Hajj 78?)'),
    zone(77, 0.20, 0.46, 0.03, 0.99, 'B2. p77 mabadi-a l-yusri (iltizam mabadi-a? rifqan bi-l-? / taysiran / tahbiban / ijtinaban li-t-ta-siri?)'),
    zone(77, 0.42, 0.78, 0.03, 0.99, 'B3. p77 NAHYU ANA L-IHTILAF + note grammaticale (bi-dammi l-hai? ma-tuf ala kathrata?) + ayat Al Imran 103'),
    zone(78, 0.045, 0.33, 0.03, 0.99, 'B4. p78 SUB-2 (wajha l-amali? hamulat as-ilata s-sahabati? al-anfala? al-kalalata?)'),
    zone(78, 0.28, 0.50, 0.03, 0.99, 'B5. p78 li-anna kathrata s-su-ali rubbama ... (phrase exacte)'),
    zone(78, 0.84, 0.99, 0.03, 0.99, 'B6. p78 YUSTAFAD item 2 (hadya l-? at-taysiru fi umuri d-dini wa-d-dunya?)'),
    zone(79, 0.03, 0.32, 0.03, 0.99, 'B7. p79 TAQWIM items 1-3 (u-addidu? limada qayyida l-amru ...?)'),
    zone(79, 0.52, 0.82, 0.03, 0.99, 'B8. p79 ISTITHMAR items (ubayyinu? astahdiruha?)'),
    zone(79, 0.80, 0.99, 0.03, 0.99, 'B9. p79 I-DAD QABLI (uawaffifu muktasabati? adillata d-darsi l-qadimi?)'),
], f'{Z}/comp-B13.png')
