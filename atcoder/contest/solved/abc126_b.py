s = input()

a = int(s[:2])
b = int(s[2:])

if 0 < a <= 12 and 0 < b <= 12:
    print('AMBIGUOUS')
elif 0 < a <= 12:
    print('MMYY')
elif 0 < b <= 12:
    print('YYMM')
else:
    print('NA')
