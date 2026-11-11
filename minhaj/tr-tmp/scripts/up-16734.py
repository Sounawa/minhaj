#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16734 (tawhid-1es, leçon 13 — la mission
de notre maître Muḥammad ﷺ, sceau des révélations célestes).

Vérifications et restitutions (cache quran = Ḥafṣ ; sunnah.com UA navigateur) :
- Matn : « ثم ختم الرسالة والنذارة والنبوة بمحمد ﷺ... وهدى به الصراط
  المستقيم » — rendu fidèlement (le matn reprend Aḥzāb 45-46).
- HADITH VÉRIFIÉ sunnah.com : « أنت مني بمنزلة هارون من موسى إلا أنه لا
  نبي من بعدي » → Muslim 2404 (Kitāb Faḍāʾil al-Ṣaḥāba, voie Saʿīd b.
  al-Musayyib ← ʿĀmir b. Saʿd ← Saʿd b. Abī Waqqās) — le texte reçu porte
  « lā nabiyya baʿdī » SANS le « min » : la particule du manuel est une
  variante mineure de citation, notée inline (Bukhārī 4416 : « laysa
  nabiyyun baʿdī »). La réf imprimée (Muslim, faḍāʾil al-ṣaḥāba, bāb
  faḍāʾil ʿAlī) est EXACTE.
- CITATIONS VIDES (perte OCR) RESTAURÉES du cache, cibles doctrinales :
  * [الأحزاب: 40] → CONFORME (« وخاتم النبيين » — cible univoque du
    scellement) ;
  * [المدثر: 1] → Muddaththir 1-2 (« قم فأنذر ») — la visée de
    l'avertissement est le verset 2 : les deux versets rendus, écart noté ;
  * [الأنعام: 20] → Anʿām 19 (« لأنذركم به ومن بلغ » — l'universalité de
    la mission : cible univoque) — réf d'adjacence (−1) notée ;
  * [الفرقان: 1] → CONFORME (« ليكون للعالمين نذيرا ») ;
  * [هود: 1] → CONFORME (« كتاب أحكمت آياته... من لدن حكيم خبير » — le
    Livre sage) ;
  * [الإسراء: 88] → CONFORME (le défi coranique — l'inimitabilité) ;
  * [الشورى: 49-50] → Shūrā 52-53 (« وإنك لتهدي إلى صراط مستقيم » —
    cible univoque : le miroir exact du matn « هدى به الصراط المستقيم ») —
    écart +3 noté (comme Wāqiʿa 88→85, leçon 7) ; Shūrā 49-50 (les
    filles, les fils, la stérilité) est sans rapport au contexte ;
  * [الأحزاب: 45-48] (istithmār) → CONFORME (les missions du Prophète +
    le traitement des hostiles — couvre les deux travaux demandés).
- Doublon OCR des objectifs : « أن أتعرف صفات خاتم الأنبياء » imprimé 2×,
  4 phrases fusionnées en 1 paragraphe — 3 objectifs rendus, noté.
- Les 2 items d'extraction fusionnés (3 phrases) — rendus en 3 items, noté.
- Les 2 questions de l'iʿdād fusionnées en 1 item — rendues séparément.
- Titre « التحليل » absent de l'extrait — restitué selon la série, noté.
- Coquilles du tampon (« صلى الله عيه وسلم », « صلى لله عليه ») rendues
  normalement ; tampon de date du site non rendu (règle corpus).
- « كرم الله وجهه » après ʿAlī — formule pieuse imprimée rendue telle
  quelle.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : la mission de notre maître Muḥammad ﷺ, sceau des révélations célestes</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la treizième leçon (13).</p>
<ul>
<li>Connaître les attributs du Sceau des prophètes et des messagers. [Objectif imprimé deux fois — rendu une fois.]</li>
<li>Saisir la finalité de l’envoi de notre maître Muḥammad — paix et bénédiction sur lui.</li>
<li>Faire miens en ma vie les caractères du Prophète — paix et bénédiction sur lui.</li>
</ul>
<h2>Préambule</h2>
<p>Dieu, glorifié et magnifié soit-Il, Se distingua par la création et la production, la subsistance et l’octroi à l’ensemble de Ses créatures ; Il chargea Ses serviteurs de Son obéissance, et les gratifia de l’envoi des messagers — de Sa faveur et de Sa grâce — pour leur exposer les droits de leur Seigneur sur eux ; et Il scella les révélations par la mission de notre maître Muḥammad — paix et bénédiction sur lui.</p>
<p>Quelle est la finalité de l’envoi de notre maître Muḥammad — paix et bénédiction sur lui ? Et par quoi la mission de notre maître Muḥammad — paix et bénédiction sur lui — se distingua-t-elle ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>Ibn Abī Zayd — que Dieu lui fasse miséricorde — dit : « Puis Il scella la mission, l’avertissement et la prophétie par Muḥammad — paix et bénédiction sur lui — et fit de lui le dernier des envoyés : annonciateur et avertisseur, invitant vers Dieu par Sa permission, et lampe lumineuse ; et Il fit descendre sur lui Son Livre sage, et exposa par lui Sa religion droite, et guida par lui vers le chemin droit. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li>l’avertissement (<em>nadhāra</em>) : la mise en garde et l’intimidation.</li>
<li>la prophétie (<em>nubuwwa</em>) : de <em>nabaʾ</em> — la nouvelle ; ou de <em>nabwa</em> — l’élévation.</li>
<li><em>sirājan</em> (une lampe) : un flambeau, une source de lumière.</li>
<li><em>sharaḥa</em> (exposer) : faire comprendre.</li>
<li>le chemin droit (<em>al-ṣirāṭ al-mustaqīm</em>) : la voie droite et le sentier égal.</li>
</ul>
<h3>L’extraction des contenus du <em>matn</em></h3>
<ul>
<li>J’extrais du <em>matn</em> ce par quoi la mission de notre maître Muḥammad — paix et bénédiction sur lui — se distingua.</li>
<li>J’extrais du <em>matn</em> le miracle permanent du Prophète — paix et bénédiction sur lui. [Deux items imprimés fusionnés — rendus séparément.]</li>
<li>J’extrais du <em>matn</em> la fonction des messagers, dont notre maître Muḥammad — paix et bénédiction sur lui.</li>
</ul>
<h2>L’analyse</h2>
<p>[Titre restitué selon la série — absent de l’extrait, noté.] La leçon contient ce qui suit :</p>
<h3>Premièrement : la mission de notre maître Muḥammad, sceau des révélations célestes</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Puis Il scella la mission, l’avertissement et la prophétie par Muḥammad — paix et bénédiction sur lui — et fit de lui le dernier des envoyés. » L’auteur — que Dieu lui fasse miséricorde — ayant mentionné, en la leçon précédente, que l’Elevé envoya les messagers pour transmettre à Ses serviteurs les règles, et coupa par là leur excuse, informe ici que l’Elevé paracheva la mission et la scella par Muḥammad — paix et bénédiction sur lui : nul ne se tient en sa place en elle.</p>
<p>Sa parole — que Dieu lui fasse miséricorde — : « scella » procède du scellement au sens de l’achèvement, comme tu dirais : « je scellai le Coran », c’est-à-dire : je l’achevai. Que la mission de notre maître Muḥammad — paix et bénédiction sur lui — soit le sceau des révélations célestes, l’attestent le Livre, la Sunna et le consensus. Du Livre, la parole du Très-Haut :</p>
<p>« Muḥammad n’est le père d’aucun de vos hommes ; mais il est l’Envoyé de Dieu et le Sceau des prophètes — et Dieu, de toute chose, est sachant. » (al-Aḥzāb, 40)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<p>De la Sunna, sa parole — paix et bénédiction sur lui — à ʿAlī b. Abī Ṭālib — que Dieu honore sa face :</p>
<p>« Tu es de moi au rang de Hārūn auprès de Mūsā — sauf qu’il n’est point de prophète après moi. »</p>
<p>[<em>Ṣaḥīḥ</em> de Muslim, Livre des mérites des Compagnons, chapitre des mérites de ʿAlī b. Abī Ṭālib — que Dieu l’agrée ; vérifié : Muslim 2404, voie de Saʿd b. Abī Waqqās — le texte reçu porte « il n’est point de prophète après moi » sans le « de » : particule du manuel, variante mineure de citation notée.]</p>
<p>Et le consensus se noua sur cela. L’auteur s’en tint à l’avertissement, qui est la mise en garde du mal, sans mentionner l’annonce — se contentant de l’un des deux contraires pour l’autre, car il l’entraîne. C’est la parole du Très-Haut :</p>
<p>« Ô toi, l’enveloppé ! Lève-toi, et avertis ! » (al-Muddaththir, 1-2)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte « 1 », la visée « lève-toi et avertis » inclut le verset 2 — les deux versets rendus, écart noté.]</p>
<p>La parole de l’auteur — que Dieu lui fasse miséricorde — : « et fit de lui le dernier des envoyés » est l’exposé de sa parole : « Il scella la mission ». Sa parole : « annonciateur » — par la récompense, pour qui obéit, et par le Paradis, pour qui croit ; sa parole : « et avertisseur » — par le châtiment, pour qui désobéit, et par le Feu, pour qui dénie ; sa parole : « invitant vers Dieu par Sa permission » — invitant à la reconnaissance de Son unicité et de ce qui est obligatoire de la foi en Ses attributs. Le Prophète — paix et bénédiction sur lui — se tint à la fonction d’orienter les créatures et de les enseigner de la plus belle tenue : il ne cessa de les appeler, de user de douceur avec eux et de porter leurs nuisances, jusqu’à ce qu’ils se pliassent à lui et s’assemblassent sur lui. L’universalité de sa mission — paix et bénédiction sur lui — est attestée par la parole du Très-Haut :</p>
<p>« Dis : quelle chose est plus grand témoignage ? Dis : Dieu — témoin entre moi et vous. Et c’est ce Coran qui me fut révélé, pour que j’avertisse par lui vous et quiconque il atteint. » (al-Anʿām, 19 — extrait)</p>
<p>et Sa parole :</p>
<p>« Béni soit Celui qui fit descendre le Discernement (<em>al-Furqān</em>) sur Son serviteur, pour qu’il fût pour les mondes un avertisseur. » (al-Furqān, 1)</p>
<p>[Deux citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; la référence imprimée de la première porte « 20 », la visée est le verset 19 — « quiconque il atteint », l’universalité : réf d’adjacence notée ; la seconde CONFORME.]</p>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « et lampe lumineuse ». La comparaison du Prophète — paix et bénédiction sur lui — à la lampe indique que son existence et sa faveur — paix et bénédiction sur lui — ne furent point limitées à un peuple plutôt qu’à un autre. Et il fut comparé à la lampe plutôt qu’au soleil et à la lune, lors même que leur lumière est universelle, parce que leur lumière décline en leur disparition — tandis que sa lumière, sur lui paix et bénédiction, ne s’interrompt jamais et ne décline point : elle est continue.</p>
<h3>Deuxièmement : le noble Coran, miracle permanent de notre maître Muḥammad</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « et Il fit descendre sur lui Son Livre sage ». Au nombre de ce qu’il faut croire : Dieu, glorifié et magnifié soit-Il, fit descendre sur Son prophète Muḥammad b. ʿAbd Allāh — paix et bénédiction sur lui — Son Livre sage : celui dont les sciences des premiers et des derniers furent affermies, contenant la sagesse, qui est d’apporter chaque chose à sa face. Un Livre dont Dieu dit en Sa description :</p>
<p>« Alif, Lām, Rāʾ. Un Livre dont les signes furent affermis, puis détaillés, de par un Sage, un Bien-Informé. » (Hūd, 1)</p>
<p>Et le glorifié dit :</p>
<p>« Dis : si les hommes et les djinns s’assemblaient pour venir avec pareil à ce Coran, ils ne viendraient point avec son pareil — dussions-ils être, les uns pour les autres, auxiliaires. » (al-Isrāʾ, 88)</p>
<p>[Deux citations restaurées d’après le corpus canonique : les emplacements imprimés sont vides — perte OCR ; les références imprimées CONFORMES.]</p>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « et exposa par lui Sa religion droite, et guida par lui vers le chemin droit ». Dieu Très-Haut exposa et fit comprendre, par Son Prophète — paix et bénédiction sur lui — Sa religion droite, et guida par lui les gens vers Son chemin droit, qui est l’islam. Le Très-Haut dit :</p>
<p>« Et ainsi Nous te révélâmes un esprit de Notre commandement — tu ne savais ce qu’est le Livre ni la foi ; mais Nous fîmes de toi une lumière, par laquelle Nous marchons qui Nous voulons de Nos serviteurs. Et certes, tu guides vers un chemin droit : le chemin de Dieu, à qui appartient ce qui est aux cieux et ce qui est en la terre. » (al-Shūrā, 52-53)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée porte « 49-50 », la visée est « et certes, tu guides vers un chemin droit » — versets 52-53, écart +3 noté (les versets imprimés 49-50 — les filles, les fils, la stérilité — sont sans rapport au contexte).] La parole de l’auteur : « droite » (<em>qawīm</em>) : la droite, en laquelle il n’y a point de torsion.</p>
<h2>Les fruits de la leçon</h2>
<p>L’appel des messagers, et de leur Sceau notre maître Muḥammad — paix et bénédiction sur lui — aux hommes vers la finalité de l’existence des créatures : l’unicité de Dieu Très-Haut et Son culte. Et la mission des prédicateurs : orienter les hommes et les guider vers la religion droite et le chemin droit, qui libère l’homme de toutes les adorations et donne à sa vie un sens en ce monde et en la dernière [demeure].</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>Par quoi la mission de notre maître Muḥammad — paix et bénédiction sur lui — fut-elle décrite ?</li>
<li>J’expose la fonction des messagers, dont notre maître Muḥammad — sur eux la paix — avec appui.</li>
<li>Pourquoi le Livre fut-il décrit de sage ?</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Le Très-Haut dit :</p>
<p>« Ô Prophète ! Certes, Nous t’envoyâmes témoin, annonciateur, avertisseur, invitant vers Dieu par Sa permission, et lampe lumineuse. Annonce aux croyants que, de Dieu, leur est une faveur immense. N’obéis point aux infidèles ni aux hypocrites, et délaisse leur nuisance — et remets-toi à Dieu : Dieu suffit comme dépositaire. » (al-Aḥzāb, 45-48)</p>
<p>[Citation restaurée d’après le corpus canonique : l’emplacement imprimé est vide — perte OCR ; la référence imprimée CONFORME.]</p>
<h3>Je lis les nobles versets en méditation et réalise ce qui suit :</h3>
<ul>
<li>J’extrais des versets les missions du Prophète — paix et bénédiction sur lui.</li>
<li>J’expose, à partir des versets, la manière du prédicateur avec les hostiles à son appel.</li>
</ul>
<h2>La préparation préalable (<em>iʿdād</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et réponds aux questions suivantes :</p>
<ul>
<li>Qu’est-ce que l’Heure ? Et qu’y a-t-il après elle ? [Questions imprimées fusionnées — rendues séparément.]</li>
<li>Quelles sont les espèces des fautes ? Et par quoi sont-elles pardonnées ?</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16734":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16734 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16734 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
