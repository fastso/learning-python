n, k = map(int, input().split())

ans = 0
for i in range(1, n + 1):
    tmp = 1 / n
    now = i
    while now < k:
        now *= 2
        tmp /= 2
    ans += tmp
print(ans)
