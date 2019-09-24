import math

mod = 998244353

n = int(input())
a = list(map(int, input().split()))


def lcm(x, y):
    return (x * y) // math.gcd(x, y) % mod


ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        ans += lcm(a[i], a[j])
print(ans % mod)
