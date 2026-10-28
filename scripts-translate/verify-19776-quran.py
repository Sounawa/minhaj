# -*- coding: utf-8 -*-
"""R341 — Vérification coranique 19776 (fascule du rāʾ).
~28 fentes vides à restituer mot pour mot : taradaytum, mīraṯ, wa-raʿinā, firāšan,
aṣ-ṣirāṭa (muṭlaqan), i-krihihinna, a-rayta (ibdāl Warš), jamʿ muḏakkar sālim
(raḥimīn, rizqīn, raʿūna, ḫarrāṣūna, rakiʿūn), jamʿ muʾannaṯ sālim (mubašširāt,
ʿawrāt, mudabbirāt, ḥāsirāt ×2 Baqara+Fāṭir, ġāmirāt, nāširāt, ṯamarāt, ṣābirāt,
maqṣūrāt), alif muṯannā wusṭā (saḥirāni, ʾāḫarāni)."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

def bare(t):
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t).replace('\u0671', '\u0627')

def find(skel, limit=12):
    out = []
    for (sn, an, tx) in corpus:
        b = bare(tx)
        if skel in b:
            i = b.index(skel)
            out.append((sn, an, b[max(0, i-30):i+len(skel)+30]))
    return out[:limit]

def cps(sn, an):
    return data[str(sn)]["ar"][an-1][1]

QUERIES = [
    ("تَرَضَيْتُمْ (taradaytum)", "ترضيتم"),
    ("رضيتم variant", "رضيتم"),
    ("رضوا (racine رضو)", "رضوا"),
    ("تَرَضَّيْتُمْ (form V)", "ترضيتم".replace("رضي","رضّي")),
    ("مِيرَثُ (mīraṯ ḥaḏf)", "ميرث"),
    ("مِيرَاث (pleine)", "ميراث"),
    ("وَرَعِينَا (wa-raʿinā)", "ورعينا"),
    ("رَاعِينَا (pleine)", "راعينا"),
    ("فِرَاشًا (firāšan ḥaḏf)", "فرشا"),
    ("فِرَاشًا (pleine)", "فراشا"),
    ("أَفْرَاش (pluriel)", "افراش"),
    ("اَلصِّرَط (ḥaḏf)", "صرط"),
    ("صِرَاط (pleine — contrôle)", "صراط"),
    ("إِكْرَهِهِنَّ", "اكرههن"),
    ("إِكْرَه (racine)", "اكره"),
    ("أَكْرَه (hamza)", "أكره"),
    ("أَرَأَيْتَ (bare/sing.)", "ارايت"),
    ("أَرَأَيْتُمُ (pluriel)", "ارايتكم"),
    ("اَلرَّحِيمِينَ", "الرحيمين"),
    ("رَحِيمِينَ (nu)", "رحيمين"),
    ("رَزِقِينَ", "رزقين"),
    ("رَازِقِينَ (pleine)", "رازقين"),
    ("رَعُونَ", "رعون"),
    ("رَاعُونَ (pleine)", "راعون"),
    ("اَلْخَرَّصُونَ", "الخرصون"),
    ("خَرَّاصُونَ (pleine)", "خراصون"),
    ("وَرَكِعُونَ", "وركعون"),
    ("رَاكِعُونَ (pleine)", "راكعون"),
    ("الرَّاكِعِينَ", "الراكعين"),
    ("مُبَشِّرَاتٍ", "مبشرات"),
    ("مُبَشِّرَتٍ (ḥaḏf)", "مبشرت"),
    ("عَوْرَاتٍ", "عورات"),
    ("عَوْرَتٍ (ḥaḏf)", "عورت"),
    ("مُدَبِّرَاتٍ", "مدبرات"),
    ("مُدَبِّرَتٍ (ḥaḏf)", "مدبرت"),
    ("حَاسِرَاتٍ", "حاسرات"),
    ("حَاسِرَتٍ (ḥaḏf)", "حاسرت"),
    ("حَسَرَتٍ (sans lettre)", "حسرت"),
    ("غَامِرَاتٍ", "غامرات"),
    ("غَامِرَتٍ (ḥaḏf)", "غامرت"),
    ("غَمَرَتٍ (sans lettre)", "غمرت"),
    ("نَاشِرَاتٍ", "ناشرات"),
    ("النَّاشِرَاتِ", "الناشرات"),
    ("النَّشَرَتِ (ḥaḏf)", "النشرت"),
    ("نَشَرَتٍ (sans lettre)", "نشرت"),
    ("ثَمَرَاتٍ", "ثمرات"),
    ("الثَّمَرَاتِ", "الثمرات"),
    ("الثَّمَرَتِ (ḥaḏf)", "الثمرت"),
    ("ثَمَرَتٍ (sans lettre)", "ثمرت"),
    ("صَابِرَاتٍ", "صابرت"),
    ("الصَّابِرَاتِ", "الصابرت"),
    ("الصَّبِرَتِ (ḥaḏf)", "الصبرت"),
    ("صَبِرَتٍ (sans lettre)", "صبرت"),
    ("مَقْصُورَاتٍ", "مقصورت"),
    ("مَقْصُورَتٌ (ḥaḏf)", "مقصورت"),
    ("سَحِرَانِ / سَحَرَانِ", "سحران"),
    ("سَحِرَنِ (ḥaḏf)", "سحرن"),
    ("سَاحِرَانِ (pleine)", "ساحران"),
    ("آخَرَانِ", "آخران"),
    ("أَخَرَنِ (ḥaḏf)", "اخرن"),
    ("ءَاخَرَنِ", "ءاخرن"),
    ("آخَرَانِ (alef pleine)", "اخران"),
]
for label, skel in QUERIES:
    res = find(skel)
    print(f"== {label} : {len(res)}")
    for (sn, an, ctx) in res[:8]:
        print(f"   {sn}:{an}  …{ctx}…")

print("\n########## CPS COMPLETS DES VERSETS PIVOTS ##########")
pivots = [
    (3,180), (57,10), (2,104), (78,38), (24,58), (35,8),
]
for (sn, an) in pivots:
    print(f"--- FULL {sn}:{an}")
    print(cps(sn, an))
