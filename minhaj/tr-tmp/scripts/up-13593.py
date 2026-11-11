#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13593 (tafsir-tanawi-2, Sourate al-Isrāʾ
37-40, leçon 11 du manuel — al-Muḥarrar al-wajīz d'Ibn ʿAṭiyya).

Vérifications et restitutions :
- Bloc d'ouverture (17:37-40) : <p> vide après « الآيات » → restauré du
  quran-cache (4 versets).
- Citations inline perdues par l'OCR :
  * v37 complet après « قال تعالى : » ; qirāʾa مرحا : maṣdar (ḍamma/maftūḥ
    mīm-rāʾ chez le jumhūr) vs ism fāʿil (kasra du rāʾ) ; maṣdar en ḥāl,
    majāz ʿaqlī, mafʿūl muṭlaq du verbe « يمشي » ;
  * v37 p2 (لن تخرق الأرض…) après « فقال : » (tauhum/tehkom du fier) ;
  * v38 complet après « ثم قال تعالى : » ; qirāʾat سيئه (Kufans + Ibn
    ʿĀmir, iḍāfa) vs سيئة (Ibn Kathīr/Nāfiʿ/Abū ʿAmr) ;
  * dans le taʾwīl de سيئه : « من قوله تعالى : [v22 لا تجعل مع الله إلها
    آخر — DEBUT de la série des interdits] » + citation finale masculine
    = v38 lui-même ; dans le 1er taʾwīl de سيئة : A = v36 (ولا تقف),
    B = v37 (ولا تمش), D = v38 ; mot « ذلك » (2e taʾwīl) ; iʿrāb de
    « مكروها » : 4 facettes — kāna / sayyiʾatan / dhālika + ʿinda
    rabbika en adjectif de makrūhan (4e facette reconstituée : le source
    ne garde que 3 slots, la lecture al-Baḥr standard) ;
  * v39 p1 (ذلك مما أوحى… الحكمة) ; v39 p2 (ولا تجعل… ملوما مدحورا) ;
    mot « ولا تجعل » coordonné aux interdits précédents ;
  * v40 (أفأصفاكم ربكم بالبنين…) ;
  * citation à réf imprimée « الزمر: 5 » : le contenu (Ibn ʿAṭiyya sur
    17:40) = az-Zumar 39:4 (لو أراد الله أن يتخذ ولدا…) → canonique en
    principal + note de la réf imprimée (5) ;
  * Abū Ḥayyān (istithmār) : v22-fin et v39-fin restituées (مذموما
    مخذولا vs ملوما مدحورا — son propos même).
- Heading « Le commentaire (tafsīr) » absent du source (l'intro « اشتملت
  هذه الآيات » arrive nue) → restitué (convention du corpus), noté.
- Lexique : la 1re entrée imprimée « ملوما : مسرورا بدنياه مقبلا على
  راحته » est un MALLABELING OCR — la glose est celle de مَرَحًا (v37,
  cf. le tafsīr même de la leçon) → terme restitué مَرَحًا, doublon
  « ملوما » réel conservé en 3e entrée.
- Réf Abū Ḥayyān « 51/7 » inversée → 7/51 (doctrine R113).
- iʿdād (versets 41-44 = leçon suivante 13597) : 3 expressions restituées
  de son lexique : صرفنا / ليذكروا / نفورا ; la citation « استحالة وجود
  الشريك par syllogisme » = v42 (dalīl du tamānuʿ : “ S'il y avait des
  divinités avec Lui… ”).
- GT non copié ; hadith absent ; réfs fidèles.
"""

import json

BOOK = "/home/z/my-project/content/books/tafsir-tanawi-2.json"

HTML_FR = """<h1>La sourate al-Isrāʾ — <em>al-Muḥarrar al-wajīz</em> d’Ibn ʿAṭiyya, versets 37 à 40</h1>
<p>Leçon d’exégèse de la sourate al-Isrāʾ, versets 37 à 40, du livre du Tafsīr à travers <em>al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz</em> du cadi Abū Muḥammad Ibn ʿAṭiyya, à l’intention des élèves de la deuxième année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>), phase 2 (leçon 11).</p>
<h3>Les objectifs de la leçon</h3>
<ul>
<li>Reconnaître quelques convenances de la marche et les dangers de l’orgueil.</li>
<li>Conclure des versets l’exonération de Dieu, Puissant et Majestueux, de l’associé et de l’enfant.</li>
<li>Incarnar le caractère d’humilité, et éviter toute conduite qui suggère la morgue et la supériorité sur les gens.</li>
</ul>
<h3>Introduction (tamhīd)</h3>
<p>Après que Dieu, le Très-Haut, eut interdit aux gens de suivre ce dont ils n’ont point science des paroles, Il interdit en ces versets la morgue et la marche de déhanche, et ordonna au musulman de s’en tenir aux valeurs d’humilité avec Dieu et avec les gens ; puis Il avertit que ces ordres et ces interdits sont révélation divine et sagesse seigneuriale — fondements du bonheur des deux demeures ; enfin les versets s’achèvent sur l’exonération de Dieu, Puissant et Majestueux, de l’associé et de l’enfant.</p>
<p>Pourquoi donc Dieu, Puissant et Majestueux, a-t-Il interdit la marche orgueilleuse ? Et quelle est la rétribution de l’au-delà pour qui assigne à Dieu une autre divinité ?</p>
<h3>Les versets</h3>
<p>Allah, le Très-Haut, a dit :</p>
<p>« Et ne foule pas la terre avec orgueil : (37) tu ne sauras jamais fendre la terre et tu ne pourras jamais atteindre la hauteur des montagnes ! (38) Ce qui est mauvais en tout cela est détesté de ton Seigneur. (39) Tout cela fait partie de ce que ton Seigneur t’a révélé de la Sagesse. N’assigne donc pas à Allah d’autre divinité, sinon tu seras jeté dans l’Enfer, blâmé et repoussé. (40) Votre Seigneur, aurait-Il réservé exclusivement pour vous des fils, et Lui, aurait-Il pris pour Lui des filles parmi les Anges ? Vous prononcez là une parole monstrueuse. » (al-Isrāʾ, 37-40)</p>
<p>[Citations coraniques restaurées d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR.]</p>
<h3>La compréhension</h3>
<h4>Explication des termes</h4>
<ul>
<li><em>marḥan</em> (avec orgueil) : enjoué de son bas-monde, porté à son aise.</li>
<li><em>lan takhruqa l-arḍa</em> (tu ne sauras fendre la terre) : tu ne couperas point la terre ni ne l’essuieras par ta marche.</li>
<li><em>malūman</em> (blâmé) : l’objet du reproche, à qui l’on condamne ce qu’il a fait.</li>
<li><em>madḥūran</em> (repoussé) : le banni humilié, éloigné de la miséricorde de Dieu.</li>
</ul>
<h3>Extraction des idées des versets</h3>
<ul>
<li>De quoi Dieu, Puissant et Majestueux, a-t-Il interdit au début des versets ?</li>
<li>Qu’est-ce que les associateurs arabes attribuaient à Dieu, Puissant et Majestueux ?</li>
</ul>
<h3>Le commentaire (tafsīr)</h3>
<p>[Heading absent de la source numérisée — restitué selon la convention du corpus.]</p>
<p>Ces versets comprennent ce qui suit :</p>
<h3>Premièrement : l’interdit de l’orgueil et de la marche de déhanche</h3>
<p>Le Très-Haut a dit :</p>
<p>« Et ne foule pas la terre avec orgueil : tu ne sauras jamais fendre la terre et tu ne pourras jamais atteindre la hauteur des montagnes ! »</p>
<p>[Citation coranique (v. 37) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>L’interlocution s’adresse au Prophète — paix et bénédiction sur lui —, et vise tous les gens. Le <em>jumhūr</em> lut au <em>fatḥa</em> du <em>mīm</em> et du <em>rāʾ</em> : infinitif de <em> mariḥa yamraḥu</em>, “ il s’enjoue ”, quand il devient enjoué de son bas-monde, porté à son aise — tel est le <em>marḥ</em> : il est interdit à l’homme, en ce verset, que sa marche en terre soit de cette allure. On lut aussi <em>marḥan</em> au <em>kasra</em> du <em>rāʾ</em>, sur le schème du nom d’agent.</p>
<p>[<em>Marḥan</em>] est un infinitif (<em>maṣdar</em>) advenu en position d’état (<em>ḥāl</em>) du pronom ; et la venue de l’infinitif en <em>ḥāl</em>, comme sa venue en adjectif, vise l’excès dans le caractère. Il se résout en nom d’agent — c’est-à-dire : ne marche point, enjoué (<em>māriḥan</em>) —, la marche de l’enjoué : celle qui dénote la morgue du marcheur par balancement et déhanchement. Il est loisible aussi que <em>marḥan</em> soit un complément absolu du verbe [“ marcher ” (<em>yamshī</em>)], précisant l’espèce : la marche de qui s’enjoue — l’attribut de l’enjouement à la marche étant métaphore intellectuelle (<em>majāz ʿaqlī</em>).</p>
<p>Puis le Très-Haut affermit l’interdit de la déhanche et de la morgue. Il dit :</p>
<p>« tu ne sauras jamais fendre la terre et tu ne pourras jamais atteindre la hauteur des montagnes ! »</p>
<p>— moquerie du fier, et motif de l’interdit précédent : tu ne couperas point la terre ni ne l’essuieras par ta marche, et n’atteindras point en hauteur les montagnes pour les égaler en stature : puisque tu es tel, te restreindre à ce qu’exige le vrai, en marche et en agir, est plus juste et plus dû.</p>
<p>[Citation coranique (v. 37, fin) et mot « yamshī » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Ibn ʿAṭiyya [dit] : l’engouement des gens pour la chasse et ce qui s’en approche, en délassement sans besoin, entre dans ce verset ; mais l’homme qui se repose le jour rare, ou l’heure de son jour, y rafraîchissant son âme par le divertissement et le repos, pour s’en aider en une œuvre de bien — lecture de science ou priée —, cela n’entre point en ce verset.</p>
<p>Puis le Très-Haut dit :</p>
<p>« Ce qui est mauvais en tout cela est détesté de ton Seigneur. »</p>
<p>[Citation coranique (v. 38) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Les Kufans et Ibn ʿĀmir lurent <em>sayyiʾahu</em>, avec annexation du <em>sayyiʾ</em> au pronom ; Ibn Kathīr, Nāfiʿ et Abū ʿAmr lurent <em>sayyiʾatan</em>.</p>
<p>Quant à la lecture <em>sayyiʾahu</em> avec annexation : <em>sayyiʾuhu</em> est le nom de <em>kāna</em>, et “ détesté ” son prédicat. Son sens fut dirigé en ceci : Dieu, le Très-Haut, a mentionné avant cela des choses — dont Il a ordonné les unes et interdit les autres — ; le sens est alors : ce qui, de ces qualités mentionnées avant, depuis Sa parole, le Très-Haut :</p>
<p>« N’assigne point à Allah d’autre divinité ; » (al-Isrāʾ, 22)</p>
<p>jusqu’à ce verset, fut un mal : il est détesté auprès de Dieu — car si nous jugeions que tout ce qui fut mentionné avant est un mal (<em>sayyiʾa</em>), il faudrait dire “ détestée ” (<em>makrūha</em>) au féminin ; or il n’en est rien, puisque le Très-Haut a dit :</p>
<p>« Ce qui est mauvais en tout cela est détesté de ton Seigneur. » (al-Isrāʾ, 38 — lecture à l’annexation)</p>
<p>Et la lecture à l’annexation fait le sens : le mal de ces classes-là sera détesté — et le discours se tient droit.</p>
<p>[Citations coraniques (v. 22 ; v. 38) restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR. La série des interdits s’ouvre au v. 22 — identification par l’exégèse même.]</p>
<p>Quant à la lecture de Nāfiʿ, d’Ibn Kathīr et d’Abū ʿAmr : <em>sayyiʾatan</em> (“ un mal ”) est le prédicat de <em>kāna</em>, son nom un pronom caché. Son sens fut dirigé en des facettes :</p>
<ul>
<li>Première : les ordres et les interdits précédents s’achevèrent à Sa parole :</li>
</ul>
<p>« Et ne poursuis pas ce dont tu n’as aucune connaissance. » (al-Isrāʾ, 36)</p>
<p>puis Il recommença et dit :</p>
<p>« Et ne foule pas la terre avec orgueil… » (al-Isrāʾ, 37)</p>
<p>puis Il dit :</p>
<p>« Ce qui est mauvais en tout cela est détesté de ton Seigneur. » (al-Isrāʾ, 38)</p>
<p>— le visé est alors ces dernières choses que Dieu a interdites.</p>
<ul>
<li>Seconde : le visé par Sa parole : [“ cela ” (<em>dhālika</em>)] est tout ce que Dieu a interdit en ce qui précède.</li>
</ul>
<p>[Citations coraniques (v. 36 ; v. 37 ; v. 38) et mot « dhālika » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Le visé, ici, par “ détesté ” (<em>makrūh</em>), est l’interdit (<em>ḥarām</em>) — non le “ détesté ” reçu chez les juristes, qui est au-dessous de l’interdit. Ils mentionnèrent, en l’<em>iʿrāb</em> de [“ détesté ” (<em>makrūhan</em>)], des facettes :</p>
<ul>
<li>Première : second prédicat de [<em>kāna</em> (fut)], portant sur le mot <em>kull</em> — l’estimation : tout cela fut un mal détesté.</li>
<li>Seconde : apposition de [<em>sayyiʾatan</em> (un mal)] ou son adjectif — car son féminin n’étant pas de vérité, il se peut qu’il soit décrit par un masculin.</li>
<li>Troisième : il y a antéposition et postposition — l’estimation : tout cela fut détesté, et un mal, auprès de ton Seigneur.</li>
<li>Quatrième : il est un état (<em>ḥāl</em>) du mentionné en Sa parole : [“ cela ” (<em>dhālika</em>)] ; et Sa parole : [“ auprès de ton Seigneur ” (<em>ʿinda rabbika</em>)] est en position d’adjectif de [“ détesté ” (<em>makrūhan</em>)].</li>
</ul>
<p>[Mots de la discussion d’iʿrāb restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>En somme, le sens est : tout ce qui fut mentionné, que Dieu a interdit, son œuvre fut laide et interdite auprès de Dieu, le Très-Haut.</p>
<p>Puis le Glorifié clôt en exposant que ces règles sont révélation et sagesse de Dieu. Il dit :</p>
<p>« Tout cela fait partie de ce que ton Seigneur t’a révélé de la Sagesse. »</p>
<p>— l’indexation de “ cela ” porte sur ces convenances et règles que contiennent les versets précédents : celles-ci relèvent des actes réglés qu’exige la sagesse de Dieu en Ses serviteurs, et Sa création pour eux des mœurs excellentes ; la sagesse est l’ensemble des lois des sens réglés et des actes vertueux.</p>
<p>[Citation coranique (v. 39, début) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<h3>Deuxièmement : l’unicité de Dieu, Puissant et Majestueux, et Son exonération de ce qui ne Lui sied pas</h3>
<p>Comme Dieu, le Très-Haut, avait ouvert ces counsels par l’appel à l’unicité, Il les clôt par l’appel à l’unicité. Le Glorifié dit :</p>
<p>« N’assigne donc pas à Allah d’autre divinité, sinon tu seras jeté dans l’Enfer, blâmé et repoussé. »</p>
<p>Sa parole : [“ et n’assigne point ” (<em>wa-lā tajʿal</em>)] est coordonnée aux interdits précédents ; l’interlocution s’adresse au Prophète — paix et bénédiction sur lui —, et vise quiconque des hommes entendit le verset.</p>
<p>[Citation coranique (v. 39, fin) et mot « wa-lā tajʿal » restaurés d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Après que le Glorifié eut averti de la gravité du polythéisme envers Dieu et de son issue, Il y fit suivre le reproche à ceux qui Lui attribuèrent un enfant. Il dit :</p>
<p>« Votre Seigneur, aurait-Il réservé exclusivement pour vous des fils, et Lui, aurait-Il pris pour Lui des filles parmi les Anges ? Vous prononcez là une parole monstrueuse. »</p>
<p>L’interrogation y vaut la négation et le reproche ; l’interlocution s’adresse aux associateurs arabes, qui disaient : les anges sont les filles de Dieu.</p>
<p>[Citation coranique (v. 40) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>
<p>Le visé du noble verset est la négation, en la plus éloquente manière, de leur prétention que les anges sont les filles de Dieu — car Dieu, Puissant et Majestueux, est exonéré de l’associé, de l’enfant, du père et du semblable. Le Très-Haut dit :</p>
<p>« Si Allah avait voulu S’attribuer un enfant, Il aurait certes choisi ce qu’Il eût voulu parmi ce qu’Il crée. Gloire à Lui ! C’est Lui Allah, l’Unique, le Dominateur suprême. » (az-Zumar, 4 — le manuel imprime « 5 »)</p>
<p>[Citation coranique (az-Zumar, 4) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; référence imprimée « 5 » notée.]</p>
<h3>Troisièmement : les finalités des versets</h3>
<p>Ces versets orientent vers la réalisation d’un ensemble de finalités éducatives, dont :</p>
<ul>
<li>L’importance de l’humilité avec les gens, l’abstention de la morgue sur eux, et la purification des âmes de toute maladie et mauvaise moeur — au premier rang desquelles le polythéisme, l’ostentation, l’auto-admiration et l’orgueil. La santé des cœurs de ces maladies se répercute sur le comportement extérieur de l’homme, car il s’affranchit de l’égoïsme, du ressentiment, de l’ostentation et de l’auto-admiration qui outrecuide l’âme et l’asservit.</li>
<li>Les mauvaises mœurs concourent à la dissolution de la société et à l’affaiblissement de la confiance entre ses membres ; les mœurs excellentes et l’humilité sont un caractère généreux qui contribue à répandre l’affection et l’harmonie entre les composantes de la société, et aide à bâtir la confiance sur laquelle se fondent la coopération et l’entraide.</li>
<li>Toute la Loi de Dieu est révélation et sagesse : qui s’y tient s’est guidé vers la voie droite ; qui s’en détourne et s’en écarte a perdu le chemin.</li>
<li>L’appel à l’unicité de Dieu, Puissant et Majestueux, à ne point Lui associer, et à Son exonération de tout ce qui ne Lui sied pas en attributs — dont d’avoir un enfant, ou que les anges soient les filles de Dieu. Nombre de versets et de hadiths répondent à ces croyances corrompues que tenaient les associateurs.</li>
</ul>
<h3>L’évaluation (taqwīm)</h3>
<ul>
<li>Pourquoi Dieu, Puissant et Majestueux, a-t-Il interdit de fouler la terre avec orgueil ?</li>
<li>Que signifie la parole du Très-Haut : « Ce qui est mauvais en tout cela est détesté de ton Seigneur » — sur les deux lectures ?</li>
<li>Pourquoi les associateurs attribuèrent-ils à Dieu, Puissant et Majestueux, des filles ? Et comment Dieu leur répondit-Il ?</li>
</ul>
<h3>L’investissement (istithmār)</h3>
<p>« Le Très-Haut répéta l’interdit du polythéisme : dans le premier interdit,</p>
<p>« … sinon tu te trouveras méprisé et abandonné. » (al-Isrāʾ, 22)</p>
<p>et dans le second</p>
<p>« … sinon tu seras jeté dans l’Enfer, blâmé et repoussé. » (al-Isrāʾ, 39)</p>
<p>La différence entre <em>madhmūm</em> (méprisé) et <em>malūm</em> (blâmé) : être méprisé, c’est qu’il soit dit que l’acte qu’il a osé est laid et condamnable ; être blâmé, c’est qu’on lui dise, après l’acte et son blâme : “ Pourquoi as-tu fait cela ? Qu’est-ce qui t’y a porté ? Qu’en as-tu gagné, sinon d’attenter à toi-même ? ” — le blâme est le premier, le reproche le dernier. La différence entre <em>makhdhūl</em> (abandonné) et <em>madḥūr</em> (repoussé) : l’abandonné est celui dont l’aide et le secours sont délaissés, livré à lui-même ; le repoussé est le chassé, éloigné à titre d’ignominie et de mépris — le premier état est l’abandon, le dernier le renvoi couvert d’ignominie. C’est comme si la qualification de mépris et d’abandon relevait de ce monde, et celle de reproche et de bannissement, de l’au-delà — c’est pourquoi vint :</p>
<p>« … sinon tu seras jeté dans l’Enfer, blâmé et repoussé. » (al-Isrāʾ, 39) » [al-Baḥr al-Muḥīṭ, d’Abū Ḥayyān : 7/51 — réf. imprimée « 51/7 », ordre inversé]</p>
<p>[Citations coraniques (v. 22 et v. 39) de la citation d’Abū Ḥayyān restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR.]</p>
<p>Je contemple le texte et réponds à ce qui suit :</p>
<ul>
<li>Pourquoi le terme : “ et n’assigne point ” (<em>wa-lā tajʿal</em>)</li>
</ul>
<ul>
<li>se répète-t-il au début et à la fin de ces counsels ?</li>
<li>Quelle est la différence entre les deux rétributions portées par les deux versets ?</li>
</ul>
<h3>La préparation (iʿdād)</h3>
<p>Je contemple les versets 41 à 44 de la sourate al-Isrāʾ et réponds à ce qui suit :</p>
<ul>
<li>Je recherche la portée des expressions suivantes :</li>
</ul>
<p><em>ṣarafnāhu</em> (صَرَفْنَاهُ — Nous l’avons exposé).</p>
<p><em>li-yadhkurū</em> (لِيَذَّكَّرُوا — qu’ils se rappellent).</p>
<p><em>nufūran</em> (نُفُورًا — la répulsion).</p>
<p>[Expressions restituées du lexique de la leçon suivante (versets 41-44) : les emplacements imprimés sont vides — perte OCR.]</p>
<ul>
<li>Je recherche les dires des exégètes sur la manière dont les êtres glorifient Dieu par Sa louange.</li>
</ul>
<ul>
<li>J’explicite la portée de la parole du Très-Haut :</li>
</ul>
<p>« Dis : “ S’il y avait des divinités avec Lui, comme ils le disent, elles auraient alors cherché un chemin [pour atteindre] le Détenteur du Trône ”. » (al-Isrāʾ, 42)</p>
<p>— sur l’impossibilité de l’existence d’un associé, à l’aide des règles du syllogisme logique.</p>
<p>[Citation coranique (v. 42, de la leçon suivante) restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13593":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13593 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13593 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
