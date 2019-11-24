a, b, x = map(int, input().split())

left = 0
right = x

while left < right:
    mid = (left + right) // 2
    tmp1 = a * mid + b * len(str(mid))
    tmp2 = a * (mid + 1) + b * len(str(mid + 1))
    if tmp1 <= x < tmp2:
        if mid <= 1000000000:
            print(mid)
        else:
            print(1000000000)
        exit()
    elif tmp1 <= x:
        left = mid + 1
    elif tmp1 > x:
        right = mid
print(0)
