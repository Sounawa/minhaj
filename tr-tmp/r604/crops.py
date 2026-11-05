import subprocess, sys
PDF='content/textbooks-src/ulum-hadith-1-thanawi.pdf'
# (page, y300, h300, tag)  full width
CROPS=[
 (129, 0,    700, 'banner'),
 (129, 1150, 850, 'tahmid'),
 (129, 1900, 800, 'matn'),
 (129, 2550, 800, 'sharh1'),
 (130, 0,    1000,'estikhraj'),
 (130, 1950, 700, 'sakhawi'),
 (130, 2550, 600, 'hadith'),
 (131, 300,  750, 'juybar'),
 (131, 1300, 500, 'hukm'),
 (131, 2100, 550, 'ibnulmulqin'),
 (131, 2550, 600, 'dihlawi'),
 (132, 950,  400, 'ibnHajar'),
 (132, 1400, 600, 'istithmar'),
 (132, 1950, 1150,'taammul'),
]
R=1800
for page,y300,h300,tag in CROPS:
    k=R//300
    y=y300*k; h=h300*k; x=0; w=2550*k
    out=f'tr-tmp/r604/c{page}-{tag}'
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r',str(R),
                    '-x',str(x),'-y',str(y),'-W',str(w),'-H',str(h),'-png',PDF,out],check=True)
    src=out+f'-{page}.png'
    subprocess.run(['tesseract',src,out,'--tessdata-dir','scripts-translate/tessdata','-l','ara','--psm','6'],
                   stderr=subprocess.DEVNULL,check=False)
    print('==',tag,f'p{page}','y300=',y300)
    print(open(out+'.txt').read())
