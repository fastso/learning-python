n = int(input())

# dp[l][r]
dp = [[0] * n for _ in range(n)]

# size : [2, n]
for size in range(2, n + 1):
    # left : [0, n)
    for l in range(n):
        r = l + size
        if r > n:
            break
        # do something
        for mid in range(l, r):
            # Example :
            dp[l][r] = max(dp[l][r], dp[l][mid] + dp[mid][r])
