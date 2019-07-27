n = int(input())
a1 = list(map(int, input().split()))

a2 = a1[:]
a2.sort()

diff = 0
for i in range(n):
    if a1[i] != a2[i]:
        diff += 1
print('YES' if diff == 0 or diff == 2 else 'NO')
