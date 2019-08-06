n = int(input())
t = [int(input()) for i in range(n)]

ans = float('inf')
for i in range(2 ** n):
    a = 0
    b = 0
    for j in range(n):
        if (i >> j) & 1:
            a += t[j]
        else:
            b += t[j]
    ans = min(ans, max(a, b))
print(ans)
