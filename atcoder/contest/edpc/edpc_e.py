n, w = map(int, input().split())
item = [list(map(int, input().split())) for i in range(n)]

max_v = 100005

dp = [[float('inf')] * max_v for j in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for sum_v in range(max_v):
        if sum_v - item[i][1] >= 0:
            dp[i + 1][sum_v] = min(dp[i + 1][sum_v], dp[i][sum_v - item[i][1]] + item[i][0])
        dp[i + 1][sum_v] = min((dp[i + 1][sum_v], dp[i][sum_v]))

for sum_v in reversed(range(max_v)):
    if dp[-1][sum_v] <= w:
        print(sum_v)
        break
