#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12945 (hadith-1es, l'appel à la prière
en voyage — Muwaṭṭaʾ n° 193-195, + Bukhārī + Abū ʿAwāna + Bayhaqī).

Conventions main (cf. 12875, 12884-12929 du même livre) :
- h1 « Règlement sur l'appel à la prière en voyage », 14e leçon ; objectifs
  en infinitifs (source 1re personne).
- Muwaṭṭaʾ 193 (ʿUrwa à Hishām : adhān+iqāma ou iqāma seule), 194 (adhān
  monté), 195 (Ibn ʿUmar : nuit froide et venteuse, « priez dans les
  demeures » — le manuel imprime « 193 » une 2e fois : numéro déjà porté
  par le hadith d'ʿUrwa ; numérotation standard 195, noté).
- Taḥlīl I : Ibn al-Qāsim (l'adhān n'incombe qu'au miṣr — le voyage est
  lieu d'allègement) vs Ashhab (refaire si délaissé délibérément) vs rājiḥ
  (il suffit) ; adhān monté (l'état n'empêche pas la transmission ; pas de
  continuité adhān-prière ; ʿAṭāʾ : karāha sauf excuse) ; iqāma monté :
  deux narrations (al-Shaykh Abū Bakr vs Ibn Wahb — acte léger non
  séparateur) ; adhān assis : Mudawwana vs qāḍī Abū l-Faraj ; « Ya Bilāl,
  lève-toi » (Ṣaḥīḥayn) : Ibn al-Mundhir/Ibn Khuzayma/ʿIyāḍ vs Nawawī
  (« va à un endroit exposé ») vs Ḥāfiẓ (formule susceptible des deux,
  l'avis de Nawawī plus fort).
- Taḥlīl II : Ibn ʿUmar a étendu au vent (ʿilla : la peine — Bājī) ; «
  dans les rahāl » indique le voyage (Bājī : derrière lui / individuellement
  / chaque groupe) ; Bukhārī (« ou » de variété, propre au voyage) vs
  narration de Mālik absolue (jumhūr) ; règle muṭlaq/muqayyad ; Abū ʿAwāna
  (« froide ou pluvieuse ou venteuse ») ; Ibn Baṭṭāl consensus vs Mālikites/
  Shāfiʿites (vent de nuit seulement).
- Istimhār : Salmān al-Fārisī (Bayhaqī : rangs d'anges derrière l'homme en
  terre éloignée — arḍ fāʾ).
- Lexique : al-raḥāl (pl. de raḥl : demeure ; aussi le bagage de voyage).
- Préparation préalable : leçon SUIVANTE 12948 (ouverture de la prière) —
  ḥadhw (« à la hauteur de / en face de »), mankibayhi (« ses deux épaules
  », articulation bras-épaule).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Règlement sur l’appel à la prière en voyage (<em>aḥkām al-nidāʾ li-l-ṣalāh fī l-safar</em>)</h1>
<p>Leçon sur les règles de l’appel à la prière en voyage, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la quatorzième leçon.</p>
<ol>
<li>Connaître le statut de l’appel à la prière en voyage.</li>
<li>Distinguer la meilleure manière d’être de celui qui appelle à la prière.</li>
<li>S’appliquer à appeler à la prière chaque fois que l’occasion m’en est offerte.</li>
</ol>
<h2>Préambule</h2>
<p>L’appel à la prière, cinq fois le jour, est un rite des rites de l’islam : c’est pourquoi les juristes s’y sont attachés et en ont exposé en détail les règles et les sagesses — non seulement en résidence, mais aussi en voyage.</p>
<p>Quelles sont donc les règles propres à l’appel à la prière en voyage ? Et quelle est la manière d’être préférée de l’appelant à la prière en voyage ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Hishām ibn ʿUrwa : « que son père lui dit : Si tu es en voyage : si tu veux faire l’appel et l’iqāma, fais-le ; et si tu veux, fais l’iqāma et ne fais pas l’appel. » [Muwaṭṭaʾ, n° 193]</li>
<li>Yaḥyā a dit : « j’ai entendu Mālik dire : “Il n’y a pas de mal que l’homme fasse l’appel monté [sur sa bête].” » [Muwaṭṭaʾ, n° 194]</li>
<li>D’après Mālik, d’après Nāfiʿ : « que ʿAbd Allāh ibn ʿUmar fit l’appel à la prière une nuit de froid et de vent, puis dit : Ne priez-vous pas dans les demeures ! Il dit ensuite : Le Messager de Dieu — paix et bénédiction sur lui — ordonnait au muezzin, quand la nuit était froide et pluvieuse, de dire : “Ne priez-vous pas dans les demeures !” » [Muwaṭṭaʾ, n° 195 — le manuel imprime « 193 », numéro déjà porté par le premier hadith]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>al-raḥāl</em> (« les demeures ») : pluriel de <em>raḥl</em> — c’est la demeure et l’habitation ; et <em>raḥl</em> désigne aussi ce que l’homme emporte avec lui, en voyage, de son ameublement.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Extrais du premier hadith le statut de l’appel en voyage.</li>
<li>Expose la manière d’être sur laquelle se trouve l’appelant à la prière.</li>
<li>Déduis du troisième hadith le statut de s’abstenir de la prière en commun la nuit froide.</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : le statut de l’appel à la prière en voyage, et la manière d’être de l’appelant</h3>
<h4>Le statut de l’appel à la prière en voyage</h4>
<p>La parole d’ʿUrwa à son fils Hishām — « Si tu es en voyage : si tu veux faire l’appel et l’iqāma, fais-le ; et si tu veux, fais l’iqāma et ne fais pas l’appel » — indique la recommandation de l’adhān en voyage et la légitimité de l’iqāma. Les compagnons de Mālik divergèrent sur le statut de l’adhān en voyage, en plusieurs avis :</p>
<ul>
<li>Ibn al-Qāsim rapporta de Mālik que l’adhān n’est [de règle] que dans la métropole, pour les congrégations dans les mosquées ; quant au voyageur, l’adhān ne lui incombe pas — car le voyage est lieu d’allègement, et pour cause d’absence de mosquée et d’imam ; et quant à ce qui fut institué de l’adhān du voyageur à l’aube ou en d’autres [temps], pour manifester le rite de l’islam, il n’incombe pas.</li>
<li>Ashhab rapporta de Mālik : s’il délaisse l’adhān en voyage délibérément, il refait la prière. Et l’avis le plus solide de la parole de Mālik : si le voyageur délaisse l’adhān, délibérément ou par oubli, sa prière lui tient lieu.</li>
</ul>
<h4>La manière d’être de l’appelant à la prière en voyage</h4>
<p>Ce que l’on vise par la manière d’être, c’est l’état où se trouvent le muezzin et celui qui fait l’iqāma : monté, debout ou assis. L’explication en voici :</p>
<ul>
<li>L’appel monté [sur sa bête]
<p>L’imam Mālik voit la permission de l’adhān monté — car c’est un état qui n’empêche pas la transmission ; et il n’est pas de la sunna de l’adhān d’être suivi sans intervalle de la prière : on sépare donc l’un de l’autre par la descente et la marche jusqu’au lieu de la prière. Yaḥyā a dit : j’ai entendu Mālik dire : il n’y a pas de mal que l’homme fasse l’appel monté. Ibn ʿAbd al-Barr a dit : Ibn ʿUmar faisait l’appel sur le chameau, puis descendait et faisait l’iqāma. Et ʿAṭāʾ a réprouvé l’appel monté, sauf infirmité ou nécessité.</p>
<p>Quant à l’iqāma du monté, il y a en la matière deux narrations de Mālik : la première — qu’il ne fait pas l’iqāma [monté] : il est des conditions de l’iqāma d’être suivie sans intervalle de la prière, or sa descente de sa monture et sa marche jusqu’au lieu de sa prière sont un acte qui sépare l’iqāma de la prière — c’est ce qu’a dit al-shaykh Abū Bakr. La seconde — que le monté fait l’iqāma : car sa descente vers la prière est un acte léger, qui n’est pas compté pour séparateur — comme le fait de prendre le vêtement et de déployer ce sur quoi l’on prie ; rapportée par Ibn Wahb de Mālik.</p></li>
<li>L’appel assis
<p>Mālik et al-Awzāʿī ont réprouvé que l’on fasse l’appel assis. Il est dit dans la <em>Mudawwana</em> : que l’assis ne fasse pas l’appel ; et dans le livre du qāḍī Abū l-Faraj : « il n’y a pas de mal que l’assis fasse l’appel ». Le fondement de ce qui est dans la <em>Mudawwana</em> : la transmission et l’élévation sont de règle dans l’adhān — c’est pourquoi l’adhān fut institué sur le minaret, et l’assise est le contraire de l’élévation ; le fondement de la narration d’Abū l-Faraj : l’élévation est de règle quant au lieu, non quant à l’état du muezzin — preuve en est que l’on fait l’appel monté. Et dans les deux <em>Ṣaḥīḥ</em>, il dit — paix et bénédiction sur lui — : « Ô Bilāl, lève-toi et fais l’appel. » Ibn al-Mundhir, Ibn Khuzayma et ʿIyāḍ [en ont tiré] : il y a là preuve pour l’adhān debout ; al-Nawawī l’a contesté : ce que vise sa parole “lève-toi” est : va à un endroit exposé et y appelle à la prière, que les gens t’entendent — il n’y est pas traité du fait d’être debout pendant l’adhān. Al-Ḥāfiẓ [Ibn Ḥajar] a dit : et ce qu’il a nié n’est pas loin de l’apparent de la formule — car la formule est susceptible des deux sens, même si ce qu’il a dit est le plus fort.</p></li>
</ul>
<h3>Deuxièmement : le statut de s’abstenir de la congrégation la nuit pluvieuse et de vent violent</h3>
<p>Dans la parole de ʿAbd Allāh ibn ʿUmar — « le Messager de Dieu — paix et bénédiction sur lui — ordonnait au muezzin, quand la nuit était froide et pluvieuse, de dire : Ne priez-vous pas dans les demeures ! » — il y a preuve de la permission de s’abstenir de la prière en commun la nuit froide et pluvieuse. Et Ibn ʿUmar a fait du vent l’analogique de la pluie : la cause commune entre eux deux est la peine qui s’ensuit — c’est ce qu’a dit al-Bājī, s’en tenant à cette narration. Al-Bājī a dit : l’expression « dans les demeures » indique le voyage : il leur permit donc de prier derrière lui s’il était imam ; et il se peut qu’il leur ait permis d’y prier chacun pour soi, ou que chaque groupe eût pour imam un homme des leurs. Et dans [le <em>Ṣaḥīḥ</em> d’]al-Bukhārī : « il nous informa que le Messager de Dieu — paix et bénédiction sur lui — ordonnait à un muezzin de faire l’appel, puis de dire à sa suite : Ne priez-vous pas dans les demeures ! — la nuit froide et pluvieuse, en voyage. » Al-Ḥāfiẓ a dit : et le « ou » est de variété, non de doute ; et l’apparent, c’est que cela est propre au voyage — la narration de Mālik est absolue, et c’est d’elle qu’ont pris le plus grand nombre ; mais la règle qui porte l’absolu sur le restreint exige que cela soit propre au voyageur sans restriction, et qu’y soit adjoint quiconque subit en résidence une peine pareille à la sienne — à la différence de celui qui n’en subit pas. Il a dit : et dans le <em>Ṣaḥīḥ</em> d’Abū ʿAwāna : « nuit froide, ou pluvieuse, ou venteuse » — cela montre que chacun des trois est excuse pour différer [l’office] de la congrégation ; et Ibn Baṭṭāl y a transmis le consensus ; mais le connu chez les mālikites et les shāfiʿites est que le vent n’est excuse que de nuit — et l’apparent du hadith restreint les trois à la nuit.</p>
<h2>L’évaluation</h2>
<ol>
<li>Cite les paroles des juristes au sujet du statut de l’appel en voyage.</li>
<li>Est-il permis au muezzin de faire l’appel assis ?</li>
<li>Qu’indique sa parole — paix et bénédiction sur lui — : « Ne priez-vous pas dans les demeures ! » ?</li>
</ol>
<h2>L’exploitation</h2>
<p>D’après Salmān al-Fārisī : « qu’il dit : le Prophète — paix et bénédiction sur lui — a dit : Il n’est pas un homme qui soit en une terre éloignée (<em>arḍ fāʾ</em>), qui fasse l’appel à l’approche de la prière, mette en place la prière et prie, sans qu’il y ait derrière lui des rangs d’anges dont on ne voit pas les extrémités — s’inclinant de son inclinaison, se prosternant de sa prosternation, et disant amen sur son invocation. » [Rapporté par al-Bayhaqī dans ses <em>Sunan</em>]</p>
<ol>
<li>Extrais du hadith le mérite de l’appel à la prière en voyage.</li>
<li>Expose le rapport entre ce hadith et le titre de la leçon.</li>
</ol>
<h2>La préparation préalable</h2>
<ol>
<li>Explique : <em>ḥadhw</em> (« à la hauteur de, en face de ») – <em>mankibayhi</em> (« ses deux épaules » — l’assemblage de l’os du bras et de la clavicule).</li>
<li>Extrais les contenus des hadiths de la leçon des règles de l’ouverture de la prière.</li>
<li>Quel est le statut de l’élévation des mains au takbīr d’entrée en prière ?</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12945":
            l["htmlFr"] = HTML_FR
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12945 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12945 upgradée main: FR {len(HTML_FR)} car")


if __name__ == "__main__":
    main()
