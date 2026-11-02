#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Carte leçons↔pages du manuel miroir Tafsīr 3 ثانوي (al-Kahf) + extraction.

ÉTABLI R487 : le manuel complet (224 p., collection archive.org
1_20220304_20220304_2251, couche texte OCR en ordre visuel inversé mot à mot —
le mot الكهف arrive « فهكلا ») porte les leçons de sūrat al-Kahf, même mécanique
que isra-map.py (R458). Source tranchée par la GRILLE DU LIVRE (pdfUrl des
slots pdf-mut23h3c-739+ = dossier التفسير-الثالثة-ثانوي du portail) et par le
contenu : la préface p.5 porte « دروس في تفسير سورة الكهف », la grille de
compétences p.8 « تحصيل معاني سورة الكهف ».

SONDAGE R487 : p.5-8 = préface + compétences ; p.9 = fihris du livre ; la leçon 1
(Kahf v1-5, slot pdf-mut23h3c-739) commence p.10 (objectifs « أن أتعرف سورة
الكهف وفضلها وسبب نزولها ») et s'achève p.16 ; la leçon 2 (v6-9) ouvre p.17
(objectifs « مناظر النبي ﷺ » sondés R487) et s'achève p.22 (استثمار + invocations,
sondés R488) ; la leçon 3 ouvre p.23.

SONDAGE R491 : en-têtes imprimés du livre TRANCHÉS PAR LE CONTENU (précédent de
la leçon 28 d'Isrāʾ, jamais deviné) : p.23 porte « أهداف الدرس (الكهف: الآيات
10-14) » — la leçon 3 couvre donc les āyāt 10 à 14 (contre (10-12) à la grille
du portail, divergence documentée) et s'achève avant p.29 ; p.29 porte « أهداف
الدرس (الكهف: الآيات 15-16) » — la leçon 4 couvre les āyāt 15 à 16 (contre
(13-16) à la grille du portail, divergence documentée) et ouvre p.29 ; sa borne
supérieure à trancher par sondage à l'armement de la leçon 4.

SONDAGE R492 : p.37 porte « أهداف الدرس » — la leçon 5 ouvre p.37, la leçon 4
s'achève donc p.36 ; p.44 porte « أهداف الدرس » — la leçon 6 ouvre p.44, la
leçon 5 s'achève p.43 (p.44 sondant « مشهد استغراب أصحاب الكهف بعد اليقظة »,
conforme à la grille v19-20). Bornes 5+ restant à trancher à chaque armement.

SONDAGE R497 : p.50 porte « أهداف الدرس » — la leçon 7 ouvre p.50, la leçon 6
couvre donc p.44-49 (p.44 NUM « 91-02 » = āyāt 19-20, convergence avec la
grille ; p.51 NUM « 12-42 » = āyāt 21-24, conforme à la grille de la leçon 7).

Usage :
  python3 scripts-translate/kahf-map.py            # imprime la carte
  python3 scripts-translate/kahf-map.py 1          # extrait la leçon 1 (p.10-16)
"""
import sys

import fitz

PDF = "/home/z/my-project/content/textbooks-src/tafsir-3-thanawi_text.pdf"

# Vrais départs (fixes) : leçon i = pages STARTS[i] .. STARTS[i+1]-1
# p5-9 = matière liminaire (préface, compétences, fihris) — la leçon 1 RÉELLE
# commence p10 ; leçon 2 ouvre p17 (objectifs sondés R487).
STARTS = [10, 17, 23, 29, 37, 44, 50, 58, 65, 73, 79, 87, 96, 102, 110, 118, 125,
          132, 142, 150, 157, 165, 171, 179, 188, 195]
# +96 : borne leçon 13 tranchée par sondage R511 (kahf-probe-l12.py + rendu
# image p87 « (الآيات: 36-43) » badge 12 et p96 « (الآيات: 44-45) » badge 13)
# — la leçon 12 couvre p.87-95, JAMAIS devinée.
# +102 : borne leçon 14 tranchée par sondage R512 (kahf-probe-l13.py, texte
# brut : « أهداف الدرس » p.102 — objectifs « مشاهد القيامة / إحصاء الأعمال /
# يوم العرض » conformes au slot -752 v46-48) — la leçon 13 couvre p.96-101.
# +110 : borne leçon 15 tranchée par sondage R512 (sonde textuelle p.105-113 :
# « أهداف الدرس » p.110) — la leçon 14 couvre p.102-109.
# +118 : borne leçon 15 tranchée par sondage R514 (kahf-probe-l15.py :
# « أهداف الدرس » p.118, badge « (الكهف: 55-35…) » inversé = (الكهف: 53-55)
# imprimé = cache 54-56, objectifs « الأمثال / إرسال الرسل / الجدال بالباطل »
# conformes) — la leçon 15 couvre p.110-117, JAMAIS devinée.
# +125 : borne leçon 17 tranchée par sondage R514 (sonde textuelle p.122-128 :
# p.124 porte l'إعداد القبلي de la leçon 16, NUM inversé « 85-65 » = (56-58)
# imprimé = cache 57-59 versets de la leçon 17 ; p.125 ouvre « أهداف الدرس »
# objectifs « صفات الكافرين المعرضين / سعة رحمة الله في تأخير العقوبة »
# conformes au slot -755) — la leçon 16 couvre p.118-124, JAMAIS devinée.
# +132 : borne leçon 18 tranchée par sondage R515 (kahf-probe-l18.py, texte
# brut : p.132 porte « أهداف الدرس (الكهف: الآيات 59-64) » — objectifs « تفاصيل
# قصة موسى والعبد الصالح / أهمية الرحلة في طلب العلم وآدابها » conformes au
# slot -756 ; p.133 commentaire de v60 cache « و موسى وهو موسى بن عمران » ;
# badge p.132 conforme à la grille v59-64 imprimé = cache 60-65, moins un
# depuis leçon 12, et à la continuité v58→v59) — la leçon 17 couvre p.125-131,
# JAMAIS devinée.
# +142 : borne leçon 19 tranchée par sondage R517 (kahf-probe-l19.py + rendu
# image relu p.141-143, texte brut : p.142 porte « سورة الكهف (الآيات: 65-72) »
# (couche texte « 65 - 295 », fin corrompue, début « 65 » propre) + « أهداف
# الدرس » — objectifs « قواعد الصحبة وآداب التعلم خلال قصة موسى والخضر »
# conformes au slot -757 ; l'iʿdād qiblī de p.141 porte le NUM « أرجع تفسير
# الآيات: 65 – 72 من سورة الكهف » (couche texte « 5 - 72 », le « 6 » perdu,
# relu sur image zoomée) ; p.143 cite « [الكهف: 65 _ 72] » (couche texte
# « 65 172 », tiret lu « 1 ») ; p.146 tafsir clos sur « لا تواخذني » = imprimé
# 72 = cache 73, et p.150 ouvre أهداف الدرس (leçon 20, intro citant le refus
# du poisson puis le سكّت de la navire) — CONVERGENCE QUADRUPLE badge p.142 +
# iʿdād qiblī p.141 + citation p.143 + contenu, la grille VERSE_RANGE[19]
# « v65-72 » CONFIRMÉE PAR SONDAGE (imprimé 65-72 = cache 66-73, décalage +1
# tranché R511), JAMAIS devinée — la leçon 18 couvre p.132-141, la leçon 19
# couvre p.142-149.
# +150 : borne leçon 20 tranchée par sondage R519 (kahf-probe-l19b.py texte
# brut + rendus image 10× relu par vision : p.150 porte « أهداف الدرس » avec
# badge « 20 » et NUM relu sur crops zoomés « (٧٣-٧٧) » = (73-77) imprimé =
# cache 74-78, conforme à la grille VERSE_RANGE[20] et à la continuité imprimé
# 72→73 ; objectifs « فعلان آخران للخضر : قتل الغلام و إقامة الجدار » conformes
# au contenu des āyāt 74-78 ; p.149 porte l'إعداد القبلي de la leçon 20
# (« أرجع تفسير الآيات » NUM « 7 » dégradé) — CONVERGENCE QUADRUPLE, la leçon 19
# couvre p.142-149, JAMAIS devinée.
# +157 : borne leçon 20 tranchée par sondage R520 (kahf-probe-l20.py texte
# brut : p.156 porte l'إعداد القبلي de la leçon 21 NUM « أرجع تفسير الآيات
# من 78 - 81 » (imprimé 78-81 = cache 79-82, conforme à la grille VERSE_RANGE[21])
# et p.157 ouvre « أهداف الدرس » — objectifs « تأويل أفعال الخضر والحكمة منها /
# رفعت الله عباده المؤمنين وحفظهم / التزام أوامر الله » conformes aux āyāt
# 78-81 (meurtre du garçon, mur et trésor) ; p.151 cite « [الكهف: 73 _ 77] »
# confirmant la plage de la leçon 20 imprimée 73-77 = cache 74-78 — CONVERGENCE
# DOUBLE إعداد+أهداف+NUM, la leçon 20 couvre p.150-156, JAMAIS devinée.
# +165 : borne leçon 21 tranchée par sondage R521 (kahf-probe-l21.py + rendus
# image relus par vision : p.164 porte l'إعداد القبلي de la leçon 22 relu sur
# image « أرجع تفسير الآيات من 82 - 84 من سورة الكهف » (couche texte propre
# « 82 - 84 », chiffres latins intacts) et p.165 ouvre « أهداف الدرس » avec
# badge relu sur image « سورة الكهف الآيات: ٨٢ – ٨٤ » (couche texte « 89 -
# 64 », corruption des chiffres arabes-indiens ٨٢-٨٤) — objectifs « قصة ذي
# القرنين من خلال آيات القرآن الكريم / ما أعطاه الله لذي القرنين من الملك
# والوسع / قيمة العدل أساس ملك ذي القرنين » conformes au contenu des āyāt
# imprimées 82-84 = cache 83-85 (ويسألونك عن ذي القرنين…) ; p.165 cite «
# [الكهف: 82 _ 84] » et p.171 ouvre أهداف الدرس de la leçon 23 badge « (الكهف:
# الآيات 85-91) » (couche « 55 - 91 », le 8 lu « 5 », corruption connue
# +157) ; départ confirmé : badge p.157 relu sur image « سورة الكهف (الآيات:
# ٧٨ – ٨١) ٢١ » — CONVERGENCE QUINTUPLE badge p.157 + iʿdād qiblī p.164 +
# badge p.165 + citation p.165 + objectifs leçon 23 p.171, la grille
# VERSE_RANGE[22] « v82-84 » CONFIRMÉE PAR SONDAGE (imprimé 82-84 = cache
# 83-85, décalage +1 tranché R511), JAMAIS devinée — la leçon 21 couvre
# p.157-164, la leçon 22 couvre p.165-170.
# +171 : borne leçon 22 tranchée par sondage R522 (kahf-probe-l22.py texte
# brut p.158-180 + badges relus sur rendus image 3,2× par la présente passe :
# p.165 badge relu « سورة الكهف : الآيات 82 – 84 » badge 22 (converge avec la
# sonde indépendante du R521 — même borne +165) et p.171 badge relu « سورة
# الكهف (الآيات) : 85 – 91 » badge 23, objectifs « تفاصيل أخرى من قصة ذي
# القرنين / أهمية الصالح والإصلاح في الأرض » conformes aux āyāt 85-91 (les
# deux levers et le milieu, le peuple de Gog-Magog à venir) — CONVERGENCE
# badge p.165 + badge p.171 + objectifs p.165 et p.171, la grille
# VERSE_RANGE[23] « v85-91 » CONFIRMÉE PAR SONDAGE (imprimé 85-91 = cache
# 86-92), JAMAIS devinée — la leçon 22 couvre p.165-170.
# +179 et +188 : bornes leçons 24-25 tranchées par sondage R523
# (kahf-probe-l24.py texte brut + rendus image 200 dpi relu par vision, slot
# 762) : p.178 porte l'iʿdād qiblī de la leçon 24 relu sur image « أرجع تفسير
# الآيات من 92 - 97 من سورة الكهف وأجب عن... » (couche texte « 97 ل نع », fin
# de ligne, le NUM 92-97 relu sur crop) et p.179 ouvre « أهداف الدرس » avec
# badge relu sur image « 24 — سورة الكهف (الآيات: 92 - 97) » — objectifs
# « عمل ذي القرنين لبناء الردم / أهمية التعاون واكتمال الجهد / العمل الصالح
# وتجنب الإفساد » et تمهيد « وصول ذي القرنين إلى القوم الذين دون السدين,
# فساد يأجوج ومأجوج, طلب الردم » conformes au contenu des āyāt imprimées
# 92-97 = cache 93-98 (بين السدين، زبر الحديد، دكاء) ; p.180-186 commentaire
# (زبر الحديد/نحاس, أفرغ عليه قطرا, فما استطاعوا أن يظهره, دكاء, ينفقون) ;
# ANOMALIE DOCUMENTÉE : la boîte des āyāt de p.179 porte en coquille du livre
# un fragment de sūrat an-Nabāʾ (ألم نجعل الأرض مهادا... وجعلنا سراجا وهاجا)
# avec cercles 92/93/94 CORRECTS pour la numérotation imprimée — coquille du
# muṣḥaf crop, les cercles confirmant la plage imprimée 92-97 ; p.187 porte
# l'iʿdād qiblī de la leçon 25 NUM relu sur image « أرجع تفسير الآيات من 98 -
# 101 » et p.188 ouvre « أهداف الدرس » avec badge relu sur image « 25 — سورة
# الكهف (الآيات: 98 - 101) », boîte clôturée par « [الكهف: 98 - 101] » imprimé,
# objectifs « جزاء المستهزئين بآيات الله / الإخلاص و الرياء » conformes au
# cache 99-102 (جهنم العرض، الأخسرين أعمالا) — CONVERGENCE QUADRUPLE badge
# p.179 + iʿdād p.178 + objectifs/تمهيد + commentaire, la grille
# VERSE_RANGE[24] « v92-97 » CONFIRMÉE PAR SONDAGE (imprimé 92-97 = cache
# 93-98, décalage +1 tranché R511), JAMAIS devinée — la leçon 23 couvre
# p.171-178, la leçon 24 couvre p.179-187, la leçon 25 ouvre p.188.
# +195 : borne leçon 25 tranchée par sondage R526 (kahf-probe-l25.py texte
# brut + rendus image 150/300/500 dpi relus par vision, slot 763) :
# p.194 porte l'iʿdād qiblī de la leçon 26 NUM relu sur image « راجع تفسير
# الآيات من 102 - 105 » (couche texte miroir « 201 - 501 » = 102-105 inversés)
# et p.195 ouvre « أهداف الدرس » avec badge relu sur image « سورة الكهف
# (الآيات: 102 – 105) » (couche texte « 109 - 105 », le ٠٢ lu « ٩ », corruption
# connue) — objectifs « جزاء الذي أعدّه الله لأولياء المؤمنين / الاستعداد
# للقاء الله / سعة كلمات الله في المثل » et تمهيد « أمران موجّهان للنبي :
# الأول بكلمات الله والثاني بالرسول ومهمته، لتختم السورة » conformes aux āyāt
# imprimées 102-105 = cache 106-110 (الجزاء جهنم/الفردوس، البحر مداد، قل إنما
# أنا بشر) ; p.194 استثمار clôturant la leçon 25 (Jundub + حديث لا ينفع عمل)
# — CONVERGENCE QUADRUPLE badge p.188 + iʿdād p.194 + badge p.195 + contenu,
# la grille VERSE_RANGE[25] « v98-101 » CONFIRMÉE PAR SONDAGE, JAMAIS
# devinée — la leçon 25 couvre p.188-194, la leçon 26 ouvre p.195.
# DÉCOUVERTE DE DÉCALAGE (R526, slot 763) : la boîte des āyāt de p.188 (lue
# sur crops 300/500 dpi) OUvre sur « أَفَحَسِبَ الَّذِينَ كَفَرُوا... إِنَّا
# أَعْتَدْنَا » sous médaillon (98) = cache 102, et le commentaire p.189-193
# glose EXCLUSIVEMENT les āyāt cache 102 (قراءات أفحسب/عبادي/نُزُلًا p.190),
# 103 (قل هل ننبئكم بالأخسرين p.190-191), 104 (ضل سعيهم... يحسبون p.191), 105
# (أولئك الذين كفروا... فلا نقيم لهم وزنا + حديث البخاري باب « أولئك الذين »
# p.191-193) — AUCUNE glose des cache 100-101 dans la leçon 25 : le décalage
# imprimé→cache passe donc de +2 (fin de la leçon 24, R523) à +4 (médaillon
# (98) = cache 102) — la leçon 25 rend la cache 102-105 aux numéros imprimés
# (98)-(101) ; les āyāt cache 100-101 (عرضنا جهنم / غطاء عن ذكري) sont
# réunies par la numérotation warš dans la zone de la leçon 24 (gloses
# « يومئذ/عرضنا جهنم » p.185-186 documentées R523, réservées puis couvertes
# par le numéro (97) de la leçon 24) — aucun vide ni doublon, fendo warš
# déclaré. NB au prochain ouvrier du slot 764 (leçon 26) : le décalage +4
# tient-il sur toute la zone (102)-(105) = cache 106-109, ou croît-il encore
# (le تمهيد de p.195 mentionne le البحر مدادا des كلمات = cache 109 ET
# « والثاني بالرسول ومهمته » = cache 110 : la (105) pourrait réunir 109+110) — à
# trancher PAR LE CONTENU, jamais deviné.
# bornes des annexes (à trancher par sondage quand la leçon 26 sera atteinte)
ACTIVITES = None   # slot 765
FIHRIS = None      # slot 766
SOURCES = None     # slot 767
# NB R526 : après la leçon 26 (p.195-200, dernière leçon du tafsīr), les
# p.201+ portent التقويم النهائي / أنشطة إثرائية / المعجم / المصادر (annexes
# slots 765-767) — bornes à trancher par sondage quand leurs slots seront
# revendiqués.

# slots tafsir-5ep dans l'ordre (739..764 = leçons 1..26, 765 activités,
# 766 fihris, 767 sources)
SLOTS = {i: 738 + i for i in range(1, 27)}   # leçon i -> docId slot
VERSE_RANGE = {
    1: "v1-5", 2: "v6-9", 3: "v10-14", 4: "v15-16", 5: "v17-18", 6: "v19-20",
    7: "v21-24", 8: "v25-27", 9: "v28-29", 10: "v30-31", 11: "v32-35",
    12: "v36-43", 13: "v44-45", 14: "v46-48", 15: "v49-52", 16: "v53-55",
    17: "v56-58", 18: "v59-64", 19: "v65-72", 20: "v73-77", 21: "v78-81",
    22: "v82-84", 23: "v85-91", 24: "v92-97", 25: "v98-101", 26: "v102-105",
}
# R491 : plages 3-4 tranchées par les en-têtes imprimés du livre (p.23 : 10-14 ;
# p.29 : 15-16) — la grille du portail (10-12 / 13-16) diverge, documenté ; les
# plages 5+ restent celles de la grille, à trancher par sondage à chaque armement.
# R492 : départs sondés p.37 (leçon 5) et p.44 (leçon 6) — en-têtes أهداف الدرس.
# R497 : départ de la leçon 7 sondé p.50 — la leçon 6 couvre p.44-49 (v19-20).
# R500ter/R508 : départs sondés p.58 (leçon 8), p.65 (leçon 9), p.73 (leçon 10) —
# NUM p.66 «92-82» inversé = 28-29 ; R509 : borne de la leçon 10 tranchée p.78
# (الإعداد القبلي NUM «23-53» inversé = 32-35) — la leçon 11 ouvre p.79
# (أهداف الدرس sondé, NUM p.79).
# R509bis : borne de la leçon 11 tranchée — l'إعداد القبلي de p.86 porte NUM
# «34-63» inversé = 36-43 (verses de la leçon 12) et les objectifs de la
# leçon 12 ouvrent p.87 (أهداف الدرس, p.87 citant « (الكهف: 36-43) » p.88) —
# la leçon 11 couvre donc p.79-86, jamais devinée.


def fix_line(s: str) -> str:
    return " ".join(w[::-1] for w in s.split())


def extract(lesson: int) -> dict:
    doc = fitz.open(PDF)
    lo = STARTS[lesson - 1]
    hi = STARTS[lesson] - 1 if lesson < len(STARTS) else None
    if hi is None:
        raise SystemExit("STARTS incomplets : borne supérieure de la leçon "
                         f"{lesson} à trancher par sondage avant extraction")
    pages = {}
    for p in range(lo, hi + 1):
        raw = doc[p - 1].get_text()
        pages[p] = {"raw": raw, "fixed": "\n".join(fix_line(l) for l in raw.split("\n"))}
    return {"lesson": lesson, "slot": f"pdf-mut23h3c-{SLOTS[lesson]}",
            "verses": VERSE_RANGE[lesson], "pages": (lo, hi), "content": pages}


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        n = int(sys.argv[1])
        d = extract(n)
        print(f"KAHF LEÇON {n} — slot {d['slot']} — {d['verses']} — pages {d['pages'][0]}-{d['pages'][1]}")
        print("=" * 70)
        for p in range(d["pages"][0], d["pages"][1] + 1):
            print(f"\n===== PAGE {p} (décodé) =====")
            print(d["content"][p]["fixed"])
    else:
        print("CARTE KAHF — 26 leçons + annexes (manuel miroir 3 ثانوي, 224 p.)")
        for i in range(1, 27):
            if i - 1 >= len(STARTS):
                print(f"  leçon {i:2d} | slot pdf-mut23h3c-{SLOTS[i]} | {VERSE_RANGE[i]:8s} | start à trancher")
                continue
            hi = STARTS[i] - 1 if i < len(STARTS) else None
            rng = f"p{STARTS[i-1]}-{hi}" if hi else f"p{STARTS[i-1]}-?"
            print(f"  leçon {i:2d} | slot pdf-mut23h3c-{SLOTS[i]} | {VERSE_RANGE[i]:8s} | {rng}")
        print("  annexes | slots 765 activités / 766 fihris / 767 sources — bornes à trancher")


if __name__ == "__main__":
    main()
