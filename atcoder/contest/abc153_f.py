import math

n, d, a = map(int, input().split())
xh = [list(map(int, input().split())) for _ in range(n)]

xh.sort(key=lambda x: (x[0]))

ans = 0
for i in range(n):
    count = math.ceil(xh[i][1] / a)
    if not count:
        continue

    ans += count
    for j in range(i + 1, n):
        if xh[j][0] > xh[i][0] + 2 * d:
            break
        else:
            if xh[j][1] - count * a > 0:
                xh[j][1] -= count * a
            else:
                xh[j][1] = 0
print(ans)