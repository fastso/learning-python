n = int(input())

dp = [[0 for i in range(3)] for j in range(n)]

dp[0] = list(map(int, input().split()))

for i in range(1, n):
    a, b, c = map(int, input().split())
    dp[i][0] = max(a + dp[i - 1][1], a + dp[i - 1][2])
    dp[i][1] = max(b + dp[i - 1][0], b + dp[i - 1][2])
    dp[i][2] = max(c + dp[i - 1][0], c + dp[i - 1][1])
print(max(dp[-1]))
