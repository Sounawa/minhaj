#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16723 (tawhid-1es, leçon 11 — la volonté
divine (mašīʾa), la félicité et l'infortune).

Vérifications et restitutions (cache quran = Ḥafṣ ; sunnah.com UA navigateur) :
- Matn : « فكل ميسر بتيسيره إلى ما سبق من علمه وقدره من شقي أو سعيد... » —
  rendu fidèlement.
- HADITHS VÉRIFIÉS sunnah.com :
  * ʿImrān b. Ḥuṣayn « كل ميسر لما خلق له » → Bukhārī 7551 (Livre 97
    Tawḥīd, bāb « ولقد يسرنا القرآن للذكر » — EXACTEMENT le bāb imprimé par
    le manuel) — texte VERBATIM ;
  * Anas « إن الله وكّل بالرحم ملكا » → Bukhārī 3333 (Kitāb Aḥādīth
    al-Anbiyāʾ, voie ʿUbayd Allāh b. Abī Bakr b. Anas ← Anas) — texte
    recevable avec variantes de récit (في/بالرحم ; أن يخلقها/أن يقضي خلقه ;
    فما الرزق فما الأجل/فما الرزق والأجل ; « عز وجل » ajouté) ; la réf
    imprimée « كتاب الحيض باب مخلقة وغير مخلقة » désigne le bāb du hadith
    PARALLÈLE d'Ibn Masʿūd (3208) — divergence de localisation notée.
- CITATIONS VIDES (perte OCR) RESTAURÉES du cache, cibles doctrinales :
  * [الأنبياء: 23] → CONFORME (« لا يسأل عما يفعل وهم يسألون ») ;
  * [الرعد: 40] → Raʿd 39 « يمحوا الله ما يشاء ويثبت وعنده أم الكتاب » —
    réf d'adjacence (−1) notée ;
  * [التكوير: 29] → CONFORME (déjà restitué en la leçon 9) ;
  * [الأنعام: 62] → CONFORME (« ثم ردوا إلى الله مولاهم الحق ») ;
  * [فاطر: 15] → CONFORME (« أنتم الفقراء إلى الله » — cible univoque du
    ghināʾ) ;
  * [الأنعام: 103] → Anʿām 102 « خالق كل شيء » — réf d'adjacence (−1)
    notée (la série des trois : le Créateur unique) ;
  * [فاطر: 3] → CONFORME (« هل من خالق غير الله ») ;
  * [النحل: 17] → CONFORME (« أفمن يخلق كمن لا يخلق ») ;
  * [يونس: 49] (iʿdād) → CONFORME.
- JAWHARAT AL-TAWḤĪD (istithmār) : cinq vers imprimés en tableau à deux
  colonnes d'hémistiches [p. 162 du comm. Hidāyat al-murīd de l'auteur] ;
  l'ordre des colonnes de l'imprimé permute les hémistiches des vers 2 et 4
  (artefact de composition/OCR — l'ordre canonique de la Jawhara est suivi
  par les vers 1, 3 et 5) — ordre canonique restitué, noté ; le dernier
  vers (condensé de la doctrine du kasb) rendu au plus près de la lettre.
- Qāḍī ʿAbd al-Wahhāb (sharḥ al-Risāla) : « مذهب أئمة السنة وسلف الأمة » —
  rendu fidèlement.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la volonté divine (<em>mašīʾa</em>), la félicité et l’infortune</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la onzième leçon (11).</p>
<h2>Les objectifs</h2>
<ul>
<li>Connaître la croyance correcte au sujet de la volonté divine, de la félicité et de l’infortune.</li>
<li>Connaître les causes de l’infortune et de la félicité.</li>
<li>Suivre les causes de la félicité, les faire miennes, et éviter en ma vie les causes de l’infortune.</li>
</ul>
<h2>Préambule</h2>
<p>Nous voyons et observons des gens commettre les interdits et les transgressions, et dilapider les obéissances — mais voici que leurs états se retournent bientôt : ils s’appliquent aux biens et reviennent aux œuvres de piété et de bienfaisance.</p>
<p>Quelle en est la cause ? Et qu’indique le retournement de l’homme des désobéissances vers les obéissances ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et chacun est facilité, par Sa facilitation, vers ce qui, de Sa science et de Sa prédestination, a précédé : malheureux ou heureux. Transcendant qu’Il soit qu’il soit, en Son royaume, ce qu’Il ne veut pas ; qu’il soit, pour quiconque, une dispense à l’égard de Lui ; ou qu’il soit créateur de quelque chose autre que Lui. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>shaqiyy</em> (malheureux) : l’infortune — le dommage qui s’attache en la dernière demeure.</li>
<li><em>saʿīd</em> (heureux) : la félicité — le profit qui s’attache en la dernière demeure ; et l’heureux est le musulman.</li>
<li><em>ghanī</em> (riche) : l’autosuffisance — l’absence de besoin.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> que les serviteurs sont facilités vers la félicité ou l’infortune.</li>
<li>J’extrais du <em>matn</em> qu’il n’advient point, en le royaume de Dieu, ce qu’Il ne veut pas.</li>
<li>J’extrais du <em>matn</em> l’indigence de l’homme envers son Seigneur.</li>
</ul>
<h2>L’analyse</h2>
<p>La leçon contient ce qui suit :</p>
<h3>Premièrement : la facilitation des serviteurs vers la félicité ou l’infortune</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Et chacun est facilité, par Sa facilitation, vers ce qui, de Sa science et de Sa prédestination, a précédé : malheureux ou heureux. » Au nombre de ce qu’il faut croire : chaque homme est facilité, préparé et conduit par la facilitation de Dieu vers la chose dont la science de Dieu et Sa prédestination ont précédé pour lui en la pré-éternité. D’ʿImrān b. Ḥuṣayn : je dis : « Ô Envoyé de Dieu, en vue de quoi agissent les agents ? » Il dit :</p>
<p>« Chacun est facilité pour ce en vue de quoi il fut créé. »</p>
<p>[<em>Ṣaḥīḥ</em> d’al-Bukhārī, Livre du Tawḥīd, chapitre de la parole de Dieu Très-Haut : « Et certes, Nous avons facilité le Coran pour le rappel » — vérifié : Bukhārī 7551, voie de ʿImrān b. Ḥuṣayn — texte verbatim.]</p>
<p>C’est-à-dire que chaque homme est conduit à faire ce qui, de la science de Dieu et de Sa prédestination, a précédé pour lui — infortune ou félicité — par l’accomplissement de ce qui y mène. Et le sens de la parole de l’auteur : « de Sa science et de Sa prédestination » est : de Sa volonté — la science et la prédestination visant ici les choses sues et les choses voulues.</p>
<p>Sa parole : « malheureux ou heureux » signifie que chacun, des malheureux et des heureux, est préparé à faire ce à quoi se sont attachées la volonté de Dieu et Sa science en la pré-éternité. Et il n’advient sur les serviteurs que ce dont Sa science, l’Elevé, et Sa prédestination, glorifié soit-Il, ont précédé : Il rend heureux qui Il veut, sans médiatrice qui précéda ; et écarte qui Il veut, sans crime qui précéda. Le glorifié dit :</p>
<p>« Il n’est point interrogé sur ce qu’Il fait — et eux, ils le seront. » (al-Anbiyāʾ, 23)</p>
<p>Et l’Elevé dit :</p>
<p>« Dieu efface ce qu’Il veut et confirme — et auprès de Lui est la Mère du Livre. » (al-Raʿd, 39)</p>
<p>[Deux citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la première référence imprimée CONFORME ; la seconde porte « 40 », la visée est le verset 39 — réf d’adjacence notée.] — c’est-à-dire : de ce qui est écrit sur Ses serviteurs. D’Anas b. Mālik — que Dieu l’agrée — d’après le Prophète — paix et bénédiction sur lui :</p>
<p>« Certes, Dieu, Puissant et Magnifié, chargea de la matrice un ange, qui dit : Seigneur, une goutte ! Seigneur, une adhérence ! Seigneur, un embryon ! Et lorsqu’Il veut parfaire sa création, il dit : mâle ou femelle ? malheureux ou heureux ? — et quoi ? la subsistance et le terme : cela s’écrit en le ventre de sa mère. »</p>
<p>[Réf imprimée : <em>Ṣaḥīḥ</em> d’al-Bukhārī, Livre des menstrues, chapitre : « une [créature] formée et une non formée » ; vérifié : le texte correspond au hadith d’Anas = Bukhārī 3333 (Livre des récits des Prophètes), avec variantes de récit (« de la matrice » / « chargea » ; « parfaire sa création » ; « la subsistance et le terme ») ; le chapitre imprimé est celui du hadith parallèle d’Ibn Masʿūd (3208) — divergence de localisation notée.] Le sens du hadith : la subsistance, le terme, l’œuvre, l’infortune et la félicité sont au nombre de ce dont l’Écriture a précédé. Le Très-Haut dit :</p>
<p>« Et vous ne voulez, que si veut Dieu, le Seigneur des mondes. » (al-Takwīr, 29)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — déjà restituée en la leçon 9.]</p>
<h3>Deuxièmement : la volonté de Dieu, Puissant et Magnifié, embrasse tout ce qui est en l’univers</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Transcendant qu’Il soit qu’il soit, en Son royaume, ce qu’Il ne veut pas ; qu’il soit, pour quiconque, une dispense à l’égard de Lui ; ou qu’il soit créateur de quelque chose autre que Lui. » Le Qāḍī ʿAbd al-Wahhāb dit, en son commentaire de la <em>Risāla</em> : « Ce que l’auteur a mentionné est l’école des imams de la Sunna et des prédécesseurs de la communauté : Dieu, Puissant et Magnifié, veut tout ce qui advient en Son empire. »</p>
<p>Le sens de la parole de l’auteur : « transcendant » (<em>taʿālā</em>) est : Sa transcendance et Sa sainteté au point qu’il soit, en Son royaume, ce qu’Il ne veut pas — car s’il entrait en l’existence ce qu’Il ne veut pas, il s’ensuivrait nécessairement l’impuissance, la faiblesse et l’imposition. Comment donc, alors qu’Il a dit, glorifié soit-Il :</p>
<p>« Puis ils seront ramenés à Dieu, leur vrai Maître — quoi ! n’est-ce pas à Lui le jugement ? et Il est le plus prompt des comptables. » (al-Anʿām, 62)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<p>Dieu Très-Haut veut l’ensemble de ce qui advient en Son empire : cependant, les obéissances [adviennent] par Sa volonté, Son amour, Son agrément et Son commandement ; et les désobéissances par Sa volonté, sans Son amour, ni Son agrément, ni Son commandement. L’agrément et l’amour sont synonymes, comme la volonté et la <em>mašīʾa</em> sont synonymes.</p>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « ou qu’il soit, pour quiconque, une dispense à l’égard de Lui ». Au nombre de ce qu’il faut croire : Dieu Très-Haut est riche à l’égard de tout ce qui n’est pas Lui, et tout ce qui n’est pas Lui est indigent envers Lui. Le Très-Haut dit :</p>
<p>« Ô hommes : c’est vous, les indigents envers Dieu ; et Dieu, Lui, est le Riche, le Digne de louange. » (al-Fāṭir, 15)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.] Toute créature est indigente envers son Créateur, au commencement et à la durée : car Il est, l’Elevé, riche à l’égard des mondes. La richesse absolue, c’est Sa subsistance par Lui-même — Son autosuffisance, l’Elevé, à l’égard du substrat, du particularisant, du fils, du père, du secoureur et du reste.</p>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « ou qu’il soit créateur de quelque chose autre que Lui » — ceci est coordonné à ce qui précède : c’est-à-dire qu’il n’advient en l’être que ce que Dieu a voulu, car Il fait ce qu’Il veut ; qu’il n’y a pour quiconque de dispense à l’égard de Lui, car l’affaire de ce monde et de la dernière est en Sa main ; et qu’il n’est de créateur de quelque chose autre que Lui — bien plutôt, Il est le Créateur des essences, des attributs et des actes. Le Très-Haut dit :</p>
<p>« Cela est Dieu, votre Seigneur : il n’est de dieu que Lui, Créateur de toute chose — adorez-Le ! et Il est, sur toute chose, dépositaire. » (al-Anʿām, 102)</p>
<p>Et le Très-Haut dit :</p>
<p>« Ô hommes ! Rappelez-vous le bienfait de Dieu sur vous : y a-t-il un créateur autre que Dieu, qui vous nourrisse du ciel et de la terre ? Il n’est de dieu que Lui — comment vous détournez-vous donc ? » (al-Fāṭir, 3)</p>
<p>Et le Très-Haut dit :</p>
<p>« Quoi ! Celui qui crée est-il comme celui qui ne crée point ? Ne vous remémorez-vous donc pas ? » (al-Naḥl, 17)</p>
<p>[Trois citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la référence imprimée de la première porte « 103 », la visée est le verset 102 — réf d’adjacence notée ; les deux autres CONFORMES.]</p>
<h2>Les fruits de la leçon</h2>
<ul>
<li>Purifier l’âme du pouvoir et de la force, et l’éduquer à la soumission à Dieu, qui fait ce qu’Il veut : ce que Dieu veut est, et ce qu’Il ne veut point n’est pas.</li>
<li>Éduquer l’âme en la croyance ferme que l’affaire de la subsistance et du terme est réglée d’avance : l’homme n’obtient de la subsistance que ce qui lui en fut écrit.</li>
<li>Libérer l’homme de la crainte de l’avenir, que nul ne connaît sinon Dieu, glorifié soit-Il.</li>
<li>Éduquer le croyant à suivre les causes de la félicité, et à ne point s’enorgueillir de l’œuvre — car les œuvres [se jugent] à leurs scellés.</li>
</ul>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>J’expose le sens de la parole de l’auteur : « Et chacun est facilité, par Sa facilitation, vers ce qui, de Sa science et de Sa prédestination, a précédé » — avec appui.</li>
<li>L’homme est-il en pouvoir de se rendre heureux ou malheureux ? Avec justification et appui.</li>
<li>Je clarifie le sens de la volonté et de son embrassement de toute chose, avec appui de la transmission et de la raison.</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Al-Laqqānī — que Dieu lui fasse miséricorde — dit en la <em>Jawharat al-tawḥīd</em> :</p>
<table>
<tbody>
<tr><td>Créateur de Son serviteur et de son œuvre —</td><td>qui donne la réussite à celui qu’Il veut faire parvenir.</td></tr>
<tr><td>qui accomplit Sa promesse envers qui Il veut —</td><td>et abandonne celui qu’Il veut laisser en arrière.</td></tr>
<tr><td>Le gain de l’heureux est auprès de Lui depuis la pré-éternité —</td><td>de même le malheureux : il ne change point ensuite.</td></tr>
<tr><td>Et il n’est point cause — sache-le —</td><td>et, selon nous, le serviteur a une acquisition (<em>kasb</em>) dont il est redevable.</td></tr>
<tr><td>Il n’est ni contraint, ni [autonome] en son choix —</td><td>et certes, point il n’agit par [pouvoir de] choix.</td></tr>
</tbody>
</table>
<p>[<em>Jawharat al-tawḥīd</em>, avec le commentaire <em>Hidāyat al-murīd</em> de l’auteur : p. 162 — réf imprimée telle quelle. Les cinq vers sont imprimés en tableau à deux colonnes d’hémistiches ; l’ordre des colonnes de l’imprimé permute les hémistiches des vers 2 et 4 — l’ordre canonique de la Jawhara (suivi par les vers 1, 3 et 5) est restitué, noté ; le dernier vers, condensé de la doctrine de l’acquisition (<em>kasb</em>), est rendu au plus près de la lettre.]</p>
<h2>La préparation préalable (<em>iʿdād</em>)</h2>
<ul>
<li>Je lis le <em>matn</em> de la leçon suivante et réponds à ce qui suit :
<ul>
<li>Quel est le sens du Seigneur (<em>rabb</em>) des serviteurs ?</li>
<li>Qui est Celui qui détermine le terme ?</li>
</ul>
</li>
<li>Je recherche l’interprétation de la parole de Dieu Très-Haut : « Dis : je ne dispose, pour moi-même, ni d’un mal ni d’un bien, contre ce que veut Dieu. Pour toute communauté un terme : lorsque leur terme vient, ils ne sauraient le retarder d’une heure ni l’avancer. » (Yūnus, 49) [référence imprimée CONFORME ; citation restituée d’après le corpus canonique.]</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16723":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16723 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16723 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
