import fractions


def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


n = int(input())
a = list(map(int, input().split()))
mod = 1000000007

lcm_pre = lcm(a[0], a[1])
lcm_current = lcm_pre
ans = lcm_current // a[0]
ans += lcm_current // a[1]

if n == 1:
    print(a[0] % mod)
    exit()
elif n == 2:
    print(ans % mod)
    exit()

for i in range(2, n):
    lcm_current = lcm(lcm_pre, a[i])
    if lcm_current != lcm_pre:
        ans *= lcm_current // lcm_pre
        lcm_pre = lcm_current
    ans += lcm_current // a[i]
    ans %= mod
print(ans % mod)
