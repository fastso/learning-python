import math

a, b, x = map(int, input().split())

b_1 = x / (a ** 2)
area_1 = a * b_1
area_2 = (a * b) / 2

if b_1 == b:
    ans = 90
elif area_2 > area_1:
    # 三角形
    h = (a * b_1 * 2) / b
    ans = math.degrees(math.atan(h / b))
else:
    # 梯形
    upside_len = b_1 * 2 - b
    ans = math.degrees(math.atan(a / (b - upside_len)))

print(90 - ans)
