import math

n = int(input())
a = [int(input()) for i in range(n)]

a.sort(reverse=True)

ans = 0
change = 1
for i in range(n):
    ans += a[i] ** 2 * change
    change *= -1
print(ans * math.pi)
