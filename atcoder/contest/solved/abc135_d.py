s = input()

mod = 1000000007
n = 13

dp = [0] * 13
dp[0] = 1

mul = 1
for i in reversed(range(len(s))):
    nextDp = [0] * 13
    if s[i] == '?':
        for k in range(10):
            for j in range(n):
                nextDp[(k * mul + j) % n] += dp[j]
        for j in range(n):
            nextDp[j] %= mod
    else:
        k = int(s[i])
        for j in range(n):
            nextDp[(k * mul + j) % n] = dp[j]

    mul *= 10
    mul %= n
    dp = nextDp
print(dp[5])
