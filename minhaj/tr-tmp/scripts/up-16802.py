#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16802 (tawhid-1es, leçon imprimée 26 —
l'obligation d'obéir au détenteur de l'autorité et de délaisser la dispute
en religion).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire) ;
traduction savante avec restaurations du corpus canonique (cache quran = Ḥafṣ).

Vérifications et restaurations :
- 2 citations vides (perte OCR systématique CMS) :
  Nisāʾ 59 CONFORME (أطيعوا الله وأطيعوا الرسول وأولي الأمر منكم — l'ancre
  du commandement ; la double lecture ulémas/gouverneurs) ; Ḥashr 10 CONFORME
  (ربنا اغفر لنا ولإخواننا الذين سبقونا بالإيمان — l'ancre du pardon pour
  les prédécesseurs).
- 5 hadiths VÉRIFIÉS sunnah.com :
  Abū Hurayra « من أطاعني فقد أطاع الله » = Bukhārī 7137, Kitāb al-Aḥkām,
  bāb nommé d'après le verset même (أطيعوا الله وأطيعوا الرسول وأولي الأمر)
  — CONFORME MOT À MOT (hadith SANS réf imprimée — identification notée) ;
  Ibn ʿUmar « على المرء المسلم السمع والطاعة » = Muslim 1839, bāb وجوب
  طاعة الأمراء في غير معصية EXACT — CONFORME (variantes أو كره/وكره،
  إن لم يؤمر/إلا أن يؤمر notées) ;
  ʿĀʾisha « من أحدث في أمرنا » = Bukhārī 2697, Kitāb al-Ṣulḥ, bāb إذا
  اصطلحوا على صلح جور فالصلح مردود EXACT — la leçon imprimée ما ليس منه
  suit Muslim 1718 (Bukhārī : ما ليس فيه — variante notée) ;
  Jābir « من يهده الله فلا مضل له » = Muslim 867, Kitāb al-Jumʿa, bāb
  تخفيف الصلاة والخطبة EXACT — CONFORME (formule complète de la khuṭba ;
  « كاب » imprimé = coquille OCR pour كتاب, corrigée) ;
  Ibn ʿUmar « من أتى إليكم معروفا فكافئوه » = al-Bayhaqī (réf imprimée
  conservée, Kitāb al-Zakāt).
- Le matn se clôt par l'eulogie finale de la Risāla — leçon-boucle du livre.
- Ibn Ghāzī : les cinq catégories légales de la bidʿa en vers (table
  bilingue) — kuntu tābiʿan wa-wāfiqn...
- Doctrines rendues au plus près : la double lecture d'ulī l-amr ; l'obéissance
  en ce qui n'est pas désobéissance (et ce qui n'y mène pas) ; la Risāla
  citée en son propre texte (« dans le suivi des vertueux prédécesseurs est
  le salut ») ; le pardon aux prédécesseurs (la dette de la umma) ; le
  mirāʾ = nier le vrai manifeste après son apparition ; la réserve de Mālik ;
  la distinction dispute blâmable/dispute défensive ; le fiqh de « ce qui
  n'en est pas » (conformité aux visées et règles ; ce sans quoi l'obligation
  ne s'achève pas est obligatoire).
- OCR/artefacts : dl/dt/dd vides + <p> vides + écho du titre en queue + divs
  vides — artefacts non rendus ; paragraphe « فطاعتهم طاعة لله » scindé par
  l'extraction (« وتُحفظ / الأعراض ») — rejoint ; « كاب » → corrigé.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : l’obligation d’obéir au détenteur de l’autorité et de délaisser la dispute en religion</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la vingt-sixième leçon (26).</p>
<ul>
<li>Connaître le statut de l’obéissance à l’imam.</li>
<li>Saisir les dangers de la dispute (<em>mirāʾ</em>) en religion.</li>
<li>Avoir présent à l’esprit l’obligation de s’éloigner des innovations.</li>
<li>Incarné les finalités de l’obéissance au détenteur de l’autorité et de l’abandon de la dispute.</li>
</ul>
<h2>Préambule</h2>
<p>La vie des musulmans ne tient droite que par l’existence d’un guide qui prenne soin de leurs affaires, d’un détenteur de l’autorité qui préserve leur groupe, protège leur religion et leur monde d’ici-bas, et veille sur leur sécurité et leur salut, en leur religion et en leur monde.</p>
<p>Qu’entend-on par détenteur de l’autorité ? Quel est le statut de son obéissance en islam ? Quelles en sont les conditions ? Et quelle est la preuve de l’obligation d’obéir au prince dans le Coran ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et l’obéissance aux imams des musulmans, parmi les détenteurs de leurs affaires et leurs savants ; et le suivi des vertueux prédécesseurs, la poursuite de leurs traces et la demande de pardon pour eux ; et l’abandon de la dispute et de la controverse en religion, et l’abandon de tout ce qu’ont innové les innovateurs. Que Dieu prie sur notre maître Muḥammad, Son Prophète, ainsi que sur sa famille, ses épouses et sa descendance, et qu’Il le salue d’une salutation abondante. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>aʾimmat al-muslimīn</em> (les imams des musulmans) : pluriel d’<em>imām</em> — les imams des musulmans sont ceux qui se chargent de leurs affaires.</li>
<li><em>wulāt</em> (détenteurs) : pluriel de <em>wālī</em> — celui qui prend en charge les affaires d’autrui.</li>
<li><em>iqtifāʾ</em> (poursuite des traces) : le suivi.</li>
<li><em>mirāʾ</em> (dispute) : la controverse et le contentieux.</li>
<li><em>aḥdatha</em> (a innové) : a forgé, inventé.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> le statut de l’obéissance aux imams des musulmans.</li>
<li>Je dégage du <em>matn</em> le statut de la dispute en religion.</li>
</ul>
<h2>L’analyse (<em>taḥlīl</em>)</h2>
<p>La leçon embrasse les axes suivants :</p>
<h3>Premièrement : le statut de l’obéissance aux détenteurs des affaires des musulmans</h3>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et l’obéissance aux imams des musulmans, parmi les détenteurs de leurs affaires et leurs savants. » L’obéissance aux imams des musulmans et aux détenteurs de leurs affaires est obligatoire — en creed et en acte : par l’exécution de leurs ordres et l’arrêt devant leurs interdits. L’auteur a explicité les imams par sa parole : « parmi les détenteurs de leurs affaires et leurs savants » — c’est-à-dire leurs gouverneurs et leurs savants : il a ainsi réuni les deux exégèses d’« ulī l-amr » en la parole de Dieu Très-Haut :</p>
<p>« Ô les croyants ! Obéissez à Dieu, et obéissez au Messager et à ceux d’entre vous qui détiennent le commandement. Puis, si vous vous disputez en quoi que ce soit, renvoyez-le à Dieu et au Messager, si vous croyez en Dieu et au Jour dernier : cela est meilleur pour vous, et de plus belle interprétation. » (al-Nisāʾ, 59)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — le verset du commandement, fondement de l’obéissance.] Le sens de sa parole — que Dieu lui fasse miséricorde : au nombre des obligations des religions est l’obéissance aux détenteurs du commandement en ce qui n’est pas désobéissance et ne mène pas à une désobéissance — car par les détenteurs du commandement s’établissent les règles, se réforment les états, et se conservent les honneurs et les biens : leur obéir, c’est obéir à Dieu et à Son Messager ﷺ. D’après Abū Salama b. ʿAbd al-Raḥmān, il entendit Abū Hurayra — que Dieu l’agrée — dire : le Messager de Dieu ﷺ a dit : « Quiconque m’obéit a obéi à Dieu ; quiconque me désobéit a désobéi à Dieu ; quiconque obéit à mon émir m’a obéi ; et quiconque désobéit à mon émir m’a désobéi. » [Ṣaḥīḥ d’al-Bukhārī, Kitāb al-Aḥkām, bāb de la parole de Dieu Très-Haut : « Obéissez à Dieu, obéissez au Messager et à ceux d’entre vous qui détiennent le commandement » — hadith sans référence imprimée : identifié comme Bukhārī 7137, d’Abū Hurayra — texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com.] Et d’après Ibn ʿUmar — que Dieu les agrée tous deux — : le Prophète ﷺ a dit : « Il est au musulman d’écouter et d’obéir en ce qu’il aime comme en ce qu’il déteste, tant qu’il ne lui est pas commandé une désobéissance ; s’il lui est commandé une désobéissance : ni écoute, ni obéissance. » [Ṣaḥīḥ Muslim, bāb de l’obligation d’obéir aux émirs en ce qui n’est pas désobéissance — bāb imprimé EXACT (hadith 1839, d’Ibn ʿUmar) : texte VÉRIFIÉ sur sunnah.com ; « en ce qu’il aime ou déteste » et « tant qu’il ne lui est pas commandé » suivent la leçon de l’imprimé (variantes mineures notées).]</p>
<h3>Deuxièmement : le suivi des vertueux prédécesseurs et la demande de pardon pour eux</h3>
<h4>1. Le suivi des vertueux prédécesseurs</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et le suivi des vertueux prédécesseurs, la poursuite de leurs traces ». Suivre la voie des vertueux prédécesseurs — les Compagnons et les Suivants — et s’accorder à eux en leur science et en leur œuvre relève des obligations légales : qu’ils l’aient reçue du Prophète ﷺ, ou qu’elle remonte à leur dérivation (<em>istinbāṭ</em>) et à leur effort d’interprétation. Il est donc obligatoire de les suivre en ce qu’ils interprétèrent et dérivèrent de leur effort : aussi Mālik — que Dieu l’agrée — œuvrait selon ce sur quoi les gens de Médine s’étaient accordés d’œuvrer, et selon ce sur quoi s’était fixé la parole de la plupart d’entre eux en les points de divergence. L’auteur — que Dieu lui fasse miséricorde — dit à la fin de la <em>Risāla</em> : « Dans le suivi des vertueux prédécesseurs est le salut : eux sont le modèle en l’interprétation de ce qu’ils interprétèrent et l’extraction de ce qu’ils dérivèrent ; et s’ils divergent en les ramifications (<em>furūʿ</em>) et les cas nouveaux (<em>ḥawādith</em>), nul ne sort de leur groupe. »</p>
<h4>2. La demande de pardon pour les vertueux prédécesseurs</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et la demande de pardon pour eux ». Des obligations de la religion : demander le pardon pour les vertueux prédécesseurs, pour le droit qu’ils ont sur ceux qui vinrent après eux, en ce qu’ils portèrent de l’affaire de la Loi : ils établivrent ses fondements, obtinrent ses ramifications, rassemblèrent ses textes, et conseillèrent la Communauté par ce qu’ils firent. Il n’est personne, dans la Communauté, qui n’ait envers eux une dette — en sa religion et en son monde d’ici-bas — au prorata de ce qui lui parvint d’eux : il est donc obligatoire de les récompenser de ce qu’ils avancèrent, par la demande de pardon pour eux — selon la parole de Dieu Très-Haut :</p>
<p>« … et ceux qui sont venus après eux en disant : „Seigneur, pardonne-nous, ainsi qu’à nos frères qui nous ont précédés dans la foi ; et ne mets dans nos cœurs aucune rancœur envers ceux qui croient. Seigneur, Tu es, certes, compatissant et miséricordieux“. » (al-Ḥashr, 10)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — le pardon pour les prédécesseurs dans la foi.] Et d’après Ibn ʿUmar — que Dieu les agrée tous deux — : le Prophète ﷺ a dit : « … Et quiconque vous fait un bien : récompensez-le ; si vous ne trouvez pas de quoi le récompenser, alors faites son éloge, jusqu’à ce que vous sachiez que vous l’avez récompensé. » [Al-Bayhaqī, <em>al-Sunan</em>, Kitāb al-Zakāt, bāb : le don de qui demande par Dieu, puissant et majestueux — référence imprimée conservée.] Et cela ne se limite pas aux Compagnons : il embrasse quiconque nous a précédés dans la foi et nous a fait un bien.</p>
<h3>Troisièmement : l’abandon de la dispute, de la controverse et des innovations</h3>
<h4>1. L’abandon de la dispute et de la controverse en religion</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et l’abandon de la dispute et de la controverse en religion ». Ce que visent la dispute (<em>mirāʾ</em>) et la controverse (<em>jidāl</em>) : la négation du vrai après sa manifestation, et sa répulsion par le faux et la controverse. L’abandon de la dispute et de la controverse en religion est une obligation légale : elles mènent à loger le doute dans le cœur, et font paraître la supériorité sur les gens, la rivalité ostentatoire, l’orgueil, la vanité, l’envie, la rancune, la compétition et l’auto-certification — et les autres corruptions de cette sorte. Mālik — que Dieu l’agrée — dit : « Cette controverse n’est rien de la religion. » Que si ce que l’on vise par la controverse est la réfutation d’un faux ou la manifestation d’un vrai — sans obstination, ni négation, ni visée de l’emporter sur l’adversaire —, cela est permis, voire recommandé.</p>
<h4>2. L’abandon de ce qu’ont innové les gens de l’innovation</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et l’abandon de tout ce qu’ont innové les innovateurs ». L’abandon de ce qu’ont innové les innovateurs est obligatoire par le Livre et la Sunna : il est obligatoire de se cramponner au Livre et à la Sunna et de prendre modèle sur les vertueux prédécesseurs. D’après la Mère des croyants ʿĀʾisha — que Dieu l’agrée — : le Messager de Dieu ﷺ a dit : « Quiconque innove en notre affaire ce qui n’en est pas : il est rejeté. » [Ṣaḥīḥ d’al-Bukhārī, Kitāb al-Ṣulḥ, bāb : s’ils conviennent d’un accord inique, l’accord est rejeté — bāb imprimé EXACT (hadith 2697, de ʿĀʾisha) : texte VÉRIFIÉ sur sunnah.com ; « ce qui n’en est pas » (<em>mā laysa minhu</em>) suit la leçon de Muslim 1718 — Bukhārī porte « ce qui n’y est pas » (<em>mā laysa fīhi</em>) — variante canonique notée.]</p>
<p>Le sens de « ce qui n’en est pas » : ce qui ne fut pas conforme à ses visées (<em>maqāṣid</em>) et à ses règles. Quant à ce qui fut conforme, il en est — car l’innovation ne s’énonce que du nouveau ; et rien n’est dit « de l’affaire de la religion », en premier lieu, qu’au prorata des règles et des visées : car ce sans quoi l’obligatoire ne s’achève pas est lui-même obligatoire ; et sur cette analogie en le reste des règles. Que si le sens était « quiconque apporte ce dont le texte ne vient pas dans la Loi… », la description d’innovation ne serait pas valide. [Ellipse imprimée conservée.]</p>
<p>Et d’après Jābir — que Dieu l’agrée — : le Messager de Dieu ﷺ haranguait les gens : il louait Dieu et Le célébrait de ce dont Il est digne, puis disait : « Quiconque Dieu guide, nul ne l’égare ; et quiconque Il égare, nul ne le guide. Le meilleur des propos est le Livre de Dieu ; la meilleure guidance est la guidance de Muḥammad ; les pires des affaires sont leurs nouveautés ; et toute innovation est égarement. » [Ṣaḥīḥ Muslim, Kitāb al-Jumʿa, bāb de l’allègement de la prière et du prône — bāb imprimé EXACT (hadith 867, de Jābir) : texte VÉRIFIÉ sur sunnah.com ; « Livre du vendredi » imprimé avec coquille (<em>kāb</em> pour <em>kitāb</em>) — corrigée.]</p>
<p>Puis l’auteur — que Dieu Très-Haut lui fasse miséricorde — clôt ce chapitre comme il clôt le livre, disant : « Que Dieu prie sur notre maître Muḥammad, Son Prophète, ainsi que sur sa famille, ses épouses et sa descendance, et qu’Il le salue d’une salutation abondante. »</p>
<h2>Les fruits de la leçon</h2>
<p>Éduquer le musulman à se tenir à ce sur quoi étaient les vertueux prédécesseurs, de la guidance de l’islam en sa figure lumineuse — faite de miséricorde, d’amour et de fraternité ; et à s’éloigner de la dispute et de la controverse en religion, pour ce qui en naît d’effets négatifs sur l’unité des musulmans, leur affection mutuelle, leur amour et leur fraternité — et de la dépense d’énergies intellectuelles en ce qui ne rapporte au musulman nul profit, ni en ce monde ni en l’autre.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<p>Que doivent les musulmans à leurs détenteurs de l’autorité ? En appuyant du Livre, de la Sunna et de la raison.</p>
<p>Qui sont les vertueux prédécesseurs ? Et pourquoi demandons-nous pardon pour eux ? En appuyant.</p>
<p>L’imam Ibn Ghāzī — que Dieu lui fasse miséricorde — dit ce qui suit :</p>
<table>
<tbody>
<tr><td>Sois un suiveur — accorde-toi à qui suit :</td><td>les innovations se partagent en cinq :</td></tr>
<tr><td>obligatoire — tel écrire la science,</td><td>et les points du <em>muṣḥaf</em>, pour la compréhension ;</td></tr>
<tr><td>recommandée — telle la latrine,</td><td>le pont, le <em>miḥrāb</em> et les écoles ;</td></tr>
<tr><td>puis indifférente — tel le tamis,</td><td>et répréhensible — telle la table des mets ;</td></tr>
<tr><td>puis interdite — telle la lotion aux miettes,</td><td>et les vêtues-dénudées, inclinées.</td></tr>
</tbody>
</table>
<p>Je médite les vers et en extrais le contenu.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16802":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16802 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print(f"OK 16802 -> {len(HTML_FR)} car FR injectés")


if __name__ == "__main__":
    main()
