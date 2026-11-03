#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Vérification de la leçon hadith2-pdf-8 (leçon 7, صلاة الخوف والكسوف
والخسوف, p.53-59) : contrôle de contenu, numéros du Muwaṭṭaʾ tranchés par
preuve image (506/509 contre couches 605/905 — mécanique d'inversion totale
R535-R540), bornes p.53-59 à triple convergence (objectifs p.53, إعداد p.59,
STARTS l7=53/l8=60 carte R534), citations coraniques portées telles
qu'imprimées (écarts d'impression déclarés, aucun rendu du cache coranique),
lexies tranchées 400-600 dpi (fa-amāda contre couches aṭāla, wa-ibṭāli contre
wa-iṭāli), fragments non élucidés déclarés, dates ʿĀʾiša tranchées (57/58
contre couches 75/85).
Usage: python3 scripts-translate/verify-hadith2-pdf8.py
"""
import re

HTML = "/home/z/my-project/tr-tmp/lesson-hadith2-pdf-8-fr.html"

ok, fail = 0, 0
def chk(label, cond):
    global ok, fail
    if cond: ok += 1
    else:
        fail += 1
        print(f"ÉCHEC: {label}")

html = open(HTML, encoding="utf-8").read()
text = re.sub(r"<[^>]+>", " ", html).replace("\u202f", " ").replace("\u00a0", " ")

# 0 arabe (ﷺ U+FDFA exempté par convention corpus)
arab = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDF9\uFDFB-\uFDFF\uFE70-\uFEFF]", text)
arab = [c for c in arab if c != "\ufdfa"]
chk("0 caractère arabe au corps", len(arab) == 0)

# structure générale
chk("h1 leçon 7", "leçon 7" in html and "<h1>" in html)
chk("lesson-meta présent", 'class="lesson-meta"' in html and "Source du cours" in html)
chk("bornes pages 53 à 59", "pages 53 à 59" in html)
chk("slot pdf-8 déclaré", "pdf-8" in html)
chk("badge portail Leçon 8 / 31", "Leçon 8 / 31" in text)
chk("titre portail prière du danger", "La prière du danger" in text)
chk("matière déclarée R540 renvoyée", "R540" in text)
chk("carte STARTS R534 renvoyée", "R534" in text)
chk("claim R541 consigné", "R541" in text)
chk("STARTS l7=53 l8=60 déclarés", "l7 = 53" in text and "l8 = 60" in text)
chk("trois objectifs", "trois objectifs" in text)

# numéros du Muwaṭṭaʾ — imprimés tranchés par preuve image
for n in ["506", "509"]:
    chk(f"imprimé n° {n} présent", f"n° {n}" in text)
for n in ["605", "905"]:
    chk(f"couche « {n} » déclarée", re.search(rf"«\s*{n}\s*»", text) is not None)
chk("inversion totale déclarée", "inversion totale" in text)
chk("mécanique R535-R540 déclarée", "R535-R540" in text)
chk("preuve image déclarée", "preuve image" in text)

# les deux textes du cours
chk("premier texte", "premier texte" in text)
chk("deuxième texte", "deuxième texte" in text)
chk("isnād 1 : Yaḥyā b. Saʿīd", "Yaḥyā b. Saʿīd" in text)
chk("isnād 1 : al-Qāsim b. Muḥammad", "al-Qāsim b. Muḥammad" in text)
chk("isnād 1 : Ṣāliḥ b. Khawwāt", "Ṣāliḥ b. Khawwāt al-Anṣārī" in text)
chk("isnād 1 : Sahl b. Abī Ḥathama", "Sahl b. Abī Ḥathama al-Anṣārī" in text)
chk("matn 1 : deux ṭāʾifa", "une ṭāʾifa de ses compagnons" in text and "face à l’ennemi" in text)
chk("matn 1 : lexie bi-t-ṯalāṯīna déclarée", "bi-t-ṯalāṯīna" in text and "jamais reconstituée" in text)
chk("isnād 2 : Hišām b. ʿUrwa", "Hišām b. ʿUrwa" in text)
chk("isnād 2 : d’après son père", "d’après son père" in text)
chk("matn 2 : rang serré bil-qās", "en rang serré" in text)
chk("matn 2 : soleil s’éclipsa", "le soleil s’éclipsa au temps du Messager" in text)
chk("matn 2 : deux āyāt", "deux āyāt des āyāt de Dieu" in text)
chk("matn 2 : ni mort ni vie", "ni pour la mort de quelqu’un ni pour sa vie" in text)
chk("matn 2 : invoquez-magnifiez-aumône", "invoquez Dieu, magnifiez-Le et donnez l’aumône" in text)
chk("matn 2 : Ô communauté de Muḥammad", "Ô communauté de Muḥammad" in text)
chk("matn 2 : jalousie de Dieu", "nul n’est plus jaloux que Dieu" in text)
chk("matn 2 : ririez peu pleureriez beaucoup", "vous ririez peu et vous pleureriez beaucoup" in text)
chk("matn 2 : élévations longues", "demeura long dans la station" in text and "demeura long dans l’inclinaison" in text)
chk("matn 2 : lexie fa-amāda tranchée", "fa-amāda" in text and "aṭāla" in text)
chk("matn 2 : prêcha aux gens", "prêcha aux gens, loua Dieu et Le glorifia" in text)

# transmetteuse ʿĀʾiša
chk("ʿĀʾiša mère des croyants", "mère des croyants" in text)
chk("fille d’Abū Bakr aṣ-Ṣiddīq", "fille d’Abū Bakr aṣ-Ṣiddīq" in text)
chk("Taymiyya Qurayšite", "Taymiyya" in text and "Qurayšite" in text)
chk("citation d’ʿUrwa", "ʿUrwa dit" in text and "plus savante en fiqh et en poésie" in text)
chk("dates imprimées 57 ou 58", "l’an 57 ou 58 de l’hégire" in text)
chk("couches 75/85 déclarées", "« 75 »" in text and "« 85 »" in text)

# āyāt — AUCUN rendu du cache, écarts d'impression déclarés
chk("renvoi al-Isrāʾ āya 59", "sūrat al-Isrāʾ, āya 59" in text)
chk("écart tamhīd déclaré", "wa-mā arsalnā" in text and "jamais tranché" in text)
chk("āya demeurée au renvoi", "demeurée au renvoi" in text)
chk("couches 95 déclarées (paire inversée)", "« 95 »" in text)
chk("citation an-Nisāʾ 101-102", "sūrat an-Nisāʾ, āyāt 101-102" in text)
chk("citation : quand tu es parmi eux", "quand tu es parmi eux" in text)
chk("citation : se dresse avec toi", "qu’un groupe d’entre eux se dresse avec toi" in text)
chk("citation : emportant vos armes", "emportant vos armes" in text)
chk("citation : derrière vous", "qu’ils soient derrière vous" in text)
chk("citation : autre groupe vienne", "qu’un autre groupe vienne, qui n’a pas encore prié" in text)
chk("citation : précaution et armes", "prenant leur précaution et leurs armes" in text)
chk("écart aṣ-ṣalāta déclaré", "aṣ-ṣalāta" in text and "ṣalātan" in text)
chk("écart wa-asliḥatahum déclaré", "wa-asliḥatahum" in text and "wa-asliḥatakum" in text)
chk("aucun rendu du cache déclaré (citation)", "aucun rendu du cache coranique" in text)

# corps : khawf
chk("corps Premièrement", "Premièrement" in text)
chk("division en deux ṭāʾifa", "l’imām divise l’armée en deux ṭāʾifa" in text)
chk("thunāʾiyya : ṣubḥ et voyage", "double (ṯunāʾiyya)" in text and "aṣ-ṣubḥ et la prière en voyage" in text)
chk("une seule rakʿa / deux rakʿa", "une seule rakʿa" in text and "deux rakʿa" in text)
chk("afḏāḏan", "afḏāḏan" in text)
chk("imām debout invoquant ou silencieux", "invoquant ou silencieux" in text)
chk("seconde ṭāʾifa retourne à la garde", "retourne à la garde" in text)
chk("maġrib clause", "de même la prière du maġrib" in text)
chk("corps Deuxièmement", "Deuxièmement" in text)
chk("jugement : sunna en tout combat", "sunna prescrite en tout combat régulier" in text)
chk("qiṭāl mašrūʿ", "qiṭāl mašrūʿ" in text)
chk("résidence ou voyage", "en résidence ou en voyage" in text)

# corps : kasūf
chk("kasūf définition", "le retrait de la lumière du soleil ou son amoindrissement" in text)
chk("lune entre terre et soleil", "la lune se trouve entre la terre et le soleil" in text)
chk("sunna homme ou femme", "homme ou femme, fût-elle en voyage" in text)
chk("wa-law musāfira déclarée", "wa-law musāfira" in text)
chk("Fātiḥa et sūra longue", "la Fātiḥa du Livre et une sūra longue" in text)
chk("capacité des gens", "tenant compte de la capacité des gens" in text)
chk("rukuʿ à la mesure de la récitation", "à la mesure de ce dont il a prolongé la récitation" in text)
chk("sūra moindre que la première", "moindre que la première" in text)
chk("sujūd comme le sujūd habituel", "comme le sujūd habituel" in text)
chk("deux inclinaisons", "avec deux inclinaisons" in text)
chk("première sunna seconde obligation", "la première sunna et la seconde obligation" in text)
chk("ne se répète point", "ne se répète point" in text)
chk("invocation et évocation", "ils se contentent plutôt de l’invocation et de l’évocation" in text)
chk("tamāḍā : poursuivent et n’interrompent point", "les gens la poursuivent et ne l’interrompent point" in text)

# corps : khutba
chk("sermon après la prière", "après la prière, que l’imām se tourne vers les gens" in text)
chk("loue Dieu glorifie", "il loue Dieu, Le glorifie, prie et salue le Messager de Dieu" in text)
chk("takbīr invocation aumône", "le takbīr, l’invocation et l’aumône" in text)
chk("exhorte et effraie", "il les exhorte et les effraie" in text)
chk("défend toute infamie", "il leur défend toute infamie, de la fornication et de la turpitude" in text)
chk("rappel jour de la Résurrection", "leur rappelle le jour de la Résurrection" in text)
chk("délices châtiment du feu asile de la tombe", "de délices, du châtiment du feu et de la recherche d’asile contre le châtiment de la tombe" in text)

# corps : khusūf
chk("khusūf définition", "le retrait de la lumière de la lune ou son amoindrissement" in text)
chk("signe cosmique", "ce signe cosmique" in text)
chk("maisons plutôt que mosquées", "dans les maisons plutôt que dans les mosquées" in text)
chk("peine de sortir de nuit", "la peine de sortir vers elles de nuit" in text)
chk("deux rakʿa comme les surérogatoires", "comme le reste des prières surérogatoires" in text)
chk("individuellement", "la priant individuellement" in text)
chk("répéter jusqu’à la lune se manifeste", "jusqu’à ce que la lune se manifeste" in text)
chk("récitation à voix haute", "la récitation y est à voix haute" in text)

# hikma
chk("ǧāhiliyya vénéraient", "vénéraient le soleil et la lune" in text)
chk("deux āyāt créées", "deux āyāt créées par Dieu" in text)
chk("amoindrissement comme les semblables", "l’amoindrissement et le changement surviennent sur elles" in text)
chk("compassion et crainte", "compassion pour sa communauté et de crainte intense de son Seigneur" in text)
chk("ibṭāl : mise à néant", "la mise à néant de ce que la ǧāhiliyya croyait" in text)
chk("mort ou dommage", "mort ou dommage" in text)

# définitions
chk("waǧāt al-ʿadūw", "Waǧāt al-ʿadūw" in text and "vis-à-vis de l’ennemi" in text)
chk("muqābil al-ʿadūw", "muqābil al-ʿadūw" in text)
chk("taǧallat aš-šams", "Taǧallat aš-šams" in text and "sa lumière est revenue" in text)
chk("āyatāni deux indices", "deux indices attestant l’unicité de Dieu exalté et l’immensité de Sa puissance" in text)

# extraction / évaluation / exploration / préparation
chk("extraction 2 contenus", "J’expose le jugement de la prière de la peur et sa description" in text)
chk("évaluation : description choisie", "la description choisie dans la prière de la peur" in text)
chk("évaluation : différence kasūf/ḫusūf", "la différence entre l’éclipse de soleil et l’éclipse de lune" in text)
chk("évaluation : description kusūf et khusūf", "la description de la prière de l’éclipse de soleil et de l’éclipse de lune" in text)
chk("exploration Abū Hurayra", "D’après Abū Hurayra" in text)
chk("exploration Ḏiǧnān ʿUsfān", "Ḏiǧnān et ʿUsfān" in text)
chk("exploration cernant les associateurs", "cernant les associateurs" in text)
chk("exploration plus chère que leurs enfants", "plus chère que leurs enfants et leurs jeunes filles" in text)
chk("exploration joignez votre commandement", "joignez votre commandement" in text)
chk("exploration Gabriel", "Gabriel — sur lui le salut — vint et lui ordonna de diviser ses compagnons en deux moitiés" in text)
chk("exploration Sunan an-Nasāʾī", "Sunan an-Nasāʾī, livre de la prière de la peur" in text)
chk("préparation : istasqā ridāʾ banūʾ", "istasqā" in text and "ridāʾ" in text and "banūʾ" in text)
chk("préparation : bienséances istisqāʾ", "les bienséances de la prière de la demande de pluie (al-istisqāʾ)" in text)
chk("leçon suivante page 60", "la page 60 ouvre la leçon suivante" in text)
chk("triple convergence", "triple convergence du sondage" in text)
chk("jamais devinée", "jamais devinée" in text)

# fragments déclarés
chk("fragments non élucidés déclarés", "non élucidés" in text)
chk("tels qu’imprimés déclarés", "tels qu’imprimés" in text)

print(f"\nVÉRIFICATION : {ok} contrôles OK, {fail} échec(s)")
raise SystemExit(1 if fail else 0)
