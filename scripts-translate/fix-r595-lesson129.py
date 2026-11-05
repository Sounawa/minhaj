#!/usr/bin/env python3
"""R595 — corrections post-QA lesson-129 : hémistiche, bandeaux tamhīd/matn/fahm, titre aš-šarḥ."""
G = "\u202f"
NB = "\u00a0"
P = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-129-fr.html"

h = open(P, encoding="utf-8").read()

def guil(s):
    return f"«{G}&nbsp; {s}&nbsp;{G}»"

# 1. faute : hémistique -> hémistiche
h = h.replace("hémistique", "hémistiche")

# 2. dd : liste bandeaux + titre texte aš-šarḥ
old = guil("at-taḥlīl") + ", " + guil("at-taqwīm") + ", " + guil("al-istiṯmār") + ", " + guil("al-iʿdād al-qablī") + ", la citation"
new = (guil("at-tamhīd") + ", " + guil("al-matn") + ", " + guil("al-fahm") + ", "
       + guil("at-taḥlīl") + ", " + guil("at-taqwīm") + ", " + guil("al-istiṯmār") + ", "
       + guil("al-iʿdād al-qablī") + " et le titre texte " + guil("aš-šarḥ") + ", la citation")
assert old in h, "ancre bandeaux introuvable"
h = h.replace(old, new)

# 3. glose : mention bandeau al-fahm + titre aš-šarḥ
old2 = "(al-ǧamāʿa min an-nās), et elle est"
new2 = ("(al-ǧamāʿa min an-nās) [le bandeau " + guil("al-fahm")
        + " précède la section, muet pour tesseract, adjudiqué à l’image à 600 dpi"
        + NB + G + "; le titre " + guil("aš-šarḥ") + NB + G + ":" + NB + G
        + "’" + "s’imprime en rouge au-dessous".replace("’", "’") + "]".replace("]", "]"),)
new2 = ("(al-ǧamāʿa min an-nās) [le bandeau " + guil("al-fahm")
        + " précède la section, muet pour tesseract, adjudiqué à l’image à 600 dpi"
        + NB + G + "; le titre " + guil("aš-šarḥ") + NB + G + ":" + NB + G
        + " s’imprime en rouge au-dessous], et elle est")
assert old2 in h, "ancre glose introuvable"
h = h.replace(old2, new2)

open(P, "w", encoding="utf-8").write(h)
print("corrections appliquées")
