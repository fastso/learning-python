n, x = map(int, input().split())

left = x - 1
right = n - x

if left < right:
    print(left)
else:
    print(right)
