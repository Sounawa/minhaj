#!/usr/bin/env python3
# r623 — crops d'adjudication pour la leçon 10 (ulum-hadith-tanawi-2, pages PDF 57-62)
# Génère des recadrages 600/900 dpi dans tr-tmp/r623-crops/ à partir du PDF source.
import fitz, os

PDF = 'content/textbooks-src/ulum-hadith-2-thanawi_text.pdf'
OUT = 'tr-tmp/r623-crops'
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

# (nom, page_pdf_1based, x0, y0, x1, y1, dpi) — coordonnées en points PDF (595x842)
CROPS = [
    # p57 : bannière + boîte objectifs
    ('ADJ1-p57-header-objectifs', 57, 30, 60, 565, 235, 900),
    # p57 : boîte du matn (citation Ibn Ḥaǧar) + question introductive
    ('ADJ2-p57-matn', 57, 30, 340, 565, 560, 900),
    # p57 : šarḥ + istiḫrāǧ al-maḍāmīn (bas de page)
    ('ADJ3-p57-sharh-istikhradj', 57, 30, 545, 565, 800, 600),
    # p58 : définition lugha/istiṣlāḥ + renvoi Maqāyīs
    ('ADJ4-p58-mutaba-lugha', 58, 30, 60, 565, 300, 900),
    # p58 : exemple Šāfiʿī al-Umm + renvoi 2/301|103
    ('ADJ5-p58-umm-ref', 58, 30, 300, 565, 560, 900),
    # p58 : bas de page — mutābaʿa qāṣira Ibn Ḫuzayma + renvoi
    ('ADJ6-p58-qasira-ibnkhuzayma', 58, 30, 540, 565, 810, 900),
    # p59 : déf. šāhid lugha + renvoi Maqāyīs 3/122|221
    ('ADJ7-p59-shahid-lugha', 59, 30, 300, 565, 560, 900),
    # p59 : šāhid lafẓī — isnād Nasāʾī (nom du rawī) + renvoi
    ('ADJ8-p59-nasai-isnad', 59, 30, 480, 565, 760, 900),
    # p59 : šāhid maʿnawī Buḫārī + phrase de clôture
    ('ADJ9-p59-shahid-manawi', 59, 30, 620, 565, 810, 900),
    # p60 : déf. iʿtibār lugha + renvoi Maqāyīs 4/210|012
    ('ADJ10-p60-itibar-lugha', 60, 30, 400, 565, 660, 900),
    # p60 : citation al-ʿIrāqī (début)
    ('ADJ11-p60-iraqi-cite', 60, 30, 660, 565, 815, 900),
    # p61 : renvois Šarḥ aṭ-Ṭabṣira (2 occurrences)
    ('ADJ12-p61-tabsira-refs', 61, 30, 180, 565, 480, 900),
    # p61 : citation Ibn Raǧab (ahtadī) + renvoi
    ('ADJ13-p61-ibnrajab', 61, 30, 460, 565, 730, 900),
    # p61 : taqwīm (3 items)
    ('ADJ14-p61-taqwim', 61, 30, 730, 565, 815, 600),
    # p62 : istiṯmār — citation Ibn aṣ-Ṣalāḥ complète + question
    ('ADJ15-p62-istithmar', 62, 30, 60, 565, 400, 900),
    # p62 : iʿdād al-qiblī (2 consignes)
    ('ADJ16-p62-i3dad-qibli', 62, 30, 400, 565, 815, 600),
]

for name, pg, x0, y0, x1, y1, dpi in CROPS:
    page = doc[pg - 1]
    zoom = dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=fitz.Rect(x0, y0, x1, y1))
    path = f'{OUT}/{name}-{dpi}.png'
    pix.save(path)
    print('OK', path, pix.width, 'x', pix.height)
print('done', len(CROPS), 'crops')
