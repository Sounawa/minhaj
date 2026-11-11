#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13005 (hadith-1es, des règles
propres à l'imam et au suivi — Muwaṭṭaʾ n° 351/352/355/356/357/360/362
+ Bukhārī/Muslim).

Conventions main (cf. 12875-13004 du même livre) :
- h1 « Des règles propres à l'imam et au suivi (aḥkām khāṣṣa bi-l-imām
  wa-l-maʾmūm) », 28e leçon ; titleFr officiel conservé.
- Préambule : états de l'imam et du maʾmūm + étiquettes du groupe —
  suivre la sunna, écarter divergence et division.
- Hadiths : 351 (Zayd b. Aslam/Busr b. Miḥjan (Banū l-Dīyl)/son père
  Miḥjan : resté au conseil sans prier — « qu'est-ce qui t'a empêché
  de prier avec les gens ? n'es-tu pas un homme musulman ? — j'ai
  prié avec les miens — quand tu viens, prie avec les gens, même
  ayant prié ») ; 357 (Abū Hurayra : « quand l'un de vous prie avec
  les gens, qu'il allège : parmi eux le faible, le malade, le
  vieillard ; et quand il prie pour soi, qu'il prolonge à souhait »)
  ; 360 (Ibn Shihāb/Anas : cheval, chute, flanc droit éraflé ; prière
  assis, eux assis derrière — « l'imam n'est institué que pour être
  suivi… et quand il prie assis, priez assis, tous ensemble »).
- Lexique : ṣallaytu fī ahlī (ma maison, avec les miens), fu-ṣuriʿa,
  juḥisha (éraflé — khashsh = peler la peau).
- Taḥlīl I : refaire avec l'imam — 352 (Ibn ʿUmar : « oui — laquelle
  est ma prière ? — cela t'appartient-il ? c'est à Dieu ») ; 355
  (maghrib/ṣubḥ atteints : ne pas répéter) ; 356 (Mālik : pas de mal
  SAUF le maghrib — répété il devient pair).
- Taḥlīl II : l'allègement — la Loi apporta l'aisance ; l'individu
  prolonge à souhait ; l'homme qui manque le ṣubḥ par la faute de
  l'imam prolongeant — colère : « parmi vous des repousseurs !
  quiconque guide les gens, qu'il abrege : derrière lui le petit, le
  grand et l'homme au besoin » (Bukhārī/Muslim) ; Ibn ʿAbd al-Barr
  (l'imam allège de son mieux — on ne sait ce qui survient) ;
  al-Yaʿmarī/al-Fākihānī (les règles tiennent au prépondérant, non au
  rare — comme le qaṣr du voyage, motivé par la peine mais légiféré
  même sans elle).
- Taḥlīl III : suivre l'imam — l'opposition invalide ; 360 + la
  narration des deux Shaykhs (Ḥumayd/Anas : « il pria avec eux assis
  tandis qu'ils étaient debout ») — conciliation : commencés debout,
  geste de s'asseoir (al-Zuhrī transmit l'un, Ḥumayd l'autre,
  ʿĀʾisha réunit les deux) ; Ibn ʿAbd al-Barr (Istidhkār) : addition
  de Maʿn « ne divergez pas sur lui » — preuve de Mālik/Thawrī/Abū
  Ḥanīfa + Successors de Médine et Koufa : diverger d'intention de
  son imam invalide (nulle divergence plus dure que celle des
  intentions) ; jumhūr : interdiction de prier assis au farḍ si l'on
  peut debout ; certains + Shāfiʿī : le debout suit l'assis malade
  (chacun son devoir selon sa force) ; la plupart des Mālikites :
  non, au farḍ comme à la surérogation.
- Istimḥār : 362 (Hishâm/son père : le Prophète malade trouve Abū
  Bakr debout guidant ; Abū Bakr recule ; geste « tel quel » ; s'assit
  à son côté ; Abū Bakr priait de la prière du Messager assis, le
  peuple de la prière d'Abū Bakr) + 1 question — **HADITH 362
  DOUBLÉ par OCR dans la source (2× avec la même question) — traduit
  une seule fois, précédent R118/180**.
- Pas d'iʿdād qablī dans la source (la leçon s'achève sur
  l'istimḥār) — fidèle au source.
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Des règles propres à l’imam et au suivi (<em>aḥkām khāṣṣa bi-l-imām wa-l-maʾmūm</em>)</h1>
<p>Leçon sur des règles propres à l’imam et au suivi, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la vingt-huitième leçon.</p>
<ol>
<li>Connaître quelques-unes des règles propres à l’imam et au suivi.</li>
<li>Comprendre l’aisance de la Loi en son ordre à l’imam d’alléger.</li>
<li>Prendre l’imam pour modèle en ma prière, pour gagner le salaire et la récompense.</li>
</ol>
<h2>Préambule</h2>
<p>L’imam et le suivi rencontrent, en la prière, des états qui requièrent de les connaître ; et il y a des étiquettes propres à la prière en commun auxquelles ils doivent l’un et l’autre se conformer — en suivi de la sunna, et en écart de la divergence et de la scission.</p>
<p>Quels sont ces états ? Et quelles règles s’y rattachent ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Zayd ibn Aslam, d’après un homme des Banū l-Dīyl nommé Busr ibn Miḥjan, d’après son père Miḥjan : « qu’il était en une séance avec le Messager de Dieu — paix et bénédiction sur lui — ; on appela à la prière ; le Messager de Dieu — paix et bénédiction sur lui — se leva et pria, puis revint — et Miḥjan en sa place, n’ayant point prié avec lui. Le Messager de Dieu — paix et bénédiction sur lui — lui dit : Qu’est-ce qui t’a empêché de prier avec les gens ? N’es-tu pas un homme musulman ? Il dit : Si, ô Messager de Dieu — mais j’ai prié avec les miens. Le Messager de Dieu — paix et bénédiction sur lui — lui dit : Quand tu viens, prie avec les gens, même si tu as déjà prié. » [Muwaṭṭaʾ, n° 351]</li>
<li>D’après Mālik, d’après Abū l-Zinad, d’après al-Aʿraj, d’après Abū Hurayra : « que le Messager de Dieu — paix et bénédiction sur lui — dit : Quand l’un de vous prie avec les gens, qu’il allège : parmi eux sont le faible, le malade et le vieillard ; et quand l’un de vous prie pour soi-même, qu’il prolonge autant qu’il veut. » [Muwaṭṭaʾ, n° 357]</li>
<li>D’après Mālik, d’après Ibn Shihāb, d’après Anas ibn Mālik : « que le Messager de Dieu — paix et bénédiction sur lui — monta un cheval, en fut jeté, et son flanc droit fut éraflé ; il pria l’une des prières assis, et nous prîmes derrière lui assis. Quand il eut fini, il dit : “L’imam n’est institué que pour être suivi : quand il prie debout, priez debout ; quand il s’incline, inclinez-vous ; quand il relève, relevez-vous ; quand il dit : Dieu entend celui qui Le loue, dites : Notre Seigneur, et à Toi la louange ; et quand il prie assis, priez assis — tous ensemble.” » [Muwaṭṭaʾ, n° 360]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>ṣallaytu fī ahlī</em> (« j’ai prié avec les miens ») : c’est-à-dire : je priai en ma maison, avec ma famille.</li>
<li><em>fu-ṣuriʿa</em> (« en fut jeté ») : il tomba du cheval.</li>
<li><em>juḥisha</em> (« fut éraflé ») : griffé — et le <em>khashsh</em> : l’écorchement de la peau.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Explicite le statut de qui pria en sa maison puis atteignit le groupe.</li>
<li>Définis le concept de prise de l’imam pour modèle, et comment il se réalise.</li>
<li>Mets en relief la sagesse de l’ordre à l’imam d’alléger sur les orants.</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : la reprise de la prière avec l’imam pour qui a déjà prié</h3>
<p>Qui pria l’obligation en particulier en sa maison, puis vint à la mosquée et trouva les gens prier : prie-t-il avec eux ou non ? Le statut de ce cas, le premier hadith l’expose — où le Messager de Dieu — paix et bénédiction sur lui — ordonna à l’homme qui avait prié en sa maison puis atteint le groupe d’entrer en la prière avec l’imam, pour gagner la récompense du groupe.</p>
<p>L’imam Mālik apporta d’autres rapports qui le renforcent, parmi eux : « qu’un homme interrogea ʿAbd Allāh ibn ʿUmar et dit : Voici que je prie en ma maison, puis j’atteins la prière avec l’imam — dois-je prier avec lui ? ʿAbd Allāh ibn ʿUmar lui dit : Oui. L’homme dit : Laquelle des deux dois-je compter pour ma prière ? Ibn ʿUmar lui dit : Cela t’appartient-il ? cela n’appartient qu’à Dieu — Il compte laquelle Il veut. » [Muwaṭṭaʾ, n° 352] Et l’imam Mālik apporta aussi, d’après Nāfiʿ, que ʿAbd Allāh ibn ʿUmar disait : « Quiconque pria le maghrib ou le point du jour, puis les atteignit avec l’imam, qu’il ne les recommence pas pour eux. » [Muwaṭṭaʾ, n° 355] Yaḥyā a dit : Mālik dit : « Et je ne vois pas de mal à ce que prie avec l’imam quiconque a déjà prié en sa maison — sauf la prière du maghrib : s’il la recommence, elle devient paire. » [Muwaṭṭaʾ, n° 356]</p>
<h3>Deuxièmement : l’ordre à l’imam d’alléger en la prière</h3>
<p>La Loi islamique indulgente vint avec l’aisance et la facilité, et la négation de la peine et de la gêne ; c’est pourquoi, en la prière qui est la plus grande des adorations, le Prophète — paix et bénédiction sur lui — ordonna à l’imam d’y alléger, pour qu’elle soit aisée et facile aux suivis, et qu’ils en sortent la désirant — car parmi les suivis est qui ne supporte pas la prolongation, soit par impotence, maladie ou besoin. Si l’orant est en particulier, qu’il prolonge autant qu’il veut : il ne lèse personne en cela.</p>
<p>Et indique la répréhension du Prophète — paix et bénédiction sur lui — de la prolongation qui lèse les gens : quand un homme vint à lui et l’informa qu’il se retardait de la prière du point du jour avec le groupe, à cause de l’imam qui prie avec eux et prolonge la prière — le Prophète — paix et bénédiction sur lui — se courrouça d’un courroux violent et dit : « Ô gens : parmi vous sont des repousseurs ! Quiconque de vous guide les gens, qu’il abrege : derrière lui sont le petit, le grand et l’homme au besoin. » [Rapporté par al-Bukhārī et Muslim]</p>
<p>Ibn ʿAbd al-Barr a dit : il sied à tout imam d’alléger de son mieux — de l’ordre qui lui fut fait d’alléger ; et quand l’imam connaît la force de qui est derrière lui, il ne sait ce qui peut leur survenir d’événement, d’occupation, d’occurrence de besoin, de rupture d’ablutions ou d’autre. Al-Yaʿmarī a dit : les règles ne s’attachent qu’au prépondérant, non à la forme rare — il sied donc aux imams d’alléger absolument ; dit-il : c’est comme le raccourcissement (<em>qaṣr</em>) légiféré en voyage, motivé par la peine — et il est légiféré malgré cela même sans peine, en travail du prépondérant : car on ne sait ce qui lui surviendra ; ici de même.</p>
<h3>Troisièmement : l’obligation de prendre l’imam pour modèle</h3>
<p>Des exigences de la prière en commun : prendre l’imam pour modèle et ne point s’opposer à lui — car son opposition invalide la prière, selon les savants. La preuve : ce qui vient au hadith du chapitre : « que le Messager de Dieu — paix et bénédiction sur lui — monta un cheval, en fut jeté, et son flanc droit fut éraflé ; il pria l’une des prières assis, et nous prîmes derrière lui assis. Quand il eut fini, il dit : L’imam n’est institué que pour être suivi… » ; et dans une narration des deux Shaykhs, de Ḥumayd, d’après Anas : “il pria avec eux assis, tandis qu’ils étaient debout”. La conciliation des deux narrations : ils commencèrent la prière debout ; il leur fit signe de s’asseoir et ils s’assirent — al-Zuhrī transmit l’un des deux [états] et Ḥumayd l’autre, et ʿĀʾisha — que Dieu soit satisfait d’elle — réunit les deux.</p>
<p>Ibn ʿAbd al-Barr dit dans l’<em>Istidhkār</em> : Maʿn ajouta, dans le <em>Muwaṭṭaʾ</em>, de Mālik : “ne divergez pas sur lui” — il y a là preuve pour la parole de Mālik, al-Thawrī, Abū Ḥanīfa et de la plupart des Suivants à Médine et à Koufa : celui dont l’intention diverge de l’intention de son imam, sa prière est invalide — car il n’est pas de divergence plus dure que la divergence des intentions, sur lesquelles roule l’édifice des œuvres.</p>
<p>Et le <em>jumhūr</em> des gens de science [tient] la non-permission de s’asseoir en la prière de devoir pour le capable de se tenir debout — qu’il soit imam, suivi ou particulier. Parmi eux, qui permit la prière du debout derrière l’imam malade assis : car chacun des deux s’acquitte de son devoir selon sa force — et al-Shāfiʿī y alla ; et ce qui est chez la plupart des Mālikites : le debout ne prend pas l’assis pour modèle, ni en obligation ni en surérogation.</p>
<h2>L’évaluation</h2>
<ul>
<li>Pourquoi l’Envoyé — paix et bénédiction sur lui — interdit-il la prolongation sur les orants ?</li>
<li>Détermine le statut des deux cas suivants, avec l’appui convenable :
<ul>
<li>Un homme s’assit à la mosquée pendant que les gens prient, prétextant qu’il a prié en sa maison.</li>
<li>L’imam pria assis pour excuse, et certains des gens prièrent derrière lui debout.</li>
</ul></li>
</ul>
<h2>L’exploitation</h2>
<p>D’après Mālik, d’après Hishām ibn ʿUrwa, d’après son père : « que le Messager de Dieu — paix et bénédiction sur lui — sortit en sa maladie, vint et trouva Abū Bakr debout, priant avec les gens ; Abū Bakr se retint en arrière, et le Messager de Dieu — paix et bénédiction sur lui — lui fit signe : Tel que tu es. Le Messager de Dieu — paix et bénédiction sur lui — s’assit auprès d’Abū Bakr : Abū Bakr priait de la prière du Messager de Dieu — paix et bénédiction sur lui — qui était assis, et les gens priaient de la prière d’Abū Bakr. » [Muwaṭṭaʾ, n° 362]</p>
<ul>
<li>Résume ce que ce hadith apporte.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13005":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13005 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13005 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
