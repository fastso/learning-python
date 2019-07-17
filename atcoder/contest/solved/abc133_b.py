import math

n, d = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        sum_value = 0
        for k in range(d):
            sum_value += (arr[i][k] - arr[j][k]) ** 2
        if math.sqrt(sum_value).is_integer():
            ans += 1

print(ans)
