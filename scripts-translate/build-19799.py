# -*- coding: utf-8 -*-
"""R344 — assemblage 19799 : concatène les fragments FR en tr-tmp/19799.html."""
import re
parts = []
for i in (1, 2, 3):
    with open(f"/home/z/my-project/tr-tmp/fr19799_{i}.html", encoding="utf-8") as fh:
        parts.append(fh.read().strip())
full = "\n".join(parts) + "\n"
with open("/home/z/my-project/tr-tmp/19799.html", "w", encoding="utf-8") as fh:
    fh.write(full)
n_o, n_c = full.count("«"), full.count("»")
arabic = re.findall(r'[\u0600-\u06FF]', full)
droite = full.count("'")
nnbsp = full.count('\u202f')
print(f"longueur: {len(full)} | guillemets: {n_o}/{n_c} {'OK' if n_o==n_c else 'ERREUR'} | arabe: {len(arabic)} | apostrophe droite: {droite} | nnbsp: {nnbsp} | h1: {len(re.findall(chr(60)+'h1', full))} | h2: {len(re.findall(chr(60)+'h2', full))} | h3: {len(re.findall(chr(60)+'h3', full))} | tables: {len(re.findall(chr(60)+'table', full))}")
N = '\u202f'
probes = [
    # structure
    "Le rasm et le ḍabṭ"+N+": le chapitre du zāy",
    "Leçon 21 / 30",
    "ad-dars at-tāsiʿ ʿašar",
    "dix-neuvième leçon",
    "Notes du traducteur",
    "Kašf al-ʿamā wa-r-rīn",
    "bayts 388 à 394",
    "bayts 90 à 94",
    # citations (format famille : N espace fine :M)
    "Yūsuf 12"+N+":20", "al-Wāqiʿa 56"+N+":64", "aṣ-Ṣāffāt 37"+N+":2", "al-Muʾminūn 23"+N+":97",
    "al-Kahf 18"+N+":17", "al-Kahf 18"+N+":74", "al-Ḥašr 59"+N+":17", "az-Zumar 39"+N+":34",
    "Yūsuf 12"+N+":74", "Yūsuf 12"+N+":75", "aš-Šūrā 42"+N+":40", "al-Māʾida 5"+N+":33",
    "al-Māʾida 5"+N+":29", "al-Māʾida 5"+N+":95", "Fuṣṣilat 41"+N+":28", "al-Ḥaǧǧ 22"+N+":19",
    "Āl ʿImrān 3"+N+":156", "al-Baqara 2"+N+":2", "an-Naǧm 53"+N+":19", "al-Baqara 2"+N+":197",
    "5"+N+":23",
    # vedettes et squelettes
    "zāhidīna", "zāriʿūna", "zaǧarāt", "hamazāt", "tazāwaru", "zakātan",
    "ǧazāʾū", "ǧazāʾuhu", "ǧazāʾu ẓ-ẓālimīna", "ǧazāʾu l-muḥsinīna", "ǧazāʾu sayyiʾatin",
    "fa-mā ǧazāʾuhu", "wa-ǧazāʾu", "innamā ǧazāʾu", "fa-ǧazāʾun miṯlu", "ǧazāʾu ʾaʿdāʾi",
    "ġuzzan", "hudan", "hāḏāni", "ḫaṣmāni", "raǧulāni", "al-ʿUzzā", "Taqwā",
    "z-h-d-n", "z-r-ʿ-w-n", "z-ǧ-r-t", "h-m-z-t", "t-z-w-r", "ǧ-z-h-h", "ǧ-z-ʾ-alif", "ġ-z-y",
    # doctrine et école
    "ʿUmdat al-bayān", "al-Waḏġīrī", "nāẓim", "šarḥ", "muṣḥaf", "qiyās",
    "ḥaḏf ʾišāra", "pluriel masculin sain", "pluriel féminin sain", "maqṣūr",
    "taḥmarra", "tazwarra", "zakīyatan", "muṯannā", "al-ʾūlayān", "bi-l-hāʾ",
    "al-ʿĀqib", "al-Ǧakanī", "aš-Šinqīṭī",
    "divergence", "sans reconstruction", "septième leçon consécutive",
    "l’ʿAzīz", "Dormants", "Rangés", "Table", "Groupes", "Pèlerinage",
    "alif élidée", "squelette", "hamza-porteuse",
]
miss = 0
for probe in probes:
    ok = probe in full
    if not ok:
        miss += 1
    print(("OK  " if ok else "MANQUE ") + probe.replace('\u202f', '~'))
print(f"=== {len(probes) - miss}/{len(probes)} sondes OK ===")
