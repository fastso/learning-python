a, b, c = map(int, input().split())

x = c
for i in range(10):
    x = a * x - b
    print(x)
