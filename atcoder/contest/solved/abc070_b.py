a, b, c, d = map(int, input().split())

if b <= c or d <= a:
    print(0)
elif a >= c and b <= d:
    print(b - a)
elif a <= c and b >= d:
    print(d - c)
elif a >= c and b >= d:
    print(d - a)
elif a <= c and b <= d:
    print(b - c)
