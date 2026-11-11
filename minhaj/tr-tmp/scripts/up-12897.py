#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minhāj — Upgrade GT→main : leçon 12897 (hadith-1es, les ablutions du madhī,
du toucher des parties intimes et du baiser — Muwaṭṭaʾ n° 97-102, 108-110).

Conventions main (cf. 12875, 12884, 12885, 12889 du même livre) :
- h1 « Les ablutions du madhī, du toucher des parties intimes et du baiser
  (al-wuḍūʾ min al-madhī wa-mass al-farj wa-l-qubla) », 7e leçon.
- FIX titleFr : la baseline imprimait « …et de la Qiblah » — contresens :
  القُبْلة (avec ḍamma) = le baiser (objectif 3 : « distinguer le baiser qui
  annule les ablutions… ») ; corrigé en « du baiser ».
- Muwaṭṭaʾ 97 (al-Miqdād pour ʿAlī — pudeur, « j'ai chez moi la fille du
  Messager de Dieu »), 99 (Jundub → Ibn ʿUmar), 100 (balal — Saʿīd : « dût-il
  couler sur ma cuisse »), 101 (al-Ṣalt ibn Ziyād — « détourne-t'en »),
  102 (ʿUrwa/Marwān/Busra bint Ṣafwān), 108 (Ibn ʿUmar — mulāmasa),
  109 (Ibn Masʿūd) : chaînes et textes intégraux.
- Mudawwana 1/118 (Dār al-Kutub al-ʿIlmiyya 1415 H/1994) : sharj (anus) /
  rafʿ (vulve) / dos de la main / creux des doigts = creux de la paume.
- Lexique : madhī (fatḥa du mīm, sukūn du dhāl, yāʾ allégé) ; naḍḥ =
  aspersion/lavage ; jass = attouchement intentionnel ; ifḍāʾ = porter le
  creux de la paume ; sils = incontinence ; balal = humidité.
- « الجناية » imprimé = coquille pour الجنابة (janāba) — prépar. suivante.
- Préparation préalable : questions de la leçon SUIVANTE 12899 (ghusl).
"""

import json

BOOK = "/home/z/my-project/content/books/hadith-1es.json"

HTML_FR = """<h1>Les ablutions du <em>madhī</em>, du toucher des parties intimes et du baiser (<em>al-wuḍūʾ min al-madhī wa-mass al-farj wa-l-qubla</em>)</h1>
<p>Leçon sur les ablutions consécutives au <em>madhī</em>, au toucher des parties intimes et au baiser, matière Ḥadīth, sur la base du <em>Muwaṭṭaʾ</em> de l’imam Mālik avec le commentaire de l’imam al-Zarqānī, à l’intention des élèves de la première année de l’enseignement secondaire traditionnel (<em>ʿatīq</em>) — la septième leçon.</p>
<ul>
<li>Connaître les règles du <em>madhī</em> (liquide pré-éjaculatoire).</li>
<li>Comprendre les règles du toucher des parties intimes.</li>
<li>Distinguer le baiser qui annule les ablutions de celui qui ne les annule pas.</li>
</ul>
<h2>Préambule</h2>
<p>Les annulatifs des ablutions sont des états (<em>aḥdāth</em>) ou des causes d’états ; et le fiqh a donné à la cause le statut de ce qu’elle cause, lorsqu’elle l’entraîne habituellement. Au nombre des états : la sortie du <em>madhī</em> ; au nombre des causes : le toucher des parties intimes et le baiser.</p>
<p>Quel est le statut des ablutions de celui dont est sorti le <em>madhī</em> ? Et quand le toucher des parties intimes et le baiser annulent-ils les ablutions ?</p>
<h2>Les hadiths</h2>
<ul>
<li>D’après Mālik, d’après Abū al-Naḍr — l’affranchi de ʿUmar ibn ʿUbayd Allāh —, d’après Sulaymān ibn Yasār, d’après al-Miqdād ibn al-Aswad : « ʿAlī ibn Abī Ṭālib le chargea d’interroger pour lui le Messager de Dieu — paix et bénédiction sur lui — au sujet de l’homme qui s’approche de son épouse et dont sort le <em>madhī</em> : qu’incombe-t-il ? ʿAlī dit : j’ai chez moi la fille du Messager de Dieu — paix et bénédiction sur lui —, et j’ai honte de l’interroger. Al-Miqdād dit : j’interrogeai le Messager de Dieu — paix et bénédiction sur lui — sur cela ; il dit : “Quand l’un de vous trouve cela, qu’il asperge son sexe d’eau, et qu’il fasse les ablutions — les ablutions de la prière.” » [Muwaṭṭaʾ, n° 97]</li>
<li>D’après Mālik, d’après ʿAbd Allāh ibn Abī Bakr, d’après Ibn Muḥammad ibn ʿAmr ibn Ḥazm : « qu’il entendit ʿUrwa ibn al-Zubayr dire : J’entrai chez Marwān ibn al-Ḥakam ; nous évoquâmes ce dont les ablutions découlent. Marwān dit : et du toucher du sexe [déculent] les ablutions. ʿUrwa dit : je n’ai point eu science de cela. Marwān ibn al-Ḥakam dit : Busra bint Ṣafwān m’informa qu’elle entendit le Messager de Dieu — paix et bénédiction sur lui — dire : “Quand l’un de vous touche son sexe, qu’il fasse les ablutions.” » [Muwaṭṭaʾ, n° 102]</li>
<li>D’après Mālik, d’après Ibn Shihāb, d’après Sālim ibn ʿAbd Allāh, d’après son père ʿAbd Allāh ibn ʿUmar — qu’il avait coutume de dire : « Le baiser de l’homme à son épouse, et son attouchement (<em>jass</em>) de la main, relèvent de la mulāmasa : quiconque embrasse son épouse ou la touche de la main — les ablutions lui incombent. » [Muwaṭṭaʾ, n° 108]</li>
</ul>
<h3>Explication lexicale</h3>
<ul>
<li><em>le madhī</em> (<em>al-madhī</em>) — avec <em>fatḥa</em> du <em>mīm</em>, <em>sukūn</em> du <em>dhāl</em> pointée et allègement du <em>yāʾ</em>, selon la forme la plus pure : un liquide blanc, fluide et visqueux, qui sort lors des préliminaires, à l’évocation du coït ou à son intention.</li>
<li><em>qu’il asperge</em> (<em>fa-l-yanḍaḥ</em>) : le <em>naḍḥ</em> est l’aspersion et le lavage.</li>
<li><em>son attouchement</em> (<em>jassahā</em>) : la toucher avec intention.</li>
</ul>
<h3>Extraction des contenus</h3>
<ul>
<li>Tire [du corpus] ce qui incombe à celui dont est sorti le <em>madhī</em>.</li>
<li>Le baiser annule-t-il les ablutions ?</li>
<li>Expose le statut des ablutions de celui qui a touché son sexe.</li>
</ul>
<h2>L’analyse</h2>
<h3>Premièrement : le statut de la sortie du madhī</h3>
<p>La sortie du <em>madhī</em> fait partie des annulatifs des ablutions ; il y est obligatoire de laver tout le sexe avec l’eau, ensemble avec les ablutions, si l’on veut prier — c’est sa parole dans le hadith : « Quand l’un de vous trouve cela, qu’il asperge son sexe d’eau, et qu’il fasse les ablutions — les ablutions de la prière. » De ce hadith on a tiré que les ablutions ne sont pas obligatoires du seul fait de sa sortie, mais lorsqu’on veut prier ; comme on en a tiré l’obligation d’employer l’eau — l’<em>istijmār</em> [essuyage avec des pierres] ne suffit pas. Ainsi, dans [le commentaire d’]al-Zarqānī : l’eau s’y impose à l’exclusion des pierres, car son sens apparent est l’imposition du lavage — et l’agent déterminé ne reçoit l’acquittement que par lui. Tel est l’avis de Mālik ; et Ibn ʿAbd al-Barr a dit : il n’est fait mention, dans les hadiths du <em>madhī</em> — pourtant nombreux —, d’aucun <em>istijmār</em>.</p>
<p>Et ce qui l’atteste encore, parmi les rapports : ce que rapporta Mālik, d’après Zayd ibn Aslam, d’après Jundub — l’affranchi de ʿAbd Allāh ibn ʿAyāsh : « qu’il dit : J’interrogeai ʿAbd Allāh ibn ʿUmar au sujet du <em>madhī</em> ; il dit : quand tu le trouves, lave ton sexe, et fais tes ablutions — les ablutions de la prière. » [Muwaṭṭaʾ, n° 99]</p>
<h3>Deuxièmement : le statut de l’incontinence du madhī</h3>
<p>L’imam Mālik a intitulé la règle de cette question : « la dispense (<em>rukhsa</em>) de délaisser les ablutions pour le <em>madhī</em> » — or la dispense est le changement du statut vers la facilité, pour excuse, alors que demeure la cause du statut originel. L’excuse requérant cette dispense est l’état de celui qui est atteint d’incontinence (<em>sils</em>). On tire du propos d’Ibn ʿAbd al-Barr que l’incontinence est ce qui ne cesse pas — <em>madhī</em> ou urine —, du fait d’une affection venue de l’âge, du froid ou d’autre chose encore.</p>
<p>L’imam Mālik, par son intitulé « la dispense de délaisser les ablutions pour le <em>madhī</em> », visait à exposer le support (<em>maḥmal</em>) des rapports placés dessous : ils s’entendent de l’atteint d’incontinence — ses ablutions sont valables, tant que l’incontinence n’est pas légère [au point de ne plus durer la majeure partie du temps], et tant qu’il ne peut la faire cesser, fût-elle abondante. Mais si elle est abondante ou dominante — de maladie ou d’autre chose — et qu’il ne peut la faire cesser : il lui est recommandé de faire les ablutions pour chaque prière, tant que cela ne lui est pas pénible, du fait du froid ou d’autre chose.</p>
<p>Et le hadith de l’ordre d’asperger et de faire les ablutions concerne celui qui n’est pas atteint d’incontinence. Al-Zarqānī a dit : à la différence de l’atteint d’incontinence, car celle-ci naît d’une affection du corps. Et Ibn ʿAbd al-Barr rapporta d’al-Mughīra ibn ʿAbd al-Raḥmān : « Le <em>madhī</em> me sortait ; parfois je fis les ablutions deux et trois fois. Je vins trouver al-Qāsim ibn Muḥammad, qui dit : cela ne vient que du diable — détourne-t’en. Je m’en détournai, et cela cessa de moi. »</p>
<p>Et l’avis de Mālik est que ce qui sort — sperme (<em>manī</em>), <em>madhī</em> ou urine — sur le mode de l’incontinence, n’annule pas la pureté. Et en ce sens s’entend ce que rapporta Mālik, d’après Yaḥyā ibn Saʿīd, d’après Saʿīd ibn al-Musayyab : « qu’il l’entendit alors qu’un homme l’interrogeait : “Je trouve de l’humidité (<em>balal</em>) alors que je prie — dois-je me retirer ?” Saʿīd lui dit : dût-il couler sur ma cuisse, je ne me retirerais pas jusqu’à acquitter ma prière. » [Muwaṭṭaʾ, n° 100] Abū ʿUmar [Ibn ʿAbd al-Barr] a dit : son sens est que l’abondance du <em>madhī</em> et son impureté avérée sur le corps et le vêtement n’empêchent pas l’orant d’achever sa prière — même s’il lui est ordonné de laver l’impureté avérée avant d’entrer en prière.</p>
<h3>Troisièmement : le statut du toucher du sexe et du baiser</h3>
<p>Le toucher du sexe fait partie des annulatifs des ablutions selon nous [<em>mālikites</em>] — l’atteste le hadith de Busra bint Ṣafwān, où il vient : « Quand l’un de vous touche son sexe, qu’il fasse les ablutions. » Et son caractère annulatif est conditionné par ce qui suit :</p>
<ul>
<li>que le toucher soit direct, sans interposition ;</li>
<li>que le toucher soit du creux de la paume — du fait du hadith : « Quiconque porte sa main sur son sexe sans voile entre eux, qu’il fasse les ablutions », rapporté par al-Bayhaqī et al-Dāraquṭnī dans leurs <em>Sunan</em>, et par al-Bazzār dans son <em>Musnad</em>, en formules proches. L’<em>ifḍāʾ</em> est, en langue, le toucher par le creux de la paume ; et dans la version de Tirmidhī : « il ne prie qu’après avoir fait ses ablutions » — c’est-à-dire : pour l’annulation de ses ablutions. Voilà un texte explicite au lieu même de la divergence ; et il n’y a pas de différence entre le toucher délibéré, par oubli ou par inadvertance.</li>
</ul>
<p>Quant au toucher de l’épouse à la main, il fait partie des annulatifs des ablutions — l’entendu est le toucher dont on tire habituellement jouissance, et le baiser l’est à plus forte raison. L’atteste le hadith d’ʿAbd Allāh ibn ʿUmar : « qu’il avait coutume de dire : le baiser de l’homme à son épouse, et son attouchement de la main, relèvent de la mulāmasa : quiconque embrasse son épouse ou la touche de la main — les ablutions lui incombent » ; et de même ce que rapporta Mālik : « qu’il lui fut rapporté que ʿAbd Allāh ibn Masʿūd disait : des baisers de l’homme à son épouse [dépendent] les ablutions. » [Muwaṭṭaʾ, n° 109]<br>
Et le baiser [annulatif] est conditionné par l’intention de la jouissance — qu’il la trouve ou non ; ou par le fait qu’il la trouve, même sans l’avoir visée. Quant au baiser des parentes prohibées (<em>maḥārim</em>), il n’annule jamais les ablutions ; comme ne les annule pas non plus le baiser de l’épouse par tendresse ou par compassion, dans la maladie, ou autre cas où la jouissance n’est ni visée ni trouvée habituellement.</p>
<h2>L’évaluation</h2>
<ol>
<li>Tire [du corpus] les conditions de la dispense de délaisser les ablutions pour le <em>madhī</em>.</li>
<li>Expose le statut du toucher du sexe et les conditions de l’annulation des ablutions par lui.</li>
<li>Déduis les restrictions qui annulent les ablutions de celui qui a embrassé son épouse.</li>
</ol>
<h2>L’exploitation</h2>
<p>D’après Mālik, d’après al-Ṣalt ibn Ziyād : « qu’il dit : J’interrogeai Sulaymān ibn Yasār au sujet de l’humidité que je trouvais ; il dit : asperge d’eau ce qui est sous ton vêtement, et détourne-t’en. » [Muwaṭṭaʾ, n° 101]</p>
<p>Et il vient dans la <em>Mudawwana</em> : « … Mālik dit : ses ablutions ne sont pas annulées par le toucher de l’anus (<em>sharj</em>) ni de la vulve (<em>rafʿ</em>), ni de rien de ce qui s’y rapporte — sinon le toucher du sexe seul, du creux de la paume : s’il le touche du dos de la main ou de l’avant-bras, ses ablutions ne sont pas annulées. — Et s’il le touche du creux des doigts ? — J’estime le creux des doigts du rang du creux de la paume, car Mālik m’a dit : le creux des doigts et le creux de la paume sont d’un seul rang.<br>
Il dit : et il me parvint que Mālik dit, du toucher par la femme de son propre sexe : point d’ablutions sur elle. Et Mālik dit de celui qui touche son sexe pendant son lavage de l’impureté majeure : il refait ses ablutions quand il a achevé son lavage de l’impureté majeure — sauf s’il a passé ses mains sur les endroits des ablutions, issus de son lavage : j’estime cela tenant lieu pour lui. » [<em>Mudawwana</em>, 1/118 — éd. Dār al-Kutub al-ʿIlmiyya, 1415 H/1994]</p>
<ol>
<li>Expose, au fil du premier texte, ce qu’on entend par humidité (<em>balal</em>) et son statut.</li>
<li>Tire du second texte les restrictions de l’annulation des ablutions par le toucher du sexe.</li>
</ol>
<h2>La préparation préalable</h2>
<ol>
<li>Quelle est la méthode du lavage de l’impureté majeure (<em>janāba</em>) ?</li>
<li>Quand celui qui veut se laver de l’impureté majeure doit-il faire les ablutions ?</li>
</ol>"""


def main():
    with open(BOOK, "r", encoding="utf-8") as fh:
        d = json.load(fh)
    hit = 0
    for l in d["lessons"]:
        if l.get("docId") == "12897":
            l["htmlFr"] = HTML_FR
            # FIX contresens de la baseline : القُبْلة = le baiser (pas la qibla)
            l["titleFr"] = "Les ablutions du madhī, du toucher des parties intimes et du baiser"
            hit += 1
    if hit != 1:
        raise SystemExit(f"ERREUR: {hit} leçons 12897 trouvées (attendu 1)")
    with open(BOOK, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"OK — leçon 12897 upgradée main: FR {len(HTML_FR)} car + titleFr corrigé")


if __name__ == "__main__":
    main()
