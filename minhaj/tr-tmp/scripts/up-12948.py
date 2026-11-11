#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12948 (hadith-1es, dispositions de
l'ouverture de la prière — Muwaṭṭaʾ n° 198, 206-208).

Conventions main (cf. 12875, 12884-12945 du même livre) :
- h1 « Les dispositions de l'ouverture de la prière (aḥkām iftitāḥ
  al-ṣalāh) », 15e leçon ; objectifs en infinitifs (source 1re personne).
- Muwaṭṭaʾ 198 (Ibn ʿUmar : élévation à hauteur des épaules à l'ouverture
  et à la relevée du rukūʿ + samiʿa Allāh…, pas dans la prosternation),
  206 (le maʾmūm qui oublie le takbīr d'entrée : recommencer lui est plus
  aimable ; le takbīr du rukūʿ suffit si visé comme ouverture), 208
  (l'imam qui oublie : il refait et les gens derrière refont), 207 (le
  solitaire : il recommence).
- Taḥlīl : jumhūr (recommandé) vs Awzāʿī/Ḥumaydī/Ibn Khuzayma/Dāwūd
  (obligation — Ibn ʿAbd al-Barr : shudhūd) ; Bājī/Lakhmī (permission) ;
  « la plus sûre des formules : Abū ʿUmar : consensus sur la permission » ;
  ḥadd al-rafʿ (mashhūr Mālik/Shāfiʿī : épaules ; Ashhab : poitrine ; Abū
  Ḥanīfa : oreilles — Muslim Mālik b. al-Ḥuwayrith + Wāʾil b. Ḥujr Abū
  Dāwūd ; réponse mālikite : tarjīḥ isnād Ibn ʿUmar + jamʿ paumes-épaules/
  bouts des doigts-oreilles) ; ḥāla (Sahnūn : dos des mains au ciel) ;
  zamān (concomitance — Shuʿayb/Zuhrī Bukhārī, Wāʾil ; Abū ʿAwāna :
  élévation puis takbīr ; Ḥuwayrith : takbīr puis élévation) ; sagesse
  (le sourd voit / l'aveugle entend ; rejeter le bas-monde ; Qurṭubī) ;
  Ibn ʿAbd al-Barr (magnification… ; Ibn ʿUmar « la parure de la prière ») ;
  rukūʿ : Ibn al-Qāsim (pas d'élévation hors iḥrām — Ibn Masʿūd Abū Dāwūd)
  vs Abū Muṣʿab/Ibn Wahb/Ashhab (élévation — avec Awzāʿī/Shāfiʿī/Aḥmad/
  Isḥāq/Ṭabarī) ; Muḥammad b. al-Ḥakam ; al-Aṣīlī (Nāfiʿ mawqūf) ;
  sujūd : pas d'élévation (Shuʿayb explicite) ; lever des deux rakʿa
  (Bukhārī ʿUbayd Allāh/Nāfiʿ, Abū Dāwūd Muḥārib ; attestations ʿAlī et
  Abū Ḥumayd — Ibn Khuzayma/Ibn Ḥibbān).
- VERSET restauré : Muhammad 47 : 33 « et n'annulez pas vos œuvres » —
  le manuel imprime « 34 » (le v. 34, sur les dénégateurs, est sans
  rapport avec le propos) ; doctrine R115 : contenu canonique + note.
- Lexique : ḥadw (« en face de »), mankibayhi, samiʿa Allāhu li-man
  ḥamidahu (samia = exaucer).
- Préparation préalable : leçon SUIVANTE 12953 (la lecture dans la
  prière) — qisār al-mufaṣṣal, yuraddiduhā.
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Les dispositions de l’ouverture de la prière (<em>aḥkām iftitāḥ al-ṣalāh</em>)</h1>
<p>Leçon sur les règles de l’ouverture de la prière, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la quinzième leçon.</p>
<ol>
<li>Connaître comment le Prophète — paix et bénédiction sur lui — ouvrait sa prière.</li>
<li>Saisir le statut de celui qui oublie le takbīr d’entrée en prière.</li>
<li>Éprouver le souci de conformer mes actes à ceux du Prophète — paix et bénédiction sur lui — dans ma prière.</li>
</ol>
<h2>Préambule</h2>
<p>Puisque la prière est le pilier de la religion et la meilleure des adorations, il nous faut, pour connaître ses règles et ses sagesses — de l’ouverture à la clôture —, nous appuyer sur les paroles et les actes du Prophète — paix et bénédiction sur lui.</p>
<p>Par quoi donc le Prophète — paix et bénédiction sur lui — ouvrait-il sa prière ? Et quelle est, en cela, la description préférée ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Ibn Shihāb, d’après Sālim ibn ʿAbd Allāh, d’après ʿAbd Allāh ibn ʿUmar : « que le Messager de Dieu — paix et bénédiction sur lui —, quand il ouvrait la prière, élevait ses deux mains à la hauteur de ses deux épaules ; et quand il relevait sa tête de l’inclinaison, il les élevait pareillement aussi, en disant : “Dieu entend celui qui Le loue — ô notre Seigneur, à Toi la louange” ; et il ne faisait pas cela dans la prosternation. » [Muwaṭṭaʾ, n° 198]</li>
<li>Yaḥyā a dit : on interrogea Mālik au sujet d’un homme qui entra [en prière] avec l’imam et oublia le takbīr d’ouverture et le takbīr de l’inclinaison, jusqu’à prier une rakʿa ; puis il se souvint qu’il n’avait fait ni le takbīr d’ouverture, ni celui de l’inclinaison, et fit le takbīr à la deuxième rakʿa. Il dit : « Que je vois qu’il recommence sa prière m’est plus aimable ; mais s’il fut distrait avec l’imam du takbīr d’ouverture et fit le takbīr à la première inclinaison, je l’ai estimé suffisant pour lui — pourvu qu’il y vît le takbīr d’ouverture. » [Muwaṭṭaʾ, n° 206]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>ḥadw</em> (« à la hauteur de ») : en face de, vis-à-vis.</li>
<li><em>mankibayhi</em> (« ses deux épaules ») : duel de <em>mankib</em> — l’assemblage de l’os du bras et de l’épaule.</li>
<li><em>samiʿa Allāhu li-man ḥamidahu</em> (« Dieu entend celui qui Le loue ») : <em>samiʿa</em> signifie ici « il exauce » ; le sens est : celui qui Le loue, en s’exposant à Sa récompense, Dieu — Exalté — l’exauce et lui donne ce à quoi il s’est exposé.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Extrais du premier hadith le statut du takbīr d’entrée et sa description.</li>
<li>Expose, à travers le deuxième hadith, le statut du suivi qui oublie le takbīr d’entrée.</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : le statut de l’élévation des mains au takbīr d’entrée</h3>
<p>Le hadith de ʿAbd Allāh ibn ʿUmar — « que le Messager de Dieu — paix et bénédiction sur lui —, quand il ouvrait la prière, élevait ses deux mains à la hauteur de ses deux épaules » — indique la légitimité de l’élévation des mains à l’ouverture de la prière ; mais les commentateurs du hadith divergèrent sur son statut, en deux avis :</p>
<ol>
<li>Le plus grand nombre tint qu’elle est recommandée.</li>
<li>Al-Awzāʿī, al-Ḥumaydī — le shaykh d’al-Bukhārī —, Ibn Khuzayma, Dāwūd et certains shāfiʿites et mālikites tinrent l’obligation. Ibn ʿAbd al-Barr a dit : tous ceux de qui l’on rapporta l’obligation [valident la prière :] la prière n’est pas invalidée par son délaissement, sauf en une narration d’al-Awzāʿī et d’al-Ḥumaydī — et c’est singularité et erreur.</li>
</ol>
<p>Al-Bājī rapporta de beaucoup de mālikites la permission, et al-Lakhmī la rapporta comme narration de Mālik ; aussi la plus sûre des formules est-elle la parole d’Abū ʿUmar [Ibn ʿAbd al-Barr] : « Les savants sont d’accord sur la permission d’élever les mains à l’ouverture de la prière. »</p>
<h3>Deuxièmement : la description de l’élévation des mains à l’ouverture de la prière, et sa sagesse</h3>
<h4>La description de l’élévation des mains à l’ouverture de la prière</h4>
<p>Ce point comprend trois choses :</p>
<h5>La limite de l’élévation</h5>
<p>L’avis répandu (<em>mashhūr</em>) de l’imam Mālik en cette question est qu’il élève ses mains jusqu’à ses épaules — et en cela dit al-Shāfiʿī : tel est le sens de sa parole dans le hadith : « il élevait ses deux mains à la hauteur de ses deux épaules ». Ashhab rapporta de Mālik qu’il les élève jusqu’à sa poitrine ; et Abū Ḥanīfa dit : il élève jusqu’à ses oreilles, arguant du hadith de Mālik ibn al-Ḥuwayrith : « que le Prophète — paix et bénédiction sur lui —, quand il priait, faisait le takbīr puis élevait [les mains] jusqu’à en aligner ses deux oreilles » [rapporté par Muslim — en une formule : « jusqu’à en aligner le haut de ses deux oreilles »] ; et d’Abū Dāwūd, d’après Wāʾil ibn Ḥujr : « jusqu’à ce qu’elles alignassent ses deux oreilles ». Les mālikites et leurs alliés répondirent à l’avis de l’adversaire par deux choses :</p>
<ul>
<li>La préférence : ils ont préféré le hadith d’Ibn ʿUmar à celui d’Ibn al-Ḥuwayrith, parce que son isnād est plus sain.</li>
<li>La conciliation des deux hadiths : ils ont dit : il alignait ses deux paumes à ses épaules, et les bouts de ses doigts à ses oreilles — ce qui concorde les deux hadiths et vaut mieux que d’abandonner l’un d’eux.</li>
</ul>
<h5>L’état de l’élévation</h5>
<p>Ce sur quoi sont le plus grand nombre des mālikites : que ses deux mains soient dressées, ses paumes alignant ses épaules et ses doigts ses oreilles. Il fut rapporté de Sahnūn qu’elles soient dressées verticalement — le dos des deux vers le ciel et les paumes vers la terre.</li>
<h5>Le moment de l’élévation</h5>
<p>L’élévation est concomitante du takbīr, et s’achève avec son achèvement — d’après la narration de Shuʿayb d’al-Zuhrī, en ce hadith, chez al-Bukhārī : « il élève ses deux mains quand il fait le takbīr » ; et Abū Dāwūd rapporta de Wāʾil ibn Ḥujr que le Prophète — paix et bénédiction sur lui — « éleva ses deux mains avec le takbīr ». La concomitance signifie qu’elle s’achève avec son achèvement — et tel est le plus solide chez les shāfiʿites et les mālikites. Il vint aussi [l’avis de] l’antériorité de l’élévation sur le takbīr, et l’inverse : ainsi, dans le <em>Musnad</em> d’Abū ʿAwāna, d’après la narration d’Ibn Jurayj et d’un autre, d’Ibn Shihāb, en la formule : « il éleva ses deux mains, puis fit le takbīr » ; et dans son hadith de Mālik ibn al-Ḥuwayrith : « il fit le takbīr, puis éleva ses deux mains ».</p>
<h4>La sagesse de l’élévation des mains à l’ouverture de la prière</h4>
<p>Un groupe de savants a dit : la sagesse qu’il y a à accoler l’élévation au takbīr, c’est que le sourd le voit et que l’aveugle l’entend ; il a été dit : l’indication du rejet du bas-monde et la conversion de tout l’être à l’adoration ; il a été dit : pour se tenir devant Lui de tout son corps — al-Qurṭubī a dit : c’est la plus ressemblante [des interprétations].</p>
<p>Et Ibn ʿAbd al-Barr a dit : le sens de l’élévation des mains, chez les gens de science, est magnification de Dieu, adoration de Lui, supplication vers Lui, soumission et abaissement en l’état de station entre Ses mains, et suivi de la sunna de Son Prophète — paix et bénédiction sur lui. Et Ibn ʿUmar avait coutume de dire : Toute chose a sa parure — et la parure de la prière est le takbīr et l’élévation des mains.</p>
<h3>Troisièmement : le statut de l’élévation des mains à l’inclinaison et à la prosternation</h3>
<h4>Le statut de l’élévation des mains à l’inclinaison</h4>
<p>On divergea sur la légitimité de l’élévation à l’inclinaison : Ibn al-Qāsim rapporta de Mālik qu’on n’élève pas hors de l’ouverture — et en cela dirent Abū Ḥanīfa et d’autres coufés, arguant du hadith d’Ibn Masʿūd : qu’il vit le Prophète — paix et bénédiction sur lui — « élever ses mains à l’ouverture, puis ne plus y revenir » [rapporté par Abū Dāwūd dans ses <em>Sunan</em>].</p>
<p>Et Abū Muṣʿab, Ibn Wahb, Ashhab et d’autres rapportèrent de Mālik qu’il élevait en s’inclinant et en relevant la tête de l’inclinaison — du fait de ce qui est venu dans le hadith d’Ibn ʿUmar : « et quand il relevait sa tête de l’inclinaison, il les élevait pareillement aussi » ; et en cela dirent al-Awzāʿī, al-Shāfiʿī, Aḥmad, Isḥāq, al-Ṭabarī et le groupe des gens du hadith.</p>
<p>Muḥammad ibn al-Ḥakam a dit : personne n’a rapporté de Mālik le délaissement de l’élévation en les deux, sinon Ibn al-Qāsim ; et ce dont nous prenons est l’élévation — pour le hadith d’Ibn ʿUmar. Al-Aṣīlī a dit : Mālik n’en a pas pris [l’autre version], parce que Nāfiʿ l’arrêta sur Ibn ʿUmar [seul].</p>
<h4>Le statut de l’élévation des mains à la prosternation</h4>
<p>La parole d’Ibn ʿUmar dans le hadith de la leçon — « et il ne faisait pas cela dans la prosternation » — indique que l’élévation des mains n’a pas lieu dans la prosternation : ni en s’y abaissant, ni s’en relevant — comme l’explicite la narration de Shuʿayb d’al-Zuhrī, en la formule : « ni quand il se prosterne, ni quand il relève sa tête ». Cela couvre le fait de se relever de la prosternation vers la deuxième et la quatrième [rakʿa] et les deux tashahhud, et couvre aussi le fait de se lever vers la troisième — mais sans tashahhud, parce qu’il n’est pas obligatoire : al-Bukhārī rapporta, de la narration de ʿUbayd Allāh d’après Nāfiʿ, et Abū Dāwūd, de la narration de Muḥārib ibn Dathār — l’un et l’autre d’Ibn ʿUmar — : « que le Prophète — paix et bénédiction sur lui —, quand il se levait des deux rakʿa, faisait le takbīr et élevait ses deux mains » ; et cela a ses attestations du hadith d’ʿAlī et d’Abū Ḥumayd al-Sāʿidī [rapportés par Abū Dāwūd, et authentifiés par Ibn Khuzayma et Ibn Ḥibbān].</p>
<h3>Quatrièmement : le statut du suivi qui oublie le takbīr d’entrée</h3>
<p>Si le suivi oublie le takbīr d’entrée, il recommence sa prière dès qu’il s’en souvient : car il n’y a pas de divergence qu’il n’est pas entré en prière — l’intention d’y entrer et sa formule ne se trouvant pas chez lui. Dès qu’il s’en souvient, il est comme celui qui rejoint l’imam en ce moment : il lui incombe de commencer la prière. S’il fait le takbīr pour l’inclinaison en y visant le takbīr d’ouverture, cela lui suffit ; mais s’il a fait le takbīr de l’inclinaison de la première rakʿa sans y viser l’ouverture — poursuit-il la prière, ou la recommence-t-il ?</p>
<p>De Mālik en cela, deux narrations : la première — qu’il la recommence ; la seconde — qu’il la poursuit et la refait. Le fondement de la première : c’est une prière qui ne lui suffit pas, et dont l’obligation n’est pas acquittée par elle — il ne la poursuit donc pas, comme s’il n’avait pas fait le takbīr de l’inclinaison ; autre fondement : s’il la poursuit, la prière en commun lui échappe, puis il accomplplit la prière en solitaire alors qu’il pouvait obtenir le mérite du groupe.</p>
<p>Et le fondement de la seconde — l’argument dont s’appuya Mālik : c’est une prière disputée, car Ibn Shihāb tient qu’elle lui suffit, et Rabīʿa dit qu’elle ne lui suffit pas : il a donc noué une rakʿa d’une prière disputée — et il répugne [à Mālik] d’invalider sa prière, et c’est un acte dont les savants ont divergé sur la suffisance, selon la parole de Dieu — Exalté :</p>
<p>« Ô vous qui croyez ! obéissez à Dieu et obéissez au Messager, et n’annulez pas vos œuvres. » (Muhammad, 47 : 33 — le manuel imprime « 34 »)</p>
<p>[Verset restauré d’après le corpus canonique : l’emplacement imprimé correspondant est vide dans la source numérisée — perte OCR. Le verset 34 imprimé, sur les dénégateurs, est sans rapport avec le propos.]</p>
<p>Et le meilleur est qu’il poursuive, puis la refasse — réunissant ainsi les deux avis.</p>
<h2>L’évaluation</h2>
<ol>
<li>Quel est le statut de l’élévation des mains au takbīr d’entrée ?</li>
<li>Expose la description de l’élévation des mains à l’ouverture de la prière.</li>
<li>Parle du statut du suivi s’il oublie le takbīr d’entrée.</li>
</ol>
<h2>L’exploitation</h2>
<p>Mālik dit, au sujet de l’imam qui oublie le takbīr d’ouverture jusqu’à s’acquitter de sa prière : « Je vois qu’il refait, et que refassent la prière ceux qui étaient derrière lui — quand bien même ceux [qui étaient] derrière lui avaient fait le takbīr, ils refont. » [Muwaṭṭaʾ, n° 208]</p>
<p>Yaḥyā a dit : Mālik dit, au sujet de celui qui prie pour soi-même et délaisse le takbīr d’ouverture en faisant le takbīr pour l’inclinaison : « Qu’il recommence sa prière. » [Muwaṭṭaʾ, n° 207]</p>
<ul>
<li>Quel est le rapport de ces athars aux deux hadiths de la leçon ?</li>
<li>Expose le statut de l’oubli du takbīr d’entrée par l’imam.</li>
<li>Que fait celui qui prie seul s’il délaisse le takbīr d’ouverture et fait le takbīr de l’inclinaison ?</li>
</ul>
<h2>La préparation préalable</h2>
<ol>
<li>Explique : <em>qisār al-mufaṣṣal</em> (« les courtes [sourates] de la fin du Coran ») – <em>yuraddiduhā</em> (« qu’il la répète »).</li>
<li>Extrais des hadiths de la leçon ce que le Prophète — paix et bénédiction sur lui — récitait dans sa prière.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12948":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12948 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12948 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
