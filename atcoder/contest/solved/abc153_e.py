h, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
a = [_[0] for _ in ab]

inf = float('inf')
dp = [inf] * (h + max(a) + 1)

for i in range(1, len(dp)):
    for x, y in ab:
        if i - x > 0:
            dp[i] = min(dp[i], dp[i - x] + y)
        else:
            dp[i] = min(dp[i], y)

print(dp[h])
