# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-29 (leçon 28, le mérite du
jeûne ; statut du jeûne du vendredi et des six jours de šawwāl, p.192-198) :
sept crochets numérotés du Muwaṭṭaʾ tranchés à la couche + adjudication
visuelle des recadrages 600-2 400 dpi (862 ʿĀʾiša ; 864 Abū az-Zinād ;
887 six jours ; 887 vendredi ; 865 Ramadan ; 863 ǧunnat ; 866 siwāk),
AUCUNE citation coranique (cache non sollicité), matns clés, écarts
déclarés, page 198 blanche, garde-doublon, machine rétablie.
Usage: python3 scripts-translate/verify-hadith2-pdf29.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-29-fr.html"
ok, fail = 0, 0


def chk(label, cond):
    global ok, fail
    if cond:
        ok += 1
        print(f"PASS — {label}")
    else:
        fail += 1
        print(f"FAIL — {label}")


t = open(HTML, encoding="utf-8").read()
raw = t  # copie brute pour les contrôles typographiques finaux
t = t.replace("\u202f", " ")  # normalisation NNBSP pour les assertions de contenu

# --- structure générale ---
chk("h1 porte le titleFr du registre", "Le mérite du jeûne ; statut du jeûne du vendredi et des six jours de šawwāl" in t)
chk("h1 porte la série et la leçon 28", "leçon 28" in t)
chk("badge leçon 29 / 31 déclaré", "Leçon 29 / 31" in t)
chk("bornes p.192 à 198 déclarées", "pages 192 à 198" in t)
chk("source manuel miroir citée", "hadith-2-iadadi_text.pdf" in t)
chk("quadruple preuve des bornes documentée", "quadruple preuve de contenu" in t)
chk("page 198 blanche documentée", "page de clôture BLANCHE" in t)
chk("annexe p.199 (fihrist) citée comme borne haute", "fihrist al-aʿlām" in t or "fihrist al-aʿlām" in t.lower())
chk("carte hadith2-map.py conforme citée", "hadith2-map.py" in t)
chk("tail R572 cité comme autorité", "tail R572" in t)

# --- garde-doublon ---
chk("titleFr registre htmlFr 0 car consigné", "htmlFr 0 car" in t)
chk("registre savant pdf-29 absent consigné", "registre savant hand+llm pdf-29 absent" in t)
chk("contrôle positif pdf-28 consigné", "contrôle positif pdf-28 présent" in t)

# --- les sept crochets Muwaṭṭaʾ ---
chk("crochet 862 (ʿĀʾiša) présent", "al-Muwaṭṭaʾ n° 862" in t)
chk("crochet 864 (Abū az-Zinād) présent", "al-Muwaṭṭaʾ n° 864" in t)
chk("crochet 887 six jours présent", "n° 887 — numéro tranché au recadrage 900 dpi et à la couche texte convergents." in t)
chk("crochet 887 vendredi (double) déclaré", "le crochet « 887 » se répète" in t)
chk("crochet 865 (Ramadan) présent", "al-Muwaṭṭaʾ n° 865" in t)
chk("couche « 65 » tronquée documentée", "un « 65 » tronqué" in t)
chk("crochet 863 (ǧunnat) présent", "al-Muwaṭṭaʾ n° 863" in t)
chk("crochet 866 (siwāk) présent", "al-Muwaṭṭaʾ n° 866" in t)
chk("sept crochets annoncés à l’apparat", "SEPT crochets du Muwaṭṭaʾ" in t)

# --- matns clés (translittérations) ---
chk("matn 862 « yaṣūmu ḥattā naqūlu lā yufṭiru »", "yaṣūmu ḥattā naqūlu lā yufṭiru" in t)
chk("matn 862 « istakmala ṣiyāma šahrin qaṭṭ »", "istakmala ṣiyāma šahrin qaṭṭ" in t)
chk("matn 862 « ʾakṯara ṣiyāman minhū fī Šaʿbān »", "ʾakṯara ṣiyāman minhū fī Šaʿbān" in t)
chk("matn 864 « la-ḫulūfu fami ṣ-ṣāʾimi »", "la-ḫulūfu fami ṣ-ṣāʾimi ʾaṭyabu ʿinda llāhi min rīḥi l-misk" in t)
chk("matn 864 « fa-ṣ-ṣiyāmu lī wa-ʾanā ʾaǧzī bih »", "fa-ṣ-ṣiyāmu lī wa-ʾanā ʾaǧzī bih" in t)
chk("matn 864 « kullu ḥasanatin bi-ʿašarati ʾamṯālihā »", "kullu ḥasanatin bi-ʿašarati ʾamṯālihā" in t)
chk("matn 887 « yaṣūmahā » (six jours)", "yaṣūmahā" in t)
chk("matn 887 « bidʿatahū »", "bidʿatahū" in t)
chk("matn 887 vendredi « yanhai ʿan ṣiyāmi yawmi l-ǧumuʿa »", "yanhai ʿan ṣiyāmi yawmi l-ǧumuʿa" in t)
chk("matn 887 vendredi « wa-ṣiyāmih ḥasan »", "wa-ṣiyāmih ḥasan" in t)
chk("matn 865 « fu-ttiḥat ʾabwābu l-ǧann »", "fu-ttiḥat ʾabwābu l-ǧann" in t)
chk("matn 865 « wa-ṣuffidati š-šayāṭīn »", "wa-ṣuffidati š-šayāṭīn" in t)
chk("matn 863 « aṣ-ṣiyāmu ǧunnat »", "aṣ-ṣiyāmu ǧunnat" in t)
chk("matn 863 « fa-lā yarfuṯ, wa-lā yaǧhal »", "fa-lā yarfuṯ, wa-lā yaǧhal" in t)
chk("matn 863 « ʾinnī ṣāʾim, ʾinnī ṣāʾim »", "ʾinnī ṣāʾim, ʾinnī ṣāʾim" in t)
chk("matn 866 « lā yakrahūna s-siwāka liṣ-ṣāʾimi fī Ramaḍān »", "lā yakrahūna s-siwāka liṣ-ṣāʾimi fī Ramaḍān" in t)
chk("matn 866 « lā fī ʾawwalihī wa-lā fī ʾāḫirih »", "lā fī ʾawwalihī wa-lā fī ʾāḫirih" in t)
chk("hadith Ibn Masʿūd « wa-lam raʾaytuhū yufṭiru yawma l-ǧumuʿa »", "wa-lam raʾaytuhū yufṭiru yawma l-ǧumuʿa" in t)
chk("hadith Ṣaḥīḥayn « yawman ʾaw baʿdah »", "yawman ʾaw baʿdah" in t)
chk("citation az-Zarqānī « ḫayru ḫaṣāli ṣ-ṣāʾimi s-siwāk »", "ḫayru ḫaṣāli ṣ-ṣāʾimi s-siwāk" in t)
chk("citation az-Zayn b. al-Munayyir « t-tašrīf wa-t-taʿẓīm »", "t-tašrīf wa-t-taʿẓīm" in t)

# --- aucune citation coranique ---
chk("AUCUNE citation coranique déclarée", "AUCUNE citation coranique" in t)
chk("cache quran-cache non sollicité documenté", "quran-cache.json n’ayant pas été sollicité" in t)

# --- écarts déclarés ---
chk("écart yanhai/yadaʿu déclaré", "contre \"yadaʿu\" du texte canonique" in t)
chk("double 887 déclaré", "le double imprimé consigné tel quel" in t)
chk("écart bi-ʿašarati/bi-ʿašri déclaré", "contre \"bi-ʿašri\" d’autres impressions" in t)
chk("écart fa-ʾin ʾamarra déclaré", "« fa-ʾin ʾamarra ? qātilahū, ʾaw šāhidahū » du hadith 863" in t)
chk("écart wa-lam raʾaytuhū déclaré", "contre « wa-lammā raʾaytuhū » attendu" in t)
chk("écart muʾaqqat déclaré", "graphie imprimée \"muʾaqqat\"" in t)
chk("écart min sāʿāti n-nahār déclaré", "contre « fī sāʿatin mina n-nahār » du texte canonique" in t)
chk("mot katḫama non identifié déclaré", "non identifié dans les lexiques courants" in t)
chk("glose rīḥa/rāḥa tranchée déclarée", "tranchée \"rīḥa\" par le sens" in t)
chk("marfūʿan des Ṣaḥīḥ porté", "(marfūʿan)" in t)

# --- sections du fascicule ---
chk("objectifs de la leçon", "Les objectifs de la leçon" in t)
chk("tamhīd", "Le tamhīd" in t)
chk("quatre textes du cours", t.count("<h3>Le ") >= 4)
chk("traduction du rapporteur al-Aʿraǧ", "siqqat tarǧamatuh" in t)
chk("définitions qasam bi-llāh", "qasam bi-llāh" in t)
chk("définition al-ḫilāf (haleine)", "li-ḫalāʾi l-maʿida mina ṭ-ṭaʿām" in t)
chk("extraction des contenus (3 items)", "J’en extrais la méthode de jeûne" in t)
chk("analyse première : jeûne en dehors de Ramaḍān", "Le jeûne du Prophète ﷺ en dehors de Ramaḍān" in t)
chk("analyse 2-a : haleine du jeûneur", "Sa satisfaction à son égard et Son éloge" in t)
chk("analyse 2-b : az-Zayn b. al-Munayyir", "Az-Zayn b. al-Munayyir" in t)
chk("analyse 2-c : au-delà des sept cents fois", "au-delà des sept cents fois" in t)
chk("analyse deuxième : mérite de Ramaḍān", "Le mérite du mois de Ramaḍān" in t)
chk("commentaire maṣfūd/maġlūl al-yad", "maġlūlu l-yadi ʾilā l-ʿanq" in t)
chk("analyse troisième : vendredi", "Le jeûne du jour de vendredi" in t)
chk("analyse six jours de Šawwāl", "Le jeûne des six jours de Šawwāl" in t)
chk("fala karāha fīh (licence des six jours)", "falā karāha fīh" in t)
chk("évaluation (2 questions)", "Comment était le jeûne du Prophète ﷺ" in t)
chk("exploitation siwāk", "le statut du siwāk du jeûneur" in t)
chk("sources bracketées 2/244", "2/244" in t)
chk("as-Sunan al-kubrā an-Nasāʾī cité", "as-Sunan al-kubrā d’an-Nasāʾī" in t)
chk("as-Sunan al-kubrā al-Bayhaqī cité", "al-Bayhaqī" in t)

# --- chaîne de production ---
chk("trace du tick consignée", "1a1a172f41684dc9-cron-agent-loop-202611050249" in t)
chk("claim 18:56:21Z consigné", "18 :56 :21Z" in t)
chk("forensic reset consigné", "AUCUN reset destructeur" in t)
chk("machine rétablie (833 paquets) consignée", "833 paquets" in t)
chk("bundle de sûreté consigné", "minhaj-r572-securite.bdl" in t)
chk("méthode couche 6 431 car consignée", "couche texte 6 431 car" in t)
chk("51 recadrages en 10 composites consignés", "51 recadrages d’adjudication en 10 composites" in t)
chk("aucune lecture devinée", "aucune lecture devinée" in t)

# --- typographie (mêmes règles que qa-lesson) ---
AR = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]")
residus = [c for c in raw if AR.match(c) and ord(c) != 0xFDFA]
chk(f"0 arabe résiduel (hors ﷺ) — trouvé {len(residus)}", len(residus) == 0)
chk("guillemets appariés", raw.count("«") == raw.count("»"))
chk("0 apostrophe droite", "'" not in raw)
chk("ﷺ présent (convention corpus)", "\uFDFA" in raw)

print(f"\n{'=' * 60}")
print(f"verify-hadith2-pdf29 : {ok} PASS / {fail} FAIL")
raise SystemExit(1 if fail else 0)
