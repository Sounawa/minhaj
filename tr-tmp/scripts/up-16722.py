#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16722 (tawhid-1es, leçon 10 — la guidance
et l'égarement, conformément à la prescience du Subtil, le Bien-Informé).

Vérifications et restitutions (cache quran = Ḥafṣ) :
- Matn : « لا يكون من عباده قول ولا عمل إلا وقد قضاه وسبق علمه به... يضل من
  يشاء فيخذله بعدله ويهدي من يشاء فيوفقه بفضله » — rendu fidèlement.
- CITATIONS VIDES (perte OCR) RESTAURÉES du cache, cibles doctrinales :
  * [الحديد: 4] → CONFORME (l'attribut d'essence : la science antérieure —
    « يعلم ما يلج في الأرض... ») ;
  * [التغابن: 4] → CONFORME (يعلم ما في السماوات والأرض) ;
  * [الشورى: 10] → Shūrā 12 « إنه بكل شيء عليم » — écart +2 noté (la série
    des quatre versets est épistémologique ; 42:10 « le jugement revient à
    Dieu » = lecture concurrente si l'on visait le qaḍāʾ) ;
  * [الطلاق: 12] → CONFORME (« وأن الله قد أحاط بكل شيء علما ») ;
  * [الملك: 14] → CONFORME (« ألا يعلم من خلق وهو اللطيف الخبير ») — le
    manuel l'appelle « la 15e āya de Mulk » : décalage de numérotation du
    manuel noté ;
  * [الأنعام: 40] → Anʿām 39 « من يشإ الله يضلله ومن يشأ يجعله على صراط
    مستقيم » — réf d'adjacence (−1) notée ;
  * [ابراهيم: 29] → Ibrāhīm 27 « يثبت الله الذين آمنوا بالقول الثابت...
    ويضل الله الظالمين » — écart +2 noté (la série hidāya/ḍalāl) ;
  * [فاطر: 8] → CONFORME (فإن الله يضل من يشاء ويهدي من يشاء) ;
  * [الكهف: 17] → CONFORME (fin du verset — من يهد الله فهو المهتدي) ;
  * [الزمر: 37] → CONFORME (ومن يهد الله فما له من مضل).
- Ibn ʿAṭāʾ Allāh al-Sakandarī, Ḥikam p. 163 (l'istithmār) — « إلهي إن
  ظهرت المحاسن مني فبفضلك... » VERBATIM rendu fidèlement, réf imprimée.
- Titre « التحليل » absent de l'extrait (le passage saute de l'extraction à
  « اشتمل الدرس على ما يأتي ») — restitué selon la série, noté.
- Les items d'évaluation imprimés en un seul paragraphe concaténé — rendus
  en liste.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la guidance et l’égarement, conformément à la prescience du Subtil, le Bien-Informé</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la dixième leçon (10).</p>
<ul>
<li>Connaître que ce qui procède des créatures procède de la science de Dieu et de Son décret.</li>
<li>Distinguer Son décret, l’Elevé, de Sa volonté (<em>mašīʾa</em>).</li>
<li>Saisir que la réussite (<em>tawfīq</em>) et l’abandon (<em>khidhlān</em>) procèdent de Dieu.</li>
</ul>
<h2>Préambule</h2>
<p>Il nous advint, en la leçon du décret et de la prédestination, que l’ensemble des mesures est en la main de Dieu Très-Haut ; que les actes des serviteurs procèdent du décret de Dieu, de Sa prédestination et de Sa science — sans qu’ils aient part à la création de leurs actes ; qu’Il sait les états de Ses serviteurs, et le détail de leurs paroles et de leurs actes : le poids d’un atome, aux cieux et en la terre, ne Lui échappe point — glorifié et magnifié soit-Il ; qu’Il guide qui Il veut et égare qui Il veut ; qu’Il fait réussir à Son obéissance qui Il veut, par Sa faveur ; et qu’Il abandonne qui Il veut, par Sa justice.</p>
<p>Quels sont les sens de la guidance et de la réussite ? Et qu’entend-on par l’égarement et l’abandon ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Il n’est point, de la part de Ses serviteurs, de parole ni d’acte qui n’ait été décrété par Lui et dont Sa science n’ait précédé — quoi, Celui qui créa ne saurait-Il point savoir, Lui le Subtil, le Bien-Informé ? Il égare qui Il veut — et l’abandonne par Sa justice ; et Il guide qui Il veut — et le fait réussir par Sa faveur. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li>le décret de Dieu : Sa volonté et Son jugement.</li>
<li>le Subtil (<em>al-Laṭīf</em>) : au nombre de Ses noms, l’Elevé ; il reçoit plusieurs sens, parmi lesquels le Longanime, le Sachant, le Bienfaiteur, le Bienfaisant.</li>
<li><em>khadhal</em> (abandonner) : égarer et délaisser son secours.</li>
<li><em>yahdī</em> (guider) : diriger, faire réussir, faire connaître.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> que les paroles des serviteurs et leurs œuvres procèdent de la science de Dieu et de Son décret.</li>
<li>J’extrais du <em>matn</em> que la guidance et l’égarement sont en la main de Dieu Très-Haut.</li>
</ul>
<h2>L’analyse</h2>
<p>[Titre restitué selon la série — absent de l’extrait, noté.] La leçon contient ce qui suit :</p>
<h3>Premièrement : les paroles des serviteurs et leurs œuvres procèdent du décret de Dieu et de Sa science</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Il n’est point, de la part de Ses serviteurs, de parole ni d’acte qui n’ait été décrété par Lui et dont Sa science n’ait précédé. » Au nombre de ce qu’il faut croire : que Dieu Très-Haut a su toute chose avant sa survenue, et qu’elle s’accomplit selon Sa science — telle est la parole de l’auteur en la leçon précédente : « Il a su toute chose avant son être — et elle s’accomplit selon Sa mesure » : c’est là le vrai qu’il faut croire. Et comme Il sait, glorifié soit-Il, toute chose avant sa survenue, et qu’elle s’accomplit selon Sa science, l’Elevé sait les choses en leur généralité et en leur détail, l’universel et le particulier : il n’est point, de la part de Ses serviteurs, de parole ni d’acte qui n’ait été décrété par Lui et dont Sa science n’ait précédé — comme dit l’auteur. Le sens en est que toute œuvre et toute parole procédant de Ses serviteurs, Sa volonté s’y est attachée : car le décret est la volonté de Dieu, attachée de toute éternité à tout ce qui sera.</p>
<p>La parole de l’auteur — que Dieu lui fasse miséricorde — : « et dont Sa science n’ait précédé » a le même sens que sa parole : « Il a su toute chose avant son être » : il la répéta en renforcement, et en indication d’un attribut parmi ceux qu’il faut croire au sujet de Dieu Très-Haut — l’attribut de science, attribut pré-éternel subsistant en l’essence du Nécessaire étant, par lequel toute chose suie se dévoile telle qu’elle est. Le Très-Haut dit :</p>
<p>« C’est Lui qui créa les cieux et la terre en six jours, puis s’établit sur le Trône : Il sait ce qui entre en la terre et ce qui en sort, ce qui descend du ciel et ce qui y monte — et Il est avec vous, où que vous soyez ; et Dieu, de ce que vous faites, est voyant. » (al-Ḥadīd, 4 — extrait)</p>
<p>Et le Puissant et Magnifié dit :</p>
<p>« Il sait ce qui est aux cieux et en la terre, et sait ce que vous cachez et ce que vous manifestez — et Dieu, du fond des poitrines, est sachant. » (al-Taghābun, 4)</p>
<p>Et le glorifié dit :</p>
<p>« À Lui les clefs des cieux et de la terre : Il étend la subsistance à qui Il veut et la mesure — certes, de toute chose Il est sachant. » (al-Shūrā, 12)</p>
<p>Et le glorifié dit :</p>
<p>« Dieu qui créa sept cieux et de la terre autant : l’Ordre descend entre eux, afin que vous sachiez que Dieu, sur toute chose, est puissant — et que Dieu, de toute chose, embrasse la science. » (al-Ṭalāq, 12 — extrait)</p>
<p>[Quatre citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les trois premières et dernières références imprimées CONFORMES ; la référence imprimée de la troisième porte « 10 », la visée est le verset 12 — écart +2 noté : la série des quatre est épistémologique (la science embrassante) ; 42:10 « le jugement de quoi vous divergez revient à Dieu » resterait la lecture concurrente si l’on visait le décret.]</p>
<h3>Deuxièmement : le Subtil, au nombre de Ses noms, l’Elevé</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « quoi, Celui qui créa ne saurait-Il point savoir, Lui le Subtil, le Bien-Informé ? » L’auteur appuya l’embrassement de Sa science, l’Elevé, sur toute chose, par cette quinzienne āya de Sūrat al-Mulk, advenue dans le contexte de l’āya qui la précède — la parole de Dieu Très-Haut :</p>
<p>« Quoi, Celui qui créa ne saurait-Il point savoir, Lui le Subtil, le Bien-Informé ? » (al-Mulk, 14)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME (le manuel numérote « la quinzaine āya » : décalage de numérotation du manuel noté).] Le secret est une créature ; et la créature ne procède point sans que le Créateur la sache. Et Il est le Subtil, le Bien-Informé : le Subtil est au nombre de Ses noms les plus beaux — le Sachant des réalités subtiles des choses, de leurs profondeurs et de leurs difficultés.</p>
<h3>Troisièmement : l’égarement et la guidance sont en Sa main, glorifié soit-Il</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Il égare qui Il veut — et l’abandonne par Sa justice ; et Il guide qui Il veut — et le fait réussir par Sa faveur. » Ce discours relève du sens de ce qui précède : toute chose procède de Dieu Très-Haut. Il est pareil à Sa parole, Puissant et Magnifié :</p>
<p>« Ceux qui crièrent au mensonge Nos signes : sourds et muets, aux ténèbres — qui Dieu veut, Il l’égare ; et qui Il veut, Il le met sur un chemin droit. » (al-Anʿām, 39)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte « 40 », la visée est le verset 39 — réf d’adjacence notée.] Un pareil discours advint déjà en la parole de l’auteur : « Il guida celui à qui il donna la réussite par Sa faveur » ; et il n’y a point de divergence entre les musulmans et les prédécesseurs guidés de la communauté : Dieu, glorifié et magnifié soit-Il, égare qui Il veut et guide qui Il veut — nul n’est guidé que par Sa guidance, et nul n’est égaré que par Son égarement. Nombreux versets l’indiquent, parmi eux la parole du Très-Haut :</p>
<p>« Dieu affermit les croyants par la parole ferme, en la vie de ce monde et en la dernière ; et Dieu égare les injustes — et Dieu fait ce qu’Il veut. » (Ibrāhīm, 27)</p>
<p>et Sa parole, l’Elevé :</p>
<p>« Quoi ! Celui dont l’œuvre mauvaise fut embellie, au point qu’il la vit belle... certes, Dieu égare qui Il veut et guide qui Il veut. Ne te consumes donc point de regrets sur eux. » (al-Fāṭir, 8 — extrait)</p>
<p>et Sa parole :</p>
<p>« ...Cela est des signes de Dieu : qui Dieu guide, il est le guidé ; et qui Il égare, tu ne lui trouveras point de patron qui le dirige. » (al-Kahf, 17 — extrait)</p>
<p>et Sa parole :</p>
<p>« Et qui Dieu guide, nul ne l’égare. Dieu n’est-Il pas Puissant, détenteur de la vengeance ? » (al-Zumar, 37)</p>
<p>[Quatre citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la référence imprimée de la première porte « 29 », la visée est le verset 27 — écart +2 noté (la série hidāya/ḍalāl : l’affermissement et l’égarement) ; les trois autres CONFORMES.]</p>
<h2>Les fruits de la leçon</h2>
<p>Éduquer le croyant à la remise et à la soumission au décret de Dieu et à Sa prédestination, et à la vigilance envers son Maître, qui sait ses mouvements, ses repos et tous ses états ; et que le bien qui procède de l’homme est faveur de Dieu et réussite dont il Lui doit la gratitude. Ibn ʿAṭāʾ Allāh dit : « Mon Dieu, si les beautés paraissent de moi, c’est par Ta faveur — et à Toi la grâce sur moi ; et si les laideurs paraissent de moi, c’est par Ta justice — et à Toi l’argument contre moi. » [Les <em>Ḥikam</em> d’Ibn ʿAṭāʾ Allāh al-Sakandarī : p. 163 — citation verbatim, référence imprimée telle quelle.]</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>J’expose le sens de la parole de l’auteur : « Il n’est point, de la part de Ses serviteurs, de parole ni d’acte qui n’ait été décrété par Lui ».</li>
<li>Je cite des preuves que la science de Dieu Très-Haut embrasse toute chose, jusque les détails.</li>
<li>Je cite d’autres preuves coraniques que la guidance et l’égarement sont en la main de Dieu Très-Haut.</li>
</ul>
<h2>La préparation préalable (<em>iʿdād</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et en extrais les manifestations du décret de Dieu et de Sa prédestination en l’univers.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16722":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16722 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16722 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
