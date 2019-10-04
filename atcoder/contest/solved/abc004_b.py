a = [list(input()) for i in range(4)]
b = []

for i in range(4):
    c = []
    for j in range(7):
        c.append(a[3 - i][6 - j])
    b.append(c)

for i in range(4):
    print(''.join(b[i]))
