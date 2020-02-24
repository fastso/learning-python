"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=jp
"""

n, w = map(int, input().split())
item = [list(map(int, input().split())) for i in range(n)]

# dp[i][j]
dp = [[0 for j in range(w + 1)] for i in range(n + 1)]

# i: i 番目のアイテム
# sum_w: 総容量 sum_w の場合
for i in range(n):
    for sum_w in range(w + 1):
        if sum_w - item[i][1] >= 0:
            # i 番目のアイテムを選ぶ場合
            dp[i + 1][sum_w] = max(dp[i + 1][sum_w], dp[i][sum_w - item[i][1]] + item[i][0])
        # i 番目のアイテムを選ばない場合
        dp[i + 1][sum_w] = max((dp[i + 1][sum_w], dp[i][sum_w]))
print(dp[n][w])
