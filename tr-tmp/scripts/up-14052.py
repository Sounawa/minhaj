#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 14052 (tafsir-5ep, Sourate al-Ṭāriq 11-17, leçon 28).

Vérifications :
- Citations coraniques PERDUES par l'OCR (paragraphes vides) → restaurées du
  canonique quran-cache.json : Ṭāriq 86:11-17 ; istithmār = al-Nisāʾ 4:58
  (rapport avec « parole décisive » : juger avec justice par ce qu'Allah a
  révélé).
- TABLE شرح dégradée : gloses seules — termes restitués des versets (الرجع /
  الصدع / فصل / هزل / أمهلهم / رويدًا).
- Gloses Jalālayn exactes conservées : الرجع = المطر « ainsi nommée pour sa
  récurrence » ; الصدع = la fente pour la végétation ; رُوَيْدًا = مصدر مؤكد
  pour le sens de l'opérateur, diminutif de رود ou أرواد par tarkhīm ;
  أمهلهم = emphase embellie par la variation lexicale.
- Pas de section الإعداد القبلي dans la source (fin du Ṭāriq — le doc
  suivant est l'index biographique 14063) — structure fidèle.
- Harmonisation 14042 (leçons 27 de la même sourate, déjà main) : « Par le
  ciel… », style des serments et références.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate al-Ṭāriq — le Tafsīr al-Jalālayn des versets 11 à 17</h1>
<p>Leçon de tafsīr de la sourate al-Ṭāriq (versets 11 à 17) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 28.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître certains attributs du Noble Coran.</li>
<li>Dégager des versets le laxisme (imhāl) d'Allah, le Très-Haut, envers les négateurs du Noble Coran.</li>
<li>Méditer ce que renferme le livre d'Allah, Puissant et Majestueux, et m'y conformer en ses règles.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>Après que la Vérité, glorifié soit-Il, a exposé les merveilles de Sa puissance dans la création de l'homme, Il expose ici la véracité du Prophète — paix et bénédiction sur lui — et du contenu du Noble Coran, avertissant Son prophète de la ruse de ces obstinés moqueurs, et du laxisme d'Allah envers eux.<br>
Quelle est la réponse coranique aux moqueurs du Coran ? Et quelle est leur rétribution pour cela ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Par le ciel détenteur du retour (11) et par la terre qui se fend ! (12) C'est certes une parole décisive — (13) et ce n'est point une plaisanterie. (14) Eux, ourdissent une ruse : (15) et Moi aussi J'ourdis une ruse. (16) Accorde donc délai aux négateurs : accorde-leur délai, un peu ! (17) » (al-Ṭāriq, 11-17)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Table imprimée dégradée : seules les gloses ont survécu à la numérisation ; les termes ont été restitués d'après les versets.]</p>
<ul>
<li>rajʿ (le retour) : la pluie.</li>
<li>ṣadʿ (la fente) : la fêlure d'où sort la végétation.</li>
<li>faṣl (décisive) : qui départage le vrai du faux.</li>
<li>hazl (plaisanterie) : le jeu et le futile.</li>
<li>amhilhum (accorde-leur délai) : diffère-les.</li>
<li>ruwaydan (un délai bref) : peu.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>Par quoi Allah, Puissant et Majestueux, a-t-Il décrit le Noble Coran dans les versets ?</li>
<li>Comment Allah, le Très-Haut, a-t-Il opposé [Son décret] à la ruse des associateurs et à leurs moqueries du Coran ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : le Coran départage le vrai du faux</h3>
<p>Après qu'Allah, Puissant et Majestueux, a établi les preuves de la possibilité de la résurrection, Il fit suivre cela de l'exposé que le Coran est vérité, et le Très-Haut dit :</p>
<p>« Par le ciel détenteur du retour »</p>
<p>c'est-à-dire : Je jure par le ciel détenteur de la pluie (rajʿ) — ainsi nommée pour sa récurrence ;</p>
<p>« et par la terre qui se fend ! »</p>
<p>c'est-à-dire : et Je jure par la terre qui se fend pour la végétation. Et la réponse du serment est Sa parole, glorifié soit-Il :</p>
<p>« C'est certes une parole décisive — »</p>
<p>« C'est » (innahu) : le Coran ; « décisive » (faṣl) : qui départage le vrai du faux ;</p>
<p>« et ce n'est point une plaisanterie. »</p>
<p>c'est-à-dire : et il n'est point jeu ni futile.</p>
<h3>Deuxièmement : le laxisme d'Allah, Puissant et Majestueux, envers les associateurs</h3>
<p>Puis Allah, glorifié soit-Il, clôtura cette noble sourate par la consolation du Messager — paix et bénédiction sur lui — et par sa bonne annonce, et le Très-Haut dit :</p>
<p>« Eux, ourdissent une ruse : »</p>
<p>« Eux » (innahum) : les négateurs ; « ourdissent une ruse » : machinent les complots contre le Prophète — paix et bénédiction sur lui ;</p>
<p>« et Moi aussi J'ourdis une ruse. »</p>
<p>c'est-à-dire : Je les attire progressivement (astadrijuhum) sans qu'ils le sachent.</p>
<p>« Accorde donc délai aux négateurs : »</p>
<p>— ô Muḥammad ;</p>
<p>« accorde-leur délai, »</p>
<p>— emphase embellie par la variation lexicale : c'est-à-dire : diffère-les ;</p>
<p>« un peu ! »</p>
<p>c'est-à-dire : peu de temps. Et c'est un verbe nominal soulignant le sens de son opérateur — diminutif (muṣagghar) de rūd ou arwād, par troncation (tarkhīm).</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers un ensemble de finalités éducatives, dont les plus importantes :</p>
<ul>
<li>rappeler à l'homme les faveurs d'Allah envers lui ;</li>
<li>guider l'homme vers l'obligation de répondre à ces faveurs par la gratitude ;</li>
<li>l'affirmation de la véracité du Noble Coran, qui départage le vrai du faux ;</li>
<li>le laxisme d'Allah, le Très-Haut, envers les négateurs, par miséricorde envers eux, afin qu'ils se repentent.</li>
</ul>
<h2>L'évaluation</h2>
<ol>
<li>Je détermine ce par quoi on jure et ce sur quoi on jure au début des versets.</li>
<li>Quel est le sens du fait que le Noble Coran soit « une parole décisive » (qawl faṣl) ?</li>
<li>Je conclus des versets [l'existence de] l'attirance progressive (istidrāj) d'Allah, le Très-Haut, envers les négateurs du Coran.</li>
</ol>
<h3>L'enrichissement (istithmār)</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Allah vous commande de restituer les dépôts à leurs ayants droit, et, lorsque vous jugez entre les gens, de juger avec équité. Allah vous exhorte admirablement à cela : Allah est Audient et Clairvoyant. » (al-Nisāʾ, 58)</p>
<ol>
<li>Quel est le rapport entre ce verset et le thème de la leçon ?</li>
<li>Quelle est la méthode légale correcte pour résoudre le différend entre les gens ?</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "14052":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 14052 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 14052 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
