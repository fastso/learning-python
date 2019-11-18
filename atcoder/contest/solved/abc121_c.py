n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

a.sort(key=lambda x: (x[0]))

ans = 0
for i in range(n):
    if m >= a[i][1]:
        m -= a[i][1]
        ans += a[i][0] * a[i][1]
    else:
        ans += m * a[i][0]
        break
print(ans)
