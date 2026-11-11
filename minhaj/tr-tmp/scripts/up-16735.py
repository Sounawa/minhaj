#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16735 (tawhid-1es, leçon 14 — la foi en la
survenue de l'Heure, la résurrection et la rétribution).

Pipeline : extraction scripts-translate/extract.py (src.html autoritaire) ;
traduction savante avec restaurations du corpus canonique (cache quran = Ḥafṣ).

Vérifications et restaurations (cache quran = Ḥafṣ) :
- 11 citations vides [سورة ... الآية N] (perte OCR systématique CMS) restaurées :
  Naḥl 77 (CONFORME — أمر الساعة كلمح البصر) ; Luqmān 33→34 (adjacence +1 —
  le verset des cinq inconnaissables, cible univoque) ; Aʿrāf 29 (citation vide
  sans réf — cible univoque : reprise littérale « كما بدأكم تعودون » du matn) ;
  Yā-Sīn 50 (réf imprimée conservée — non univoque, le v51 adjacent noté) ;
  Baqara 260→261 (adjacence +1 — parabole du grain sept épis × cent grains,
  miroir du sept centuple du hadith ; cible univoque) ; Zumar 10 (CONFORME) ;
  Anʿām 160 (CONFORME) ; Nisāʾ 31 (CONFORME) ; Najm 32 (CONFORME) ;
  Nisāʾ 115→116 (adjacence +1 — le verset exact du non-pardon de l'association,
  repris mot à mot dans le matn ; Nisāʾ 48 pendant parallèle noté) ;
  Zalzala 8 (CONFORME — assignment de recherche de l'iʿdād).
- Hadiths : miʿrāj « هي خمس وهن خمسون ما يبدل القول لديّ » — Bukhārī 349
  (bāb كيف فرضت الصلاة في الإسراء exact) : le texte reçu porte « لا يبدل » —
  variante de citation notée ; hadith qudsī d'Ibn ʿAbbās (كتب الحسنات والسيئات)
  — Bukhārī 6491 (bāb من هم بحسنة أو بسيئة exact) CONFORME.
- Doublons/artefacts OCR : « اشتمل الدرس على ما يأتي » imprimé 2× → rendu une
  fois ; phrases soudées « بها.ومعنى » séparées ; dl/dt/dd vides + <p> vides +
  echo du titre en queue + divs vides — artefacts non rendus ; relatif « الذي »
  singulier pour un pluriel (المرجئة) — coquille rendue correctement.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la foi en la survenue de l’Heure, la résurrection et la rétribution</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la quatorzième leçon (14).</p>
<ul>
<li>Connaître les réalités invisibles dont la foi est obligatoire.</li>
<li>Connaître les espèces de péchés, et par quoi elles sont pardonnées.</li>
<li>Réaliser dans ma vie les effets de la foi en ces réalités invisibles.</li>
<li>Éviter les péchés par le repentir et par la préservation d’y tomber.</li>
</ul>
<h2>Préambule</h2>
<p>Parmi ce qu’apporta le Messager de Dieu — paix et bénédiction sur lui — : qu’il incombe à tout responsable légal (<em>mukallaf</em>) de croire en Dieu, en Ses anges, en Ses Livres, en Ses messagers et au Dernier Jour.</p>
<p>Quelle est donc la signification de la foi au Dernier Jour ? Et quels sont les déroulements de ses états ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que l’Heure vient — nul doute à son sujet ; que Dieu ressuscite quiconque meurt : comme Il les a commencés, ils retourneront ; que Dieu — glorifié et magnifié soit-Il — a multiplié pour Ses serviteurs croyants les bonnes actions, leur a passé outre, par le repentir, les péchés majeurs, et leur a pardonné les péchés mineurs moyennant l’évitement des majeurs ; et qu’Il a fait de quiconque ne se repent pas des péchés majeurs un devenir tributaire de Sa volonté — Dieu ne pardonne pas qu’on Lui associe quoi que ce soit, et Il pardonne ce qui est en deçà à qui Il veut. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>yabʿathu</em> (ressuscite) : redonne la vie et rassemble pour le jugement.</li>
<li><em>ḍāʿafa</em> (a multiplié) : a rendu abondantes et a accrues.</li>
<li><em>ṣafaḥa</em> (a passé outre) : a fait grâce, a pardonné, a dépassé la faute.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> le statut de la foi en l’Heure.</li>
<li>Je dégage du <em>matn</em> les événements qui surviennent après la venue de l’Heure.</li>
<li>J’extrais du <em>matn</em> le péché que Dieu ne pardonne pas.</li>
</ul>
<h2>L’analyse (<em>taḥlīl</em>)</h2>
<p>La leçon comprend ce qui suit : [Phrase imprimée deux fois — rendue une fois.]</p>
<h3>Premièrement : la foi en la survenue de l’Heure, la résurrection et le rassemblement</h3>
<h4>1. La foi en l’Heure</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que l’Heure vient — nul doute à son sujet. » Il est de la croyance obligatoire que l’Heure — qui est la Résurrection (<em>al-qiyāma</em>) — vient, sans nul doute : elle désigne l’achèvement des jours du bas-monde et leur extinction ; on l’a nommée « Heure » (<em>al-sāʿa</em>) pour la proximité de son affaire. Dieu Très-Haut dit :</p>
<p>« C’est à Dieu qu’appartient l’inconnaissable des cieux et de la terre ; et l’affaire de l’Heure n’est que comme un clin d’œil — ou plus proche encore. Dieu, de toute chose, est capable. » (al-Naḥl, 77)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<p>Le Prophète — paix et bénédiction sur lui — a annoncé sa proximité et mentionné ses signes mineurs et majeurs : le lever du soleil depuis son couchant, la sortie de la Bête, l’ouverture de la digue de Gog et Magog, la descente de ʿĪsā — sur lui la paix —, la sortie de l’Antéchrist (<em>al-Dajjāl</em>) : voilà cinq [signes] majeurs sur lesquels on s’accorde. Et l’échéance de la survenue de l’Heure relève des cinq [inconnaissables] que Dieu Très-Haut Seul connaît. Le Glorifié dit :</p>
<p>« C’est auprès de Dieu qu’est la science de l’Heure ; c’est Lui qui fait descendre la pluie, et Il sait ce que recèlent les matrices. Nul ne sait ce qu’acquerront les âmes demain, et nul ne sait en quelle terre il mourra. Dieu est savant, informé. » (Luqmān, 34)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte Luqmān 33 : cible 34 par adjacence (+1) — le verset des cinq inconnaissables que Dieu Seul sait (l’Heure, la pluie, les matrices, l’acquisition de demain, la terre de la mort) ; cible univoque par le contexte.]</p>
<h4>2. La résurrection et le rassemblement</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Que Dieu ressuscite quiconque meurt : comme Il les a commencés, ils retourneront. » Il est de la croyance obligatoire que Dieu — glorifié et magnifié soit-Il — ressuscite quiconque meurt : les musulmans ont unanimement convenu de cela. Les savants y ont avancé plusieurs arguments, dont l’analogie de la restitution sur la production première — vers quoi l’auteur pointe par sa parole : « comme Il les a commencés, ils retourneront », par laquelle il fait allusion à la parole du Très-Haut :</p>
<p>« Dis : “Mon Seigneur a ordonné l’équité ; dressez vos visages à chaque lieu de prosternation, et invoquez-Le, Lui vouant une religion sincère. Comme Il vous a commencés, vous retournerez.” » (al-Aʿrāf, 29)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; cible univoque : la reprise littérale « comme Il vous a commencés, vous retournerez » (<em>kamā badaʾakum taʿūdūn</em>) est la source même de la clause du <em>matn</em>.]</p>
<p>— c’est-à-dire : comme Il vous a produits du néant à l’être, de même Il vous produira après votre mort, pour le rassemblement. Les savants ont encore appuyé [la résurrection] de nombreux versets coraniques, dont la parole du Très-Haut :</p>
<p>« Ils ne pourront alors ni faire de recommandation, ni retourner vers les leurs. » (Yā-Sīn, 50)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée (Yā-Sīn 50) est conservée — non univoque : le verset adjacent 51 (« On soufflera dans la Trompe, et voilà que des tombes ils sortiront vers leur Seigneur ») est le verset de la sortie des tombes ; écart possible (+1) non tranché, référence imprimée rendue telle quelle.]</p>
<h3>Deuxièmement : la multiplication des bonnes actions et le pardon des péchés par le repentir</h3>
<h4>1. La multiplication des bonnes actions des croyants</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Et que Dieu — glorifié et magnifié soit-Il — a multiplié pour Ses serviteurs croyants les bonnes actions. » Dieu a réservé à cette communauté noble, en honneur à notre Prophète — paix et bénédiction sur lui —, la multiplication de ses bonnes actions et leur accroissement : notre Maître — glorifié soit-Il — agrée d’elle le peu et la rétribue du beaucoup. Cela est de la croyance obligatoire, en raison de sa venue dans le Livre et la Sunna. Du Livre, la parole du Très-Haut :</p>
<p>« L’image de ceux qui dépensent leurs biens dans le chemin de Dieu : un grain d’où naissent sept épis, à cent grains l’épi — et Dieu multiplie à qui Il veut ; Dieu est immense, sachant. » (al-Baqara, 261)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte Baqara 260 : cible 261 par adjacence (+1) — la parabole du grain (sept épis à cent grains : jusqu’au sept centuple, miroir du hadith qui suit) ; la imprimée 260 (Ibrāhīm et la revivification des morts) relève de l’argument de la résurrection ; cible univoque par le contexte.]</p>
<p>Et la parole du Très-Haut :</p>
<p>« Dis : “Ô Mes serviteurs qui avez cru, craignez votre Seigneur. Ceux qui, ici-bas, auront fait le bien auront une belle part — et la terre de Dieu est vaste. Seuls les patients verront leur salaire intégralement versé, sans compte.” » (al-Zumar, 10)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<p>Et la parole du Très-Haut :</p>
<p>« Quiconque vient avec une bonne action, à lui dix semblables ; et quiconque vient avec une mauvaise, on ne le rétribue que par son équivalent — et ils ne seront point lésés. » (al-Anʿām, 160)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<p>De la Sunna, [viennent] de nombreux hadiths, dont le hadith du Voyage nocturne (<em>miʿrāj</em>) au sujet de la prière : « … Elles sont cinq, et elles en valent cinquante : la parole ne sera point changée auprès de Moi. »</p>
<p>[<em>Ṣaḥīḥ</em> d’al-Bukhārī, Livre de la prière, chapitre : comment la prière fut prescrite lors du Voyage nocturne — hadith d’Anas b. Mālik, d’après Mālik b. Saʿsaʿa ; vérifié : Bukhārī 349 — le texte reçu porte « la parole ne sera point changée » (<em>lā yubaddalu</em>) : la tournure « <em>mā</em> » du manuel est une variante de citation notée.]</p>
<p>Et le hadith d’Ibn ʿAbbās — que Dieu les agrée — rapportant du Prophète — paix et bénédiction sur lui — ce qu’il transmet de son Seigneur — Puissant et Majestueux : « Dieu a inscrit les bonnes actions et les mauvaises, puis Il a exposé cela : quiconque forme le projet d’une bonne action sans l’accomplir, Dieu la lui inscrit auprès de Lui comme bonne action entière ; s’il en forme le projet et l’accomplit, Dieu la lui inscrit auprès de Lui comme dix bonnes actions — jusqu’à sept cents fois, et jusqu’à des multiplications sans nombre ; quiconque forme le projet d’une mauvaise action sans l’accomplir, Dieu la lui inscrit auprès de Lui comme bonne action entière ; s’il en forme le projet et l’accomplit, Dieu la lui inscrit comme une seule mauvaise action. »</p>
<p>[<em>Ṣaḥīḥ</em> d’al-Bukhārī, Livre de l’adoucissement des cœurs (<em>al-raqāʾiq</em>), chapitre : quiconque forme le projet d’une bonne ou d’une mauvaise action — vérifié : Bukhārī 6491, voie d’Ibn ʿAbbās — hadith rapporté de son Seigneur (<em>qudsī</em>) ; CONFORME.]</p>
<h4>2. Le pardon des péchés par le repentir</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — dit : « Leur a passé outre, par le repentir, les péchés majeurs, et leur a pardonné les péchés mineurs moyennant l’évitement des majeurs. » Il est de la croyance obligatoire que Dieu — glorifié et magnifié soit-Il — passe outre et efface les péchés majeurs grâce au repentir, par faveur et générosité de Sa part envers Ses serviteurs ; et qu’Il efface les péchés mineurs moyennant l’évitement des majeurs.</p>
<p>Cela est venu dans le Noble Coran, comme en la parole du Très-Haut :</p>
<p>« Si vous évitez les péchés majeurs qui vous sont interdits, Nous effacerons vos méfaits, et Nous vous ferons entrer par une entrée généreuse. » (al-Nisāʾ, 31)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<p>Et la parole du Très-Haut :</p>
<p>« … qui évitent les péchés majeurs et les turpitudes — hormis les fautes légères. Certes, le pardon de ton Seigneur est immense. » (al-Najm, 32)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<p>Le pardon (<em>maghfira</em>) est la couverture des péchés et l’absence de reddition de comptes pour eux. [Deux phrases imprimées soudées — séparées.] Et la signification de la parole de l’auteur — que Dieu Très-Haut lui fasse miséricorde : « et qu’Il a fait de quiconque ne se repent pas des péchés majeurs un devenir tributaire de Sa volonté » — est que le croyant qui ne s’est pas repenti des péchés majeurs et meurt persistant en cela devient tributaire de la volonté de Dieu — glorifié soit-Il : s’Il veut, Il lui pardonne ; s’Il veut, Il le châtie, puis le fait ensuite entrer au Paradis.</p>
<h4>3. L’associationnisme, que Dieu ne pardonne pas</h4>
<p>L’auteur — que Dieu Très-Haut lui fasse miséricorde — a appuyé [que] l’associationnisme n’est pas pardonné par Dieu [au moyen] de la parole du Très-Haut :</p>
<p>« Dieu ne pardonne pas qu’on Lui associe ; et Il pardonne ce qui est en deçà à qui Il veut. Quiconque associe à Dieu s’est égaré d’un égarement extrême. » (al-Nisāʾ, 116)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte Nisāʾ 115 : cible 116 par adjacence (+1) — le verset exact du non-pardon de l’association, repris mot à mot dans le <em>matn</em> ; Nisāʾ 48 en est le pendant parallèle ; la imprimée 115 (la scission d’avec le Messager) est étrangère au propos ; cible univoque.]</p>
<p>Ce verset a enveloppé la réfutation de quatre groupes en la question du statut du désobéissant :</p>
<ul>
<li>les Khārijites, qui déclarent mécréant le désobéissant s’il ne se repent pas, et qui disent de lui qu’il est un hypocrite ;</li>
<li>les Murjiʾites, qui disent qu’avec la foi aucune désobéissance ne nuit, comme avec la mécréance aucune obéissance ne profite ; [Le relatif imprimé est au singulier pour un pluriel — coquille rendue correctement.]</li>
<li>les <em>Waʿīdiyya</em> parmi les Muʿtazila, qui soutiennent qu’il faut nécessairement exécuter la menace, et que le péché vaut la perpétuité dans le Feu ;</li>
<li>les Muʿtazila, qui soutiennent qu’il est en une position entre les deux positions — on ne dit de lui ni croyant ni mécréant —, et qui ont fait de la perversité un degré entre la mécréance et la foi ;</li>
<li>et la doctrine des gens de la Sunna, les Ashʿarites, en la matière : la possibilité légale du pardon pour le désobéissant — son affaire est renvoyée à Dieu Très-Haut : s’Il veut, Il le châtie ; s’Il veut, Il lui pardonne — pour autant qu’il ne tienne pas pour licite un interdit unanimement convenu, ni ne prenne son Seigneur à la légère. Leur preuve est ce verset et d’autres arguments tranchants.</li>
</ul>
<h2>Les fruits de la leçon</h2>
<p>La préparation du croyant à la rencontre de son Seigneur par sa foi en l’Heure, la résurrection et la rétribution, et l’œuvre en conséquence ; la présence intérieure de la grandeur du stationnement devant son Seigneur — glorifié soit-Il. Cela appelle à accomplir les obéissances et à éviter les désobéissances, qui troublent la limpidité du lien du serviteur avec son Seigneur, lui font perdre de vue la finalité de son existence, le rendent captif d’elles et le précipitent dans les abîmes des contraventions.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>J’explicite la signification de la parole de l’auteur : « Et que l’Heure vient — nul doute à son sujet. »</li>
<li>Quels sont les arguments de la résurrection et du rassemblement ?</li>
<li>Quelles sont les espèces de péchés, et par quoi Dieu les pardonne-t-Il ?</li>
</ul>
<h2>La préparation préalable (<em>iʿdād qablī</em>)</h2>
<ul>
<li>Quelles sont les œuvres qui mènent leur auteur au Feu ?</li>
<li>Par quoi les hommes entrent-ils au Paradis ?</li>
<li>Je cherche l’interprétation de la parole du Très-Haut :</li>
</ul>
<p>« … et quiconque fait un mal, fût-il du poids d’un atome, le verra. » (al-Zalzala, 8)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16735":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16735 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    # contrôle apostrophes typographiques : aucune droite dans le corps
    n_droites = HTML_FR.count("'")
    print(f"OK — leçon 16735 main: FR {len(HTML_FR)} car ; apostrophes droites: {n_droites} (attendu 0)")


if __name__ == "__main__":
    main()
