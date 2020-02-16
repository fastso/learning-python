n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = list()
for i in range(n - 1):
    for j in range(i + 1, n):
        ans.append(a[i] * a[j])
ans.sort()

print(ans[k - 1])
