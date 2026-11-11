#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16718 (tawhid-1es, leçon 7 — Sa science,
glorifié soit-Il, embrasse toute chose).

Vérifications et restitutions (cache quran = Ḥafṣ) :
- Matn : « خلق الإنسان ويعلم ما توسوس به نفسه... له الأسماء الحسنى والصفات
  العلى » — le passage de la Risāla (reprend Qāf 16 et Anʿām 59-60), rendu
  fidèlement.
- DÉCOUVERTE — RÈGLE Ṭā-Hā −1 : les réfs imprimées Ṭā-Hā 4 (→ Ḥafṣ 5,
  « الرحمن على العرش استوى ») et Ṭā-Hā 7 (→ Ḥafṣ 8, « له الأسماء الحسنى »)
  suivent un décalage −1 cohérent (les deux cibles doctrinales sont
  univoques : istiwāʾ et asmāʾ ḥusnā) — documenté.
- CITATIONS VIDES (perte OCR) RESTAURÉES du cache, cibles doctrinales :
  * [الروم: 19] → Rūm 20 « ومن آياته أن خلقكم من تراب » — adjacency notée ;
  * [التغابن: 3] → CONFORME (صوركم فأحسن صوركم) ;
  * [ق: 16] → CONFORME (ونحن أقرب إليه من حبل الوريد — la source du matn) ;
  * [الأنعام: 4] → Anʿām 59 « وعنده مفاتيح الغيب » — écart 4→59 noté
    (chiffre des dizaines vraisemblablement perdu à l'OCR) ;
  * [غافر: 19] → CONFORME (يعلم خائنة الأعين) ;
  * [الواقعة: 88] → Wāqiʿa 85 « ونحن أقرب إليه منكم ولكن لا تبصرون » —
    la visée qurb ; écart noté ;
  * [الأنعام: 60] → CONFORME (يتوفاكم بالليل) ;
  * [طه: 4] → Ṭā-Hā 5 « الرحمن على العرش استوى » — règle −1 notée ;
  * [الأعراف: 53] → Aʿrāf 54 (istiwāʾ) — adjacency notée ;
  * [القصص: 13] → CONFORME (واستوى = بلوغ الأشد) ;
  * [الفتح: 29] → CONFORME — « فاستوى على سوقه » (istiwāʾ = se dresser) ;
  * [هود: 44] → CONFORME (واستوت على الجوديّ) ;
  * [آل عمران: 7] → CONFORME (muḥkam/mutashābih) ;
  * [الأعراف: 180] → CONFORME (ولله الأسماء الحسنى) ;
  * [طه: 7] → Ṭā-Hā 8 « له الأسماء الحسنى » — règle −1 notée.
- Doublon OCR : le paragraphe « وكما يعلم سبحانه ما على الأرض... مصداقا
  لقوله تعالى » imprimé 2× entrelacé (bloc ﴿...﴾ parasite) — rendu UNE
  fois, noté.
- Abū l-Ḥasan cité [كفاية الطالب الرباني 1/76] (istiwāʾ = hauteur de
  rang) — réf rendue telle qu'imprimée.
- Zarrūq/Ghazālī (istithmār) [شرح زروق 1/30] — citation INTÉGRALE
  (l'iḥāṭa ʿilman, la fuqāwiyya sans rapprochement, rafīʿ al-darajāt
  sur le Trône comme sur le seuil de terre) — rendue fidèlement.
- « أختُه » hmm : none. FIX GT-ismes : « les vertèbres » (الوريد !) →
  « la veine du cou (al-warīd) » ; « il a hérité » → rendu correct.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : Sa science — glorifié soit-Il — embrasse toute chose</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la septième leçon (7).</p>
<ul>
<li>Connaître les manifestations de l’embrassement de Sa science, l’Elevé.</li>
<li>Saisir les sens des choses qu’embrasse Sa science, Puissant et Élevé.</li>
<li>Éprouver, en mon comportement, la science de Dieu sur moi et Sa proximité de moi.</li>
</ul>
<h2>Préambule</h2>
<p>De ce qui précède, tu as acquis la science que le méditant intelligent doit tirer considération des créatures de Dieu, et non méditer Son essence ; et Dieu ordonna à Ses serviteurs la méditation de Ses créatures — parmi elles, l’homme — pour en inférer Sa grandeur en Son royaume et Sa puissance, Puissant et Élevé, sur toute chose qu’Il veut.</p>
<p>Quelles sont les plus éminentes de ces créatures dont la méditation est requise ? Quelle en est la fin ? Et quel est le rapport de cela avec la science de Dieu Très-Haut ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Il créa l’homme, et sait ce que son âme lui suggère en secret ; et Il est plus proche de lui que la veine du cou (<em>ḥabl al-warīd</em>). Point de feuille qui tombe qu’Il ne sache ; point de grain dans les ténèbres de la terre, point d’humide ni de sec, qui ne soit en un livre manifeste. Sur le Trône Il s’établit, et sur le royaume Il exerce Son empire ; à Lui les noms les plus beaux et les attributs les plus hauts. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>tūswisu bihi nafsuhu</em> (son âme lui suggère) : ce qui traverse sa pensée.</li>
<li><em>ḥabl al-warīd</em> (la veine du cou) : le <em>warīd</em> est la veine de l’intérieur du cou — c’est le <em>wadaj</em>.</li>
<li><em>istawā</em> (s’établit) : prit possession et s’éleva.</li>
<li><em>iḥtawā</em> (exerce Son empire) : embrassa.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> les manifestations de la science de Dieu Très-Haut et de Sa puissance.</li>
<li>J’extrais du <em>matn</em> ce dont Dieu garde l’œuvre à Lui seul.</li>
</ul>
<h2>L’analyse</h2>
<p>La leçon contient ce qui suit :</p>
<h3>Premièrement : la création de l’homme par Dieu, Sa science de ses états et Sa proximité de lui</h3>
<h4>1. La création de l’homme</h4>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Il créa l’homme. » Des indices de la puissance de Dieu Très-Haut : qu’Il créa l’homme de terre, et fit exister son espèce mâle et femelle, le décréta et le forma, embellissant sa forme. Le Très-Haut dit :</p>
<p>« Et parmi Ses signes : qu’Il vous créa de terre — puis, voilà que vous êtes hommes qui vous répandez. » (al-Rūm, 20)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte « 19 », la visée est le verset 20 — réf d’adjacence notée.] Et le Très-Haut dit :</p>
<p>« Il créa les cieux et la terre en la vérité, vous forma et embellit vos formes — et vers Lui est le devenir. » (al-Taghābun, 3)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.] Et cela est au nombre de ce qu’il faut croire.</p>
<h4>2. Sa science, Puissant et Élevé, des états de l’homme</h4>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « et sait ce que son âme lui suggère en secret ». Sa science, l’Elevé, embrasse tout ce que l’âme de l’homme lui suggère, et tout ce qui traverse sa pensée — une allusion à Sa parole :</p>
<p>« Certes, Nous créâmes l’homme, et Nous savons ce que son âme lui suggère : Nous sommes plus proche de lui que la veine du cou. » (Qāf, 16)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.] Dieu, Puissant et Élevé, sait ce qui sera avant qu’il soit, et sait le considérable des choses et le vil, leur manifeste et leur caché. Le Très-Haut dit :</p>
<p>« Auprès de Lui sont les clefs de l’invisible — nul autre que Lui ne les connaît. Et Il sait ce qui est en la terre ferme et en la mer ; et point de feuille qui tombe qu’Il ne sache ; point de grain dans les ténèbres de la terre, point d’humide ni de sec, qui ne soit en un livre manifeste. » (al-Anʿām, 59)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte « 4 », la visée est le verset 59 — chiffre des dizaines vraisemblablement perdu à l’OCR, noté.] Et le Très-Haut dit :</p>
<p>« Il sait la trahison des yeux et ce que les poitrines cachent. » (Ghāfir, 19)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<h4>3. Sa proximité, Puissant et Élevé, de l’homme</h4>
<p>L’auteur dit : « et Il est plus proche de lui que la veine du cou ». Le Créateur, Puissant et Élevé, est plus proche de l’homme que la veine du cou — laquelle est la plus proche des choses de l’homme, car le souffle y court et par elle. Et la proximité au sens d’extension de la science, de la volonté et de la puissance en tous les états — c’est elle qu’on vise ici : c’est proximité de science, non proximité de distance. Il est, l’Elevé, plus proche du serviteur que tout proche, selon Sa parole, Puissant et Élevé :</p>
<p>« Et Nous sommes plus proche de lui que vous — mais vous ne voyez point. » (al-Wāqiʿa, 85)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte « 88 », la visée de la proximité est le verset 85 — écart noté.]</p>
<h3>Deuxièmement : l’embrassement de Sa science et de Sa puissance, l’Elevé</h3>
<h4>1. Sa science de toute chose</h4>
<p>L’auteur — que Dieu lui fasse miséricorde — dit, en emprunt au noble Coran : « Point de feuille qui tombe qu’Il ne sache ; point de grain dans les ténèbres de la terre, point d’humide ni de sec, qui ne soit en un livre manifeste. » Au nombre de ce qu’il faut croire : Dieu, Puissant et Élevé, sait quelle feuille tombe de quelque arbre que ce soit, en toutes les contrées de la terre ; Il sait de même son existence et la distance de son lieu, la durée de sa permanence, son mouvement et son repos, son espace, sa qualité et le lieu de sa chute, et comment elle tombe ; et Sa science, Puissant et Élevé, s’y rapporte avant son existence, en l’état de son être et après son existence.</p>
<p>Et comme Il sait, Puissant et Élevé, ce qui est sur la terre, Il sait ce qui est dans ses ténèbres — les ténèbres de la terre étant ses strates ; l’humide (<em>al-raṭb</em>) : ce qui pousse ; et le sec (<em>al-yābis</em>) : ce qui ne pousse pas. Il fut dit : l’humide est le cœur du croyant, pour son impression par le bien ; et le sec, le cœur de l’infidèle, pour sa dureté — jusqu’à d’autres manifestations, au nombre de celles-ci, de la science de Dieu embrassant toute chose, selon Sa parole :</p>
<p>« Et c’est Lui qui vous fait mourir de nuit, et sait ce que vous acquérez de jour... » (al-Anʿām, 60 — extrait)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME. Le paragraphe est imprimé deux fois entrelacé — duplication OCR rendue une fois.]</p>
<h4>2. Son établissement, l’Elevé, sur le Trône et Son empire sur le royaume</h4>
<p>L’auteur — que Dieu lui faisse miséricorde — dit : « Sur le Trône Il s’établit, et sur le royaume Il exerce Son empire. » Au nombre de ce qu’il faut croire : qu’Il est, Puissant et Élevé, établi sur le Trône ; le Très-Haut dit :</p>
<p>« le Miséricordieux sur le Trône s’établit. » (Ṭā-Hā, 5)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte « 4 », la visée est le verset 5 — règle Ṭā-Hā −1 de la leçon, notée.] Et le Très-Haut dit :</p>
<p>« Certes, votre Seigneur est Dieu, qui créa les cieux et la terre en six jours, puis s’établit sur le Trône... » (al-Aʿrāf, 54 — extrait)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte « 53 », la visée est le verset 54 — réf d’adjacence notée.] L’établissement (<em>istiwāʾ</em>) a, en la parole des Arabes, des sens : l’empire et la conquête ; l’achèvement de la jeunesse, comme Sa parole :</p>
<p>« Et quand il eut atteint sa pleine force et mûri (<em>istawā</em>)... » (al-Qaṣaṣ, 13 — extrait)</p>
<p>la station debout, comme Sa parole :</p>
<p>« ...comme une pousse qui sorta ses jets, puis les renforça, s’épaissit et se dressa droite sur sa tige (<em>fa-stawā ʿalā sūqihi</em>)... » (al-Fatḥ, 29 — extrait)</p>
<p>et la stabilité et l’installation, comme Sa parole :</p>
<p>« ...et il fut dit : terre, absorbe ton eau ; ciel, cesse ! Et l’eau reflua, l’affaire fut décidée, et [l’arche] s’installa (<em>istawat</em>) sur al-Jūdiyy. » (Hūd, 44 — extrait)</p>
<p>[Quatre citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées CONFORMES.] L’établissement, envers Lui, l’Elevé, est du ressort de l’équivoque (<em>mutashābih</em>) — comme la Face, l’Œil et la Main. Et sur l’équivoque, deux écoles célèbres :</p>
<ul>
<li>La première : l’obligation de remettre son sens à Dieu Très-Haut, après la certitude de la transcendance au sujet de l’apparent impossible — le Très-Haut dit : « C’est Lui qui fit descendre sur toi le Livre : de Ses signes sont des versets équivoques (<em>mutashābihāt</em>)... » (Āl ʿImrān, 7 — extrait) [référence imprimée CONFORME ; citation restaurée].</li>
<li>La seconde : la permission d’interpréter l’équivoque, de la tirer de son apparent et de la ramener à ce qu’exigent les indices des intelligences — ce qui est valide par indication du contexte ou par la fréquence de l’usage des Arabes : l’établissement est alors l’empire et la conquête. Abū l-Ḥasan dit : “ Il fut dit : l’établissement au sens de la hauteur — hauteur de rang et de dignité, non de lieu. ” [<em>Kifāyat al-ṭālib al-rabbānī</em> : 1/76 — réf rendue telle qu’imprimée.]</li>
</ul>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « à Lui les noms les plus beaux et les attributs les plus hauts. » Au nombre de ce qu’il faut croire : qu’à Dieu Très-Haut appartiennent les noms les plus beaux. Les noms — pluriel — furent décrits par <em>al-ḥusnā</em> — singulier — parce qu’ils sont un pluriel au sens ; et le valide est que Ses noms, l’Elevé, ne sont pas limités aux quatre-vingt-dix-neuf rapportés au hadith. Le plus juste est que Ses noms, l’Elevé, sont d’attestation : on ne Le nomme que de ce dont Il Se nomma Lui-même, ou de ce dont Le nomma Son prophète — paix et bénédiction sur lui. Dieu dit :</p>
<p>« À Dieu les noms les plus beaux : invoquez-Le par eux ; et délaissez ceux qui dévient en Ses noms... » (al-Aʿrāf, 180)</p>
<p>Et, Puissant et Élevé :</p>
<p>« Dieu — il n’est de dieu que Lui ; à Lui les noms les plus beaux. » (Ṭā-Hā, 8)</p>
<p>[Deux citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la première référence imprimée CONFORME ; la seconde porte « 7 », la visée est le verset 8 — règle Ṭā-Hā −1, notée.]</p>
<h2>Les fruits de la leçon</h2>
<ul>
<li>Éprouver que la science de Dieu Très-Haut embrasse le caché et le manifeste : cela élève en l’homme le sens de la vigilance et de l’arrêt aux limites de Dieu Très-Haut.</li>
<li>Faire présent Sa puissance, l’Elevé : cela greffe en l’âme du croyant l’arbre du remise-à-Dieu (<em>tawakkul</em>), qui porte le fruit de la soumission au Créateur et de la remise entière au Puissant sur toute chose — et par là le croyant réalise sa servitude envers Dieu Très-Haut.</li>
</ul>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>J’expose les manifestations de l’embrassement de la science de Dieu Très-Haut.</li>
<li>J’analyse la parole de l’auteur : « Sur le Trône Il s’établit, et sur le royaume Il exerce Son empire ».</li>
<li>Je mets en relief l’effet, sur le comportement et sa correction, de l’éprouver que la science de Dieu embrasse l’homme.</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Le shaykh Aḥmad Zarrūq dit : « L’imam al-Ghazālī dit : — En somme, Dieu Très-Haut embrasse toute chose en science, et est au-dessus de toute chose en science : une surélévation qui ne L’accroît point de proximité du Trône et du ciel — mais Il est l’Éleveur des degrés au-dessus du Trône, comme Il est l’Éleveur des degrés au-dessus du seuil de terre ; et Il est, de surcroît, proche de tout existant, plus proche du serviteur que la veine du cou, témoin sur toute chose : Sa proximité, en effet, ne ressemble pas à la proximité des corps, comme Son essence ne ressemble pas à l’essence des corps. » [Le commentaire de Zarrūq sur la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī : 1/30 — citation intégrale et conforme ; réf rendue telle qu’imprimée.]</p>
<h3>Je contemple le texte et réalise ce qui suit :</h3>
<ul>
<li>J’explique ce texte, en le comparant à ce que j’ai acquis en la leçon.</li>
<li>J’appuie d’arguments coraniques les attributs de Dieu Très-Haut venus au texte.</li>
</ul>
<h2>La préparation préalable (<em>iʿdād</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et recherche ce qui distingue les attributs de Dieu Très-Haut.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16718":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16718 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16718 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
