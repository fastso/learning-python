a = list(map(int, input().split()))

i5 = 0
i7 = 0

for i in a:
    if i == 5:
        i5 += 1
    if i == 7:
        i7 += 1
if i5==2 and i7==1:
    print('YES')
else:
    print('NO')
