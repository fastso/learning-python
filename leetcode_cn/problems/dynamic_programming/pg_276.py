class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0
        elif n == 1:
            return k
        elif n == 2:
            return k ** 2
        else:
            dp = [0] * n
            dp[0] = k
            dp[1] = k ** 2

            for i in range(2, n):
                dp[i] = dp[i - 2] * (k - 1) + dp[i - 1] * (k - 1)
            return dp[-1]
