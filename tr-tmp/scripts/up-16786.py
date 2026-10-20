#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16786 (tawhid-1es, leçon imprimée 20 — la
foi au Bassin du Prophète ﷺ et ses visiteurs).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire) ;
traduction savante avec restaurations du corpus canonique (cache quran = Ḥafṣ).

Vérifications et restaurations (cache quran = Ḥafṣ) :
- 1 citation vide (perte OCR CMS) : Kawthar 1 CONFORME (إنا أعطيناك الكوثر —
  l'ancre du Bassin, préparée par l'iʿdād qablī de la leçon précédente).
- Hadiths VÉRIFIÉS sunnah.com (curl + UA navigateur) :
  Abū Dharr « ما آنية الحوض » = Muslim 2300, Kitāb al-Faḍāʾil, bāb إثبات
  حوض نبينا وصفاته EXACT — texte VÉRIFIÉ avec variantes de leçon notées
  (والذي نفسي بيده/والذي نفس محمد بيده ; ليس يظمأ/لم يظمأ ; ألا
  في/في الليلة) ;
  ʿAbd Allāh b. ʿAmr « حوضي مسيرة شهر » = Muslim 2292 (même bāb) —
  attribution confirmée par recherche sunnah.com (page en accès intermittent) ;
  Samura b. Jundab « إن لكل نبي حوضا » = Tirmidhī 2443 (Kitāb Ṣifat
  al-qiyāma) — attribution confirmée par recherche ;
  Asmāʾ « إني على الحوض حتى أنظر » — bāb imprimé EXACT (les narrations
  d'Asmāʾ en Muslim 2292-2294 avec variantes) ; la leçon imprimée suit mot à
  mot la version parallèle de Bukhārī 6593 (Riqāq, bāb du Bassin — أمَا
  شعرت/هَل شعرت près) — divergence de localisation notée (pattern documenté) ;
  Abū Hurayra ghurra « لكم سيما ليست لأحد من الأمم » = Muslim 247a, Kitāb
  al-Ṭahāra, bāb استحباب إطالة الغرة والتحجيل في الوضوء EXACT — texte
  VÉRIFIÉ CONFORME mot à mot.
- OCR/artefacts : la leçon EST COMPLÈTE structurellement (titres présents) ;
  al-Ḍarīr (Abū l-Ḥajjāj Yūsuf, m. 520 H) du Tanbīh wa-l-irshād : quatre
  vers en tableau (colonne médiane vide = artefact) — IDENTIFICATION du
  « al-Ḍarīr » du vers d'al-Maqqarī de la leçon précédente, notée ; dl/dt/dd
  vides + <p> vides + echo du titre en queue + divs vides — artefacts non
  rendus.
- Doctrines rendues au plus près : le tawātur du Bassin ; l'ummat al-ijāba ;
  l'antériorité du Bassin (avant Balance/Pont/compte — l'argument de non-retour) ;
  l'arḍ al-mubaddala (terre transmuée) ; le Kawthar propre au Prophète ﷺ et
  la réconciliation avec « à chaque prophète un bassin » ; les tabdīl/taḥrīf
  chassés — au pire les pécheurs publics.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la foi au Bassin du Prophète ﷺ et ses visiteurs</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la vingtième leçon (20).</p>
<ul>
<li>Connaître le Bassin du Prophète ﷺ.</li>
<li>Connaître qui est éloigné et chassé du Bassin du Prophète ﷺ.</li>
<li>Accomplir les œuvres salutaires, pour obtenir l’honneur de la venue au Bassin du Prophète ﷺ.</li>
</ul>
<h2>Préambule</h2>
<p>Les terreurs du Jour de la Résurrection sont immenses, et la plus grande frayeur saisit les gens du Stationnement : le soleil se rapproche au-dessus de leurs têtes, ils suent — et la sueur, de certains, atteint les nuques. Tandis que les gens sont en cet état, Dieu ouvre une porte de miséricorde : le Bassin de notre maître Muḥammad ﷺ.</p>
<p>Qu’est-ce donc que le Bassin ? Qui vient à lui ? Et qui en est chassé ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>Ibn Abī Zayd — que Dieu Très-Haut lui fasse miséricorde — dit : « Et la foi au Bassin du Messager de Dieu ﷺ : sa communauté y vient ; quiconque en boit n’a plus soif ; et en est chassé quiconque altéra et changea. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>ḥawḍ</em> (bassin) : le lieu où l’eau s’assemble ; pluriel : <em>aḥwāḍ</em> et <em>ḥiyāḍ</em>.</li>
<li><em>tariduh</em> (y vient) : l’atteint ; et l’abord (<em>mawrid</em>) est le lieu où l’on vient à l’eau pour l’abreuver ; le <em>ward</em> est la boisson.</li>
<li><em>yaẓmaʾ</em> (a soif) : a soif.</li>
<li><em>yuʾdhā</em> (est chassé) : est éloigné et repoussé.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>Je dégage du <em>matn</em> le statut de la foi au Bassin du Prophète ﷺ.</li>
<li>J’extrais du <em>matn</em> les états des gens au Bassin du Prophète ﷺ.</li>
<li>Je dégage du <em>matn</em> la cause de l’éloignement de certains du Bassin du Prophète ﷺ.</li>
</ul>
<h2>L’analyse (<em>taḥlīl</em>)</h2>
<h3>Premièrement : la foi au Bassin du Prophète ﷺ, et qui y vient</h3>
<h4>1. La foi au Bassin du Prophète ﷺ</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et la foi au Bassin du Messager de Dieu ﷺ. » Il est de la croyance obligatoire, et de la conviction de son existence, qu’il y a un Bassin du Messager de Dieu ﷺ : les transmissions à son sujet sont récurrentes (<em>tawātur</em>), les auteurs des recueils de santé en ont produit les hadiths, les anciens vertueux sont unanimes dessus, et, d’un accord unanime, ils implorent Dieu de les en abreuver. D’après Abū Dharr — que Dieu l’agrée — : je dis : « Ô Messager de Dieu, que sont les vaisseaux du Bassin ? » Il dit : « Par Celui qui tient mon âme en Sa main : ses vaisseaux sont plus nombreux que les étoiles du ciel et ses constellations, en la nuit sombre et sereine. Ce sont des vaisseaux du Paradis : quiconque en boit n’a plus soif — jamais plus. Deux canaux du Paradis y déversent : quiconque en boit n’a plus soif. Sa largeur égale sa longueur — d’Amman à Ayla ; son eau est plus blanche que le lait, et plus douce que le miel. » [Ṣaḥīḥ Muslim, Kitāb al-Faḍāʾil, bāb de l’établissement du Bassin de notre Prophète ﷺ et de ses attributs — bāb imprimé EXACT (hadith 2300, d’Abū Dharr) : texte VÉRIFIÉ sur sunnah.com avec les variantes de leçon notées (« Par Celui qui tient mon âme / qui tient l’âme de Muḥammad en Sa main » ; « n’a plus / n’aura plus soif »).]</p>
<p>Et ʿAbd Allāh b. ʿAmr b. al-ʿĀṣ — que Dieu l’agrée — dit : le Messager de Dieu ﷺ dit : « Mon Bassin est d’un mois de chemin ; ses angles sont égaux ; son eau est plus blanche que le lait, son parfum plus suave que le musc ; ses coupes sont comme les étoiles du ciel : quiconque en boit n’a plus jamais soif. » [Ṣaḥīḥ Muslim, Kitāb al-Faḍāʾil, bāb de l’établissement du Bassin de notre Prophète ﷺ et de ses attributs — bāb imprimé EXACT (hadith 2292) : attribution confirmée par la recherche sunnah.com.] Il — le Bassin — est l’une des positions sur le sens du Kawthar ; et il sera en la terre transmuée (<em>al-arḍ al-mubaddala</em>) : une terre blanche comme l’argent, où nul sang ne fut versé et où personne ne fut lésé sur son dos ; quiconque en boit une gorgée n’a plus jamais soif après elle.</p>
<h4>2. Qui vient au Bassin du Prophète ﷺ</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « sa communauté y vient ; quiconque en boit n’a plus soif » — c’est-à-dire : la communauté de la réponse (<em>ummat al-ijāba</em>) — ceux qui suivirent sa Législation ﷺ — y vient et en boit, à leur sortie des tombeaux, altérés. Et le sens apparent est que sa venue est avant la Balance, le Pont et le compte : car s’il était après le Pont, il ne serait pas valable qu’on en chasse quelqu’un vers le Feu — quiconque a traversé le Pont n’a, vers le Feu, nul retour jamais. Et il n’y a pas, en la question, d’argument tranchant auquel revenir : l’obligatoire est donc la conviction de la fermeté du Bassin, du Pont, de la Balance et du compte — et Dieu sait mieux lequel précède l’autre.</p>
<p>Dieu l’a donné à notre Prophète Muḥammad ﷺ en propre ; mais il est venu, dans le hadith d’al-Tirmidhī, d’après Samura b. Jundab, que le Messager de Dieu ﷺ dit : « À chaque prophète est un Bassin ; et ils se prévaudront de savoir lequel a le plus de venants. J’espère être celui d’entre eux aux venants les plus nombreux. » [Sunan d’al-Tirmidhī, Kitāb de la description de la Résurrection, des exhortations et de la scrupulosité, bāb de ce qui est venu sur la description du Bassin — réf imprimée conservée (hadith 2443) : attribution confirmée par la recherche sunnah.com.] On réconcilie les deux en ce que ce qui est propre à lui ﷺ est le Kawthar, qui verse de son eau en son Bassin : son pareil n’a pas été transmis pour un autre, et le bienfait en a été objet de gratitude en la parole de Dieu Très-Haut :</p>
<p>« Nous t’avons certes donné l’Abondance (<em>al-Kawthar</em>). » (al-Kawthar, 1)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — l’ancre du Bassin, dont la leçon précédente portait la préparation.]</p>
<p>La parole de l’auteur — que Dieu lui fasse miséricorde — « quiconque en boit n’a plus soif » : quiconque en boit n’a plus soif, fût-ce d’une seule gorgée — car c’est la boisson des gens du Paradis.</p>
<h3>Deuxièmement : qui est chassé du Bassin du Prophète ﷺ</h3>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et en est chassé quiconque altéra et changea ». Est chassé, écarté et repoussé du Bassin du Prophète ﷺ — et n’en boit pas — quiconque altéra et changea en sa Législation : quiconque apostasia de la religion de Dieu, ou y innova ce que Dieu n’agrée pas et n’a pas autorisé, celui-là est de ceux qu’on chasse du Bassin du Prophète ﷺ ; et les plus durement chassés : ceux qui exhibent les péchés majeurs et prennent les désobéissances à la légère.</p>
<p>La preuve de ce que dit l’auteur : des hadiths nombreux, dont le hadith d’Asmāʾ bt. Abī Bakr — que Dieu l’agrée —, qui dit : le Messager de Dieu ﷺ dit : « Je suis au Bassin, à regarder qui, de vous, vient à moi. Des gens seront retranchés avant moi, et je dirai : “ Seigneur ! des miens, et de ma communauté ! ” Il sera dit : “ N’as-tu pas su ce qu’ils ont fait après toi ? Par Dieu, ils n’ont point cessé, après toi, de revenir sur leurs talons. ” » [Ṣaḥīḥ Muslim, Kitāb al-Faḍāʾil, bāb de l’établissement du Bassin de notre Prophète ﷺ et de ses attributs — bāb imprimé EXACT : les narrations d’Asmāʾ s’y lisent (hadiths 2292-2294) avec leurs variantes (« je regarde/attends qui vient », “ des hommes seront retranchés/des gens seront pris ”, “ n’as-tu pas su/tu ne sais pas ”) ; la leçon imprimée suit mot à mot la version parallèle de Bukhārī 6593 (Kitāb al-Riqāq, bāb du Bassin) — divergence de localisation notée.] ; et d’après Abū Hurayra — que Dieu l’agrée —, le Messager de Dieu ﷺ dit : « … Et je repousse les gens de lui, comme l’homme repousse les chameaux des gens de son bassin. » Ils dirent : « Nous reconnaîtras-tu, ce jour-là ? » Il dit : « Oui : vous aurez une marque qu’aucune communauté n’aura — vous viendrez à moi, au front et aux membres marqués de blanc, des traces de l’ablution. » [Ṣaḥīḥ Muslim, Kitāb al-Ṭahāra, bāb du caractère recommandé de l’élargissement du front blanc et des membres blancs en l’ablution — bāb imprimé EXACT (hadith 247, d’Abū Hurayra) : texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com.]</p>
<h2>Les fruits de la leçon</h2>
<p>L’explication du rang du Prophète ﷺ auprès de son Seigneur — puissant et majestueux : Il l’honora d’un Bassin que visite sa communauté — celle qui répondit à son appel et s’agrippa à sa Législation, puisque lui obéir est obéir à Dieu Très-Haut. Il y a là une exhortation à s’agripper à sa Législation, à marcher sur sa guidance et à se parer de ses caractères ﷺ : il fut, certes, une miséricorde offerte aux mondes.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>Qui vient au Bassin du Prophète ﷺ ?</li>
<li>D’où le Bassin du Prophète ﷺ tire-t-il son eau ?</li>
<li>Quelle est la rétribution de quiconque altéra et changea en la Loi ?</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Abū l-Ḥajjāj Yūsuf al-Ḍarīr — mort en 520 H — dit ce qui suit :</p>
<table>
<tbody>
<tr><td>Le Bassin du Prophète, en vérité, sera dressé :</td><td>sa communauté y vient, et boit ;</td></tr>
<tr><td>le renégat innovateur en est chassé,</td><td>comme sont chassées les chamelles égarées ;</td></tr>
<tr><td>ses vaisseaux, en nombre, sont comme les étoiles —</td><td>qui en boit n’a plus soif, jamais ;</td></tr>
<tr><td>sa boisson, en saveur et en beauté,</td><td>dépasse tout ce qu’on connut des états.</td></tr>
</tbody>
</table>
<p>[<em>Al-Tanbīh wa-l-irshād fī ʿilm al-iʿtiqād</em> d’Abū l-Ḥajjāj Yūsuf al-Ḍarīr (m. 520 H), p. 236 — réf imprimée conservée ; quatre vers en tableau à deux colonnes d’hémistiches — la colonne médiane vide est un artefact d’extraction, non rendue ; l’auteur est l’« al-Ḍarīr » du vers d’al-Maqqarī cité en la leçon précédente — identification notée.]</p>
<p>J’explique le contenu des vers en abrégé, à l’appui de certains versets coraniques et hadiths prophétiques sur le sujet.</p>
<h2>La préparation préalable (<em>iʿdād qablī</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et recherche ce qui suit :</p>
<ul>
<li>La définition de la foi (<em>īmān</em>) et ses piliers.</li>
<li>Par quoi la foi croît-elle, et décroît-elle ?</li>
<li>Quel rapport la foi a-t-elle avec l’œuvre ?</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16786":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16786 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    # contrôle apostrophes typographiques : aucune droite dans le corps
    n_droites = HTML_FR.count("'")
    print(f"OK — leçon 16786 main: FR {len(HTML_FR)} car ; apostrophes droites: {n_droites} (attendu 0)")


if __name__ == "__main__":
    main()
