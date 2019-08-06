n, s = map(int, input().split())

for x in range(n + 1):
    for y in range(n + 1):
        if n-x-y < 0:
            break
        if x * 10000 + y * 5000 + (n - x - y) * 1000 == s:
            print('%d %d %d' % (x, y, n - x - y))
            exit()
print('-1 -1 -1')
