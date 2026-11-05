import subprocess, sys
# TSV scan to find y of lines containing keywords
for pg, kws in [(137, ["تاجم","تراجم","الاعلام","الصلاح","الشهرزوري"]),
                (138, ["رشي","العيبة","الامعن","الضبي","الحاكم","النبع"]),
                (139, ["الفرائد","اليدين","العقيلي","المك","بن معين","المر"]),
                (140, ["المصادر","المراجع"])]:
    subprocess.run(["TESSDATA_PREFIX=/tmp/tessdata","tesseract",f"tr-tmp/r611/p-{pg}.png",
                    f"tr-tmp/r611/tsv{pg}","-l","ara","--psm","6","tsv"], capture_output=True)
    # tesseract doesn't accept env in list; rerun properly
