"""
0-1ナップサック問題
容量 w のナップサックが一つと、n 種類のアイテム（各々、容積と価値）が与えられたとき、
ナップサックの容量 w を超えない範囲でいくつかの品物をナップサックに詰め、
ナップサックに入れた品物の価値の和を最大化するにはどの品物を選べばよいか。

n: アイテムの種類
w: ナップサックの容量
item: [0]-容積　[1]-価値

Input Sample:
6 15
2 3
1 2
3 6
2 1
1 3
5 85

Output Sample:
100

References:
https://qiita.com/drken/items/dc53c683d6de8aeacf5a#d-%E5%95%8F%E9%A1%8C---knapsack-1
"""

n, w = map(int, input().split())
item = [list(map(int, input().split())) for i in range(n)]

dp = [[0 for i in range(w + 1)] for j in range(n + 1)]

# i: i 番目のアイテム
# sum_w: 総容量 sum_w の場合
for i in range(n):
    for sum_w in range(w + 1):
        if sum_w - item[i][0] >= 0:
            # i 番目のアイテムを選ぶ場合
            dp[i + 1][sum_w] = max(dp[i + 1][sum_w], dp[i][sum_w - item[i][0]] + item[i][1])
        # i 番目のアイテムを選ばない場合
        dp[i + 1][sum_w] = max((dp[i + 1][sum_w], dp[i][sum_w]))
print(dp[n][w])
