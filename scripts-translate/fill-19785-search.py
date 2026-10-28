# -*- coding: utf-8 -*-
"""R342 — Recherche des fentes vides de 19785 (chapitre du rāʾ, تتمة — suite).
Restitution mot pour mot, ancrage cps, contre-vérification aux boundaries (règles ca).
Vedettes : 12 jamʿ muʾannaṯ sālim + 2 jamʿ muḏakkar + 2 duel + 2 aʿǧamī
         + 2 ḥaḏf ʾišāra + 4 maḥḏūf muṭlaqan + classe al-murawwada + 4 exemples Dānī."""
import json, re

CACHE = "/home/z/my-project/scripts-translate/quran-cache.json"
data = json.load(open(CACHE))
corpus = [(int(k), a[0], a[1]) for k in sorted(data, key=int) for a in data[k]["ar"]]

def bare(t):
    return re.sub(r'[\u064B-\u065F\u0670\u06D6-\u06ED\u0640\u0610-\u061A]', '', t).replace('\u0671', '\u0627')

def find(skel, limit=14, boundary=False):
    out = []
    for (sn, an, tx) in corpus:
        b = bare(tx)
        start = 0
        while True:
            i = b.find(skel, start)
            if i < 0:
                break
            okb = True
            if boundary:
                okb = (i == 0 or b[i-1] == ' ') and (i+len(skel) == len(b) or b[i+len(skel)] == ' ')
            if okb:
                out.append((sn, an, b[max(0, i-28):i+len(skel)+28]))
            start = i + 1
    return out[:limit]

QUERIES = [
    # ——— أ. jamʿ muʾannaṯ sālim (12 vedettes) ———
    ("a1 ad-dakirat (الذكرت)", "الذكرت", False),
    ("a1b dakarat (ذكرت)", "ذكرت", False),
    ("a1c pleine (ذاكرت)", "ذاكرت", False),
    ("a2 al-mu'sirat (المعصرت)", "المعصرت", False),
    ("a2b mu'sirat (معصرت)", "معصرت", False),
    ("a2c pleine (معاصرت)", "معاصرت", False),
    ("a3 magarat (مغرت)", "مغرت", False),
    ("a3b pleine (مغارات)", "مغارات", False),
    ("a3c sing غار", "غار", True),
    ("a4 az-zajrat (الزجرت)", "الزجرت", False),
    ("a4b pleine (زاجرت)", "زاجرت", False),
    ("a5 muhajrat (مهجرت)", "مهجرت", False),
    ("a5b pleine (مهاجرت)", "مهاجرت", False),
    ("a5c masc (المهاجرين)", "المهاجرين", False),
    ("a6 al-khayrat (الخيرت)", "الخيرت", False),
    ("a6b pleine (خيرات)", "خيرات", False),
    ("a7 marrat (مرت MOT)", "مرت", True),
    ("a7b pleine (مرات MOT)", "مرات", True),
    ("a8 musakhkharat (مسخرت)", "مسخرت", False),
    ("a8b sing (مسخرة)", "مسخرة", False),
    ("a9 al-hujrat (الحجرت)", "الحجرت", False),
    ("a10 qasirat (قصرت)", "قصرت", False),
    ("a10b pleine (قاصرت)", "قاصرت", False),
    ("a11 baqarat (بقرت)", "بقرت", False),
    ("a11b collective (البقر MOT)", "البقر", True),
    ("a12 mutajawirat (متجورت)", "متجورت", False),
    ("a12b pleine (متجاورت)", "متجاورت", False),
    # ——— ب. jamʿ muḏakkar sālim (2) ———
    ("b1 ar-rashidun (الرشدون)", "الرشدون", False),
    ("b1b pleine (الرشيدون)", "الرشيدون", False),
    ("b2 ar-rasikhun (الرسخون)", "الرسخون", False),
    ("b2b racine (رسخ)", "رسخ", False),
    # ——— ت. المثنى (2) ———
    ("t1 tantasira (تنتصرن)", "تنتصرن", False),
    ("t1b intasara (انتصر)", "انتصر", False),
    ("t1c yantasirun (ينتصرون)", "ينتصرون", False),
    ("t2 al-bahran (البحرن)", "البحرن", False),
    ("t2b pleine-y (البحرين)", "البحرين", False),
    ("t2c pleine-a (البحران)", "البحران", False),
    ("t2d mot (بحرين)", "بحرين", True),
    # ——— ث. أسماء أعجمية (2) ———
    ("j1 'Imran (عمرن)", "عمرن", False),
    ("j1b pleine (عمران MOT)", "عمران", True),
    ("j2 Ibrahim (إبرهم)", "إبرهم", False),
    ("j2b var (أبرهم)", "أبرهم", False),
    ("j2c pleine (إبرهيم)", "إبرهيم", False),
    # ——— ثانيا: ḥaḏf ʾišāra (2) ———
    ("i1 wa-harman (وحرم MOT)", "وحرم", True),
    ("i1b pleine (حرام)", "حرام", False),
    ("i2 sirajan (سرج)", "سرج", False),
    ("i2b pleine (سراج)", "سراج", False),
    # ——— ثالثا: maḥḏūf muṭlaqan (4) ———
    ("m1 murghaman (مرغم)", "مرغم", False),
    ("m1b racine (رغم)", "رغم", False),
    ("m2 tardaw (ترضوا)", "ترضوا", False),
    ("m2b sans-alif (ترضو MOT)", "ترضو", True),
    ("m3 corpus hamzé (ارأيتم)", "ارأيتم", False),
    ("m3b avec-k (ارأيتكم)", "ارأيتكم", False),
    ("m3c waršien (أريتم)", "أريتم", False),
    ("m4 darahima (درهم)", "درهم", False),
    ("m4b pleine (دراهم)", "دراهم", False),
    # ——— classe al-murawwada (راد/يرود — rasm r-w-d) ———
    ("w1 rawadat (رودت)", "رودت", False),
    ("w1b pleine (روادت)", "روادت", False),
    ("w1c rawaduhu (رودوه)", "رودوه", False),
    ("w1d pleine (روادوه)", "روادوه", False),
    ("w2 yarudu (يرود)", "يرود", False),
    ("w3 arada MOT (اراد)", "اراد", True),
    ("w4 yuridu (يريد)", "يريد", False),
    ("w5 radu (رضو MOT)", "رضو", True),
    # ——— Istitimār Dānī : 4 alif maḥḏūfa nommés ———
    ("s1 ula'ika (اولئك)", "اولئك", False),
    ("s2 al-mala'ika (الملئكة)", "الملئكة", False),
    ("s3 ya-ayyuha (يايها)", "يايها", False),
    ("s4 ha'ula' (هؤلاء)", "هؤلاء", False),
]

for label, skel, strict in QUERIES:
    hits = find(skel, limit=14, boundary=strict)
    print(f"== {label} : {len(hits)}")
    for (sn, an, ctx) in hits[:8]:
        print(f"   {sn}:{an}  …{ctx}…")
print("########## CPS COMPLETS DES VERSETS PIVOTS ##########")
for (sn, an) in [(33,35),(3,41),(78,14),(37,1),(37,2),(37,3),(9,57),(60,10),(55,70),
                 (16,12),(49,4),(37,48),(38,52),(2,67),(2,68),(2,69),(2,70),(2,71),
                 (13,4),(3,7),(4,162),(2,157),(35,12),(25,53),(55,19),(55,20),(18,60),
                 (42,39),(3,33),(3,35),(66,12),(21,95),(25,61),(71,16),(78,13),(9,96),
                 (10,50),(10,59),(35,40),(12,20),(12,23),(12,32),(54,37),(23,61),(21,90),(3,114)]:
    try:
        tx = data[str(sn)]["ar"][an-1][1]
        b = bare(tx)
        print(f"--- FULL {sn}:{an}")
        print(b)
    except Exception as e:
        print(f"--- {sn}:{an} ERR {e}")
