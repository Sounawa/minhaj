# -*- coding: utf-8 -*-
"""R670 — corrections du HTML 402 : guillemet, kataba (r669-f), épithètes 1270, cas 2 taqwīm, ahdāf, apparat."""
import re

P = "/home/z/my-project/tr-tmp/lesson-hadith3-pdf-mut23h2x-402-fr.html"
t = open(P, encoding="utf-8").read()
n0 = len(t)

def rep(old, new, label):
    global t
    if old in t:
        t = t.replace(old, new, 1)
        print(f"OK   {label}")
    else:
        print(f"MISS {label}")

# 1) guillemet double en trop (fin du matn 1188)
rep("»\u202f» (Muwaṭṭaʾ n° 1188)", "» (Muwaṭṭaʾ n° 1188)", "guillemet 1188")
rep("&nbsp;»&nbsp;» (Muwaṭṭaʾ n° 1188)", "&nbsp;» (Muwaṭṭaʾ n° 1188)", "guillemet 1188 (variante)")

# 2) kataba (lecture r669-f)
rep("“J’étais auprès d’al-Malik b. Marwān [le texte imprimé porte «&nbsp;ilā&nbsp;»], de al-Ḥaǧǧāǧ b. Yūsuf&nbsp;: qu’on ne contredise pas",
    "“ʿAbd al-Malik b. Marwān écrivit (kataba) à al-Ḥaǧǧāǧ b. Yūsuf&nbsp;: qu’on ne contredise pas", "kataba (r669-f)")
rep("[le texte imprimé porte «&nbsp;ilā&nbsp;»], de al-Ḥaǧǧāǧ b. Yūsuf",
    "[lecture d’image r669-f tranchant «&nbsp;kataba&nbsp;»&nbsp;; la couche OCR portait «&nbsp;kuntu ʿinda&nbsp;» suivi de «&nbsp;ilā&nbsp;» — récusation documentée], de al-Ḥaǧǧāǧ b. Yūsuf", "note kataba")

# 3) titre exploitation + h1
rep("l’encadré n° 1270 — ce qui n’est pas vu le jour de ʿArafa",
    "l’encadré n° 1270 — la petitesse du diable le jour de ʿArafa", "h2 exploitation")
rep("l’exploitation par l’encadré n° 1270 (ce qui n’est pas vu le jour de ʿArafa — la descente de la miséricorde et le pardon de Dieu sur les péchés majeurs&nbsp;; la question de Badr&nbsp;: il a vu Jibrīl [forme imprimée hésitante] les anges)",
    "l’exploitation par l’encadré n° 1270 (la petitesse du diable le jour de ʿArafa — quatre épithètes imprimées&nbsp;; la descente de la miséricorde et le pardon de Dieu sur les péchés majeurs&nbsp;; la question de Badr&nbsp;: il a vu Jibrīl rangeant les anges)", "h1 exploitation")

# 4) encadré 1270 : quatre épithètes (r669-f)
rep("d’après Karīz&nbsp;: le Messager de Dieu (que la paix soit sur lui) a dit&nbsp;: “[début imprimé dégradé, non restituable] le jour de ʿArafa — cela n’a eu lieu que par ce qu’il a vu",
    "d’après [chaîne imprimée partiellement dégradée — croppée]&nbsp;: [le diable, le jour de ʿArafa, est] plus petit (aṣġara), plus repoussé (adḥara), plus méprisable (aḥqara) et plus irrité (aġyaẓa) qu’en tout autre jour [les quatre épithètes imprimées tranchées sur image&nbsp;; les couches OCR portaient «&nbsp;akhfar&nbsp;»/«&nbsp;aʿghiẓ&nbsp;», récusées]&nbsp;; cela n’a lieu que par ce qu’il voit", "épithètes 1270")
rep("“il a vu Jibrīl [«&nbsp;yazʿu&nbsp;» — forme imprimée hésitante rendue telle quelle, croppée] les anges.”",
    "“il a vu Jibrīl rangeant les anges (yazaʿu l-malāʾika) [forme imprimée «&nbsp;yazʿu&nbsp;», croppée].”", "Jibrīl yazaʿu")
rep("le sens imprimé du fil du commentaire fait apparaître le mérite du jour de ʿArafa&nbsp;: la descente de la miséricorde et le pardon des péchés majeurs",
    "le mérite du jour de ʿArafa apparaît ainsi&nbsp;: la petitesse du diable (ṣiġār aš-šayṭān), la descente de la miséricorde et le pardon des péchés majeurs", "mérite 1270")

# 5) taqwīm : second cas (r669-e)
rep("<li>explique le jugement de la question suivante, avec preuve et motivation&nbsp;: un homme a stationné à ʿArafa sans être en état de pureté (ġayr ṭāhir).</li>",
    "<li>explique le jugement des deux cas suivants, avec preuve et motivation&nbsp;: un homme a stationné à ʿArafa puis s’en est retourné vers al-Muzdalifa avant le coucher du soleil [second cas récupéré sur l’image, couche R669 r669-e]&nbsp;; et un homme a stationné à ʿArafa sans être en état de pureté (ġayr ṭāhir).</li>", "taqwīm cas 2")

# 6) ahtāf → ahdāf (orthographe)
t = t.replace("ahtāf", "ahdāf")
print("OK   ahtāf→ahdāf (tous)")

# 7) apparat : audit + couche R669 + garde-doublon
rep("machine&nbsp;: sandbox recyclée une sixième fois pendant le tour",
    "audit de la passe&nbsp;: trace 1a1c23c49937a9b9 — tick 04h56 (+08:00), job 499559, ouvrier D puis continuation ouvrière A (05h37, job 496554) — aucun reset destructif&nbsp;; machine&nbsp;: sandbox recyclée une sixième fois pendant le tour", "apparat audit")
rep("ZÉRO āya rendue hors cache coranique&nbsp;: la matière imprimée de la leçon ne contient aucun verset — la section «&nbsp;Les versets&nbsp;» du gabarit est omise, aucune substitution au cache n’a été nécessaire&nbsp;;",
    "couche d’adjudication R669 régénérée par la session jumelle du même fil (tr-tmp/qa-crops-r669/)&nbsp;: trois adjudications majeures adoptées et documentées — «&nbsp;kataba&nbsp;» p.91 (r669-f), les quatre épithètes du diable p.95 (r669-f), le second cas d’évaluation p.95 (r669-e)&nbsp;; GARDE-DOUBLON&nbsp;: une variante de session est possible sur ce slot (précédent R668-bis) — le registre fait foi&nbsp;; ZÉRO citation coranique rendue hors cache&nbsp;: la matière imprimée de la leçon ne contient aucun verset — la section «&nbsp;Les versets&nbsp;» du gabarit est omise, aucun recours au cache n’a été nécessaire&nbsp;;", "apparat R669 + garde-doublon")

open(P, "w", encoding="utf-8").write(t)
print(f"taille {n0} → {len(t)}")
