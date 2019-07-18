n = int(input())
a = list(map(int, input().split()))

left = 0
right = sum(a)

ans = 10000
for i in range(1, n):
    left += a[i - 1]
    right -= a[i - 1]
    if abs(left - right) < ans:
        ans = abs(left - right)
    else:
        break

print(ans)
