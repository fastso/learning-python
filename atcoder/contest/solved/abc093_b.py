a, b, k = map(int, input().split())

if k * 2 > (b - a):
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, a + k):
        print(i)
    for i in range(b - k + 1, b + 1):
        print(i)
