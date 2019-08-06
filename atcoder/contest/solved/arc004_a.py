import math

n = int(input())
p = [list(map(int, input().split())) for i in range(n)]

ans = 0
for i in range(n - 1):
    for j in range(i, n):
        ans = max(ans, math.sqrt((p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2))
print(ans)
