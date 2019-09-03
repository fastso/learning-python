a, b, c = map(int, input().split())
mod = 1000000007

a %= mod
b %= mod
c %= mod

print(a * b % mod * c % mod)
