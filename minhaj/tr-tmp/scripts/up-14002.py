#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 14002 (tawhid-1es, leçon 4 — ce que le
cœur doit croire et la langue professer : l'ouverture du credo de la Risāla).

Vérifications et restitutions (corpus canonique pour les versets ; sunnah.com
pour les hadiths — vérifié ce tour) :
- Matn : « باب ما تنطق به الألسنة وتعتقده الأفئدة من واجب أمور الديانات... »
  — l'ouverture du credo de la Risāla, rendue fidèlement (awwaliyya/
  ākhiriyya = primauté/postériorité ; « mithl/nidd » rendus « pareil/pair »).
- TROIS CITATIONS VIDES (perte OCR) après « la preuve de Son unicité en Son
  essence, Ses attributs et Ses actes » → RESTITUÉES selon le triple objet
  annoncé par la phrase : l'essence (Āl ʿImrān 18 : « Dieu atteste... »),
  les attributs (al-Shūrā 11 : « il n'est rien qui Lui soit semblable »),
  les actes (al-Aʿrāf 54 : « Certes, votre Seigneur est Dieu, qui créa les
  cieux et la terre... ») — note éditoriale le documentant.
- Shūrā 11, Ikhlāṣ 4, Ikhlāṣ 3-4, Nisāʾ 170, Jinn 3, Ḥadīd 3 : emplacements
  imprimés VIDES (réfs imprimées seules) → RESTAURÉES du corpus canonique,
  noté pour chaque bloc.
- Hadith des 99 noms [Bukhārī, Kitāb al-Daʿawāt, bāb li-llāh miʾat ism
  ghayr wāḥid] — réf CONFORME ; l'imprimé porte « lā yaḥfaẓuhā aḥadun illā
  dakhala l-janna » + « huwa witrun yuḥibb al-witr » : le texte reçu du
  Ṣaḥīḥ (7392) lit « man aḥṣāhā » ; la teneur « witrun yuḥibb al-witr »
  attestée chez Muslim 2677 — variante de récit notée.
- Hadith « اللهم أنت الأول... » : l'imprimé écrit « روى البخاري عن عمران
  بن حصين » mais renvoie à [صحيح مسلم كتاب الذكر... باب ما يقول عند النوم
  وأخذ المضجع] — DISCRÉPANCE IMPRIMÉE notée ; la formule est attestée
  VERBATIM en Ṣaḥīḥ Muslim 2713 a (voie d'Abū Ṣāliḥ d'après Abū Hurayra),
  vérifié ce tour sur sunnah.com.
- « الحدوث والفناء » : la survenance et l'anéantissement Lui sont
  impossibles (muḥāl).
- La leçon imprimée n'a NI taqwīm NI istithmār NI iʿdād : structure rendue
  telle quelle (clôture synthétique « يُستفاد من الدرس »).
- FIX GT-ismes : « Dieu est un dieu » (périphrase vide) → « Dieu est un dieu
  unique » ; « pair et similaire » → « semblable et pair (nidd) ».
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : ce que le cœur doit croire et la langue professer</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la quatrième leçon (4).</p>
<ul>
<li>Connaître le sens de la foi.</li>
<li>Faire présent, puis réaliser, le fruit de la foi en ma vie.</li>
</ul>
<h2>Préambule</h2>
<p>Avant la mission du Prophète — paix et bénédiction sur lui —, les hommes s’étaient détournés de la religion de leur père Abraham — sur lui la paix : ils adoraient les idoles, les étoiles, la lumière et les ténèbres, et d’autres créatures. C’est pourquoi Dieu envoya le Sceau des prophètes, notre maître Muḥammad — paix et bénédiction sur lui —, pour redresser les croyances corrompues et ramener les hommes à la religion du Tawḥīd et au credo correct : la religion de leur père Abraham — sur lui la paix.</p>
<p>Quel est donc le fondement de l’appel du Prophète — paix et bénédiction sur lui ? Et que doit croire le musulman ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Chapitre de ce que prononcent les langues et croient les cœurs (<em>afʾida</em>), des matières obligées de la religion. Au nombre de cela : la foi par le cœur, et la profession par la langue — que Dieu est un dieu unique : il n’est pas d’autre dieu que Lui, ni de semblable à Lui, ni d’égal à Lui ; qu’Il n’a ni enfant, ni père, ni épouse, ni associé ; qu’à Sa primauté (<em>awwaliyya</em>) il n’est pas de commencement, ni à Sa postériorité (<em>ākhiriyya</em>) d’achèvement. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<p><em>ilāh</em> (dieu) : adoré — de <em>alaha</em> (avec l’ouverture du hamza, du lām et du hāʾ) au sens de <em>ʿubida</em>, “ il fut adoré ” : il est donc <em>ilāh</em> au sens de <em>maʾlūh</em>, c’est-à-dire adoré.</p>
<p><em>afʾida</em> (les cœurs) : pluriel de <em>fuʾād</em>, qui est le cœur.</p>
<p><em>naẓīr</em> (égal) : semblable et pair (<em>nidd</em>).</p>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> le siège de la foi, et par quoi elle est connue.</li>
<li>J’extrais du <em>matn</em> ce que vise la foi en Dieu.</li>
<li>Que signifient : « ni semblable à Lui, ni égal à Lui » ?</li>
</ul>
<h2>L’analyse</h2>
<p>La leçon contient les axes suivants :</p>
<h3>Premièrement : la croyance en l’unicité de Dieu Très-Haut</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Au nombre de cela : la foi par le cœur, et la profession par la langue — que Dieu est un dieu unique. » Au nombre de ce qu’il faut croire : la foi par le cœur, et la profession par la langue, que Dieu est un dieu unique. La preuve de Son unicité — Puissant et Élevé — en Son essence, Ses attributs et Ses actes est le noble Coran, comme Sa parole, l’Élevé :</p>
<p>« Dieu atteste qu’il n’est de dieu que Lui — et les anges et les doués de science, debout en équité — ; il n’est de dieu que Lui, le Puissant, le Sage. » (Āl ʿImrān, 18)</p>
<p>Et Sa parole :</p>
<p>« ...Le Créateur (<em>Fāṭir</em>) des cieux et de la terre... il n’est rien qui Lui soit semblable ; et Il est l’Audiant, le Voyant. » (al-Shūrā, 11 — extrait)</p>
<p>Et Sa parole :</p>
<p>« Certes, votre Seigneur est Dieu, qui créa les cieux et la terre en six jours, puis s’établit sur le Trône ; Il couvre la nuit du jour, qui la poursuit avec hâte... À Lui la création et le commandement. Béni soit Dieu, Seigneur des mondes ! » (al-Aʿrāf, 54 — extrait)</p>
<p>[Trois citations coraniques perdues à l’OCR — restituées d’après le triple objet qu’annonce la phrase : l’essence (Āl ʿImrān 18), les attributs (al-Shūrā 11), les actes (al-Aʿrāf 54) ; les emplacements imprimés sont vides.]</p>
<p>Et la Sunna prophétique, comme sa parole — paix et bénédiction sur lui : « À Dieu, Puissant et Majestueux, appartiennent quatre-vingt-dix-neuf noms — cent moins un : nul ne les conserve sans entrer au Paradis ; et Il est l’Impair (<em>witr</em>), qui aime l’impair. » [Ṣaḥīḥ d’al-Bukhārī, Livre des invocations, chapitre : à Dieu cent noms moins un — réf CONFORME ; l’imprimé lit « lā yaḥfaẓuhā aḥadun illā dakhala l-janna » (nul ne les conserve...), variante de récit — le texte reçu du Ṣaḥīḥ lit « man aḥṣāhā », “ quiconque les dénombre ”, et la teneur “ Impair qui aime l’impair ” est attestée chez Muslim (2677)].</p>
<p>La parole de l’auteur — que Dieu lui fasse miséricorde — : « il n’est pas d’autre dieu que Lui » est un affermissement (<em>taʾkīd</em>) : il n’est pas de différence entre elle et sa parole « un dieu unique » ; et il fut dit : celle-ci est plus éloquente, parce qu’elle fait sentir la négation d’un dieu autre que Lui, du fait de la présence conjointe de la négation et de l’affirmation : la négation de la divinité d’un autre que Lui, après Son affirmation pour Lui, est plus éloquente à affirmer pour Lui, Puissant et Élevé, l’unicité.</p>
<h3>Deuxièmement : Sa transcendance — Puissant et Élevé — de toutes les imperfections</h3>
<h4>1. Sa transcendance du semblable et de l’égal</h4>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « ni de semblable à Lui, ni d’égal à Lui. » Au nombre de ce qu’il faut croire : Dieu n’a ni pareil, ni semblable en Son essence, ni égal en Ses attributs. Dieu, l’Élevé, dit :</p>
<p>« ...Il n’est rien qui Lui soit semblable ; et Il est l’Audiant, le Voyant. » (al-Shūrā, 11)</p>
<p>Et l’Élevé dit :</p>
<p>« Et nul n’est égal à Lui. » (al-Ikhlāṣ, 4)</p>
<p>[Citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées seules.] C’est-à-dire que Son essence, l’Élevé, ne ressemble pas aux essences, et ne se conforme à aucune des déterminations que saisissent les perceptions : tout ce que se représentent les pensées, et où s’arrêtent les regards, est trop saint pour ressembler à l’Un, le Dominateur.</p>
<h4>2. Sa transcendance — Puissant et Élevé — de l’enfant, du père et de l’épouse</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « qu’Il n’a ni enfant, ni père, ni épouse. » Au nombre de ce qu’il faut croire : Dieu, Puissant et Élevé, est transcendant de toutes les imperfections — Lui, le Grand en Sa hauteur, qui dit :</p>
<p>« Il n’a jamais engendré, n’a pas été engendré non plus, et nul n’est égal à Lui. » (al-Ikhlāṣ, 3-4)</p>
<p>Et Sa parole, Puissant et Élevé :</p>
<p>« Ô hommes ! Le Messager vous est venu avec la vérité de la part de votre Seigneur : croyez donc, il vaut mieux pour vous ; et si vous mécroyez — certes, à Dieu appartient ce qui est dans les cieux et la terre... » (al-Nisāʾ, 170 — extrait)</p>
<p>Et Puissant et Élevé :</p>
<p>« ...Et exaltée soit la majesté de notre Seigneur : Il n’a pris ni épouse ni enfant. » (al-Jinn, 3)</p>
<p>[Citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées seules.] L’épouse (<em>ṣāḥiba</em>) est la femme : Dieu est transcendant de tout cela, car cela répugne au rang de la divinité, lequel exige la perfection en propre et la richesse absolue — Lui, Puissant et Élevé, riche de tout autre que Lui, tandis que tout ce qui n’est pas Lui a besoin de Lui.</p>
<h3>Troisièmement : Il est le Premier sans commencement, et le Dernier sans terme — Puissant et Élevé</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « qu’à Sa primauté il n’est pas de commencement, ni à Sa postériorité d’achèvement. » Le sens de la parole de l’auteur : Dieu, Puissant et Élevé, n’a pas une existence commencée, telle qu’Il aurait un premier ; ni achevée, telle qu’Il aurait un dernier — selon Sa parole :</p>
<p>« Il est le Premier et le Dernier, l’Apparent et le Caché ; et Il est, de toute chose, savant. » (al-Ḥadīd, 3)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée seule.] — c’est-à-dire le Précédent des choses sans commencement, leur Survivant après elles sans fin : Il est le Premier avant toute chose, sans début ; et le Dernier après toute chose, sans fin. Al-Bukhārī — selon l’imprimé — rapporte de ʿImrān b. Ḥuṣayn que le Prophète — paix et bénédiction sur lui — dit : « Ô Dieu, Tu es le Premier : rien n’est avant Toi ; et Tu es le Dernier : rien n’est après Toi. » [Ṣaḥīḥ de Muslim, Livre du rappel, de l’invocation, du repentir et de la demande de pardon, chapitre : ce qu’on dit au sommeil et à la prise du lit — l’imprimé écrit « al-Bukhārī rapporta », alors que le renvoi est au Ṣaḥīḥ de Muslim (n° 2713 a) : la formule est attestée verbatim chez Muslim, par la voie d’Abū Ṣāliḥ d’après Abū Hurayra — la divergence d’attribution est notée telle qu’imprimée.] Et la survenance (<em>ḥudūth</em>) et l’anéantissement (<em>fanāʾ</em>) Lui sont impossibles.</p>
<p>Il se déduit de la leçon que la fin de l’existence de l’homme est l’unicité de Dieu Très-Haut et la réserve de l’adoration à Lui seul — droit qui Lui est dû, l’Élevé, sur toutes les créatures —, et la croyance qu’Il est l’Un, l’Unique, le Singulier, le Maître absolu (<em>al-Ṣamad</em>), le Puissant sur toute chose ; et l’orientation du dessein vers Lui, le recours et l’extrême besoin vers Lui, en l’acquit des besoins : car Il est le Vivant, le Subsistant, à qui appartiennent les trésors des cieux et de la terre. Par là, l’homme s’affranchit de toute entrave et de tout carcan qui s’interposent entre lui et son Maître et Créateur.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "14002":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 14002 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 14002 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
