n = int(input())
a = list(map(int, input().split()))

if sum(a) % n != 0:
    print(-1)
    exit()
b = sum(a) / n

temp = 0
ans = 0
for i in range(n):
    temp += a[i] - b
    if temp != 0:
        ans += 1
print(ans)
