import json

q = json.load(open('/home/z/my-project/scripts-translate/quran-cache.json'))

print('=== الخلطاء / خلطاء ===')
for sura, sdata in q.items():
    ar = sdata.get('ar', [])
    for i, text in enumerate(ar, 1):
        if 'الخلطاء' in text or 'خلطاؤ' in text:
            print(f'[{sura}:{i}] {text[:150]}')

print()
print('=== sh-r-k root in MUSA-story suras ===')
musa_suras = ['7', '10', '11', '14', '17', '18', '20', '23', '25', '26', '27', '28', '29', '33', '40', '42', '43', '44', '46', '51', '54', '73', '79']
for sura, sdata in q.items():
    if sura not in musa_suras:
        continue
    ar = sdata.get('ar', [])
    for i, text in enumerate(ar, 1):
        if any(w in text for w in ['شِرْك', 'شرك', 'اشترك', 'شريك', 'شارك', 'استشر']):
            print(f'[{sura}:{i}] {text[:160]}')

print()
print('=== الخلطة / خلتا ===')
for sura, sdata in q.items():
    ar = sdata.get('ar', [])
    for i, text in enumerate(ar, 1):
        if 'الخلطة' in text or 'خَلْطَة' in text:
            print(f'[{sura}:{i}] {text[:150]}')
