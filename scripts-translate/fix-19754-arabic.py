#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Translittération des citations arabes de fr19754_* + coquilles."""
import re

MAP = [
    # coquilles
    ("documment", "document"),
    # fr_3
    ("(بُهْتَٰن)", "(buhtān)"),
    ("كَمَا ٱسْتَـْٔذَنَ ٱلَّذِينَ مِن قَبْلِهِمْ", "kamā s-taʾḏana l-laḏīna min qablihim"),
    ("يَسْتَـْٔذِنُوكَ", "yastaʾḏinūka"),
    ("quant au nom اِسْتِيذَان lui-même", "quant au nom al-istīḏān lui-même"),
    ("ٱلْفِئَتَانِ à 8:48 (فَلَمَّا تَرَآءَتِ ٱلْفِئَتَانِ نَكَصَ عَلَىٰ عَقِبَيْهِ, duel médian s'il en fut)",
     "al-fiʾatāni à 8:48 (falammā tarāʾati l-fiʾatāni nakaṣa ʿalā ʿaqibayhi, duel médian s'il en fut)"),
    ("l'oblique ٱمْرَأَتَيْنِ (28:23, وَجَدَ مِن دُونِهِمُ ٱمْرَأَتَيْنِ تَذُودَانِ — duel lui aussi médian, mais dessiné au yāʾ de la déclinaison oblique, non à l'alif)",
     "l'oblique imraʾatayni (28:23, wa-ǧada min dūnihimu mraʾatayni taḏūdāni — duel lui aussi médian, mais dessiné au yāʾ de la déclinaison oblique, non à l'alif)"),
    ("au marfūʿ, هَٰذَا بُهْتَٰنٌ عَظِيمٌۭ (24:16)", "au marfūʿ, hāḏā buhtānun ʿaẓīm (24:16)"),
    ("au manṣūb, بُهْتَٰنًۭا وَإِثْمًۭا مُّبِينًۭا (4:20, et de même 4:112, 4:156, 33:58)",
     "au manṣūb, buhtānan wa-iṯman mubīn (4:20, et de même 4:112, 4:156, 33:58)"),
    ("au maǧrūr, بِبُهْتَٰنٍۢ يَفْتَرِينَهُۥ (60:12)", "au maǧrūr, bi-buhtānin yaftarīnahu (60:12)"),
    # fr_2
    ("Le mot بُهْتَـن, que le vers écrit", "Le mot buhtān, que le vers écrit"),
    ("Le mot كِلْتَا — « toutes deux » —", "Le mot kil-tā — « toutes deux » —"),
    # fr_4
    ("كِلْتَا ٱلْجَنَّتَيْنِ ءَاتَتْ أُكُلَهَا", "kil-tā l-ǧannatayni ʾātat ʾulatahā"),
    ("جَنَّتَانِ (55:46, 55:62)", "ǧannatāni (55:46, 55:62)"),
    ("(أَتَىٰ, ءَاتَىٰ)", "(atā, ʾātā)"),
    ("l'interjection يَٰحَسْرَتَىٰ de 39:56", "l'interjection yā ḥasratā de 39:56"),
    ("(آتَى — zéro occurrence)", "(ātā au madda initial — zéro occurrence)"),
    ("(ءَاتَىٰ, vingt-six positions)", "(ʾātā, vingt-six positions)"),
    # fr_5
    ("de هُدًۭى لِّلْمُتَّقِينَ 2:2 à 5:46", "de hudan li-l-muttaqīn (2:2) à 5:46"),
    ("(cinq vers, أَلَيْسَ فِى جَهَنَّمَ مَثْوًۭى لِّلْكَٰفِرِينَ)", "(cinq vers, a-laysa fī ǧahannama maṯwan li-l-kāfirīn)"),
    ("toutes à l'alif suscrite (بُهْتَٰن)", "toutes à l'alif suscrite (buhtān)"),
    ("en 24:59 (كَمَا ٱسْتَـْٔذَنَ) et 24:62 (يَسْتَـْٔذِنُوكَ)", "en 24:59 (kamā s-taʾḏana) et 24:62 (yastaʾḏinūka)"),
    ("(سَوَآءٌ, 2:6)", "(sawāʾun, 2:6)"),
    ("سَدًّا (18:94, la redoute, à la shadda) et سُدًى (75:36, en vain, à la maqṣūra noonée)",
     "saddan (18:94, la redoute, à la shadda) et sudan (75:36, en vain, à la maqṣūra noonée)"),
    ("le passif يُؤْذَنَ (cinq vers) et le simple أَذِنَ (sept vers)",
     "le passif yuʾḏana (cinq vers) et le simple aḏina (sept vers)"),
]

total = 0
for i in range(1, 6):
    p = f"/home/z/my-project/tr-tmp/fr19754_{i}.html"
    h = open(p, encoding="utf-8").read()
    n = 0
    for ar, tr in MAP:
        if ar in h:
            n += h.count(ar)
            h = h.replace(ar, tr)
    open(p, "w", encoding="utf-8").write(h)
    left = len(re.findall(r"[\u0600-\u06FF]", h))
    print(f"fr19754_{i}.html : {n} remplacements, AR restants = {left}")
    total += n
print("TOTAL:", total)
