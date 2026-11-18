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
                      "aw", "aḥad", "idhā", "ilā", "abīhi", "innī", "innamā",
                      "ab'adakanna", "andād",                       # ʾadam, ibtighāʾ, aʾdhara, ʾastakhliḍ/ṣ, ʾaw, ʾaḥadukum, ʾilā, ʾabīhi, ʾinnī, ʾinnamā, ʾab'adakanna (print), ʾandād
                      "aṭaytuk", "ujjila", "alif"}                  # W17 (fiqh-tanawi-1) : ʾataytuk (أتيتك), ʾujjila (أُجِّل), ʾalif (الألف) — cartes R714-R715d
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
              "yasma": "ʿ", "ṭa": "ʿ",                                          # yasmaʿ, ṭaʿ (الطعن)
              "yaḍṭaji": "ʿ", "qaṭ": "ʿ", "mauḍi": "ʿ",                         # yaḍṭajiʿ, qaṭʿ, mauḍiʿ
              "mutābi": "ʿ", "jam": "ʿ",                                        # mutābiʿ, jamʿ (الجمع)
              "san": "ʿ",                                                       # sanʿ (OCR cité — récusé)
              "muqri": "ʿ",                                                     # muqriʿ (المقرئ)
              "naw": "ʿ",                                                       # nawʿ (النوع)
              "mukhtara": "ʾ", "yatabawwa": "ʾ",                                # mukhtaraʾ (المختار), yatabawwaʾ
              "qawāṭi": "ʿ", "mal": "ʾ",                                        # Qawāṭiʿ, Malʾ (ملء)
              "marāji": "ʿ"}                                                    # marājiʿ (المراجع, graphie j)
# W17 (fiqh-tanawi-1, cartes R714-R715d) — finales :
WORD_FINAL.update({"tawābi": "ʿ", "sila": "ʿ", "tāsi": "ʿ", "majma": "ʿ",
                   "mawāni": "ʿ", "tabi": "ʿ", "taqṭa": "ʿ", "ḍa": "ʿ",
                   "ḍar": "ʿ", "daf": "ʿ", "judh": "ʿ", "shar": "ʿ",         # tawābiʿ, as-silaʿ, at-tāsiʿ, majmaʿ, mawāniʿ, tabiʿ, taqṭaʿ, ḍaʿ, ḍarʿ (الضَّرْع), ad-dafʿ, al-judhʿ, ash-sharʿ
                   "laba": "ʾ", "istiqra": "ʾ", "sa": "ʾ"})                  # labaʾ (اللَّبَأ), istiqraʾ (الاستقراء), as-saʾ (السَّاء)
# finales ʿayn après voyelle longue — la règle « ā/ī/ū → ʾ » est suspendue pour
# ces racines en ʿ (ijtimāʿ, ijmāʿ, dhirāʿ, intifāʿ, madfūʿ, buyūʿ, mabīʿ, maklūʿ) :
WORD_FINAL_LONG_AYN = {"ijtimā", "ijmā", "dhirā", "intifā",
                       "madfū", "bayū", "buyū", "mabī", "maklū"}
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
               ("i", "nana"): "ʿ", ("sami", "at"): "ʿ", ("ruk", "at"): "ʿ",                         # iʿnana (العِنان), samiʿat
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
               ("yarfa", "uhu"): "ʾ", ("shāfi", "īt"): "ʿ",                     # yarfaʾuhu, shāfiʿītes
               ("ta", "ammud"): "ʿ", ("ta", "lamu"): "ʿ", ("naw", "āni"): "ʿ",  # taʿammud, taʿlamu, nawʿāni
               ("ma", "mar"): "ʿ", ("i", "lāl"): "ʾ", ("jam", "in"): "ʿ",       # Maʿmar, iʾlāl, jamʿin
               ("muta", "ammid"): "ʿ", ("yatabawwa", "a"): "ʾ",                 # mutaʿammidan, yatabawwaʾa
               ("maq", "adahu"): "ʿ", ("yan", "arif"): "ʿ", ("rak", "a"): "ʿ",  # maqʿadahu, yanʿarif, rakʿa
               ("ta", "ammul"): "ʾ", ("yata", "arraf"): "ʿ", ("luhay", "a"): "ʾ", # taʾammul, yataʿarraf, Luhayʾa
               ("mu", "aḍḍal"): "ʾ",                                            # muʾaḍḍal (incertaine consignée W12 — lecture muʿḍal possible)
               ("ṣana", "ta"): "ʾ", ("sami", "tu"): "ʿ", ("ta", "lama"): "ʿ",    # ṣanaʾta, samiʿtu, taʿlama
               ("sa", "altu"): "ʾ", ("a", "war"): "ʿ", ("ma", "nan"): "ʿ",      # saʾaltu, Aʿwar, maʿnan
               ("chi", "ta"): "ʾ", ("ba", "ḍi"): "ʿ", ("a", "immati"): "ʾ",     # chiʾta, baʿḍi, aʾimmati
               ("muṭṭali", "īna"): "ʿ", ("ḍabba", "ī"): "ʿ", ("na", "lam"): "ʿ", # muṭṭaliʿīna, Ḍabbaʿī, naʿlam
               ("faq", "ud"): "ʿ", ("taf", "ud"): "ʿ", ("yu", "taqad"): "ʿ",    # faqʿud, tafʿud (récusan), yuʿtaqad
               ("a", "qābi"): "ʿ", ("yuṭ", "ima"): "ʾ", ("ma", "ak"): "ʿ",      # aʿqābi, yuṭʾima, maʿak
               ("ji", "tuhum"): "ʾ", ("ba", "da"): "ʿ",                         # jiʾtuhum, baʿda
               ("ṣan", "ā"): "ʿ", ("mu", "āwiya"): "ʿ", ("ruf", "ahu"): "ʾ",    # Ṣanʿāʾ (1er signe), Muʿāwiya, rufʾahu
               ("yaqa", "u"): "ʿ", ("ya", "khudhna"): "ʾ", ("mu", "talif"): "ʾ", # yaqaʿu, yaʾkhudhna, muʾtalif
               ("ru", "ūs"): "ʾ",                                               # ruʾūs (رؤوس)
               ("muḍa", "ṭṭaf"): "ʿ", ("a", "ẓamu"): "ʿ", ("taj", "alū"): "ʾ",  # muḍaʿṭaf, aʿẓamu, tajʾalū
               ("taj", "ala"): "ʾ", ("ra", "aytu"): "ʾ",                        # tajʾala, raʾaytu (رأيت)
               ("ya", "taqidu"): "ʿ", ("ta", "lamūn"): "ʿ", ("taq", "uda"): "ʿ", # yaʿtaqidu, taʿlamūn, taqʿuda
               ("ta", "aṣṣub"): "ʿ", ("ju", "fī"): "ʿ", ("ta", "dīl"): "ʿ",     # taʿaṣṣub, Juʿfī, taʿdīl
               ("ya", "rifhu"): "ʿ", ("khaṭa", "uhu"): "ʾ", ("sabī", "ī"): "ʿ", # yaʿrifhu, khaṭaʾuhu, Sabīʿī
               ("ta", "ṣīm"): "ʿ", ("ya", "hadu"): "ʿ", ("chay", "i"): "ʾ",     # taʿṣīm, yaʿhadu (lecture consignée W15), chayʾi
               ("waḍa", "ū"): "ʾ", ("i", "tibāri"): "ʾ", ("ra", "nu"): "ʾ",     # waḍaʾū, iʾtibār, raʾnu (OCR tronqué)
               ("ajma", "ū"): "ʿ", ("ḍa", "fihī"): "ʾ", ("muta", "abbid"): "ʿ", # ajmaʿū, ḍaʾfihī, mutaʿabbidīn
               ("musta", "mal"): "ʿ", ("shu", "ab"): "ʿ",                       # mustaʿmal, Shuʿab
               ("zur", "a"): "ʾ", ("ta", "mīm"): "ʿ", ("ma", "idatu"): "ʾ",     # Zurʾa, taʿmīm, maʾidatu
               ("waḍ", "i"): "ʿ", ("waḍ", "u"): "ʿ", ("arba", "a"): "ʾ",        # waḍʿi/waḍʿu, arbaʿa
               ("yaqi", "u"): "ʿ", ("yaqṭa", "uhā"): "ʿ", ("ya", "idu"): "ʾ",   # yaqiʿu, yaqṭaʿuhā, yaʾidu (OCR récusé — consignée)
               ("i", "jām"): "ʿ",                                               # iʿjām (الإعجام)
               ("a", "rāḍi"): "ʿ", ("arba", "in"): "ʾ", ("ṭa", "n"): "ʿ",       # aʿrāḍi, arbaʿin, ṭaʿn
               ("ta", "ālā"): "ʿ", ("ya", "tuddu"): "ʿ", ("tibi", "ī"): "ʿ",    # taʿālā, yaʿtuddu, Tibiʿī (forme fautive)
               ("mu", "ṭī"): "ʿ", ("qal", "ajī"): "ʿ", ("ma", "ānī"): "ʿ",      # Muʿṭī, Qalʿajī, maʿānī
               ("mu", "aẓẓam"): "ʿ", ("ya", "lā"): "ʿ", ("am", "an"): "ʾ",      # Muʿaẓẓam, Yaʿlā, al-amʾan (المأمن, print)
               ("wāqi", "ayn"): "ʿ", ("mu", "all"): "ʿ",                        # wāqiʿayn, muʿall (المعلّ)
               ("mun", "im"): "ʿ", ("maṭba", "a"): "ʿ", ("mu", "minīn"): "ʾ",   # Munʿim, Maṭbaʿa, muʾminīn
               ("arna", "ūṭ"): "ʾ"}                                             # Arnaʾūṭ (الأرناؤط)
# W18 (fiqh-tanawi-2, cartes R714-R715d + arbitrages du tour) — couples médiaux :
PAIR_MEDIAL.update({
    ("a", "dama"): "ʿ", ("a", "qār"): "ʿ", ("af", "āl"): "ʿ",                    # (A)ʿdama, al-aʿqār, afʿāl
    ("a", "ẓamī"): "ʿ",                                                          # al-Aʿẓamī (الأعظمي — révision du supp ʾʿ, signe unique = ʿayn)
    ("ash", "ath"): "ʿ", ("aṣma", "ī"): "ʿ",                                     # al-Ashʿath, al-Aṣmaʿī (révisions du supp ʾ — canon ʿayn)
    ("di", "āma"): "ʿ",                                                          # Qatāda b. Diʿāma (tel qu'imprimé دِعامة — canon دِئامة consigné)
    ("i", "dhānan"): "ʾ", ("i", "mār"): "ʿ", ("i", "tiqād"): "ʿ",                # iʾdhānan (الإذناء), iʿmār (الإعمار), iʿtiqād
    ("iṣ", "āf"): "ʿ", ("iṣṭana", "a"): "ʿ", ("lum", "at"): "ʿ",                 # Iṣʿāf (إصعاف), iṣṭanaʿa, Lumʿat (اللمعة)
    ("lu'lu", "a"): "ʾ", ("lu", "lu"): "ʾ", ("la", "ālī"): "ʾ",                  # luʾluʾa, Luʾluʾ, laʾālīʾ (لؤلؤ/لألئ, hamza)
    ("ma", "dan"): "ʿ", ("ma", "dhūn"): "ʾ", ("ma", "lūfan"): "ʿ",               # Maʿdan, maʾdhūn (مأذون), maʿlūfan
    ("ma", "wūḍ"): "ʿ", ("ma", "ālāt"): "ʿ", ("ma", "ṣara"): "ʿ",                # maʿwūḍ, maʿālāt, maʿṣara
    ("mar", "ashlī"): "ʿ", ("mar", "ā"): "ʿ", ("mazra", "a"): "ʿ",               # al-Marʿashlī, marʿā, mazraʿa
    ("mu", "awwana"): "ʿ", ("mu", "lim"): "ʿ", ("mu", "īr"): "ʿ",                # (A)l-Muʿawwana, al-muʿlim (المعلّم, print), al-muʿīr
    ("musta", "īr"): "ʿ", ("muta", "allim"): "ʿ", ("nu", "aym"): "ʿ",            # al-mustaʿīr, mutaʿallim, Nuʿaym
    ("nu", "mān"): "ʿ", ("ru", "aynī"): "ʾ",                                     # al-Nuʿmān, al-Ḥaṭṭāb al-Ruʾaynī (الرُّؤَيْنِي hamza, d. 954 H)
    ("ta", "ajjal"): "ʿ", ("ta", "ajjala"): "ʿ", ("ta", "yīn"): "ʿ",             # taʿajjala (تعجّل ʿayn, ≠ taʾajjala), taʿyīn
    ("yardu", "u"): "ʾ", ("ḍay", "a"): "ʾ", ("ṭubi", "a"): "ʿ"})                 # yarduʾa (ر-ض-أ), ḍayʾa (ضَيْئة loss), ṭubiʿa
# W19 (faraid-tanawi-3, cartes R714-R715d + arbitrages du tour) — couples médiaux :
PAIR_MEDIAL.update({
    ("ba", "charīna"): "ʿ", ("da", "m"): "ʿ",                                    # bacharīna (بشر), daʿm (دعم)
    ("chay", "u"): "ʾ", ("chā'i", "in"): "ʾ",                                    # chayʾu/chāʾiʾin (شيء, graphie ch du tirage)
    ("imru", "un"): "ʾ", ("qor", "ān"): "ʾ",                                     # imruʾun (امرؤ), Qorʾān (graphie q)
    ("joum", "a"): "ʿ", ("joum", "āt"): "ʿ", ("jāmi", "a"): "ʿ",                 # joumʿa/āt, jāmiʿa
    ("ma", "jam"): "ʿ", ("ma", "āda"): "ʿ",                                      # majmaʿ, maʿāda
    ("mas", "ala"): "ʾ", ("mas", "alatayn"): "ʾ", ("yas", "alūnaka"): "ʾ",       # masʾala(tayn) (مسألة), yasʾalūnaka
    ("mu", "tabara"): "ʿ", ("mu", "tiq"): "ʿ", ("mu", "ūnat"): "ʿ",              # muʿtabar, muʿtiq, muʿūnat
    ("muta", "addid"): "ʿ", ("ta", "malu"): "ʿ", ("ta", "mīr"): "ʿ",             # mutaʿaddid, taʿmalu, taʿmīr(i)
    ("ta", "mīri"): "ʿ", ("ta", "sīb"): "ʿ", ("ta", "ṣīl"): "ʿ",                 # taʿmīri, taʿṣīb (التعصيب), taʿṣīl
    ("ta", "ṣīb"): "ʿ", ("ta", "īl"): "ʿ",                                       # taʿṣīb, taʿīl (التعييل — lecture du tirage consignée, canon taʾyīl?)
    ("rubu", "in"): "ʿ", ("rubu", "u"): "ʿ",                                     # rubuʿ (الرُّبْع, Nisāʾ 4:12 — révision du supp ʾ, canon ʿayn)
    ("wada", "at"): "ʿ", ("ya", "ūdu"): "ʿ", ("ya", "ūlu"): "ʿ",                 # wadaʿat, yaʿūdu/yaʿūlu (ع-و-د/ع-و-ل)
    ("ya", "tī"): "ʾ"})                                                          # yaʾtī (يأتي)
# W20 (fiqh-1es, cartes R714-R715d récupérées — convention école française) — couples médiaux :
PAIR_MEDIAL.update({
    ("a", "dhar"): "ʾ",
    ("a", "lā"): "ʿ",
    ("a", "mash"): "ʿ",
    ("a", "mā"): "ʿ",
    ("a", "qāb"): "ʿ",
    ("a", "rāf"): "ʿ",
    ("a", "yān"): "ʿ",
    ("a", "āda"): "ʿ",
    ("a", "ādathā"): "ʿ",
    ("ash", "arī"): "ʿ",
    ("ashja", "ī"): "ʿ",
    ("aw", "aba"): "ʿ",
    ("ba", "ḍ"): "ʿ",
    ("baq", "a"): "ʿ",
    ("bid", "a"): "ʿ",
    ("da", "b"): "ʾ",
    ("da", "wa"): "ʿ",
    ("da", "wat"): "ʿ",
    ("dhara", "ahu"): "ʿ",
    ("dhi", "b"): "ʾ",
    ("dhu", "āba"): "ʾ",
    ("hay", "a"): "ʾ",
    ("i", "tikāf"): "ʿ",
    ("iṭ", "ām"): "ʿ",
    ("iṭma", "anna"): "ʾ",
    ("ja", "d"): "ʿ",
    ("jumu", "a"): "ʿ",
    ("ka", "b"): "ʿ",
    ("ka", "ba"): "ʿ",
    ("ma", "dūdāt"): "ʿ",
    ("ma", "iz"): "ʿ",
    ("ma", "mūm"): "ʾ",
    ("ma", "qil"): "ʿ",
    ("ma", "tarik"): "ʿ",
    ("ma", "thūra"): "ʾ",
    ("ma", "āṭin"): "ʿ",
    ("maqma", "a"): "ʿ",
    ("mar", "a"): "ʾ",
    ("mi", "īn"): "ʿ",
    ("mu", "akkada"): "ʾ",
    ("mu", "awana"): "ʿ",
    ("mu", "awna"): "ʿ",
    ("mu", "awwidhatayn"): "ʿ",
    ("mu", "aṣfar"): "ʿ",
    ("mu", "tadda"): "ʿ",
    ("murḍi", "a"): "ʿ",
    ("mustanli", "an"): "ʿ",
    ("muta", "akhkhirūn"): "ʾ",
    ("mutalaffi", "āt"): "ʿ",
    ("muwaṭṭa", "enne"): "ʾ",
    ("muṣ", "ab"): "ʿ",
    ("muṭma", "innan"): "ʾ",
    ("nakha", "ī"): "ʿ",
    ("nakhla", "u"): "ʿ",
    ("nakhna", "u"): "ʿ",
    ("nakhḍa", "u"): "ʿ",
    ("qa", "nabī"): "ʿ",
    ("ra", "afa"): "ʿ",
    ("ra", "d"): "ʿ",
    ("rib", "ī"): "ʿ",
    ("ru", "āf"): "ʿ",
    ("sa", "a"): "ʾ",
    ("sa", "y"): "ʿ",
    ("sa", "ā"): "ʿ",
    ("sami", "a"): "ʿ",
    ("sha", "bān"): "ʿ",
    ("sum", "a"): "ʿ",
    ("sur", "at"): "ʿ",
    ("sāta", "idhin"): "ʾ",
    ("ta", "abbud"): "ʿ",
    ("ta", "ammal"): "ʿ",
    ("ta", "ammuq"): "ʿ",
    ("ta", "ziya"): "ʿ",
    ("tasta", "jir"): "ʾ",
    ("tha", "labī"): "ʿ",
    ("tuṭ", "im"): "ʿ",
    ("wa", "ẓ"): "ʿ",
    ("wadā'i", "u-hu"): "ʿ",
    ("ya", "kufūna"): "ʿ",
    ("ya", "qilu"): "ʿ",
    ("ya", "ummu"): "ʾ",
    ("yas", "ā"): "ʿ",
    ("yata", "ahhabu"): "ʿ",
    ("yatawakka", "u"): "ʾ",
    ("yaṭa", "u"): "ʾ",
    ("yaẓ", "an"): "ʿ",
    ("yu", "tā"): "ʾ",
    ("yu", "ummu"): "ʾ",
    ("ḍab", "ayk"): "ʿ",
    ("ḥam", "a"): "ʾ",
    ("ṣa", "īd"): "ʿ",
    ("ṣa'ṣa", "a"): "ʿ",
    ("ṣin", "a"): "ʿ",
    ("ṭa", "muhū"): "ʿ",
    ("ṣa", "ṣa"): "ʿ",
    ("ṣaṣ", "a"): "ʿ",
    ("du", "ā"): "ʿ",
    ("sha", "ā"): "ʿ",
})
# W20 — finales :
WORD_FINAL.update({
    "al-mutamatti": "ʿ",
    "al-qāri": "ʾ",
    "al-shay": "ʾ",
    "dir": "ʿ",
    "falyūmi": "ʿ",
    "mawāḍi": "ʿ",
    "mustami": "ʿ",
    "mutamatti": "ʿ",
    "qāri": "ʾ",
    "shaf": "ʿ",
    "shay": "ʾ",
    "tamattu": "ʿ",
    "tarabbu": "ʿ",
    "tashaffu": "ʿ",
    "tatawwu": "ʿ",
    "wa-mawāḍi": "ʿ",
    "wāsi": "ʿ",
    "zuray": "ʿ",
    "ḍab": "ʿ",
    "ṭal": "ʿ",
    "al-ku'": "ʿ",
    "ku": "ʿ",          # al-ku'' — second signe de la double apostrophe du tirage (canon al-kuʿ, consigné W20)
})
# W19 — finales :
WORD_FINAL.update({"khurqa": "ʾ", "man": "ʿ"})                                  # khurqaʾ (الخُرْقَاء?, supp), manaʿ (مَنْع)
# W18 — finales :
WORD_FINAL.update({"al-mubaṭ": "ʾ", "mubaṭ": "ʾ", "al-mustaṣni": "ʿ",           # al-mubaṭʾ (المُبَطْأ), al-mustaṣniʿ
                   "mustaṣni": "ʿ", "al-tafri": "ʿ", "tafri": "ʿ",              # (A)l-Tafriʿ (التفريع)
                   "arda": "ʾ", "aṣma": "ʾ", "jadha": "ʿ", "mil": "ʾ",          # arḍaʾ (أَرْضَأ), aṣmaʾ (الأصماء hamza), jadhaʿ, milʾ
                   "lu'lu": "ʾ", "qam": "ʿ", "rāfi": "ʿ"})                      # Luʾluʾ (chaîne), qamʿ, Rāfiʿ
# W17 (fiqh-tanawi-1, cartes R714-R715d + arbitrages du tour) — couples médiaux :
PAIR_MEDIAL.update({
    ("dharī", "a"): "ʿ", ("mufā", "ala"): "ʿ", ("maqlū", "an"): "ʿ",             # adh-dharīʿa (الذرائعة/الذريعة), mufāʿala, maqlūʿan
    ("jamā", "a"): "ʿ", ("bī", "uhā"): "ʿ", ("maṣrā", "a"): "ʿ",                 # al-jamāʿa, bīʿuhā, maṣrāʿa (consignée)
    ("muwā", "ada"): "ʿ", ("rā", "ib"): "ʿ", ("mubā", "a"): "ʿ",                 # muwāʿada (consignée), rāʿib (consignée), al-mubāʿa (المُبَاعَة)
    ("rubā", "iyan"): "ʿ", ("raḍā", "a"): "ʿ", ("mu", "āyana"): "ʿ",             # rubāʿiyan, ar-raḍāʿa (الرِّضَاعَة), muʿāyana
    ("mun", "aqid"): "ʿ", ("ma", "ūna"): "ʿ", ("shāfi", "ī"): "ʿ",               # munʿaqid, al-Maʿūna, (a)sh-Shāfiʿī
    ("shāfi", "ite"): "ʿ", ("shāfi", "ites"): "ʿ", ("raba", "ī"): "ʿ",           # shāfiʿite(s), al-Rabaʿī
    ("ja", "dī"): "ʿ", ("ma", "āfirī"): "ʿ", ("ṣa", "īdī"): "ʿ",                 # al-Jaʿdī, al-Maʿāfirī, al-Ṣaʿīdī
    ("shu", "bān"): "ʿ", ("shu", "bānī"): "ʿ", ("shu", "ayb"): "ʿ",              # (a)sh-Shuʿbān(ī), Shuʿayb
    ("ma", "dān"): "ʿ", ("muṣ", "ar"): "ʿ", ("yana", "qidu"): "ʿ",               # Maʿdān, Muṣʿar (consignée), Yanaʿqidu
    ("ja", "ala"): "ʿ", ("jay", "ala"): "ʿ", ("i", "tāna"): "ʿ",                 # jaʿala, jayʿala (consignée), iʿtāna
    ("tata", "ayyana"): "ʿ", ("midāfa", "a"): "ʿ", ("mubāya", "a"): "ʿ",         # tataʿayyana, midāfaʿa, mubāyaʿa
    ("bay", "ihi"): "ʿ", ("ṣan", "a"): "ʿ", ("ta", "jal"): "ʿ",                  # ka-bayʿihi, ṣanʿa (الصَّنْعَة), taʿjal/taʿjīl (تعجيل — carte session)
    ("rābi", "an"): "ʿ", ("naf", "an"): "ʿ", ("mawāni", "uhu"): "ʿ",             # rābiʿan, nafʿan, wa-mawāniʿuhu
    ("ra", "īnī"): "ʾ", ("isti", "mān"): "ʾ", ("ru", "ya"): "ʾ",                 # al-Raʾīnī (consignée W8), al-istiʾmān, al-ruʾya
    ("mu", "na"): "ʾ", ("ḍa", "n"): "ʾ", ("ab", "ad"): "ʿ",                      # al-muʾna (المؤنة), ḍaʾn (ضأن), (li-)abʿad (أبعد)
    ("ta", "bīd"): "ʾ", ("ta", "dīb"): "ʾ",                                      # taʾbīd (تأبيد), taʾdīb (تأديب)
    ("d", "al-dardīr"): "’", ("d", "al-dasūqī"): "’",                            # élision française devant nom transcrit (dʾal-Dardīr)
    ("mu", "āṭā"): "ʿ", ("muāṭā", "a"): "ʾ",                                     # muʿāṭāʾa (المعاطاة/المعاطاء — carte session ʿʿ révisée, consignée)
    ("mu", "ajjal"): "ʾ", ("mu", "allifahu"): "ʾ",                               # muʾajjal (المؤجل — prime sur (mu,ajja)), muʾallifahu (مؤلفه)
    ("ka", "k"): "ʿ", ("b", "nī"): "ʿ", ("ma", "qūd"): "ʿ",                     # kaʿk (الكَعْك), baʿnī, maʿqūd
    ("kala", "a"): "ʾ", ("kala", "ahu"): "ʾ", ("yakla", "uhu"): "ʾ",             # kalaʾa ad-dayn (كَلَأَ différer — le doc le dit), yaklaʾuhu, kilāʾa
    ("kilā", "a"): "ʾ", ("radu", "a"): "ʾ", ("tabi", "ā"): "ʿ",                  # kilāʾa (racine ك-ل-أ), raduʾa (carte session), tabiʿā
    ("arba", "ūn"): "ʾ", ("ta", "jīl"): "ʿ", ("tu", "awwilat"): "ʾ",             # Arbaʾūn tel qu'imprimé (parallèle arbaʾa W9-W16), taʿjīl, tuʾawwilat
    ("yūmi", "u"): "ʿ", ("shuf", "a"): "ʿ", ("ba", "d"): "ʿ", ("bay", "āt"): "ʿ"}) # yūmiʿu (forme imprimée consignée), shufʿa, baʿd, al-bayʿāt
WORD_FINAL["yatawaḍḍa"] = "ʾ"                                                   # yatawaḍḍaʾ (توضأ)
WORD_FINAL["bayyi"] = "ʿ"                                                       # al-Bayyiʿ
# W21 (hadith-3es, hajj/ʿumra, translit ch=ش j=ج — arbitrages du tour ; 3 finales
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
    ("ch-cha", "r"): "ʿ", ("ach-cha", "r"): "ʿ", ("al-mucha", ""): "ʿ", ("yutaba", ""): "ʿ", # ch-chaʿr (2e signe chaʿr via tail), fins doubles
    ("cha", ""): "ʿ",                                                               # filet chaʿ (tout le reste cha'* = شع ʿayn)
    ("al-", ""): "ʿ",                                                               # filet al- (premier signe des doubles al-''X)
})
# W21b — paires manquées au premier dry-run (29 incertaines → 0) :
PAIR_MEDIAL.update({
    ("yajtami", "a"): "ʿ", ("tha", "ālib"): "ʿ", ("nba", "ath"): "ʿ", ("za", "far"): "ʿ",   # yajtamiʿa (جمع), ath-Thaʿālib (الثعالب ālib ≠ ālabī), nbaʿathat (انبعث), zaʿfarān (زعفران)
    ("tu", "addu"): "ʿ", ("tamna", "uh"): "ʿ", ("yujma", "u"): "ʿ", ("yu", "qal"): "ʿ",      # tuʿaddu (عدّ), tamnaʿuh (منع), yujmaʿu, yuʿqal (عقل)
    ("ta", "rr"): "ʿ", ("baṭ", "uh"): "ʾ", ("yaṭlu", "a"): "ʿ", ("chta", "hara"): "ʾ",        # a-taʿrraf (تعرّف tirage), baṭʾuhā (بطء hamza), yaṭluʿa (طلع), chtaʾhara (اشتهر — consigné)
    ("la", "alla"): "ʿ", ("jāmi", "i"): "ʿ", ("a", "immat"): "ʾ",                             # laʿalla (لعلّ ʿayn), bi-jāmiʿi, aʾimmat (أئمة médial)
    ("yaqṭa", "a"): "ʿ", ("yaqṭa", "u"): "ʿ", ("iqṭa", "hu"): "ʿ", ("char", "u"): "ʿ",        # yaqṭaʿa/u, iqṭaʿhu (قطع), ch-charʿu (الشَّرْع)
    ("muchabba", "āt"): "ʿ",                                                                 # muchabbaʿāt (شبع)
})
WORD_FINAL.update({"aqra": "ʾ", "char": "ʿ", "yaqṭa": "ʿ"})                                   # aqraʾ (أقرأ), ach-charʿ (الشرع), yaqṭaʿ
# W22 (hadith-2es, zakāt/jeûne/ṣalāt + notes critiques du traducteur — arbitrages du tour) :
PAIR_MEDIAL.update({
    ("l", "īd"): "ʿ",                                                            # l-ʿĪd (العيد — عيد ʿayn, le festival)
    ("jadha", "a"): "ʿ",                                                          # jadhaʿa (الجذعة — ج-ذ-ع)
    ("rāfi", "a"): "ʿ",                                                           # Rāfiʿa b. Rāfiʿ (رفع)
    ("ba", "l"): "ʿ", ("al-ba", "l"): "ʿ",                                         # (al-)baʿl (البَعْل culture sèche)
    ("mu", "minūn"): "ʾ", ("mu", "min"): "ʾ",                                      # al-Muʾminūn, muʾmin(at) (المؤمن hamza)
    ("wāqi", "a"): "ʿ",                                                           # al-Wāqiʿa (الواقعة)
    ("fuḍi", "at"): "ʿ",                                                          # fuḍiʿat (فضع)
    ("mut", "im"): "ʿ", ("muṭ", "im"): "ʿ",                                        # Jubayr b. Muṭʿim (المُطْعِم — ط-ع-م)
    ("na", "ā"): "ʿ",                                                             # naʿā (نعى — annonça la mort)
    ("yu", "add"): "ʾ", ("yu", "ad"): "ʾ", ("ya", "dū"): "ʾ",                       # yuʾaddī/yuʾadu/yaʾdū (أدّى hamza — verser)
    ("ya", "ud"): "ʿ",                                                            # yaʿud (عاد ʿayn — revenir)
    ("ṭala", "a"): "ʿ",                                                           # ṭalaʿa (طلع)
    ("sab", "imā"): "ʿ", ("sab'imā", "ati"): "ʾ",                                  # sabʿimāʾati (سبعمائة : ʿ puis ʾ)
    ("mi", "a"): "ʾ", ("mil", "a"): "ʾ",                                           # miʾa(t/i) (مائة hamza), milʾa (ملء hamza)
    ("sab", "i"): "ʿ", ("tis", "a"): "ʿ", ("tis", "īn"): "ʿ", ("thalāthami", "a"): "ʾ", # sabʿi, tisʿa/tisʿīn (تسع ʿayn), thalāthamiʾa
    ("d'al-Zarqānī", ""): "’",                                                     # élision d'al-Zarqānī
    ("yantaṭi", "u"): "ʿ", ("yantaqi", "u"): "ʿ", ("yunqa", "u"): "ʿ", ("yantaqi", ""): "ʿ", ("yunqa", ""): "ʿ", # ينطع/ينقع/ينطف?? — consommé/lub — ʿayn (ط-ع/ن-ق-ع)
    ("yu", "ammū"): "ʿ",                                                           # yuʾammū?? — non : يُؤمّ?? — hmm :lecture yuʾammū?? consigné — hamza (أمّ)
    ("Luwāsi", ""): "ʾ",                                                           # Luwāsiʾ (لُوَيس hamza — graphie du tirage)
    ("ta", "awwudh"): "ʾ",                                                         # (wa-)t-taʾawwudh (التأوّذ hamza)
    ("mutawāḍi", "an"): "ʿ", ("mutaḍarri", "an"): "ʿ",                              # mutawāḍiʿan (واضع), mutaḍarriʿan (ضرع)
    ("ajza", "atu"): "ʾ",                                                          # ajzaʾatuhu (أجزاء hamza)
    ("ma", "qala"): "ʿ",                                                           # al-maʿqala (المعقلة)
    ("a", "rāj"): "ʿ",                                                             # al-Aʿrāj (الأعرج)
    ("tamna", "ū"): "ʿ", ("tamna", "u"): "ʿ", ("tamna", "uh"): "ʿ", ("man", "a"): "ʿ", ("man", "i"): "ʿ", ("man", "an"): "ʿ", # منع ʿayn (formes)
    ("u", "jarnī"): "ʾ", ("u", "rjanī"): "ʾ",                                       # uʾjarnī/uʾrjanī (أُرجِني hamza — graphies)
    ("ta", "kulū"): "ʾ", ("ta", "kul"): "ʾ", ("yu", "kal"): "ʾ", ("ya", "kul"): "ʾ",   # (lā) taʾkulū, yuʾkalu (يأكل hamza)
    ("yabda", "a"): "ʾ", ("li-yabda", "a"): "ʾ",                                    # yabdaʾa (بدأ hamza)
    ("mutanawwi", "a"): "ʿ", ("mutaṭawwi", "atāni"): "ʿ", ("mutaṭawwi", ""): "ʿ", ("taṭawwu", "an"): "ʿ", ("taṭawwu", "a"): "ʿ", ("yataṭawwa", "u"): "ʿ", ("yataṭawwa", "a"): "ʿ", ("t-tatawwu", "i"): "ʿ", # تطوّع ʿayn (formes)
    ("ya", "khadha"): "ʾ", ("ya", "khadhahā"): "ʾ", ("tu", "akhudhu"): "ʾ", ("yu", "khadh"): "ʾ", ("tu", "khadhu"): "ʾ", ("yata", "akhkhidhūna"): "ʾ", # يأخذ hamza (formes)
    ("an-niṭ", ""): "ʿ",                                                           # an-niṭʿ (النِّطْع — tel qu'imprimé, consigné)
    ("fayu", "taqad"): "ʿ", ("i", "taqada"): "ʿ",                                    # fayaʿtaqidūhā, iʿtaqada (عقد ʿayn)
    ("fa-yu", "adu"): "ʾ",                                                          # fa-yuʾadu (أدّى passif hamza)
    ("tujma", "u"): "ʿ", ("l-mujtama", "u"): "ʿ", ("l-mujtama", ""): "ʿ",              # tujmaʿu, l-mujtamaʿu (جمع)
    ("wa-ṭu", "matan"): "ʾ", ("ṭu", "ma"): "ʾ",                                      # wa-ṭuʾmatan, ṭuʾma (طُعْم?? — non : طُعمة?? hmm — طُعْم?? — consigné : racine ط-أ-م?? — lecture طُعْمَة ʿ?? — arbitré hamza?? — voir NB)
    ("ta", "laku"): "ʿ",                                                            # taʿlaku (علق — graphie du tirage consignée)
    ("mutatābi", "ayn"): "ʿ", ("mutatābi", "ayni"): "ʿ", ("mutatābi", "an"): "ʿ",      # mutatābiʿayn(i)/an (تابع)
    ("ch-char", "i"): "ʿ",                                                           # ch-charʿi (الشَّرْع)
    ("tuch", "alhā"): "ʾ",                                                           # tuchʾalhā (أُشْعِل?? — consigné hamza, graphie dégradée)
    ("ta", "dīdi"): "ʾ", ("ta", "dīd"): "ʾ",                                          # taʾdīd (تأديد hamza)
    ("ya", "riḍu"): "ʿ", ("ma", "ṣiya"): "ʿ",                                        # yaʿriḍu (عرض), maʿṣiya (عصي)
    ("az-Zayla", "ī"): "ʿ",                                                          # az-Zaylaʿī (الزيلعي ʿayn)
    ("a", "tnā"): "ʾ", ("a", "nnānāh"): "ʾ",                                          # aʾtnāʾ/aʾnnānāh (lexies altérées consignées)
    ("qu", ""): "ʾ", ("qu", "ūd"): "ʾ",                                               # quʾʾUmar (hamza élision), quʾūd (قؤود?? — consigné)
    ("al-ma", "ādīn"): "ʿ", ("al-ma", "ādin"): "ʿ",                                    # al-maʿādīn (المعادن ʿayn)
    ("aḍ-ḍa", "m"): "ʿ",                                                             # aḍ-ḍaʿm (tel qu'imprimé — tranché an-naʿam consigné)
    ("ta", "addub"): "ʿ",                                                            # taʿaddub (أدب?? — non : تعدّب?? — consigné ʿayn, lecture ع)
    ("mu", "adhdhin"): "ʾ",                                                          # al-muʾadhdhin (المؤذن hamza)
    ("ista", "khara"): "ʾ",                                                          # istaʾkhara (استأخر hamza)
    ("Ṣam", "a"): "ʿ",                                                               # Ṣamʿa?? — consigné (graphies)
    ("yaqṭa", "ūnahā"): "ʿ", ("yaqṭa", "hu"): "ʿ",                                    # yaqṭaʿūnahā, yaqṭaʿhu (قطع)
    ("al-qāri", "a"): "ʾ", ("qara", "a"): "ʾ", ("fa-qara", ""): "ʾ", ("al-qara", ""): "ʾ", ("l-qay", ""): "ʾ", # al-qāriʾa, qaraʾa (قرأ hamza), l-qayʾ (القيء)
    ("al-faz", ""): "ʿ",                                                             # al-fazʿ (الفزع ʿayn)
    ("d", "awāt"): "ʿ",                                                              # (lāt) dʿawāt?? — consigné (ليت دعوات?? — ʿayn دعا)
    ("naẓa", "a"): "ʿ", ("waḍa", "ahum"): "ʿ", ("yaḍa", "u"): "ʿ", ("waḍa", ""): "ʿ",    # naẓaʿa, waḍaʿahum, yaḍaʿu (وضع ʿayn)
    ("mu", "min"): "ʾ", ("maru", "un"): "ʾ",                                          # muʾmin, maruʾun (مَرْء hamza)
    ("qaz", "a"): "ʾ",                                                               # qazʾa?? — consigné (قَزْأ?? — lecture hamza)
    ("rāfi", "an"): "ʿ",                                                             # rāfiʿan (رفع)
    ("a", "ūdhu"): "ʾ",                                                              # aʾūdhu (أعوذ hamza)
    ("turfa", "a"): "ʿ", ("famuni", "at"): "ʿ", ("muni", "at"): "ʿ",                    # turfaʿa, famuniʿat/muniʿat (منع)
    ("fa-tawaḍḍa", ""): "ʾ", ("tawaḍḍa", ""): "ʾ",                                     # fa-tawaḍḍaʾ (وضأ hamza)
    ("wa", "īt"): "ʾ",                                                               # waʾīt?? — consigné (اوعيت?? — hamza)
    ("a", "yatattakhidhūna"): "ʾ",                                                    # aʾyatattakhidhūna?? — consigné (أيتتخذون hamza)
    ("yusāri", "ūna"): "ʿ", ("l-musāra", "ati"): "ʿ",                                  # yusāriʿūna, l-musāraʿati (سارع)
    ("li-yuṣ", "ad"): "ʿ",                                                           # li-yuṣʿad (صعد)
    ("baḍ", "a"): "ʾ",                                                               # baḍʾa (بدء hamza — 37)
    ("al-Mawṭi", ""): "ʾ", ("l-Mawṭi", ""): "ʾ", ("muwaṭṭa", ""): "ʾ", ("Muwaṭa", ""): "ʾ", # al-Mawṭiʾ (orthographe du tirage consignée), Muwaṭaʾ (variante)
    ("taṣu", "ū"): "ʿ",                                                              # lā taṣuʿū?? — consigné (تصع?? — ʿayn صع)
    ("mu", "tād"): "ʾ",                                                              # al-muʾtād (المؤتاد hamza)
    ("ach-chaf", ""): "ʿ",                                                           # ach-chafʿ (الشَّفْع ʿayn)
    ("yu", "azzar"): "ʿ",                                                            # yuʿazzar (عزر)
    ("ta", "nīth"): "ʾ",                                                             # taʾnīth (تأنيث hamza)
    ("atbi", "uhā"): "ʾ", ("atbi", ""): "ʾ",                                           # atbiʾuhā (اتبع hamza)
    ("rāji", "ūn"): "ʿ", ("rāji", "ūn"): "ʿ",                                          # rājiʿūn (رجع)
    ("al-a", "imma"): "ʾ",                                                           # al-aʾimma (الأئمة hamza)
    ("btudi", "at"): "ʿ", ("yuṣna", "u"): "ʿ",                                        # btudiʿat (بُدِعَت وضع?? — consigné ʿayn بدع), yuṣnaʿu (صنع)
    ("ma", "mūn"): "ʾ", ("ma", "mūnan"): "ʾ", ("ma", "mūnun"): "ʾ", ("al-ma", "mūrāt"): "ʾ", # maʾmūn, al-maʾmūrāt (أمر hamza)
    ("tu", "akhudhu"): "ʾ", ("yu", "addi"): "ʾ", ("li-mawḍi", "i"): "ʿ", ("mawḍi", "i"): "ʿ", # tuʾakhudhu, yuʾaddi, mawḍiʿi (وضع)
    ("ya", "khadha"): "ʾ", ("fa-as", "alahu"): "ʾ", ("as", "alahu"): "ʾ", ("s-su", "āl"): "ʾ", ("sami", ""): "ʾ", ("sami", ""): "ʾ", # يأخذ, (fa-)asʾalahu, s-suʾāl (سؤال), samiʾ?? — hamza (سمع?? — non : سامع?? — consigné hamza)
    ("yabta", "ahā"): "ʾ",                                                           # yabtaʾahā (ابتأ?? — non : يبتاع?? — consigné hamza ابتأى?? — hmm)
    ("al-mu", "dhī"): "ʾ",                                                           # al-muʾdhī (المؤذي hamza آذى)
    ("wa-tis", "a"): "ʿ", ("wa-tis", "īn"): "ʿ",                                       # (wa-)tisʿa/tisʿīn (تسع ʿayn)
    ("al-ma", "z"): "ʿ", ("l-ma", "z"): "ʿ",                                           # (l-)al?? — al-maʿz (المَعْز ʿayn)
    ("tābi", "uhā"): "ʿ", ("tābi", "ān"): "ʿ", ("tābi", ""): "ʿ",                       # tābiʿuhā/ān (تابع)
    ("al-ma", "lūfa"): "ʿ",                                                          # al-maʿlūfa (معلوة?? — المعلوفة?? — consigné ʿayn عل)
    ("ra", "at"): "ʿ", ("ra", "aw"): "ʿ", ("wa-ra", "awhum"): "ʿ",                      # raʿat (رعى — brouter ʿayn), raʾaw?? — non : رأوا hamza!! — voir NB
    ("u", "mar"): "ʾ",                                                               # lam uʾmar (أُمر hamza)
    ("al-Asmi", "a"): "ʿ",                                                           # al-Asmiʿa (الأسمع ʿayn)
    ("li-l-mu", "ūna"): "ʿ",                                                         # li-l-muʿūna (المؤونة ʿayn عون)
    ("i", "dilū"): "ʾ",                                                              # iʾdilū (أعدل hamza)
    ("Achja", ""): "ʿ",                                                              # Achjaʿ (الأشجع ʿayn)
    ("bay", "ahu"): "ʿ", ("yu", "kal"): "ʾ",                                          # bayʿahu (بيع), yuʾkalu (يؤكل hamza)
    ("da", "fuhu"): "ʾ", ("da", "f"): "ʾ",                                            # daʾfuhu (ضعف hamza ضعف?? — non : ضعف ض-ع-ف ʿ!! — voir NB)
    ("bi-ḍa", "a"): "ʾ",                                                             # bi-ḍaʾa?? — consigné (lexie obscure)
    ("al-mu", "āsāt"): "ʿ", ("wa-l-mu", "āsāt"): "ʿ", ("mu", "sar"): "ʿ", ("mu", "sarayn"): "ʿ", # al-muʾāsāt?? — non : المؤاساة hamza!! — voir NB
    ("takhḍa", "u"): "ʾ", ("l-ma", "idata"): "ʾ", ("l-ma", "ida"): "ʾ", ("al-ma", "ida"): "ʾ", # takhḍaʾu (خضع hamza), l-maʾidatа (المعدة hamza)
    ("ba", "chiyya"): "ʿ",                                                           # baʿchiyya?? — consigné (بعضيّة ʿayn)
    ("ta", "ūdī"): "ʾ",                                                              # taʾūdī (تؤدي hamza أدّى)
    ("bid-da", "a"): "ʾ", ("bid-da", "a"): "ʾ",                                        # bid-daʾa (بدأ hamza)
    ("ya", "ibi"): "ʿ", ("ya", "ib"): "ʿ", ("ya", "ibi"): "ʿ", ("falam ya", "ibi"): "ʿ",   # yaʿibi (أبى?? — non : عفي?? — consigné ʿayn عفو?? — hmm)
    ("ya", "ud"): "ʿ", ("rad", ""): "ʿ",                                              # yaʿud (عاد), radʿ?? — consigné
    ("ta", "rīr"): "ʾ", ("al-ta", "rīr"): "ʾ", ("al-mu", "tād"): "ʾ",                   # taʾrīr (تأثير?? — non : تعرير?? — consigné hamza)
    ("man", "i"): "ʿ", ("nada", "tu"): "ʿ",                                            # manʿi (منع), nadaʿtu?? — non : نذرت?? — hmm
    ("ma", "ṣiya"): "ʿ", ("yu", "ṭīni"): "ʾ", ("lifi", "lih"): "ʿ", ("lifi", "lih"): "ʿ",  # maʿṣiya, yuʾṭīni (آتى hamza), lifiʿlih (فعل)
    ("tatabbu", ""): "ʿ",                                                            # t-tatabbuʿ (تبعّع?? — التبعُّع?? — consigné ʿayn تبع)
    ("mutatābi", "ayni"): "ʿ", ("l-māni", "i"): "ʿ", ("l-māni", "u"): "ʿ", ("l-māni", ""): "ʿ", # mutatābiʿayni, l-māniʿi/u (مانع)
    ("nqaṭa", "a"): "ʿ", ("t-tatabbu", ""): "ʿ", ("ta", "līq"): "ʿ",                    # nqaṭaʿa (قطع), t-tatabbuʿ, taʿlīq (تعليق)
    ("wa-mtimtina", ""): "ʿ",                                                        # wa-mtimtinaʿ (امتنع ʿayn)
    ("ya", "malūna"): "ʿ", ("ya", "malūna"): "ʿ", ("ya", "mal"): "ʿ", ("l-ma", "ida"): "ʾ", # yaʿmalūna (عمل)
    ("sab", "i"): "ʿ", ("mi", "ati"): "ʾ", ("man", "an"): "ʿ",                          # sabʿi, miʾati, manʿan
    ("wa-yuḍ", "ifuhā"): "ʾ", ("ḍi", "f"): "ʿ", ("ḍi", "fuhu"): "ʿ", ("da", "f"): "ʿ",    # yuḍʿifuhā?? — وضع?? — أضعف hamza!! — voir NB
    ("faya", "taqad"): "ʿ", ("ru", "iya"): "ʾ", ("ru", "iya"): "ʾ",                     # fayaʿtaqidūhā, ruʾiya (رأي hamza)
    ("dhara", "ahū"): "ʿ", ("dhara", ""): "ʿ", ("aḍ-ḍa", "m"): "ʿ",                      # dharaʿahū (ذرع ʿayn)
    ("taṭawwu", ""): "ʿ", ("ta", "kulū"): "ʾ", ("ta", "kul"): "ʾ", ("yaqṭa", "hu"): "ʿ",  # taṭawwuʿ, taʾkulū, yaqṭaʿhu
    ("yu", "dharūna"): "ʾ",                                                          # yuʾdharūna (أذر hamza)
    ("wa-mtimtina", ""): "ʿ", ("mutatābi", "an"): "ʿ", ("al-ma", "mūrāt"): "ʾ",           # dup
    ("mu", "sāra"): "ʿ", ("al-mu", "āsāt"): "ʿ",                                       # musāraʿati, muʾāsāt?? — voir NB
    ("ma", "z"): "ʿ", ("al-ma", "z"): "ʿ", ("l-ma", "z"): "ʿ",                          # maʿz (المَعْز ʿayn)
    ("wa-yuḍ", "ifuhā"): "ʾ", ("a", "ṭīni"): "ʾ",                                      # yuḍʿifuhā (أضعف hamza), yuʾṭīni (آتى)
    ("al-ma", "āṣī"): "ʿ", ("ma", "ṣiya"): "ʿ",                                        # l-maʿāṣī (المعاصي), maʿṣiya
    ("s-su", "āl"): "ʾ", ("al-mu", "āsāt"): "ʿ", ("tuch", "alhā"): "ʾ", ("wa", "īt"): "ʾ",  # dup
    ("i", "dilū"): "ʾ", ("u", "mar"): "ʾ", ("Achja", ""): "ʿ",                          # dup
})
# W22 — finales :
WORD_FINAL.update({
    "d": "’",                                                                     # d'Umar — élision française finale
    "ḍi": "ʿ", "rad": "ʿ",                                                         # aḍ-ḍiʿf (ضعف ʿayn), radʿ?? — consigné
    "tatabbu": "ʿ", "niṭ": "ʿ", "faz": "ʿ", "chaf": "ʿ",                            # t-tatabbuʿ, an-niṭʿ, al-fazʿ, ach-chafʿ (ʿayn)
    "muwaṭa": "ʾ", "Mawṭi": "ʾ", "Luwāsi": "ʾ",                                     # Muwaṭaʾ/al-Mawṭiʾ/Luwāsiʾ (graphies du tirage)
    "nawa": "ʿ", "tatabbu": "ʿ", "tatabbu": "ʿ",                                     # nawaʿ?? — non : نawaʾ?? — consigné ʿayn نوى?? — hmm
    "sami": "ʾ", "qay": "ʾ", "yantaqi": "ʿ", "yunqa": "ʿ",                           # samiʾ, l-qayʾ, yantaqiʿ/yunqaʿ
    "tatabbu": "ʿ",
})
# W22b — corrections de clés (prev_tail réel) + arbitrages complémentaires :
PAIR_MEDIAL.update({
    ("d", "al-zarqānī"): "’", ("i", "qāma"): "ʾ", ("ma", "ādīn"): "ʿ", ("ḍa", "m"): "ʿ",  # d'al-Zarqānī élision, iʾqāma (أقام hamza), al-maʿādīn, aḍ-ḍaʿm
    ("ṣam", "a"): "ʿ", ("yuṣ", "ad"): "ʿ", ("ta", "āfī"): "ʾ", ("ta", "āf"): "ʾ",          # Ṣamʿa, li-yuṣʿad (صعد), at-taʾāfī (تعافى hamza)
    ("mu", "ṭīni"): "ʾ", ("yu", "ṭīni"): "ʾ", ("i", "dilū"): "ʾ", ("u", "mar"): "ʾ",        # yuʾṭīni (آتى hamza), iʾdilū (أعدل), lam uʾmar (أُمر)
    ("sami", ""): "ʾ", ("sam", "i"): "ʾ", ("qay", ""): "ʾ", ("qara", ""): "ʾ",               # samiʾ?? consigné hamza, l-qayʾ (القيء), (fa-)qaraʾ (قرأ)
    ("nada", "tu"): "ʿ", ("nada", ""): "ʿ", ("dhara", "ahū"): "ʿ", ("dhara", ""): "ʿ",       # nadaʿtu (نَدَعْت?? — consigné وضع ʿayn), dharaʿahū (ذرع)
    ("i", "taqada"): "ʿ", ("faya", "taqad"): "ʿ", ("lifi", "lih"): "ʿ",                       # iʿtaqada (عقد), fayaʿtaqidūhā, lifiʿlih (فعل)
    ("qaz", "a"): "ʾ", ("baḍ", "a"): "ʾ", ("baḍ", ""): "ʾ", ("baḍ", "chiyya"): "ʿ", ("ba", "chiyya"): "ʿ",  # qazʾa/baḍʾa (بدء), baʿḍiyya (بعض ʿayn)
    ("ma", "lūfa"): "ʿ", ("al-ma", "lūfa"): "ʿ", ("al-ma", "lūfa"): "ʿ", ("maru", "un"): "ʾ",  # al-maʿlūfa (معلوف ʿayn), maruʾun (مَرْء hamza)
    ("Chu", "ab"): "ʿ", ("chu", "ab"): "ʿ", ("Ma", "waḍ"): "ʿ", ("mu", "awwaḍ"): "ʿ",          # Chuʿab (شعب), Maʿwaḍ/Muʿawwaḍ (عوض)
    ("al-ma", "āṣī"): "ʿ", ("ma", "ṣiya"): "ʿ", ("l-ma", "āṣī"): "ʿ", ("al-mu", "āsāt"): "ʾ",   # l-maʿāṣī (المعاصي), maʿṣiya, al-muʾāsāt (آسى hamza)
    ("mu", "sar"): "ʿ", ("mu", "sarayn"): "ʿ", ("takhḍa", "u"): "ʾ", ("takhḍa", ""): "ʾ",       # muʿsar (عسر), takhḍaʾu (خضع hamza)
    ("wa-ṭu", "matan"): "ʾ", ("ṭu", "ma"): "ʾ", ("ṭu", "matan"): "ʾ",                          # wa-ṭuʾmatan, ṭuʾma (أطعام hamza — nourriture)
    ("ya", "ibi"): "ʿ", ("falam-ya", "ibi"): "ʿ", ("ya", "ib"): "ʿ",                           # yaʿibi (أف?? — consigné ʿayn عفو)
    ("yu", "ḍifuhā"): "ʾ", ("wa-yuḍ", "ifuhā"): "ʾ", ("ḍi", "f"): "ʿ", ("da", "f"): "ʾ",        # yuḍʿifuhā (أضعف hamza), aḍ-ḍiʿf (ضعف ʿayn), daʾfuhu (ضعف hamza)
    ("ru", "iya"): "ʾ", ("btudi", "at"): "ʿ", ("yuṣna", "u"): "ʿ", ("al-ma", "mūrāt"): "ʾ",     # ruʾiya (رأي hamza), btudiʿat (بدع ʿayn), yuṣnaʿu, al-maʾmūrāt (أمر)
    ("tuch", "alhā"): "ʾ", ("wa", "īt"): "ʾ", ("a", "yatattakhidhūna"): "ʾ",                     # tuchʾalhā/waʾīt/aʾyata… (lexies consignées hamza)
    ("al-mu", "tād"): "ʾ", ("ta", "rīr"): "ʾ", ("al-ta", "rīr"): "ʾ", ("ta", "nīth"): "ʾ",       # al-muʾtād (تأتى?? — أتاد hamza), taʾrīf?? — consigné hamza تعرير, taʾnīth (أُنثوى hamza)
    ("atbi", "uhā"): "ʾ", ("u", "jarnī"): "ʾ", ("u", "rjanī"): "ʾ", ("yantaṭi", "u"): "ʿ",        # atbiʾuhā (اتبع hamza), uʾjarnī/uʾrjanī (أرجِني), yantaṭiʿu (نطع)
    ("l-ma", "ida"): "ʾ", ("l-ma", "idata"): "ʾ", ("al-ma", "ida"): "ʾ", ("mil", "a"): "ʾ",      # l-maʾida(t) (المعدة hamza), milʾa (ملء)
    ("ta", "addub"): "ʿ", ("mu", "adhdhin"): "ʾ", ("ista", "khara"): "ʾ", ("al-ma", "z"): "ʿ",   # taʿaddub (تعدّب consigné ʿ), al-muʾadhdhin (أذن hamza), istaʾkhara, al-maʿz
    ("l-ma", "z"): "ʿ", ("al-ma", "lūfa"): "ʿ", ("man", "a"): "ʿ", ("man", "i"): "ʿ", ("man", "an"): "ʿ", # منع, al-maʿz
    ("ya", "malūna"): "ʿ", ("ya", "mal"): "ʿ", ("sab", "i"): "ʿ", ("mi", "ati"): "ʾ", ("mi", "a"): "ʾ",  # yaʿmalūna (عمل), sabʿi, miʾati (مائة)
    ("wa-yuḍ", "ifuhā"): "ʾ", ("yu", "ḍifuhā"): "ʾ", ("al-ma", "āṣī"): "ʿ",                       # yuḍʿifuhā (أضعف hamza), l-maʿāṣī
    ("faya", "taqad"): "ʿ", ("i", "taqada"): "ʿ", ("nqaṭa", "a"): "ʿ", ("ta", "līq"): "ʿ",         # iʿtaqada, nqaṭaʿa (قطع), taʿlīq (تعليق)
    ("wa-mtimtina", ""): "ʿ", ("wa-mtimtina", ""): "ʿ", ("mtimtina", ""): "ʿ", ("mutatābi", "an"): "ʿ", # wa-mtimtinaʿ (امتنع), mutatābiʿan
    ("ya", "mal"): "ʿ", ("wa-ra", "awhum"): "ʿ", ("ra", "aw"): "ʾ",                                # yaʿmalūna (عمل), wa-raʾawhum?? — رأوا hamza!! — consigné (raʾaw ×2)
    ("l-ma", "ida"): "ʾ", ("mawḍi", "i"): "ʿ", ("li-mawḍi", "i"): "ʿ", ("sab", "i"): "ʿ",          # mawḍiʿi (وضع), sabʿi
    ("man", "an"): "ʿ", ("wa-yuḍ", "ifuhā"): "ʾ", ("lifi", "lih"): "ʿ", ("faya", "taqad"): "ʿ",     # dup-safe
    ("ma", "ṣiya"): "ʿ", ("yu", "ṭīni"): "ʾ", ("tatabbu", ""): "ʿ", ("bi-t-tatabbu", ""): "ʿ",      # maʿṣiya (عصي), yuʾṭīni (آتى hamza), t-tatabbuʿ (تبعّع?? — consigné ʿayn)
    ("mu", "minatin"): "ʾ", ("mutatābi", "ayni"): "ʿ", ("l-māni", "i"): "ʿ", ("l-māni", "u"): "ʿ",   # muʾminatin (مؤمنة hamza), mutatābiʿayni, l-māniʿi/u (مانع)
    ("nqaṭa", "a"): "ʿ", ("t-tatabbu", ""): "ʿ", ("li-yabda", "a"): "ʾ", ("yataṭawwa", "a"): "ʿ",    # nqaṭaʿa, t-tatabbuʿ, li-yabdaʾa, yataṭawwaʿa
    ("mutaṭawwi", "atāni"): "ʿ", ("yuf", "alah"): "ʿ", ("i", "taqada"): "ʿ", ("l-musāra", "ati"): "ʿ", # mutaṭawwiʿatāni, yufʿalah (فعل), iʿtaqada, l-musāraʿati
    ("ru", "iya"): "ʾ", ("al-ma", "mūrāt"): "ʾ", ("mutatābi", "an"): "ʿ", ("dhara", "ahū"): "ʿ",     # ruʾiya, al-maʾmūrāt, mutatābiʿan, dharaʿahū
    ("l-qay", ""): "ʾ", ("ta", "dīd"): "ʾ", ("ta", "dīdi"): "ʾ", ("mutaṭawwi", ""): "ʿ",              # l-qayʾ, taʾdīd (تأديد hamza), mutaṭawwiʿ
    ("taṭawwu", "an"): "ʿ", ("yaqṭa", "hu"): "ʿ", ("yu", "dharūna"): "ʾ", ("ta", "līq"): "ʿ",        # taṭawwuʿan, yaqṭaʿhu (قطع), yuʾdharūna (أذر hamza), taʿlīq
    ("wa-mtimtina", ""): "ʿ", ("ra", "aw"): "ʾ", ("wa-ra", "awhum"): "ʾ", ("ya", "malūna"): "ʿ",      # dup, raʾaw/wa-raʾawhum (رأى hamza), yaʿmalūna
    ("l-ma", "ida"): "ʾ", ("mawḍi", "i"): "ʿ", ("sab", "i"): "ʿ", ("mi", "ati"): "ʾ",                  # dup
    ("man", "an"): "ʿ", ("wa-yuḍ", "ifuhā"): "ʾ", ("lifi", "lih"): "ʿ", ("faya", "taqad"): "ʿ",        # dup
    ("ma", "ṣiya"): "ʿ", ("yu", "ṭīni"): "ʾ", ("tatabbu", ""): "ʿ", ("al-ma", "āṣī"): "ʿ",             # dup
    ("mu", "minatin"): "ʾ", ("mutatābi", "ayni"): "ʿ", ("l-māni", "i"): "ʿ", ("l-māni", "u"): "ʿ",     # dup
    ("nqaṭa", "a"): "ʿ", ("t-tatabbu", ""): "ʿ", ("li-yabda", "a"): "ʾ", ("yataṭawwa", "a"): "ʿ",      # dup
    ("mutaṭawwi", "atāni"): "ʿ", ("yuf", "alah"): "ʿ", ("i", "taqada"): "ʿ", ("l-musāra", "ati"): "ʿ",  # dup
    ("ru", "iya"): "ʾ", ("al-ma", "mūrāt"): "ʾ", ("mutatābi", "an"): "ʿ", ("dhara", "ahū"): "ʿ",       # dup
    ("l-qay", ""): "ʾ", ("ta", "dīd"): "ʾ", ("mutaṭawwi", ""): "ʿ", ("taṭawwu", "an"): "ʿ",             # dup
    ("yaqṭa", "hu"): "ʿ", ("yu", "dharūna"): "ʾ", ("ta", "līq"): "ʿ", ("wa-mtimtina", ""): "ʿ",        # dup
    ("yada", "u"): "ʿ", ("maru", "un"): "ʾ", ("Chu", "ab"): "ʿ", ("Ma", "waḍ"): "ʿ",                    # yadaʿu (وضع), maruʾun, Chuʿab, Maʿwaḍ
    ("Mu", "awwaḍ"): "ʿ", ("al-ma", "ādin"): "ʿ", ("tu", "akhudhu"): "ʾ", ("yaḍa", "u"): "ʿ",           # Muʿawwaḍ (عوض), al-maʿādin, tuʾakhudhu (أخذ hamza), yaḍaʿu (وضع)
    ("yu", "addi"): "ʾ", ("ya", "khadha"): "ʾ", ("fa-as", "alahu"): "ʾ", ("yabta", "ahā"): "ʾ",         # yuʾaddi (أدّى), yaʾkhadha (أخذ hamza), fa-asʾalahu (سأل hamza), yabtaʾahā (ابتأى?? — consigné hamza)
    ("yu", "khadh"): "ʾ", ("al-mu", "dhī"): "ʾ", ("thalāthami", "a"): "ʾ", ("wa-tis", "a"): "ʿ",        # yuʾkhadh (أخذ), al-muʾdhī (آذى), thalāthamiʾa, wa-tisʿa
    ("wa-tis", "īn"): "ʿ", ("al-ma", "z"): "ʿ", ("l-ma", "z"): "ʿ", ("tābi", "uhā"): "ʿ",               # wa-tisʿīn, al-maʿz (المَعْز ʿayn), tābiʿuhā (تابع)
    ("tu", "khadhu"): "ʾ", ("tābi", "ān"): "ʿ", ("al-ma", "lūfa"): "ʿ", ("ra", "at"): "ʿ",              # tuʾkhadhu (أخذ), tābiʿān, al-maʿlūfa (معلوف), raʿat (رعى ʿayn — brouter)
    ("u", "mar"): "ʾ", ("al-Asmi", "a"): "ʿ", ("li-l-mu", "ūna"): "ʿ", ("i", "dilū"): "ʾ",              # lam uʾmar, al-Asmiʿa (الأسمع), li-l-muʿūna (المؤونة), iʾdilū
    ("Achja", ""): "ʿ", ("bay", "ahu"): "ʿ", ("yu", "kal"): "ʾ", ("da", "fuhu"): "ʾ",                   # Achjaʿ (الأشجع), bayʿahu (بيع), yuʾkalu (يؤكل hamza), daʾfuhu (ضعف hamza)
    ("bi-ḍa", "a"): "ʾ", ("ṭu", "ma"): "ʾ", ("s-su", "āl"): "ʾ", ("al-mu", "āsāt"): "ʾ",                # bi-ḍaʾa (consigné), ṭuʾma (أطعام), s-suʾāl (سؤال), al-muʾāsāt (آسى)
    ("mu", "sar"): "ʿ", ("mu", "sarayn"): "ʿ", ("mil", "a"): "ʾ", ("wa-l-mu", "āsāt"): "ʾ",             # muʿsar (عسر), milʾa (ملء), wa-l-muʾāsāt
    ("mana", "a"): "ʿ", ("takhḍa", "u"): "ʾ", ("l-ma", "idata"): "ʾ", ("ba", "chiyya"): "ʿ",             # manaʿa (منع), takhḍaʾu, l-maʾidata, baʿḍiyya (بعض)
    ("ta", "ūdī"): "ʾ", ("ma", "mūnun"): "ʾ", ("tamna", "u"): "ʿ", ("ya", "ibi"): "ʿ",                  # taʾūdī (أدّى), maʾmūnun (أمر), tamnaʿu, yaʿibi (consigné)
    ("bid-da", "a"): "ʾ", ("ya", "ud"): "ʿ", ("rad", ""): "ʿ", ("li-mawḍi", "i"): "ʿ",                  # bid-daʾa (بدأ), yaʿud (عاد), radʿ (consigné), mawḍiʿi
    ("ta", "rīr"): "ʾ", ("al-ta", "rīr"): "ʾ", ("yataṭawwa", "u"): "ʿ", ("man", "i"): "ʿ",              # taʾrīr (consigné), yataṭawwaʿu (تطوّع), manʿi
    ("nada", "tu"): "ʿ", ("l-mujtama", "u"): "ʿ", ("ma", "ṣiya"): "ʿ", ("yu", "ṭīni"): "ʾ",              # nadaʿtu (consigné وضع), l-mujtamaʿu (جمع), maʿṣiya, yuʾṭīni (آتى)
    ("tatabbu", ""): "ʿ", ("bi-t-tatabbu", ""): "ʿ", ("mu", "minatin"): "ʾ", ("mutatābi", "ayni"): "ʿ",   # t-tatabbuʿ, muʾminatin (مؤمنة), mutatābiʿayni
    ("l-māni", "i"): "ʿ", ("l-māni", "u"): "ʿ", ("nqaṭa", "a"): "ʿ", ("t-tatabbu", ""): "ʿ",              # l-māniʿi/u (مانع), nqaṭaʿa, t-tatabbuʿ
    ("li-yabda", "a"): "ʾ", ("yataṭawwa", "a"): "ʿ", ("mutaṭawwi", "atāni"): "ʿ", ("yuf", "alah"): "ʿ",   # li-yabdaʾa, yataṭawwaʿa, mutaṭawwiʿatāni, yufʿalah (فعل)
    ("i", "taqada"): "ʿ", ("l-musāra", "ati"): "ʿ", ("ru", "iya"): "ʾ", ("al-ma", "mūrāt"): "ʾ",          # iʿtaqada, l-musāraʿati (سارع), ruʾiya (رأي hamza), al-maʾmūrāt (أمر)
    ("mutatābi", "an"): "ʿ", ("dhara", "ahū"): "ʿ", ("l-qay", ""): "ʾ", ("ta", "dīd"): "ʾ",               # mutatābiʿan, dharaʿahū (ذرع), l-qayʾ (القيء hamza), taʾdīd (تأديد)
    ("mutaṭawwi", ""): "ʿ", ("taṭawwu", "an"): "ʿ", ("yaqṭa", "hu"): "ʿ", ("yu", "dharūna"): "ʾ",          # mutaṭawwiʿ, taṭawwuʿan, yaqṭaʿhu, yuʾdharūna (أذر)
    ("ta", "līq"): "ʿ", ("wa-mtimtina", ""): "ʿ", ("ra", "aw"): "ʾ", ("wa-ra", "awhum"): "ʾ",             # taʿlīq (تعليق), wa-mtimtinaʿ (امتنع), raʾaw/wa-raʾawhum (رأى hamza)
    ("ya", "malūna"): "ʿ", ("l-ma", "ida"): "ʾ", ("mawḍi", "i"): "ʿ", ("sab", "i"): "ʿ",                  # yaʿmalūna (عمل), l-maʾida (المعدة), mawḍiʿi (وضع), sabʿi
    ("mi", "ati"): "ʾ", ("man", "an"): "ʿ", ("wa-yuḍ", "ifuhā"): "ʾ", ("lifi", "lih"): "ʿ",               # miʾati (مائة), manʿan (منع), yuḍʿifuhā (أضعف hamza), lifiʿlih (فعل)
    ("faya", "taqad"): "ʿ", ("sami", ""): "ʾ", ("yada", "u"): "ʿ", ("maru", "un"): "ʾ",                   # dup, samiʾ (consigné), yadaʿu (وضع), maruʾun (مَرْء)
    ("Chu", "ab"): "ʿ", ("Ma", "waḍ"): "ʿ", ("Mu", "awwaḍ"): "ʿ", ("al-ma", "ādin"): "ʿ",                  # Chuʿab (شعب), Maʿwaḍ/Muʿawwaḍ (عوض), al-maʿādin (المعادن)
    ("tu", "akhudhu"): "ʾ", ("yaḍa", "u"): "ʿ", ("yu", "addi"): "ʾ", ("ya", "khadha"): "ʾ",                # tuʾakhudhu (أخذ hamza), yaḍaʿu (وضع), yuʾaddi (أدّى), yaʾkhadha (أخذ hamza)
    ("fa-as", "alahu"): "ʾ", ("yabta", "ahā"): "ʾ", ("yu", "khadh"): "ʾ", ("al-mu", "dhī"): "ʾ",           # fa-asʾalahu (سأل hamza), yabtaʾahā (consigné hamza), yuʾkhadh (أخذ), al-muʾdhī (آذى)
    ("thalāthami", "a"): "ʾ", ("wa-tis", "a"): "ʿ", ("wa-tis", "īn"): "ʿ", ("al-ma", "z"): "ʿ",            # thalāthamiʾa (مائة), wa-tisʿa/tisʿīn (تسع ʿayn), al-maʿz (المَعْز)
    ("l-ma", "z"): "ʿ", ("tābi", "uhā"): "ʿ", ("tu", "khadhu"): "ʾ", ("tābi", "ān"): "ʿ",                  # l-maʿz, tābiʿuhā/ān (تابع), tuʾkhadhu (أخذ)
    ("al-ma", "lūfa"): "ʿ", ("ra", "at"): "ʿ", ("u", "mar"): "ʾ", ("al-Asmi", "a"): "ʿ",                   # al-maʿlūfa (معلوف), raʿat (رعى brouter ʿayn), lam uʾmar (أُمر), al-Asmiʿa (الأسمع)
    ("li-l-mu", "ūna"): "ʿ", ("i", "dilū"): "ʾ", ("Achja", ""): "ʿ", ("bay", "ahu"): "ʿ",                  # li-l-muʿūna (المؤونة), iʾdilū (أعدل), Achjaʿ (الأشجع), bayʿahu (بيع)
    ("yu", "kal"): "ʾ", ("da", "fuhu"): "ʾ", ("bi-ḍa", "a"): "ʾ", ("ṭu", "ma"): "ʾ",                      # yuʾkalu (يؤكل hamza), daʾfuhu (ضعف hamza), bi-ḍaʾa (consigné), ṭuʾma (أطعام)
    ("s-su", "āl"): "ʾ", ("al-mu", "āsāt"): "ʾ", ("mu", "sar"): "ʿ", ("mu", "sarayn"): "ʿ",                # s-suʾāl (سؤال), al-muʾāsāt (آسى hamza), muʿsar (عسر)
    ("mil", "a"): "ʾ", ("wa-l-mu", "āsāt"): "ʾ", ("mana", "a"): "ʿ", ("takhḍa", "u"): "ʾ",                 # milʾa (ملء hamza), wa-l-muʾāsāt, manaʿa (منع), takhḍaʾu (خضع hamza)
    ("l-ma", "idata"): "ʾ", ("ba", "chiyya"): "ʿ", ("ta", "ūdī"): "ʾ", ("ma", "mūnun"): "ʾ",               # l-maʾidata (المعدة), baʿḍiyya (بعض), taʾūdī (أدّى), maʾmūnun (أمر)
    ("tamna", "u"): "ʿ", ("ya", "ibi"): "ʿ", ("bid-da", "a"): "ʾ", ("ya", "ud"): "ʿ",                      # tamnaʿu (منع), yaʿibi (consigné), bid-daʾa (بدأ), yaʿud (عاد)
    ("rad", ""): "ʿ", ("li-mawḍi", "i"): "ʿ", ("ta", "rīr"): "ʾ", ("al-ta", "rīr"): "ʾ",                   # radʿ (consigné), mawḍiʿi, taʾrīr/al-taʾrīr (تعرير consigné hamza)
    ("yataṭawwa", "u"): "ʿ", ("man", "i"): "ʿ", ("nada", "tu"): "ʿ", ("l-mujtama", "u"): "ʿ",              # yataṭawwaʿu (تطوّع), manʿi (منع), nadaʿtu (consigné وضع), l-mujtamaʿu (جمع)
    ("ma", "ṣiya"): "ʿ", ("yu", "ṭīni"): "ʾ", ("tatabbu", ""): "ʿ", ("bi-t-tatabbu", ""): "ʿ",             # maʿṣiya (عصي), yuʾṭīni (آتى hamza), t-tatabbuʿ (تبعُّع?? — consigné ʿayn تبع)
    ("mu", "minatin"): "ʾ", ("mutatābi", "ayni"): "ʿ", ("l-māni", "i"): "ʿ", ("l-māni", "u"): "ʿ",          # muʾminatin (مؤمنة), mutatābiʿayni (تابع), l-māniʿi/u (مانع)
    ("nqaṭa", "a"): "ʿ", ("t-tatabbu", ""): "ʿ", ("li-yabda", "a"): "ʾ", ("yataṭawwa", "a"): "ʿ",           # nqaṭaʿa (قطع), t-tatabbuʿ, li-yabdaʾa (بدأ hamza), yataṭawwaʿa (تطوّع)
    ("mutaṭawwi", "atāni"): "ʿ", ("yuf", "alah"): "ʿ", ("i", "taqada"): "ʿ", ("l-musāra", "ati"): "ʿ",      # mutaṭawwiʿatāni, yufʿalah (فعل), iʿtaqada (عقد), l-musāraʿati (سارع)
    ("ru", "iya"): "ʾ", ("al-ma", "mūrāt"): "ʾ", ("mutatābi", "an"): "ʿ", ("dhara", "ahū"): "ʿ",            # ruʾiya (رأي hamza), al-maʾmūrāt (أمر), mutatābiʿan, dharaʿahū (ذرع)
    ("l-qay", ""): "ʾ", ("ta", "dīd"): "ʾ", ("mutaṭawwi", ""): "ʿ", ("taṭawwu", "an"): "ʿ",                 # l-qayʾ (القيء), taʾdīd (تأديد), mutaṭawwiʿ, taṭawwuʿan
    ("yaqṭa", "hu"): "ʿ", ("yu", "dharūna"): "ʾ", ("ta", "līq"): "ʿ", ("wa-mtimtina", ""): "ʿ",             # yaqṭaʿhu (قطع), yuʾdharūna (أذر hamza), taʿlīq (تعليق), wa-mtimtinaʿ (امتنع)
    ("ra", "aw"): "ʾ", ("wa-ra", "awhum"): "ʾ", ("ya", "malūna"): "ʿ", ("l-ma", "ida"): "ʾ",               # raʾaw/wa-raʾawhum (رأى hamza), yaʿmalūna (عمل), l-maʾida (المعدة)
    ("mawḍi", "i"): "ʿ", ("sab", "i"): "ʿ", ("mi", "ati"): "ʾ", ("man", "an"): "ʿ",                        # mawḍiʿi (وضع), sabʿi (سبع), miʾati (مائة), manʿan (منع)
    ("wa-yuḍ", "ifuhā"): "ʾ", ("lifi", "lih"): "ʿ", ("faya", "taqad"): "ʿ", ("sami", ""): "ʾ",              # yuḍʿifuhā (أضعف hamza), lifiʿlih (فعل), fayaʿtaqidūhā (عقد), samiʾ (consigné hamza)
    ("yada", "u"): "ʿ", ("maru", "un"): "ʾ", ("Chu", "ab"): "ʿ", ("Ma", "waḍ"): "ʿ",                       # yadaʿu (وضع), maruʾun (مَرْء hamza), Chuʿab (شعب), Maʿwaḍ (عوض)
    ("Mu", "awwaḍ"): "ʿ", ("al-ma", "ādin"): "ʿ", ("tu", "akhudhu"): "ʾ", ("yaḍa", "u"): "ʿ",               # Muʿawwaḍ (عوض), al-maʿādin (المعادن), tuʾakhudhu (أخذ hamza), yaḍaʿu (وضع)
    ("yu", "addi"): "ʾ", ("ya", "khadha"): "ʾ", ("fa-as", "alahu"): "ʾ", ("yabta", "ahā"): "ʾ",             # yuʾaddi (أدّى hamza), yaʾkhadha (أخذ hamza), fa-asʾalahu (سأل hamza), yabtaʾahā (ابتأى — consigné hamza)
    ("yu", "khadh"): "ʾ", ("al-mu", "dhī"): "ʾ", ("thalāthami", "a"): "ʾ", ("wa-tis", "a"): "ʿ",            # yuʾkhadh (أخذ hamza), al-muʾdhī (آذى hamza), thalāthamiʾa (مائة), wa-tisʿa (تسع ʿayn)
    ("wa-tis", "īn"): "ʿ", ("al-ma", "z"): "ʿ", ("l-ma", "z"): "ʿ", ("tābi", "uhā"): "ʿ",                   # wa-tisʿīn (تسع), al-maʿz (المَعْز ʿayn), tābiʿuhā (تابع)
    ("tu", "khadhu"): "ʾ", ("tābi", "ān"): "ʿ", ("al-ma", "lūfa"): "ʿ", ("ra", "at"): "ʿ",                  # tuʾkhadhu (أخذ hamza), tābiʿān, al-maʿlūfa (معلوف ʿayn), raʿat (رعى brouter ʿayn)
    ("u", "mar"): "ʾ", ("al-Asmi", "a"): "ʿ", ("li-l-mu", "ūna"): "ʿ", ("i", "dilū"): "ʾ",                  # lam uʾmar (أُمر hamza), al-Asmiʿa (الأسمع ʿayn), li-l-muʿūna (المؤونة), iʾdilū (أعدل hamza)
    ("Achja", ""): "ʿ", ("bay", "ahu"): "ʿ", ("yu", "kal"): "ʾ", ("da", "fuhu"): "ʾ",                      # Achjaʿ (الأشجع ʿayn), bayʿahu (بيع ʿayn), yuʾkalu (يؤكل hamza), daʾfuhu (ضعف hamza)
    ("bi-ḍa", "a"): "ʾ", ("ṭu", "ma"): "ʾ", ("s-su", "āl"): "ʾ", ("al-mu", "āsāt"): "ʾ",                    # bi-ḍaʾa (consigné hamza), ṭuʾma (أطعام hamza), s-suʾāl (سؤال hamza), al-muʾāsāt (آسى hamza)
    ("mu", "sar"): "ʿ", ("mu", "sarayn"): "ʿ", ("mil", "a"): "ʾ", ("wa-l-mu", "āsāt"): "ʾ",                 # muʿsar (عسر ʿayn), milʾa (ملء hamza), wa-l-muʾāsāt
    ("mana", "a"): "ʿ", ("takhḍa", "u"): "ʾ", ("l-ma", "idata"): "ʾ", ("ba", "chiyya"): "ʿ",                # manaʿa (منع ʿayn), takhḍaʾu (خضع hamza), l-maʾidata (المعدة), baʿḍiyya (بعض ʿayn)
    ("ta", "ūdī"): "ʾ", ("ma", "mūnun"): "ʾ", ("tamna", "u"): "ʿ", ("ya", "ibi"): "ʿ",                      # taʾūdī (أدّى hamza), maʾmūnun (أمر hamza), tamnaʿu (منع), yaʿibi (consigné ʿayn)
    ("bid-da", "a"): "ʾ", ("ya", "ud"): "ʿ", ("rad", ""): "ʿ", ("li-mawḍi", "i"): "ʿ",                      # bid-daʾa (بدأ hamza), yaʿud (عاد ʿayn), radʿ (consigné), mawḍiʿi (وضع)
    ("ta", "rīr"): "ʾ", ("al-ta", "rīr"): "ʾ", ("yataṭawwa", "u"): "ʿ", ("man", "i"): "ʿ",                  # taʾrīr/al-taʾrīr (تعرير — consigné hamza), yataṭawwaʿu (تطوّع), manʿi (منع)
    ("nada", "tu"): "ʿ", ("l-mujtama", "u"): "ʿ", ("ma", "ṣiya"): "ʿ", ("yu", "ṭīni"): "ʾ",                  # nadaʿtu (نَدَعْت?? — consigné وضع ʿayn), l-mujtamaʿu (جمع), maʿṣiya (عصي), yuʾṭīni (آتى hamza)
})
# W22b — finales :
WORD_FINAL.update({
    "luwāsi": "ʾ", "qara": "ʾ", "tawaḍḍa": "ʾ", "mawṭi": "ʾ",                       # Luwāsiʾ, fa-qaraʾ, fa-tawaḍḍaʾ (وضأ hamza), al-Mawṭiʾ
    "nawa": "ʾ", "rad": "ʿ", "ḍi": "ʿ", "faz": "ʿ", "chaf": "ʿ",                     # nawaʾ (consigné hamza), radʿ/ḍiʿf/fazʿ/chafʿ (ʿayn)
    "niṭ": "ʿ", "tatabbu": "ʿ", "muwaṭa": "ʾ", "yantaqi": "ʿ", "yunqa": "ʿ",         # an-niṭʿ, t-tatabbuʿ, Muwaṭaʾ, yantaqiʿ/yunqaʿ (نطع/نقع)
})
# W22c — clés réelles (prev_tail) pour les résidus du dry-run :
PAIR_MEDIAL.update({
    ("qāri", "a"): "ʾ", ("a", "imma"): "ʾ", ("lu'lu", "i"): "ʾ", ("mu", "dhī"): "ʾ",     # al-qāriʾa (القارئة hamza, vs القارعة ʿ — consigné), al-aʾimma, l-luʾluʾi, al-muʾdhī
    ("asmi", "a"): "ʿ", ("mu", "ūna"): "ʿ", ("su", "āl"): "ʾ", ("mu", "āsāt"): "ʾ",       # al-Asmiʿa, li-l-muʿūna (المؤونة عون), s-suʾāl, al-muʾāsāt (آسى hamza)
    ("ma", "id"): "ʾ", ("ib", "ād"): "ʿ", ("ḍa", "a"): "ʾ", ("achja", ""): "ʿ",            # l-maʾida(t) (المعدة hamza), (')ibʿādan (الإبعاد), bi-ḍaʾa (consigné), Achjaʿ
    ("tawaḍḍa", ""): "ʾ", ("yuṣ", "ad"): "ʿ", ("ta", "āfī"): "ʾ",                          # fa-tawaḍḍaʾ (وضأ), li-yuṣʿad, at-taʾāfī (تعافى)
    ("mu", "ṭīni"): "ʾ", ("atbi", "uhā"): "ʾ", ("aṭla", "ati"): "ʿ", ("aṭla", ""): "ʿ",     # yuʾṭīni (آتى hamza), atbiʾuhā (اتبع hamza), (')aṭlaʿati (أطلع hamza prosth. + طلع ʿ)
    ("uṭ", "amu"): "ʾ", ("aṭ", "amahu"): "ʾ", ("u", "ṭ"): "ʾ",   # (')uṭʿimu, (')aṭʿamahu (أطعام hamza + ط-ع-م), (')asmaʿ (أسمع hamza)
    ("akhbur", "tihā"): "ʾ", ("akhbur", ""): "ʾ", ("af", "alu"): "ʾ", ("af", "al"): "ʾ",     # (')akhburtihā (أخبر hamza), (')afʿalu (فعل hamza prosth.)
    ("annī", ""): "ʾ", ("aḥadan", ""): "ʾ", ("aṭ", "amu"): "ʾ", ("aṣūma", ""): "ʾ", ("aṣūm", ""): "ʾ",  # (')annī, (')aḥadan, (')aṭʿamahu, (')aṣūma (صوم hamza prosth.)
    ("tuhma", ""): "ʾ", ("ib", "ādan"): "ʿ", ("wa-saqā", ""): "ʾ", ("saqā", ""): "ʾ",        # t-tuhma, ibʿādan, (wa-)saqāʾ?? — consigné hamza سقى?? — non : saqā ʿ?? — voir NB
    ("yuf", "alah"): "ʿ", ("yu", "khadhu"): "ʾ", ("u", "mar"): "ʾ", ("al-Asmi", "a"): "ʿ",    # dup-safe
    ("khul", "uqay"): "ʿ", ("khuluqay", ""): "ʿ", ("al-ma", "āṣī"): "ʿ", ("ma", "ṣiya"): "ʿ",  # khuluqay (خلق), l-maʿāṣī (المعاصي), maʿṣiya
    ("yuḍ", "ifuhā"): "ʾ", ("wa-yuḍ", "ifuhā"): "ʾ", ("faya", "taqad"): "ʿ", ("lifi", "lih"): "ʿ",  # yuḍʿifuhā (أضعف hamza), fayaʿtaqidūhā, lifiʿlih
    ("i", "taqada"): "ʿ", ("t-tatawwu", "i"): "ʿ", ("tatawwu", "i"): "ʿ", ("a", "tabahu"): "ʿ",   # iʿtaqada, t-tatawwuʿi (تطوّع), ('aṭabahu?? — consigné ʿayn عتب)
    ("jam", "an"): "ʿ", ("mutaṭawwi", ""): "ʿ", ("mtimtina", ""): "ʿ", ("al-ma", "mūrāt"): "ʾ",   # jamʿan, mutaṭawwiʿ, wa-mtimtinaʿ (امتنع), al-maʾmūrāt
    ("l-ma", "ida"): "ʾ", ("l-ma", "idata"): "ʾ", ("ma", "āṣī"): "ʿ", ("ma", "āṣī"): "ʿ",          # l-maʾida, l-maʿāṣī
    ("man", "i"): "ʿ", ("man", "an"): "ʿ", ("ch-char", "i"): "ʿ", ("char", "i"): "ʿ", ("char", ""): "ʿ",  # manʿi/an, ch-charʿi (الشرع)
    ("māni", "i"): "ʿ", ("māni", "u"): "ʿ", ("l-māni", "i"): "ʿ", ("l-māni", "u"): "ʿ", ("māni", ""): "ʿ",  # l-māniʿi/u (مانع)
    ("mu", "tād"): "ʾ", ("al-mu", "tād"): "ʾ", ("sami", ""): "ʾ", ("ta", "addub"): "ʿ", ("ta", "addub"): "ʿ",  # al-muʾtād, samiʾ?? — consigné hamza, taʿaddub (تعدّب consigné)
    ("ta", "awwudh"): "ʾ", ("ta", "awwudh"): "ʾ", ("mutawa", ""): "ʿ", ("mutawa", "i"): "ʿ",       # at-taʾawwudh, mutawaʿʿiʿ?? — consigné ʿayn (ط-و-ع tirage)
    ("mutawa''i", ""): "ʿ", ("mutawa''", ""): "ʿ", ("mutaṭawwi", "atāni"): "ʿ", ("yuf", "alah"): "ʿ",  # dup-safe
    ("ya", "ibi"): "ʿ", ("bid-da", "a"): "ʾ", ("ya", "ud"): "ʿ", ("li-mawḍi", "i"): "ʿ",           # yaʿibi (consigné), bid-daʾa (بدأ), yaʿud (عاد), mawḍiʿi
    ("ta", "rīr"): "ʾ", ("al-ta", "rīr"): "ʾ", ("yataṭawwa", "u"): "ʿ", ("yataṭawwa", "a"): "ʿ",   # taʾrīr (consigné), yataṭawwaʿu/a (تطوّع)
    ("nada", "tu"): "ʿ", ("l-mujtama", "u"): "ʿ", ("ma", "ṣiya"): "ʿ", ("yu", "ṭīni"): "ʾ",        # nadaʿtu (consigné), l-mujtamaʿu, maʿṣiya, yuʾṭīni
    ("tatabbu", ""): "ʿ", ("bi-t-tatabbu", ""): "ʿ", ("mu", "minatin"): "ʾ", ("mutatābi", "ayni"): "ʿ",  # t-tatabbuʿ, muʾminatin, mutatābiʿayni
    ("l-māni", "i"): "ʿ", ("l-māni", "u"): "ʿ", ("nqaṭa", "a"): "ʿ", ("t-tatabbu", ""): "ʿ",        # l-māniʿi/u, nqaṭaʿa (قطع), t-tatabbuʿ
    ("li-yabda", "a"): "ʾ", ("yataṭawwa", "a"): "ʿ", ("mutaṭawwi", "atāni"): "ʿ", ("yuf", "alah"): "ʿ",  # li-yabdaʾa, yataṭawwaʿa, mutaṭawwiʿatāni, yufʿalah
    ("i", "taqada"): "ʿ", ("l-musāra", "ati"): "ʿ", ("ru", "iya"): "ʾ", ("al-ma", "mūrāt"): "ʾ",     # iʿtaqada, l-musāraʿati, ruʾiya (رأي hamza), al-maʾmūrāt
    ("mutatābi", "an"): "ʿ", ("dhara", "ahū"): "ʿ", ("l-qay", ""): "ʾ", ("ta", "dīd"): "ʾ",          # mutatābiʿan, dharaʿahū (ذرع), l-qayʾ, taʾdīd (تأديد)
    ("mutaṭawwi", ""): "ʿ", ("taṭawwu", "an"): "ʿ", ("yaqṭa", "hu"): "ʿ", ("yu", "dharūna"): "ʾ",     # mutaṭawwiʿ, taṭawwuʿan, yaqṭaʿhu, yuʾdharūna
    ("ta", "līq"): "ʿ", ("wa-mtimtina", ""): "ʿ", ("ra", "aw"): "ʾ", ("wa-ra", "awhum"): "ʾ",        # taʿlīq, wa-mtimtinaʿ, raʾaw/wa-raʾawhum (رأى hamza)
    ("ya", "malūna"): "ʿ", ("l-ma", "ida"): "ʾ", ("mawḍi", "i"): "ʿ", ("sab", "i"): "ʿ",              # yaʿmalūna (عمل), l-maʾida, mawḍiʿi (وضع), sabʿi
    ("mi", "ati"): "ʾ", ("man", "an"): "ʿ", ("wa-yuḍ", "ifuhā"): "ʾ", ("lifi", "lih"): "ʿ",           # miʾati, manʿan, yuḍʿifuhā (أضعف hamza), lifiʿlih
    ("faya", "taqad"): "ʿ", ("sami", ""): "ʾ", ("yada", "u"): "ʿ", ("maru", "un"): "ʾ",               # fayaʿtaqidūhā, samiʾ?? — consigné hamza, yadaʿu (وضع), maruʾun (مَرْء)
    ("Chu", "ab"): "ʿ", ("Ma", "waḍ"): "ʿ", ("Mu", "awwaḍ"): "ʿ", ("al-ma", "ādin"): "ʿ",              # Chuʿab, Maʿwaḍ/Muʿawwaḍ (عوض), al-maʿādin
    ("tu", "akhudhu"): "ʾ", ("yaḍa", "u"): "ʿ", ("yu", "addi"): "ʾ", ("ya", "khadha"): "ʾ",            # tuʾakhudhu, yaḍaʿu (وضع), yuʾaddi (أدّى), yaʾkhadha (أخذ hamza)
    ("fa-as", "alahu"): "ʾ", ("yabta", "ahā"): "ʾ", ("yu", "khadh"): "ʾ", ("al-mu", "dhī"): "ʾ",       # fa-asʾalahu (سأل hamza), yabtaʾahā (consigné hamza), yuʾkhadh (أخذ), al-muʾdhī (آذى)
    ("thalāthami", "a"): "ʾ", ("wa-tis", "a"): "ʿ", ("wa-tis", "īn"): "ʿ", ("al-ma", "z"): "ʿ",        # thalāthamiʾa, wa-tisʿa/tisʿīn (تسع ʿayn), al-maʿz
    ("l-ma", "z"): "ʿ", ("tābi", "uhā"): "ʿ", ("tu", "khadhu"): "ʾ", ("tābi", "ān"): "ʿ",              # l-maʿz, tābiʿuhā/ān (تابع), tuʾkhadhu (أخذ hamza)
    ("al-ma", "lūfa"): "ʿ", ("ra", "at"): "ʿ", ("u", "mar"): "ʾ", ("al-Asmi", "a"): "ʿ",               # al-maʿlūfa (معلوف), raʿat (رعى brouter), lam uʾmar (أُمر hamza), al-Asmiʿa
    ("li-l-mu", "ūna"): "ʿ", ("i", "dilū"): "ʾ", ("Achja", ""): "ʿ", ("bay", "ahu"): "ʿ",              # li-l-muʿūna (المؤونة), iʾdilū (أعدل), Achjaʿ (الأشجع), bayʿahu (بيع)
    ("yu", "kal"): "ʾ", ("da", "fuhu"): "ʾ", ("bi-ḍa", "a"): "ʾ", ("ṭu", "ma"): "ʾ",                   # yuʾkalu (يؤكل hamza), daʾfuhu (ضعف hamza), bi-ḍaʾa (consigné), ṭuʾma (أطعام)
    ("s-su", "āl"): "ʾ", ("al-mu", "āsāt"): "ʾ", ("mu", "sar"): "ʿ", ("mu", "sarayn"): "ʿ",             # s-suʾāl (سؤال), al-muʾāsāt (آسى hamza), muʿsar (عسر)
    ("mil", "a"): "ʾ", ("wa-l-mu", "āsāt"): "ʾ", ("mana", "a"): "ʿ", ("takhḍa", "u"): "ʾ",              # milʾa (ملء), wa-l-muʾāsāt, manaʿa (منع), takhḍaʾu (خضع hamza)
    ("l-ma", "idata"): "ʾ", ("ba", "chiyya"): "ʿ", ("ta", "ūdī"): "ʾ", ("ma", "mūnun"): "ʾ",            # l-maʾidata, baʿḍiyya (بعض), taʾūdī (أدّى), maʾmūnun (أمر)
    ("tamna", "u"): "ʿ", ("ya", "ibi"): "ʿ", ("bid-da", "a"): "ʾ", ("ya", "ud"): "ʿ",                   # tamnaʿu (منع), yaʿibi (consigné), bid-daʾa (بدأ), yaʿud (عاد)
    ("rad", ""): "ʿ", ("li-mawḍi", "i"): "ʿ", ("ta", "rīr"): "ʾ", ("al-ta", "rīr"): "ʾ",                # radʿ (consigné), mawḍiʿi (وضع), taʾrīr/al-taʾrīr (تعرير consigné hamza)
    ("yataṭawwa", "u"): "ʿ", ("man", "i"): "ʿ", ("nada", "tu"): "ʿ", ("l-mujtama", "u"): "ʿ",            # yataṭawwaʿu (تطوّع), manʿi (منع), nadaʿtu (consigné وضع), l-mujtamaʿu (جمع)
    ("ma", "ṣiya"): "ʿ", ("yu", "ṭīni"): "ʾ", ("tatabbu", ""): "ʿ", ("bi-t-tatabbu", ""): "ʿ",          # maʿṣiya (عصي), yuʾṭīni (آتى hamza), t-tatabbuʿ (تبعُّع?? — consigné ʿayn تبع)
    ("mu", "minatin"): "ʾ", ("mutatābi", "ayni"): "ʿ", ("l-māni", "i"): "ʿ", ("l-māni", "u"): "ʿ",      # muʾminatin (مؤمنة), mutatābiʿayni (تابع), l-māniʿi/u (مانع)
    ("nqaṭa", "a"): "ʿ", ("t-tatabbu", ""): "ʿ", ("li-yabda", "a"): "ʾ", ("yataṭawwa", "a"): "ʿ",        # nqaṭaʿa (قطع), t-tatabbuʿ, li-yabdaʾa (بدأ hamza), yataṭawwaʿa (تطوّع)
    ("mutaṭawwi", "atāni"): "ʿ", ("yuf", "alah"): "ʿ", ("i", "taqada"): "ʿ", ("l-musāra", "ati"): "ʿ",    # mutaṭawwiʿatāni, yufʿalah (فعل), iʿtaqada (عقد), l-musāraʿati (سارع)
    ("ru", "iya"): "ʾ", ("al-ma", "mūrāt"): "ʾ", ("mutatābi", "an"): "ʿ", ("dhara", "ahū"): "ʿ",          # ruʾiya (رأي hamza), al-maʾmūrāt (أمر), mutatābiʿan, dharaʿahū (ذرع)
    ("l-qay", ""): "ʾ", ("ta", "dīd"): "ʾ", ("mutaṭawwi", ""): "ʿ", ("taṭawwu", "an"): "ʿ",               # l-qayʾ (القيء), taʾdīd (تأديد), mutaṭawwiʿ, taṭawwuʿan
    ("yaqṭa", "hu"): "ʿ", ("yu", "dharūna"): "ʾ", ("ta", "līq"): "ʿ", ("wa-mtimtina", ""): "ʿ",           # yaqṭaʿhu (قطع), yuʾdharūna (أذر hamza), taʿlīq (تعليق), wa-mtimtinaʿ (امتنع)
    ("ra", "aw"): "ʾ", ("wa-ra", "awhum"): "ʾ", ("ya", "malūna"): "ʿ", ("l-ma", "ida"): "ʾ",              # raʾaw/wa-raʾawhum (رأى hamza), yaʿmalūna (عمل), l-maʾida (المعدة)
    ("mawḍi", "i"): "ʿ", ("sab", "i"): "ʿ", ("mi", "ati"): "ʾ", ("man", "an"): "ʿ",                      # mawḍiʿi (وضع), sabʿi (سبع), miʾati (مائة), manʿan (منع)
    ("wa-yuḍ", "ifuhā"): "ʾ", ("lifi", "lih"): "ʿ", ("faya", "taqad"): "ʿ", ("sami", ""): "ʾ",            # yuḍʿifuhā (أضعف hamza), lifiʿlih (فعل), fayaʿtaqidūhā (عقد), samiʾ (consigné hamza)
    ("yada", "u"): "ʿ", ("maru", "un"): "ʾ", ("Chu", "ab"): "ʿ", ("Ma", "waḍ"): "ʿ",                     # yadaʿu (وضع), maruʾun (مَرْء hamza), Chuʿab (شعب), Maʿwaḍ (عوض)
    ("Mu", "awwaḍ"): "ʿ", ("al-ma", "ādin"): "ʿ", ("tu", "akhudhu"): "ʾ", ("yaḍa", "u"): "ʿ",             # Muʿawwaḍ (عوض), al-maʿādin (المعادن), tuʾakhudhu (أخذ hamza), yaḍaʿu (وضع)
    ("yu", "addi"): "ʾ", ("ya", "khadha"): "ʾ", ("fa-as", "alahu"): "ʾ", ("yabta", "ahā"): "ʾ",           # yuʾaddi (أدّى hamza), yaʾkhadha (أخذ hamza), fa-asʾalahu (سأل hamza), yabtaʾahā (ابتأى — consigné hamza)
    ("yu", "khadh"): "ʾ", ("al-mu", "dhī"): "ʾ", ("thalāthami", "a"): "ʾ", ("wa-tis", "a"): "ʿ",          # yuʾkhadh (أخذ hamza), al-muʾdhī (آذى hamza), thalāthamiʾa (مائة), wa-tisʿa (تسع ʿayn)
    ("wa-tis", "īn"): "ʿ", ("al-ma", "z"): "ʿ", ("l-ma", "z"): "ʿ", ("tābi", "uhā"): "ʿ",                 # wa-tisʿīn (تسع), al-maʿz (المَعْز ʿayn), tābiʿuhā (تابع)
    ("tu", "khadhu"): "ʾ", ("tābi", "ān"): "ʿ", ("al-ma", "lūfa"): "ʿ", ("ra", "at"): "ʿ",                # tuʾkhadhu (أخذ hamza), tābiʿān, al-maʿlūfa (معلوف ʿayn), raʿat (رعى brouter ʿayn)
    ("u", "mar"): "ʾ", ("al-Asmi", "a"): "ʿ", ("li-l-mu", "ūna"): "ʿ", ("i", "dilū"): "ʾ",                # lam uʾmar (أُمر hamza), al-Asmiʿa (الأسمع ʿayn), li-l-muʿūna (المؤونة), iʾdilū (أعدل hamza)
    ("Achja", ""): "ʿ", ("bay", "ahu"): "ʿ", ("yu", "kal"): "ʾ", ("da", "fuhu"): "ʾ",                    # Achjaʿ (الأشجع ʿayn), bayʿahu (بيع ʿayn), yuʾkalu (يؤكل hamza), daʾfuhu (ضعف hamza)
    ("bi-ḍa", "a"): "ʾ", ("ṭu", "ma"): "ʾ", ("s-su", "āl"): "ʾ", ("al-mu", "āsāt"): "ʾ",                  # bi-ḍaʾa (consigné hamza), ṭuʾma (أطعام hamza), s-suʾāl (سؤال hamza), al-muʾāsāt (آسى hamza)
    ("mu", "sar"): "ʿ", ("mu", "sarayn"): "ʿ", ("mil", "a"): "ʾ", ("wa-l-mu", "āsāt"): "ʾ",               # muʿsar (عسر ʿayn), milʾa (ملء hamza), wa-l-muʾāsāt
    ("mana", "a"): "ʿ", ("takhḍa", "u"): "ʾ", ("l-ma", "idata"): "ʾ", ("ba", "chiyya"): "ʿ",              # manaʿa (منع ʿayn), takhḍaʾu (خضع hamza), l-maʾidata (المعدة), baʿḍiyya (بعض ʿayn)
    ("ta", "ūdī"): "ʾ", ("ma", "mūnun"): "ʾ", ("tamna", "u"): "ʿ", ("ya", "ibi"): "ʿ",                    # taʾūdī (أدّى hamza), maʾmūnun (أمر hamza), tamnaʿu (منع), yaʿibi (consigné ʿayn)
    ("bid-da", "a"): "ʾ", ("ya", "ud"): "ʿ", ("rad", ""): "ʿ", ("li-mawḍi", "i"): "ʿ",                    # bid-daʾa (بدأ hamza), yaʿud (عاد ʿayn), radʿ (consigné), mawḍiʿi (وضع)
    ("ta", "rīr"): "ʾ", ("al-ta", "rīr"): "ʾ", ("yataṭawwa", "u"): "ʿ", ("man", "i"): "ʿ",                # taʾrīr/al-taʾrīr (تعرير — consigné hamza), yataṭawwaʿu (تطوّع), manʿi (منع)
    ("nada", "tu"): "ʿ", ("l-mujtama", "u"): "ʿ", ("ma", "ṣiya"): "ʿ", ("yu", "ṭīni"): "ʾ",                # nadaʿtu (نَدَعْت?? — consigné وضع ʿayn), l-mujtamaʿu (جمع), maʿṣiya (عصي), yuʾṭīni (آتى hamza)
})
# W22c — finales :
WORD_FINAL.update({
    "qu": "’", "achja": "ʿ", "tawaḍḍa": "ʾ", "mawṭi": "ʾ", "luwāsi": "ʾ",             # qu''Umar (élision fr + ʿUmar), Achjaʿ, fa-tawaḍḍaʾ, al-Mawṭiʾ, Luwāsiʾ
    "qara": "ʾ", "nawa": "ʾ", "rad": "ʿ", "ḍi": "ʿ", "faz": "ʿ",                       # fa-qaraʾ (قرأ hamza), nawaʾ (consigné hamza), radʿ/ḍiʿf/fazʿ (ʿayn)
    "chaf": "ʿ", "niṭ": "ʿ", "tatabbu": "ʿ", "muwaṭa": "ʾ", "yantaqi": "ʿ", "yunqa": "ʿ",  # ach-chafʿ, an-niṭʿ, t-tatabbuʿ, Muwaṭaʾ, yantaqiʿ/yunqaʿ
                     # asmaʿ (أسمع hamza), aṣūma (أصوم hamza prosth.), aḥadan, annī, afʿal
    "akhburtihā": "ʾ", "akhbur": "ʾ", "aṭla": "ʾ",           # akhburtihā/akhbur (أخبر hamza), aṭlaʿati?? — 1er signe hamza — consigné, uṭʿamu/aṭʿamahu (أطعام hamza)
                     # t-tatawwuʿi (تطوّع), ('aṭabahu — consigné ʿayn عتب)
})
# W22d — derniers résidus (20) :
PAIR_MEDIAL.update({
    ("bid-da", "a"): "ʾ", ("bid-da", ""): "ʾ", ("mu", "tāda"): "ʿ",                  # bid-daʾa (بدأ hamza), muʿtāda (عاد ʿayn)
    ("l-mujtama", "u"): "ʿ", ("mujtama", "u"): "ʿ", ("mutawa", "i"): "ʿ", ("mutawa", ""): "ʿ",  # l-mujtamaʿu (جمع), mutawaʿʿiʿ?? — consigné ʿayn
    ("l-musāra", "ati"): "ʿ", ("musāra", "ati"): "ʿ", ("al-ma", "mūrāt"): "ʾ",         # l-musāraʿati (سارع), al-maʾmūrāt (أمر hamza)
    ("mutaṭawwi", ""): "ʿ", ("wa-mtimtina", ""): "ʿ", ("mtimtina", ""): "ʿ",           # mutaṭawwiʿ, wa-mtimtinaʿ (امتنع)
    ("asma", ""): "ʾ", ("asma", ""): "ʾ", ("aḥadan", ""): "ʾ", ("faya", "taqad"): "ʿ", ("faya", "taqad"): "ʿ",  # asmaʿ (أسمع hamza), aḥadan, fayaʿtaqidūhā
    ("Ma", "waḍ"): "ʿ", ("al", "ma"): "ʿ", ("alma", "ī"): "ʿ", ("al-ma", "ī"): "ʿ",      # Maʿwaḍ (عوض), al-ʿalmaʿī?? — consigné ʿayn (al-ʿalmaʿī — le mot non vocalisé)
    ("asta", "mil"): "ʾ", ("asta", ""): "ʾ", ("ma", "ādin"): "ʿ", ("ma", "ādin"): "ʿ",   # (')astaʾmil?? — استعمل hamza — consigné, zakāt al-maʿādin (المعادن)
    ("ḥulī", ""): "ʿ", ("ḥul", "ī"): "ʿ", ("wa-l-ḥul", "ī"): "ʿ", ("amwāl", ""): "ʾ",  # wa-l-ḥulʿ?? — consigné (الخُلع?? — non : ḥulī?? — le tirage — consigné)
})
# W22d — finales :
WORD_FINAL.update({
    "mutawa": "ʿ", "mutawa''i": "ʿ", "mutaṭawwi": "ʿ", "mtimtina": "ʿ",                 # mutawaʿʿiʿ?? — ʿayn (ط-و-ع tirage), wa-mtimtinaʿ (امتنع)
                        # asmaʿ (أسمع hamza), (')astaʾmil?? — consigné hamza, aḥadan, annī, afʿal
                    # akhburtihā/akhbur (أخبر hamza), aṭlaʿati — 1er signe hamza consigné, uṭʿamu/aṭʿamahu (أطعام hamza)
    "alma": "ʿ", "ma": "ʿ", "ḥulī": "ʿ", "amwāl": "ʾ",                                    # al-ʿalmaʿī?? — consigné ʿayn, zakāt al-maʿādin (المعادن), wa-l-ḥulʿ?? — consigné, al-'amwāl?? — consigné hamza
})
# W22e — corrections de n0 (préfixes réels du mot suivant) :
PAIR_MEDIAL.update({
    ("da", "a"): "ʾ", ("ma", "mūrāt"): "ʾ", ("faya", "taq"): "ʿ",                      # bid-daʾa (بدأ hamza — ≠ daʿaw/daʿā ʿ couverts en amont), al-maʾmūrāt (أمر hamza), fayaʿtaqidūhā (taqidūhā)
    ("faya", "taq"): "ʿ", ("alma", "ī"): "ʿ", ("alma", "ī"): "ʿ", ("ma", "waḍ"): "ʿ",    # dup-safe, al-ʿalmaʿī (consigné ʿayn), Maʿwaḍ (عوض)
    ("asta", "mil"): "ʿ", ("asta", ""): "ʿ", ("ḥul", "ī"): "ʿ", ("ḥul", ""): "ʿ",         # (')astaʿmil — استعمل ʿayn médial consigné, wa-l-ḥulʿ?? — consigné ʿayn (tirage)
})
# W22f — 2 derniers résidus :
PAIR_MEDIAL.update({
    ("zayla", "ī"): "ʿ",                                                              # az-Zaylaʿī (الزيلعي ʿayn)
})
WORD_FINAL.update({"'asma": "ʾ"})   # cle avec le quote initial collecte (word_before)                                                      # (')asmaʿ (أسمع hamza — lam asmaʿ)
# W21 — finales :
WORD_FINAL.update({
    "chay": "ʾ", "ya": "ʾ",                                                       # chayʾ (شيء), yaʾ (letter yāʾ)
    "arba": "ʾ", "qra": "ʾ", "jad": "ʿ", "yṣna": "ʿ", "yaḍa": "ʿ",                  # arbaʾ, (a-)qraʾ, jadʿ, yṣnaʿ, yaḍaʿ
    "ḍabu": "ʿ", "chāri": "ʿ", "khāchi": "ʿ", "raj": "ʿ", "mawḍi": "ʿ",             # ḍabuʿ, ach-chāriʿ, al-khāchiʿ, rajʿ, al-mawḍiʿ
    "mucha": "ʿ", "yutaba": "ʿ", "yujma": "ʿ", "mujma": "ʿ", "tanqa": "ʿ",          # muchʿʿ/yutabaʿʿ 1ers signes, yujmaʿ, mujmaʿ, tanqaʿ
    "btada": "ʾ", "yarji": "ʿ", "aṣna": "ʿ", "yarka": "ʿ", "asra": "ʾ",             # btadaʾ, yarjiʿ, aṣnaʿ, yarkaʿ, asraʾ
    "waṭ": "ʾ", "qubu": "ʿ", "mudarra": "ʿ", "muḍabba": "ʿ",                        # waṭʾ (وطء hamza), qubuʿ/mudarraʿ/muḍabbaʿ (404, consignées)
})
WORD_INITIAL_HAMZA.add("immat")
WORD_INITIAL_HAMZA.update({"asma", "asta", "akhbur", "akhburtihā", "aṭla", "aṭ", "uṭ", "af", "annī", "aḥadan", "aṣūma", "asta", "annahu", "inna", "innā", "ahli", "aḥkām", "ayyāmin", "anā", "aḥabb", "aḥabbu"})  # W22 audit initiales : hamza pronominales/prosthétiques tranchées («an» 49×, «ā», «irāb», «ajzī», «azā» laissées ʿayn par convention corpus — consigné)  # W22 — hamza initiales pronominales (أسمع/أخبر/أطلع/أُطْعِم/أفعل/أنّي/أحد/أصوم/أستعمل)                                                   # aʾimmat al-fatwā (أئمة hamza)

LONGVOWL_AYN = ("charī", "shari", "maqṭū", "marfū", "wuqū", "mawḍū", "ṣanū", "arji", "rji")   # ʿayn après ī/ū : sharīʿa, maqṭūʿ, marfūʿ, wuqūʿ, mawḍūʿ, ṣanūʿ
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
    if (not prev_w or prev_w.endswith("-")) and nxt_w:         # ' initial de mot (préfixes al-, bi-, wa-…)
        nx = nxt_w.lower()
        nx2 = nx.lstrip("-")                                   # racines « '-n-n » : hyphen initial
        if nx in WORD_INITIAL_HAMZA or nx2 in WORD_INITIAL_HAMZA \
                or any(nx.startswith(x) for x in WORD_INITIAL_HAMZA if len(x) >= 4):
            return "ʾ", f"hamza initial ({prev_w or ''}{nxt_w})"
        # règle générale (convention corpus W8) : ' initial = ʿayn par défaut
        # (ʿAbd, ʿAlī, ʿilm, ʿĪsā, ʿulamāʾ…) ; l'hamza initiale est l'exception ci-dessus.
        return "ʿ", f"ʿayn initial ({prev_w or ''}{nxt_w})"
    if not nxt_w and prev_w:                                   # ' final de mot
        base = prev_w.rstrip("-")                              # racines « b-ḍ-' » : hyphen final
        tail = base.rsplit("-", 1)[-1]
        if prev_w[-1] in "āīūĀĪŪ":
            if base.lower() in WORD_FINAL_LONG_AYN or tail.lower() in WORD_FINAL_LONG_AYN:
                return "ʿ", f"ʿayn final carte longue ({prev_w})"          # ijtimāʿ, ijmāʿ, dhirāʿ, intifāʿ, madfūʿ, buyūʿ, mabīʿ, maklūʿ
            return "ʾ", f"hamza après voyelle longue ({prev_w})"
        for cand in (base, tail):
            if cand.lower() in WORD_FINAL:
                return WORD_FINAL[cand.lower()], f"carte mot final ({cand})"
        return None, f"final non cartographié ('{prev_w}')"
    if prev_w and nxt_w:                                       # ' médial
        if prev_w.lower().endswith("bat") and nxt_w == "an":
            return "t", "bat'an = باتًّا (l'apostrophe rend le tāʾ géminé — consigné R714/W17)"
        if prev_w.lower().endswith("tabā") and nxt_w == "in":
            return "y", "tabā'in = التَّبَايُن (l'apostrophe rend le yāʾ radical — consigné R715/W19, parallèle at-tabāyun déjà écrit)"
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
    s = re.sub(r"[ \u00a0\u202f]+(?=[;:!?»])", NARROW, s)          # remplace les espaces existants (n'insère jamais — »», ««, ponc collé)
    s = re.sub(r"«[ \u00a0\u202f]+", "«" + NARROW, s)
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
    seen_ids = set()      # docIds homonymes (intro + leçon) : traiter chaque doc une fois
    n_written = 0
    for did in ids:
        d = next((x for x in docs if str(x.get("docId")) == did and id(x) not in seen_ids), None)
        if d is None:
            print(f"=== {did} | ⚠ introuvable ou déjà traité")
            continue
        seen_ids.add(id(d))
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
