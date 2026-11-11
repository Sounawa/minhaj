#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16721 (tawhid-1es, leçon 9 — la foi au
décret et à la prédestination, qaḍāʾ et qadar).

RESTITUTION post-rollback : traduction livrée à l'origine au tour R127 d'origine
(perdu du disque) — tête et queue restituées verbatim depuis la mémoire de
session, partie centrale traduite à l'identique depuis la source AR.

Vérifications et restitutions (cache quran = Ḥafṣ ; sunnah.com UA navigateur) :
- Matn : « والإيمان بالقدر خيره وشره حلوه ومره، وكل ذلك قد قدّره ربّنا،
  ومقادير الأمور بيده، ومصدرها عن قضائه، علم كل شيء قبل كونه فجري على
  قدره » — rendu fidèlement.
- Takwīr 29 (citation vide, perte OCR) RESTAURÉE du cache :
  « وما تشاءون إلا أن يشاء الله رب العالمين » — CONFORME (la volonté
  créaturelle sous la volonté divine — cible univoque du contexte des fruits).
- Hadith de Jibrīl « وأن تؤمن بالقدر خيره وشره » — VÉRIFIÉ sunnah.com :
  Muslim 8 (Livre de la Foi, question de Jibrīl) porte « وَتُؤْمِنَ
  بِالْقَدَرِ خَيْرِهِ وَشَرِّهِ » — le manuel imprime « وأن تؤمن » :
  variante mineure de citation, notée inline.
- Hadith de Jābir (istithmār) — VÉRIFIÉ sunnah.com : Tirmidhī 2144
  (Chapitres sur al-Qadar), voie Jaʿfar b. Muḥammad ← son père ← Jābir b.
  ʿAbdallāh — TEXTE VERBATIM (« لا يؤمن عبد حتى يؤمن بالقدر خيره وشره حتى
  يعلم أن ما أصابه لم يكن ليخطئه وأن ما أخطأه لم يكن ليصيبه ») ; le manuel
  ajoute le wāw devant « حتى يعلم » (variante mineure de citation) ; Abū
  ʿĪsā juge le hadith gharīb, connu seulement par la voie de ʿAbdallāh b.
  Maymūn — noté inline (la leçon l'invoque comme istithmār, rendu fidèle).
- DOUBLON OCR : le hadith de Jābir imprimé 2× (entrelacé) — rendu UNE fois,
  noté.
- COQUILLE de titre : la dernière section « الاستثمار » imprimée au lieu de
  « الإعداد القبلي » (le contenu — « je lis le matn de la leçon suivante... »
  est celui de l'iʿdād) — titre restitué, coquille notée.
- Lisān al-ʿArab, matières qaḍā/qadar (Ibn Manẓūr : le décret et la
  prédestination comme fondation et édifice) — rendu fidèlement avec réfs.
- Le taʿalluq tanjīzī (le lien exécutoire de la volonté et de la puissance
  au possible) rendu dans les fruits, tel que l'imprimé.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la foi au décret et à la prédestination (qaḍāʾ et qadar)</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la neuvième leçon (9).</p>
<ul>
<li>Connaître le sens du décret (qaḍāʾ) et de la prédestination (qadar).</li>
<li>Distinguer le décret de la prédestination.</li>
<li>Faire mienne en ma vie l’effet de la foi au décret et à la prédestination.</li>
</ul>
<h2>Préambule</h2>
<p>Il advient à l’homme, en sa vie, des choses qu’il n’attendait point et qui ne lui étaient point connues avant leur survenue ; et lui échappent des choses dont il attendait la survenue. Le croyant traite ce qui advint et ce qui échappa par l’agrément, la soumission et le remise-à-Dieu : car il croit que Dieu a écrit ce qui fut, ce qui sera et ce qui est en train d’être, et a décrété et prédestiné cela dans la pré-éternité. Le non-croyant, lui, s’affole et n’agrée point — et il n’empêche que n’advienne que ce que Dieu a décrété et prédestiné.</p>
<p>Qu’est-ce que le décret ? Qu’est-ce que la prédestination ? Et quel est l’effet de la foi aux deux sur la vie du musulman ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et la foi à la prédestination (<em>qadar</em>) — en son bien et en son mal, en son doux et en son amer : tout cela, notre Seigneur l’a prédestiné ; les mesures des choses sont en Sa main, et leur surgissement procède de Son décret (<em>qaḍāʾ</em>) ; Il a su toute chose avant son être — et elle s’accomplit selon Sa mesure. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>al-qadar</em> (la prédestination) : le mesurage (<em>al-taqdīr</em>).</li>
<li><em>al-qaḍāʾ</em> (le décret) : en la langue, il reçoit plusieurs sens, parmi lesquels le jugement, l’imposition, la création, le mesurage et l’achèvement.</li>
<li><em>maṣdar</em> (le surgissement) : le lieu du procéder, de la survenue et de l’avènement.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> le comportement du croyant devant la prédestination.</li>
<li>J’extrais du <em>matn</em> : d’où procèdent les choses ? Et comment s’accomplissent-elles ?</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : la foi au décret et à la prédestination</h3>
<h4>1. La définition du décret et de la prédestination</h4>
<p>a. Le décret (<em>al-qaḍāʾ</em>). En la langue (<em>lughatan</em>) : il reçoit plusieurs sens, parmi lesquels l’achèvement, le jugement, la création et le mesurage [<em>Lisān al-ʿArab</em>, racine <em>q-ḍ-y</em>]. En le terme (<em>iṣṭilāḥan</em>) : la volonté des choses par Dieu en la pré-éternité, telles qu’elles sont et tant qu’elles sont — il est donc un attribut d’essence.</p>
<p>b. La prédestination (<em>al-qadar</em>). En la langue : le décret et le jugement — c’est ce que Dieu, Puissant et Magnifié, décrète du décret et juge des choses [<em>Lisān al-ʿArab</em>, racine <em>q-d-r</em>]. En le terme : la production (<em>ījād</em>) des choses par Dieu selon une mesure particulière et un mesurage déterminé que Dieu veut en leurs essences et leurs états, conforme à ce dont Sa science a précédé — elle remonte donc aux attributs d’action, car elle est dite de la production : elle est au nombre des attributs d’action.</p>
<h4>2. La foi au décret et à la prédestination</h4>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Et la foi à la prédestination — en son bien et en son mal, en son doux et en son amer : tout cela, notre Seigneur l’a prédestiné. » Ibn Manẓūr dit : « Le décret et la prédestination sont deux réalités solidaires, dont l’une ne se sépare point de l’autre : l’une est au rang de fondation — la prédestination ; et l’autre au rang d’édifice — le décret. Quiconque entreprend de séparer les deux entreprend de démolir l’édifice et de le défaire. » [<em>Lisān al-ʿArab</em>, racine <em>q-d-r</em>.]</p>
<p>La foi à la prédestination signifie la foi que la prédestination s’accomplit par le bien — ce en quoi il y a profit —, et par le mal — ce en quoi il y a dommage —, par le doux — ce en quoi il y a délectation —, et par l’amer — ce en quoi il y a peine.</p>
<p>La foi à la prédestination, son bien et son mal, est un pilier des six piliers de la foi : la foi n’est point valide sans elle. Les pronoms de « son bien et son mal, son doux et son amer » reviennent sur la prédestination — il faut donc croire et attester la généralité de la volonté de Dieu Très-Haut sur l’ensemble des possibles, qu’ils soient bien ou mal, doux ou amer. Les savants interprétèrent le bien par les obéissances, le doux par leur délectation et leur récompense, le mal par la désobéissance, et l’amer par sa peine et son châtiment.</p>
<h3>Deuxièmement : les mesures des choses et leur surgissement en Sa main, glorifié soit-Il</h3>
<h4>1. Les mesures des choses en la main de Dieu Très-Haut</h4>
<p>L’auteur dit : « les mesures des choses sont en Sa main » — le commencement des choses est en Sa main, l’Elevé : tous les contingents adviennent par la volonté de Dieu, Sa volonté (<em>mašīʾa</em>), Son décret et Sa prédestination — qu’ils soient bien ou mal, obéissance ou désobéissance. Cependant, l’obéissance [advient] par Son décret, Sa prédestination, Son amour, Son agrément et Son commandement ; et la désobéissance par Sa volonté, Son décret et Sa prédestination : car il n’advient en Son royaume que ce qu’Il veut, et l’on ne saurait Lui désobéir par contrainte. Et le châtiment s’ensuit de la désobéissance — la remise étant possible — car le désobéissant contredit le commandement de Dieu, lors même qu’il s’accorde à Sa volonté.</p>
<h4>2. Le surgissement des choses par le décret de Dieu Très-Haut</h4>
<p>L’auteur dit : « et leur surgissement procède de Son décret » — le surgissement des choses, c’est-à-dire leur procéder et leur survenue, procède de Son décret, Sa prédestination, Son jugement et Sa volonté. Toute chose [advient] par le décret de Dieu et Sa prédestination : c’est-à-dire par Sa mesure — en une forme plutôt qu’une autre, un temps plutôt qu’un autre, une époque plutôt qu’une autre, un lieu plutôt qu’un autre.</p>
<h4>3. Le rapport de la science à la prédestination</h4>
<p>L’auteur dit : « Il a su toute chose avant son être — et elle s’accomplit selon Sa mesure. » Au nombre de ce qu’il faut croire : que Dieu, glorifié soit-Il, a su toute chose des possibles avant son être — c’est-à-dire sa survenue — et qu’elle s’accomplit et advient selon Sa mesure : selon Sa science. Sa science précède les choses sues : ce qu’Il sut devoir être, Il le voulut ; et ce qui n’est point tel, non.</p>
<h4>4. L’obligation de l’agrément du décret et de la prédestination</h4>
<p>Il faut croire au décret et à la prédestination, et l’agrément des deux est obligatoire de même — selon le hadith de Jibrīl : le Prophète — paix et bénédiction sur lui — dit : « et que tu crois à la prédestination, son bien et son mal ». [<em>Ṣaḥīḥ</em> de Muslim, Livre de la Foi, chapitre de la question de Jibrīl au Prophète — paix et bénédiction sur lui. Le texte reçu porte « et tu crois » (<em>wa-tuʾmin</em>) : le <em>wāw</em> initial est une variante mineure de citation, notée.]</p>
<p>Le décret et la prédestination, en tant qu’ils sont le décret de Dieu et Sa prédestination, exigent l’agrément absolument, de tout responsible. Et si le décret de Dieu Très-Haut et Sa prédestination désignent, chez la plupart, le lien exécutoire (<em>al-taʿalluq al-tanjīzī</em>) de Sa volonté et de Sa puissance au possible, l’agrément des deux signifie : délaisser la contestation et l’objection, et croire à l’établissement de la sagesse et de la justice.</p>
<h2>Les fruits de la leçon</h2>
<p>Purifier l’âme et l’épanouir par la soumission à Celui qui la créa, en tout ce qu’Il décréta pour elle et prédestina sur elle — bien ou mal ; et remettre les affaires à Dieu, glorifié soit-Il, en confiance en ce qui est auprès de Lui. Cela est la servitude même et la liberté parfaite : l’homme se libère du gouvernement de soi, et remet ses affaires à Celui en la main de qui sont les mesures des choses et de qui procède leur surgissement — ce qu’Il veut est, et ce qu’Il ne veut point n’est pas. Il est Celui qui dit, glorifié soit-Il :</p>
<p>« Et vous ne voulez, que si veut Dieu, le Seigneur des mondes. » (al-Takwīr, 29)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>Je fais connaître le décret et la prédestination, en la langue et en le terme.</li>
<li>J’analyse la parole de l’auteur : « les mesures des choses sont en Sa main, et leur surgissement procède de Son décret ».</li>
<li>J’expose le rapport de la prédestination à la science.</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Jābir — que Dieu l’agrée — rapporte que l’Envoyé de Dieu — paix et bénédiction sur lui — dit : « Point ne croit le serviteur qu’il ne croie à la prédestination, son bien et son mal, et qu’il ne sache que ce qui l’a atteint ne pouvait le manquer, et que ce qui l’a manqué ne pouvait l’atteindre. » [<em>Sunan</em> d’at-Tirmidhī — chapitre de ce qui est venu sur la foi à la prédestination, son bien et son mal ; vérifié : Tirmidhī 2144, voie de Jābir b. ʿAbdallāh — texte verbatim, le <em>wāw</em> imprimé devant « et qu’il sache » en est une variante mineure de citation ; Abū ʿĪsā le juge <em>gharīb</em>, connu seulement par la voie de ʿAbdallāh b. Maymūn — noté. Le hadith est imprimé deux fois — duplication OCR rendue une fois.]</p>
<h3>Je contemple le texte et réalise ce qui suit :</h3>
<ul>
<li>J’expose, à la lumière du hadith, la relation de la prédestination à la foi : est-elle constitutive ou complémentaire ?</li>
</ul>
<h2>La préparation préalable (<em>iʿdād</em>)</h2>
<p>[Titre imprimé « الاستثمار » par coquille — le contenu est celui de la préparation préalable ; titre restitué, noté.] Je lis le <em>matn</em> de la leçon suivante et recherche les sens des concepts suivants :</p>
<ul>
<li>la guidance (<em>hidāya</em>) — l’égarement (<em>ḍalāl</em>) — la réussite (<em>tawfīq</em>) — l’abandon (<em>khidhlān</em>).</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16721":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16721 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16721 restaurée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
