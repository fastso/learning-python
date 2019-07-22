n, t = map(int, input().split())

ans = 1001
for i in range(n):
    a, b = map(int, input().split())
    if b <= t:
        ans = min(ans, a)

if ans == 1001:
    print('TLE')
else:
    print(ans)
