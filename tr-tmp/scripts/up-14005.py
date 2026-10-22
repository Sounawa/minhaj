#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 14005 (tafsir-5ep, Sourate al-Burūj 10-16, leçon 25).

Vérifications :
- Citations coraniques PERDUES par l'OCR (paragraphes vides) → restaurées du
  canonique quran-cache.json : Burūj 85:10-16 ; hadith Abū Mūsā (istithmār) =
  Hūd 11:102 ; préparation = 85:17-21 (leçon SUIVANTE 14018).
- Garble d'ouverture « سورة اليروج » = البروج (h1 correct) ; «:» parasite en
  tête de la 4e ligne de la table شرح (OCR) — corrigés au rendu.
- TABLE شرح dégradée : gloses seules — termes restitués des versets (بطش /
  الودود / ذو العرش / المجيد).
- Gloses Jalālayn exactes conservées : يبديء ويعيد = الخلق (la création) ;
  الغفور = للمذنبين المؤمنين ; الودود = المتودد إلى أوليائه بالكرامة ;
  ذو العرش = ربه وخالقه ومالكه ; المجيد lu بالرفع = المستحق لكمال صفات
  العلو (note qirāʾique) ; فعال لما يريد = لا يعجزه شيء… كن فيكون.
- Hadith Bukhārī « إن الله ليملي للظالم… » (kitāb al-tafsīr) + Hūd 102
  restaurés ; récit étayé par la référence imprimée conservée.
- Harmonisation 13992 (leçon précédente, même sourate) : « rigueur » pour
  بطش, « Pardonneur / Tout-Affectueux / Maître du Trône / Glorieux », « ce
  qu'Il veut » pour لما يريد.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate al-Burūj — le Tafsīr al-Jalālayn des versets 10 à 16</h1>
<p>Leçon de tafsīr de la sourate al-Burūj (versets 10 à 16) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 25.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître la rétribution des injustes et des croyants à travers les versets.</li>
<li>Dégager des versets la grandeur d'Allah, le Très-Haut, et la perfection de Sa puissance.</li>
<li>Garder présents la puissance d'Allah et Sa grandeur dans toutes les circonstances de ma vie.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>Après qu'Il a rapporté, glorifié soit-Il, l'histoire des gens de la fosse et exposé les nuisances et les supplices qu'ils infligèrent aux croyants, Il mentionne en ces versets le châtiment douloureux préparé aux négateurs, et la rétribution généreuse préparée aux croyants.<br>
Quelle est la rétribution des injustes et des croyants ? Et quels sont les attributs d'Allah, Puissant et Majestueux, indiquant Sa puissance et Sa grandeur ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Ceux qui ont éprouvé les croyants et les croyantes, puis ne se sont pas repentis : à eux le châtiment de la Géhenne, et le châtiment de la brûlure. (10) Ceux qui croient et accomplissent les œuvres bonnes ont des jardins sous lesquels coulent les ruisseaux : tel est l'immense succès. (11) Oui, la rigueur de ton Seigneur est terrible : (12) c'est Lui qui commence et recommence ; (13) et c'est Lui le Pardonneur, le Tout-Affectueux, (14) le Maître du Trône, le Glorieux, (15) l'Effecteur de ce qu'Il veut. (16) » (al-Burūj, 10-16)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Table imprimée dégradée : seules les gloses ont survécu à la numérisation ; les termes ont été restitués d'après les versets.]</p>
<ul>
<li>baṭsh (la rigueur) : la prise avec dureté.</li>
<li>al-wadūd (le Tout-Affectueux) : qui témoigne de l'affection à Ses amis.</li>
<li>dhū al-ʿarsh (le Maître du Trône) : le possesseur du Trône.</li>
<li>al-majīd (le Glorieux) : le digne des attributs parfaits de hauteur, et qualifié par eux.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>En quoi Allah, Puissant et Majestueux, a-t-Il comparé les injustes et les croyants dans les versets ?</li>
<li>Qu'indiquent les attributs d'Allah, Puissant et Majestueux, mentionnés à la fin des versets ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : la comparaison entre la rétribution des injustes et celle des croyants</h3>
<p>Dans ces versets, Allah, le Très-Haut, a durci le blâme contre les criminels qui ont supplicié les croyants, et les a menacés du châtiment de la Géhenne. Le Glorifié a dit :</p>
<p>« Ceux qui ont éprouvé les croyants et les croyantes, »</p>
<p>c'est-à-dire : ont brûlé les croyants et les croyantes par le feu.</p>
<p>« puis ne se sont pas repentis »</p>
<p>c'est-à-dire : puis ne sont pas revenus de leur injustice.</p>
<p>« : à eux le châtiment de la Géhenne, »</p>
<p>c'est-à-dire : le châtiment de la Géhenne dans l'au-delà, en rétribution de leur combustion des croyants.</p>
<p>Puis le Glorifié exposa la rétribution des croyants, et dit :</p>
<p>« Ceux qui croient et accomplissent les œuvres bonnes ont des jardins sous lesquels coulent les ruisseaux : tel est l'immense succès. »</p>
<h3>Deuxièmement : la grandeur d'Allah, le Très-Haut, et la perfection de Sa puissance</h3>
<p>Allah, le Très-Haut, a exposé la perfection de Sa puissance, et le Glorifié a dit :</p>
<p>« Oui, la rigueur de ton Seigneur est terrible : »</p>
<p>c'est-à-dire : envers les négateurs.</p>
<p>« c'est Lui qui commence et recommence ; »</p>
<p>c'est-à-dire : la création — selon Sa volonté.</p>
<p>« et c'est Lui le Pardonneur, »</p>
<p>— envers les pécheurs croyants ;</p>
<p>« le Tout-Affectueux, »</p>
<p>c'est-à-dire : qui témoigne de l'affection à Ses amis par Ses faveurs. Et Sa parole :</p>
<p>« le Maître du Trône, »</p>
<p>c'est-à-dire : son Seigneur, son Créateur et son Possesseur [à propos du Trône] ;</p>
<p>« le Glorieux, »</p>
<p>— lu avec rafʿ [en apposition à « Maître »] : le digne des attributs parfaits de hauteur ;</p>
<p>« l'Effecteur de ce qu'Il veut. »</p>
<p>c'est-à-dire : rien de ce qu'Il veut ne L'embarrasse — rien ne Le met en défaut : quand Il veut une chose, Il lui dit : « Sois ! » — et elle est.</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers un ensemble de finalités éducatives, dont les plus importantes :</p>
<ul>
<li>la justice d'Allah entre les gens, et leur rétribution conformément à leurs œuvres ;</li>
<li>le rappel de la grandeur d'Allah, de la perfection de Sa puissance et de Sa volonté, et de Sa qualification par tous les attributs de perfection.</li>
</ul>
<h2>L'évaluation</h2>
<ol>
<li>Je compare la rétribution des injustes et celle des croyants.</li>
<li>J'expose les attributs d'Allah, Puissant et Majestueux, indiquant la perfection de Sa puissance, à partir des versets.</li>
<li>Comment les attributs d'Allah, le Très-Haut, mentionnés dans les versets contribuent-ils à corriger mon comportement ?</li>
</ol>
<h3>L'enrichissement (istithmār)</h3>
<p>D'après Abū Mūsā al-Ashʿarī — qu'Allah l'agrée —, le Messager d'Allah — paix et bénédiction sur lui — a dit : « Allah donne certes du laxisme à l'injuste ; mais lorsqu'Il le saisit, Il ne le laisse pas échapper. » Il dit : puis il récita :</p>
<p>« Ainsi ton Seigneur saisit-Il, lorsqu'Il saisit les cités qui sont injustes. Sa saisie est douloureuse, terrible. » (Hūd, 102)</p>
<p>[Ṣaḥīḥ al-Bukhārī : Livre de l'exégèse du Coran, chapitre de Sa parole — glorifié et exalté soit-Il :]</p>
<ol>
<li>Quel est le sens de « Allah donne du laxisme à l'injuste » (yumliya) ?</li>
<li>Quel est le sens de « lorsqu'Il le saisit, Il ne le laisse pas échapper » ?</li>
</ol>
<h2>La préparation préalable</h2>
<p>Je lis les versets 17 à 22 de la sourate al-Burūj et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« T'est-il parvenu le récit des armées » (al-Burūj, 17) ;</p>
<p>« de Pharaon et de Thamūd » (al-Burūj, 18) ;</p>
<p>« alors qu'Allah, derrière eux, les enveloppe » (al-Burūj, 20) ;</p>
<p>« Non ! C'est un Coran glorieux » (al-Burūj, 21).</p>
<p>[Expressions restituées d'après les versets 17 à 22 de la sourate al-Burūj (leçon suivante) : les lignes imprimées correspondantes sont vides dans la source numérisée — perte OCR.]</p>
<ul>
<li>Comment Allah, Puissant et Majestueux, a-t-Il répondu aux négateurs du Noble Coran ?</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "14005":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 14005 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 14005 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
