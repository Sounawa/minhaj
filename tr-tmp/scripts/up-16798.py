#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16798 (tawhid-1es, leçon imprimée 23 —
la foi aux anges, sur eux la paix).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire) ;
traduction savante avec restaurations du corpus canonique (cache quran = Ḥafṣ).

Vérifications et restaurations :
- 9 citations vides (perte OCR systématique CMS) :
  Infitār 10 CONFORME (لحافظين) ; Qāf 17-18 CONFORMES (les deux recueillants
  + l'observateur prêt) ; Anʿām 62 CONFORME ×2 (le retour au Maître véritable,
  le plus prompt des juges) ; Infitār 10-12 (imprimé « 12-11-10 » en ordre
  descendant → restitué en ordre canonique) CONFORME (les nobles scribes qui
  savent) ; Kahf 48 CONFORME (la présentation en rangs — l'établissement de la
  preuve) ; Ṭāriq 4 CONFORME (nulle âme qui n'ait un gardien) ; Sajda 11
  CONFORME (l'Ange de la mort — déjà ancrée par l'iʿdād de 16795) ; Zumur :
  imprimé « verset 39 » → écart, cible univoque 39:42 (الله يتوفى الأنفس حين
  موتها — le retrait des âmes attribué à Dieu ; 39:39 est étranger au propos).
- Hadith VÉRIFIÉ sunnah.com : « يتعاقبون فيكم ملائكة بالليل وملائكة بالنهار »
  = Bukhārī 555 (Mawāqīt, bāb فضل صلاة العصر) = 7486 (Tawḥīd, bāb كلام الرب
  مع جبريل) — le texte imprimé suit la leçon de 555 (ordre Fajr-ʿAsr,
  « أعلم بهم ») avec l'addition « يعرج إليه » (variante canonique alignée sur
  le titre du bāb imprimé) ; le bāb imprimé « تعرج الملائكة والروح إليه »
  désigne le Kitāb al-Tawḥīd (7486) — division des bāb variable selon les
  éditions — 6e occurrence du pattern bāb/localisation.
- Hadith d'al-Ṭabarānī (l'Ange de la mort et le moustique) : rendu tel quel,
  réf imprimée conservée (« rapporté par al-Ṭabarānī et d'autres » — hors des
  Six Livres).
- OCR/artefacts : dl/dt/dd vides + <p> vides + écho du titre en queue + divs
  vides — artefacts non rendus ; le muqaddima de 16795 (l'iʿdād) se referme
  ici (Sajda 11 citée).
- Doctrines rendues au plus près : la garde depuis le taklīf (hommes, djinns,
  croyants, mécréants) ; l'écriture universelle (jusqu'au mubāḥ et au
  gémissement, le signe de l'œuvre du cœur) ; la science divine totale (la
  phrase du matn comme clause anti-anthropomorphiste) ; le luṭf (les deux
  bénéfices : retenue et preuve) ; les trois attributions du tawaffī
  (l'agent véritable / l'exécutant immédiat / les auxiliaires — qābiḍ et
  muʿālijūn) ; l'échelle des anges d'al-Lawh (Jibrīl, Mīkhāʾīl, Isrāfīl,
  l'Ange de la mort, les gardes, les scribes, Munkar-Nakīr, Riḍwān).
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la foi aux anges (sur eux la paix)</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la vingt-troisième leçon (23).</p>
<ul>
<li>Connaître l’existence d’anges gardiens qui inscrivent les œuvres des serviteurs.</li>
<li>Établir que l’Ange de la mort est chargé de la saisie des âmes.</li>
<li>Avoir présent à l’esprit la surveillance de Dieu Très-Haut sur ma conduite.</li>
</ul>
<h2>Préambule</h2>
<p>Il a été avancé en une leçon précédente que les hommes recevront leurs feuillets et les registres des œuvres accomplies en ce bas monde, pour l’exposition devant Dieu Très-Haut, l’interrogation et le compte — en bien ou en mal —, en un jour dont la devise est : « Nulle injustice aujourd’hui. »</p>
<p>Qui donc a écrit ces feuillets ? Qui les lit ? Et qui est chargé de la saisie des âmes des serviteurs ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et qu’il est sur les serviteurs des gardiens qui inscrivent leurs œuvres, et que rien de cela n’échappe à la science de leur Seigneur ; et que l’Ange de la mort saisit les âmes sur l’autorisation de son Seigneur. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>ḥafaza</em> (gardiens) : pluriel de <em>ḥāfiẓ</em> — préserver la chose, la protéger et l’empêcher de l’altération et de la perte.</li>
<li><em>yaqbiḍ</em> (saisit) : retient et prend.</li>
<li><em>al-arwāḥ</em> (les âmes) : singulier <em>rūḥ</em> — ce par quoi les âmes ont la vie.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> la mission des gardiens.</li>
<li>Je dégage du <em>matn</em> qui prend en charge la saisie des âmes.</li>
</ul>
<h2>L’analyse (<em>taḥlīl</em>)</h2>
<p>La leçon embrasse les axes suivants :</p>
<h3>Premièrement : la foi aux anges gardiens et leur mission</h3>
<h4>1. La foi aux anges gardiens</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et qu’il est sur les serviteurs des gardiens ». Ce qu’il faut tenir pour vrai : il est, sur les serviteurs — hommes et djinns, croyants et mécréants, mâles et femelles —, depuis le moment de l’imposition légale (<em>taklīf</em>), des gardiens et des scribes, du fait de l’arrivée du texte à ce sujet dans le Noble Coran et les hadiths authentiques. Du Coran, la parole de Dieu Très-Haut :</p>
<p>« … alors que veillent sur vous des gardiens… » (al-Infitār, 10)</p>
<p>et Sa parole :</p>
<p>« … quand les deux recueillants, assis à droite et à gauche, recueillent. Il ne prononce pas une parole sans avoir auprès de lui un observateur prêt à l’inscrire. » (Qāf, 17-18)</p>
<p>[Citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées CONFORMES — les gardiens, les deux recueillants et l’observateur prêt : les trois ancre de la doctrine de la garde.] Et Sa parole :</p>
<p>« Ils sont ensuite ramenés vers Dieu, leur vrai Maître. C’est à Lui qu’appartient le jugement, et Il est le plus prompt des juges. » (al-Anʿām, 62)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.] Et du hadith, sa parole ﷺ : « Des anges se relaient en vous : des anges de nuit et des anges de jour ; ils se rejoignent à la prière de l’aube et à la prière de l’après-midi ; puis montent vers Lui ceux qui ont passé la nuit parmi vous — et Il les interroge, Lui qui sait mieux qu’eux : Comment avez-vous laissés Mes serviteurs ? Ils disent : Nous les avons laissés en prière, et Nous sommes venus à eux alors qu’ils priaient. » [Ṣaḥīḥ d’al-Bukhārī, Kitāb al-Tawḥīd, bāb de la parole de Dieu Très-Haut : « Les anges et l’Esprit montent vers Lui » — le texte imprimé suit la leçon de la narration 555 (Kitāb Mawāqīt al-ṣalāt, bāb du mérite de la prière de l’après-midi : ordre aube-après-midi et « Lui qui sait mieux qu’eux ») et celle de 7486 (Kitāb al-Tawḥīd), avec l’addition « montent vers Lui » (<em>yaʿruju ilayhi</em>) — variante canonique alignée sur le titre du bāb : texte VÉRIFIÉ sur sunnah.com.]</p>
<h4>2. La mission des anges gardiens</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « qui inscrivent leurs œuvres » — c’est-à-dire : la mission des gardiens est l’inscription des œuvres des serviteurs, leurs paroles et leurs actes — même l’indifférent (<em>mubāḥ</em>) et le gémissement en la maladie. Quant à l’œuvre du cœur, Dieu place en eux un signe de l’œuvre du cœur, par quoi ils distinguent la bonne action de la mauvaise. Le fondement de ce que l’auteur a mentionné — que Dieu lui fasse miséricorde — est la parole de Dieu Très-Haut :</p>
<p>« … alors que veillent sur vous des gardiens, de nobles scribes, qui savent ce que vous faites. » (al-Infitār, 10-12)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée « versets 12-11-10 » est en ordre descendant — restituée en ordre canonique — la série des trois versets des nobles scribes.] La parole de l’auteur : « et que rien de cela n’échappe à la science de leur Seigneur » — il l’a explicitée pour repousser ce que l’on pourrait supposer : que le bénéfice de l’inscription des gardiens serait que quelque chose des œuvres, paroles et affaires des serviteurs échappe à Sa science — Dieu est exalté au-dessus de cela, d’une exaltation immense. Le bénéfice de leur charge est la prévenance (<em>luṭf</em>) de Dieu Très-Haut envers Ses serviteurs : s’ils savent que des anges conservent leurs paroles, leurs actes et leurs intentions, et les inscrivent, ils se retiennent des désobéissances ; et l’établissement de la preuve contre eux — comme en la parole de Dieu Très-Haut :</p>
<p>« Et ils seront présentés en rangs devant ton Seigneur : „Vous voilà venus à Nous comme Nous vous avons créés la première fois. Pourtant vous prétendiez que Nous ne remplirions pas Nos promesses“. » (al-Kahf, 48)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — la présentation en rangs, ancre de l’établissement de la preuve.] Et Sa parole :</p>
<p>« Il n’est pas d’âme qui n’ait sur elle un gardien. » (al-Ṭāriq, 4)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — nulle âme sans gardien.]</p>
<h3>Deuxièmement : la foi en ce que l’Ange de la mort saisit les âmes</h3>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et que l’Ange de la mort saisit les âmes sur l’autorisation de son Seigneur ». Ce qu’il faut tenir pour vrai : l’Ange de la mort prend en charge la saisie de toutes les âmes — les âmes des hommes et des djinns, et de tout ce qui possède une âme —, et tout cela sur l’autorisation et le commandement de son Seigneur. Dieu Très-Haut dit :</p>
<p>« Dis : „L’Ange de la mort, qui est chargé de vous, vous saisira ; puis vous serez ramenés vers votre Seigneur“. » (al-Sajda, 11)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — le verset de l’Ange de la mort, annoncé par l’iʿdād de la leçon précédente.] Et dans un long hadith rapporté par al-Ṭabarānī et d’autres, l’Ange de la mort dit : « Par Dieu, si je voulais saisir l’âme d’un moustique, je ne le pourrais pas, jusqu’à ce que Dieu Lui-même autorise sa saisie. » [Référence imprimée conservée — hadith d’al-Ṭabarānī, hors des Six Livres.] Le Coran est venu attribuant le retrait (<em>tawaffī</em>) à Dieu Très-Haut en un lieu, et aux anges en un autre. Dieu Très-Haut dit :</p>
<p>« Dieu reçoit les âmes au moment de leur mort, ainsi que celles qui ne meurent pas au cours de leur sommeil. Il retient celles à qui Il a décrété la mort, et renvoie les autres jusqu’à un terme fixé… » (al-Zumar, 42)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée « verset 39 » est en écart : la cible est univoque — le verset du retrait des âmes attribué à Dieu est 39:42 ; le verset 39:39 est étranger au propos.] Et Il dit :</p>
<p>« Ils sont ensuite ramenés vers Dieu, leur vrai Maître. C’est à Lui qu’appartient le jugement, et Il est le plus prompt des juges. » (al-Anʿām, 62)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — seconde occurrence du verset du retour.] La réponse : l’attribution du retrait à Dieu Très-Haut — car Il est l’agent au sens véritable (<em>al-fāʿil al-ḥaqīqī</em>) ; à l’Ange de la mort — car il est l’exécutant immédiat de la saisie de l’âme ; aux anges — car ils sont les auxiliaires de l’Ange de la mort : ils participent à l’extraire du corps. Lui saisit (<em>qābiḍ</em>) — eux opèrent (<em>muʿālijūn</em>).</p>
<h2>Les fruits de la leçon</h2>
<p>La présence constante de la surveillance de Dieu Très-Haut en toute chose — Lui, glorifié soit-Il, connaît ce que fait l’homme : Il a commis sur l’homme des gardiens de ses actes, et Il l’en informera au jour de l’exposition devant Lui. Par là, l’homme réalise la finalité de son existence : réaliser la servitude (<em>ʿubūdiyya</em>) envers Dieu et la sincérité envers Lui en toute chose, et répondre à Son ordre et à Son interdit — et se réalisent alors l’équité et la sagesse en ses conduites.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>Qui sont les gardiens (<em>ḥafaza</em>) ? Et pourquoi furent-ils nommés ainsi ?</li>
<li>Quelle est la finalité de l’inscription des œuvres des serviteurs ?</li>
<li>Quand les anges de la nuit et les anges du jour se rejoignent-ils ? Et quel en est le bénéfice ?</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Le maître al-ʿArabī al-Lawh — que Dieu lui fasse miséricorde — dit : « Parmi eux — les anges — : celui qui est chargé de la révélation de Dieu Très-Haut à Ses messagers — sur eux la paix : l’Esprit fidèle, Gabriel (<em>Jibrīl</em>) — sur lui la paix ; celui qui est chargé de la pluie et de ses conduites là où Dieu l’a ordonné : Mīkhāʾīl — sur lui la paix ; celui qui est chargé de la Trompe : Isrāfīl — sur lui la paix —, qui y soufflera trois souffles sur l’ordre de son Seigneur, puissant et majestueux ; celui qui est chargé de la saisie des âmes : l’Ange de la mort et ses auxiliaires ; celui qui est chargé de la garde du serviteur en sa résidence et ses déplacements, en son sommeil et sa veille, en tous ses états ; ceux qui sont chargés de conserver l’œuvre du serviteur, de bien comme de mal : les nobles scribes (<em>al-kirām al-kātibūn</em>) ; ceux qui sont chargés de l’épreuve de la tombe : Munkar et Nakīr ; les gardiens du Paradis, dont le chef est Riḍwān — sur eux la paix ; et d’autres encore, parmi les espèces d’anges. » [<em>Al-Rāʾid fī ʿilm al-ʿaqāʾid</em>, p. 199 — adapté (<em>bi-taṣarruf</em>).]</p>
<p>Je lis bien le texte et réalise ce qui suit :</p>
<ul>
<li>J’extrais du texte les catégories d’anges.</li>
</ul>
<h2>La préparation préalable (<em>iʿdād qablī</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et recherche ce qui suit :</p>
<ul>
<li>Quelles sont les générations préférées ?</li>
<li>Je recherche les biographies des quatre califes bien guidés et leurs mérites.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16798":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16798 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print(f"OK 16798 -> {len(HTML_FR)} car FR injectés")


if __name__ == "__main__":
    main()
