# -*- coding: utf-8 -*-
"""W23 — carte taqtit-tanawi-1 : insère les paires/finales arbitrées dans fix-typo.py."""
P = "scripts-ia3/fix-typo.py"
s = open(P, encoding="utf-8").read()
assert "W23" not in s, "déjà appliqué"

PAIRS = '''
# W23 — taqtit-tanawi-1 (taqwīt/al-Malṭaʿ + al-Muqniʿ) :
PAIR_MEDIAL.update({
    ("i", "tidāl"): "ʿ", ("i", "dād"): "ʾ", ("i", "rāb"): "ʿ", ("i", "tabir"): "ʿ", ("i", "lam"): "ʿ",  # iʿtidāl اعتدال ʿ ; l-iʾdād إعداد ʾ ; al-iʿrāb ʿ ; fa-iʿtabir ; wa-iʿlam
    ("ta", "lamū"): "ʿ", ("lita", "lamū"): "ʿ", ("ta", "uddu"): "ʿ", ("ta", "rif"): "ʿ",                 # taʿlamūn/li-taʿlamū (ع-ل-م), taʿuddu (ع-د-د), taʿrifuhu
    ("ta", "yīm"): "ʾ", ("ta", "rīkh"): "ʾ",                                                            # taʾyīm تأييم, taʾrīkh تأريخ
    ("l", "ichā"): "ʿ", ("chu", "ā"): "ʿ",                                                              # l-ʿichāʾ (عشاء ʿayn + hamza finale auto), chuʿāʿ شعاع (2ʿ)
    ("s", "al"): "ʾ", ("as", "al"): "ʾ", ("fasta", "inī"): "ʿ", ("sta", "antu"): "ʿ", ("astach", "iru"): "ʿ",  # fa-sʾalū/wa-asʾalu (س-أ-ل hamza), fastaʿīnī/staʿantu/astashʿiru (ʿ-w-n, sh-ʿ-r)
    ("mu", "akhir"): "ʾ", ("mu", "tadila"): "ʿ", ("mu", "qni"): "ʿ", ("mu", "tami"): "ʿ",                 # al-muʾakhkhar المؤخر hamza ; muʿtadila ; al-muqniʿa (consigné) ; al-Muʿtamiʿ variante al-Malṭaʿ (consigné)
    ("haq", "a"): "ʿ", ("han", "a"): "ʿ", ("sa", "ūd"): "ʿ", ("su", "ūd"): "ʿ",                          # al-haqʿa/al-hanʿa (mansions h-q-ʿ, h-n-ʿ), saʿūd/as-suʿūd (س-ع-د)
    ("ṭāli", ""): "ʿ", ("ṭala", ""): "ʿ", ("qṭa", "ā"): "ʿ",                                             # ṭāliʿa/ṭ-ṭāliʿu (ط-ل-ع), ṭalaʿā, iqṭaʿā/qṭaʿā (ق-ط-ع)
    ("qiṭ", "a"): "ʿ", ("qi", "da"): "ʿ", ("qaṭ", "an"): "ʿ", ("rub", ""): "ʿ",                          # qiṭʿa (ق-ط-ع), qiʿda al-qiʿda (ق-ع-د), qaṭʿan, rubʿ/wa-rubʿun (ر-ب-ع)
    ("ba", "īd"): "ʿ", ("rābi", ""): "ʿ", ("sābi", ""): "ʿ", ("tāsi", ""): "ʿ", ("al-a", "ẓam"): "ʿ",     # al-baʿīd (ب-ع-د), rābiʿu, sābiʿuhū/sābiʿin, tāsiʿun, al-aʿẓam
    ("j", "al"): "ʿ", ("ij", "al"): "ʿ", ("zar", "an"): "ʿ", ("turja", ""): "ʿ", ("mun", "adim"): "ʿ",    # ijʿal/wa-jʿali (ج-ع-ل ʿayn médial!), zarʿan (ز-ر-ع), turjaʿūn (ر-ج-ع), munʿadim (ن-ع-د-م)
    ("ṣa", "faḍ"): "ʿ", ("sa", "faṣ"): "ʿ", ("ṣa", "ba"): "ʿ", ("nu", "in"): "ʿ",                        # ṣaʿfaḍ/saʿfaṣ (abjad سعفص ʿayn), ṣaʿba, nuʿīn (babt نعين)
    ("naf", "a"): "ʿ", ("mi", "rāj"): "ʿ", ("a", "rāḍīn"): "ʿ",                                          # nafʿa (ن-ف-ع), miʿrāj (م-ع-ر-ج), aʿrāḍīn (أعراض ʿayn)
    ("wajma", "u"): "ʿ", ("ṭ", "ṭāli"): "ʿ", ("al-han", "atun"): "ʿ", ("al-ba", "īd"): "ʿ",               # wajmaʿu (consigné), dup-safety
})
WORD_FINAL.update({
    "muqni": "ʿ", "muqin": "ʿ", "malṭa": "ʿ", "ṭāli": "ʿ", "ṭala": "ʿ", "ttabi": "ʿ", "tāsi": "ʿ",        # al-Muqniʿ (ق-ن-ع), Al-Muqinʿ, al-Malṭaʿ (ط-ل-ع), ṭāliʿ/aṭ-ṭāliʿ, ṭalaʿ, wa-ttabiʿ (ت-ب-ع), at-tāsiʿ
    "munṭaba": "ʿ", "sab": "ʿ", "jama": "ʿ", "bula": "ʿ", "subu": "ʿ", "tami": "ʿ", "mumti": "ʿ",        # (al-)munṭabaʿ (ط-ب-ع), sabʿ (سبع 7), jamaʿ (consigné), (al-)bulaʿ (ب-ل-ع mansion), subuʿ (consigné), (al-Muʾ)tamiʿ, (al-)Mumtiʿ (م-ت-ع)
    "munaqqa": "ʿ", "marji": "ʿ", "ka": "ʿ",                                                             # (al-)Munaqqaʿ (ن-ق-ع), marjiʿ (ر-ج-ع), ka-ʿadadi (ʿayn)
    "miqra": "ʾ", "maqri": "ʾ", "bda": "ʾ", "fay": "ʾ", "mabda": "ʾ", "nufay": "ʾ",                       # (Abū) Miqraʾ/Maqriʾ (ق-ر-ء — consigné), (wa-/fa-)bdaʾ (ب-د-أ), fayʾ (فيء), mabdaʾ (ب-د-أ), Nufayʾ (نفيء)
})
LONGVOWL_AYN = getattr(LONGVOWL_AYN, "add", None) and LONGVOWL_AYN or LONGVOWL_AYN
try:
    LONGVOWL_AYN.add("chu'-ā")   # chuʿāʿ شعاع : 2e ' final après ā = ʿayn (couvre la règle longue-voyelle)
except AttributeError:
    pass
'''
s = s.replace("# W22f — 2 derniers résidus :", PAIRS + "\n# W22f — 2 derniers résidus :")
compile(s, P, "exec")
open(P, "w", encoding="utf-8").write(s)
print("W23 carte insérée")
