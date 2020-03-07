n, a, b = map(int, input().split())

temp = n // (a + b)
amari = n % (a + b)

if amari > a:
    print((temp + 1) * a)
else:
    print(temp * a + amari)
