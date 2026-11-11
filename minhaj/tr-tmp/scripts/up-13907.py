#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 13907 (tafsir-5ep, Sourate al-Muṭaffifīn 1-6).

Conventions main (cf. 16711 ; harmonisation 13931 — même sourate) :
- h1 « La sourate al-Muṭaffifīn — le Tafsīr al-Jalālayn des versets 1 à 6 ».
- Paragraphe d'ouverture : auteurs Jalāl al-Dīn al-Maḥallī (864 H) / Jalāl
  al-Dīn al-Suyūṭī (911 H), 5e année primaire traditionnel phase 2, leçon 17.
- « Objectifs de la leçon » en h2 + infinitifs.
- Versets : numérotation (1)-(6) + référence (al-Muṭaffifīn, 1-6) ;
  rabb al-ʿālamīn = « le Seigneur des mondes » (usage du projet, cf. 16741).
- Versets 1-6 et citations du tafsīr RESTAURÉS du canonique (cache sourate
  83) : le source imprimé ne livre que les gloses, les <p> des citations
  sont vides (perte OCR) ; la baseline LLM les avait paraphrasés.
- Table du شرح : seule la colonne des gloses survit (« كلمة عذاب أو واد في
  جهنم », « أخذوا منهم », « يأخذون الكيل وافيا », « ينقصون الكيل أو
  الوزن », « يتيقن ») ; les termes (wayl, iktālū, yastawfūna, yukhsirūna,
  yaẓunnu) restitués d'après les versets — note OCR explicite (cf. 13931).
- Préparation préalable : les 8 expressions vides du CMS restituées du
  canonique Muṭaffifīn 7-14 avec références (le LLM rendait marqūm par
  « déjà cacheté (achevé) » : c'est « un livre inscrit »).
- Corrections vs baseline : « [leur] causent perte » → « lèsent »
  (yukhsirūna, glosé « diminuent la mesure ou le poids ») ; « jour
  terrible » → « jour immense » (ʿaẓīm, glosé « terreurs qu'il renferme ») ;
  « le Vérité » → « le Vrai » (al-Ḥaqq) ; « Seigneur de l'Univers » →
  « Seigneur des mondes » ; GT-ismes (*mikyāl*, *mīzān* entre astérisques,
  « J'investigue », « Jour de la Religion ») éliminés.
- istithmār : athar de Yaḥyā ibn Saʿīd / Saʿīd ibn al-Musayyib, référence
  [موطأ الإمام مالك، كتاب البيوع، باب جامع البيوع] conservée.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate al-Muṭaffifīn — le Tafsīr al-Jalālayn des versets 1 à 6</h1>
<p>Leçon de tafsīr de la sourate al-Muṭaffifīn (versets 1 à 6) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 17.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître la notion de fraude (taṭfīf) et la rétribution des fraudeurs (mutaffifīn).</li>
<li>Dégager l'issue des fraudeurs dans la mesure et le poids.</li>
<li>M'engager à la justice dans la mesure et le poids.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>La sourate al-Muṭaffifīn est mecquoise et compte trente-six versets. Dans ses six premiers versets, elle a traité de la menace adressée à ceux qui fraudent dans la mesure et le poids, et leur a rappelé le jour de la rétribution, lorsque les gens seront présentés au Seigneur des mondes pour rendre compte des œuvres qu'ils auront acquises dans ce bas monde.<br>
Quelle est la menace d'Allah aux fraudeurs ? Et comment rencontreront-ils Allah, Puissant et Majestueux, au jour de la rétribution ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Malheur aux fraudeurs, (1) qui, lorsqu'ils se font mesurer par les gens, exigent la pleine mesure, (2) et qui, lorsqu'ils mesurent pour eux ou pèsent pour eux, lèsent. (3) Ne pensent-ils pas qu'ils seront ressuscités, (4) en un jour immense, (5) le jour où les gens se lèveront devant le Seigneur des mondes ? (6) » (al-Muṭaffifīn, 1-6)</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<ul>
<li>wayl (malheur) : une parole de châtiment, ou une vallée en Géhenne.</li>
<li>iktālū ʿalā l-nāsi (se font mesurer par les gens) : ils ont pris d'eux [la marchandise].</li>
<li>yastawfūna (exigent la pleine mesure) : ils prennent la mesure au complet.</li>
<li>yukhsirūna (lèsent) : ils diminuent la mesure ou le poids.</li>
<li>yaẓunnu (pensent) : sont certains, se convainquent.</li>
</ul>
<p>[Le tableau du source imprimé ne livre que la colonne des gloses — l'autre colonne est vide, perte OCR ; les termes sont restitués d'après les versets.]</p>
<h3>Extraction des idées des versets</h3>
<ol>
<li>Qui Allah, Puissant et Majestueux, a-t-Il menacé à l'ouverture de la sourate ?</li>
<li>De quoi Allah a-t-Il rappelé les fraudeurs dans ces versets, afin qu'ils se reprennent ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la menace d'Allah aux fraudeurs</h3>
<p>Après que le Vrai, glorifié soit-Il, a établi, à la fin de la sourate al-Infiṭār, qu'au Jour de la Résurrection nulle âme ne possédera quoi que ce soit sur une autre âme, Il le fit suivre de Sa parole :</p>
<p>« Malheur aux fraudeurs ! »</p>
<p>c'est-à-dire : un châtiment sévère, ou une vallée en Géhenne, pour quiconque fraude dans la mesure et le poids — et ce sont :</p>
<p>« ceux qui, lorsqu'ils se font mesurer par les gens, exigent la pleine mesure, »</p>
<p>— « la pleine mesure » : la mesure, et ils la prennent au complet ;</p>
<p>« et qui, lorsqu'ils mesurent pour eux ou pèsent pour eux, lèsent. »</p>
<p>c'est-à-dire : et lorsqu'ils mesurent pour les gens ou pèsent pour eux, ils diminuent la mesure et le poids.</p>
<h3>Deuxièmement : le rappel aux fraudeurs de la résurrection et du compte</h3>
<p>Après la menace du malheur (wayl) proférée contre les fraudeurs, le Très-Pur leur a rappelé la résurrection et le compte. Il a dit :</p>
<p>« Ne pensent-ils pas qu'ils seront ressuscités »</p>
<p>— interrogation de blâme à l'adresse des fraudeurs, c'est-à-dire : ces fraudeurs-là ne sont-ils pas certains qu'ils seront ressuscités</p>
<p>« en un jour immense, »</p>
<p>c'est-à-dire : en un jour immense, qui est le Jour de la Résurrection — ainsi nommé en raison des terreurs qu'il renferme ;</p>
<p>« le jour où les gens se lèveront devant le Seigneur des mondes. »</p>
<p>c'est-à-dire : le jour où les gens se lèveront de leurs tombeaux pour l'ordre du Seigneur des mondes, le compte et la rétribution.</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers un ensemble de finalités éducatives, dont les plus importantes :</p>
<ol>
<li>Exhorter à l'équité dans les transactions, en vente et en achat, en prise et en don.</li>
<li>Mettre en garde contre tout ce qui conduit à la désunion entre les gens du fait de la fraude dans la mesure et le poids.</li>
<li>Rappeler le Jour de la Résurrection, pour en tirer leçon et admonition.</li>
</ol>
<h2>L'évaluation</h2>
<ol>
<li>Quel est le sens de la fraude (taṭfīf) dans la mesure et le poids ?</li>
<li>Pourquoi Allah, Puissant et Majestueux, a-t-Il interdit la fraude dans la mesure et le poids ?</li>
<li>Par quoi Allah a-t-Il menacé les fraudeurs, afin de les amener à s'en tenir à l'équité dans leurs transactions ?</li>
</ol>
<h2>L'enrichissement (istithmār)</h2>
<p>« D'après Yaḥyā ibn Saʿīd, il a entendu Saʿīd ibn al-Musayyib dire : "Si tu arrives en un pays où l'on donne la pleine mesure et le juste poids, prolonge ton séjour en elle ; et si tu arrives en un pays où l'on diminue la mesure et le poids, écourte ton séjour en elle." » [Muwaṭṭaʾ de l'imam Mālik, Kitāb al-Buyūʿ (Livre des ventes), Bāb Jāmiʿ al-buyūʿ (chapitre général des ventes)]</p>
<ul>
<li>Pourquoi Saʿīd ibn al-Musayyib — qu'Allah l'agrée — a-t-il mis en garde contre l'établissement dans le pays des fraudeurs ?</li>
</ul>
<h2>La préparation préalable</h2>
<p>Je lis les versets 7 à 17 de la sourate al-Muṭaffifīn et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Non ! Le livre des libertins est certes dans le Sijjīn » (al-Muṭaffifīn, 7) ;</p>
<p>« Et qui te dira ce qu'est le Sijjīn ? » (al-Muṭaffifīn, 8) ;</p>
<p>« un livre inscrit » (al-Muṭaffifīn, 9) ;</p>
<p>« Malheur, ce jour-là, aux négateurs » (al-Muṭaffifīn, 10) ;</p>
<p>« qui traitent de mensonge le Jour de la Rétribution » (al-Muṭaffifīn, 11) ;</p>
<p>« Or, ne le traite de mensonge que tout transgresseur, pécheur » (al-Muṭaffifīn, 12) ;</p>
<p>« qui, lorsque Nos versets lui sont récités, dit : "Des contes des anciens !" » (al-Muṭaffifīn, 13) ;</p>
<p>« Non ! Mais ce qu'ils ont acquis a couvert leurs cœurs » (al-Muṭaffifīn, 14).</p>
<p>[Expressions restituées d'après les versets 7 à 14 de la sourate al-Muṭaffifīn : les huit lignes correspondantes du source imprimé sont vides — perte OCR.]</p>
<ul>
<li>Je recherche la rétribution des négateurs du Jour de la Rétribution.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13907":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13907 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13907 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
