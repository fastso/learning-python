n = int(input())
a = list(map(int, input().split()))

x = sum(a) - sum(a[1::2]) * 2
print(x, end=' ')
for i in range(0, n-1):
    x = 2 * a[i] - x
    print(x, end=' ')
