n, w = map(int, input().split())
item = [list(map(int, input().split())) for i in range(n)]

dp = [[0 for i in range(w + 1)] for j in range(n + 1)]

for i in range(n):
    for sum_w in range(w + 1):
        if sum_w - item[i][0] >= 0:
            dp[i + 1][sum_w] = max(dp[i + 1][sum_w], dp[i][sum_w - item[i][0]] + item[i][1])
        dp[i + 1][sum_w] = max((dp[i + 1][sum_w], dp[i][sum_w]))
print(dp[n][w])
