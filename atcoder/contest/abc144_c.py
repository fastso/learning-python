import math


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n = int(input())
a = prime_factorize(n)

sq = math.sqrt(n)

if len(a) == 1:
    print(n - 1)
    exit()

x = 1
y = 1
temp = 0
for i in range(len(a)):
    if x <= sq:
        x *= a[i]
        temp = i
    else:
        y *= a[i]

ans1 = x + y - 2

if i == 0:
    print(ans1)
else:
    ans2 = x / a[i - 1] + y * a[i - 1] - 2
    print(min(ans1, int(ans2)))
