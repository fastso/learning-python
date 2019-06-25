n = int(input())
k = 0
for i in range(1, n + 1):
    k += i
k = k * 10000 / n
print(k)
