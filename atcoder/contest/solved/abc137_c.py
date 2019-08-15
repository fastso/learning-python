n = int(input())
a = [list(input()) for i in range(n)]

for i in range(n):
    a[i].sort()

a.sort()

ans = 0
same_n = 0
for i in range(1, n):
    if a[i] != a[i - 1]:
        same_n = 0
    else:
        same_n += 1
    ans += same_n

print(ans)
