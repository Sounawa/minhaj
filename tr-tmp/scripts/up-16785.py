#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16785 (tawhid-1es, leçon imprimée 19 — la
foi au Pont, ṣirāṭ).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire) ;
traduction savante avec restaurations du corpus canonique (cache quran = Ḥafṣ).

Vérifications et restaurations (cache quran = Ḥafṣ) :
- 2 citations vides (perte OCR systématique CMS) :
  Maryam 71 CONFORME (وإن منكم إلا واردها — le verset de la descente sur la
  Géhenne, ancre de la doctrine du Pont ; le fragment imprimé isolé « في بعض
  الأقول في تفسير الآية الكريمة » réintégré à la phrase) ;
  Kawthar 1 (citation SANS réf de l'iʿdād qablī — cible univoque : la leçon
  suivante traite du Bassin, dont l'ancre coranique est le Kawthar, vérifié
  sur le matn de 16786).
- Hadiths VÉRIFIÉS sunnah.com (curl + UA navigateur) :
  Bukhārî « فيضرب الصراط بين ظهراني جهنم فأكون أول من يجوز من الرسل بأمتي » —
  bāb imprimé (Adhān, فضل السجود) EXACT = ch. 129 = **Bukhārī 806** : texte
  VÉRIFIÉ CONFORME MOT À MOT (variante graphique ظهراني/ظهرانىْ notée) ;
  Abū Saʿīd « بلغني أن الجسر أدق من الشعرة وأحد من السيف » — notice
  imprimée telle quelle (la recherche sunnah.com la localise au voisinage
  immédiat du hadith 183, dont la description du pont — hameçons et épines —
  corrobore — noté) ;
  Anas « أليس الذي أمشاه على رجليه... » = Muslim 2806, Kitāb Ṣifat
  al-qiyāma, bāb يحشر الكافر على وجهه EXACT — texte VÉRIFIÉ CONFORME mot à
  mot ;
  Abū Saʿīd al-Khudrī « فيمر المؤمنون كطرف العين... » et « ومخدوش مرسل
  ومكدوس في نار جهنم » = Muslim 183a, bāb معرفة طريق الرؤية EXACT — textes
  VÉRIFIÉS CONFORMES mot à mot ;
  ʿĀʾisha (les trois stations) — al-Ḥākim, Mustadrak : réf imprimée conservée
  (le Mustadrak n'est pas hébergé sur sunnah.com).
- OCR/artefacts : titre « من فوائد الدرس » absent (paragraphe fondu) → h2
  restitué ; fragment « في بعض الأقوال... » en paragraphe isolé réintégré ;
  poème d'al-Maqqarī (Īḍāʾat al-dujna) : tableau 2 colonnes (colonne médiane
  vide = artefact), pages imprimées « 48-47 » en ordre descendant restituées
  47-48, graphie « أنقد » (pour أنقذ) rendue par le sens, dernier vers écho
  d'al-Aḥqāf 33 noté ; coquille الأبيت/الأبيات corrigée ; المومنين (ʿĀʾisha
  umm al-mūminīn) qayrawānienne notée ; dl/dt/dd vides + <p> vides + echo du
  titre en queue + divs vides — artefacts non rendus.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la foi au Pont (ṣirāṭ)</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la dix-neuvième leçon (19).</p>
<ul>
<li>Connaître le concept du Pont (<em>ṣirāṭ</em>) selon la Loi.</li>
<li>Saisir la graduation des gens en la vitesse de la traversée du Pont.</li>
<li>M’incorporer les vertus morales qui conduisent au passage sain sur le Pont.</li>
</ul>
<h2>Préambule</h2>
<p>Nous poursuivons l’entretien des scènes du Jour de la Résurrection et de ses terreurs — ce qui appelle tout croyant, en ce bas-monde, aux œuvres salutaires qui le sauveront de la plus grande frayeur au Jour de la Résurrection. Nous aborderons une autre espèce de ces terreurs : le passage sur le Pont.</p>
<p>Qu’entend-on par le Pont ? Et quels sont les rangs des gens dans le passage sur lui ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que le Pont est vérité : les serviteurs le traversent à la mesure de leurs œuvres — sauvés, gradués en la vitesse du salut sur lui, hors du Feu de la Géhenne ; et il est des gens que leurs œuvres y précipitèrent. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>ṣirāṭ</em> : la voie.</li>
<li><em>mutafāwit</em> (gradués) : inégaux en mérite, en compétition.</li>
<li><em>awbaqa</em> (perdit) : anéantit, fit choir.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> le moyen du passage sur le Pont.</li>
<li>Je dégage du <em>matn</em> la manière de la traversée du Pont par les serviteurs.</li>
</ul>
<h2>L’analyse (<em>taḥlīl</em>)</h2>
<p>La leçon comprend les axes suivants :</p>
<h3>Premièrement : l’obligation de la foi au Pont, et la manière du passage sur lui</h3>
<h4>1. L’obligation de la foi au Pont, et ses attributs</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que le Pont est vérité. » Le Pont relève de ce dont la foi et la conviction de l’existence sont obligatoires, comme la conviction que le passage sur lui est vérité — telle est la doctrine des gens de la Sunna, dont les Ashʿarites. D’après Abū Hurayra — que Dieu l’agrée —, le Prophète ﷺ dit : « … le Pont est alors jeté entre les deux versants de la Géhenne : je serai le premier des messagers à passer, avec ma communauté ; et nul ne parle, ce jour-là, hormis les messagers — et la parole des messagers, ce jour-là : “ Ô Dieu, salut, salut ! ” » [Ṣaḥīḥ al-Bukhārī, Kitāb al-Adhān, bāb du mérite de la prosternation — bāb imprimé EXACT (ch. 129 du Kitāb al-Adhān, hadith 806 d’Abū Hurayra) : texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com (variante graphique <em>ẓahrānay/ẓahrānā</em> notée).] Et d’après Abū Saʿīd — que Dieu l’agrée — : « Il m’est parvenu que le pont est plus fin qu’un cheveu, et plus tranchant qu’une épée. » [Ṣaḥīḥ Muslim, Kitāb al-Īmān, bāb de la connaissance de la voie de la vision — notice imprimée conservée : la recherche sunnah.com la localise au voisinage immédiat du hadith 183, dont la description du pont (hameçons et épines du <em>saʿdān</em>) la corrobore — noté.]</p>
<p>Et d’après Anas b. Mālik : un homme dit : « Ô Messager de Dieu, comment le mécréant sera-t-il rassemblé sur son visage, au Jour de la Résurrection ? » Il dit : « … Celui qui le fit marcher sur ses deux pieds en ce bas-monde n’est-Il pas capable de le faire marcher sur son visage, au Jour de la Résurrection ? » [Ṣaḥīḥ Muslim, Kitāb de la description de la Résurrection, du Paradis et du Feu, bāb « le mécréant est rassemblé sur son visage » — bāb imprimé EXACT (hadith 2806) : texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com.] Et ce pont est dressé sur la Géhenne : nul n’entre au Paradis sans passer sur la Géhenne — telle est la parole du Tout-Puissant :</p>
<p>« Il n’est, parmi vous, personne qui n’y vienne : c’est, sur ton Seigneur, un arrêt décrété. » (Maryam, 71)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — le verset de la venue à la Géhenne, ancre de la doctrine du Pont ; le fragment imprimé isolé « en certaines des interprétations du noble verset » est réintégré à la phrase.]</p>
<h4>2. La manière du passage sur le Pont</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « les serviteurs le traversent à la mesure de leurs œuvres ». Il est de la croyance obligatoire que les serviteurs passent sur le Pont à la mesure des œuvres qu’ils faisaient en ce bas-monde : les uns sauvés, les autres que leurs péchés précipitent. Et il apparaît que cela embrasse les croyants et les mécréants — vu ce qu’il y a dans le <em>Ṣaḥīḥ</em> d’al-Bukhārī, que le Prophète ﷺ dit : « … le Pont est alors jeté entre les deux versants de la Géhenne : je serai le premier des messagers à passer, avec ma communauté. » [Ṣaḥīḥ al-Bukhārī, Kitāb al-Adhān, bāb du mérite de la prosternation — réf imprimée conservée (hadith 806).] Le moment du passage sur lui est après le compte : quiconque le dépasse est sauvé, et quiconque ses péchés précipitent tombe dans le Feu.</p>
<h3>Deuxièmement : les états des gens dans le passage sur le Pont</h3>
<h4>1. Les états des justes</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « sauvés, gradués en la vitesse du salut sur lui, hors du Feu de la Géhenne ». Le passage des serviteurs sur le Pont est à la mesure de leurs œuvres : les uns, sauvés — gradués en la vitesse du passage sur lui, gradués dans le salut de la chute dans le Feu, inégaux en la vitesse du salut sur lui, hors du Feu de la Géhenne. Les uns le traversent comme l’éclair ; d’autres, comme le vent lâché ; d’autres sont comme les chevaux de tête ; d’autres courent, de course ; d’autres marchent, de marche ; d’autres marchent une fois et trébuchent une autre. D’après Abū Saʿīd al-Khudrī — que Dieu l’agrée —, le Prophète ﷺ dit : « Les croyants passent alors comme le clin d’œil, comme l’éclair, comme le vent, comme les oiseaux, comme les coursiers de race et les montures : l’un rescapé et préservé… » [Ṣaḥīḥ Muslim, Kitāb al-Īmān, bāb de la connaissance de la voie de la vision — bāb imprimé EXACT (hadith 183, d’Abū Saʿīd al-Khudrī) : texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com.] Tels sont les genres des sauvés sur le Pont, et la manière de leur passage. Il y a là l’explication de l’importance de l’œuvre dans le salut de l’homme et sa béatitude auprès de son Seigneur.</p>
<h4>2. Les états des non-justes</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et il est des gens que leurs œuvres y précipitèrent ». Voici la seconde espèce de ceux qui passent sur le Pont : des gens que leurs péchés anéantirent, que leurs désobéissances précipitèrent et firent choir en la Géhenne. D’après Abū Saʿīd al-Khudrī — que Dieu l’agrée —, le Prophète ﷺ dit, de ceux que leurs péchés précipitent sur le Pont : « … l’un éraflé, puis relâché ; l’autre précipité dans le Feu de la Géhenne. » [Ṣaḥīḥ Muslim, Kitāb al-Īmān, bāb de la connaissance de la voie de la vision — réf imprimée conservée (hadith 183) : texte VÉRIFIÉ CONFORME mot à mot.] Et d’après la Mère des croyants ʿĀʾisha — que Dieu l’agrée —, elle mentionna le Feu et pleura ; le Prophète ﷺ lui dit : « Qu’as-tu à pleurer ? » Elle dit : « J’ai mentionné le Feu, et pleuré. Vous souviendrez-vous des vôtres, au Jour de la Résurrection ? » Le Prophète ﷺ dit : « En trois stations, nul ne se souvient que de lui-même, tant est grand leur effroi et violente leur épouvante : à la Balance, quand elle est posée — jusqu’à savoir si elle s’allège ou s’alourdit ; au Livre — s’il tombe en sa main droite ou en sa gauche ; et au Pont, quand il est posé — jusqu’à ce qu’on le traverse. » [<em>Al-Mustadrak</em> d’Abū ʿAbd Allāh al-Ḥākim, Kitāb al-ahwāl — réf imprimée conservée (le <em>Mustadrak</em> n’est pas hébergé sur sunnah.com).]</p>
<h2>Les fruits de la leçon</h2>
<p>[Titre absent de l’extraction (paragraphe fondu) — restitué d’après la série.] On tire de la leçon que la finalité de l’étendue du Pont sur la Géhenne et du passage sur lui est la manifestation de l’immense grâce de Dieu Très-Haut et de Son bienfait envers Ses serviteurs croyants, dans le salut hors du Feu — et le regret de ceux que leurs péchés précipitèrent, à voir les croyants gagner la félicité perpétuelle au Paradis, tandis qu’eux pâtissent, de leur chute en la Géhenne, la misère éternelle — tous cependant partageant le passage en son principe. [Al-ʿArabī al-Lawh, <em>al-Rāʾid fī ʿilm al-ʿaqāʾid</em>, p. 232 — réf imprimée conservée.]</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>Je définis le Pont : au sens propre, et selon la terminologie de la Loi.</li>
<li>Je mentionne certains attributs du Pont.</li>
<li>Comment les serviteurs franchissent-ils ce Pont ? Et quelle est la sagesse de son dressage ?</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Abū l-ʿAbbās Aḥmad al-Maqqarī dit, en l’<em>Īḍāʾat al-dujna fī iʿtiqād ahl al-sunna</em> :</p>
<table>
<tbody>
<tr><td>Et tel le Pont aux crochets : quiconque en est tiré —</td><td>digne est-il alors du salut.</td></tr>
<tr><td>Un pont sur le dos de la Géhenne, en laquelle</td><td>précipite celui dont le pied a glissé.</td></tr>
<tr><td>Et ce qu’on dit — qu’il est plus fin qu’un cheveu :</td><td>Il l’a confirmé, et c’est vérité.</td></tr>
<tr><td>Et dans le <em>Ṣaḥīḥ</em> de Muslim est ce qui y mène,</td><td>et al-Ḍarīr y récita.</td></tr>
<tr><td>Et le Seigneur : leur marche sur lui ne L’accable point —</td><td>puisque à les créer Il ne s’est point lassé.</td></tr>
</tbody>
</table>
<p>[<em>Īḍāʾat al-dujna</em> d’al-Maqqarī : cinq vers sur le Pont, imprimés en tableau à deux colonnes d’hémistiches — la colonne médiane vide est un artefact d’extraction, non rendue ; pages imprimées « 48-47 » en ordre descendant, restituées 47-48 ; la graphie « <em>anqada</em> » de l’imprimé (pour <em>anqadha</em>, « en est tiré » — un point sous la lettre) rendue par le sens ; le dernier vers reprend al-Aḥqāf 33 (« et Il n’est point accablé par leur création ») — noté.]</p>
<ul>
<li>Je transcris les vers en mon cahier et les mémorise.</li>
<li>J’explique les vers en une explication concise, selon ce que j’ai compris de la leçon.</li>
<li>Je présente deux savants mentionnés en ces vers. [Coquille de l’imprimé <em>al-abīt</em> pour <em>al-abyāt</em> — corrigée ; les deux savants visés : Muslim, et « al-Ḍarīr » — identifié d’après la leçon suivante comme Abū l-Ḥajjāj Yūsuf al-Ḍarīr, mort en 520 H, auteur de vers de créance (<em>al-Tanbīh wa-l-irshād</em>).]</li>
</ul>
<h2>La préparation préalable (<em>iʿdād qablī</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et recherche ce qui suit :</p>
<ul>
<li>Ce dont la leçon traite, des affaires de l’au-delà.</li>
<li>Je recherche l’interprétation de la parole de Dieu Très-Haut :</li>
</ul>
<p>« Nous t’avons certes donné l’Abondance (<em>al-Kawthar</em>). » (al-Kawthar, 1)</p>
<p>[Citation imprimée vide, sans référence — perte OCR ; cible univoque : la leçon suivante traite du Bassin du Prophète ﷺ, dont l’ancre coranique est le Kawthar — restituée.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16785":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16785 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    # contrôle apostrophes typographiques : aucune droite dans le corps
    n_droites = HTML_FR.count("'")
    print(f"OK — leçon 16785 main: FR {len(HTML_FR)} car ; apostrophes droites: {n_droites} (attendu 0)")


if __name__ == "__main__":
    main()
