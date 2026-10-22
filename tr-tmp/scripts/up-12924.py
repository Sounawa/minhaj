#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12924 (hadith-1es, règles de l'urine
du petit et de l'adulte — Muwaṭṭaʾ n° 167-170).

Conventions main (cf. 12875, 12884-12911 du même livre) :
- h1 « Dispositions pour l'urine des garçons et des adultes », 12e leçon ;
  objectifs en infinitifs (source 1re personne أن أتعرف).
- Muwaṭṭaʾ 167 (Umm Qays bt. Miḥṣan : petit garçon pas encore nourri,
  lappe du Prophète, nadaḥ sans lavage), 169 (Ibn Dīnār : Ibn ʿUmar pissait
  debout), 170 (Mālik : les anciens faisaient wuḍūʾ du ghāʾiṭ ; « j'aime
  laver le sexe de l'urine »), 168 (l'A'rābī dans la mosquée : « laissez-le »
  + dhanūb d'eau versé).
- Taḥlīl I : 3 écoles (mashhūr Mālik/Abū Ḥanīfa : lavage obligatoire —
  qiyās + consensus après sevrage ; réponse au naḍḥ = ghisl chez les Arabes,
  ḥadīth ʿUmān de Bayhaqī ; Awzāʿī : aspersion suffit, Ibn al-ʿArabī
  restreint au jeûne absolu).
- Taḥlīl II : Ibn ʿUmar/Zayd b. Thābit/Ibn Sīrīn/Nakhaʿī/Aḥmad vs jumhūr
  (karāha tanẓīhiyya) vs Mālik (éclaboussure) ; Hudhayfa Ṣaḥīḥayn (subāṭa —
  Ibn Ḥibbān : pas de place pour s'asseoir + terre meuble ; plus apparent :
  bayān al-jawāz) ; ʿĀʾisha (Abū ʿAwāna/Ḥākim/Tirmidhī) vs non-abrogation —
  « son hadith repose sur sa connaissance » → maisons de Médine.
- Taḥlīl III : ghusl > istijmār/istibrāʾ ; l'urine liquide s'étend → eau ;
  athar des gens de Qubāʾ → VERSET restauré : al-Baqara 2 : 222, extrait
  (« Dieu aime ceux qui reviennent… ») — le manuel imprime « 220 »
  (numérotation maghrébine, cf. 12884 du même livre).
- Lexique : ḥajr (lappe), naḍḥ (asperger), ghāʾiṭ (lieu bas → excrément),
  wuḍūʾ du ghāʾiṭ (lavage de l'anus).
- Préparation préalable : leçon SUIVANTE 12929 (adhān) — khashabatayn
  (nāqūs : deux bois), ḍirāṭ (petit vent — hadith Abū Hurayra « le diable
  recule d'un ḍirāṭ »), thawb bi-l-ṣalāh (iqāma — de thāba « revenir »),
  yakhṭir (s'insinuer entre l'homme et son âme).
- Artéfact CMS « الإثنين 25 مارس 2019 » dans le dl : ignoré.
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Dispositions pour l’urine des garçons et des adultes (<em>aḥkām bawl al-ṣabī wa-l-kabīr</em>)</h1>
<p>Leçon sur les règles de l’urine du petit enfant et de l’adulte, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la douzième leçon.</p>
<ol>
<li>Connaître les règles de l’urine du petit et de l’adulte.</li>
<li>Saisir certains cas où l’urine du petit garçon n’est pas tenue pour impure.</li>
<li>Éprouver le souci d’écarter l’impureté.</li>
</ol>
<h2>Préambule</h2>
<p>L’islam a tenu la propreté pour une part de la foi : c’est pourquoi il a ordonné au musulcroyant de se garder de l’urine, d’en prendre son assurance (<em>istibrāʾ</em>) et de s’en purifier avec l’eau. Il faut donc user de précaution à l’égard de l’impureté de l’urine, qu’elle vienne du petit enfant ou de l’adulte.</p>
<p>Quel est donc le statut de l’urine du petit enfant ? Et est-il permis à l’homme d’uriner debout ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Ibn Shihāb, d’après ʿUbayd Allāh ibn ʿAbd Allāh ibn ʿUtba ibn Masʿūd, d’après Umm Qays bint Miḥṣan : « qu’elle vint trouver le Messager de Dieu — paix et bénédiction sur lui — avec un jeune fils d’elle qui n’avait pas encore mangé d’aliment ; il l’assit sur ses genoux, et il urina sur son vêtement. “Le Messager de Dieu — paix et bénédiction sur lui — appela alors de l’eau, l’en aspergea, et ne le lava pas.” » [Muwaṭṭaʾ, n° 167]</li>
<li>D’après Mālik, d’après ʿAbd Allāh ibn Dīnār : « qu’il dit : J’ai vu ʿAbd Allāh ibn ʿUmar “uriner debout”. » [Muwaṭṭaʾ, n° 169]</li>
<li>Yaḥyā a dit : on interrogea Mālik au sujet du lavage du sexe après l’urine et les selles — y a-t-il en la matière quelque transmission ? Il dit : « Il m’est parvenu que certains de ceux qui ont passé [avant nous] faisaient leurs ablutions après les selles ; et quant à moi, j’aime à laver le sexe de l’urine. » [Muwaṭṭaʾ, n° 170]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>fa-ajlasahu fī ḥajarihi</em> (« il l’assit sur ses genoux ») : il le plaça sur ses genoux.</li>
<li><em>fa-naḍghu</em> (« il en aspergea ») : verser l’eau dessus.</li>
<li><em>al-ghāʾiṭ</em> : au sens propre, le lieu bas et enfoncé ; ce qui est visé, c’est l’excrément qui sort de l’anus de l’homme.</li>
<li><em>yatawaḍḍaʾūna mina l-ghāʾiṭ</em> (« ils faisaient leurs ablutions après les selles ») : ils lavaient l’anus.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Expose, d’après le premier hadith, le statut de l’urine du petit garçon.</li>
<li>Extrais du deuxième hadith le statut de l’urine debout.</li>
<li>Comment s’accomplit la purification de l’urine et des selles ?</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : le statut de l’urine du petit garçon et de la petite fille</h3>
<p>Les savants divergèrent sur le statut de l’urine du petit garçon et de la petite fille, en trois écoles, parmi lesquelles :</p>
<ol>
<li>L’obligation de laver [le lieu atteint par] l’urine du petit garçon et de la petite fille — c’est l’avis répandu (<em>mashhūr</em>) de Mālik et d’Abū Ḥanīfa et de leurs partisans, et un groupe l’a dit. Les ḥanafites et les mālikites ont argumenté que le lavage, en l’un et l’autre cas, est l’analogie et la règle originaire de l’élimination de l’impureté — et l’analogie du petit garçon sur la petite fille, du fait de l’accord des savants sur l’égalité du statut en les deux après qu’ils ont mangé autre chose que le lait : le lavage de leur urine est alors un consensus. Et ils répondirent au hadith de la leçon par de nombreuses réponses, parmi lesquelles : ce que vise ici l’aspergement (<em>naḍḥ</em>) est le lavage — sens bien connu dans la langue des Arabes ; d’où le hadith où le Messager de Dieu — paix et bénédiction sur lui — a dit : « Je connais une terre qu’on appelle ʿUmān, dont le flanc est baigné par la mer : y vit une tribu des Arabes qui, si mon messager leur venait, ne lui jetterait ni flèche ni pierre. » [Rapporté par al-Bayhaqī dans ses <em>Sunan</em>]</li>
<li>L’aspergement suffit en les deux — école d’al-Awzāʿī, rapportée aussi de Mālik et d’al-Shāfiʿī ; et Ibn al-ʿArabī restreignit cette attribution au cas où rien n’était encore entré dans leur ventre.</li>
</ol>
<h3>Deuxièmement : le statut de l’urine debout</h3>
<p>On divergea sur le statut de l’urine debout — entre le permis sans condition, le permis restreint et la répugnance ; l’explication en voici :</p>
<ul>
<li>L’école de ʿAbd Allāh ibn ʿUmar, de Zayd ibn Thābit, d’Ibn al-Musayyab, d’Ibn Sīrīn, d’al-Nakhaʿī et d’Aḥmad : la permission d’uriner debout, sans répugnance.</li>
<li>La généralité des savants l’a réprouvée par voie d’avoidance (répugnance <em>tanẓīhiyya</em>).</li>
<li>Mālik a dit : si c’est en un lieu d’où rien ne peut rejaillir sur lui, il n’y a pas de mal ; sinon, c’est réprouvé. Dans les deux <em>Ṣaḥīḥ</em> et ailleurs, d’après Hudhayfa : « le Prophète — paix et bénédiction sur lui — vint à un dépôt d’ordures (<em>subāṭa</em>) de gens, et urina debout. » Ibn Ḥibbān [en donna la raison] : parce qu’il ne trouva aucune place propice à s’asseoir — il se tint donc debout, la part du dépôt qui lui échue étant pour l’essentiel [meuble], à l’abri de ce que rien de son urine ne rejaillît sur lui ; et l’on a dit : parce que le dépôt (balayures et ordures des maisons) est meuble, que l’urine y pénètre — rien de son urine ne rejaillissant alors sur celui qui urine. Et le plus apparent est qu’il fit cela pour faire connaître la permission — la plus grande part de ses états étant d’uriner assis. Abū ʿAwāna et Ibn Shāhīn ont prétendu que l’urine debout est abrogée, arguant du hadith d’ʿĀʾisha : « Il n’urina jamais debout après que le Coran lui fut descendu » [rapporté par Abū ʿAwāna et al-Ḥākim], et de son hadith pareillement : « Quiconque vous dit qu’il urinait debout, ne le croyez pas : il n’urinait qu’assis. » [Rapporté par al-Tirmidhī dans ses <em>Sunan</em>] — et l’avis fondé est qu’il n’y a pas d’abrogation : le hadith d’ʿĀʾisha repose sur sa science, et se rapporte à ce qui se produisit de lui dans les maisons — elle n’avait pas connaissance de son urine debout ; or Hudhayfa l’a conservé en mémoire, lui qui est des plus grands des Compagnons, et cela fut à Médine : cela renferme donc la réplique à ce qu’elle a nié, à savoir que cela ne se produisit pas après la descente du Coran. Et il est établi de ʿUmar et de son fils, d’ʿAlī, de Zayd ibn Thābit et d’autres qu’ils urinèrent debout — ce qui indique la permission, sans répugnance, quand on est à l’abri du rejaillissement ; et rien ne s’établit du Prophète — paix et bénédiction sur lui — qui interdise cela.</li>
</ul>
<h3>Troisièmement : la méthode de purification de l’urine et des selles</h3>
<p>Il est su des juristes que le lavage après l’urine et les selles est préférable à l’usage de pierres (<em>istijmār</em>) et à la précaution (<em>istibrāʾ</em>). On interrogea Mālik au sujet du lavage du sexe après l’urine et les selles — y a-t-il en la matière quelque transmission ? Il dit : Il m’est parvenu que certains de ceux qui ont passé [avant nous] faisaient leurs ablutions après les selles ; et quant à moi, j’aime à laver le sexe de l’urine. L’imam Mālik a réservé le lavage du sexe à l’eau parce que l’urine est fluide et n’échappe guère à se répandre — c’est pourquoi il la jugea plus digne qu’on y emploie l’eau. Et il se peut que Mālik ait su qu’il détenait une transmission au sujet du lavage du sexe après les selles, et que le lavage du sexe de l’urine soit recommandé : il exposa donc ce sur quoi il avait une transmission, et le distingua de ce à quoi il inclinait par une sorte de réflexion. Il est rapporté, dans le récit des gens de Qubāʾ, qu’ils faisaient leurs ablutions après les selles avec l’eau — et c’est à leur sujet que fut descendue la parole de Dieu — Exalté et Magnifié :</p>
<p>« …Dieu aime ceux qui reviennent [à Lui] et aime ceux qui se purifient. » (al-Baqara, 2 : 222, extrait — le manuel imprime « 220 »)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR. Numérotation maghrébine du manuel, en cohérence avec la leçon 12884 du même livre.]</p>
<h2>L’évaluation</h2>
<ol>
<li>Cite les paroles des juristes et leurs preuves au sujet du statut de l’urine du petit garçon.</li>
<li>Quel est le statut de l’urine debout ?</li>
<li>Quelle est la manière préférée de se purifier de l’urine et des selles ?</li>
</ol>
<h2>L’exploitation</h2>
<p>D’après Mālik, d’après Yaḥyā ibn Saʿīd : « qu’il dit : Un bédouin entra dans la Mosquée et découvrit son sexe pour uriner ; les gens l’apostrophèrent, jusqu’à ce que la voix montât. Le Messager de Dieu — paix et bénédiction sur lui — dit : “Laissez-le !” Ils le laissèrent, et il urina. Puis le Messager de Dieu — paix et bénédiction sur lui — ordonna un seau d’eau, qu’on versa sur cet endroit. » [Muwaṭṭaʾ, n° 168]</p>
<p>Lis le hadith et réponds à ce qui suit :</p>
<ol>
<li>Pourquoi les gens crièrent-ils au visage du bédouin ?</li>
<li>Comment le Prophète — paix et bénédiction sur lui — s’y prit-il avec le bédouin ?</li>
<li>Expose ce que le hadith montre de la miséricorde du Messager envers ce Compagnon.</li>
</ol>
<h2>La préparation préalable</h2>
<ol>
<li>Explique : <em>khashabatayn</em> (« les deux pièces de bois » — le <em>nāqūs</em>) – <em>ḍirāṭ</em> (« le petit vent ») – <em>thawb bi-l-ṣalāh</em> (« l’iqāma de la prière ») – <em>yakhṭir</em> (« qu’il s’insinue »).</li>
<li>Extrais des hadiths la légitimité de l’appel à la prière et ses mérites.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12924":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12924 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12924 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
