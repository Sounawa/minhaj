#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16738 (tawhid-1es, leçon imprimée 16 — le
Paradis, ses habitants et ses délices).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire) ;
traduction savante avec restaurations du corpus canonique (cache quran = Ḥafṣ).

Vérifications et restaurations (cache quran = Ḥafṣ) :
- 9 emplacements de citation vides/tronqués (perte OCR systématique CMS) :
  2 citations SANS référence (Paradis/Feu existent à présent) — cibles
  univoques par le verbe أُعِدَّتْ (parfait passif : déjà advenue), sur quoi
  enchaîne exactement le commentaire « ولا يكون معدا إلا ما كان حاصلا ثابتا » :
  Āl ʿImrān 133 (janna uʿiddat lil-muttaqīn) + Āl ʿImrān 131 (nār uʿiddat
  lil-kāfirīn) — paire canonique restituée ;
  Najm 15-14 (paire écrite en ordre descendant) → restituée 53:14-15 CONFORME
  (sidrat al-muntahā + jannat al-maʾwā — l'argument du rang supérieur) ;
  Baqara 34 → 35 écart +1 (MÊME règle que Baqara 29→30 de cette même page :
  le verset du vicariat imprimé 29 = 2:30 Ḥafṣ ; cible : « اسكن أنت وزوجك
  الجنة » — la demeure d'Adam au Jardin, l'article défini désignant le Jardin
  céleste ; le v34 imprimé (prosternation des anges, gens des cieux) ouvre la
  péricope et soutient le même argument — noté) ;
  Fāṭir 35 CONFORME (dār al-muqāma « la Demeure de la permanence » — miroir
  exact du propos « demeure d'éternité ») ;
  Qiyāma « الآيتان 22-21 » (paire en ordre inverse, décalage) → restituée
  75:22-23 — le miroir ḍād/ẓāʾ (nāḍira/nāẓira) ;
  2 citations de MOTS vides (nāḍira au ḍād / nāẓira au ẓāʾ) — cibles
  univoques, le commentaire glosant chacune par sa lettre ;
  Ṭā-Hā 112 → 115 écart +3 — règle Ṭā-Hā de ce livre confirmée une TROISIÈME
  fois (107→110 leçon six ; 109→112 leçon quinze) ; cible univoque : « ولقد
  عهدنا إلى آدم من قبل فنسي » — l'alliance antérieure et l'oubli d'Adam,
  repris mot à mot dans le propos (« oublieux de ce que Dieu lui avait
  recommandé ») ;
  Baqara 29 → 30 écart +1 (le verset du vicariat إني جاعل في الأرض خليفة =
  2:30 Ḥafṣ — cible univoque) ;
  Aʿrāf 22 — citation tronquée (référence amputée du numéro) : cible
  univoque, le recouvrement par les feuilles du Paradis repris mot à mot.
- Hadiths VÉRIFIÉS sunnah.com (curl + UA navigateur, Cloudflare contourné) :
  Bukhārī « إني رأيت الجنة أو أريت الجنة فتناولت منها عنقودا » — le bāb
  imprimé (Adhān 91, lever des yeux vers l'imam) existe à l'identique et
  abrite le taʿlīq de ʿĀʾisha sur la retraite en la prière de l'éclipse ; le
  texte cité = narration d'Ibn ʿAbbās, Bukhārī 5197 (Nikāḥ) CONFORME mot à
  mot (« ou il m'a été montré » + « de lui ») ; parallèle 1052 (Kusūf) sans
  les deux additions — divergence de localisation notée ;
  Muslim Ṣuhaib « تريدون شيئا أزيدكم... فيكشف الحجاب » = Muslim 181a, bāb
  ithbāt ruʾyat al-muʾminīn EXACT — texte VÉRIFIÉ CONFORME mot à mot.
- Doublons/artefacts OCR : titre « من فوائد الدرس » fondu dans le paragraphe
  précédent (question rhétorique) → h2 restitué ; objectifs avec &nbsp;
  parasites non rendus ; dl/dt/dd vides + <p> vides + echo du titre en queue
  + divs vides — artefacts non rendus ; réf « جسوس » de l'imprimé rendue
  telle quelle (graphie probablement altérée) ; المومنين non concerné ici.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : le Paradis, ses habitants et ses délices</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la seizième leçon (16).</p>
<ul>
<li>Connaître les délices du Paradis, et qui sont ses habitants.</li>
<li>Mettre devant les yeux l’éternité des croyants en la Demeure des délices.</li>
<li>Réaliser la servitude envers Dieu Très-Haut, pour être gratifié de Sa vision — exalté soit-Il — au Paradis.</li>
</ul>
<h2>Préambule</h2>
<p>Tu as su que Dieu — exalté soit-Il — fait sortir du Feu qui Il veut, parmi les croyants désobéissants, en raison de leur foi et de l’intercession des intercesseurs agréés en leur faveur — fût leur foi comme un grain de moutarde —, et les fait entrer en Son Paradis, par Sa grâce, Sa générosité et Sa miséricorde.</p>
<p>Qu’est-ce donc que le Paradis ? Pour qui Dieu Très-Haut l’a-t-Il préparé ? Et quel est le plus grand honneur dont Dieu y honore Ses serviteurs ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>Ibn Abī Zayd — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que Dieu — exalté soit-Il — a créé le Paradis, l’a préparé comme demeure d’éternité pour Ses alliés, et les y a honorés de la contemplation de Sa Noble Visage ; et c’est celui d’où fut descendu Adam, Son prophète et Son vicaire, vers Sa terre, conformément à ce qui a précédé en Sa science antérieure. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>aʿadda</em> (a préparé) : a disposé et facilité.</li>
<li><em>khuld</em> (éternité) : permanence et stabilité.</li>
<li><em>ahbaṭa</em> (fit descendre) : fit descendre.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> ceux pour qui le Paradis a été préparé.</li>
<li>Je dégage du <em>matn</em> qui sera gratifié, au Jour de la Résurrection, de la contemplation de la Noble Visage de Dieu.</li>
</ul>
<h2>L’analyse (<em>taḥlīl</em>)</h2>
<h3>Premièrement : la foi en l’existence du Paradis et en sa préparation pour les croyants</h3>
<h4>1. La création — exalté soit-Il — du Paradis</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que Dieu — exalté soit-Il — a créé le Paradis. » Il est de la croyance obligatoire que Dieu — exalté et magnifié soit-Il — a créé le Paradis et l’a préparé comme demeure d’éternité, de stabilité permanente et sans fin, pour Ses alliés — qui sont les croyants en Lui, parmi les hommes et les djinns.</p>
<p>Le sens de la parole de l’auteur — « a créé le Paradis » — est que le Paradis et le Feu sont créés et existent à présent, selon la parole de Dieu Très-Haut :</p>
<p>« Et hâtez-vous vers un pardon de votre Seigneur et un Paradis vaste comme les cieux et la terre, préparé pour les gens de piété. » (Āl ʿImrān, 133)</p>
<p>et Sa parole :</p>
<p>« Et craignez le Feu qui a été préparé pour les mécréants. » (Āl ʿImrān, 131)</p>
<p>[Deux citations imprimées sans référence — emplacements vides, perte OCR ; cibles univoques par le verbe « a été préparé » (<em>uʿiddat</em> — parfait passif : déjà advenue), sur quoi enchaîne exactement le commentaire qui suit ; la paire canonique Paradis/Feu — gens de piété/mécréants — restituée.]</p>
<p>Rien n’est « préparé » sinon ce qui est déjà existant et ferme : s’en tenir au sens apparent des textes est donc obligatoire — telle est la doctrine des gens de la Sunna. Et la plupart des savants tiennent que le Paradis est au-dessus des sept cieux et sous le Trône, selon la parole de Dieu Très-Haut :</p>
<p>« Auprès de la <em>sidra</em> de la limite (<em>sidrat al-muntahā</em>) ; auprès d’elle, le Jardin du refuge (<em>jannat al-maʾwā</em>). » (al-Najm, 14-15)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée écrit la paire en ordre descendant « 15-14 » — restituée 14-15 (Ḥafṣ) ; la <em>sidra</em> est au terme supérieur, par-delà les sept cieux — d’où l’argument du rang.]</p>
<p>et Sa parole :</p>
<p>« Ô Adam, demeure, toi et ton épouse, au Paradis ; et mangez de lui, en abondance, où vous voudrez tous deux ; mais ne vous approchez pas de cet arbre : vous seriez alors du nombre des injustes. » (al-Baqara, 35)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Référence imprimée : [Baqara 34] — écart +1, la même règle que Baqara 29→30 de cette même page (le verset du vicariat imprimé 29 = 2:30 Ḥafṣ) ; cible : la demeure d’Adam au Jardin — l’article défini désigne le Jardin céleste, pendant du verset de la <em>sidra</em> ; le verset 34 imprimé — la prosternation des anges, gens des cieux — ouvre la péricope et soutient le même argument, noté.]</p>
<p>Et le Prophète ﷺ dit : « J’ai vu le Paradis — ou : il m’a été montré le Paradis — et j’en ai tendu une grappe. » [Ṣaḥīḥ al-Bukhārī, Kitāb al-Adhān, bāb du lever des yeux vers l’imam en la prière — réf imprimée : le bāb existe à l’identique (ch. 91 du Kitāb al-Adhān) et abrite le <em>taʿlīq</em> de ʿĀʾisha sur la retraite du Prophète ﷺ en la prière de l’éclipse (« je vis la Géhenne se briser elle-même, quand vous me vîtes reculer ») ; le texte cité est la narration d’Ibn ʿAbbās de cette même prière — Bukhārī 5197 (Kitāb al-Nikāḥ) : texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com (« ou il m’a été montré » + « de lui ») ; la version parallèle Bukhārī 1052 (Kitāb al-Kusūf) lit « je vis le Paradis, et j’ai tendu une grappe », sans ces deux additions — divergences de localisation et de leçon notées.]</p>
<h4>2. La préparation du Paradis comme demeure d’éternité pour les croyants</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « l’a préparé comme demeure d’éternité pour Ses alliés. » Il est de la croyance obligatoire que Dieu Très-Haut a préparé le Paradis, l’a disposé et facilité, comme demeure d’éternité, de séjour et de permanence perpétuelle sans fin, pour Ses alliés croyants. Dieu Très-Haut dit :</p>
<p>« … qui, de Sa grâce, nous a fait demeurer en la Demeure de la permanence : nul labeur ne nous y touche, et nulle fatigue ne nous y touche. » (Fāṭir, 35)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME — « la Demeure de la permanence » (<em>dār al-muqāma</em>) : miroir exact du propos « demeure d’éternité ».]</p>
<p>La parole de l’auteur — que Dieu lui fasse miséricorde — « pour Ses alliés » : les alliés (<em>awliyāʾ</em>) sont le pluriel de <em>walī</em> ; et <em>walī</em> se prête à être un <em>fiʿīl</em> au sens de <em>fāʿil</em> — son sens serait alors : celui dont l’obéissance s’est enchaînée, sans défaillir — comme il se prête au sens de <em>mafʿūl</em> : celui dont Dieu prend en charge la sauvegarde et la protection, et à qui Il fait durer la réussite vers Son obéissance.</p>
<h3>Deuxièmement : la foi en la contemplation de la Noble Visage de Dieu Très-Haut</h3>
<h4>1. La doctrine des gens de la Sunna sur le statut de la contemplation de la Noble Visage de Dieu Très-Haut</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et les y a honorés de la contemplation de Sa Noble Visage ». Le plus grand honneur dont Dieu honore les croyants au Paradis est la contemplation de Sa Visage — exalté soit-Il ; la promesse en est venue pour l’au-delà en la parole de Dieu Très-Haut :</p>
<p>« Des visages, ce jour-là, resplendissants (<em>nāḍira</em>) ; vers leur Seigneur, regardants (<em>nāẓira</em>). » (al-Qiyāma, 22-23)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Référence imprimée : « les deux versets 22-21 » — la paire écrite en ordre inverse (comme Najm « 15-14 »), en décalage d’une unité ; la cible univoque est le miroir ḍād/ẓāʾ : <em>nāḍira</em> (75:22) / <em>nāẓira</em> (75:23) en Ḥafṣ — restituée.]</p>
<p>Sa parole <em>nāḍira</em> — au <em>ḍād</em> — relève de la fraîcheur radieuse (<em>naḍāra</em>), qui est la beauté et la grâce ; et Sa parole <em>nāẓira</em> — au <em>ẓāʾ</em> — relève du regard (<em>naẓar</em>), qui est la vision par les clairvoyances intérieures et les yeux. [Les deux citations de mots imprimées vides — restituées : cibles univoques, le commentaire glosant chacune par sa lettre.] Dieu — exalté soit-Il — lève alors le voile sur les regards des croyants, comme se découvre la lune en la nuit du plein lune — ainsi qu’il est venu dans le hadith authentique rapporté par plus de vingt des plus éminents des Compagnons.</p>
<p>Les savants ont dit : le plus excellent de ce qui est donné au serviteur en ce bas-monde est l’évocation ; et, dans l’au-delà, la contemplation de la Noble Visage de Dieu. D’après Ṣuhaib — que Dieu l’agrée —, le Messager de Dieu ﷺ dit : « Quand les gens du Paradis entrent au Paradis — rapporte-t-il —, Dieu, béni et exalté soit-Il, dit : “ Désirez-vous quelque chose que J’ajoute ? ” Ils disent : “ N’as-Tu pas blanchi nos visages ? Ne nous as-Tu pas fait entrer au Paradis, et sauvés du Feu ? ” — rapporte-t-il — : alors Il lève le voile ; et rien de ce qui leur a été donné ne leur est plus cher que la contemplation de leur Seigneur — puissant et majestueux. » [Ṣaḥīḥ Muslim, Kitāb al-Īmān, bāb de l’établissement de la vision des croyants de leur Seigneur en l’au-delà — hadith de Ṣuhaib (n° 181) : bāb imprimé EXACT, texte VÉRIFIÉ CONFORME mot à mot sur sunnah.com.]</p>
<h4>2. Le Paradis promis</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « et c’est celui d’où fut descendu Adam, Son prophète et Son vicaire, vers Sa terre ». L’auteur expose que le Paradis promis est celui d’où fut descendu Adam, le père des humains — sur lui la paix. Sa descente eut lieu un vendredi — le jour même où il fut créé, et le jour où il en fut fait sortir et descendu vers la terre.</p>
<p>La parole de l’auteur — que Dieu lui fasse miséricorde — « conformément à ce qui a précédé en Sa science antérieure » fait allusion à la cause de sa descente : il lui fut interdit de manger de l’arbre, et il en mangea, oublieux de ce que Dieu lui avait recommandé ; et son fait de manger de l’arbre qui lui était interdit n’advenait que par l’effet de Son jugement exécutoire et de Son décret antérieur. Dieu Très-Haut dit :</p>
<p>« Et certes, Nous avions fait alliance avec Adam auparavant ; mais il oublia, et Nous n’avons pas trouvé en lui de ferme résolution. » (Ṭā-Hā, 115)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Référence imprimée : [Ṭā-Hā 112] — écart +3 : la règle Ṭā-Hā de ce livre confirmée une troisième fois (107→110 en la leçon six ; 109→112 en la leçon quinze) ; cible univoque : l’alliance antérieure et l’oubli d’Adam — le propos l’explicite mot à mot (« oublieux de ce que Dieu lui avait recommandé »).]</p>
<p>La parole de l’auteur — que Dieu lui fasse miséricorde — « Son prophète et Son vicaire » expose le privilège d’Adam et la majesté de son rang, afin que rien ne soit soupçonné de déficient dans son acte de manger et dans sa descente : il — sur lui la paix — est en effet préservé de la désobéissance qui entraîne la faute ; et son vicariat est fermement établi par la parole de Dieu Très-Haut :</p>
<p>« Et quand ton Seigneur dit aux anges : “ Je vais établir sur terre un vicaire. ” Ils dirent : “ Y établiras-Tu celui qui y corrompra et y versera le sang, quand nous sommes là à Te sanctifier et à Te glorifier ? ” Il dit : “ Je sais ce que vous ne savez pas. ” » (al-Baqara, 30)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR. Référence imprimée : [Baqara 29] — écart +1 : le verset du vicariat (<em>khilāfa</em>) est 2:30 en Ḥafṣ ; cible univoque.]</p>
<p>Comment donc L’installerait-Il sur terre comme Son vicaire, et le ferait-Il lieu de déficience et de désobéissance ?</p>
<h2>Les fruits de la leçon</h2>
<p>[Titre de section fondu dans le paragraphe précédent par l’extraction — restitué.]</p>
<p>Ce que dit Ibn ʿAṭāʾillāh al-Iskandarī : « C’est uniquement pour rétribuer Ses serviteurs croyants que Dieu a fait de la Demeure dernière le lieu : ce bas-monde, en effet, ne contient pas ce qu’Il veut leur donner ; et leur rang est trop élevé pour qu’Il les rétribue en une demeure sans permanence. » [<em>Al-Ḥikam</em>, p. 119 — d’après la transmission de « <em>Jaṣṣūs</em> » en son commentaire du Tawḥīd de la <em>Risāla</em>, 2/640 — réf imprimée telle quelle (graphie de l’imprimé conservée).]</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>J’explicite pour qui Dieu a préparé le Paradis, avec appui.</li>
<li>Quelle est la plus grande faveur dont Dieu a gratifié Ses serviteurs au Paradis ?</li>
<li>Pourquoi Dieu a-t-Il fait sortir Adam du Paradis ?</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Ibn ʿAṭāʾillāh dit : « Parmi les fruits [de cette histoire] : Adam et Ève — sur eux la paix — étaient au Paradis, et [Dieu] Se leur faisait connaître par la subsistance, le don, la bienfaisance et les grâces. Le Vrai — exalté soit-Il — voulut alors, par le secret de Sa bienveillance en Son gouvernement, qu’ils mangent de l’arbre, pour Se leur faire connaître par la douceur (<em>ḥilm</em>), le voile (<em>satr</em>), le pardon, le repentir et l’élection. La douceur : Il ne les frappa pas aussitôt du châtiment quand ils eurent agi — le Doux ne te frappe pas sur-le-champ du châtiment pour ce que tu as fait : il t’accorde un délai, soit vers Son pardon et Sa grâce, soit vers Sa rigueur et Sa vengeance. Le voile : quand ils eurent mangé et que leurs nudités leur apparurent, par la disparition de leurs vêtements du Paradis, Il les couvrit de ses feuilles, comme Dieu Très-Haut dit : </p>
<p>… quand ils eurent goûté de l’arbre, leurs nudités leur apparurent, et ils entreprirent de se couvrir de feuilles du Paradis. » (al-Aʿrāf, 22)</p>
<p>[<em>Al-Tanwīr fī isqāṭ al-tadbīr</em> d’Ibn ʿAṭāʾillāh, § 26, adapté (<em>bi-taṣarruf</em>) — réf imprimée conservée. La citation coranique, tronquée dans l’imprimé (référence amputée du numéro de verset), est restituée : cible univoque — le recouvrement par les feuilles du Paradis, repris mot à mot dans le texte ; la suite de la citation imprimée (l’explicitation du pardon, du repentir et de l’élection) est coupée par l’extraction — noté.]</p>
<p>Je contemple le texte et en extrais ce qui suit :</p>
<ul>
<li>Les manifestations de la sollicitude de Dieu envers Son vicaire Adam — sur lui la paix.</li>
<li>La qualité du traitement de Dieu — exalté soit-Il — envers les gens de l’élection (<em>ahl al-khuṣūṣiyya</em>), d’entre Ses serviteurs rapprochés.</li>
</ul>
<h2>La préparation préalable (<em>iʿdād qablī</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et recherche les scènes du Jour de la Résurrection.</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16738":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16738 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    # contrôle apostrophes typographiques : aucune droite dans le corps
    n_droites = HTML_FR.count("'")
    print(f"OK — leçon 16738 main: FR {len(HTML_FR)} car ; apostrophes droites: {n_droites} (attendu 0)")


if __name__ == "__main__":
    main()
