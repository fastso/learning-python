n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

pre = a[0] - 1
ans = 0
for i in range(n):
    if a[i] - 1 - pre == 1:
        ans += c[a[i] - 1 - 1]
    ans += b[a[i] - 1]
    pre = a[i] - 1
print(ans)
