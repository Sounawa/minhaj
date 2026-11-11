#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12899 (hadith-1es, la méthode du lavage de
l'impureté majeure — Muwaṭṭaʾ n° 111-117).

Conventions main (cf. 12875, 12884, 12885, 12889, 12897 du même livre) :
- h1 « La méthode du lavage de l'impureté majeure (kayfiyyat al-ghusl min
  al-janāba) », 8e leçon.
- Muwaṭṭaʾ 111 (ʿĀʾisha — la méthode prophétique : mains → ablutions →
  racines des cheveux → 3 poignées → toute la peau), 112 (le farq — 3 ṣāʿ),
  113 (Ibn ʿUmar — main droite → sexe → madmada/istinthār → visage+yeux →
  mains → tête → āfāʿa), 114 (ḥufna + ḍaghth pour la femme), 115 (ʿUmar,
  ʿUthmān, ʿĀʾisha : khitān/khitān), 116 (Abū Salama — métaphore du farūj
  « le poussin criaille avec les coqs »), 117 (Abū Mūsā al-Ashʿarī —
  « interroge-moi de ce dont tu n'interrogerais pas ta mère ») : chaînes et
  textes intégraux.
- Lexique : takhlīl = faire pénétrer l'eau aux racines ; uṣūl al-shaʿr ;
  afāḍa = faire couler ; ḥufna = le remplissage des deux mains ; ḍaghth =
  pétrir les cheveux ; kumra/ḥashafa = le gland ; farq = récipient de 3 ṣāʿ ;
  farūj = le poussin.
- ʿĀʾisha = Compagne + mère des croyants → « que Dieu soit satisfait
  d'elle » là où le manuel l'imprime (raḍiya).
- Préparation préalable : questions de la leçon SUIVANTE 12901 (dormir avant
  le ghusl ; prier en ayant oublié l'état d'impureté).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>La méthode du lavage de l’impureté majeure (<em>kayfiyyat al-ghusl min al-janāba</em>)</h1>
<p>Leçon sur la méthode du lavage de l’impureté majeure, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la huitième leçon.</p>
<ul>
<li>Connaître la méthode du lavage de l’impureté majeure.</li>
<li>Distinguer ce qui rend le lavage obligatoire de ce qui ne le rend pas, lors de la jonction des deux circoncisions.</li>
<li>Incarner la méthode requise dans le lavage.</li>
</ul>
<h2>Préambule</h2>
<p>La pureté majeure — le lavage de l’impureté majeure (<em>janāba</em>) — est une obligation ; elle est de ces adorations dont le croyant doit se soucier, comme il doit suivre le Prophète — paix et bénédiction sur lui — en la description qui fut transmise de lui en cela.</p>
<p>Quelle est la méthode du lavage ? Les ablutions y sont-elles requises ? Et le lavage est-il obligatoire lorsque le coït a lieu sans éjaculation ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Hishām ibn ʿUrwa, d’après son père, d’après ʿĀʾisha, mère des croyants : « Le Messager de Dieu — paix et bénédiction sur lui —, quand il se lavait de l’impureté majeure, commençait par laver ses deux mains ; puis il faisait les ablutions, comme il les faisait pour la prière ; puis il introduisait ses doigts dans l’eau et en passait aux racines de ses cheveux ; puis il versait sur sa tête trois poignées, de ses deux mains ; puis il faisait couler l’eau sur toute sa peau. » [Muwaṭṭaʾ, n° 111]</li>
<li>D’après Mālik : « qu’il lui fut rapporté que ʿĀʾisha, mère des croyants, fut interrogée sur le lavage de la femme pour l’impureté majeure ; elle dit : “Qu’elle verse sur sa tête trois poignées d’eau, et qu’elle pétrisse sa tête avec ses deux mains.” » [Muwaṭṭaʾ, n° 114]</li>
<li>D’après Mālik, d’après Ibn Shihāb, d’après Saʿīd ibn al-Musayyab : « que ʿUmar ibn al-Khaṭṭāb, ʿUthmān ibn ʿAffān et ʿĀʾisha — l’épouse du Prophète, paix et bénédiction sur lui — avaient coutume de dire : quand la circoncision touche la circoncision, le lavage est devenu obligatoire. » [Muwaṭṭaʾ, n° 115]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>il en passait aux racines</em> (<em>yukhallil</em>) : fait parvenir l’eau à la peau.</li>
<li><em>les racines de ses cheveux</em> (<em>uṣūl shaʿrihi</em>) : les points de naissance des cheveux de sa tête.</li>
<li><em>il faisait couler</em> (<em>yufīḍ</em>) : c’est-à-dire faisait s’écouler.</li>
<li><em>qu’elle verse</em> (<em>li-taḥfin</em>) : la <em>ḥufna</em> est le remplissage des deux mains d’eau ; le sens de <em>li-taḥfin</em> : qu’elle répande les poignées.</li>
<li><em>et qu’elle pétrisse</em> (<em>wa-li-taḍghath</em>) : le <em>ḍaghth</em> est le traitement des cheveux de la tête à la main lors du lavage — comme si elle en mêlait les uns aux autres pour que l’eau y pénètre.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Comment se lave-t-on de l’impureté majeure ?</li>
<li>Qu’incombe-t-il à la femme dans le lavage de ses cheveux pour l’impureté majeure ?</li>
<li>Qu’entraîne la jonction des deux circoncisions ?</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : la description du lavage de l’impureté majeure</h3>
<p>Qui veut se laver de l’impureté majeure procède comme suit :</p>
<ul>
<li>laver ses deux mains du lavage légal, avant de les introduire dans le récipient ;</li>
<li>se purifier de l’impureté concrète (<em>khabath</em>), en commençant par laver son sexe ;</li>
<li>faire ensuite les ablutions — les ablutions de la prière —, comme il vient dans le premier hadith : « il commença par laver ses deux mains, puis il fit les ablutions comme il les faisait pour la prière » — cela sur le mode du recommandé ; et il lave les membres des ablutions une fois, une fois, selon l’avis répandu ;</li>
<li>introduire ses doigts dans l’eau, et en passer aux racines de ses cheveux ;</li>
<li>laver sa tête trois fois, avec trois poignées ;</li>
<li>couvrir son corps d’eau, et s’assurer que l’eau parvient à l’ensemble des parties du corps — parvenue liée au frottement de la main, ou au moyen d’une corde, ou avec l’aide d’un époux.</li>
</ul>
<p>Et atteste la continuité de la pratique de la méthode transmise du Messager de Dieu — paix et bénédiction sur lui — ce que rapporta Mālik, d’après Nāfiʿ : que ʿAbd Allāh ibn ʿUmar « quand il se lavait de l’impureté majeure, commençait par répandre sur sa main droite, la lavait ; puis lavait son sexe ; puis se rinçait la bouche et aspirait [l’eau] par le nez ; puis lavait son visage et aspergeait ses deux yeux ; puis lavait sa main droite, puis lavait sa main gauche ; puis lavait sa tête ; puis se lavait et faisait couler l’eau sur lui. » [Muwaṭṭaʾ, n° 113]</p>
<h3>Deuxièmement : la méthode de lavage des cheveux de la femme lors du lavage</h3>
<p>Le lavage de la femme — pour l’impureté majeure ou les menstrues — est comme celui de l’homme, si ce n’est qu’elle ne défait pas les tresses des cheveux de sa tête : elle verse dessus trois poignées, et traite les cheveux de la tête afin que l’eau parvienne à la peau. L’atteste la parole de ʿĀʾisha — que Dieu soit satisfait d’elle — : « qu’elle verse sur sa tête trois poignées d’eau, et qu’elle pétrisse sa tête avec ses deux mains ».</p>
<p>Et se rattache aux règles du lavage la quantité d’eau qui y suffit : il fut transmis que ce sont trois <em>ṣāʿ</em> — soit l’équivalent de douze poignées. L’atteste ce que rapporta Mālik, d’après Ibn Shihāb, d’après ʿUrwa ibn al-Zubayr, d’après ʿĀʾisha, mère des croyants : « Le Messager de Dieu — paix et bénédiction sur lui — se lavait de l’impureté majeure avec un récipient : le <em>farq</em>. » [Muwaṭṭaʾ, n° 112] — le <em>farq</em> — avec <em>fatḥa</em> du <em>rāʾ</em>, selon la forme pure et répandue — est un récipient de la contenance de trois <em>ṣāʿ</em>.</p>
<h3>Troisièmement : le statut de la jonction des deux circoncisions</h3>
<p>Au nombre des causes entraînant le lavage : le contact de la circoncision avec la circoncision — quand elles se joignent, le lavage est devenu obligatoire. L’entendu est le dépassement de la circoncision par la circoncision, au sens de l’enfouissement du gland (<em>kumra</em>) dans le sexe — c’est là la mesure qui explique le mot de « contact » (<em>mass</em>) venant dans le hadith cité. Tel est l’arrêté chez nous, dans l’école mālikite. L’appuie ce que rapporta Mālik, d’après Abū al-Naḍr — l’affranchi de ʿUmar ibn ʿUbayd Allāh —, d’après Abū Salama ibn ʿAbd al-Raḥmān ibn ʿAwf : « qu’il dit : J’interrogeai ʿĀʾisha — l’épouse du Prophète, paix et bénédiction sur lui — : qu’est-ce qui entraîne le lavage ? Elle dit : “Sais-tu à quoi tu ressembles, Abū Salama ? Au poussin (<em>farūj</em>) : il entend les coqs criarder, et criaille avec eux ! Quand la circoncision dépasse la circoncision, le lavage est devenu obligatoire.” » [Muwaṭṭaʾ, n° 116]</p>
<p>L’éjaculation n’est pas requise lors de l’enfouissement du gland : le seul enfouissement suffit à rendre le lavage obligatoire. L’atteste ce que rapporta Mālik : « qu’Abū Mūsā al-Ashʿarī vint trouver ʿĀʾisha — l’épouse du Prophète, paix et bénédiction sur lui — et lui dit : La divergence des Compagnons du Prophète — paix et bénédiction sur lui — sur une chose m’a bel et bien peinée, et j’ai grand scrupule à te l’exposer. Elle dit : “Qu’est-ce donc ? Ce dont tu ne saurais interroger ta mère — interroge-moi donc sur lui.” Il dit : L’homme approche son épouse, puis se relâche sans éjaculer. Elle dit : quand la circoncision dépasse la circoncision, le lavage est devenu obligatoire. Abū Mūsā al-Ashʿarī dit : je n’interrogerai sur cela personne après toi, jamais. » [Muwaṭṭaʾ, n° 117]</p>
<h2>L’évaluation</h2>
<ol>
<li>Un homme a couvert son corps d’eau dans le lavage de l’impureté majeure — cela lui suffit-il ? Appuie ta réponse.</li>
<li>Qu’entend-on par la jonction de la circoncision avec la circoncision ?</li>
<li>Expose ce qui suffit à la femme dans le lavage de ses cheveux.</li>
</ol>
<h2>L’exploitation</h2>
<p>Il vient dans les <em>Nawādir</em> et <em>Ziyādāt</em> : « Et l’impur majeur (<em>junub</em>) commence : il lave ses deux mains, puis se nettoie de l’impureté, puis fait les ablutions — les ablutions de la prière —, puis fait pénétrer [l’eau] aux racines de ses cheveux ; et dans le hadith : puis il plonge ses mains dans l’eau et en passe, avec ses doigts, aux racines des cheveux de sa tête, jusqu’à s’assurer de la peau ; puis il puise sur sa tête trois poignées d’eau, de ses deux mains ; puis il fait couler l’eau sur toute sa peau. » [<em>al-Nawādir wa-l-ziyādāt</em> d’Ibn Abī Zayd al-Qayrawānī, 1/62-63]</p>
<ol>
<li>Compare ce qui vient dans la leçon et ce qui figure en ce texte, en appuyant les règles qui s’y trouvent.</li>
</ol>
<h2>La préparation préalable</h2>
<ol>
<li>Qu’est-il recommandé à l’impur majeur qui veut dormir avant le lavage ?</li>
<li>Quel est le statut de l’impur majeur qui prie en ayant oublié qu’il est en état d’impureté majeure ?</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12899":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12899 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12899 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
