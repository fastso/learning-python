n = int(input())
k = int(input())

a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i] - 0 > k - a[i]:
        ans += k - a[i]
    else:
        ans += a[i] - 0
print(ans * 2)
