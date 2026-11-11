#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 16691 (tawhid-1es, leçon 2 — le motif de
la rédaction de la Risāla et son contenu : la khutba liminaire du matn).

Vérifications et restitutions :
- Matn = la khutba d'ouverture de la Risāla (basmala + taḥlīl d'auteur +
  hamdala + istikhbār de Muḥriz b. Khalaf al-Bukrī) — DOUBLONS OCR
  détangles : le paragraphe tamhīd est imprimé 2× d'affilée (coupure/
  reprise de composition) et le segment « المومنين لليسرى… عمّا حرّم
  عليهم » 2× entrelacé — rendu UNE fois, noté.
- « المُرْسَلِينَ المُومِنِينَ لِلْيُسْرَى » : orthographe qayrawānienne du
  wāw redoublé (المُومِنِينَ = المُؤْمِنِينَ, comme « أولاد المومنين » plus
  bas) — rendue « croyants en la voie de la facilité (al-yusrā) », notée.
- Coquille du tamhīd : « أبو عبد الله محمد بن أبي زيد » — inversion
  kunya/nom (le personnage est Abū Muḥammad ʿAbd Allāh) — notée, rendu
  corrigé.
- Hadith d'Abū Hurayra « كل أمر ذي بال لا يبدأ فيه بالحمد لله فهو أجذم »
  [سنن أبي داود كتاب الأدب باب: الهدي في الكلام] — VÉRIFIÉ sunnah.com :
  Abū Dāwūd 4840 (Kitāb al-Adab, bāb al-hidāya fī l-kalām) — réf CONFORME ;
  l'imprimé lit « كل أمر ذي بال », le texte reçu « كل كلام » — les deux
  leçons sont transmises (cf. ʿAwn al-maʿbūd) — variante notée. « أجذم »
  glosé par le manuel : « أقطع قليل البركة » (amputé de bénédiction).
- « أجذم » / ajdham : amputé — rendu avec la glose imprimée.
- Glose « الخيرة : بكسر الخاء وفتح الياء — المختارين من خلقه » : la vedette
  n'apparaît PAS dans l'extrait du matn imprimé — glose conservée telle
  quelle + note (le mot relève de la khutba complète de la Risāla).
- FIX GT-ismes : « abrégé de phrases » → « une somme abrégée » ; « les
  cœurs les plus espérants » → « les plus enclins à l'espérance du bien » ;
  « quiconque le lit et travaille » → « quiconque lit son livre et agit
  selon ce qu'il contient ».
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : le motif de la rédaction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī et son contenu</h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la deuxième leçon (2), portant sur le motif de la rédaction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī et sur son contenu.</p>
<ul>
<li>Connaître le motif de la rédaction de la <em>Risāla</em> et ses contenus.</li>
<li>Connaître les traits des meilleurs des cœurs.</li>
</ul>
<h2>Préambule</h2>
<p>Dieu créa l’homme et fit merveille en sa facture : Il le forma et embellit sa forme, le créa en la meilleure conformation, et lui ordonna de méditer les faveurs de Dieu sur lui-même, pour en inférer son Créateur ; et Il lui rendit obligatoire la connaissance de tout ce qui touche aux matières obligées de la religion, en actes et paroles fondés sur l’unicité de Dieu Très-Haut. Et c’est ce qu’affermit l’imam, jurisconsulte et illustre savant Abū Muḥammad ʿAbd Allāh b. Abī Zayd al-Qayrawānī dans l’introduction de son livre la <em>Risāla</em>. [L’imprimé écrit « Abū ʿAbd Allāh Muḥammad b. Abī Zayd al-Qayrawānī » — coquille (inversion de la kunya et du nom) : le personnage est Abū Muḥammad ʿAbd Allāh ; le paragraphe est imprimé deux fois d’affilée — duplication de composition rendue une fois.]</p>
<p>Quel est le motif qui poussa Ibn Abī Zayd à composer son livre la <em>Risāla</em> ? Et quels sont ses principaux contenus ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>Ibn Abī Zayd al-Qayrawānī — que Dieu lui fasse miséricorde — dit : « Au nom de Dieu, le Miséricordieux, le Très-Miséricordieux ; que Dieu prie sur notre maître Muḥammad, sur sa famille et ses compagnons, et les salue. Abū Muḥammad ʿAbd Allāh, fils d’Abī Zayd al-Qayrawānī — que Dieu l’agrée et soit satisfait de lui — dit : Louange à Dieu, qui entama l’homme par Sa faveur, le forma dans les matrices par Sa sagesse, le tira dehors vers Sa douceur et [lui accorda] ce qu’Il lui facilita de Sa subsistance ; qui lui enseigna ce qu’il ne savait pas — et la faveur de Dieu sur lui fut immense ; qui l’éveilla par les traces de Sa facture, et Lui présenta Son excuse par les langues des envoyés — croyants en la voie de la facilité (<em>al-yusrā</em>) [l’imprimé porte <em>al-mūminīn</em> : orthographe qayrawānienne du wāw redoublé pour <em>al-muʾminīn</em>, “ les croyants ”] —, et ouvrit leurs poitrines au rappel : ils crurent en Dieu, parlant de leurs langues, sincères de leurs cœurs, agissant selon ce que Ses messagers et Ses livres leur apportèrent ; ils apprirent ce qu’Il leur enseigna, s’arrêtèrent à ce qu’Il leur délimita, et se passèrent de ce qu’Il leur interdit par ce qu’Il leur permit... Or donc : que Dieu nous secoure, toi et moi, à garder Ses dépôts (<em>wadāʾiʿ</em>) et à préserver ce qu’Il nous a confié de Ses lois. Tu m’as demandé d’écrire pour toi une somme abrégée des matières obligées de la religion — de ce que prononcent les langues, croient les cœurs et accomplissent les membres. Sache que les meilleurs des cœurs sont les plus aptes au bien ; et les plus enclins à l’espérance du bien, ceux que le mal n’a pas devancés. Et la chose la plus juste dont s’occupent les conseillers, et que désirent — en sa récompense — les désireux, est la conduite du bien aux cœurs des enfants des croyants pour qu’il s’y enracine, et leur éveil aux repères de la religion et aux limites de la Loi pour qu’ils s’y exercent et s’y plient — et ce qu’ils ont en charge, que leurs cœurs le croient de la religion et que leurs membres l’accomplissent. » [Le segment « croyants en la voie de la facilité... de ce qu’Il leur interdit » est imprimé deux fois entrelacé — duplication OCR rendue une fois.]</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>abraza-hu ilā raṣi-hi</em> (le tira dehors vers Sa douceur) : le fit sortir et paraître vers son utilité.</li>
<li><em>nabba-hu bi-āthār ṣanʿati-hi</em> (l’éveilla par les traces de Sa facture) : l’éveilla par la considération (<em>iʿtibār</em>) de Ses ouvrages.</li>
<li><em>al-khīra</em> (kasra du khāʾ, fatḥa du yāʾ) : les choisis (<em>al-mukhtārīn</em>) parmi Sa création. [La vedette n’apparaît pas dans l’extrait du <em>matn</em> imprimé — glose conservée telle quelle : le mot relève de la khutba complète de la <em>Risāla</em>.]</li>
<li><em>yunāḍa</em>, lire <em>yurāḍa</em> (s’y exercent) : être dompté et soumis.</li>
</ul>
<h3>L’extraction des contenus</h3>
<ul>
<li>J’extrais du <em>matn</em> quelques règles de bonne composition et d’enseignement.</li>
<li>J’extrais du <em>matn</em> ce qui est obligé parmi les matières de la religion.</li>
<li>J’extrais du <em>matn</em> ce dont doivent s’occuper les conseillers et guides.</li>
</ul>
<h2>L’analyse</h2>
<p>La leçon contient les axes suivants :</p>
<h3>Premièrement : la louange de Dieu — Puissant et Élevé — pour Ses faveurs</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Louange à Dieu. » Après s’être présenté, l’auteur — que Dieu lui fasse miséricorde — entama sa composition par la louange et la célébration de Dieu, Puissant et Élevé, en acquit de ce qui lui était dû de gratitude envers le Bienfaiteur pour Ses faveurs, et en exécution du hadith d’Abū Hurayra rapporté du Prophète — paix et bénédiction sur lui — : « Toute affaire de conséquence où l’on ne commence pas par : “ Louange à Dieu ”, est amputée (<em>ajdham</em>) » — c’est-à-dire coupée, pauvre en bénédiction. [Sunan d’Abū Dāwūd, Livre des bons usages, chapitre : la guidance en la parole — réf CONFORME (n° 4840) ; l’imprimé lit « toute affaire de conséquence » (<em>kullu amrin dhī bālin</em>), le texte reçu « toute parole » (<em>kullu kalāmin</em>) — les deux leçons sont transmises, cf. <em>ʿAwn al-maʿbūd</em>.]</p>
<h4>L’exposé du sens de la louange (<em>ḥamd</em>) est ce qui suit :</h4>
<ul>
<li>a. Au sens propre : la description par le beau, en manière de magnification — or la description n’a lieu que par la langue.</li>
<li>b. Au sens technique : un acte qui fait connaître la magnification du Bienfaiteur, du fait qu’Il est bienfaiteur ; et l’acte est plus général que la description : il est ou acte du cœur — la croyance qu’Il est, Puissant et Élevé, paré des attributs de perfection, de beauté et de majesté —, ou acte de la langue — l’énoncé de ce qui Le fait connaître, l’Élevé —, ou acte des membres : l’accomplissement d’actes qui font connaître la célébration de Dieu Très-Haut.</li>
</ul>
<h4>La gratitude (<em>shukr</em>)</h4>
<ul>
<li>Au sens propre, la gratitude est la louange.</li>
<li>Au sens technique, c’est : porter le serviteur à employer tout ce dont Dieu l’a gratifié à ce en vue de quoi cela fut créé — comme employer la vue à contempler Ses ouvrages et à en inférer, par eux, [l’existence de] Dieu, Puissant et Élevé.</li>
</ul>
<h3>Deuxièmement : le motif de la rédaction de la <em>Risāla</em> et son contenu</h3>
<h4>Le motif de la rédaction de la <em>Risāla</em></h4>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « Tu m’as demandé d’écrire pour toi une somme abrégée des matières obligées de la religion. » Après la louange de Dieu et la gratitude pour Ses faveurs, et la prière sur Son prophète notre maître Muḥammad — paix et bénédiction sur lui —, il exposa — que Dieu lui fasse miséricorde — que le motif de la rédaction de la <em>Risāla</em> fut la demande du shaykh Muḥriz, lui demandant d’écrire une somme abrégée des matières obligées de la religion.</p>
<h4>Le contenu du livre de la <em>Risāla</em> d’Ibn Abī Zayd</h4>
<p>L’auteur — que Dieu lui fasse miséricorde — dit : « — de ce que prononcent les langues, croient les cœurs et accomplissent les membres, et de ce qui se rattache à l’obligé, de cela, des sunna attestées (<em>muʾakkada</em>), de ses surérogatoires (<em>nawāfil</em>) et de ses pratiques méritoires (<em>raghāʾib</em>), et de quelque chose des convenances (<em>ādāb</em>) de cela, et de sommes des principes du droit et de ses chapitres (<em>uṣūl al-fiqh wa-funūnihi</em>). »</p>
<p>Le livre de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī — que Dieu lui fasse miséricorde — contient une somme abrégée, pauvre en mots, riche en sens, des matières suivantes :</p>
<ul>
<li>a. Ce qui est obligé parmi les matières de la religion, de ce que prononcent les langues : comme les deux attestations, l’ordonnance du convenable et l’interdiction du blâmable, et leurs semblables.</li>
<li>b. Ce qui est obligé parmi les matières de la religion, de ce que croient les cœurs (<em>afʾida</em>) : comme la foi en Dieu, en Ses anges, en Ses livres, en Ses messagers, au Dernier Jour et au Décret, en son bon et son mauvais, son doux et son amer.</li>
<li>c. Ce qui est obligé parmi les matières de la religion, de ce qu’accomplissent les membres : comme la prière, la dîme, le jeûne, le pèlerinage, la vente, le mariage et le reste.</li>
<li>d. Ce qui se rattache à l’obligé et le complète : les sunna attestées, les surérogatoires et les pratiques méritoires.</li>
<li>e. Quelque chose des convenances, et les matières-mères des questions du droit et ses principes, par quoi le livre s’achève.</li>
</ul>
<h3>Troisièmement : les meilleurs des cœurs et ce dont les conseillers doivent le plus s’occuper</h3>
<p>L’auteur — que Dieu lui fasse miséricorde — mentionne que les meilleurs des cœurs, les plus aptes à retenir et les plus proches du bien, sont le cœur que le mal n’a pas devancé : car si le mal ne l’a pas devancé, il reçoit bien ce qui lui parvient de bien ; mais si la croyance du mal l’a devancé, grande est la ruse à l’extirper. Il expose ensuite que la chose la plus juste et la plus due dont s’occupent les conseillers et les guides vers le bien est triple :</p>
<ul>
<li>La première : conduire le bien et le faire parvenir aux cœurs des enfants des croyants, pour qu’il s’y enracine et s’y affermisse.</li>
<li>La deuxième : les éveiller et les réveiller du sommeil de l’ignorance et de l’inadvertance aux règles de la religion, qui sont les repères (<em>maʿālim</em>) de la foi.</li>
<li>La troisième : les avertir de s’arrêter aux limites de la Loi — qui sont les règles qui concernent les actes des redevables, et ce qu’ils ont charge que leurs cœurs croient de la religion et que leurs membres accomplissent des règles de la Loi.</li>
</ul>
<h2>Les fruits de la leçon</h2>
<p>Approuver d’ouvrir les œuvres pies par leurs convenances légales — parmi lesquelles la basmala et la parole de louange — en acquit du droit de Dieu Très-Haut et en conquête de bénédiction : car la célébration de Dieu pour Ses faveurs est l’annonce de leur continuation et de leur accroissement ; et le rappel que la félicité d’ici-bas et de l’au-delà ne se réalise que par la droiture du credo, la pureté du cœur, la sauvegarde des membres et la sincérité en l’action.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>Qu’est-ce que la louange, au sens propre et au sens technique ? Et quelle est la différence entre la louange (<em>ḥamd</em>) et la gratitude (<em>shukr</em>) ?</li>
<li>J’expose ce que vise la parole de l’auteur : « ...que croient les cœurs et accomplissent les membres ».</li>
<li>Je mentionne ce dont doivent s’occuper les conseillers et les guides vers le bien.</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>Les matières de la religion (<em>umūr al-diyāna</em>) sont ses questions ; et la religion (<em>dīn</em>) vient de <em>dāna yadīnu</em>, “ il obéit ” ; la <em>diyāna</em> est le commerce [avec Dieu] ; et ce que l’on vise est ce par quoi on “ dîne ” Dieu — c’est-à-dire ce par quoi on L’adore : c’est Sa Loi (<em>sharīʿa</em>), qui contient les offices de la religion, en paroles et en actes.</p>
<h3>Je contemple cette parole et réalise ce qui suit :</h3>
<ul>
<li>Je définis : la religion (<em>dīn</em>) et la Loi (<em>sharīʿa</em>).</li>
<li>J’expose la différence entre la religion et la Loi, en l’appuyant de preuves tirées du Livre et de la Sunna.</li>
<li>J’expose le plus important des actes des membres parmi les matières de la religion, avec l’appui de la preuve.</li>
</ul>
<h2>La préparation préalable (<em>iʿdād</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et réalise ce qui suit :</p>
<ul>
<li>Je recherche les sens de ces vocables : le Tawḥīd — le credo (<em>ʿaqīda</em>) — la science du kalām — la foi (<em>īmān</em>) — l’adoration (<em>ʿibāda</em>).</li>
<li>Je mentionne l’importance du credo en ma vie d’ici-bas et de l’au-delà.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "16691":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 16691 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 16691 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
