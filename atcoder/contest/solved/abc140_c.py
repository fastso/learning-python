n = int(input())
b = list(map(int, input().split()))

a = [0] * n
a[0] = b[0]
for i in range(1, n - 1):
    a[i] = min(b[i - 1], b[i])
ans = 0
for i in range(n):
    ans += a[i]
print(ans + b[-1])
