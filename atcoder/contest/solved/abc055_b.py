n = int(input())

mod = 1000000007
ans = 1
for i in range(1, n + 1):
    ans *= i
    ans %= mod
print(ans)
