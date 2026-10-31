#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R456 — Amendement d'audit des pièces 310-316 de faraid-tanawi-3.

(1) Leçons 310-315 : la ligne « Source du cours » portait l'attribution erronée
    « le manuel des farāʾiḍ de la troisième année du cycle secondaire
    traditionnel, portant la manẓūma al-Ǧawāhir al-Maknūna » — l'audit de
    clôture (R455/leçon 336) a reconnu le volume de 181 pages pour une édition
    SAOUDIENNE (formule royale, filière de la loi religieuse, éd. 1447/2025).
    L'attribution est corrigée ; la revendication d'origine est consignée dans
    une note d'amendement (doctrine de la double vérité du corpus).
    La leçon 310 porte en outre sa ligne de source sous l'étiquette fautive
    « Arǧūza source » — ramenée à « Source du cours ».
(2) Leçon 316 : arbitrage du chevauchement 316/325 — les deux pièces vivent du
    même chapitre final du manuel de deuxième année (p. 191-201) ; renvoi de
    référence vers la leçon 325 (dars 27, 104 comptes exacts).
"""
import json

BOOK = 'content/books/faraid-tanawi-3.json'

TRUE_HDR = ("Le volume du miroir — une édition saoudienne du cours de farāʾiḍ "
            "(la formule royale d\u2019Arabie saoudite décidant l\u2019enseignement du livre "
            "et son impression à ses frais, la filière de la loi religieuse, éd. 1447/2025)")

TRUE_HDR_SHORT = ("Le volume du miroir — une édition saoudienne du cours de farāʾiḍ "
                  "(la formule royale d\u2019Arabie saoudite décidant l\u2019enseignement du livre "
                  "et son impression à ses frais, la filière de la loi religieuse)")

NOTE_AMENDEE = (" Attribution amendée par l\u2019audit de clôture du volume (leçon 336) : "
                "la ligne d\u2019origine désignait l\u2019imprimé comme « le manuel de la troisième année "
                "du cycle secondaire traditionnel, portant la manẓūma al-Ǧawāhir al-Maknūna » — "
                "la page de titre porte les marques de l\u2019édition saoudienne, et la manẓūma "
                "authentique de la troisième année marocaine (celle de Rasmūkī) n\u2019est pas dans "
                "le miroir local ; l\u2019attribution est corrigée, la revendication d\u2019origine "
                "consignée par la présente note.")

RENVOI_316 = (" Arbitrage d\u2019audit (clôture du volume) : le chapitre final du manuel de "
              "deuxième année a reçu deux traitements — la présente pièce, première portée du "
              "chapitre (p. 191-201 de l\u2019imprimé), et la leçon 325 (le dars 27, p. 193-201 : "
              "les 104 comptes exacts, le trilogue du Code de la famille, la voie de correction "
              "en sept étapes) — les deux vivant du même imprimé ; le traitement de référence "
              "pour le chapitre entier est la leçon 325, la présente conservant la matière de "
              "sa livraison d\u2019origine.")


def span_replace(s, start_anchor, end_anchor, replacement, incl_end=True):
    i = s.find(start_anchor)
    assert i >= 0, f'ancre introuvable : {start_anchor[:40]!r}'
    j = s.find(end_anchor, i)
    assert j >= 0, f'fin introuvable : {end_anchor[:40]!r}'
    j += len(end_anchor) if incl_end else 0
    return s[:i] + replacement + s[j:], s[i:j]


def append_note(dd_html, note):
    k = dd_html.find('</dd>')
    assert k >= 0, 'pas de </dd>'
    return dd_html[:k] + note + dd_html[k:]


def main():
    with open(BOOK) as f:
        book = json.load(f)
    lessons = book['lessons']
    report = []

    # ---- 310 : étiquette + en-tête faux (Arǧūza source) ----
    l = lessons[0]
    assert l['docId'] == 'pdf-mut23h2v-310', l['docId']
    h = l['htmlFr']
    assert '<dt>Arǧūza source</dt>' in h
    h = h.replace('<dt>Arǧūza source</dt>', '<dt>Source du cours</dt>')
    new, old = span_replace(
        h,
        'Manẓūmat al-Ǧawāhir al-Maknūna',
        'le poème des farāʾiḍ porté par la troisième année du cycle secondaire traditionnel.',
        TRUE_HDR + '.')
    h = append_note(new, NOTE_AMENDEE)
    l['htmlFr'] = h
    report.append(('310', old, new))

    # ---- 311 : en-tête + phrase « aucun vers du poète » (ne vivait que de la fausse attribution) ----
    l = lessons[1]
    assert l['docId'] == 'pdf-mut23h2v-311', l['docId']
    h = l['htmlFr']
    new, old = span_replace(
        h,
        'Le manuel des farāʾiḍ de la troisième année',
        'la prose du cours est celle des auteurs du manuel.',
        TRUE_HDR + '\u202f—, la prose du cours étant celle des auteurs du volume.')
    h = append_note(new, NOTE_AMENDEE)
    l['htmlFr'] = h
    report.append(('311', old, new))

    # ---- 312-315 : en-tête seul, la suite (édition/OCR) reste ----
    for idx in range(2, 6):
        l = lessons[idx]
        assert l['docId'] == f'pdf-mut23h2v-{310 + idx}', l['docId']
        h = l['htmlFr']
        i = h.find('Le manuel des farāʾiḍ de la troisième année')
        assert i >= 0, f'ancre introuvable ({l["docId"]})'
        k_sunna = h.find('sunna', i)
        assert k_sunna >= 0, f'sunna introuvable ({l["docId"]})'
        k = h.find('—,', k_sunna)
        assert k >= 0, f'fin introuvable ({l["docId"]})'
        old = h[i:k + 2]
        new = h[:i] + TRUE_HDR_SHORT + '\u202f—,' + h[k + 2:]
        l['htmlFr'] = append_note(new, NOTE_AMENDEE)
        report.append((str(310 + idx), old, new))

    # ---- 316 : renvoi d'arbitrage ----
    l = lessons[6]
    assert l['docId'] == 'pdf-mut23h2v-316', l['docId']
    h = l['htmlFr']
    h = append_note(h, RENVOI_316)
    l['htmlFr'] = h
    report.append(('316', '(renvoi appended)', RENVOI_316[:120]))

    with open(BOOK, 'w') as f:
        json.dump(book, f, ensure_ascii=False, indent=2)

    for doc, old, new in report:
        print(f'=== {doc} ===')
        print('AVANT :', old[:150].replace('\n', ' '))
        print('APRÈS :', new[:150].replace('\n', ' '))
        print()
    print('JSON réécrit :', BOOK)


if __name__ == '__main__':
    main()
