n, g = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

ans = float('inf')
for i in range(2 ** n):
    g_sum = 0
    count = 0
    rest_max = -1
    for j in range(n):
        if (i >> j) & 1:
            g_sum += 100 * (j + 1) * a[j][0] + a[j][1]
            count += a[j][0]
        else:
            rest_max = j

    if g_sum < g:
        s1 = 100 * (rest_max + 1)
        need = (g - g_sum + s1 - 1) // s1
        if need >= a[rest_max][0]:
            continue
        count += need
    ans = min(ans, count)

print(ans)
