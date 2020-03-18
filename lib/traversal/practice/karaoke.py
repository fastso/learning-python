"""
https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c?lang=ja
"""

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for x in range(m - 1):
    for y in range(x, m):
        temp = 0
        for i in range(n):
            temp += max(a[i][x], a[i][y])
        ans = max(ans, temp)

print(ans)
