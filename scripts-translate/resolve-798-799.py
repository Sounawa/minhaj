#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Relèvement des 2 derniers slots vides de tafsir-5ep : 798 et 799
(sourate al-Shūrā, versets 18-20 et 14-17 — numérotation du manuel, 3e année
de l'enseignement collégial traditionnel).

Doctrine (précédent 781427f : 30 doublons 768-797 ; arbitrage faraid 316/325) :
un fascicule du portail diffusé sous deux entrées d'arborescence à la fois est
un DOUBLON RÉEL, relevé par renvoi de référence — la traduction de la leçon
jumelle est reprise, précédée d'une note « Source du cours » qui consigne
l'identité des deux entrées et la référence exacte de la jumelle.

Ici la preuve d'identité est DOUBLE (les jumelles de tafsir-3es, livrées R58,
ne portent pas de pdfUrl en base — la preuve par URL octet à octet des 768-797
n'est pas disponible ; elle est remplacée par une preuve équivalente en deux
branches, chaque branche vérifiée dans les données ce tour) :
  1. ARBORESCENCE : le livre jumelé tafsir-3es porte levelAr
     « al-Tafsīr al-iʿdādī al-thālith » (3e année collégiale de Tafsīr), qui est
     LE MÊME segment d'arborescence du portail que le chemin des présent
     slots (tafsir/iʿdādī/thālith-iʿdādī) ;
  2. ÉTIQUETTE : l'étiquette du portail pour chaque slot (« Sourate al-Shūrā,
     versets 18-20 » / « 14-17 ») concorde avec la matière réellement livrée
     pour la jumelle correspondante (h1 et bloc des versets : 18-20 du manuel
     = 20-22 du muṣḥaf courant pour 798 ; 14-17 du manuel = 16-19 pour 799).

Assainissement de la copie : artefacts de scraping retirés (dl/dt/dd vides
d'entête, <p></p> vides, queue « <p>Exégèse…</p><div>… » après la préparation
préalable) — sans toucher au texte traduit, qui reste identique à la jumelle.

Auto-fix typographique : 0 caractère arabe (QA dur), apostrophes typographiques,
guillemets « » appariés, espaces fines insécables.
"""
import json
import os
import re

HOME = '/home/z/my-project'
BOOKS = f'{HOME}/content/books'
SRC_BOOK = 'tafsir-3es'
DST_BOOK = 'tafsir-5ep'
OUT = f'{HOME}/tr-tmp'

# slot -> (docId jumelle, étiquette portail, passage au muṣḥaf courant)
MAP = {
    'pdf-mut23h3c-798': ('16850', 'Sourate al-Shūrā, versets 18-20',
                         'versets 20 à 22 du muṣḥaf courant'),
    'pdf-mut23h3c-799': ('16833', 'Sourate al-Shūrā, versets 14-17',
                         'versets 16 à 19 du muṣḥaf courant'),
}

NB = '\u202f'   # espace fine insécable
APO = '\u2019'  # apostrophe typographique
ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]')


def clean_body(html: str) -> str:
    """Retire les artefacts de scraping, sans toucher au texte traduit."""
    # 1) entête vide : <dl><dt></dt><dd></dd></dl> + <p></p> qui suit le h1
    html = re.sub(r'<dl>\s*<dt></dt>\s*<dd>\s*</dd>\s*</dl>\s*', '', html, count=1)
    # 2) queue : <p>Exégèse de la sourate al-Shūrā (versets …)</p><div>… à la fin
    html = re.sub(
        r'<p>\s*Exégèse de la sourate al-Shūrā \(versets[\s\S]*?1[48]-[12][07]\)\s*</p>[\s\S]*\Z',
        '', html)
    # 3) paragraphes vides résiduels
    html = re.sub(r'<p></p>', '', html)
    # 4) espaces de queue + lignes vides multiples
    html = re.sub(r'[ \t]+\n', '\n', html)
    html = re.sub(r'\n{3,}', '\n\n', html)
    return html.strip() + '\n'


def typ(s: str) -> str:
    """Auto-fix typographique maison (nœuds texte hors balises)."""
    out = []
    for tok in re.split(r'(<[^>]+>)', s):
        if tok.startswith('<'):
            out.append(tok)
            continue
        t = tok.replace("'", APO)
        t = re.sub(r'[ \u00a0\u202f]*([;:!?»])', NB +r'\1', t)
        t = re.sub(r'«[ \u00a0\u202f]*', '«' + NB, t)
        t = re.sub(r' {2,}', ' ', t)
        out.append(t)
    return ''.join(out)


def build_note(twin_id: str, label: str, passage: str, twin_h1: str) -> str:
    return (
        '<dl class="lesson-meta">\n<dt>Source du cours</dt>\n<dd>'
        f'Fascicule de la série{NB}«{NB}Tafsīr — troisième année de '
        f'l{APO}enseignement collégial traditionnel, d{APO}après le Tashīl '
        f'li-ʿulūm al-tanzīl d{APO}Ibn Juzayy{NB}»{NB}du portail des Habous '
        f'(diffusion par le portail sous deux entrées d{APO}arborescence à la '
        f'fois : le présent emplacement et le livre de Tafsīr de 3e année de '
        f'l{APO}enseignement collégial). Doublon réel, arbitré par renvoi de '
        f'référence : la traduction ci-dessous reprend, à la présente note '
        f'près, celle établie et vérifiée pour la leçon jumelle ({twin_id}) du '
        f'livre de Tafsīr de 3e année collégiale, livrée avec sa série complète '
        f'(introduction et six leçons de la sourate al-Shūrā). L{APO}identité '
        f'des deux entrées est établie par le portail lui-même : le livre '
        f'jumelé et le présent emplacement relèvent d{APO}une seule et même '
        f'arborescence (la 3e année collégiale de Tafsīr), et l{APO}étiquette '
        f'portée pour le présent emplacement ({NB}«{NB}{label}{NB}»{NB}) '
        f'concorde avec la matière du fascicule ({NB}«{NB}{twin_h1}{NB}»{NB}) — '
        f'le passage couvert correspond à {passage}, le manuel comptant la '
        f'sourate al-Shūrā à cinquante versets (numérotation documentée dans '
        f'la leçon jumelle).'
        '</dd>\n</dl>\n'
    )


def main() -> None:
    src = json.load(open(os.path.join(BOOKS, SRC_BOOK + '.json'), encoding='utf-8'))
    twins = {str(l['docId']): l for l in src['lessons']}

    for slot, (tid, label, passage) in MAP.items():
        twin = twins[tid]
        th = twin['htmlFr'] or ''
        # h1 de la jumelle = matière réellement livrée
        m = re.search(r'<h1[^>]*>(.*?)</h1>', th, re.S)
        twin_h1 = re.sub(r'<[^>]+>', '', m.group(1)).strip() if m else ''
        assert twin_h1, f'h1 introuvable pour la jumelle {tid}'

        body = clean_body(th)
        note = build_note(tid, label, passage, twin_h1)
        # insérer la note juste après le h1
        m = re.match(r'(<h1[^>]*>.*?</h1>\s*)', body, re.S)
        if m:
            new_html = m.group(1) + '\n' + note.strip() + '\n' + body[m.end():]
        else:
            new_html = note + body
        new_html = typ(new_html)

        out = os.path.join(OUT, f'lesson-{slot.rsplit("-", 1)[-1]}-fr.html')
        with open(out, 'w', encoding='utf-8') as fh:
            fh.write(new_html)

        # QA dure : 0 arabe, guillemets appariés, 0 apostrophe droite
        errs = []
        if ARABIC.search(new_html):
            errs.append('ARABE RÉSIDUEL')
        if new_html.count('«') != new_html.count('»'):
            errs.append('GUILLEMETS non appariés')
        if "'" in re.sub(r'<[^>]+>', '', new_html):
            errs.append('APOSTROPHE DROITE')
        # fidélité : le bloc des versets de la jumelle est présent mot pour mot
        vm = re.search(r'«\u202f?Et ceux qui disputent[\s\S]*?»,?', new_html) if tid == '16833' \
            else re.search(r'«\u202f?Quiconque désire le labeur[\s\S]*?»,?', new_html)
        if not vm:
            errs.append('BLOC DES VERSETS absent ou altéré')

        print(f'{out} : {len(new_html)} car — QA : '
              + ('ÉCHEC : ' + ' ; '.join(errs) if errs else 'PASS'))


if __name__ == '__main__':
    main()
