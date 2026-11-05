import subprocess
PDF='content/textbooks-src/ulum-hadith-1-thanawi.pdf'
CROPS=[
 (129, 0,    330, 'title'),
 (129, 380,  330, 'obj3'),
 (129, 2050, 350, 'v1'),   # hemistich line 1 of matn (y300)
 (129, 2280, 260, 'v2'),
 (129, 2620, 220, 'gloss1'),
 (129, 2740, 240, 'gloss2'),
 (129, 1330, 320, 'tahmid2'),
 (130, 330,  260, 'def1'),   # عرفه الناظم بقوله quote
 (130, 580,  480, 'def2'),   # بقيد الانفراد/التهمة
 (130, 2080, 200, 'sakhawi2'), # جزماء line
 (130, 2650, 420, 'hadith2'),  # hadith lines 2-3
 (131, 480,  180, 'afraz'),  # لم يفرده line
 (131, 740,  120, 'suyuti_v1'),
 (131, 850,  120, 'suyuti_v2'),
 (131, 1320, 180, 'hukm1'),  # لا يقبل في الشواهد
 (131, 2110, 240, 'mulqin_q'), # ابن الملقن quote
 (131, 2620, 200, 'muslim_intro'), # استند رحمه الله
 (132, 900,  320, 'ibn_hajar'),
 (132, 1240, 220, 'v_est1'),
 (132, 1400, 220, 'v_est2'),
 (132, 2820, 380, 'idad'),
]
for page,y300,h300,tag in CROPS:
    R=3600; k=R//300
    out=f'tr-tmp/r604/m{page}-{tag}'
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r',str(R),
                    '-x','0','-y',str(y300*k),'-W',str(2550*k),'-H',str(h300*k),'-png',PDF,out],check=True)
    subprocess.run(['tesseract',out+f'-{page}.png',out,'--tessdata-dir','scripts-translate/tessdata','-l','ara','--psm','6'],
                   stderr=subprocess.DEVNULL,check=False)
    print('==',tag,f'p{page} y300={y300}')
    print(open(out+'.txt').read().strip())
