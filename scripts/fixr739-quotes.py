# -*- coding: utf-8 -*-
"""R739 — remplace les guillemets droits internes (imbriqués) par des guillemets
courbes « anglais » (U+201C/U+201D) dans scripts/comm-r739.py : les chaines
Python du fichier sont delimitées par des guillemets droits, et les citations
imbriquées rompent la chaine. Application exacte des motifs, puis recompilation."""
import re

F = 'scripts/comm-r739.py'
src = open(F, encoding='utf-8').read()

mots = [
    ('"Donne-la-moi en cadeau"', '“Donne-la-moi en cadeau”'),
    ('"Par bonne grâce"', '“Par bonne grâce”'),
    ('"dot"', '“dot”'),
    ('"Je me marie à toi sans dot"', '“Je me marie à toi sans dot”'),
    ('"je te vends mon vêtement contre un dīnār"', '“je te vends mon vêtement contre un dīnār”'),
    ('"Après toi, il ne sera permis à personne d\'avoir une dot."', '“Après toi, il ne sera permis à personne d\'avoir une dot.”'),
    ('"comment prendriez-vous cet engagement, alors que vous avez déjà goûté l\'un de l\'autre et qu\'elles ont obtenu de vous un engagement ferme ?"',
     '“comment prendriez-vous cet engagement, alors que vous avez déjà goûté l\'un de l\'autre et qu\'elles ont obtenu de vous un engagement ferme ?”'),
    ('"à elle sa condition, et les musulmans sont à leurs conditions."', '“à elle sa condition, et les musulmans sont à leurs conditions.”'),
    ('"et cohabitez avec elles selon la bienséance"', '“et cohabitez avec elles selon la bienséance”'),
    ('"goût"', '“goût”'),
    # écritures lʿidda / dʿasal → avec apostrophe (normalisée ensuite par norme_fr)
    ('lʿidda', "l'ʿidda"),
    ('dʿasal', "d'ʿasal"),
]

appliques = 0
for old, new in mots:
    n = src.count(old)
    appliques += n
    src = src.replace(old, new)
    print(f'{n} × {old[:40]}')

open(F, 'w', encoding='utf-8').write(src)
print('remplacements totaux :', appliques)
compile(src, F, 'exec')
print('compilation : OK')
