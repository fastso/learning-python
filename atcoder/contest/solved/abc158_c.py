import math
a, b = map(int, input().split())

max_value = 1250

for i in range(1, max_value + 1):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
        print(i)
        exit()

print(-1)
