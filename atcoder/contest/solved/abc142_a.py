n = int(input())

if n == 1:
    print(1.0000000000)
elif n % 2 == 0:
    print(0.5000000000)
else:
    print((n // 2 + 1) / n)
