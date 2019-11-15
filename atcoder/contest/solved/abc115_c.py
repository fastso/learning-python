n, k = map(int, input().split())
a = [int(input()) for i in range(n)]
a.sort()

ans = float('inf')
for i in range(n - k + 1):
    ans = min(ans, a[i + k - 1] - a[i])
print(ans)
