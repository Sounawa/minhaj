#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minhāj — Fix systémique des h1 d'intros (R54).
(a) 20 intros savantes : h1 « Présentation du manuel » (doublon du titre lecteur)
    → remplacé par la traduction main de la ligne-matière AR du source.
(b) 4 intros dont le source AR n'a PAS de h1 → suppression du h1 redondant.
(c) 18 intros GT : h1 GT erroné (« 6 août », « Atiq », « Hashiyat Al-Dasouki »…)
    → remplacé par la traduction main de la ligne-matière AR.
"""
import json, os, re, sys

HOME = "/home/z/my-project"
NB = "\u202f"

def fix_text(t: str) -> str:
    t = t.replace("'", "\u2019")
    t = re.sub(r"[ \u00a0\u202f]*([;:!?»])", NB + r"\1", t)
    t = re.sub(r"«[ \u00a0\u202f]*", "«" + NB, t)
    return t

# slug -> nouveau h1 (None = supprimer le h1)
H1 = {
    # (a) doublons savants avec ligne-matière AR
    "faraid-tanawi-3": "Le farāʾiḍ : la manẓūma al-Rasmūkiyya, avec le commentaire Īḍāḥ al-asrār al-maṣūna d’Aḥmad b. Sulaymān al-Jazūlī al-Rasmūkī — 3ᵉ année de l’enseignement secondaire traditionnel",
    "fikr-islami-tanawi-2": "Matière : Pensée islamique (la philosophie islamique) — 2ᵉ année de l’enseignement secondaire traditionnel",
    "fiqh-1ep": "Le fiqh : le Mukhtaṣar d’al-Akhḍarī avec le commentaire d’al-Ābī al-Azharī — 4ᵉ année de l’enseignement primaire traditionnel",
    "fiqh-6ep": "Le fiqh : la manẓūma al-Murshid al-Muʿīn d’Ibn ʿĀshir avec le commentaire de Mayyāra — 6ᵉ année de l’enseignement primaire traditionnel",
    "fiqh-tanawi-2": "Le fiqh : le Mukhtaṣar de Cheikh Khalīl avec le commentaire d’al-Dardīr et la glose (ḥāšiyya) d’al-Dasūqī — 2ᵉ année de l’enseignement secondaire traditionnel",
    "hadith-3es": "Le ḥadīth : les règles du pèlerinage (ḥaǧǧ), de la ʿumra, du sacrifice (uḍḥiya), des égorgements (ḏabāʾiḥ), de la chasse et de la ʿaqīqa, tirées du Muwaṭṭaʾ de l’imam Mālik avec le commentaire d’al-Zarqānī — 3ᵉ année de l’enseignement collégial traditionnel",
    "hadith-tanawi-3": "Le ḥadīth : jugements rendus (aqḍiya) et règles selon la sentence et la pratique des gens de Médine, tirés du Muwaṭṭaʾ de l’imam Mālik avec le commentaire d’al-Zarqānī — 3ᵉ année de l’enseignement secondaire traditionnel",
    "qiraat-tanawi-2": "Les qirāʾāt : le matn Ḥirz al-amānī wa-wajh al-tahānī d’Abū l-Qāsim al-Shāṭibī — 2ᵉ année de l’enseignement secondaire traditionnel",
    "rasm-wa-dabt-6ep": "Le rasm et le ḍabṭ [graphie et vocalisation du Coran] : l’arǧūza ʿUmdat al-bayān d’Idrīs al-Wadghīrī avec le commentaire Bahjat al-naẓar wa-l-ʿiyān de Muḥammad b. al-ʿArabī al-Massarī — 6ᵉ année de l’enseignement primaire traditionnel",
    "tafsir-6ep": "Le tafsīr : à travers le Tafsīr al-Jalālayn — 6ᵉ année de l’enseignement primaire traditionnel",
    "tafsir-tanawi-3": "Le tafsīr : l’exégèse de la sourate al-Kahf à travers al-Muḥarrar al-wajīz fī tafsīr al-kitāb al-ʿazīz d’Ibn ʿAṭiyya — 3ᵉ année de l’enseignement secondaire traditionnel",
    "tajwid-5ep": "Le tajwīd : applications sur le poème Tuḥfat al-aṭfāl d’al-Jamzūrī — 5ᵉ année de l’enseignement primaire traditionnel",
    "taqtit-tanawi-2": "Le tawqīt : la manẓūma ʿUmdat ahl al-thabt fī ʿilm al-awqāt wa-samt al-bayt, avec le commentaire Ḥall al-ʿuqda ʿan maqāṣid al-ʿumda de Muḥammad al-ʿAlamī — 2ᵉ année de l’enseignement secondaire traditionnel",
    "ulum-hadith-tanawi-1": "Les sciences du ḥadīth : la Manẓūma al-Bayqūniyya avec le commentaire d’al-Zarqānī — 1ʳᵉ année de l’enseignement secondaire traditionnel",
    "ulum-hadith-tanawi-2": "Les sciences du ḥadīth : le matn Nukhbat al-fikar avec le commentaire Nuzhat al-naẓar d’Ibn Ḥaǧar al-ʿAsqalānī — 2ᵉ année de l’enseignement secondaire traditionnel",
    "ulum-hadith-tanawi-3": "Les sciences du ḥadīth : le matn Nukhbat al-fikar avec le commentaire Nuzhat al-naẓar du ḥāfiẓ Ibn Ḥaǧar al-ʿAsqalānī — 3ᵉ année de l’enseignement secondaire traditionnel",
    "usul-fiqh-tanawi-2": "Les uṣūl al-fiqh : la manẓūma Marṭaqī al-wuṣūl ilā l-ḍarūrī min al-uṣūl d’Ibn ʿĀṣim al-Gharnāṭī al-Andalusī al-Mālikī — 2ᵉ année de l’enseignement secondaire traditionnel",
    "usul-qiyam-4ep": "Les fondements des valeurs dans le Coran et la Sunna — 4ᵉ année de l’enseignement primaire traditionnel",
    "usul-qiyam-5ep": "Les fondements des valeurs dans le Coran et la Sunna — 5ᵉ année de l’enseignement primaire traditionnel",
    "usul-qiyam-6ep": "Les fondements des valeurs dans le Coran et la Sunna — 6ᵉ année de l’enseignement primaire traditionnel",
    # (b) doublons sans ligne-matière AR → suppression
    "fiqh-5ep": None,
    "hadith-2es": None,
    "hadith-5ep": None,
    "tafsir-1ep": None,
    # (c) h1 GT erronés → traduction main de la ligne-matière AR
    "fikr-islami-tanawi-1": "La pensée islamique : des questions de théologie (kalām) — 1ʳᵉ année de l’enseignement secondaire traditionnel",
    "fiqh-3es": "Le fiqh : le matn al-Risāla d’Ibn Abī Zayd al-Qayrawānī avec le commentaire Kifāyat al-ṭālib al-rabbānī d’Abū l-Ḥasan et la glose (ḥāšiyya) d’al-ʿAdawī — 3ᵉ année de l’enseignement collégial traditionnel",
    "fiqh-tanawi-1": "Le fiqh : le matn du Mukhtaṣar de Cheikh Khalīl avec le commentaire d’al-Dardīr et la glose (ḥāšiyya) d’al-Dasūqī — 1ʳᵉ année de l’enseignement secondaire traditionnel",
    "fiqh-tanawi-3": "Le fiqh : le Mukhtaṣar de Cheikh Khalīl avec le commentaire d’al-Dardīr et la glose (ḥāšiyya) d’al-Dasūqī — 3ᵉ année de l’enseignement secondaire traditionnel",
    "hadith-6ep": "Le ḥadīth : les Quarante hadiths (al-Arbaʿūn al-nawawiyya) avec le commentaire d’Ibn Daqīq al-ʿĪd — 6ᵉ année de l’enseignement primaire traditionnel",
    "hadith-tanawi-1": "Le ḥadīth : le Muwaṭṭaʾ de l’imam Mālik avec le commentaire d’al-Zarqānī — 1ʳᵉ année de l’enseignement secondaire traditionnel",
    "qiraat-tanawi-1": "Les qirāʾāt : le matn Ḥirz al-amānī wa-wajh al-tahānī d’Abū l-Qāsim al-Shāṭibī avec le commentaire Sirāǧ al-qāriʾ al-mubtadī wa-tadhkār al-muqrīʾ al-muntahī d’Ibn al-Qāṣiḥ — 1ʳᵉ année de l’enseignement secondaire traditionnel",
    "qiraat-tanawi-3": "Les qirāʾāt : le matn Ḥirz al-amānī wa-wajh al-tahānī d’Abū l-Qāsim al-Shāṭibī — 3ᵉ année de l’enseignement secondaire traditionnel",
    "rasm-wa-dabt-5ep": "Le rasm et le ḍabṭ [graphie et vocalisation du Coran] : l’arǧūza ʿUmdat al-bayān d’Idrīs al-Wadghīrī avec le commentaire Bahjat al-naẓar wa-l-ʿiyān de Muḥammad b. al-ʿArabī al-Massarī — 5ᵉ année de l’enseignement primaire traditionnel",
    "sira-1es": "La sīra nabawiyya [biographie prophétique] — 1ʳᵉ année de l’enseignement collégial traditionnel",
    "sira-2es": "La sīra nabawiyya [biographie prophétique] — 2ᵉ année de l’enseignement collégial traditionnel",
    "sira-3es": "La sīra nabawiyya [biographie prophétique] : la période médinoise après l’hégire du Prophète — 3ᵉ année de l’enseignement collégial traditionnel",
    "tafsir-2es": "Le tafsīr : l’exégèse des sourates Fāṭir, al-Ḥadīd et al-Muǧādala à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Ǧuzay — 2ᵉ année de l’enseignement collégial traditionnel",
    "tafsir-3es": "Le tafsīr : l’exégèse des sourates al-Shūrā, al-Ṭalāq et al-Taḥrīm à travers le Tashīl li-ʿulūm al-tanzīl d’Ibn Ǧuzay — 3ᵉ année de l’enseignement collégial traditionnel",
    "tajwid-2es": "Le tajwīd : le poème al-Durar al-lawāmiʿ d’Ibn Barī avec le commentaire al-Nuǧūm al-ṭawāliʿ d’Ibrāhīm al-Mārġanī — 2ᵉ année de l’enseignement collégial traditionnel",
    "tajwid-3es": "Le tajwīd : le poème al-Durar al-lawāmiʿ d’Ibn Barī avec le commentaire al-Nuǧūm al-ṭawāliʿ d’Ibrāhīm al-Mārġanī — 3ᵉ année de l’enseignement collégial traditionnel",
    "taqtit-tanawi-3": "Le tawqīt : la manẓūma al-Ǧāmiʿ al-mufīd fī ḥisāb al-khusūf wa-l-kusūf wa-ruʾyat al-ahilla de Muḥammad b. Muḥammad al-ʿAlamī — 3ᵉ année de l’enseignement secondaire traditionnel",
    "usul-fiqh-waraqat": "Les uṣūl al-fiqh : les Waraqāt [« Les feuillets »] de l’imam des deux nobles sanctuaires [al-Juwaynī] avec le commentaire d’al-Ḥaṭṭāb — 3ᵉ année de l’enseignement collégial traditionnel",
}

def main() -> None:
    changed = 0
    for slug, new_h1 in H1.items():
        path = f"{HOME}/content/books/{slug}.json"
        with open(path, "r", encoding="utf-8") as fh:
            book = json.load(fh)
        hfr = book.get("intro", {}).get("htmlFr") or ""
        if not hfr:
            print(f"⚠︎ {slug}: pas d’htmlFr, ignoré")
            continue
        m = re.match(r"\s*<h1[^>]*>.*?</h1>", hfr, re.S)
        if not m:
            print(f"⚠︎ {slug}: aucun h1 initial trouvé, ignoré")
            continue
        if new_h1 is None:
            new_html = hfr[m.end():].lstrip("\n")
        else:
            new_html = "<h1>" + fix_text(new_h1) + "</h1>" + hfr[m.end():]
        if new_html == hfr:
            print(f"= {slug}: inchangé")
            continue
        book["intro"]["htmlFr"] = new_html
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(book, fh, ensure_ascii=False, indent=2)
        os.replace(tmp, path)
        changed += 1
        tag = "SUPPR h1" if new_h1 is None else "h1 → " + fix_text(new_h1)[:58] + "…"
        print(f"✓ {slug}: {tag}")
    print(f"\n{changed}/{len(H1)} livres modifiés")

if __name__ == "__main__":
    main()
