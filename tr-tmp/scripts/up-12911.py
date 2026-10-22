#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12911 (hadith-1es, règles des menstrues
et de la métrorragie — Muwaṭṭaʾ n° 148, 152, 153, 158-160, 163, 164).

Conventions main (cf. 12875, 12884-12908 du même livre) :
- h1 « Les règles des menstrues et de la métrorragie (aḥkām al-ḥayḍ
  wa-l-istiḥāḍa) », 11e leçon ; objectifs en infinitifs (le source imprime
  « أن أتعرف » etc., 1re personne).
- Muwaṭṭaʾ 148 (Zayd b. Aslam : « qu'elle noue son izār… le haut t'est
  licite »), 152 (ʿAlqama/ʿĀʾisha : daraja + kursuf, « ne vous hâtez pas
  jusqu'à la qaṣṣa blanche »), 160 (Umm Salama : la femme qui "versait le
  sang" — compter les nuits/jours, laver, istithfār, prier), 159 (Fāṭima bt.
  Abī Ḥubaysh : « ce n'est qu'une veine »), 163 (un seul ghusl + wuḍūʾ par
  prière — jumhūr : obligation ; Mālik : recommandation), 164 (l'époux après
  la prière), 158 (Asmāʾ : frotter puis rincer), 153 (fille de Zayd b.
  Thābit blâme les lampes nocturnes).
- Ṣaḥīḥayn ʿĀʾisha (izār au fort du ḥayḍ + « qui de vous maîtrise son
  irb comme le Prophète maîtrisait son irb ») ; Bukhārī Ibn ʿAbbās
  (« la prière est plus grande »).
- Lexique : izār, daraja (kasre dāl/fatha rāʾ-jīm, pl. de darj), kursuf,
  qaṣṣa bayḍāʾ (eau blanche, cf. qaṣṣ = chaux), tuhāraq al-dimāʾ, khalafat
  (khāʾ pointé), istithfār (bourrer + nouer).
- Taḥlīl : Azharī/Harawī (définitions ḥayḍ vs istiḥāḍa — fond vs veine du
  col), jufūf vs qaṣṣa (l'existence plus probante que l'absence), jumhūr
  (interdit nombril-genoux), grossesse : mashhūr Mālik/ Jadīd Shāfiʿī vs
  Abū Ḥanīfa/Aḥmad/Thawrī (istibrāʾ — le rare n'infirme pas le dominant),
  istithār, ijmāʿ sukūtī (ʿĀʾisha : « qu'elle délaisse la prière »).
- « أراد… أن يباشرها » : le sujet (رَسُولُ الله) manque dans l'OCR —
  restitué d'après Ṣaḥīḥayn ; « اقرئي » imprimé « اقرأ (ئي) ».
- Préparation préalable : leçon SUIVANTE 12924 (urine du petit et du
  grand — fanaḍugh, al-ghāʾiṭ, yatawaḍḍaʾūna).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Les règles des menstrues et de la métrorragie (<em>aḥkām al-ḥayḍ wa-l-istiḥāḍa</em>)</h1>
<p>Leçon sur les règles des menstrues et de la métrorragie, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la onzième leçon.</p>
<ul>
<li>Connaître ce qui est licite à l’homme de son épouse lorsqu’elle est menstruée.</li>
<li>Distinguer le sang des menstrues du sang de la métrorragie (<em>istiḥāḍa</em>).</li>
<li>Éprouver le dessein de la sollicitude de la Loi pour la purification à l’égard des menstrues.</li>
</ul>
<h2>Préambule</h2>
<p>Au nombre des questions propres aux femmes sont le sang des menstrues, celui de la métrorragie et celui des lochies (<em>nifās</em>) ; et le Noble Coran ainsi que la Sunna prophétique ont exposé l’ensemble des règles qui en découlent.</p>
<p>Qu’est-ce à dire des menstrues et de la métrorragie ? Et quels sont les règles de chacune ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Zayd ibn Aslam : « qu’un homme interrogea le Messager de Dieu — paix et bénédiction sur lui — en disant : Que m’est-il licite de mon épouse tandis qu’elle est menstruée ? Le Messager de Dieu — paix et bénédiction sur lui — dit : “Qu’elle noue sur elle son pagne (<em>izār</em>), puis qu’il t’en aille du haut de son corps.” » [Muwaṭṭaʾ, n° 148]</li>
<li>D’après Mālik, d’après ʿAlqama ibn Abī ʿAlqama, d’après sa mère, affranchie de ʿĀʾisha, mère des croyants : « qu’elle dit : Les femmes envoyaient à ʿĀʾisha le plateau (<em>daraja</em>) contenant le coton (<em>kursuf</em>) marqué de jaunâtre par le sang des menstrues, pour l’interroger au sujet de la prière. Elle leur disait : Ne vous hâtez pas, jusqu’à ce que vous voyiez l’écoulement blanc (<em>qaṣṣa bayḍāʾ</em>) — voulant par là la purification des menstrues. » [Muwaṭṭaʾ, n° 152]</li>
<li>D’après Mālik, d’après Nāfiʿ, d’après Sulaymān ibn Yasār, d’après Umm Salama, épouse du Prophète — paix et bénédiction sur lui : « qu’une femme, au temps du Messager de Dieu — paix et bénédiction sur lui —, versait le sang [à flots] ; Umm Salama consulta pour elle le Messager de Dieu — paix et bénédiction sur lui —, et il dit : “Qu’elle considère le nombre de nuits et de jours qu’elle avait coutume d’être menstruée chaque mois, avant que ne la frappe ce qui l’a frappée ; qu’elle délaisse la prière pour cette part du mois ; puis, quand elle l’aura passé derrière elle, qu’elle se lave, qu’elle se bande d’un tissu, puis qu’elle prie.” » [Muwaṭṭaʾ, n° 160]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>izāruhā</em> (« son pagne ») : ce dont elle se ceint le milieu du corps.</li>
<li><em>al-daraja</em> (« le plateau ») : avec kasre du <em>dāl</em>, fatha du <em>rāʾ</em> et du <em>jīm</em> — pluriel de <em>darj</em> (avec ḍamma puis sukūn) ; il vise un petit récipient, ou un chiffon.</li>
<li><em>al-kursuf</em> (« le coton ») : avec ḍamma du <em>kāf</em> et du <em>sīn</em> (non pointé), séparés d’un <em>rāʾ</em> quiescent, puis <em>fāʾ</em> : la ouate de coton.</li>
<li><em>al-qaṣṣa al-bayḍāʾ</em> (« l’écoulement blanc ») : avec fatha du <em>qāf</em> et shadda du <em>ṣād</em> (non pointé) : une eau blanche que l’utérus chasse au moment où les menstrues tarissent ; l’écoulement fut semblé, pour sa blancheur, à la chaux (<em>qaṣṣ</em>) — d’où « il enduisit sa maison » (<em>qaṣṣa dārahu</em>) : il la crépit à la chaux.</li>
<li><em>tuhāraq al-dimāʾ</em> (« versait le sang ») : avec ḍamma du <em>tāʾ</em> et fatha du <em>hāʾ</em> — l’abondance du sang chez elle, comme si elle le répandait.</li>
<li><em>fa-idhā khalafat dhālika</em> (« quand elle l’aura passé derrière elle ») : avec fatha du <em>khāʾ</em> (pointé), du <em>lām</em> appuyé et du <em>fāʾ</em> — c’est-à-dire : elle laissa derrière elle les jours des menstrues qu’elle connaissait par habitude.</li>
<li><em>tastathfir</em> (« qu’elle se bande ») : c’est-à-dire qu’elle serre son sexe d’un tissu, après s’être bourré de coton, et qu’elle attache les deux bouts du tissu à ce dont elle se ceint le milieu — arrêtant par là l’écoulement du sang.</li>
</ul>
<h3>Extraction des contenus</h3>
<ol>
<li>Détermine ce qui est licite à l’homme de son épouse pendant les menstrues.</li>
<li>Déduis des hadiths la marque de la purification de la femme au sortir des menstrues.</li>
<li>Quelle est la différence entre les menstrues et la métrorragie ?</li>
</ol>
<h2>L’analyse</h2>
<h3>Premièrement : le concept des menstrues, et la marque de la purification au sortir d’elles</h3>
<h4>Le concept des menstrues</h4>
<p>Al-Azharī, al-Harawī et d’autres ont dit : les menstrues (<em>ḥayḍ</em>) sont l’écoulement du sang de la femme en des temps connus, que relâche le fond de son utérus après qu’elle a atteint la puberté.</p>
<p>Quant à la métrorragie (<em>istiḥāḍa</em>) : c’est l’écoulement de ce sang hors de sa saison — il s’écoule d’une veine située dans le bas de l’utérus, et non de son fond. On dit : la femme fut atteinte de métrorragie (au passif) : elle est alors <em>mustaḥāḍa</em>.</p>
<h4>La marque de la purification au sortir des menstrues</h4>
<p>La marque de la purification de la menstruée est l’une de deux choses :</p>
<ul>
<li>le tarissement (<em>jufūf</em>) : la femme introduit le coton ou le chiffon dans son vagin, et il ressort sec, sans rien de sang sur lui ;</li>
<li>l’écoulement blanc (<em>qaṣṣa bayḍāʾ</em>) : une eau blanche que l’utérus chasse quand les menstrues tarissent — marque plus forte que le tarissement : car le tarissement est une absence, et l’écoulement une présence, et la présence est plus probante que l’absence ; l’utérus peut tarir au beau milieu des menstrues, et la menstruée se laver, et son utérus rester sec une heure — tandis que l’écoulement blanc n’est jamais que pureté. L’atteste la parole de la mère des croyantes ʿĀʾisha — que Dieu soit satisfait d’elle — aux femmes qui lui envoyaient le plateau avec le coton marqué de jaunâtre par le sang des menstrues, pour l’interroger sur la prière : « Ne vous hâtez pas, jusqu’à ce que vous voyiez l’écoulement blanc. »</li>
</ul>
<h3>Deuxièmement : ce qui est licite à l’homme de son épouse tandis qu’elle est menstruée</h3>
<p>La parole du Messager de Dieu — paix et bénédiction sur lui —, « Qu’elle noue sur elle son pagne, puis qu’il t’en aille du haut de son corps », indique que le coït est interdit pendant les menstrues — point d’accord entre les juristes —, et qu’il est permis de jouir (<em>istimtāʿ</em>) de la menstruée ; mais ils divergèrent sur les limites de cette jouissance, en plusieurs avis : l’école du plus grand nombre — parmi lesquels les trois imams Mālik, al-Shāfiʿī et Abū Ḥanīfa — interdit de jouir de ce qui est entre le nombril et les genoux, par coït ou autrement. Dans les deux <em>Ṣaḥīḥ</em>, d’après ʿĀʾisha — que Dieu soit satisfait d’elle — : « Quand l’une de nous était menstruée et que le Messager de Dieu — paix et bénédiction sur lui — voulait l’étreindre, il lui ordonnait de se ceindre d’un pagne au fort de ses menstrues, puis il l’étreignait. Elle dit : Et qui d’entre vous peut maîtriser son ardeur (<em>irb</em>) comme le Prophète — paix et bénédiction sur lui — maîtrisait son ardeur ? » [Rapporté par al-Bukhārī et Muslim dans leurs deux <em>Ṣaḥīḥ</em>] ; et ils portèrent le hadith d’ʿĀʾisha des deux <em>Ṣaḥīḥ</em> et celui du <em>Muwaṭṭaʾ</em> sur la recommandation — pour accorder ensemble les preuves.</p>
<h3>Troisièmement : la femme enceinte est-elle menstruée ?</h3>
<p>Les juristes divergèrent sur le sang que voit la femme enceinte : compte-t-il pour sang de menstrues, ou non ? Deux écoles :</p>
<ul>
<li>Ibn al-Musayyab, Ibn Shihāb, Mālik selon l’avis répandu, al-Shāfiʿī dans le <em>Jadīd</em> et d’autres tinrent que la femme enceinte est menstruée ; ils argumentèrent de ce que rapporta l’imam Mālik : qu’il lui parvint qu’ʿĀʾisha dit, au sujet de la femme enceinte qui voit le sang : « Qu’elle délaisse la prière » — et personne ne désavoua sa parole : ce fut donc un consensus tacite. Ils dirent [pareillement] : s’il est admis que les lochies aillent de pair avec la grossesse — lorsqu’un des jumeaux se fait tard —, il en va de même des menstrues.</li>
<li>Abū Ḥanīfa et ses compagnons, Aḥmad et al-Thawrī tinrent qu’elle n’est pas menstruée ; le plus fort de leurs arguments : les menstrues sont une marque de la vacuité de l’utérus pour l’assurance de non-grossesse (<em>istibrāʾ</em>) — or, si la femme enceinte était menstruée, cette assurance ne serait pas acquise par les menstrues.</li>
</ul>
<p>On y répondit : cette marque de la vacuité de l’utérus vaut selon la dominante des cas ; et les menstrues de la femme enceinte sont rares — et le rare n’est pas infirmé par le dominant. [Le rare n’infirme pas le dominant.]</p>
<h3>Quatrièmement : les règles de la femme en métrorragie</h3>
<p>Lorsque le sang descend de la femme en ses jours habituels, elle est menstruée ; mais il arrive que le temps coutumier des menstrues s’achève sans que le sang cesse : on l’appelle alors <em>mustaḥāḍa</em>, et celle-ci a ses règles propres, parmi lesquelles :</p>
<ol>
<li>La prière : il est su que la menstruée délaisse la prière ; mais quand le temps des menstrues est achevé — ayant poussé à bout sa coutume (<em>istithār</em>) — et que le sang continue de descendre d’elle, elle est en métrorragie : il lui incombe de se laver, de poser un chiffon sur son sexe et de prier, car la métrorragie n’empêche pas la prière — d’après ce que rapporta l’imam Mālik dans le <em>Muwaṭṭaʾ</em>, d’après Hishām ibn ʿUrwa, d’après son père, d’après ʿĀʾisha, épouse du Prophète — paix et bénédiction sur lui : « qu’elle dit : Fāṭima bint Abī Ḥubaysh dit : Ô Messager de Dieu, je ne suis jamais pure — dois-je délaisser la prière ? Le Messager de Dieu — paix et bénédiction sur lui — lui dit : “Ce n’est là qu’une veine, et non les menstrues : quand les menstrues surviennent, délaisse la prière ; et quand elles ont fui leur mesure, lave de toi le sang, et prie.” » [Muwaṭṭaʾ, n° 159]</li>
<li>Les ablutions : on divergea sur la femme en métrorragie : lui incombe-t-il de faire ses ablutions pour chaque prière, ou non ? Le plus grand nombre dit : obligation ; Mālik dit : recommandation. Preuve en est ce qui fut rapporté de Mālik, d’après Hishām ibn ʿUrwa, d’après son père, qui dit : « Il n’y a sur la femme en métrorragie rien d’autre que de se laver d’un seul lavage, puis de faire ses ablutions après cela pour chaque prière. » [Muwaṭṭaʾ, n° 163]. Cela montre donc que, lorsque le temps de ses menstrues est achevé — ayant poussé à bout sa coutume —, il lui incombe de se laver et de prier ; et, puisque le sang descend encore d’elle, elle doit faire ses ablutions chaque fois qu’elle veut prier. Mais ils divergèrent sur le sens de l’impératif dans sa parole : « puis de faire ses ablutions après cela pour chaque prière » : le plus grand nombre le porta sur l’obligation, et l’imam Mālik sur la recommandation.</li>
<li>Le coït : il est permis à l’époux de la femme en métrorragie de la connaîdre, selon la parole de Mālik : « La chose chez nous est que, lorsque la femme en métrorragie a prié, son époux peut la connaître. » [Muwaṭṭaʾ, n° 164] — et en cela l’avis du plus grand nombre des savants. Et dans [le <em>Ṣaḥīḥ</em> d’]al-Bukhārī, d’après Ibn ʿAbbās : « Son époux la connaît lorsqu’elle a prié : la prière est plus grande. » Mālik a dit : le Messager de Dieu — paix et bénédiction sur lui — a dit : « Ce n’est là qu’une veine, et non les menstrues » — quand ce ne sont pas les menstrues, qu’est-ce qui l’empêcherait de la connaître, alors qu’elle a reçu l’ordre de prier ?</li>
</ol>
<h2>L’évaluation</h2>
<ol>
<li>Qu’est-ce qui est licite à l’homme de son épouse quand elle est menstruée ?</li>
<li>Précise la différence entre les menstrues et la métrorragie.</li>
<li>Expose les règles de la femme en métrorragie quant à la prière et au coït.</li>
</ol>
<h2>L’exploitation</h2>
<p>D’après Mālik, d’après Hishām ibn ʿUrwa, d’après son père, d’après Fāṭima bint al-Mundhir ibn al-Zubayr, d’après Asmāʾ bint Abī Bakr al-Ṣiddīq : « qu’elle dit : Une femme interrogea le Messager de Dieu — paix et bénédiction sur lui — et dit : Que dire de l’une de nous quand le sang des menstrues atteint son vêtement — que doit-elle faire ? Le Messager de Dieu — paix et bénédiction sur lui — dit : “Quand le sang des menstrues atteint le vêtement de l’une de vous, qu’elle l’y frotte, puis l’asperge d’eau, puis y prie.” » [Muwaṭṭaʾ, n° 158]</p>
<p>D’après Mālik, d’après ʿAbd Allāh ibn Abī Bakr, d’après sa tante, d’après la fille de Zayd ibn Thābit : « qu’il lui parvint que des femmes se faisaient appeler à la lueur des lampes, au cœur de la nuit, pour guetter la pureté ; elle désapprouvait cela de leur part et disait : “Les femmes n’avaient pas coutume de faire cela.” » [Muwaṭṭaʾ, n° 153]</p>
<ol>
<li>Expose le statut du vêtement de la femme lorsque le sang des menstrues l’a atteint.</li>
<li>Pourquoi la fille de Zayd ibn Thābit désapprouvait-elle l’agir des femmes au sujet des menstrues ?</li>
</ol>
<h2>La préparation préalable</h2>
<p>Lis les hadiths de la leçon des règles de l’urine du petit et de l’adulte, et réponds à ce qui suit :</p>
<ol>
<li>Explique : <em>fa-naḍugh</em> (« qu’elle l’asperge ») — <em>al-ghāʾiṭ</em> (le lieu d’aisance) — <em>yatawaḍḍaʾūna</em> (« ils font leurs ablutions »).</li>
<li>Extrais des hadiths de la leçon le statut de l’urine du petit.</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12911":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12911 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12911 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
