n = int(input())
a = list(input())

ans = 1
temp = a[0]
for i in range(1, n):
    if a[i] != temp:
        ans += 1
        temp = a[i]
print(ans)
