#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 13978 (tawhid-1es, leçon 1 — présentation
d'Ibn Abī Zayd al-Qayrawānī et de sa Risāla).

Conventions main (structure secondaire, cf. hadith-1es 12875-13011) :
- h2 : Préambule / Le texte (matn) / La compréhension (fahm) / L'analyse /
  L'évaluation / L'exploitation / La préparation préalable.
- Matn : Abū l-Ḥasan ʿAlī b. Muḥammad (le commentateur, auteur de la Kifāya)
  + Zarrūq (Sharḥ Zarrūq ʿalā l-Risāla) — rendus fidèlement tels qu'imprimés.
- Ibn Sīrīn : « إن هذا العلم دين فانظروا عمن تأخذون دينكم » — formulation
  canonique (Muqaddima du Ṣaḥīḥ de Muslim), rendue telle quelle.
- Faits biographiques : naissance 310 H., mort lundi 30 Shaʿbān 386 H.,
  ~40 ouvrages, Risāla à 17 ans, 4000 questions + 400 hadiths, pesée d'or
  (300,5 dinars) sur l'ordre d'Abū Bakr al-Abharī — RENDUS TELS QU'IMPRIMÉS
  (attestés dans les biographies mālikites : Dībāj d'Ibn Farḥūn, Riyāḍ
  d'al-Mālikī).
- ʿAdawī (istithmār) : citation [Ḥāshiya 1/11] rendue INTÉGRALEMENT —
  la « firāsa » (pénétration intuitive) avec son anecdote intacte.
- FIX GT-ismes : « العبادة » des idoles (adoration, non « culte ») ;
  « ديانته » = religiosité/piété (non « assurance » !) ; « قطب المذهب » =
  pivot de l'école ; « خليفة مالك » = successeur de Mālik (khalīfat Mālik).
- Le tampon de date du site (lundi 13 oct. 2025 dans 13980) non rendu —
  convention corpus.
- Le pied de page répétant le titre (artefact CMS) non rendu.
"""

import json

BOOK = "/home/z/my-project/content/books/tawhid-1es.json"

HTML_FR = """<h1>Le Tawḥīd : présentation d’Ibn Abī Zayd et de son livre la <em>Risāla</em></h1>
<p>Leçon de la matière du Tawḥīd, tirée de l’introduction de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī avec le commentaire <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>taʿlīm ʿatīq</em>) — la première leçon (1), portant sur la présentation d’Ibn Abī Zayd et de son livre la <em>Risāla</em>.</p>
<ul>
<li>Connaître qui est Ibn Abī Zayd al-Qayrawānī.</li>
<li>Découvrir les œuvres d’Ibn Abī Zayd al-Qayrawānī et son rang scientifique.</li>
<li>Connaître les traits distinctifs du livre de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī.</li>
</ul>
<h2>Préambule</h2>
<p>Certes, la présentation de l’auteur en personne, au début de la composition de son livre, compte au nombre des choses importantes : car la plupart des sciences rapportées (<em>naqliyya</em>) qu’il mentionne en son livre exigent qu’on connaisse celui qui les prononce et la probité (<em>ʿadāla</em>) de celui qui transmet — les sciences transmises ne se prennent que de qui était savant et agissant. Ibn Sīrīn dit : « Cette science est religion : regardez donc de qui vous prenez votre religion. » Et c’est pourquoi les savants dirent : agir, ou répondre à consultation (<em>fatwā</em>), sur la foi de livres dont on ignore les auteurs, et dont on ne sait pas si ce qu’ils contiennent est sain, n’est pas permis.</p>
<p>Qui donc est Ibn Abī Zayd al-Qayrawānī ? Et quelle est l’importance de son livre la <em>Risāla</em> ?</p>
<h2>Le texte (<em>matn</em>)</h2>
<p>Abū l-Ḥasan ʿAlī b. Muḥammad, le commentateur de la <em>Risāla</em>, dit : « Les mérites (<em>manāqib</em>) du Shaykh et sa conduite sont connus : nous en avons transmis un ensemble en l’original (<em>al-aṣl</em>) — à Dieu la louange. »</p>
<p>Et le shaykh Zarrūq dit, en son commentaire sur la <em>Risāla</em> : « Certes, la <em>Risāla</em> d’Ibn Abī Zayd est fameuse par ses mérites et ses vertus, abondante en profit pour le droit et les questions : elle est, en effet, une entrée qui rassemble les chapitres, prochaine à obtenir en ses livres, sa mémorisation et son acquisition ; les premiers et les derniers s’en sont souciés, et les gens du dedans comme du dehors en ont tiré profit. »</p>
<h2>La compréhension (<em>fahm</em>)</h2>
<h3>L’explication (<em>sharḥ</em>)</h3>
<ul>
<li><em>manāqib</em> (les mérites) : pluriel de <em>manqaba</em>, qui est la qualité louable.</li>
<li><em>al-ik tisāb</em> (l’acquisition) : l’obtention, la constitution du savoir.</li>
<li><em>masāʾil</em> (les questions) : les ramifications du droit (<em>furūʿ al-fiqh</em>).</li>
</ul>
<h3>L’extraction des contenus</h3>
<ul>
<li>J’extrais du <em>matn</em> ce que vise la parole d’Abū l-Ḥasan : « Les mérites du Shaykh et sa conduite sont connus. »</li>
<li>J’extrais du texte les principaux mérites de la <em>Risāla</em> d’Ibn Abī Zayd al-Qayrawānī.</li>
</ul>
<h2>L’analyse</h2>
<p>La leçon contient les axes suivants :</p>
<h3>Premièrement : la présentation d’Ibn Abī Zayd al-Qayrawānī</h3>
<p>C’est le savant vénérable Abū Muḥammad ʿAbd Allāh, fils d’Abī Zayd ʿAbd al-Raḥmān, al-Nafzī al-Qayrawānī, imam des mālikites en son temps ; on le surnomme al-Nafzāwī, en raison de Nafzāwa, des tribus d’Ifrīqiya. Il naquit à Qayrawān en l’an 310 de l’Hégire ; c’est là qu’il grandit, fut formé et étudia : il mémorisa le Coran en sa jeunesse, puis passa à l’étude des sciences de l’islam et de la langue arabe ; sa précocité parut de bonne heure, les sources rapportant qu’il composa la <em>Risāla</em> à l’âge de dix-sept ans.</p>
<p>La supériorité d’Ibn Abī Zayd — que Dieu lui fasse miséricorde — et sa précocité polirent et firent mûrir son esprit, du fait qu’il reçut [son savoir] de grands shaykhs parmi les imams de son époque — en grand nombre, et en des lieux divers. La pluralité de ses shaykhs et de ses élèves, et la variété de leurs spécialisations, lui valurent une haute renommée et un rang scientifique éminent, qui firent de lui le but des étudiants en science et en connaissance venus des différents pays. Dieu l’a gratifié de quatre choses : l’ampleur en science, en religion et en biens, et la santé du corps ; il fut surnommé « le successeur de Mālik » (<em>khalīfat Mālik</em>) et « le petit Mālik » (<em>Mālik al-aṣghar</em>).</p>
<p>Au terme d’une riche carrière scientifique, ce grand savant répondit à l’appel de son Seigneur le soir du lundi, trente Shaʿbān de l’an 386 de l’Hégire, laissant derrière lui un patrimoine scientifique considérable qu’on évalue à environ quarante ouvrages, en les divers arts du savoir.</p>
<h3>Deuxièmement : l’importance du livre de la <em>Risāla</em> d’Ibn Abī Zayd</h3>
<p>Le livre de la <em>Risāla</em> compte parmi les plus importants ouvrages de l’imam Ibn Abī Zayd al-Qayrawānī : il reçut des savants une grande attention, car on ne connaît pas, en droit mālikite, après le <em>Muwaṭṭaʾ</em> et la <em>Mudawwana</em>, de livre qui ait obtenu ce qu’obtint la <em>Risāla</em> d’agrément, de soin, de renommée et d’expansion aux horizons — en enseignement, en commentaires et en gloses. Elle se distingua par la concision et la précision, et elle compte parmi les premières abréviations du droit mālikite. Elle contient quatre mille questions et quatre cents hadiths, ce qui témoigne, en faveur de son auteur, de l’excellence scientifique et de l’enracinement en le droit de l’école mālikite. Sa composition achevée, son auteur l’envoya au shaykh Abū Bakr al-Abharī, qui en fit voir sa joie, en répandit la nouvelle parmi les gens et ordonna de la vendre, disant : « On ne la vend que de son pesant d’or, poids pour poids » — et son pesant se monta à trois cents dinars et demi.</p>
<p>Le goût pour la <em>Risāla</em> s’est maintenu depuis sa composition jusqu’à notre époque, et elle fut traduite en deux langues : l’anglais et le français.</p>
<h2>L’évaluation (<em>taqwīm</em>)</h2>
<ul>
<li>Par quoi Ibn Abī Zayd al-Qayrawānī se distingua-t-il au cours de sa quête du savoir ?</li>
<li>Où apparaît l’importance scientifique de son livre la <em>Risāla</em> ?</li>
<li>Quelles sont les valeurs morales dont doit être doté l’étudiant en science ?</li>
</ul>
<h2>L’exploitation (<em>istithmār</em>)</h2>
<p>L’illustre savant (<em>al-ʿallāma</em>) ʿAlī al-Ṣaʿīdī al-ʿAdawī al-Mālikī dit, des mérites de l’imam Ibn Abī Zayd al-Qayrawānī : « Au nombre d’eux : son abondante mémorisation et sa religiosité, la perfection de sa scrupulosité (<em>waraʿ</em>) et de son détachement (<em>zuhd</em>) — Dieu l’ayant gratifié de trois choses : la santé du corps, et l’ampleur en science et en biens ; et quiconque lit son livre — celui-ci — et agit selon ce qu’il contient, il est inévitable que se trouve en lui l’ensemble de ces caractères ou une part d’eux. Il était surnommé le successeur de Mālik (<em>khalīfat Mālik</em>) et le petit Mālik (<em>Mālik al-aṣghar</em>) ; on disait de lui : le pivot de l’école (<em>quṭb al-madhhab</em>) ; il était doué de pénétration (<em>firmāsa</em>) : il lui arrivait de dire : “ Mon for intérieur m’a rapporté qu’en ce lieu il y a telle et telle question — lequel de vous en est l’auteur ? ” L’un disait : “ Moi ” — et il lui répondait. » [Ḥāshiya d’al-ʿAdawī sur la <em>Kifāyat al-ṭālib al-rabbānī</em> d’Abū l-Ḥasan sur la <em>Risāla</em> : 1/11]</p>
<p>Je lis le texte et réalise ce qui suit :</p>
<ul>
<li>Je présente Abū l-Ḥasan et ʿAlī al-ʿAdawī — que Dieu leur fasse miséricorde.</li>
<li>J’extrais les mérites de l’imam Ibn Abī Zayd al-Qayrawānī — que Dieu lui fasse miséricorde.</li>
<li>Je mets en relief son rang scientifique.</li>
</ul>
<h2>La préparation préalable (<em>iʿdād</em>)</h2>
<p>Je lis le <em>matn</em> de la leçon suivante et réalise ce qui suit :</p>
<ul>
<li>Je recherche la cause de la composition de la <em>Risāla</em>.</li>
<li>Je recherche, à travers le <em>matn</em>, les traits des meilleurs des cœurs.</li>
</ul>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "13978":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 13978 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 13978 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
