import itertools

n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(2, n):
    l = itertools.combinations(p, i)
    for j in l:
        sorted(j)
        ans += j[-2]
print(ans)
