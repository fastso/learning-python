n = int(input())
a = list(map(int, input().split()))
a_b = []
for i in range(n):
    a_b.append([a[i], i + 1])
a_b.sort(key=lambda x: (x[0]))

for i in range(n):
    print(a_b[i][1], end=' ')
