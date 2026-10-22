#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade LLM→main : leçon 13936 (tafsir-5ep, Sourate al-Inshiqāq 1-9, leçon 21).

Vérifications :
- Citations coraniques PERDUES par l'OCR (paragraphes vides) → restaurées du
  canonique quran-cache.json : Inshiqāq 84:1-9 ; hadith ʿĀʾisha (1re narration)
  = 84:8, 2e narration = 84:7-8 (le span imprimé « الانشقاق: 8-7 » a l'ordre
  inversé — corrigé) ; préparation = 84:10-14 (leçon SUIVANTE 13979).
- TABLE شرح dégradée : gloses seules — termes restitués des versets (انشقت /
  أذنت / وحقت / مدت / كادح).
- Note grammaticale du jawāb elidé : trois estimations (لقي الإنسان عمله /
  فملاقيه / ما أحضرت) + renvoi Takwīr-Infiṭār conservées.
- Hadiths Bukhārī (kitāb al-riqāq, « من نوقش الحساب عذب ») avec les deux
  narrations ʿĀʾisha ; hadith du corps « ومن نوقش الحساب هلك » (kitāb
  al-tafsīr) — variantes imprimées conservées telles quelles.
- Fin de leçon : le second groupe (livre derrière le dos) renvoyé à la leçon
  suivante (13979) — annonce conservée.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-5ep.json"

HTML_FR = """<h1>La sourate al-Inshiqāq — le Tafsīr al-Jalālayn des versets 1 à 9</h1>
<p>Leçon de tafsīr de la sourate al-Inshiqāq (versets 1 à 9) selon le Tafsīr al-Jalālayn — de Jalāl al-Dīn al-Maḥallī (mort en 864 H) et Jalāl al-Dīn al-Suyūṭī (mort en 911 H) — pour les élèves de la cinquième année de l'enseignement primaire traditionnel (taʿlīm ʿatīq), phase 2, leçon 21.</p>
<h2>Objectifs de la leçon</h2>
<ul>
<li>Reconnaître la sourate al-Inshiqāq et ses contenus fondamentaux.</li>
<li>Dégager des versets certaines marques précurseurs du Jour de la Résurrection.</li>
<li>Incarner l'œuvre juste, pour recevoir mon livre en ma main droite et être joyeux de la rencontre de mon Seigneur.</li>
</ul>
<h2>Introduction (tamhīd)</h2>
<p>La sourate al-Inshiqāq est mecquoise et compte vingt-cinq versets. Sa raison d'être après la sourate al-Muṭaffifīn : la première a parlé des livres des gardiens et de leur lieu ; la seconde est venue [exposer] la manière dont ces livres seront présentés au Jour de la Résurrection ; elle a parlé des signes de l'Heure et du jour de la résurrection, et de la diversité des états des gens en ce jour, entre bienheureux et malheureux.<br>
Quelles sont les marques précurseurs du Jour de la Résurrection ? Et comment sera le compte des croyants en ce jour ?</p>
<h2>Les versets</h2>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Quand le ciel se fendra, (1) et qu'il aura entendu son Seigneur — comme il était juste qu'il le fît —, (2) et que la terre sera étendue, (3) et qu'elle aura rejeté ce qu'elle renferme et s'en sera vidée, (4) et qu'elle aura entendu son Seigneur — comme il était juste qu'elle le fît — ! (5) Ô homme ! Tu peines vers ton Seigneur avec peine, et tu Le rencontreras. (6) Quant à celui qui recevra son livre en sa main droite, (7) il sera soumis à un compte facile, (8) et il retournera aux siens, joyeux. (9) » (al-Inshiqāq, 1-9)</p>
<p>[Citations coraniques restaurées d'après le corpus canonique : les emplacements imprimés correspondants sont vides dans la source numérisée — perte OCR.]</p>
<h2>La compréhension</h2>
<h3>Explication des termes</h3>
<p>[Table imprimée dégradée : seules les gloses ont survécu à la numérisation ; les termes ont été restitués d'après les versets.]</p>
<ul>
<li>inshaqqat (s'est fendue) : s'est fissurée et disjointe.</li>
<li>adhinat (aura entendu) : a entendu et obéi.</li>
<li>wa-ḥuqqat (comme il était juste) : il lui était juste d'entendre et d'obéir.</li>
<li>muddat (étendue) : accrue en largeur.</li>
<li>kādiḥun (tu peines) : luttant dans ton œuvre.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ol>
<li>De quoi Allah, Puissant et Majestueux, a-t-Il averti l'homme au début de la sourate ?</li>
<li>Comment sera le compte des gens de la droite ?</li>
</ol>
<h2>Le commentaire (tafsīr)</h2>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : les terreurs du Jour de la Résurrection</h3>
<p>La Vérité, glorifié soit-Il, a exposé aux débuts de cette sourate certaines terreurs du Jour de la Résurrection, et le Très-Haut a dit :</p>
<p>« Quand le ciel se fendra, »</p>
<p>c'est-à-dire : il se fendra et se disjoindra.</p>
<p>« et qu'il aura entendu son Seigneur »</p>
<p>c'est-à-dire : il aura entendu l'ordre de son Seigneur et obéi dans le fendage.</p>
<p>« — comme il était juste qu'il le fît — »</p>
<p>c'est-à-dire : il lui était juste d'entendre et d'obéir à l'ordre de son Seigneur.</p>
<p>« et que la terre sera étendue »</p>
<p>— sa largeur a été accrue comme on étend le cuir, et il ne restera sur elle ni construction ni montagne.</p>
<p>« et qu'elle aura rejeté ce qu'elle renferme »</p>
<p>c'est-à-dire : elle aura fait sortir à sa surface ce qui était en son ventre : les morts.</p>
<p>« et s'en sera vidée »</p>
<p>c'est-à-dire : de ce qui était en son ventre.</p>
<p>« et qu'elle aura entendu son Seigneur — comme il était juste qu'elle le fît — ! »</p>
<p>— en tout cela, c'est-à-dire : elle aura entendu et répondu ; c'est-à-dire : il lui était juste d'entendre, de répondre et d'obéir. Et tout cela aura lieu au Jour de la Résurrection.</p>
<p>Et la réponse [à « Quand… »] — elle et ce qui lui est coordonné — est élidée ; ce qui suit l'indique, et son estimation est : « l'homme a rencontré son œuvre », ou [c'est] « et tu Le rencontreras » (fa-mulāqīhi), ou « ce qu'elle a fait surgir » ; et son pareil [se trouve] aux sourates al-Takwīr et al-Infiṭār.</p>
<h3>Deuxièmement : l'aisance du compte des gens de la droite</h3>
<p>Après l'exposé de certaines terreurs du Jour de la Résurrection, le Noble Coran revient rappeler à l'homme qu'il sera rétribué de sa peine et de son œuvre en ce bas monde, et dit :</p>
<p>« Ô homme ! »</p>
<p>— vise le genre humain, et comprend le croyant et le négateur.</p>
<p>« Tu peines vers ton Seigneur »</p>
<p>c'est-à-dire : luttant et t'appliquant dans ton œuvre,</p>
<p>« vers ton Seigneur »</p>
<p>c'est-à-dire : vers la rencontre de ton Seigneur après la mort, pour trouver auprès de Lui ce que tu as œuvré de bien ou de mal.</p>
<p>« avec peine (kadḥan) »</p>
<p>c'est-à-dire : d'une lutte sérieuse.</p>
<p>« et tu Le rencontreras »</p>
<p>c'est-à-dire : tu rencontreras ton œuvre mentionnée — de bien ou de mal — au Jour de la Résurrection.</p>
<p>Puis le Glorifié et Très-Haut mentionna la division des gens en deux factions au Jour de la Résurrection, et commença par la première, et dit :</p>
<p>« Quant à celui qui recevra son livre en sa main droite, »</p>
<p>c'est-à-dire : quant à celui qui recevra le livre de ses œuvres en sa main droite — le croyant —, il sera soumis à un compte aisé : ses œuvres lui seront présentées, et après la présentation il en sera excusé — comme [il est dit] dans le hadith des deux Ṣaḥīḥ : « Quiconque est confronté au compte est perdu. » [Ṣaḥīḥ al-Bukhārī : Livre de l'exégèse du Coran — chapitre « il sera soumis à un compte facile »]</p>
<p>Puis le Très-Haut dit :</p>
<p>« et il retournera aux siens, joyeux »</p>
<p>c'est-à-dire : il retournera aux siens, au Paradis, joyeux de ce qu'Allah lui a donné de faveur et de noblesse.</p>
<p>Quant à la seconde faction — ceux qui recevront leur livre derrière leur dos —, elle fait l'objet de la leçon suivante.</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers un ensemble de finalités éducatives, dont les plus importantes :</p>
<ul>
<li>l'invitation à tirer leçon et à se laisser impressionner par les terreurs de la Résurrection ;</li>
<li>tout ce que l'homme fait et avance, il le retrouvera conservé auprès de son Seigneur, et en sera rétribué — fut-ce en bien ou en mal ;</li>
<li>l'affirmation de la justice divine, en rétribuant chacun de ce que contient le livre de ses œuvres.</li>
</ul>
<h2>L'évaluation</h2>
<ul>
<li>Je présente la sourate al-Inshiqāq et expose sa connexion avec la sourate précédente.</li>
<li>Je conclus des versets certaines terreurs de la Résurrection.</li>
<li>Quelle est la réponse à [« Quand… »] dans la parole du Très-Haut : « Quand le ciel se fendra… » (al-Inshiqāq, 1-4) — et ce qui la suit ?</li>
<li>Quelle est la voie que j'emprunte en cette vie pour recevoir mon livre en ma main droite et être parmi les sauvés dans l'au-delà ?</li>
</ul>
<h3>L'enrichissement (istithmār)</h3>
<p>D'après ʿĀʾisha — qu'Allah l'agrée —, d'après le Prophète — paix et bénédiction sur lui —, il a dit : « Quiconque est confronté au compte sera châtié. » Elle dit : Je dis : Allah, le Très-Haut, ne dit-Il pas :</p>
<p>« il sera soumis à un compte facile » (al-Inshiqāq, 8)</p>
<p>Il dit : « Cela est la présentation (ʿarḍ). » [Ṣaḥīḥ al-Bukhārī, Livre de l'attendrissement des cœurs (al-riqāq), chapitre « quiconque est confronté au compte sera châtié »]</p>
<p>Et dans une autre narration d'après ʿĀʾisha — qu'Allah l'agrée — : le Messager d'Allah — paix et bénédiction sur lui — a dit : « Nul ne rendra compte au Jour de la Résurrection sans périr. » Je dis : Ô Messager d'Allah, Allah n'a-t-Il pas dit :</p>
<p>« Quant à celui qui recevra son livre en sa main droite, il sera soumis à un compte facile » (al-Inshiqāq, 7-8)</p>
<p>Le Messager d'Allah — paix et bénédiction sur lui — dit alors : « Cela n'est que la présentation (ʿarḍ) ; et nul n'est confronté au compte au Jour de la Résurrection sans être châtié. » [Ṣaḥīḥ al-Bukhārī : Livre de l'attendrissement des cœurs (al-riqāq) — chapitre « quiconque est confronté au compte sera châtié »]</p>
<ol>
<li>Quel est le sens de « Quiconque est confronté au compte sera châtié » ?</li>
<li>Quelle est la différence entre la présentation (ʿarḍ) et le compte (ḥisāb) ?</li>
</ol>
<h2>La préparation préalable</h2>
<p>Je lis les versets 10 à 15 de la sourate al-Inshiqāq et je réponds à ce qui suit :</p>
<ul>
<li>J'explique les expressions suivantes :</li>
</ul>
<p>« Quant à celui qui recevra son livre derrière son dos » (al-Inshiqāq, 10) ;</p>
<p>« il appellera bientôt la perdition sur lui » (al-Inshiqāq, 11) ;</p>
<p>« et il brûlera dans un feu ardent » (al-Inshiqāq, 12) ;</p>
<p>« Il pensait qu'il ne retournerait jamais [vers Allah] » (al-Inshiqāq, 14).</p>
<p>[Expressions restituées d'après les versets 10 à 15 de la sourate al-Inshiqāq (leçon suivante) : les lignes imprimées correspondantes sont vides dans la source numérisée — perte OCR.]</p>
<ul>
<li>Qui sont ceux qui recevront leur livre derrière leur dos ? Et pourquoi ?</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13936":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13936 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13936 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
