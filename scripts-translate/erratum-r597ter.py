# -*- coding: utf-8 -*-
"""R597-ter — ERRATUM chirurgical sur la leçon livrée pdf-mut23h2q-131.
Défauts PROUVÉS réparés (rime + OCR ×2/×4 + glose imprimée + lecture image) :
 ḫafan→ḫafā (rime ʿurifā, OCR ×4) ; nasakh ʿillah/fa-ǧnaḫ lah (rime, lām-hāʾ
 imprimé, compZ-bayt, glose «il a penché vers sa parole») + FR retranche→incline
 (×2) ; muʿaḍḍal supprimé (tamhīd OCR ×2 = fard+muʿallal seuls ; leçon suivante
 = muḍṭarib p.104) ; natte→Ṣafiyya (×2) ; Suhayl/Wuhayb/ʿAwn/al-Kudrī ; ﷺ du
 Compagnon retiré (l’imprimé le porte après rasūl Allāh) ; riwāyatin (meta) ;
 divergence furridatuhu consignée. Zéro substitution non prouvée."""
import re
import sys

P = "/home/z/my-project/tr-tmp/lesson-ulumhadith1-pdf-mut23h2q-131-fr.html"
h = open(P, encoding="utf-8").read()
n0 = len(h)
applied = []


def rep(old, new, label, count=1):
    global h
    c = h.count(old)
    if c != count:
        print(f"!! {label}: {c} occurrence(s), attendu {count} — ABANDON")
        sys.exit(1)
    h = h.replace(old, new)
    applied.append(f"{label} ({count}x)")


def rex(pat, new, label, count=1):
    global h
    ms = list(re.finditer(pat, h))
    if len(ms) != count:
        print(f"!! {label}: {len(ms)} match(s), attendu {count} — ABANDON")
        sys.exit(1)
    h = re.sub(pat, new, h)
    applied.append(label)


# --- 1. ḫafan → ḫafā (vers ×3) ---
rep("aw ḫafan * * * muʿallalun ʿindahum qad ʿurifā",
    "aw ḫafā * * * muʿallalun ʿindahum qad ʿurifā",
    "ḫafan→ḫafā (vers)", 3)

# --- 1b. note meta ḫafan → erratum ---
rex(r"la forme imprimée «\u202f&nbsp;\s*aw ḫafan\s*&nbsp;\u202f» \(sans hamza, fathatan\) "
    r"est tenue telle quelle \(l’écart avec le canon «\u202f&nbsp;\s*aw ḫifāʾin\s*&nbsp;\u202f» "
    r"est documenté, jamais substitué\)",
    "la forme «\u202f&nbsp; aw ḫafā&nbsp;\u202f» fut révisée en erratum R597-ter : "
    "la lecture initiale «\u202f&nbsp; aw ḫafan&nbsp;\u202f» (fathatan supposé, sans hamza) "
    "est RÉCUSÉE — elle rompait la rime du bayt (ḫafā rime avec ʿurifā, comme "
    "thiqatin rime avec riwāyatin), et l’OCR tesseract ×4 passes (p99 bannière "
    "+ p101, psm 6+4) imprime ḫafā sans tanwīn",
    "note meta ḫafan → erratum")

# --- 1c. note inline §muʿallal ---
rex(r"\[la forme imprimée «\u202f&nbsp;\s*aw ḫafan\s*&nbsp;\u202f», sans hamza, "
    r"fut tranchée à l’image&nbsp;",
    "[erratum R597-ter : ḫafā — rime avec ʿurifā, OCR ×4 passes concordantes&nbsp;",
    "note inline ḫafan → erratum")

# --- 2. nasakh : vers + traductions + erratum ---
rep("wa-n-nasḫa sammā t-Tirmiḏī ʿillatan * * * fa-in yurd fī ʿamalin fa-ǧtuthhu",
    "wa-n-nasḫa sammā t-Tirmiḏī ʿillah * * * fa-in yurd fī ʿamalin fa-ǧnaḫ lah",
    "vers nasakh ʿillah/fa-ǧnaḫ lah")
rep("si donc cela est entendu de l’acte, retranche-le.",
    "si donc cela est entendu de l’acte, incline-toi vers lui.",
    "FR bayt retranche→incline")
rep("alors c’est un dire sain — retranche-le, c’est-à-dire",
    "alors c’est un dire sain — incline-toi vers lui, c’est-à-dire",
    "FR commentaire retranche→incline")
rex(r"la lecture OCR «\u202f&nbsp;\s*at-tasḫ\s*&nbsp;\u202f» est récusée\]",
    "la lecture OCR «\u202f&nbsp; at-tasḫ&nbsp;\u202f» est récusée&nbsp;\u202f; ERRATUM "
    "R597-ter : le second hémistiche «\u202f&nbsp; fa-ǧnaḫ lah&nbsp;\u202f» répare la "
    "lecture initiale «\u202f&nbsp; fa-ǧtuthhu&nbsp;\u202f» (rendue «\u202f&nbsp; "
    "retranche-le&nbsp;\u202f») — le lām-hāʾ final est imprimé (tesseract ×2 passes "
    "lisent fā-ǧtaḫ lah / fā-ǧtaḥ lah), la rime du bayt exige ʿillah/lah, la "
    "lecture image 1200 dpi (tr-tmp/qa-crops-r597/compZ-bayt-r597.png) donne "
    "«\u202f&nbsp; fa-ǧnaḫ lah&nbsp;\u202f», et la glose imprimée «\u202f&nbsp; il a penché "
    "vers sa parole&nbsp;\u202f» paraphrase ǧanaḫa — pencher vers —, jamais extirper]",
    "erratum nasakh documenté")

# --- 3. muʿaḍḍal : tamhīd + question + note meta ---
rep("la connaissance du ḥadīṯ fard, du ḥadīṯ muʿallal et du ḥadīṯ muʿaḍḍal&nbsp;",
    "la connaissance du ḥadīṯ fard et du ḥadīṯ muʿallal&nbsp;",
    "tamhīd sans muʿaḍḍal")
rep("chacun du ḥadīṯ fard, du ḥadīṯ muʿallal et du ḥadīṯ muʿaḍḍal&nbsp;\u202f?",
    "chacun du ḥadīṯ fard et du ḥadīṯ muʿallal&nbsp;\u202f?",
    "question sans muʿaḍḍal")
rex(r"le tamhīd imprime «\u202f&nbsp;\s*al-ḥadīṯ al-muʿaḍḍal\s*&nbsp;\u202f» aux côtés du "
    r"fard et du muʿallal dans ses DEUX phrases — tenu et annoncé \(le "
    r"muʿaḍḍal est la leçon suivante&nbsp;\u202f: bannière «\u202f&nbsp;\s*ad-dars 21\s*&nbsp;\u202f» "
    r"p\.104\)",
    "ERRATUM R597-ter : la lecture «\u202f&nbsp; al-ḥadīṯ al-muʿaḍḍal&nbsp;\u202f» du "
    "tamhīd est RÉCUSÉE — le tamhīd imprimé (OCR ×2 passes) porte al-ḥadīṯ "
    "al-fard et al-ḥadīṯ al-muʿallal seuls, à l’accord du titre de la leçon, "
    "des trois objectifs, du bayt «\u202f&nbsp; muʿallalun ʿindahum qad ʿurifā&nbsp;\u202f» "
    "et de la rubrique «\u202f&nbsp; ṯāniyan&nbsp;: al-ḥadīṯ al-muʿallal&nbsp;\u202f»&nbsp;\u202f; "
    "la leçon suivante est al-ḥadīṯ al-muḍṭarib (bannière «\u202f&nbsp; ad-dars 21&nbsp;\u202f» "
    "p.104, objectifs ×3 + bayt muḍṭaribun lus à l’OCR 300 dpi du cache "
    "p104-300.txt)",
    "note meta muʿaḍḍal → erratum")

# --- 4. natte → Ṣafiyya (×2) ---
rep("«\u202f&nbsp; on fit un repas de noces sur une natte avec de la bouillie "
    "grillée (sawīq) et des dattes",
    "«\u202f&nbsp; on fit un repas de noces pour Ṣafiyya avec de la bouillie "
    "grillée (sawīq) et des dattes",
    "natte→Ṣafiyya (1)")
rep("«\u202f&nbsp; on fit un repas de noces sur une natte avec de la bouillie "
    "grillée et des dattes",
    "«\u202f&nbsp; on fit un repas de noces pour Ṣafiyya avec de la bouillie "
    "grillée et des dattes",
    "natte→Ṣafiyya (2)")

# --- 5. noms propres ---
rep("Su\u1e25ayl", "Suhayl", "Suḥayl→Suhayl (ه = h, U+1E25 = ح)", 3)
rep("Wahb b. Ḫālid al-Bāhilī", "Wuhayb b. Ḫālid al-Bāhilī", "Wahb→Wuhayb")
rep("ʿŪn b. ʿAbd Allāh", "ʿAwn b. ʿAbd Allāh", "ʿŪn→ʿAwn")
rep("al-Kuḏrī", "al-Kudrī", "al-Kuḏrī→al-Kudrī", 2)

# --- 6. ﷺ réplacé : le glyphe suit rasūl Allāh, non le Compagnon ---
rep("al-Kudrī ﷺ [le glyphe ﷺ s’imprime après son nom — sic, tenu tel "
    "qu’imprimé]&nbsp;\u202f: ",
    "al-Kudrī&nbsp;\u202f: ",
    "ﷺ du Compagnon retiré")
rex(r"le ﷺ \(U\+FDFA\) après «\u202f&nbsp;\s*rasūl Allāh\s*&nbsp;\u202f» tenu, et le "
    r"glyphe ﷺ imprimé après «\u202f&nbsp;\s*Abī Saʿīd al-Kudrī\s*&nbsp;\u202f» \(sic — "
    r"la forme attendue pour un Compagnon serait «\u202f&nbsp;\s*que Dieu "
    r"l’agrée\s*&nbsp;\u202f»\) est rendu tel qu’imprimé, risque documenté, jamais corrigé",
    "le ﷺ (U+FDFA) après «\u202f&nbsp; rasūl Allāh&nbsp;\u202f» tenu (tesseract ×2 passes "
    "+ lecture image compZ-101)&nbsp;\u202f; ERRATUM R597-ter : la passe initiale "
    "plaçait un second ﷺ après le nom du Compagnon — RÉPARÉ, l’imprimé ne le "
    "porte point (la seule ligature suit rasūl Allāh, en sa place attendue)",
    "note meta ﷺ → erratum")

# --- 7. riwāya → riwāyatin (cohérence meta) ---
rep("aw ǧamʿin aw qaṣrin ʿalā riwāya&nbsp;",
    "aw ǧamʿin aw qaṣrin ʿalā riwāyatin&nbsp;",
    "riwāya→riwāyatin (meta)")

# --- 8. divergence furridatuhu consignée ---
rep("de la Manẓūma est documenté, jamais substitué),",
    "de la Manẓūma est documenté, jamais substitué&nbsp;\u202f; note R597-ter&nbsp;: "
    "la lecture de ce mot demeure divergente — cinq lectures image de la passe "
    "parallèle penchent vers le qāf à deux points (bannière OCR, VLM 2400 dpi "
    "bannière, composites ×3), deux vers le fāʾ à un point (VLM 2400 dpi "
    "corps, comptage de points), et tesseract se montre inconstant sur la "
    "paire fāʾ/qāf en cette police&nbsp;\u202f; la forme livrée est donc tenue, la "
    "divergence consignée — jamais tranchée sans preuve),",
    "divergence furridatuhu consignée")

open(P, "w", encoding="utf-8").write(h)
print(f"OK — {len(applied)} patchs appliqués ({n0} → {len(h)} car)")
for a in applied:
    print("  ✓", a)
