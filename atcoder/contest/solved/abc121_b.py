n, m, c = map(int, input().split())
b = list(map(int, input().split()))

ans = 0
for i in range(n):
    b1 = list(map(int, input().split()))
    asum = c
    for j in range(m):
        asum += b[j] * b1[j]
    if asum > 0:
        ans += 1

print(ans)
