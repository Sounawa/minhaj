#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Relèvement des 30 doublons URL-exacts de tafsir-5ep (slots 768-797).

Doctrine (précédents R455/R456, arbitrage faraid 316/325) : un fascicule du
portail diffusé sous deux entrées d'arborescence à la fois est un DOUBLON RÉEL
— la preuve étant l'URL du document, identique octet par octet. Le relèvement
se fait par renvoi de référence : la traduction de la leçon jumelle est
reprise, précédée d'une note « Source du cours » qui consigne l'identité des
deux entrées, l'écart éventuel d'étiquette du portail, et la référence exacte
de la jumelle.

Ce tour : la série « Tafsīr — deuxième année de l'enseignement collégial
traditionnel » (Tashīl d'Ibn Juzayy) est diffusée par le portail à la fois
dans le livre de Tafsīr de 2e année collégiale (tafsir-2es, déjà traduit —
fascicules 556-585) et dans le présent emplacement (tafsir-5ep, slots
768-797). 30 fascicules levés d'un coup.

Auto-fix typographique : aucun caractère arabe (QA dur), apostrophes
typographiques, guillemets « » appariés, espaces fines insécables.
"""
import json
import os
import re
import sys

BOOKS = '/home/z/my-project/content/books'
SRC_BOOK = 'tafsir-2es'
DST_BOOK = 'tafsir-5ep'

NB = '\u202f'   # narrow no-break space
APO = '\u2019'  # apostrophe typographique


def sanitize(html: str, twin_id: str) -> str:
    """Assainissement de la copie (le présent tour QA 0 arabe, guillemets
    appariés) — sans toucher aux originaux historiques de tafsir-2es."""
    # 1) marqueur de fin de verset U+06DD -> tiret séparateur
    html = re.sub(r'\s*\u06dd\s*', ' — ', html)
    # 2) citation coranique arabe de la N.d.T. (579) -> translittération + trad.
    html = html.replace(
        '« وَهُوَ مَعَكُمْ أَيْنَ مَا كُنتُمْ »',
        '«wa-huwa maʿa-kum ayna mā kuntum» (Et Il est avec vous où que vous soyez)',
    )
    html = html.replace(
        '« وَهُوَ مَعَكُمْ أَيْنَ مَا كُنتُمْ »',
        '« wa-huwa maʿa-kum ayna mā kuntum » (Et Il est avec vous où que vous soyez)',
    )
    html = re.sub(
        r'«\s*وَهُوَ مَعَكُمْ أَيْنَ مَا كُنتُمْ\s*»',
        '«wa-huwa maʿa-kum ayna mā kuntum» (Et Il est avec vous où que vous soyez)',
        html,
    )
    # 3) guillemet orphelin de 575 : la glose d'Ibn Kaṯīr ouvre sa citation
    html = html.replace(
        "c’est-à-dire\u202f: elle est une jouissance périssable",
        "c’est-à-dire\u202f: «\u202felle est une jouissance périssable",
    )
    return html


def typ(s: str) -> str:
    """Auto-fix typographique maison (nœuds texte hors balises)."""
    out = []
    for tok in re.split(r'(<[^>]+>)', s):
        if tok.startswith('<'):
            out.append(tok)
            continue
        t = tok.replace("'", APO)
        t = re.sub(r'[ \u00a0\u202f]*([;:!?»])', NB + r'\1', t)
        t = re.sub(r'«[ \u00a0\u202f]*', '«' + NB, t)
        t = re.sub(r' {2,}', ' ', t)
        out.append(t)
    return ''.join(out)


def fascicule_num(url: str, twins_ord: dict) -> int:
    """Numéro du fascicule = position ordinale de la jumelle dans la série
    traduite (556 -> 1 ... 585 -> 30) — la numérotation des noms de fichiers du
    portail étant incohérente, c'est l'ordinal de livraison qui fait foi."""
    return twins_ord.get(url, 0)


def main() -> None:
    src = json.load(open(os.path.join(BOOKS, SRC_BOOK + '.json'), encoding='utf-8'))
    dst = json.load(open(os.path.join(BOOKS, DST_BOOK + '.json'), encoding='utf-8'))
    by_url = {}
    twins_ord = {}
    for l in src['lessons']:
        u = l.get('pdfUrl')
        if u and len(l.get('htmlFr') or '') >= 500:
            by_url[u] = l
    # ordinal des jumelles dans l'ordre de la série (556 -> 1, 557 -> 2, ...)
    for i, l in enumerate([x for x in src['lessons'] if x.get('pdfUrl') and len(x.get('htmlFr') or '') >= 500]):
        twins_ord[l['pdfUrl']] = i + 1

    series_fr = ('Tafsīr — deuxième année de l' + APO + 'enseignement collégial '
                 'traditionnel, d' + APO + 'après le Tashīl li-ʿulūm al-tanzīl '
                 'd' + APO + 'Ibn Juzayy')
    raised, skipped = [], []
    for l in dst['lessons']:
        u = l.get('pdfUrl')
        if not u or u not in by_url:
            continue
        if len(l.get('htmlFr') or '') >= 500:
            skipped.append(l['docId'])
            continue
        twin = by_url[u]
        html = sanitize(twin['htmlFr'], twin['docId'])
        num = fascicule_num(u, twins_ord)
        portal_label = (l.get('titleFr') or '').strip()
        twin_title = (twin.get('titleFr') or '').strip()
        # écart d'étiquette : le portail porte-t-il un titre qui diverge de la matière ?
        norm = lambda s: re.sub(r'[\s:]+', ' ', s.lower().replace('—', '-')).strip()
        if portal_label and twin_title and norm(portal_label) != norm(twin_title):
            ecart = (f'l' + APO + 'étiquette portée par l' + APO + 'arborescence du '
                     f'portail pour le présent emplacement («{NB}{portal_label}{NB}») '
                     f'diverge de la matière du fascicule («{NB}{twin_title}{NB}») — '
                     'la traduction suit le fascicule, la divergence consignée')
        else:
            ecart = (f'l' + APO + 'étiquette portée par l' + APO + 'arborescence '
                     f'du portail («{NB}{portal_label}{NB}») concorde avec la '
                     'matière du fascicule')
        num_txt = (f'le fascicule n°{num} de la série' if num else
                   'un fascicule de la série')
        note = (
            '<dl class="lesson-meta">\n<dt>Source du cours</dt>\n<dd>'
            f'{num_txt.capitalize() if num else "Fascicule de la série"} '
            f'«{NB}{series_fr}{NB}» du portail des Habous (diffusion par le '
            'portail sous deux entrées d' + APO + 'arborescence à la fois : le '
            'présent emplacement et le livre de Tafsīr de deuxième année '
            'collégiale) — l' + APO + 'identité des deux entrées est établie par '
            'l' + APO + 'URL du document, identique octet par octet. Doublon '
            'réel, arbitré par renvoi de référence : la traduction ci-dessous '
            'reprend, à la présente note près, celle établie et vérifiée pour la '
            f'leçon jumelle ({twin["docId"]}) du livre de Tafsīr de 2e année '
            f'collégiale ; {ecart}.'
            '</dd>\n</dl>\n'
        )
        # insérer la note juste après le h1
        m = re.match(r'(<h1[^>]*>.*?</h1>\s*)', html, re.S)
        if m:
            new_html = m.group(1) + '\n' + note.strip() + '\n' + html[m.end():]
        else:
            new_html = note + html
        l['htmlFr'] = typ(new_html)
        l['titleFr'] = twin_title or portal_label
        # sample retiré le cas échéant (leçon désormais complète)
        if l.get('sample'):
            l['sample'] = None
        raised.append((l['docId'], twin['docId'], num))

    tmp = os.path.join(BOOKS, DST_BOOK + '.json.tmp')
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(dst, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    os.replace(tmp, os.path.join(BOOKS, DST_BOOK + '.json'))

    print(f'RELEVÉS : {len(raised)} doublons')
    for did, tid, num in raised:
        print(f'  {did} <- {tid} (fascicule n°{num})')
    if skipped:
        print(f'DÉJÀ FAITS (ignorés) : {skipped}')

    # QA dure : 0 caractère arabe dans chaque htmlFr relevé
    ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')
    dst2 = json.load(open(os.path.join(BOOKS, DST_BOOK + '.json'), encoding='utf-8'))
    bad = 0
    for l in dst2['lessons']:
        if l['docId'] in [d for d, _, _ in raised]:
            h = l.get('htmlFr') or ''
            if ARABIC.search(h):
                bad += 1
                print(f'⚠︎ ARABE RÉSIDUEL dans {l["docId"]}')
            if h.count('«') != h.count('»'):
                bad += 1
                print(f'⚠︎ GUILLEMETS non appariés dans {l["docId"]}')
    print('QA ARABE/GUILLEMETS :', 'ÉCHEC' if bad else 'PASS')


if __name__ == '__main__':
    main()
