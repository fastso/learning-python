n, t = map(int, input().split())

foods = [list(map(int, input().split())) for i in range(n)]
foods.sort(key=lambda x: (x[0]))
times = [x[0] for x in foods]

dp = [[0 for i in range(t + max(times) + 1)] for j in range(n + 1)]

# i: i 番目のfood
# sum_t: 総時間
for i in range(n):
    for sum_t in range(t + max(times)):
        if sum_t - foods[i][0] >= 0:
            # i 番目のアイテムを選ぶ場合
            dp[i + 1][sum_t] = max(dp[i + 1][sum_t], dp[i][sum_t - foods[i][0]] + foods[i][1])
        # i 番目のアイテムを選ばない場合
        dp[i + 1][sum_t] = max((dp[i + 1][sum_t], dp[i][sum_t]))

print(dp[n][t + max(times) - 9])
