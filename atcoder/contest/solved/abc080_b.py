n = list(input())

s = 0
for i in n:
    s += int(i)

if int(''.join(n)) % s == 0:
    print('Yes')
else:
    print('No')
