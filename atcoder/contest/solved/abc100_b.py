a, b = map(int, input().split())

if b != 100:
    print(b * 100 ** a)
else:
    print(101 * 100 ** a)
