n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        ans = max(ans, abs(a[i] - a[j]))

print(ans)
