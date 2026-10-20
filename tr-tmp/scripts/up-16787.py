#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16787 (tawhid-1es, leçon imprimée 21 — la
notion de foi, īmān, et ses degrés).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire) ;
traduction savante avec restaurations du corpus canonique (cache quran = Ḥafṣ).

Vérifications et restaurations (cache quran = Ḥafṣ) :
- 7 citations vides (perte OCR systématique CMS) :
  Anfāl 2-3-4 CONFORME (l'ouverture du préambule — le triple cœur/prières/
  degrés, miroir du matn) ; Baqara 142→143 écart +1 (cible univoque par la
  glose imprimée « أي صلاتكم » : le verset de la qibla se clôt sur « وما كان
  الله ليضيع إيمانكم » — l'exégèse d'Ibn ʿAbbās identifie la foi à la prière) ;
  Fatḥ 4 CONFORME (ليزدادوا إيمانا مع إيمانهم) ; Muddaththir 31 CONFORME
  (وليزداد الذين آمنوا إيمانا) ; Tawba 124 CONFORME (فزادتهم إيمانا) ;
  Bayyina 5 CONFORME (مخلصين له الدين) ; Ḥashr 7 CONFORME (ما آتاكم الرسول
  فخذوه).
- Hadiths VÉRIFIÉS sunnah.com (curl + UA navigateur) : ʿIrbaḍ b. Sāriya
  « أوصيكم بتقوى الله والسمع والطاعة » = Abū Dāwūd 4607, Kitāb al-Sunna,
  bāb في لزوم السنة EXACT — texte VÉRIFIÉ CONFORME mot à mot ; le hadith de
  l'intention « إنما الأعمال بالنيات » (sans réf imprimée) rendu avec la
  note d'identification (Bukhārī 1 ; Muslim 1907).
- OCR/artefacts : paragraphe scindé en deux par l'extraction (« وقيل الكمال
  في كلامه / على ظاهره ») — rejoint ; « بينهم ا » pour بينهما — rejoint ;
  dl/dt/dd vides + <p> vides + echo du titre en queue + divs vides —
  artefacts non rendus.
- Doctrines rendues au plus près : la définition tripartite (parole/
  sincérité/œuvre) ; les quatre bénéfices du matn ; la discussion sur la
  parole (condition/moitié/nié — la moitié est la juste) ; les œuvres parties
  de la foi achevée, non de la foi absolue ; les trois positions sur
  croissance et décroissance (avec le pas du matn sur les fruits de la foi et
  la réserve rapportée de Mālik) ; l'intention âme de l'œuvre (Zarrūq,
  Sharḥ ʿalā l-Risāla 1/61) ; la Sunna mesure de tout (ʿIrbaḍ) ; la
  distinction īmān/islām d'al-Lawh (al-Rāʾid, p. 60, adapté).
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la notion de foi (<em>īmān</em>) et ses degrés</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la vingt-et-unième leçon (21).</p>
<ul>
<li>Connaître la réalité de la foi.</li>
<li>Connaître que la foi croît et décroît.</li>
<li>Saisir l’effet de l’œuvre en l’achèvement de la foi.</li>
</ul>
<h2>Préambule</h2>
<p>Dieu Très-Haut dit :</p>
<p>« Les croyants sont seulement ceux dont les cœurs s’épouvant quand Dieu est mentionné ; et quand Ses signes leur sont récités, cela les accroît en foi — et en leur Seigneur ils s’en remettent. Ceux qui font la prière, et de ce que Nous leur avons attribué dépensent. Ceux-là sont les croyants, en vérité : ils ont des degrés auprès de leur Seigneur, un pardon et une subsistance généreuse. » (al-Anfāl, 2-4)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — le triple cœurs/prières/dépense/degrés : miroir exact du <em>matn</em>.]</p>
<p>Je médite les versets nobles, et m’interroge : qu’est-ce que la foi ? Et par quoi croît-elle, et décroît-elle ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que la foi est parole de la langue, sincérité du cœur et œuvre des membres ; elle croît par l’accroissement des œuvres et décroît par leur décroissance — en elles est la décroissance, et par elles l’accroissement ; et la parole de la foi ne s’achève que par l’œuvre ; ni parole ni œuvre que par l’intention ; ni parole, œuvre et intention que par la conformité à la Sunna. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>īmān</em> (foi) : la crédence.</li>
<li><em>ikhlāṣ</em> (sincérité) : la limpidité — et, en l’obéissance, l’abandon du faire-voir.</li>
<li><em>jawāriḥ</em> (membres) : pluriel de <em>jāriḥa</em> — les membres de l’homme.</li>
<li><em>niyya</em> (intention) : la visée et la résolution.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> la réalité de la foi.</li>
<li>J’extrais du <em>matn</em> par quoi la foi croît et décroît.</li>
</ul>
<h2>L’analyse (<em>taḥlīl</em>)</h2>
<h3>Premièrement : la réalité de la foi</h3>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que la foi est parole de la langue, sincérité du cœur et œuvre des membres. » Ce que l’auteur a mentionné en sa parole au début du chapitre — « de cela relèvent la foi du cœur et l’articulation de la langue » — est ce même qui est visé ici : la foi est proclamation du monothéisme par l’articulation des deux témoignages ; soumission, sincérité et véracité du cœur dans le creed que la langue articule ; et œuvre conformément au creed. La parole — les deux témoignages — traduit ce qu’il y a dans le cœur de crédence et de soumission, exprimé ici par la sincérité (<em>ikhlāṣ</em>) : la direction, en lui, est vouée à Dieu seul et à Son Messager ; et l’œuvre est condition d’achèvement en la foi. On a divergé sur la parole : est-elle condition — nulle foi pour quiconque ne l’apporte pas, en toute absolue — ? ou moitié — auquel cas elle est requise tant qu’il n’y a ni empêchement, comme la mort qui surprend après la résolution de la proférer, ni excuse, comme la contrainte à l’abandonner alors que la foi est établie en son cœur — ? Et telle est la position juste. Ou n’est-elle ni l’une ni l’autre : le seul creed suffit, tant que l’empêchement n’est ni orgueil ni rébellion — et sa mécréance, alors, ne fait pas question. Quant à la seule articulation, elle ne suffit pas — à l’unanimité des gens de la Sunna.</p>
<p>L’auteur dit : « et œuvre des membres ». L’œuvre des membres est requise en la foi à titre d’achèvement, selon les gens de la Sunna : les œuvres des membres sont une partie de la foi achevée, non une partie de la foi absolue. Et ce que l’auteur — que Dieu lui fasse miséricorde — a mentionné, que la foi est appliquée aux œuvres des membres, la parole de Dieu Très-Haut l’atteste :</p>
<p>« … Dieu n’est point tel qu’Il laisse périr votre foi. » (al-Baqara, 143)</p>
<p>« votre foi », c’est-à-dire : votre prière. [Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Référence imprimée : [Baqara 142] — écart +1 : le verset de la qibla, qui se clôt sur « votre foi », est 2:143 en Ḥafṣ ; cible univoque par la glose imprimée « c’est-à-dire votre prière » — l’exégèse d’Ibn ʿAbbās identifiant la foi à la prière vers la première qibla.]</p>
<h3>Deuxièmement : la croissance de la foi et sa décroissance</h3>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « elle croît par l’accroissement des œuvres et décroît par leur décroissance — en elles est la décroissance, et par elles l’accroissement ». C’est le premier des quatre bénéfices pour lesquels l’auteur a dit : « Et que la foi est parole de la langue, sincérité du cœur et œuvre des membres » : l’avertissement sur une question où les imams ont divergé — la croissance de la foi et sa décroissance. L’auteur pose que la foi croît et décroît — la position qu’il préfère parmi les trois de la question. Quant à ceux qui soutiennent que la foi ne croît ni ne décroît, ils s’y sont tenus en ce que la foi remonte à un sens simple, cardiaque : s’il survient, c’est la foi ; s’il ne survient pas, la foi ne survient pas ; et dès qu’elle admettrait la croissance, elle serait doute et mécréance.</p>
<p>Quant à ceux qui soutiennent qu’elle croît et décroît, les uns ont dit : la croissance et la décroissance remontent aux fruits de la foi, non à la crédence même — et c’est là-dessus que l’auteur — que Dieu lui fasse miséricorde — a procédé, en plaçant la décroissance en l’œuvre, et par elle la croissance : car l’œuvre même reçoit, en sa substance, la décroissance. Quant à ceux qui soutiennent qu’elle croît et ne décroît pas, ils se sont tenus à l’extension légale : Dieu Très-Haut n’a révélé que la croissance de la foi, non sa décroissance. Dieu Très-Haut dit :</p>
<p>« C’est Lui qui a fait descendre la quiétude dans les cœurs des croyants, pour qu’ils ajoutent foi à leur foi… » (al-Fatḥ, 4)</p>
<p>et Il dit :</p>
<p>« … et pour que croisse la foi de ceux qui croient… » (al-Muddaththir, 31)</p>
<p>et Il dit :</p>
<p>« … Quant à ceux qui ont cru, elle les a accrus en foi — et ils s’en réjouissent. » (al-Tawba, 124)</p>
<p>[Trois citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées CONFORMES — les trois versets de la croissance, miroirs exacts du propos.] Et l’hésitation sur la décroissance de la foi est rapportée de Mālik.</p>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et la parole de la foi ne s’achève que par l’œuvre » : allusion au second des quatre bénéfices — la parole de la foi, l’articulation des deux témoignages, ne s’achève que par l’œuvre des membres. Ce que dit l’auteur se fonde sur la position que l’œuvre entre dans la substance de la foi ; et il fut dit : l’achèvement, en sa parole, est sur son sens apparent — fondé sur la position que l’œuvre n’entre pas dans la substance de la foi, ce qu’il a dit au début du chapitre. Selon cela : s’il œuvre, sa foi est achevée, qui le sauve du Feu ; s’il n’œuvre pas, sa foi est valide, mais sa foi n’est pas achevée. C’est un surcroît d’accentuation et d’explication de ce qui se comprend de ce qui précède : l’œuvre de bien est l’achèvement de la foi, et la racine de la foi tient sans l’œuvre — mais foi diminuée. [Paragraphe imprimé scindé en deux par l’extraction — rejoint.]</p>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « ni parole ni œuvre que par l’intention » : le troisième des quatre bénéfices pour lesquels il a répété que la foi est parole de la langue, jusqu’à la fin de sa parole. Son sens : ni parole ni œuvre, de ce qui requiert l’intention, ne s’achève ni ne valide que par l’intention — sincérité envers Dieu Très-Haut, et exclusion de tout autre que Lui en la servitude — selon la parole du Prophète ﷺ : « Les œuvres ne sont que par les intentions. » [Le hadith de l’intention — l’ouverture des deux <em>Ṣaḥīḥ</em>s (Bukhārī 1 ; Muslim 1907) — sans référence imprimée, noté.] L’intention est l’âme de l’œuvre, et la sincérité l’âme de l’intention. Dieu Très-Haut dit :</p>
<p>« … ils n’ont reçu d’ordre sinon d’adorer Dieu, Lui vouant un culte pur… » (al-Bayyina, 5)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — le verset du culte pur, ancre de la sincérité.] L’intention est l’élixir des œuvres : elle transmue leurs substances en bien, et les accroît en salaire. [<em>Sharḥ Zarrūq ʿalā l-Risāla</em>, 1/61 — réf imprimée conservée.]</p>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « ni parole, œuvre et intention que par la conformité à la Sunna » : le quatrième — ni parole (l’articulation des deux témoignages), ni œuvre (obéissance et culte), ni intention (visée et sincérité) ne s’achève ni ne valide, sinon par la conformité à la Sunna prophétique : le suivre ﷺ en ce qu’il a apporté, et suivre les anciens vertueux. Dieu Très-Haut dit :</p>
<p>« … Ce que le Messager vous apporte : prenez-le ; et ce qu’il vous interdit : abstenez-vous… » (al-Ḥashr, 7)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — le verset de l’obéissance au Messager.] Et il dit — paix et bénédiction sur lui : « Je vous recommande la crainte de Dieu, l’écoute et l’obéissance — dût-on [vous commander] un esclave abyssin : quiconque, d’entre vous, vivra après moi verra beaucoup de divergences. Tenez-vous-en donc à ma Sunna et à la Sunna des califes bien dirigés, guidés : mordez-y à pleines dents ; et prenez garde aux innovations : toute innovation est hérésie, et toute hérésie est égarement. » [Sunan d’Abū Dāwūd, bāb de l’obligation de s’en tenir à la Sunna — bāb imprimé EXACT (hadith 4607, d’al-ʿIrbaḍ b. Sāriya) : texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com.]</p>
<h2>Les fruits de la leçon</h2>
<p>L’explication de l’effet du creed du cœur dans l’orientation des œuvres : c’est lui qui meut les membres — en sa sincérité, sa véracité et sa droiture, leur sincérité, leur véracité et leur droiture ; en sa corruption, leur corruption. Et le cœur ne se redresse que par le monothéisme de Dieu Très-Haut et l’aveu de Sa seigneurie et de Sa divinité sur les mondes. Par là, les membres se déploient, proclamant ce monothéisme — témoignage de la langue, œuvre des membres : et l’arbre de la foi, planté dans le cœur, porte ses fruits en le commerce et la conduite.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>Je définis la foi : au sens propre, et selon la terminologie de la Loi.</li>
<li>J’explicite les positions des savants sur la croissance de la foi et sa décroissance.</li>
<li>Je mentionne les preuves de la croissance de la foi.</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Le maître al-ʿArabī al-Lawh — que Dieu lui fasse miséricorde — dit : « La foi et l’islam diffèrent de concept selon la langue : la foi est la crédence absolue — la soumission à l’arrêt de l’informateur ; l’islam est la reddition et le ralliement absolus : ils sont donc, quant au concept linguistique, distincts — absolument. De même ils diffèrent selon la Loi : la foi est la crédence en Dieu Très-Haut en ce dont Il a informé — Ses ordres et Ses interdits ; l’islam est le ralliement et la soumission à la divinité, qui ne se réalise que par l’acceptation de l’ordre et de l’interdit. En la Loi donc : la foi — la crédence en Dieu Très-Haut en ce dont Il a informé, des ordres et des interdits ; l’islam — le ralliement et la soumission à ces ordres et interdits : deux concepts légaux distincts — absolument. » [<em>Al-Rāʾid fī ʿilm al-ʿaqāʾid</em>, p. 60 — adapté (<em>bi-taṣarruf</em>).]</p>
<h3>Je médite bien le texte et réponds à ce qui suit :</h3>
<ul>
<li>Quelle est la différence entre la foi et l’islam ?</li>
<li>En quoi consiste leur corrélation ? [« entre eux » imprimé « entre eux a » — rejoint.]</li>
</ul>
<h2>La préparation préalable (<em>iʿdād qablī</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et recherche le devenir des désobéissants des croyants qui commettent les abominations et les répréhensibles.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16787":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16787 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    # contrôle apostrophes typographiques : aucune droite dans le corps
    n_droites = HTML_FR.count("'")
    print(f"OK — leçon 16787 main: FR {len(HTML_FR)} car ; apostrophes droites: {n_droites} (attendu 0)")


if __name__ == "__main__":
    main()
