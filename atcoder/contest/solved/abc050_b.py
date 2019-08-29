n = int(input())
a = list(map(int, input().split()))
m = int(input())

for i in range(m):
    p, x = map(int, input().split())
    b = a[:]
    b[p - 1] = x
    print(sum(b))
