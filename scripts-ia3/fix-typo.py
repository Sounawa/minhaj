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
LONGVOWL_AYN = ("charī", "shari", "maqṭū", "marfū", "wuqū", "mawḍū", "ṣanū")   # ʿayn après ī/ū : sharīʿa, maqṭūʿ, marfūʿ, wuqūʿ, mawḍūʿ, ṣanūʿ
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
