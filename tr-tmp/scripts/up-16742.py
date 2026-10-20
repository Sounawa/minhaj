#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16742 (tawhid-1es, leçon imprimée 18 — la
foi en la Balance et la remise des feuillets).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire) ;
traduction savante avec restaurations du corpus canonique (cache quran = Ḥafṣ).

Vérifications et restaurations (cache quran = Ḥafṣ) :
- 7 emplacements de citation vides (perte OCR systématique CMS) :
  Anbiyāʾ 47 CONFORME (ونضع الموازين القسط — LE verset de la Balance, miroir
  du propos ; le bāb Bukhārī imprimé le cite littéralement) ; citation de MOT
  « al-mawāzīn » (le pluriel) — cible univoque, la glose portant sur
  l'interprétation du PLURIEL (les pesées / pluriel de majesté) ; Takwīr 10
  CONFORME (وإذا الصحف نشرت — le verset des feuillets) ; Kahf 48→49 écart +1
  (cible univoque : ووضع الكتاب — la pose du Livre qui ne néglie ni petite ni
  grande action ; le v48 adjacent = la présentation, déjà restitué en la
  leçon précédente, noté) ; Inshiqaq « الآيات 12-11-10-9-8-7 » (série
  DESCENDANTE de six versets) → restituée 84:7-12 CONFORME — le matn condense
  exactement ces six versets ; 3 citations SANS référence dans la citation
  d'al-Lawh — cibles univoques par la doctrine des feuillets (trio canonique
  de la remise) : Isrāʾ 13-14 (le livre trouvé déployé), Ḥāqqa 19 (la main
  droite), Ḥāqqa 25 (la main gauche).
- Hadiths VÉRIFIÉS sunnah.com (curl + UA navigateur) : Bukhārī « كلمتان
  خفيفتان على اللسان » — bāb imprimé « ونضع الموازين القسط » EXACT (ch. 58
  du Kitāb al-Tawḥīd = hadith 7563 d'Abū Hurayra) ; l'ordre des membres de
  l'imprimé (« légères… lourdes… aimées ») suit la leçon de Bukhārī 6682 /
  Muslim 2694, le 7563 ouvrant par « aimées » — variante d'ordre notée ;
  Muslim 223 (Abū Mālik al-Ashʿarī, Kitāb al-Ṭahāra bāb فضل الوضوء EXACT) —
  texte VÉRIFIÉ CONFORME mot à mot, y compris la variante « أو تملأ » ;
  Abū l-Dardāʾ « أثقل شيء في الميزان خلق حسن » rendu comme imprimé (al-Bayhaqī).
- OCR/artefacts : titre de section « المستفاد من لدرس » (avec ل parasite)
  rendu « Les fruits de la leçon » selon la série, noté ; deux-points
  parasites en tête d'items non rendus ; lexique يَصْلَون double glose soudée
  rendue ; dl/dt/dd vides + <p> vides + echo du titre en queue + divs vides
  — artefacts non rendus.
- Doctrines rendues au plus près : la balance sensible à deux plateaux et
  une langue (ijmāʾ ahl al-ḥaqq) ; l'unicité de la balance (pluriel de
  majesté) ; la corporéification des œuvres (tajassum) ; la parole d'Abū
  Bakr al-Ṣiddīq ; l'approbation d'al-Laqqānī (Sharḥ al-Jawhara) ; la
  science nécessaire (ḍarūriyya) à la remise du feuillet.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la foi en la Balance et la remise des feuillets</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la dix-huitième leçon (18).</p>
<ul>
<li>Connaître la manière de la pesée des œuvres des serviteurs.</li>
<li>Distinguer entre les balances et les feuillets.</li>
<li>Mettre devant les yeux que l’œuvre salutaire conduit à la prise du feuillet par la droite, au jour du compte.</li>
</ul>
<h2>Préambule</h2>
<p>Les balances furent dressées en ce bas-monde pour préserver les droits et garantir l’équité entre les gens ; et le Seigneur de la majesté — exalté soit-Il — a informé qu’Il placera les balances au Jour de la Résurrection pour l’équité entre les gens, ainsi qu’il est venu au sens apparent du Coran.</p>
<p>Qu’est-ce donc qui est pesé en la balance de l’au-delà ? Et quel rapport cela a-t-il avec les feuillets ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et les balances sont placées pour la pesée des œuvres des serviteurs : celui dont les balances seront lourdes — ceux-là sont les prospères. Et ils reçoivent leurs feuillets avec leurs œuvres : quiconque reçoit son livre en sa main droite sera certes pris à un compte aisé ; et quiconque reçoit son livre derrière son dos — ceux-là brûlent dans le Brasier. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>tuḍaʿu</em> (sont placées) : sont dressées, érigées, préparées.</li>
<li><em>mawāzīn</em> (balances) : pluriel de <em>mīzān</em> — l’instrument avec quoi l’on pèse une chose, pour connaître sa quantité.</li>
<li><em>yuʾtā</em> (est donné) : lui est remis, lui est livré.</li>
<li><em>ṣaḥāʾif</em> (feuillets) : pluriel de <em>ṣaḥīfa</em> — la feuille écrite, le papier, le registre.</li>
<li><em>yaṣlawna</em> (brûlent) : sont rôtis, consumés.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> la finalité de la pose des balances au Jour de la Résurrection.</li>
<li>Je dégage du <em>matn</em> le devenir de celui dont les balances seront lourdes, et de celui dont les balances seront légères.</li>
<li>J’extrais du <em>matn</em> la manière de la prise des feuillets par les serviteurs, au Jour de la Résurrection.</li>
</ul>
<h2>L’analyse (<em>taḥlīl</em>)</h2>
<p>La leçon comprend les axes suivants :</p>
<h3>Premièrement : la foi aux balances du Jour de la Résurrection</h3>
<h4>1. L’obligation de la foi aux balances</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et les balances sont placées pour la pesée des œuvres des serviteurs. » Il est de la croyance obligatoire que Dieu Très-Haut placera et dressera les balances pour la pesée des œuvres — c’est-à-dire des feuillets où sont les œuvres des serviteurs. Les gens de la vérité sont unanimement d’accord sur l’existence d’une balance sensible, qui a deux plateaux et une langue : y sont pesés les feuillets des œuvres des serviteurs, pour que paraisse le gagnant et le perdant. Dieu Très-Haut dit :</p>
<p>« Et Nous plaçons les balances de l’équité pour le Jour de la Résurrection : nulle âme ne sera lésée en rien ; et s’il y a le poids d’un grain de moutarde, Nous le ferons venir — et c’est Nous qui suffisons, comme comptables. » (al-Anbiyāʾ, 47)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — « Et Nous plaçons les balances de l’équité » : le verset de la Balance, miroir exact du propos ; le bāb de Bukhārī cité plus bas le reprend littéralement.]</p>
<p>Et la position juste est qu’elle est une balance unique ; et Sa parole — exalté soit-Il — <em>« al-mawāzīn »</em> (les balances) a été portée sur les choses pesées, ou sur ce qu’Il est venu avec la forme plurielle pour magnifier Son rang, glorifier Son affaire, avertir de l’acquisition des mauvaises œuvres et inciter à l’acquisition des obéissances. [Citation de mot imprimée vide — restituée : cible univoque, la glose portant sur l’interprétation du pluriel.]</p>
<p>La parole de l’auteur — « pour la pesée des œuvres des serviteurs » — : c’est-à-dire pour la pesée des feuillets des œuvres des serviteurs ; et il se peut que celles-ci prennent corps et soient pesées : les œuvres des obéissants se font alors en belle figure, et celles des malfaisants en figure laide. Cela est attesté par des hadiths nombreux, dont le hadith d’Abū Hurayra — que Dieu l’agrée —, d’après le Prophète ﷺ : « Deux paroles, légères sur la langue, lourdes dans la Balance, aimées du Tout-Miséricordieux : “ Gloire à Dieu et par Sa louange ; gloire à Dieu le Magnifique. ” » [Ṣaḥīḥ al-Bukhārī, bāb « Et Nous plaçons les balances de l’équité » — bāb imprimé EXACT (ch. 58 du Kitāb al-Tawḥīd, hadith 7563 d’Abū Hurayra) ; l’ordre des membres de la citation imprimée (« légères… lourdes… aimées ») suit la leçon de Bukhārī 6682 / Muslim 2694, le 7563 ouvrant par « aimées » — variante d’ordre notée.] ; et le hadith d’Abū Mālik al-Ashʿarī — que Dieu l’agrée —, qui dit : le Messager de Dieu ﷺ dit : « La purification est la moitié de la foi ; “ louange à Dieu ” emplit la Balance ; “ gloire à Dieu ” et “ louange à Dieu ” emplissent — ou : emplit — ce qu’il y a entre les cieux et la terre. » [Ṣaḥīḥ Muslim, Kitāb al-Ṭahāra, bāb du mérite de l’ablution — bāb imprimé EXACT (hadith 223) : texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com, y compris la variante « ou : emplit ».] ; et le hadith d’Abū l-Dardāʾ, élevé [au Prophète ﷺ] : « La chose la plus lourde dans la Balance : un beau caractère. » [Transmis par al-Bayhaqī — réf imprimée conservée.]</p>
<h4>2. La pesée des œuvres, signe de la prospérité ou de la perte</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « celui dont les balances seront lourdes — ceux-là sont les prospères » : celui dont les pesées seront lourdes et l’emporteront — ce sont les feuillets où sont les œuvres —, ceux-là sont les sauvés, les gagnants. Abū Bakr al-Ṣiddīq — que Dieu l’agrée — dit : ce n’est qu’en suivant, en ce bas-monde, le vrai, que les balances de celui dont les balances furent lourdes au Jour de la Résurrection devinrent lourdes ; et ce n’est qu’en suivant, en ce bas-monde, le faux, que les balances de celui dont les balances furent légères au Jour de la Résurrection devinrent légères.</p>
<p>La position juste est qu’elle est sur la forme de la balance de ce bas-monde — position qu’al-Laqqān a agréée en son commentaire de la <em>Jawhara</em> ; et il se peut de dire : c’est la foi qui est pesée — et, dès lors, tout croyant a la balance lourde, car rien ne pèse plus lourd que la foi.</p>
<h3>Deuxièmement : la manière de la remise des feuillets des œuvres aux serviteurs, et son effet</h3>
<h4>1. La remise des feuillets des œuvres aux serviteurs</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et ils reçoivent leurs feuillets avec leurs œuvres. » Il est de la croyance obligatoire, et de la conviction de sa survenance, que les nations — c’est-à-dire les responsables d’entre elles — reçoivent leurs feuillets : ce sont les livres où les anges ont écrit leurs œuvres en ce bas-monde.</p>
<p>La parole de l’auteur — « avec leurs œuvres » — : ils reçoivent leurs feuillets en accompagnement de leurs œuvres — le <em>bāʾ</em> est de la compagnie. Quand ils les reçoivent, Dieu crée pour eux une science nécessaire (<em>ḍarūriyya</em>), par laquelle ils comprennent ce qu’il y a en eux de ce qu’ils firent en ce bas-monde. La preuve de la prise des feuillets est la parole de Dieu Très-Haut :</p>
<p>« … et quand les feuillets seront déployés. » (al-Takwīr, 10)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — le verset des feuillets, miroir exact du propos.]</p>
<p>et Sa parole :</p>
<p>« Et le Livre sera posé : tu verras alors les criminels, effrayés de ce qu’il contient, dire : “ Malheur à nous ! Qu’a donc ce livre, à ne rien omettre, ni petite ni grande, sans l’avoir dénombrée ? ” Et ils trouveront présent ce qu’ils œuvraient… » (al-Kahf, 49)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Référence imprimée : [Kahf 48] — écart +1 : la cible univoque est la pose du Livre (v49) ; le v48 adjacent (la présentation « et ils sont présentés à ton Seigneur, en rangs ») fut restitué en la leçon précédente — noté.]</p>
<h4>2. La manière de la remise des feuillets, et son effet</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « quiconque reçoit son livre en sa main droite sera certes pris à un compte aisé ; et quiconque reçoit son livre derrière son dos — ceux-là brûlent dans le Brasier. » Il est de la croyance obligatoire que les gens reçoivent les feuillets de leurs œuvres : les uns prennent leur livre en leur main droite, les autres prennent leur livre en leur main gauche. La parole de l’auteur — « sera certes pris à un compte aisé » — : aisé, facile, où l’on n’est pas convoqué au détail, ni exposé à ce qui l’afflige. L’auteur y fait allusion à la parole de Dieu Très-Haut :</p>
<p>« Quant à celui qui reçoit son livre en sa main droite, il sera certes pris à un compte aisé, et s’en retournera vers les siens, joyeux. Et quant à celui qui reçoit son livre derrière son dos, il invoquera certes l’anéantissement, et brûlera dans le Brasier. » (al-Inshiqāq, 7-12)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Référence imprimée : « les versets 12-11-10-9-8-7 » — la série écrite en ordre descendant : restituée 7-12 CONFORME (Ḥafṣ) ; le <em>matn</em> condense exactement ces six versets.]</p>
<h2>Les fruits de la leçon</h2>
<p>[Titre de section de l’imprimé « <em>al-mustafād min (a)l-dars</em> » — rendu selon la série.] On tire de la leçon que la finalité du déploiement des feuillets, de la remise aux serviteurs des feuillets de leurs œuvres et de leur lecture est qu’au déploiement des feuillets le serviteur connaît l’accepté et le rejeté de ses bonnes actions, le pardonné et le retenu de ses mauvaises ; il y a là, pour lui, un avertissement de l’importance de la purification de l’âme par l’œuvre salutaire, en la vie de l’homme ici-bas et là-bas — et cela même est l’équité et la sagesse.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>Pourquoi les balances sont-elles placées ?</li>
<li>Qui sont ceux dont les balances s’alourdissent, et ceux dont les balances s’allègent ?</li>
<li>Comment les feuillets des œuvres sont-ils remis aux serviteurs ?</li>
<li>Et quel est l’effet de cela ?</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Le maître al-ʿArabī al-Lawh dit : « Que les serviteurs reçoivent les feuillets de leurs œuvres au Jour de la Résurrection relève de la croyance obligatoire et de la foi, pour sa venue par le Livre, la Sunna et l’unanimité — et le nier est mécréance. Sa preuve du Livre : des versets nombreux. Dieu Très-Haut dit :</p>
<p>« … et Nous ferons sortir, pour lui, au Jour de la Résurrection, un livre qu’il trouvera déployé : “ Lis ton livre : il te suffit, aujourd’hui, d’être ton propre comptable. ” » (al-Isrāʾ, 13-14)</p>
<p>et Sa parole :</p>
<p>« Quant à celui qui reçoit son livre en sa main droite, il dit : “ Tenez, lisez mon livre. ” » (al-Ḥāqqa, 19)</p>
<p>et Sa parole :</p>
<p>« Et quant à celui qui reçoit son livre en sa main gauche, il dit : “ Ah ! si seulement je n’avais pas reçu mon livre… ” » (al-Ḥāqqa, 25)</p>
<p>— à d’autres versets encore, explicites sur la remise aux serviteurs de leurs feuillets au Jour de la Résurrection. [Trois citations sans référence — emplacements vides, perte OCR ; cibles univoques par la doctrine des feuillets : le trio canonique de la remise — le livre trouvé déployé, la main droite, la main gauche — restitué.]</p>
<p>Je lis bien le texte et recherche ce qui suit :</p>
<ul>
<li>Je recherche des preuves du hadith prophétique établissant la remise aux serviteurs des feuillets de leurs œuvres, et la manière de cela.</li>
<li>Je recherche les espèces de ceux qui prennent les feuillets au Jour de la Résurrection.</li>
<li>Je ramène chacun des versets cités dans le texte à sa place en les sourates où ils se trouvent.</li>
</ul>
<h2>La préparation préalable (<em>iʿdād qablī</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et recherche ce que vise le Pont (<em>ṣirāṭ</em>), et comment s’effectue le passage sur lui.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16742":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16742 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    # contrôle apostrophes typographiques : aucune droite dans le corps
    n_droites = HTML_FR.count("'")
    print(f"OK — leçon 16742 main: FR {len(HTML_FR)} car ; apostrophes droites: {n_droites} (attendu 0)")


if __name__ == "__main__":
    main()
