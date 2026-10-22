#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16736 (tawhid-1es, leçon imprimée 15 — la sortie
des croyants désobéissants du Feu par l'intercession du Prophète ﷺ).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire) ;
traduction savante avec restaurations du corpus canonique (cache quran = Ḥafṣ).

Vérifications et restaurations (cache quran = Ḥafṣ) :
- 5 citations vides [سورة ... الآية N] (perte OCR systématique CMS) restaurées :
  Zalzala 7 (réf imprimée 8 — le verset du mal adjacent ; cible univoque = le
  verset du bien cité par le matn ; le matn ouvre par le wāw « ومن يعمل » quand
  le muṣḥaf Ḥafṣ lit فمن — forme de citation propre au matn, notée) ;
  Naḥl 97 (CONFORME — la vie heureuse + le plus beau salaire, miroir exact du
  propos « il verra la rétribution de son bien en ce bas-monde et dans
  l'au-delà ») ; Ṭā-Hā 112 (réf imprimée 109 — écart +3 de la numérotation de
  cette page CMS, MÊME règle que Ṭā-Hā 107→110 documentée en la leçon six ;
  cible univoque : l'œuvre salutaire du croyant sans crainte d'injustice ni de
  diminution ; le Ṭā-Hā 109 imprimé — la permission de l'intercession —
  appartient à la même péricope, noté) ; Āl ʿImrān 115 (CONFORME — « quelque
  bien qu'ils fassent, il ne leur en sera point dénié ») ; Muḥammad 19
  (CONFORME — l'implication du pardon pour les croyants et les croyantes ancre
  le privilège intercessoire du Prophète ﷺ).
- Hadith d'Abū Hurayra (le Feu ne dévore pas la trace de la prosternation ;
  l'eau de la vie versée sur les calcinés ; la graine dans le limon du
  torrent) : VÉRIFIÉ CONFORME sur sunnah.com = Ṣaḥīḥ Muslim 182a, Kitāb
  al-Īmān, bāb « معرفة طريق الرؤية » EXACT (bāb imprimé CONFORME) ; la
  citation est l'extrait final du long hadith de la vision ; vocalisation
  al-ḥabba/al-ḥibba divergente notée.
- Jawharat al-tawḥīd : 3 vers sur l'intercession — tableau à deux colonnes
  d'hémistiches (colonne médiane vide = artefact d'extraction, non rendue) ;
  orthographe maghrébine « مومن » conservée et notée ; tatwīl restitués.
- Doublons/artefacts OCR : intro « قال الإمام اللقاني في جوهرة التوحيد ما نصه »
  imprimée 2× → rendue une fois ; annonce de l'iʿdād qablī répétée en tête du
  premier item (imbrication d'extraction) → détangle, rendue une fois ;
  lexique ذرة/شفاعة soudés en un article → séparés ; dl/dt/dd vides + <p>
  vides + echo du titre en queue + divs vides — artefacts non rendus ;
  المومنين = المؤمنين orthographe qayrawānienne (titre/intro) — notée.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la sortie des croyants désobéissants du Feu par l’intercession du Prophète ﷺ</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la quinzième leçon (15).</p>
<ul>
<li>Connaître la station louée (<em>al-maqām al-maḥmūd</em>) du Prophète ﷺ auprès de son Seigneur.</li>
<li>Mettre devant les yeux le devenir des désobéissants (<em>ʿuṣṣāt</em>) dans l’au-delà.</li>
<li>M’acquitter des ordres de Dieu et écarter Ses interdits, pour obtenir Son agrément dans ce bas-monde et dans l’au-delà.</li>
</ul>
<h2>Préambule</h2>
<p>Quand Ibn Abī Zayd — que Dieu lui fasse miséricorde — eut mentionné, dans le <em>matn</em> de la leçon précédente, que quiconque meurt sur ses péchés sans s’en repentir remonte à la volonté de Dieu Très-Haut — s’Il veut, Il le châtie ; s’Il veut, Il lui pardonne —, il fit suite à cela de parler du devenir des désobéissants parmi les croyants, et de l’intercession du Messager de Dieu ﷺ en leur faveur.</p>
<p>Quel est donc le devenir des désobéissants parmi les croyants ? Quelle est la réalité de l’intercession du Prophète ﷺ ? Et que signifie l’intercession du Prophète ﷺ pour les désobéissants de sa communauté ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et quiconque Il châtie de Son Feu, Il le fait sortir de lui par sa foi et le fait entrer, par elle, en Son jardin ; et quiconque fait un bien, fût-il du poids d’un atome, le verra ; et sortira du Feu, par l’intercession du Prophète ﷺ, quiconque il a intercédé pour, parmi les auteurs des péchés majeurs de sa communauté. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>ʿāqabahu</em> (châtie) : le saisit pour son péché et en prit rigueur ; et le châtiment (<em>ʿiqāb</em>) est la rétribution par le mal.</li>
<li><em>mithqāl</em> : ce avec quoi l’on pèse — un nom d’instrument ; et le <em>mithqāl</em> d’une chose est son poids.</li>
<li><em>dharra</em> : partie parvenue au terme extrême de la petitesse.</li>
<li><em>shafāʿa</em> (intercession) : demander le bien pour autrui, et solliciter pour lui aide et assistance. [Deux articles du lexique imprimés soudés en un seul — séparés.]</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> le devenir des désobéissants parmi les croyants.</li>
<li>Je dégage du <em>matn</em> ceux qu’embrasse l’intercession du Prophète ﷺ.</li>
</ul>
<h2>L’analyse (<em>taḥlīl</em>)</h2>
<p>La leçon comprend les axes suivants :</p>
<h3>Premièrement : le devenir des désobéissants parmi les croyants</h3>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et quiconque Il châtie de Son Feu, Il le fait sortir de lui par sa foi et le fait entrer, par elle, en Son jardin. » Il est de la croyance obligatoire que certains désobéissants parmi les monothéistes seront atteints par le châtiment de Dieu Très-Haut au Jour de la Résurrection — châtiment gradué selon la graduation de leurs désobéissances ; et ceux-là, Dieu les fera sortir du Feu en raison de leur foi, et les fera entrer au Paradis. La parole de l’auteur : « le fait entrer, par elle, en Son jardin » : c’est l’espèce de Son jardin — car les jardins sont sept : le jardin du <em>Firdaws</em>, le jardin du <em>Maʾwā</em>, le jardin de l’éternité (<em>al-Khuld</em>), le jardin des délices (<em>al-Naʿīm</em>), le jardin de <em>ʿAdan</em>, la Demeure de la Paix (<em>Dār al-Salām</em>) et la Demeure de l’éternité (<em>Dār al-Khuld</em>).</p>
<p>Il est venu dans le hadith ce qui requiert que le Feu ne dévore pas les lieux de prosternation du croyant ; d’après Abū Hurayra — que Dieu l’agrée —, le Prophète ﷺ dit : « … Quand Dieu achève le jugement entre les serviteurs et veut faire sortir, par Sa miséricorde, qui Il veut des gens du Feu, Il ordonne aux anges de faire sortir du Feu quiconque n’associait rien à Dieu, parmi ceux dont Dieu Très-Haut veut faire miséricorde, parmi ceux qui disent : il n’y a de dieu que Dieu. Ils les reconnaissent alors dans le Feu : ils les reconnaissent à la trace de la prosternation — le Feu dévore du fils d’Adam toute chose hormis la trace de la prosternation : Dieu a interdit au Feu de dévorer la trace de la prosternation. Ils sortent alors du Feu, calcinés ; on répand sur eux l’eau de la vie, et ils en repoussent comme repousse la graine dans le limon du torrent. » [Ṣaḥīḥ Muslim, Kitāb al-Īmān, bāb de la connaissance de la voie de la vision (<em>maʿrifa ṭarīq al-ruʾya</em>) — hadith d’Abū Hurayra (n° 182) : texte VÉRIFIÉ CONFORME sur sunnah.com, bāb imprimé EXACT ; la citation est l’extrait final du long hadith de la vision ; la vocalisation de « la graine » (<em>al-ḥabba</em>/<em>al-ḥibba</em>) diverge entre l’imprimé et la transmission — notée.]</p>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et quiconque fait un bien, fût-il du poids d’un atome, le verra ». Par là l’auteur a visé la parole de Dieu Très-Haut :</p>
<p>« Quiconque fait un bien, fût-il du poids d’un atome, le verra. » (al-Zalzala, 7)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Référence imprimée : [Zalzala 8] — le verset du mal adjacent ; la cible univoque est le verset du bien (7), celui-là même que cite le <em>matn</em> ; le <em>matn</em> l’ouvre par le <em>wāw</em> (<em>wa-man yaʿmal</em>) quand le muṣḥaf Ḥafṣ lit <em>fa-man</em> — forme de citation propre au <em>matn</em>, notée.]</p>
<p>— c’est-à-dire : quiconque œuvre un bien du poids d’un atome en sera rétribué. Et le bien (<em>khayr</em>) est ce dont l’auteur est louable selon la Loi ; la foi relève du bien : le croyant verra donc la rétribution de son bien dans ce bas-monde et dans l’au-delà. Sa preuve est la parole de Dieu Très-Haut :</p>
<p>« Quiconque, homme ou femme, fait œuvre salutaire tout en étant croyant : Nous le ferons certes vivre une vie heureuse, et Nous les rétribuerons certes du plus beau salaire de ce qu’ils œuvraient. » (al-Naḥl, 97)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<p>et Sa parole :</p>
<p>« Et quiconque, étant croyant, œuvre des œuvres salutaires : il ne craindra ni injustice ni diminution. » (Ṭā-Hā, 112)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Référence imprimée : [Ṭā-Hā 109] — écart +3 de la numérotation de cette page CMS, la même règle que Ṭā-Hā 107→110 documentée en la leçon six ; cible univoque : l’œuvre salutaire du croyant, sans crainte d’injustice ni de diminution — miroir exact du propos ; le Ṭā-Hā 109 de l’impression (la permission de l’intercession) appartient à la même péricope, noté.]</p>
<p>et Sa parole :</p>
<p>« Et quelque bien qu’ils fassent, il ne leur en sera point dénié [le salaire] ; et Dieu, des gens de piété, est parfaitement savant. » (Āl ʿImrān, 115)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<h3>Deuxièmement : la foi en l’intercession du Prophète ﷺ</h3>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et sortira du Feu, par l’intercession du Prophète ﷺ, quiconque il a intercédé pour, parmi les auteurs des péchés majeurs de sa communauté. » Il est de la croyance obligatoire d’affirmer l’intercession pour notre Prophète Muḥammad ﷺ. Les anciens (<em>salaf</em>) et les postérieurs (<em>khalaf</em>) parmi les gens de la Sunna et de la vérité sont unanimement d’accord sur la fermeté de l’intercession pour notre Prophète Muḥammad ﷺ, comme, en termes absolus, pour le reste des envoyés, les anges et les croyants ; et la plus vénérable et la plus grande d’entre elles est l’intercession de notre Prophète Muḥammad ﷺ pour l’ensemble des gens du Stationnement. Il n’y a pas de divergence entre les gens de la Sunna et de la communauté (<em>jamāʿa</em>) sur le fait que l’intercession est fermement établie pour notre maître Muḥammad ﷺ en faveur des désobéissants de sa communauté, auteurs des péchés majeurs comme des péchés mineurs : ils sortent du Feu par son intercession ﷺ. Dieu Très-Haut dit :</p>
<p>« Sache donc qu’il n’est de dieu que Dieu, et implore le pardon pour ton péché ainsi que pour les croyants et les croyantes ; Dieu connaît parfaitement vos allées et venues et votre demeure. » (Muḥammad, 19)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — l’implication du pardon pour les croyants et les croyantes ancre le privilège intercessoire du Prophète ﷺ en faveur de sa communauté.]</p>
<p>Et ses intercessions ﷺ sont des intercessions dont il faut croire en la totalité ; les voici :</p>
<ul>
<li>La première : son intercession pour les gens du Stationnement lors du compte (<em>ḥisāb</em>) — cette intercession suprême (<em>al-shafāʿa al-ʿuẓmā</em>) est propre à lui seul ﷺ.</li>
<li>La deuxième : son intercession en faveur d’un peuple qui entrera au Paradis sans compte — elle est propre à lui ﷺ.</li>
<li>La troisième : son intercession en faveur d’un peuple qui a mérité le Feu : ceux-là n’y entreront pas, par son intercession ﷺ.</li>
<li>La quatrième : son intercession pour faire sortir du Feu les croyants qui y sont entrés — les prophètes, les anges et les croyants y participent avec lui.</li>
<li>La cinquième : son intercession pour l’allègement du châtiment de certains mécréants — elle est propre à lui, comme son intercession en faveur de son oncle paternel Abū Ṭālib, pour alléger son châtiment.</li>
</ul>
<h2>Les fruits de la leçon</h2>
<p>La présence intérieure de l’effet de la foi dans ce bas-monde et dans l’au-delà : cela pousse le croyant à fortifier sa foi en son Seigneur — son âme s’épure ainsi, et son cœur et ses membres se redressent : il vit alors une vie droite et bonne, dans laquelle il réalise la finalité de son existence, à savoir sa servitude envers son Seigneur et son utilité pour Ses serviteurs. De même se manifeste en la leçon la station de notre maître Muḥammad ﷺ auprès de son Seigneur : il est le détenteur de l’étendard de la louange (<em>lawāʾ al-ḥamd</em>) et de la grande intercession au Jour de la Résurrection. Heureux donc celui qui œuvre selon sa Législation clémente, se pare de ses caractères et se rapproche de Dieu par son amour et son suivi, pour obtenir son intercession ﷺ.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>J’explicite le devenir des désobéissants.</li>
<li>Par quoi les désobéissants sortent-ils du Feu ? Avec appui.</li>
<li>Je mentionne les sortes d’intercessions du Prophète ﷺ.</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Al-Laqqānī — que Dieu lui fasse miséricorde — dit en la <em>Jawharat al-tawḥīd</em> ce qui suit : [Phrase imprimée deux fois — rendue une fois.]</p>
<table>
<tbody>
<tr><td>Obligatoire est l’intercession de celui qui la reçoit —</td><td>Muḥammad, le tout premier : elle n’est point refusée.</td></tr>
<tr><td>Et d’autres que lui, parmi l’élite des agréés,</td><td>intercèdent — ainsi qu’il est venu dans les transmissions.</td></tr>
<tr><td>Puisque le pardon de tout autre que la mécréance est de possibilité légale,</td><td>point nous ne déclarons mécréant un croyant pour un péché.</td></tr>
</tbody>
</table>
<p>[<em>Jawharat al-tawḥīd</em> d’al-Laqqānī : trois vers sur l’intercession et le statut du croyant désobéissant, imprimés en tableau à deux colonnes d’hémistiches — la colonne médiane vide est un artefact d’extraction, non rendue ; l’orthographe « <em>mūminan</em> » (avec <em>wāw</em>) du troisième vers suit l’écriture maghrébine de l’auteur — conservée telle quelle ; les allongements graphiques d’extraction (<em>شـفاعـة</em>, <em>مـقـدما</em>…) restitués.]</p>
<h2>La préparation préalable (<em>iʿdād qablī</em>)</h2>
<p>Je mémorise le <em>matn</em> de la leçon suivante et recherche : [L’annonce imprimée est répétée en tête du premier item — imbrication d’extraction détangle : rendue une fois.]</p>
<ul>
<li>Qu’est-ce que le Paradis ? Pour qui Dieu Très-Haut l’a-t-Il préparé ?</li>
<li>Je recherche des versets coraniques décrivant le Paradis, ses habitants et ses délices.</li>
<li>Quel est le plus grand honneur dont Dieu honore Ses serviteurs dans l’au-delà ?</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16736":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16736 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    # contrôle apostrophes typographiques : aucune droite dans le corps
    n_droites = HTML_FR.count("'")
    print(f"OK — leçon 16736 main: FR {len(HTML_FR)} car ; apostrophes droites: {n_droites} (attendu 0)")


if __name__ == "__main__":
    main()
