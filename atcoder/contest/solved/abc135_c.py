n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(1, n + 1):
    if b[i - 1] < a[i - 1]:
        ans += b[i - 1]
    else:
        ans += a[i - 1]
        b[i - 1] -= a[i - 1]
        if b[i - 1] > a[i]:
            ans += a[i]
            a[i] = 0
        else:
            ans += b[i - 1]
            a[i] -= b[i - 1]
print(ans)
