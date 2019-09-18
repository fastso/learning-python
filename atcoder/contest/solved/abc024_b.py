n, t = map(int, input().split())
a = [int(input()) for i in range(n)]

ans = 0
for i in range(n - 1):
    if a[i + 1] - a[i] > t:
        ans += t
    else:
        ans += a[i + 1] - a[i]
ans += t
print(ans)
