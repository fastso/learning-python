a, b = map(int, input().split())

if a % (1 + 2 * b) == 0:
    print(a // (1 + 2 * b))
else:
    print(a // (1 + 2 * b) + 1)
