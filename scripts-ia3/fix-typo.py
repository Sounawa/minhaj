#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IA-3 (W1) — correction typographique du secondaire (zone IA-3 : *-es / *-tanawi-*).

Actions sur les nœuds texte (hors balises, hors commentaires HTML, hors spans
arabe dir="rtl"/lang="ar" toutes formes, nested-aware) :
  - apostrophe droite ' → ’ (élision française) / ʿ (ʿayn) / ʾ (hamza) —
    convention §5 du protocole (ʾ après voyelle longue, ʿ pour le ʿayn),
    classée par règles + carte de mots vérifiés sur le corpus (17 nov. 2026) ;
  - U+202F avant ; : ! ? » (entité &nbsp; incluse) et après « ;
  - doubles espaces → simple.
Une incertaine = laissée droite + consignée (jamais devinée) : le doc n'est
pas écrit tant qu'une incertaine subsiste.
Porte QA : scripts-translate/qa-lesson.py (outil officiel) sur copie extraite.
Usage : python3 scripts-ia3/fix-typo.py --book fiqh-tanawi-3 --docs 15355,16211 [--dry]
"""
import argparse, json, re, subprocess, sys, os

NARROW = "\u202f"
DIAC = set("āīūṭḍḥṣẓḷṃṅġšṯẋĀĪŪṢḤ")

# carte de mots vérifiée sur le corpus (vérité terrain 17 nov. 2026) :
# ʾ pour la hamza après voyelle longue (Muwaṭṭaʾ ×39, ḥunafāʾ, al-ḥamrāʾ, ḥayāʾ) ;
# ʿ pour le ʿayn (ʿatīq ×44, ʿArafa, Jāmiʿ ×5, ʿUmar ×51 main — contre ’Umar ×228
# artefact blanket d'autres livres, divergence consignée au journal W2).
WORD_INITIAL_AYN = {"atīq", "afw", "iyāḍ", "abd", "amd", "arafa", "umar", "alā",
                    "an", "alay", "usri", "usr", "admata", "ayn", "aynin", "urūḍ",
                    "azl", "ādiyāt", "amal", "arḍin", "arḍi", "uzila", "iṣma",
                    "aqd", "inda", "ā", "abbās", "aqār", "illa", "alīch", "alīsh",
                    "urf", "imāra", "achar", "uqbarī", "iwaḍ", "araḍ", "ayb",
                    "ilm", "amr", "adīm", "uqba", "ichrūn", "inān", "iyāl",
                    "adāla", "allāma", "udhr", "n-n", "alī", "aliyy", "aqīda",
                    "azīz", "ulamā", "awad", "uthmān", "arabī"}
WORD_INITIAL_HAMZA = {"adam", "adaman", "ibtighā", "adhara", "astakhli",
                      "aw", "aḥadu", "ilā", "abīhi", "innī", "innamā",
                      "ab'adakanna"}   # ʾadam, ibtighāʾ, aʾdhara, ʾastakhliḍ/ṣ, ʾaw, ʾaḥadukum, ʾilā, ʾabīhi, ʾinnī, ʾinnamā, ʾab'adakanna (print)
WORD_FINAL = {"khul": "ʿ", "jāmi": "ʿ", "rābi": "ʿ", "raja": "ʿ", "bay": "ʿ",  # khulʿ, Jāmiʿ, rābiʿ, rajaʿa, bayʿ
              "tabarru": "ʾ", "malā": "ʾ", "khaṭā": "ʾ", "muwaṭṭa": "ʾ",
              "gharamā": "ʾ", "mawḍū": "ʾ", "ḥibā": "ʾ", "ḥidā": "ʾ",
              "juz": "ʾ", "mali": "ʾ",                                          # juzʾ, maliʾ (مليء)
              "far": "ʿ", "buḍ": "ʿ", "qiṭ": "ʿ", "taba": "ʿ", "tatabba": "ʿ",
              "tab": "ʿ", "sābi": "ʿ", "ṣāni": "ʿ", "waḍ": "ʿ", "manāfi": "ʿ",  # farʿ, buḍʿ, qiṭʿ, tabaʿ, tatabbaʿ, tabʿ, sābiʿ, ṣāniʿ, waḍʿ, manāfiʿ
              "ra": "ʾ", "mustaṣna": "ʾ",                                       # raʾs final (رأس), mustaṣnaʾ
              "rab": "ʿ", "rub": "ʿ", "nāfi": "ʿ", "ğam": "ʿ", "māni": "ʿ",     # rabʿ, rubʿ, Nāfiʿ, ğamʿ, māniʿ
              "tachaffu": "ʿ",                                                  # tachaffuʿ
              "ğāmi": "ʿ", "wa": "ʿ",                                           # Ğāmiʿ, waʿd (وعد)
              "tawāṭu": "ʾ", "tanāzu": "ʿ",                                     # tawāṭuʾ (تواطؤ), tanāzuʿ (تنازع)
              "zar": "ʿ", "naf": "ʿ", "ḍ": "ʿ",                                 # zarʿ, nafʿ, racine b-ḍ-ʿ
              "rafī": "ʿ", "tafarru": "ʿ", "marāği": "ʿ",                       # Rafīʿ, tafarruʿ, marāğiʿ
              "dharā'i": "ʿ",                                                   # dharāʾiʿ (ذرائع — double signe)
              "muwatta": "ʾ",                                                   # Muwattaʾ (الموطأ)
              "bad": "ʾ", "mutāba": "ʿ", "munqaṭi": "ʿ",                        # badʾ (بدء), mutābaʿa, munqaṭiʿ ×2
              "tābi": "ʿ", "nasa": "ʿ", "yabda": "ʾ", "yuwamma": "ʾ",           # tābiʿ, Nasaʿī, yabdaʾ, yuwammaʾ
              "hāni": "ʾ", "murtafi": "ʿ", "munaqaṭi": "ʿ", "bisab": "ʿ",       # Hāniʾ, murtafiʿ, munaqaṭiʿ, bisabʿ
              "mu": "ʾ",                                                        # mu''an → muʾʾan (1er signe ; incertaine consignée W11)
              "jawāmi": "ʿ", "raf": "ʾ",                                        # jawāmiʿ, rafʾ (الرفع)
              "yasma": "ʿ", "ṭa": "ʿ"}                                          # yasmaʿ, ṭaʿ (الطعن)
# couples (fin du mot avant ', début du mot après ') tranchés mot à mot —
# la lettre entre les deux morceaux n'est pas déductible du préfixe seul :
# taʿlīm/taʿzīr (ʿayn) mais taʾkhīr/taʾbīm (hamza) ; saʾala hamza mais aʿṭā ʿayn.
PAIR_MEDIAL = {("ta", "līm"): "ʿ", ("ta", "zīr"): "ʿ", ("ta", "khīr"): "ʾ",
               ("ta", "bīm"): "ʾ", ("mu", "ajja"): "ʿ", ("mu", "dim"): "ʿ",
               ("mu", "tāda"): "ʿ", ("mu", "ğama"): "ʿ", ("ma", "lūm"): "ʿ",
               ("ba", "di"): "ʿ", ("asta", "milu"): "ʿ", ("wa", "ada"): "ʿ",
               ("sa", "ala"): "ʾ", ("a", "ṭā"): "ʿ", ("yasa", "al"): "ʾ",
               ("ustu", "niya"): "ʿ", ("shari", "a"): "ʿ", ("charī", "a"): "ʿ",
               ("shar", "ī"): "ʿ",                                              # sharʿī (شرعي)
               ("raja", "a"): "ʿ", ("ya", "ti"): "ʾ",                           # rajaʿa (رجع), yaʾti (يأتي)
               ("fa", "īl"): "ʿ", ("maf", "ūl"): "ʿ", ("ra", "y"): "ʾ",         # faʿīl, mafʿūl, raʾy
               ("ğa", "ala"): "ʿ", ("muba", "bira"): "ʾ",                       # ğaʿala, mubaʾbira
               ("mu", "ayya"): "ʿ", ("ma", "dūm"): "ʿ", ("ma", "tūh"): "ʿ",     # muʿayyana, maʿdūm, maʿtūh
               ("waqa", "a"): "ʿ", ("mawqi", "a"): "ʿ", ("far", "ī"): "ʿ",      # waqaʿa, mawqiʿa, farʿī
               ("chāfi", "ī"): "ʿ",                                             # Chāfiʿī
               ("ma", "nā"): "ʿ", ("ra", "s"): "ʾ",                             # maʿnā, raʾs (رأس)
               ("sa", "d"): "ʿ", ("dfa", "ū"): "ʿ",                             # Saʿd, dfaʿū
               ("ma", "lūl"): "ʿ", ("ma", "a"): "ʿ", ("ma", "rūf"): "ʿ",        # maʿlūl, maʿa (مَعَ), maʿrūf
               ("mu", "aqqab"): "ʾ", ("mu", "āwa"): "ʿ", ("mu", "tama"): "ʿ",   # muʾaqqab, muʿāwaḍa, muʿtamad
               ("mu", "akhk"): "ʾ",                                             # muʾakhkhar
               ("char", "ī"): "ʿ", ("chaf", "a"): "ʿ",                          # charʿī, chafʿa
               ("musta", "rā"): "ʿ", ("isti", "rā"): "ʿ",                       # mustaʿrāʾ, istiʿrāʾ
               ("manfa", "a"): "ʿ",                                             # manfaʿa (منفعة)
               ("ta", "wīl"): "ʾ", ("i", "dār"): "ʾ", ("yu", "dhir"): "ʾ",      # taʾwīl, iʾdār, yuʾdhiru
               ("mu", "ğam"): "ʿ", ("ṭa", "ām"): "ʿ", ("ya", "nī"): "ʿ",        # muʿğam, ṭaʿām, yaʿnī
               ("ju", "l"): "ʿ", ("za", "āma"): "ʿ", ("za", "īm"): "ʿ",         # juʿl, zaʿāma, zaʿīm
               ("a", "dhara"): "ʾ", ("wa", "d"): "ʿ", ("ba", "īr"): "ʿ",        # aʾdhara, waʿd, baʿīr
               ("muta", "addin"): "ʿ", ("ta", "addud"): "ʿ",                    # mutaʿaddin, taʿaddud
               ("char", "an"): "ʿ", ("ta", "līl"): "ʿ",                         # charʿan, taʿlīl
               ("ma", "dim"): "ʿ", ("ma", "rā"): "ʾ",                           # maʿdim (معدم), maʾrā (مَعْرَاء — incertaine consignée)
               ("da", "wā"): "ʿ", ("mu", "add"): "ʿ",                           # daʿwā, muʿaddī/muʿaddā
               ("ni", "ma"): "ʿ", ("ya", "qid"): "ʿ", ("tana", "qid"): "ʿ",     # niʿma, yaʿqid, tanaʿqid
               ("i", "āra"): "ʾ", ("ista", "lafa"): "ʾ", ("isti", "lāf"): "ʾ",  # iʾāra, istaʾlafa, istiʾlāf
               ("ma", "īb"): "ʿ", ("aqa", "ada"): "ʾ", ("ta", "addī"): "ʿ",     # maʿīb, aqaʾada, taʿaddī
               ("aqṭa", "a"): "ʿ", ("ma", "din"): "ʿ", ("ma", "īn"): "ʿ",       # aqṭaʿa, maʿdin, maʿīn
               ("mu", "īn"): "ʿ", ("ẓam", "ān"): "ʾ", ("rab", "ī"): "ʿ",        # muʿīn, ẓamʾān, Rabʿī
               ("i", "tirā"): "ʾ", ("i", "lām"): "ʾ", ("isti", "āra"): "ʾ",     # iʾtirāḍ, iʾlām, istiʾāra
               ("ra", "ūf"): "ʾ", ("chāfi", "it"): "ʿ", ("ri", "āsa"): "ʾ",     # Raʾūf, chāfiʿite, riʾāsa
               ("ma", "ārif"): "ʿ", ("mar", "ab"): "ʿ", ("ta", "rīf"): "ʾ",     # maʿārif, Marʿab, Taʾrīfāt
               ("ja", "fī"): "ʿ", ("fu", "ād"): "ʾ",                            # Jaʿfī, Fuʾād
               ("a", "lām"): "ʾ", ("ach", "ath"): "ʿ", ("chu", "ayb"): "ʿ",     # aʾlām, Achʾath?? — Achʿath (الأشعث)
               ("sa", "īd"): "ʿ", ("ya", "qūb"): "ʿ", ("mu", "assa"): "ʾ",      # Saʿīd, Yaʿqūb, Muʾassasa
               ("maṭba", "at"): "ʿ", ("sa", "āda"): "ʾ", ("ru", "īn"): "ʾ",     # maṭbaʿa, saʾāda, Ruʾīnī (incertaine consignée)
               ("mu", "ādh"): "ʿ", ("ma", "bad"): "ʿ", ("tha", "ālab"): "ʿ",    # Muʿādh, Maʿbad, Thaʿālabī
               ("ja", "far"): "ʿ", ("mu", "jam"): "ʿ", ("mu", "āṣir"): "ʿ",     # Jaʿfarī, muʿjam, muʿāṣira
               ("a", "rāb"): "ʿ", ("na", "īm"): "ʿ",                            # Aʿrāb (أعراب), Naʿīm
               ("isti", "āra"): "ʿ",                                            # CORRECTION W10 : istiʿāra = الاستعارة ʿayn (était ʾ — erreur)
               ("qur", "ān"): "ʾ", ("mu", "alla"): "ʿ", ("ach", "arī"): "ʿ",    # Qurʾān ×15, muʿallal, Achʿarī
               ("ma", "ālim"): "ʿ", ("na", "layn"): "ʿ", ("chu", "ba"): "ʿ",    # Maʿālim, naʿlayn, Chuʿba
               ("ḍa", "īf"): "ʿ", ("ḍa", "f"): "ʿ", ("mu", "ḍal"): "ʿ",         # ḍaʿīf ×1, ḍaʿf, muʿḍal
               ("mutāba", "a"): "ʿ",                                            # mutābaʿa (متابعة)
               ("tābi", "ūn"): "ʿ", ("bardha", "ī"): "ʿ", ("isti", "āna"): "ʿ", # tābiʿūn, Bardhaʿī, istiʿāna
               ("a", "raj"): "ʿ", ("ma", "rifa"): "ʿ", ("yu", "tar"): "ʿ",      # Aʿraj, Maʿrifa, yuʿtar
               ("mu", "tazi"): "ʿ", ("mutāba", "āt"): "ʿ", ("dhu", "ayb"): "ʿ", # muʿtazilite, mutābaʿāt, Dhuʿayb
               ("yaj", "al"): "ʾ", ("nasa", "ī"): "ʿ", ("yuwamma", "u"): "ʾ",   # yajʿal, Nasaʿī, yuwammaʾu
               ("mu", "an'an"): "ʿ", ("mu'an", "an"): "ʿ",                      # muʿanʿan (les deux signes)
               ("mu", "annan"): "ʾ", ("mou", "annan"): "ʾ",                     # muʾannan, mouʾannanoun (glose du doc)
               ("mu", "an"): "ʾ",                                               # mu''an 2e signe → muʾʾan (incertaine consignée)
               ("an", "ana"): "ʿ", ("hāni", "in"): "ʾ", ("raka", "a"): "ʿ",     # ʿanʿana, Hāniʾin, rakaʿa
               ("āfi", "ī"): "ʾ", ("ya", "lū"): "ʿ", ("irtafa", "a"): "ʾ",      # al-āfiʾī (OCR cité — consignée), yaʿlū, irtafaʾa
               ("shu", "ba"): "ʿ", ("sam", "ān"): "ʿ",                          # Shuʿba, Samʿānī
               ("i", "nana"): "ʿ", ("sami", "at"): "ʿ",                         # iʿnana (العِنان), samiʿat
               ("mas", "ūd"): "ʿ", ("a", "mach"): "ʿ", ("ṣan", "ānī"): "ʿ",     # Masʿūd, Aʿmach, Ṣanʿānī
               ("cha", "īrin"): "ʾ", ("qiṭ", "at"): "ʿ", ("yamna", "u"): "ʿ",   # chaʾīrin, qiṭʿatun, yamnaʿu
               ("a", "yāhu"): "ʾ", ("a", "ḍalahu"): "ʾ", ("tābi", "ī"): "ʿ",    # aʾyāhu, aʾḍalahu, tābiʿī
               ("ḍu", "afā"): "ʿ", ("i", "ḍāl"): "ʾ", ("i", "rsāl"): "ʾ",       # ḍuʿafā, iʾḍāl, iʾrsāl
               ("ya", "jal"): "ʾ", ("yu", "raf"): "ʿ", ("munqaṭi", "s"): "ʿ",   # yaʾjal, yuʿraf, munqaṭiʿs
               ("kānatimra", "at"): "ʾ",                                        # kānatimraʾatī (amalgame d'imprimé)
               ("i", "dād"): "ʾ", ("ab", "adakanna"): "ʿ",                      # iʾdād, abʿadakanna (print)
               ("mu", "ḍil"): "ʿ", ("yum", "i"): "ʿ", ("yum'i", "aḥ"): "ʾ",     # muʿḍila, yumʿiʾaḥadukum (2e signe)
               ("i", "aḥadukum"): "ʾ",                                          # ʾaḥadukum
               ("a", "mālu"): "ʿ", ("ya", "uqqu"): "ʿ", ("cha", "bī"): "ʿ",     # aʿmālu, yaʿqqu, Chaʿbī
               ("tajtami", "u"): "ʾ", ("ḍa", "āmahu"): "ʾ",                     # tajtamiʾu, ḍaʾāmahu (récusée — consignée)
               ("yu", "mar"): "ʾ", ("isti", "dhān"): "ʾ",                       # yuʾmar, istiʾdhān
               ("fi", "lin"): "ʿ", ("tābi", "īn"): "ʿ", ("raf", "an"): "ʾ",     # fiʿlin, tābiʿīn, rafʾan
               ("yarfa", "uhu"): "ʾ", ("shāfi", "īt"): "ʿ"}                     # yarfaʾuhu, shāfiʿītes
LONGVOWL_AYN = ("charī", "shari", "maqṭū", "marfū")   # sharīʿa / maqṭūʿ / marfūʿ : ʿayn (pas hamza) après ī/ū
FRENCH_ELISION = {"l", "d", "n", "s", "j", "c", "m", "t", "qu", "jusqu", "lorsqu",
                  "puisqu", "quelqu", "aujourd"}
ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]")


def tokenize(html):
    """[(kind, texte)] kind ∈ {text, tag, comment, prot} ; spans arabe protégés
    (toutes formes d'attributs, nested-aware par profondeur)."""
    out, i, ar_depth = [], 0, 0
    for m in re.finditer(r"<!--.*?-->|<[^>]+>", html, flags=re.S):
        if m.start() > i:
            out.append(("prot" if ar_depth else "text", html[i:m.start()]))
        tok = m.group(0)
        low = tok.lower()
        if low.startswith("<!--"):
            out.append(("comment", tok))
        elif low.startswith("</span"):
            if ar_depth:
                ar_depth -= 1
            out.append(("prot", tok))
        elif low.startswith("<span"):
            if ('dir="rtl"' in tok or "dir='rtl'" in tok or 'lang="ar"' in tok
                    or "lang='ar'" in tok):
                ar_depth += 1
            out.append(("prot", tok))
        else:
            out.append(("prot", tok))
        i = m.end()
    if i < len(html):
        out.append(("prot" if ar_depth else "text", html[i:]))
    return out


def word_before(rendered, p):
    """mot avant la position p — traverse une apostrophe interne de
    translittération (dharāʾiʿ : le second signe voit le premier)."""
    w, k = [], p - 1
    while k >= 0 and (rendered[k].isalnum() or rendered[k] in DIAC
                      or rendered[k] == "-" or rendered[k] == "'"):
        w.append(rendered[k]); k -= 1
    return "".join(reversed(w))


def word_after(rendered, p):
    w, k = [], p + 1
    while k < len(rendered) and (rendered[k].isalnum() or rendered[k] in DIAC or rendered[k] == "-"):
        w.append(rendered[k]); k += 1
    return "".join(w)


def classify(rendered, p):
    """→ (char|None, raison) pour l'apostrophe droite à la position p."""
    prev_w = word_before(rendered, p)
    nxt_w = word_after(rendered, p)
    nxt_ch = rendered[p + 1] if p + 1 < len(rendered) else ""
    # inventaire de signes : (ṣ, ḍ, ṭ, ḥ, ') → ʾ (parallèle Muwaṭṭaʾ, incertaine consignée)
    if nxt_ch == ")" and re.search(r"[,;] $", rendered[max(0, p - 3):p]):
        return "ʾ", "inventaire signes (ṣ,ḍ,ṭ,ḥ,') → ʾ consigné"
    if (not prev_w or prev_w.endswith("-")) and nxt_w:         # ' initial de mot (préfixes al-, bi-, wa-…)
        nx = nxt_w.lower()
        nx2 = nx.lstrip("-")                                   # racines « '-n-n » : hyphen initial
        if nx in WORD_INITIAL_HAMZA or nx2 in WORD_INITIAL_HAMZA \
                or any(nx.startswith(x) for x in WORD_INITIAL_HAMZA if len(x) > 4):
            return "ʾ", f"hamza initial ({prev_w or ''}{nxt_w})"
        # règle générale (convention corpus W8) : ' initial = ʿayn par défaut
        # (ʿAbd, ʿAlī, ʿilm, ʿĪsā, ʿulamāʾ…) ; l'hamza initiale est l'exception ci-dessus.
        return "ʿ", f"ʿayn initial ({prev_w or ''}{nxt_w})"
    if not nxt_w and prev_w:                                   # ' final de mot
        base = prev_w.rstrip("-")                              # racines « b-ḍ-' » : hyphen final
        tail = base.rsplit("-", 1)[-1]
        if prev_w[-1] in "āīūĀĪŪ":
            return "ʾ", f"hamza après voyelle longue ({prev_w})"
        for cand in (base, tail):
            if cand.lower() in WORD_FINAL:
                return WORD_FINAL[cand.lower()], f"carte mot final ({cand})"
        return None, f"final non cartographié ('{prev_w}')"
    if prev_w and nxt_w:                                       # ' médial
        prev_tail = prev_w.rstrip("-").rsplit("-", 1)[-1].lower().strip("'")
        for p0, n0 in sorted(PAIR_MEDIAL, key=lambda k: -len(k[1])):  # préfixes les plus longs d'abord
            if prev_tail == p0 and nxt_w[:len(n0)].lower() == n0:
                return PAIR_MEDIAL[(p0, n0)], f"carte couple ({p0}'{n0}…)"
        if prev_w.endswith(LONGVOWL_AYN):
            return "ʿ", f"ʿayn après voyelle longue ({prev_w}'{nxt_w})"
        if prev_w[-1] in "āīūĀĪŪ":
            return "ʾ", f"hamza médiale après voyelle longue ({prev_w}'{nxt_w})"
        if prev_w.lower() in FRENCH_ELISION and not (set(nxt_w) & DIAC):
            return "’", f"élision française ({prev_w}'{nxt_w})"
        return None, f"médial non classé ({prev_w}'{nxt_w})"
    return None, "cas dégénéré"


def fix_text_segment(s):
    """U+202F + doubles espaces (règles de qa-lesson.py). Les entités sont
    converties avant ponc (&nbsp;: → \u202f:) puis PROTÉGÉES — leur ';' interne
    ne doit jamais être pris pour une ponctuation française."""
    s = re.sub(r"&nbsp;(?=[;:!?»])", NARROW, s)
    s = s.replace("«&nbsp;", "«" + NARROW)
    ents = []
    def _p(m):
        ents.append(m.group(0))
        return "\x00%d\x00" % (len(ents) - 1)
    s = re.sub(r"&[a-zA-Z]+;|&#\d+;", _p, s)
    s = re.sub(r"[ \u00a0\u202f]*([;:!?»])", NARROW + r"\1", s)
    s = re.sub(r"«[ \u00a0\u202f]*", "«" + NARROW, s)
    s = re.sub(r" {2,}", " ", s)
    s = re.sub(r"\x00(\d+)\x00", lambda m: ents[int(m.group(1))], s)
    return s


def fix_html(html, dry):
    segs = tokenize(html)
    rendered, posmap = [], []
    for si, (kind, s) in enumerate(segs):
        if kind == "text":
            for off in range(len(s)):
                rendered.append(s[off]); posmap.append((si, off))
    rendered = "".join(rendered)
    segs2 = [list(x) for x in segs]
    decisions, uncertainties = [], []
    for m in re.finditer("'", rendered):
        p = m.start()
        ch, why = classify(rendered, p)
        if ch is None:
            uncertainties.append((p, rendered[max(0, p - 30):p + 30]))
            continue
        si, off = posmap[p]
        segs2[si][1] = segs2[si][1][:off] + ch + segs2[si][1][off + 1:]
        decisions.append((p, rendered[max(0, p - 22):p + 22], ch, why))
    prot_ok = all(s == s2 for (k, s), (k2, s2) in zip(segs, segs2) if k != "text")
    out = []
    for (kind, s), s2 in zip(segs, [x[1] for x in segs2]):
        out.append((kind, fix_text_segment(s2) if (kind == "text" and not dry) else s))
    fixed = "".join(s for _, s in out)
    return fixed, decisions, uncertainties, prot_ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True)
    ap.add_argument("--docs", required=True)  # ids séparés par des virgules
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    path = f"content/books/{args.book}.json"
    raw = open(path, encoding="utf-8").read()
    book = json.loads(raw)
    trail = "\n" if raw.endswith("\n") else ""
    assert json.dumps(book, ensure_ascii=False, indent=2) + trail == raw, "round-trip JSON != fichier"

    ids = [x.strip() for x in args.docs.split(",")]
    docs = ([book["intro"]] if book.get("intro") else []) + book.get("lessons", [])
    n_written = 0
    for did in ids:
        d = [x for x in docs if str(x.get("docId")) == did][0]
        html = d.get("htmlFr") or ""
        if "://" in html:
            print(f"{did}: ⚠ '://' présent — vérifier le diff ':'")
        fixed, decisions, uncertainties, prot_ok = fix_html(html, args.dry)
        print(f"=== {did} | {len(decisions)} apostrophes classées, {len(uncertainties)} incertaines, protégés {'OK' if prot_ok else 'DIFF!'}")
        for p, ctx, ch, why in decisions:
            print(f"  {ch} {ctx!r}  [{why}]")
        for p, ctx in uncertainties:
            print(f"  ? INCERTAINE {ctx!r}")
        o, c = fixed.count("«"), fixed.count("»")
        bal = all(len(re.findall(rf"<{t}[ >]", fixed)) == len(re.findall(rf"</{t}>", fixed))
                  for t in ("h1", "h2", "h3", "p", "ul", "ol", "li", "em", "strong", "span", "td", "tr", "table"))
        ar_txt = len(ARABIC.findall("".join(s for k, s in tokenize(fixed) if k == "text")))
        print(f"  guillemets {o}/{c} {'OK' if o == c else 'DIFF'} | balises {'OK' if bal else 'DIFF'} | arabe hors span: {ar_txt}")
        if uncertainties or not prot_ok or o != c or not bal or ar_txt:
            print("  → doc NON écrit (à trancher)")
            continue
        n_written += 1
        if args.dry:
            continue
        d["htmlFr"] = fixed
        os.makedirs("scripts-ia3/tmp", exist_ok=True)
        tmp = f"scripts-ia3/tmp/{did}.html"
        open(tmp, "w", encoding="utf-8").write(fixed)
        r = subprocess.run([sys.executable, "scripts-translate/qa-lesson.py", tmp],
                           capture_output=True, text=True)
        print("  qa-lesson:", (r.stdout.strip() or r.stderr.strip()).replace("\n", " | "))
    if not args.dry and n_written:
        json.dump(book, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        if trail:
            open(path, "a", encoding="utf-8").write(trail)
        print(f"livre réécrit : {path} ({n_written} docs)")


if __name__ == "__main__":
    main()
