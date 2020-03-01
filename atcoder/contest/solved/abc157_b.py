a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))

n = int(input())
b = [int(input()) for _ in range(n)]

for i in b:
    for j in range(3):
        if a1[j] == i:
            a1[j] = 0
        if a2[j] == i:
            a2[j] = 0
        if a3[j] == i:
            a3[j] = 0

for i in range(3):
    if a1[i] == a2[i] == a3[i] == 0:
        print('Yes')
        exit()

if a1[0] == a1[1] == a1[2] == 0:
    print('Yes')
    exit()
if a2[0] == a2[1] == a2[2] == 0:
    print('Yes')
    exit()
if a3[0] == a3[1] == a3[2] == 0:
    print('Yes')
    exit()

if a1[0] == a2[1] == a3[2] == 0:
    print('Yes')
    exit()
if a3[0] == a2[1] == a1[2] == 0:
    print('Yes')
    exit()

print('No')