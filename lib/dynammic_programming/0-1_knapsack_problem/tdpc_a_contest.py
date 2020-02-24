"""
https://atcoder.jp/contests/tdpc/tasks/tdpc_contest

References:
https://webbibouroku.com/Blog/Article/typical-dp-contest-a
"""

n = int(input())
p = list(map(int, input().split()))

# n <= 100 and p <= 100
max_p_sum = 10001

# dp[i][j]
dp = [[0 for j in range(max_p_sum + 1)] for i in range(n + 1)]
dp[0][0] = 1

# i: i 番目のアイテム
# sum_p: 点数合計 sum_p の場合
for i in range(n):
    for sum_p in range(max_p_sum + 1):
        if sum_p - p[i] >= 0:
            if dp[i][sum_p - p[i]]:
                dp[i + 1][sum_p] = 1
        if dp[i][sum_p]:
            dp[i + 1][sum_p] = 1
print(sum(dp[n]))
