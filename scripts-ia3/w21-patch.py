#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R745/W21 — patch fix-typo.py pour hadith-3es : carte W21 + règles classify (v3 propre)."""
import re

P = "scripts-ia3/fix-typo.py"
s = open(P, encoding="utf-8").read()
assert "W21 (hadith-3es" not in s, "patch déjà appliqué"

MAP = '''# W21 (hadith-3es, hajj/ʿumra, translit ch=ش j=ج — arbitrages du tour ; 3 finales
# qubuʿ/mudarraʿ/jadʿ arbitrées sur formes lexicales uniques, tirage pdfUrl 404, consignées).
PAIR_MEDIAL.update({
    ("mash", "ar"): "ʿ", ("mach", "ar"): "ʿ",                                     # (al-)Mashʿar al-Ḥarām
    ("cha", "ā"): "ʿ", ("cha'ā", "ir"): "ʾ", ("cha", "th"): "ʿ", ("yatacha", "th"): "ʿ", # chaʿāʾir (شعائر ʿ puis ʾ), chaʿthā, yatachaʿthath
    ("cha", "r"): "ʿ", ("cha", "n"): "ʾ",                                          # chaʿr (الشَّعْر), chaʾn (شَأْن)
    ("khuth", "am"): "ʿ", ("mutamatti", "a"): "ʿ", ("tamatta", "a"): "ʿ", ("tamattu", "i"): "ʿ", # Khuthʿam, mutamattiʿa, tamattaʿa, ka-tamattuʿi
    ("ra", "ā"): "ʾ", ("a", "rif"): "ʿ", ("ji", "r"): "ʿ", ("su", "il"): "ʾ",        # raʾā (رأى), aʿrif(a), al-Jiʿrāna, suʾila
    ("manāfi", "u"): "ʿ", ("tatawwu", "an"): "ʿ", ("ya", "talūn"): "ʿ",              # manāfiʿu, tatawwuʿan, yaʿtalūn
    ("chay", "an"): "ʾ", ("chay", "a"): "ʾ", ("shay", "in"): "ʾ",                    # chayʾan/chayʾa/shayʾin (شيء)
    ("an", "ām"): "ʿ", ("sab", "atin"): "ʿ", ("sab", "ati"): "ʿ", ("sab", "a"): "ʿ",   # Anʿām, wa-sabʿatin, s-sabʿati, sabʿa
    ("yanja", "u"): "ʿ", ("ğa", "far"): "ʿ", ("yadfa", "u"): "ʿ", ("yadfa", "a"): "ʿ",  # yanjaʿu, Ğaʿfar, yadfaʿu/a
    ("dafa", "a"): "ʿ", ("daf", "u"): "ʿ", ("daf", "i"): "ʿ", ("dāfi", "an"): "ʿ",      # dafaʿa, ad-dafʿu, bi-dafʿi, dāfiʿan
    ("ta", "arr"): "ʿ", ("ach", "ar"): "ʿ", ("ach", "ur"): "ʿ", ("aṭ", "imū"): "ʿ",     # taʿarr*, achʿarah/achʿur (شعر), wa-aṭʿimū (ط-ع-م)
    ("bi-mra", "atih"): "ʾ", ("mra", "at"): "ʾ", ("imra", "a"): "ʾ", ("amra", "a"): "ʾ",  # امرأة hamza (4 formes)
    ("rji", "ū"): "ʿ", ("raja", "tum"): "ʿ", ("raja", "ā"): "ʿ", ("yarji", "a"): "ʿ",    # rjiʿū, rajaʿtum/ā, yarjiʿa (LONGVOWL arji couvre aussi)
    ("yaf", "al"): "ʿ", ("f", "al"): "ʿ", ("if", "al"): "ʿ", ("taf", "al"): "ʿ",         # yafʿal*, ya-fʿalu, ifʿal, tafʿalu (فعل)
    ("fa", "al"): "ʿ", ("faj", "al"): "ʿ", ("fi", "l"): "ʿ", ("fi'li", "hi"): "ʿ",        # faʿal*, fajʿal, fiʿl*, li-fiʿli-h(i) 2e signe
    ("ja", "al"): "ʿ", ("ja", "lu"): "ʿ",                                            # jaʿalnā(hā), jaʿlu (جعل)
    ("yunāzi", "unnaka"): "ʿ", ("tanza", "a"): "ʿ", ("yaza", "u"): "ʿ",               # yunāziʿunnaka, tanzaʿa(hu), yazaʿu (consigné)
    ("d", "u"): "ʿ", ("tad", "ū"): "ʿ", ("yad", "ū"): "ʿ", ("da", "ā"): "ʿ", ("da", "aw"): "ʿ", # dʿu, tadʿū, yadʿū, fa-daʿānī, daʿawtanā (دعا)
    ("muta", "ajj"): "ʿ", ("yatla", "a"): "ʿ", ("ṭlu", "a"): "ʿ", ("ṭala", "ati"): "ʿ",   # mutaʿajjil, wa-yatlaʿa, yaṭluʿa, ṭalaʿati (طلع)
    ("arka", "ān"): "ʿ", ("rtafa", "ati"): "ʿ", ("rtafi", "ū"): "ʿ", ("wa-yarka", ""): "ʿ", # arkaʿān (ركع), rtafaʿati/wa-rtafiʿū (رفع), wa-yarkaʿ
    ("yu", "aẓẓim"): "ʿ", ("ta", "ẓīm"): "ʿ", ("wuḍi", "at"): "ʿ", ("ya", "kul"): "ʾ",    # yuʿaẓẓim, taʿẓīm, wuḍiʿat, yaʾkulu(hā)
    ("da", "il"): "ʿ", ("ya", "tamir"): "ʿ", ("mu", "tamir"): "ʿ", ("l-mu", "tamir"): "ʿ", # (ad-)Daʿlī, l-yaʿtamir, (l-)muʿtamir (عتمر)
    ("ata", "ammal"): "ʾ", ("ta", "umm"): "ʾ", ("yata", "ammad"): "ʿ", ("sta", "īn"): "ʿ", # ataʾammalu, taʾummū (تأمّم), yataʿammada (تعمد), wa-staʿīnu
    ("yata", "all"): "ʿ", ("ta", "all"): "ʿ", ("bada", "a"): "ʾ", ("qa", "da"): "ʿ",       # yataʿallalūn, li-taʿalluqih (علل/علق), badaʾa, (Dhū/l-)Qaʿda
    ("qra", "u"): "ʾ", ("a-qra", "u"): "ʾ",                                          # (a-)qraʾu (أقرأ hamza)
    ("yu", "allim"): "ʿ", ("jum", "a"): "ʿ", ("yuṭ", "im"): "ʿ",                        # yuʿallimu, jumʿa*, wa-yuṭʿim (RÉVISION ("yuṭ","ima"):ʾ, consignée)
    ("mu", "aṣfarāt"): "ʾ",                                                          # muʾaṣfarāt (RÉVISION ("mu","aṣfar"):ʿ W20, consignée)
    ("a", "am"): "ʿ", ("ṭa", "ana"): "ʿ", ("ṭa", "ma"): "ʿ", ("murāja", "at"): "ʿ",      # al-aʿamm, ṭaʿana, ṭaʿma, (wa-)murājaʿat
    ("yurāji", "u"): "ʿ", ("a", "dh"): "ʿ", ("ta", "adh"): "ʿ",                          # yurājiʿu, l-aʿdhār (عذر ʿ), t-taʿadhdhī (تعادي)
    ("naṣna", "u"): "ʿ", ("yaṣna", "u"): "ʿ", ("yaṣna", "ūn"): "ʿ", ("taṣna", "u"): "ʿ",  ("aṣna", "u"): "ʿ", # صنع conjuguées
    ("ṣana", "a"): "ʿ", ("ṣana", "n"): "ʿ",                                            # ṣanaʿahā/wa-ṣanaʿnāhā/ṣanaʿnā (≠ ("ṣana","ta"):ʾ, consigné)
    ("jam", "an"): "ʿ", ("jam", "i"): "ʿ", ("i", "til"): "ʿ", ("i", "tinā"): "ʿ",        # jamʿan, l-jamʿi, al-iʿtilāl, al-iʿtināʾ 1er signe
    ("i'tinā", "i"): "ʾ", ("i", "āna"): "ʿ", ("i", "ādah"): "ʿ",                        # al-iʿtināʾ 2e signe (hamza), iʿāna (عون), al-iʿādah (عاود)
    ("ifti", "āl"): "ʿ", ("ibt", "ād"): "ʿ", ("mu", "aqqat"): "ʾ", ("ta", "ṭal"): "ʿ",    # iftiʿāl, (l-)ibtʿād (ابتعاد), l-muʾaqqati (وقت hamza), taʿṭalat
    ("chi", "b"): "ʿ", ("chi", "ār"): "ʿ", ("chu", "an"): "ʿ", ("bi", "r"): "ʾ",          # bi-ch-chiʿb, chiʿār (شعار), chuʿanān (consigné), biʾr (بئر)
    ("bi", "thah"): "ʿ", ("maw", "id"): "ʿ", ("mawā", "īd"): "ʿ", ("mī", "ād"): "ʿ",      # al-biʿthah (البعثة), mawʿid/mawāʿīd/mīʿād (وعود)
    ("mata", "i"): "ʿ", ("mat", "a"): "ʿ", ("mutawaḍḍi", "an"): "ʾ", ("yabda", "u"): "ʾ",  # mataʿi (مَتَاع), mutawaḍḍiʾan (وضأ), yabdaʾu
    ("tāsi", "i"): "ʿ", ("mattasa", "an"): "ʿ", ("ista", "jal"): "ʿ", ("tawsi", "a"): "ʿ", # tāsiʿi, mattasaʿan (وسع), istaʿjalū, wa-tawsiʿatan
    ("i", "ma"): "ʿ", ("a", "lam"): "ʿ", ("ya", "udd"): "ʿ", ("ma", "āy"): "ʿ",           # (n_)iʿma (نِعْمَة), aʿlam, yaʿudd (عدّ), maʿāyīr (مِعْيَر)
    ("ma", "jūr"): "ʾ", ("ya", "ṭub"): "ʿ", ("mu", "dhiyya"): "ʾ", ("fa", "rat"): "ʾ",    # maʾjūr (مأجور), yaʿṭub, muʾdhiyya (آذى), al-faʾratu (فأرة)
    ("tha", "laba"): "ʿ", ("ka", "aba"): "ʿ", ("juz", "in"): "ʾ", ("as", "ra"): "ʾ",      # Thaʿlaba, Kaʿaba, juzʾin, asraʾ (أسرع)
    ("ṣu", "ūd"): "ʿ",                                                              # bi-ṣuʿūdi (صعود)
    ("ba", "s"): "ʾ", ("ba", "ath"): "ʿ", ("yas", "al"): "ʾ",                            # lā baʾs (بأس hamza), fa-baʿatha (بعث), yasʾal(u)
    ("ta", "ayy"): "ʿ", ("ta", "awwal"): "ʾ", ("ta", "sil"): "ʾ", ("akhṭa", "n"): "ʾ",     # fa-taʿayyanati (تعيّن), taʾawwalū (تأوّل), taʾsilannahu (تأصيل), akhṭaʾnā
    ("mucha", "ara"): "ʿ", ("al-mucha", "ara"): "ʿ", ("yutaba", "aḍ"): "ʿ",               # al-muchaʿʿara, yutabaʿʿaḍ (شعّر/تبعّض — ×2 signes)
    ("na", "am"): "ʿ", ("yasma", "a"): "ʿ",                                              # naʿam, yasmaʿa (سمع)
    ("al-mawḍi", ""): "ʿ", ("mawḍi", "u"): "ʿ", ("mawḍi", "un"): "ʿ",                      # al-mawḍiʿ (الموضع)
    ("khaṭa", "uh"): "ʾ", ("khaṭa", ""): "ʾ",                                            # khaṭaʾ* (خطأ hamza)
    ("cha", "nu"): "ʾ", ("ji", "tum"): "ʾ", ("naw", "a"): "ʿ", ("naw", "i"): "ʿ",          # chaʾnu (شأْن), jiʾtum (جئتم), nawʿa/i (نوع)
    ("wa-ajma", "a"): "ʿ", ("ajma", "a"): "ʿ", ("bi-daf", "i"): "ʿ", ("ṣu", "ūd"): "ʿ",    # wa-ajmaʿa (أجمع), bi-dafʿi, bi-ṣuʿūdi
    ("ya", "udd"): "ʿ", ("faq", "ud"): "ʿ",                                              # yaʿudd, (couvre existant)
    ("ach-char", ""): "ʿ", ("ach-chāri", ""): "ʿ", ("al-khāchi", ""): "ʿ",                 # ach-charʿu?? — couverture du 1er signe doublement?? — non : fins
    ("ch-cha", "r"): "ʿ", ("ach-cha", "r"): "ʿ", ("al-mucha", ""): "ʿ", ("yutaba", ""): "ʿ", # ch-chaʿr (2e signe chaʿr via tail), fins doubles
    ("cha", ""): "ʿ",                                                               # filet chaʿ (tout le reste cha'* = شع ʿayn)
    ("al-", ""): "ʿ",                                                               # filet al- (premier signe des doubles al-''X)
})
# W21 — finales :
WORD_FINAL.update({
    "chay": "ʾ", "ya": "ʾ",                                                       # chayʾ (شيء), yaʾ (letter yāʾ)
    "arba": "ʾ", "qra": "ʾ", "jad": "ʿ", "yṣna": "ʿ", "yaḍa": "ʿ",                  # arbaʾ, (a-)qraʾ, jadʿ, yṣnaʿ, yaḍaʿ
    "ḍabu": "ʿ", "chāri": "ʿ", "khāchi": "ʿ", "raj": "ʿ", "mawḍi": "ʿ",             # ḍabuʿ, ach-chāriʿ, al-khāchiʿ, rajʿ, al-mawḍiʿ
    "mucha": "ʿ", "yutaba": "ʿ", "yujma": "ʿ", "mujma": "ʿ", "tanqa": "ʿ",          # muchаʿʿ?? — canon : muchʿʿ/yutabaʿʿ 1ers signes, yujmaʿ, mujmaʿ, tanqaʿ
    "btada": "ʾ", "yarji": "ʿ", "aṣna": "ʿ", "yarka": "ʿ", "asra": "ʾ",             # btadaʾ, yarjiʿ, aṣnaʿ, yarkaʿ, asraʾ
    "waṭ": "ʾ", "qubu": "ʿ", "mudarra": "ʿ", "muḍabba": "ʿ",                        # waṭʾ (وطء hamza), qubuʿ/mudarraʿ/muḍabbaʿ (404, consignées)
})
WORD_INITIAL_HAMZA.add("immat")                                                   # aʾimmat al-fatwā (أئمة hamza)
'''
# nettoyage : le commentaire junk "muchа" (cyrillique) ne doit pas rester dans le code livré
MAP = MAP.replace("muchаʿʿ?? — canon : muchʿʿ/yutabaʿʿ 1ers signes, yujmaʿ, mujmaʿ, tanqaʿ",
                  "muchʿʿ/yutabaʿʿ 1ers signes, yujmaʿ, mujmaʿ, tanqaʿ")
MAP = MAP.replace('("ach-char", ""): "ʿ", ("ach-chāri", ""): "ʿ", ("al-khāchi", ""): "ʿ",                 # ach-charʿu?? — couverture du 1er signe doublement?? — non : fins\n    ', '')
s = s.replace("LONGVOWL_AYN = (", MAP + "\nLONGVOWL_AYN = (")
m = re.search(r'LONGVOWL_AYN = \(([^)]*)\)', s)
assert m, "LONGVOWL_AYN introuvable"
s = s.replace(m.group(0), 'LONGVOWL_AYN = (' + m.group(1) + ', "arji", "rji")')

ANCHOR = '''        return "ʾ", "inventaire signes (ṣ,ḍ,ṭ,ḥ,') → ʾ consigné"
'''
RULES = '''        return "ʾ", "inventaire signes (ṣ,ḍ,ṭ,ḥ,') → ʾ consigné"
    # W21 (hadith-3es) — doublement du tirage (''Amr, al-''Āṣ) : deux ' adjacents → ʿʿ (canon à un signe, consigné)
    if nxt_ch == "'" and (not prev_w or prev_w.endswith("-")):
        return "ʿ", "W21 1er signe du doublement (''X) → ʿ (canon X) consigné"
    if prev_w.endswith("'"):
        return "ʿ", "W21 2e signe du doublement → ʿ consigné"
    # W21 — inventaire des conventions "( ', ', ḥ, kh …)" : ʿ puis ʾ (consigné)
    if not prev_w and not nxt_w:
        pr2 = rendered[p - 1] if p >= 1 else ""
        if pr2 == "(" or (p >= 2 and rendered[p - 2] == "("):
            return "ʿ", "W21 1er signe inventaire conventions → ʿ consigné"
        if pr2 == "," or (p >= 2 and rendered[p - 2] == ","):
            return "ʾ", "W21 2e signe inventaire conventions → ʾ consigné"
    # W21 — mod' = مُدّ (l'apostrophe rend le dāl géminé, parallèle bat'an → battan)
    if not nxt_w and prev_w.lower().endswith("mod"):
        return "d", "W21 mod' = مُدّ (dāl géminé) consigné"
'''
assert ANCHOR in s, "ancre classify introuvable"
s = s.replace(ANCHOR, RULES)

compile(s, P, "exec")
open(P, "w", encoding="utf-8").write(s)
print("patch OK —", len(s), "car")
